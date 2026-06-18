# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-18-902
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-18（木）
- 軸: 等身大・人間味型 #1
- ソース: OpenAI status / 自動投稿運用ログ, 2026-06-18
- 画像プロンプト: Use case: productivity-visual. Asset type: social media post image for Threads, generated with image2 only. Primary request: warm conceptual visual about learning from a missed automation post: a calm AI workflow with an empty queue being noticed before the next scheduled post. No readable text, letters, numbers, logos, brand names, or watermark. 1:1 square. Friendly professional style with image creation, queue tray, schedule clock, recovery loop, and gentle amber empty-queue glow.
- 画像ファイル: storage/images/2026-06-18-902.png
- 文面:

正直に書きます。

今日、自動投稿の仕組みを確認していて、いちばん怖いのは「失敗」ではなく「成功扱いの空振り」だと痛感しました。

配信側は動いている。
でも、生成側が本文と画像を積めていない。
ログ上は成功でも、実際には投稿されないんですよね。

CodexのようなAI自動化は、作るだけなら気持ちいいです。でも実務では「空だったら検知する」「次の枠に復旧する」までが本番だと思いました💡

皆さんは、自動化の監視まで設計していますか？

- ステータス: pending

---
