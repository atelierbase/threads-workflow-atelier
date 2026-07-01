# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- 2026-06-29 の伸び悩み対応で、古い未消化キューは `archive/pending-stale-growth-reset-2026-06-29.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-07-01-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-01（水）
- 軸: サブ軸1（自分の実例）
- ソース: Tom's Hardware: AI coding agents can be tricked into installing malware via clean GitHub repositories
- 画像プロンプト: Create a square 1024x1024 PNG Japanese Threads insight card. This is a post summary card, not an atmosphere image. The card must communicate the practical realization from a post about AI coding agents and external repositories: conclusion, background, and action are understandable from the image alone. Visible text: use ONLY these exact Japanese labels, no other words, no English, no dates, no source names, no research labels: 1. Main headline, very large: 「外部repo、実行前に止める」 2. Small subheadline: 「AIに任せるほど、最初の許可が大事」 3. Left label: 「触る」 4. Middle label: 「止める」 5. Right label: 「確認する」 Visual structure: a problem-to-action flow, not a fixed 3-column research card. Show a clean code folder/repository shape on the left, a strong stop gate/checkpoint in the center, and a network/log review panel on the right. Use arrows or a curved path from left to center to right. The center checkpoint should be the visual anchor. Make it feel like a practical safety insight card for Threads, with a little tension and relief. Design: modern Japanese business infographic, high legibility, white/off-white background, deep charcoal text, restrained red for stop, green for OK, blue for review, amber caution accents. Maximum 5 text blocks. Large headline, short labels only. No generic AI atmosphere, no random laptop, no decorative-only scene, no robot mascot, no tiny explanatory text, no footer, no watermark. Ensure Japanese text is correctly spelled with no garbling, especially 「外部repo、実行前に止める」「触る」「止める」「確認する」.
- 画像ファイル: storage/images/2026-07-01-702.png
- 文面:

正直、外部repoをAIに触らせる時だけ、まだ少し怖いです。

急いで試したい時ほど「cloneして初期化して」と丸投げしたくなるんですが、Tom’s Hardwareは6月28日、Mozilla 0dinチームが“きれいに見えるGitHub repo”経由でClaude Codeに悪意ある初期化手順を実行させる例を示した、と報じていました。repoはコード置き場のことです。

気づきは、AIを疑うより先に「実行前に止まる場所」を作ること。

あなたなら最初に整えるのは、外部repoの実行許可ルールですか？それとも通信ログの確認ですか？

- ステータス: pending

---
