# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-27-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-27（土）
- 軸: 主軸（海外翻訳） #Codex利用研究
- ソース: arXiv: The Shift to Agentic AI: Evidence from Codex (2026-06-25) https://arxiv.org/abs/2606.26959
- 画像プロンプト: Use case: infographic-diagram Asset type: Threads square post information card, final PNG, 1024x1024. Primary request: Create a polished Japanese information card that summarizes a Threads post about the recent Codex usage research. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Canvas and style: square 1024x1024, clean editorial business infographic, readable Japanese typography, off-white background, charcoal text, restrained accent colors in teal and warm yellow, generous margins, professional spacing. Render this Japanese text verbatim, with no extra characters and no extra text: Top small label: 「海外調査: Codex利用が5倍超」 Main headline, large and strong: 「AI作業は\n増やすより\n整える」 Three sub elements, each in a separate compact block: 1. 「小さく頼む」 2. 「証跡を見る」 3. 「戻せる単位」 Bottom small line: 「並走より、レビュー設計。」 Visual structure: a cause-and-effect flow: stacked task cards show more parallel AI work, a narrow checkpoint shows review congestion, then three action blocks lead to calm progress. Include the practical insight: AI work should be organized, not merely increased. Constraints: short labels only, no long paragraphs, no decorative-only scene, no random laptop, no robots, no people, no fake UI screenshots with unreadable tiny text, no generic glowing AI background, no watermark, no logo. Prioritize exact Japanese text accuracy for the main headline, source label, the three action labels, and bottom line.
- 画像ファイル: storage/images/2026-06-27-701.png
- 文面:

海外で公開されたCodex利用研究を読んで、少し刺さりました。

2026年前半で利用は5倍超。しかも、3体以上のエージェントを並走させる人も増えているそうです。
AI開発エージェントは、コードを書くAIというより「仕事を同時に進めるチーム」になり始めています。

私も最近、勢いで複数タスクを走らせて、レビュー待ちで詰まったことがあります😅
増やすほど大事なのは、任せ方より戻せる単位と確認の順番でした。

皆さんは、AIに並走させすぎて詰まった経験、ありますか？

- ステータス: pending

---
## 2026-06-27-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-27（土）
- 軸: サブ軸1（自分の実例） #Skills運用
- ソース: arXiv: The Shift to Agentic AI: Evidence from Codex (2026-06-25) https://arxiv.org/abs/2606.26959
- 画像プロンプト: Use case: infographic-diagram Asset type: Threads square post information card, final PNG, 1024x1024. Primary request: Create a polished Japanese information card about Codex Skills adoption. It must summarize this insight: AI work becomes stable when repeated instructions are turned into reusable workflow assets. This is an information card, not an atmosphere image. STRICT TEXT RULE: Render ONLY the exact text below. Do not put any other letters, numbers, words, UI text, labels, handwritten marks, checklist text, or captions anywhere in the image. Icons and cards must be blank/simple shapes with no internal text. Exact text to render: Top small label: 「海外調査: Codex Skills 26.6%」 Main headline: 「頼み方を\n資産にする」 Three step labels: 「型にする」 / 「渡す」 / 「見直す」 Bottom small line: 「毎回の指示を、再利用へ。」 Visual structure: three-step flow using blank icons only: 1) a messy blank note icon transforms into 2) a reusable blank workflow card icon, then 3) a blank review checklist icon with check symbols only. Use arrows between the three steps. The image should show conclusion, background, and practical action from the card alone. Style: square 1024x1024, clean editorial business infographic, warm off-white background, charcoal text, teal and warm yellow accents, generous margins, strong hierarchy, readable on mobile, modern Japanese tech account. Avoid: any extra text beyond the exact text list, generic AI atmosphere, random laptop, robots, people, faces, code rain, fake UI screenshots, tiny paragraphs, watermarks, logos, decorative-only scene, purple/blue gradient. Spell Codex and Skills exactly.
- 画像ファイル: storage/images/2026-06-27-702.png
- 文面:

海外で出たCodex利用研究で、思わずメモした数字があります。

利用者の26.6%が「Skills」を使っているそうです。Skillsは、毎回の指示や手順を再利用できる仕組みのこと。

私も最初は、毎回プロンプトを丁寧に書けばいいと思っていました。でも投稿づくりや検証を続けるほど、うまくいく作業は“型”にして渡した方が安定するんですよね✨

AIを賢くするより、私の頼み方を資産化する。
この感覚がかなり大事だと感じています。

皆さんは、AIに渡す手順をどこまで型化していますか？

- ステータス: pending

---
