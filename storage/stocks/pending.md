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
## 2026-06-28-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-28（日）
- 軸: 主軸（海外翻訳） #AI開発エージェント記録
- ソース: arXiv: Detecting AI Coding Agents in Open Source (2026-06-23) https://arxiv.org/abs/2606.24429
- 画像プロンプト: Use case: infographic-diagram. Asset type: Threads square post information card, final PNG, 1024x1024. Create a polished Japanese information card that summarizes a Threads post about a recent overseas AI coding agents research paper analyzing 180M+ repositories. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Core insight: AI coding agent work is often invisible unless we intentionally preserve request, execution, and review records. Speed matters, but traceability protects real projects. Canvas and style: square 1024x1024, clean editorial business infographic, readable Japanese typography, warm off-white background, deep charcoal text, restrained accents in teal and amber, generous margins, professional spacing, high contrast, mobile-readable. STRICT TEXT RULE: Render ONLY the exact text below. Do not add any other letters, numbers, words, UI text, labels, captions, source names, or tiny paragraphs anywhere in the image. Icons and cards must be blank/simple shapes with no internal text. Exact text to render: Top small label: 「海外調査: 180M+ repo」 Main headline, large and strong: 「見えないAI作業を\n記録で守る」 Three action labels, each in a separate compact block: 「依頼」 / 「実行」 / 「確認」 Bottom small line: 「速さより、追える形。」 Visual structure: left side shows several blank stacked code/task cards fading into a hidden/low-visibility area; center shows a clear trace line or timeline; right side shows a simple review checklist shield icon. The three compact blocks 「依頼」「実行」「確認」 sit along the trace line as a practical 3-step action flow. Show conclusion, background, and practical action through structure, not long text. Avoid: generic AI atmosphere, glowing brain, random laptop, robots, people, faces, code rain, fake UI screenshots, unreadable tiny text, decorative-only scene, watermark, logo, purple/blue gradient, misspelled Japanese, extra text beyond the exact text list.
- 画像ファイル: storage/images/2026-06-28-701.png
- 文面:

海外の新しいAI開発エージェント研究を読んで、ちょっと冷や汗が出ました。

180M超のコード履歴を見た調査では、AIが関わった作業は1つの手がかりだけだと大きく見落とすそうです。Claude Codeのコミットも、AI専用アカウント名だけでは3.3%しか拾えなかったとのこと。

私もAIに任せた修正を、あとから「どこまで人が確認したっけ？」と追いかけた経験があります😅
速く作るほど、依頼・実行・確認の記録が効きますね。

皆さんは、AIに任せた作業の記録をどう残していますか？

- ステータス: pending

---
## 2026-06-28-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-28（日）
- 軸: サブ軸1（自分の実例） #AIレビュー設計
- ソース: arXiv: Augmentation with Dilution (2026-06-24) https://arxiv.org/abs/2606.26289
- 画像プロンプト: Use case: infographic-diagram Asset type: Threads square post information card, final PNG, 1024x1024. Primary request: Create a minimal, polished Japanese information card about a recent overseas research paper on AI coding agent adoption and human contributor ecosystems. It must be an information card, not a mood image. A viewer should understand: AI speeds up implementation, but teams must preserve review and learning space. Canvas and style: square 1024x1024, warm off-white background, deep charcoal text, restrained teal and amber accents, high contrast, clean editorial business infographic, large mobile-readable Japanese typography, generous margins. STRICT LAYOUT: Use only five text areas total: 1 top label, 1 main headline, 3 small action blocks, 1 bottom line. No other written words anywhere. The icons and diagram shapes must contain no text, no fake code letters, no UI labels, no captions, no numbers. Render exactly this text and nothing else: 1) Top label: 「海外調査: 11,097 repo」 2) Main headline: 「AIで速く作るほど\n学ぶ余白を残す」 3) Three small blocks: 「新人参加 ↓」 「レビュー深さ ↑」 「場を作る」 4) Bottom line: 「実装後に、人が学べる設計を。」 Visual structure: simple left-to-right cause-and-action flow using only unlabeled shapes: left = fast stacked task cards and speed lines; center = review checkpoint symbol; right = circular learning loop symbol. Place the three small action blocks below the flow. Keep the diagram clean and abstract, with no people, no faces, no laptops. The conclusion is the main headline. Avoid: any text not listed above, extra labels, column headings, source names, tiny paragraphs, fake UI text, code snippets, random laptop, generic AI atmosphere, glowing brain, robots, people, faces, code rain, watermark, logo, purple/blue gradient, misspelled Japanese.
- 画像ファイル: storage/images/2026-06-28-702.png
- 文面:

海外のAI開発エージェント研究を読んで、少しハッとしました。

11,097件のGitHubリポジトリ調査では、AI導入後も人間の人数自体は大きく減らない一方、新人の参加比率は3.7pt低下。レビュー、つまり変更を人が確かめる工程は5.3%深くなったそうです。

私もAIに実装を任せるほど、書く時間は減るのに「確認する力」と「人が学ぶ余白」を残す設計が大事だと感じています✨

皆さんの現場では、AIに任せた後のレビューや学びの場をどう残していますか？

- ステータス: pending

---
