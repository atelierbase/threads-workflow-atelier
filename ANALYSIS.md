# ANALYSIS — Threads 週次分析（ローカル実行）

> **Analyst ロールのローカル実行プレイブック。** 週1回このMac上で走らせる。
> Threads insights API（＋必要ならローカルの grok）を使う。

## いつ走るか

- 週1回（X分析と同じ日でまとめてOK）
- ローカル cron or 「Threadsの分析して」で秘書が手動起動

## 何をするか

`skill/agents/analyst.md` の手順に従う。要約：

1. `storage/stocks/posted.md` の直近7日（thread_id付き）を一覧化
2. **Threads Graph API insights** で各投稿の views/likes/replies/reposts/quotes/shares を取得
   ```bash
   curl -G "https://graph.threads.net/v1.0/{thread-media-id}/insights" \
     --data-urlencode "metric=views,likes,replies,reposts,quotes,shares" \
     --data-urlencode "access_token=$TOKEN"
   ```
   - 権限 `threads_manage_insights` 未承認なら申請（`skill/references/04-distribute.md`）
3. オーナーの手動フィードがあれば優先
4. 仮説 → 反証で潰す → 効くルールに蒸留（**replies/会話の深さ重視**）
5. **`storage/analytics/learnings.md` に追記** → commit & push

```bash
cd ~/atlier-base-v1/projects/sns-auto-post/threads
git add storage/analytics/learnings.md
git commit -m "analysis: weekly learnings update (Threads)"
git push
```

## ループの閉じ方

ローカル Analyst が learnings.md 更新 → push → クラウドの Writer が次回参照。
