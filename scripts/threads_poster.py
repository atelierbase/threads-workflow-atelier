#!/usr/bin/env python3
"""
Threads Scheduled Poster

pending.md から該当時間帯のストックを取り出して Threads に投稿し、
posted.md に移動する。GitHub Actions / ローカル両対応。

対応する投稿タイプ:
  - 単発: テキスト1本
  - コメント仕込み: メイン投稿 → reply_to_id でコメントを連投
  - 画像付き: 画像を公開URL(raw.githubusercontent)で添付（未配置なら本文のみ）

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
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests


# === パス定義（環境によって自動切替）===
if os.getenv("GITHUB_ACTIONS"):
    REPO_DIR = Path(__file__).resolve().parent.parent
else:
    REPO_DIR = Path.home() / "atlier-base-v1" / "projects" / "sns-auto-post" / "threads"

PENDING = REPO_DIR / "storage" / "stocks" / "pending.md"
POSTED = REPO_DIR / "storage" / "stocks" / "posted.md"
CREDS = Path.home() / ".config" / "threads-workflow" / "threads-credentials.json"
LOG_DIR = REPO_DIR / "storage" / "analytics"
LOG = LOG_DIR / "scheduler.log"

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
    log(f"画像ファイル指定あり ({rel}) だが未配置 → 本文のみでフォールバック")
    return None


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
    slot = current_slot()
    log(f"START slot={slot} dry_run={dry_run} skip_jitter={skip_jitter}")

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

    raw_text = match.group(1).strip()
    main_text, comments = parse_main_and_comments(raw_text)
    image_url = resolve_image_url(target_post)
    log(
        f"Text preview: {main_text[:30]}... ({len(main_text)} chars), "
        f"comments={len(comments)}, image={'yes' if image_url else 'no'}"
    )

    if len(main_text) > THREADS_TEXT_LIMIT:
        log(f"WARNING: text exceeds 500 char limit ({len(main_text)} chars)")

    if dry_run:
        log("DRY RUN - skipping actual post")
        print(f"\n--- DRY RUN: would post to Threads ---\n[MAIN]\n{main_text}")
        for i, c in enumerate(comments, 1):
            print(f"[COMMENT {i}]\n{c}")
        if image_url:
            print(f"[IMAGE] {image_url}")
        print("---")
        return

    # 投稿
    try:
        try:
            thread_id = post_to_threads(
                main_text, creds["access_token"], creds["user_id"], image_url=image_url
            )
        except Exception as e_img:
            if image_url:
                log(f"image post failed, retry text-only: {e_img}")
                thread_id = post_to_threads(
                    main_text, creds["access_token"], creds["user_id"], image_url=None
                )
            else:
                raise
        log(f"POSTED main thread_id={thread_id}")

        reply_to = thread_id
        comment_ids = []
        for i, comment in enumerate(comments, 1):
            cid = post_to_threads(
                comment, creds["access_token"], creds["user_id"], reply_to_id=reply_to
            )
            comment_ids.append(cid)
            reply_to = cid
            log(f"POSTED comment {i} thread_id={cid}")
    except Exception as e:
        log(f"POST FAILED: {e}")
        sys.exit(1)

    # posted.md に追記
    id_match = re.search(r"## (\d{4}-\d{2}-\d{2}-\d{3})", target_post)
    post_id = id_match.group(1) if id_match else "unknown"
    type_match = re.search(r"-\s*種類:\s*(\S+)", target_post)
    post_type = type_match.group(1) if type_match else "単発"

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
