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
## 2026-06-30-701
- 種類: 画像付き
- 投稿想定時刻: 朝（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-30（火）
- 軸: 主軸（海外翻訳）/等身大・人間味
- ソース: arXiv: Detecting AI Coding Agents in Open Source (2606.24429)
- 画像プロンプト: Create a square PNG image, 1024x1024, for a Japanese Threads post. This must be generated as a complete image2 information card, not HTML, not SVG, not a mockup, not a decorative atmosphere image. Purpose: a one-second insight card summarizing a practical lesson from a personal post about AI coding agents: if you only check pull requests, AI-made changes become hard to trace later; teams should make AI changes visible at more than one entry point. Style: clean modern Japanese business infographic, high contrast, warm white background, dark charcoal/navy text, teal accent, small amber warning accent. Professional but emotionally relatable, made to stop scrolling on Threads. No random laptop, no generic AI atmosphere, no robot face, no sci-fi glow, no code-rain. Visual structure: a problem-to-insight flow, NOT a fixed three-column layout. Use a left upper worry bubble flowing into a center bottleneck, then down/right into a simple action path. Text blocks maximum 5, short Japanese labels only: 1) Large main headline: 「AI変更、あとで追えますか？」 2) Small worry label: 「PRだけで安心」 3) Center warning label: 「見落とし」 4) Insight label: 「入口を増やす」 5) Three tiny action chips grouped together: 「署名」 「ログ」 「レビュー線引き」 Optional tiny footer, very small and not prominent: 「参考: arXiv 2606.24429」 Include simple abstract icons: pull request branch, commit dot trail, file/settings icon, checklist. Keep Japanese text clean and legible. Avoid long sentences, avoid dates as main focus, avoid research-paper layout, avoid three equal columns.
- 画像ファイル: storage/images/2026-06-30-701.png
- 文面:

正直、AIに任せた変更をあとから追うのが怖くなる時があります。

自分の小さなサービスでも、PRだけ見て安心していたら、設定ファイルやcommitの履歴に大事な手がかりが残っていて、確認が後手に回ったことがありました。

6/23公開の arXiv 論文では、PRベースの調査はcommitで検出されたClaude Code採用の79%を見逃す、という結果がありました。PRとは変更提案の入口のことです。

便利さより先に、追える設計。
最初に整えるなら、権限・ログ・レビュー線引きのどれから始めますか？

- ステータス: pending

---
