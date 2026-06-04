#!/usr/bin/env python3
"""
Threads Scheduled Poster

pending.md から該当時間帯のストックを取り出して Threads に投稿し、
posted.md に移動する。GitHub Actions / ローカル両対応。

対応する投稿タイプ:
  - 単発: テキスト1本
  - コメント仕込み: メイン投稿 → reply_to_id でコメントを連投
  - 画像付き: 画像を公開URL(raw.githubusercontent)で添付
    - REQUIRE_IMAGE=1 の場合、画像を添付できなければ投稿せず失敗する

認証情報の取得順:
  1. 環境変数（THREADS_ACCESS_TOKEN / THREADS_USER_ID）→ GitHub Actions 用
  2. ~/.config/threads-workflow/threads-credentials.json → ローカル用

Usage:
    python3 threads_poster.py [--dry-run] [--skip-jitter]

Threads API:
    https://graph.threads.net/v1.0/{user-id}/threads (コンテナ作成)
    https://graph.threads.net/v1.0/{user-id}/threads_publish (公開)
"""

import argparse
import json
import os
import random
import re
import shlex
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests


# === パス定義 ===
# GitHub Actions / ローカル / Codex worktree のどこで実行しても、このスクリプトが
# 置かれているリポジトリを正とする。
REPO_DIR = Path(__file__).resolve().parent.parent

PENDING = REPO_DIR / "storage" / "stocks" / "pending.md"
POSTED = REPO_DIR / "storage" / "stocks" / "posted.md"
CREDS = Path.home() / ".config" / "threads-workflow" / "threads-credentials.json"
ENV_FILE = Path.home() / ".config" / "sns-auto-post" / "env"
LOG_DIR = REPO_DIR / "storage" / "analytics"
LOG = LOG_DIR / "scheduler.log"
# 日×枠ごとの投稿済みマーカー（冗長クロンの二重投稿を防ぐ冪等ガード用）
STATE = LOG_DIR / "post-state.json"

JST = timezone(timedelta(hours=9))
THREADS_TEXT_LIMIT = 500

# 画像を公開URLで渡すための raw ベース（main ブランチにコミット済み画像を参照）
RAW_BASE = "https://raw.githubusercontent.com/atelierbase/threads-workflow-atelier/main/"


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = f"{datetime.now(JST).isoformat()} [threads] {msg}"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


def _today() -> str:
    return datetime.now(JST).strftime("%Y-%m-%d")


def load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def already_posted(slot: str) -> bool:
    """この日×この枠が既に投稿済みなら True（冗長クロンの二重投稿を防ぐ）。"""
    return slot in load_state().get(_today(), [])


def mark_posted(slot: str) -> None:
    """この日×この枠を投稿済みとして記録。直近14日分のみ保持。"""
    st = load_state()
    st.setdefault(_today(), [])
    if slot not in st[_today()]:
        st[_today()].append(slot)
    for k in sorted(st.keys())[:-14]:
        del st[k]
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")


def is_transient(e: Exception) -> bool:
    """一過性（リトライする価値あり）のエラーか。429/5xx を含む。"""
    status = getattr(getattr(e, "response", None), "status_code", None)
    return status in (429, 500, 502, 503, 504)


def post_main_with_retry(make_call, attempts: int = 3):
    """メイン投稿を一過性エラーに対して指数バックオフでリトライする。"""
    for i in range(1, attempts + 1):
        try:
            return make_call()
        except Exception as e:
            log(f"main post attempt {i}/{attempts} failed: {e}")
            if i < attempts and is_transient(e):
                time.sleep(min(60, 10 * i))
                continue
            raise


def load_env_file() -> None:
    """ローカルAutomation用の非公開envファイルを読む。既存の環境変数は上書きしない。"""
    if not ENV_FILE.exists():
        return
    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            parts = shlex.split(line, comments=True, posix=True)
        except ValueError:
            continue
        if parts and parts[0] == "export":
            parts = parts[1:]
        for part in parts:
            if "=" not in part:
                continue
            key, value = part.split("=", 1)
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                os.environ.setdefault(key, value)


def load_credentials() -> dict:
    if os.getenv("THREADS_ACCESS_TOKEN"):
        log("credentials: env vars")
        return {
            "access_token": os.environ["THREADS_ACCESS_TOKEN"],
            "user_id": os.environ["THREADS_USER_ID"],
        }
    log(f"credentials: file {CREDS}")
    with open(CREDS, encoding="utf-8") as f:
        return json.load(f)


def current_slot() -> str:
    hour = datetime.now(JST).hour
    if 6 <= hour < 11:
        return "朝"
    elif 11 <= hour < 15:
        return "昼"
    else:
        return "夜"


def parse_main_and_comments(raw_text: str):
    """文面を「メイン」と「コメント群」に分割。区切りは `--- コメントN ---`。"""
    segments = re.split(r"\n-{2,}\s*コメント\s*\d*\s*-{2,}\s*\n", raw_text)
    main = segments[0].strip()
    comments = [s.strip() for s in segments[1:] if s.strip()]
    return main, comments


def resolve_image_url(target_post: str):
    """画像の公開URLを解決。repo にファイルが存在する時だけURLを返す（未配置はNone）。"""
    m = re.search(r"-\s*画像ファイル:\s*(\S+)", target_post)
    if not m:
        return None
    rel = m.group(1).strip()
    if (REPO_DIR / rel).exists():
        return RAW_BASE + rel
    log(f"画像ファイル指定あり ({rel}) だが未配置")
    return None


def verify_image_url(image_url: str) -> bool:
    """Threads が取得できる公開画像URLかを事前確認する。"""
    try:
        resp = requests.head(image_url, timeout=15, allow_redirects=True)
        if resp.status_code == 405:
            resp = requests.get(image_url, timeout=15, stream=True)
        content_type = resp.headers.get("content-type", "").lower()
        if resp.ok and (not content_type or content_type.startswith("image/")):
            return True
        log(
            f"image URL is not ready: status={resp.status_code} "
            f"content-type={content_type or 'unknown'} url={image_url}"
        )
        return False
    except Exception as e:
        log(f"image URL check failed: {e}")
        return False


def post_to_threads(
    text: str,
    access_token: str,
    user_id: str,
    image_url: str = None,
    reply_to_id: str = None,
) -> str:
    """Threads API で投稿。reply_to_id 指定でセルフリプライ、image_url 指定で画像付き。投稿IDを返す。"""
    base_url = f"https://graph.threads.net/v1.0/{user_id}"

    data = {"access_token": access_token}
    if image_url:
        data["media_type"] = "IMAGE"
        data["image_url"] = image_url
        if text:
            data["text"] = text
    else:
        data["media_type"] = "TEXT"
        data["text"] = text
    if reply_to_id:
        data["reply_to_id"] = reply_to_id

    # Step 1: Media Container 作成
    container_resp = requests.post(f"{base_url}/threads", data=data, timeout=30)
    if not container_resp.ok:
        log(f"Container creation failed: {container_resp.status_code} {container_resp.text}")
        container_resp.raise_for_status()
    container_id = container_resp.json()["id"]
    log(f"container_id={container_id} (image={'yes' if image_url else 'no'}, reply={'yes' if reply_to_id else 'no'})")

    # Meta 推奨: コンテナ処理を待つ（画像はやや長め）
    time.sleep(5 if image_url else 3)

    # Step 2: 公開
    publish_resp = requests.post(
        f"{base_url}/threads_publish",
        data={"creation_id": container_id, "access_token": access_token},
        timeout=30,
    )
    if not publish_resp.ok:
        log(f"Publish failed: {publish_resp.status_code} {publish_resp.text}")
        publish_resp.raise_for_status()
    return publish_resp.json()["id"]


def main(dry_run: bool = False, skip_jitter: bool = False) -> None:
    load_env_file()

    # POST_SLOT（起動cronから決まる固定スロット）があれば優先。
    # 無い時（手動dispatch等）のみ実行時刻から判定する。
    # → GitHub Actions の発火時刻ズレで「夜投稿が朝に出る」のを防ぐ。
    slot = os.getenv("POST_SLOT") or current_slot()
    log(f"START slot={slot} (source={'POST_SLOT' if os.getenv('POST_SLOT') else 'clock'}) dry_run={dry_run} skip_jitter={skip_jitter}")

    # 冪等ガード: 同じ日×同じ枠が既に投稿済みなら何もしない。
    # → 冗長クロン（各枠を複数回発火させてドロップ対策）でも二重投稿しない。
    if not dry_run and already_posted(slot):
        log(f"SKIP slot={slot} は本日すでに投稿済み（冗長クロンの重複起動）")
        sys.exit(0)

    # ジッター
    if not dry_run and not skip_jitter and not os.getenv("SKIP_JITTER"):
        jitter = random.randint(0, 15 * 60)
        log(f"jitter={jitter}s")
        time.sleep(jitter)

    # 認証情報
    try:
        creds = load_credentials()
    except Exception as e:
        log(f"FAILED to load credentials: {e}")
        sys.exit(1)

    if not PENDING.exists():
        log(f"pending.md がありません: {PENDING}")
        sys.exit(0)

    with open(PENDING, encoding="utf-8") as f:
        content = f.read()

    parts = re.split(r"\n(?=## \d{4}-\d{2}-\d{2}-\d{3})", content)
    if len(parts) < 2:
        log("No pending posts.")
        sys.exit(0)

    header = parts[0]
    posts = parts[1:]

    # 該当時間帯のストックを探す
    target_idx = None
    for i, post in enumerate(posts):
        if f"投稿想定時刻: {slot}" in post:
            target_idx = i
            break

    if target_idx is None:
        log(f"No pending post for slot={slot}")
        sys.exit(0)

    target_post = posts[target_idx]

    # 文面抽出
    match = re.search(
        r"- 文面:\s*\n+(.+?)\n+- ステータス:", target_post, re.DOTALL
    )
    if not match:
        log("Failed to parse text from post")
        sys.exit(1)

    type_match = re.search(r"-\s*種類:\s*(\S+)", target_post)
    post_type = type_match.group(1) if type_match else "単発"

    raw_text = match.group(1).strip()
    main_text, comments = parse_main_and_comments(raw_text)
    image_url = resolve_image_url(target_post)
    require_image = os.getenv("REQUIRE_IMAGE") == "1" or post_type == "画像付き"
    log(
        f"Text preview: {main_text[:30]}... ({len(main_text)} chars), "
        f"comments={len(comments)}, image={'yes' if image_url else 'no'}"
    )

    if len(main_text) > THREADS_TEXT_LIMIT:
        log(f"WARNING: text exceeds 500 char limit ({len(main_text)} chars)")

    if require_image:
        if not image_url:
            log("REQUIRE_IMAGE=1 but no usable image file was found; aborting before post")
            sys.exit(1)
        if not verify_image_url(image_url):
            log("REQUIRE_IMAGE=1 but the image URL is not publicly available; aborting before post")
            sys.exit(1)

    if dry_run:
        log("DRY RUN - skipping actual post")
        print(f"\n--- DRY RUN: would post to Threads ---\n[MAIN]\n{main_text}")
        for i, c in enumerate(comments, 1):
            print(f"[COMMENT {i}]\n{c}")
        if image_url:
            print(f"[IMAGE] {image_url}")
        print("---")
        return

    # メイン投稿（一過性エラーはリトライ。通常は画像失敗時に本文のみへフォールバック）。
    # REQUIRE_IMAGE=1 の場合は本文のみ投稿へフォールバックしない。
    def _post_main():
        try:
            return post_to_threads(
                main_text, creds["access_token"], creds["user_id"], image_url=image_url
            )
        except Exception as e_img:
            if image_url:
                if require_image:
                    log(f"image post failed and REQUIRE_IMAGE=1; aborting: {e_img}")
                    raise
                log(f"image post failed, retry text-only: {e_img}")
                return post_to_threads(
                    main_text, creds["access_token"], creds["user_id"], image_url=None
                )
            raise

    try:
        thread_id = post_main_with_retry(_post_main)
        log(f"POSTED main thread_id={thread_id}")
    except Exception as e:
        # メイン投稿が出ていない＝この枠は未消費。次の冗長クロンが再試行する。
        log(f"POST FAILED (main): {e}")
        sys.exit(1)

    # ここから先はメイン投稿成功済み。コメントが失敗しても枠は消費して確定させる
    # （でないと次の冗長クロンがメインを二重投稿してしまう）。
    reply_to = thread_id
    comment_ids = []
    for i, comment in enumerate(comments, 1):
        try:
            cid = post_to_threads(
                comment, creds["access_token"], creds["user_id"], reply_to_id=reply_to
            )
            comment_ids.append(cid)
            reply_to = cid
            log(f"POSTED comment {i} thread_id={cid}")
        except Exception as e:
            log(f"COMMENT {i} FAILED (本文は投稿済み・続行): {e}")
            break

    # この日×この枠を投稿済みとして記録（冪等ガード用）
    mark_posted(slot)

    # posted.md に追記
    id_match = re.search(r"## (\d{4}-\d{2}-\d{2}-\d{3})", target_post)
    post_id = id_match.group(1) if id_match else "unknown"
    runner = "GitHub Actions" if os.getenv("GITHUB_ACTIONS") else "ローカル"
    extra = ""
    if comment_ids:
        extra += "- comment_ids: " + ", ".join(comment_ids) + "\n"
    if image_url:
        extra += f"- 画像: {image_url}\n"
    posted_entry = f"""
## {post_id}（Threads自動配信 / {runner}）
- プラットフォーム: Threads
- 種類: {post_type}
- 投稿日時: {datetime.now(JST).isoformat()}
- thread_id: {thread_id}
- URL: https://www.threads.com/@atelierbase_own/post/{thread_id}
{extra}- 文面:

{raw_text}

- ステータス: posted

---
"""

    with open(POSTED, "a", encoding="utf-8") as f:
        f.write(posted_entry)

    # pending.md から該当エントリ削除
    posts.pop(target_idx)
    new_content = header + "\n".join(posts) if posts else header
    with open(PENDING, "w", encoding="utf-8") as f:
        f.write(new_content)

    log(f"DONE moved {post_id} to posted (type={post_type})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="投稿せずに動作確認")
    parser.add_argument("--skip-jitter", action="store_true", help="ジッター遅延スキップ")
    args = parser.parse_args()
    main(dry_run=args.dry_run, skip_jitter=args.skip_jitter)
