# threads-workflow-atelier

Threads アカウント **@atelierbase_own**（ひろ｜AI実業家）の自動投稿パイプライン。

GitHub Actions が毎日 **JST 07:00 / 12:00 / 19:00** に起動し、`storage/stocks/pending.md` から該当時間帯のストックを取り出して Threads に投稿、`posted.md` に移動する。

## アーキテクチャ

```
[GitHub Actions schedule (cron)]
        ↓
[checkout repo]
        ↓
[setup Python + requests]
        ↓
[scripts/threads_poster.py 実行]
        ↓
[Threads API v1 経由で投稿（コンテナ作成 → publish の2段階）]
        ↓
[pending.md / posted.md を更新してコミット&プッシュ]
```

## Secrets

- `THREADS_ACCESS_TOKEN`: Meta long-lived access token
- `THREADS_USER_ID`: Threads User ID（数字17桁）

## 関連リポジトリ

- X 用: https://github.com/atelierbase/x-workflow-atelier
