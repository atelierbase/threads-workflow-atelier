# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-26-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-26（金）
- 軸: AI自動化メタ #作業委任
- ソース: Axios, Jun 25: AI agents are here for real this time
- 画像プロンプト: Create a polished square social media summary card for Threads, 1024x1024. This must summarize the post, not be an atmospheric image. IMPORTANT: do not write any full-year date and do not include a source footer. Only use the short label '6/25'. Topic: Codex usage is moving from chat to delegated work; 80.6% of sampled individual Codex users made at least one request estimated as more than 30 minutes of experienced human work. Main Japanese headline, exact and large: AIに作業を預ける時代へ. Use three connected blocks with exact labels: 質問 / 依頼 / レビュー. Include prominent stat: 80.6% and label: 30分超の作業. Small top label: Codex / 6/25. Style: clean, friendly operations board, white and charcoal base, teal and amber accents, large readable text, practical business tone. Avoid generic AI atmosphere, random laptop, tiny text, long sentences, decorative-only scene, source footer. Reject if headline, stat, date, or labels are wrong or garbled.
- 画像ファイル: storage/images/2026-06-26-701.png
- 文面:

Axiosの記事で、Codexの使われ方が「チャット」から「作業を預ける」方向へ進んでいると紹介されていました。

個人ユーザーの80.6%が、経験者なら30分以上かかる作業に相当する依頼を少なくとも1回出していた、という見方です。

私も自動投稿やリサーチを任せる中で、AIは質問相手より「作業単位の担当者」に近づいていると感じます。

皆さんは、AIにどこまで作業を預けていますか？

- ステータス: pending

---
