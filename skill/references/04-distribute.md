# 04-distribute: 配信（Threads API + GitHub Actions）

このフェーズの目的は、ストックから取り出した投稿を Threads に流すこと。

## 配信モード（現運用: api / GitHub Actions）

**現運用（2026-05-26〜）**: GitHub Actions による完全自動化
- リポジトリ: https://github.com/atelierbase/threads-workflow-atelier
- スケジュール: 毎日 JST 07:00 / 12:00 / 19:00
- PC の起動状態に関係なくクラウドで自動投稿

## Threads API の仕組み

**API**: Meta Graph API（Threads エンドポイント）
**ベースURL**: `https://graph.threads.net/v1.0/{user-id}/`

**投稿は2段階フロー**:

```
[Step 1: Media Container 作成]
POST /v1.0/{user-id}/threads
  - media_type: TEXT
  - text: [投稿本文]
  - access_token: [token]
→ container_id を返す

[Step 2: 数秒待ってから Publish]
POST /v1.0/{user-id}/threads_publish
  - creation_id: [container_id]
  - access_token: [token]
→ thread_id（投稿ID）を返す
```

詳細は `scripts/threads_poster.py` 参照。

## 接続前提

- Meta Developer Portal で App 作成済み
- Threads product 追加・Read/Write 権限
- Long-lived Access Token 取得済み
- Threads User ID（数字17桁）取得済み
- `~/.config/threads-workflow/threads-credentials.json` に保存（chmod 600）
- GitHub Secrets に `THREADS_ACCESS_TOKEN` / `THREADS_USER_ID` 登録済み

セットアップ手順の詳細は **`references/08-api-setup.md`** を参照。

## 配信フロー（scheduled_poster.py の挙動）

### Step 1: pending.md から取り出し

現在時刻に最も近い時間帯（朝/昼/夜）のストックの**最初のエントリ**を取得。

例: 現在 07:30 JST → 「朝」枠の最初のポスト

### Step 2: 投稿時刻にジッター

凍結リスク回避のため、**±15分のランダム遅延**を入れる。

```python
jitter = random.randint(0, 15 * 60)
time.sleep(jitter)
```

毎日きっかり同じ時刻に投稿しないことが、ボット判定回避の基本。

### Step 3: Threads API 経由で投稿

```python
# Container 作成
container_resp = requests.post(
    f"https://graph.threads.net/v1.0/{user_id}/threads",
    data={
        "media_type": "TEXT",
        "text": tweet_text,
        "access_token": access_token,
    }
)
container_id = container_resp.json()["id"]

# 3秒待つ
time.sleep(3)

# Publish
publish_resp = requests.post(
    f"https://graph.threads.net/v1.0/{user_id}/threads_publish",
    data={
        "creation_id": container_id,
        "access_token": access_token,
    }
)
thread_id = publish_resp.json()["id"]
```

### Step 4: 投稿成功時の処理

1. `pending.md` から該当エントリを削除
2. `posted.md` に追加
3. git commit & push（GitHub Actions が自動実行）

### Step 5: 失敗時の処理

| エラー | 原因 | 対処 |
|---|---|---|
| `401 Unauthorized` | access_token が無効・期限切れ | 再取得 → Secrets 更新 |
| `400 Bad Request` | 500文字超過、不正フォーマット | drafts.md に戻す |
| `403 Forbidden` | App 権限不足、アカウント問題 | Meta Developer で確認 |
| `429 Too Many Requests` | レート制限 | 5分後リトライ |
| `connection error` | ネットワーク一時障害 | 5分後リトライ |

リトライしても失敗する場合、エラーログを記録して pending.md に戻す。

## 凍結リスク回避（重要）

新規アカウント（or 過去あまり API 投稿していなかったアカウント）は特に注意：

1. **投稿時刻にジッター ±15分**（前述）
2. **同じ文面の連投を避ける**（過去30日と類似度チェック推奨）
3. **同じURLの連投も避ける**
4. **短時間に複数投稿しない**（最小間隔は30分以上）
5. **エンゲ（リプ・いいね・再投稿）は100%手動**
6. **最初の2週間は手動投稿も混ぜる**（API比率50%以下）

## レート制限

Threads API のレート制限：
- App ごとの制限あり（標準は 250 投稿/24時間/ユーザー）
- 通常の運用（1日3投稿）であれば余裕

## モード切替（将来）

将来的に config.json で切り替え可能にする（manual / scheduled / api）：

- `api`（現在）: GitHub Actions 自動投稿
- `scheduled`: Buffer など外部スケジューラ経由
- `manual`: コピペ用テキストのみ出力

## 関連ファイル

- `scripts/threads_poster.py`（投稿実行スクリプト）
- `.github/workflows/scheduled-post.yml`（GitHub Actions ワークフロー）
- `references/08-api-setup.md`（API セットアップ）
- `references/09-github-actions.md`（GitHub Actions 運用）

## 履歴

- v1（2026-05-26）: 初版（GitHub Actions + Threads API での自動配信）
