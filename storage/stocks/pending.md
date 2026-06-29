# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---## 2026-06-27-701
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
## 2026-06-29-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-29（月）
- 軸: 主軸（海外翻訳） #AIコスト実験
- ソース: Business Insider: Claude Code creator Boris Cherny on AI ROI and experimentation (2026-06-23) https://www.businessinsider.com/boris-cherny-anthropic-token-cost-roi-ai-2026-6
- 画像プロンプト: Use case: infographic-diagram Asset type: Threads square post information card, final PNG, 1024x1024. Primary request: Create a polished Japanese information card summarizing a Threads post about recent overseas comments from Claude Code creator Boris Cherny: companies should watch ROI, but should not restrict AI agent experimentation too early. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Core insight: For AI development agents, do not clamp down on usage before finding what creates value. Set a safe budget, run small experiments, then keep only the work with visible ROI. Canvas and style: square 1024x1024, clean editorial business infographic, readable Japanese typography, warm off-white background, deep charcoal text, restrained accents in teal and amber, generous margins, high contrast, mobile-readable, polished spacing. STRICT TEXT RULE: Render ONLY the exact text below. Do not add any other letters, numbers, source names, UI text, fake code text, captions, or tiny paragraphs anywhere in the image. Icons and diagram shapes must be blank/simple shapes with no internal text. Exact text to render: Top small label: 「海外発言: Claude Code」 Main headline, large and strong: 「AI予算は\n締める前に\n試す」 Three compact action blocks: 「予算枠」 / 「小さく実験」 / 「価値で残す」 Bottom small line: 「ROIは、使い道が見えてから。」 Visual structure: a clear 3-step flow from left to right. Left: a simple budget frame or coin/token stack showing a safe spending boundary. Center: a small experiment tray or sandbox with blank task cards moving through it. Right: selected blank task cards with check marks and a simple ROI gauge icon. Show the practical action through structure: budget -> experiment -> keep valuable work. Constraints: short labels only, no long paragraphs, no decorative-only scene, no people, no faces, no robots, no random laptop, no glowing brain, no code rain, no fake UI screenshots, no unreadable tiny text, no generic AI atmosphere, no watermark, no logo, no purple/blue gradient. Prioritize exact Japanese text accuracy for the headline, top label, three action labels, and bottom line.
- 画像ファイル: storage/images/2026-06-29-701.png
- 文面:

Claude Codeの作り手 Boris Cherny 氏が、AI投資はROI（投資対効果）を見つつ、早すぎる制限で実験を止めない方がいいと話していました。

AI開発エージェントは、使うほどトークン費用が増える道具です。私も最近、コストを気にしすぎて、小さな検証まで絞りそうになりました。

でも、最初から締めすぎると「何が効くか」を見つける前に止まるんですよね✨
大事なのは、予算を決めて試し、価値が見えた作業だけ残すこと。

皆さんは、AIのコスト管理と実験の余白、どちらを先に設計していますか？

- ステータス: pending

---
## 2026-06-29-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-29（月）
- 軸: サブ軸2（実業家視点） #AI権限設計
- ソース: TechRadar/OALABS: AI agents Claude Code and Codex breach reporting (2026-06-22) https://www.techradar.com/pro/security/a-newbie-hacker-used-vague-low-skill-prompts-in-claude-and-codex-to-breach-14-companies-and-the-ai-agents-did-all-the-legwork
- 画像プロンプト: Use case: infographic-diagram Asset type: Threads square post information card, final PNG, 1024x1024. Primary request: Create one polished Japanese information card summarizing a Threads post about recent overseas security reporting from TechRadar/OALABS: AI development agents such as Claude Code and Codex can amplify execution ability when users give broad permissions, so practical teams should pair speed with permission boundaries, logs, and human stop points. This must be an information card, not a mood image or generic AI atmosphere. A viewer should understand the conclusion, background, and practical action from the image alone. Core insight: AI development agents are powerful because they can act, not just answer. Do not hand over broad authority casually. Design three safeguards before scaling usage: limit permissions, keep logs, and define where a human can stop/review. Canvas and style: square 1024x1024, clean editorial business infographic, readable Japanese typography, warm off-white background, deep charcoal text, restrained accents in teal, muted red, and amber, generous margins, high contrast, mobile-readable, polished spacing. Use crisp flat vector-like diagram shapes. STRICT TEXT RULE: Render ONLY the exact Japanese text below. Do not add any other letters, numbers, source names, UI text, code text, captions, tiny paragraphs, watermarks, or logos anywhere in the image. Icons and diagram shapes must be blank/simple shapes with no internal text. Exact text to render: Top small label: 「海外報道: AIエージェント」 Main headline, large and strong: 「AIに権限だけ\n渡さない」 Three compact action blocks: 「権限を絞る」 / 「ログを残す」 / 「人が止める」 Bottom small line: 「速さには、止め方もセット。」 Visual structure: a clear defensive 3-step flow from left to right. Left: a permission gate or keyhole with a narrow boundary, showing limited access. Center: a clean audit trail/log line with blank task cards and check dots. Right: a human review stop point represented by a simple stop switch/checkpoint icon, with no people or faces. Use arrows and grouping to show permission boundary -> traceable logs -> human stop/review. Constraints: short labels only, no long paragraphs, no decorative-only scene, no random laptop, no robots, no humanoid icons, no faces, no people, no malware imagery, no exploit/code visuals, no fake UI screenshots, no unreadable tiny text, no generic glowing AI background, no purple/blue gradient. Prioritize exact Japanese text accuracy for the headline, top label, three action labels, and bottom line.
- 画像ファイル: storage/images/2026-06-29-703.png
- 文面:

海外のセキュリティ報道で、少し背筋が伸びました。

OALABSの分析では、低スキルの攻撃者がClaude CodeやCodexを使い、14社の侵害に関わったとされています。AI開発エージェントは、指示を受けて調査や実行を進めるAIのことです。

私も便利さに慣れるほど、「この権限まで渡して大丈夫か」を後回しにしがちでした😅
速さをくれる道具ほど、権限を絞る、ログを残す、人が止める設計が必要ですね。

皆さんは、AIに渡す権限の線引き、どこで決めていますか？

- ステータス: pending

---
