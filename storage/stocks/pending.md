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
## 2026-06-30-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-30（火）
- 軸: サブ軸1（自分の実例）/等身大・人間味
- ソース: Business Insider: OpenAI set up a 'warroom' to investigate Codex usage limits draining too quickly (2026-06-29) https://www.businessinsider.com/openai-codex-usage-limit-warroom-fix-issue-2026-6
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese Threads square image card, final PNG 1024x1024 Primary request: Create a complete square Japanese Threads “気づきカード” as one raster PNG. This is not HTML, not SVG, not a mockup, not a research summary card, not a decorative atmosphere image. Core insight: AI coding agents are fast, but if work is designed assuming unlimited usage, caps and waiting time can stop progress. Decide limits and fallback before starting. Composition: simple vertical flow with exactly three zones: top headline, middle Before→Stop→Insight flow, bottom small action chips. Avoid a fixed three-column card. Use icons and arrows instead of extra words. Style: clean modern Japanese business infographic, warm white background, dark charcoal text, teal main accent, small amber warning accent, crisp shapes, high contrast, plenty of whitespace, professional and emotionally relatable. IMPORTANT TEXT RULES: Include exactly these 5 Japanese text blocks and no other text anywhere. Do not add labels, captions, footers, notes, dates, source names, or tiny filler text. Text block 1, large headline: 「速いほど、止まり方が大事」 Text block 2, small teal label: 「走らせすぎ」 Text block 3, small amber label: 「上限で停止」 Text block 4, small teal label: 「先に決める」 Text block 5, three chips in one grouped block: 「上限・並列数・戻す線」 Visual elements without text: parallel lane icon, gauge icon near red zone, pause icon, checklist icon, arrows showing overuse → stop → pre-decided fallback. Constraints: Japanese text must be correctly spelled and very legible. Source name/date/research label must not appear. No extra words. No year/date. No long sentences. No random laptop, no generic AI atmosphere, no robot face, no sci-fi glow, no code-rain, no watermark, no clutter.
- 画像ファイル: storage/images/2026-06-30-702.png
- 文面:

正直、Codexを回す時だけ「今日どこまで任せるか」で迷います。

夢中で並列実行していると、気づいたら上限や待ち時間が先に来て、作りたい流れが止まることがあるんですよね。

Business Insiderは6/29、Codexの利用上限が想定より早く減る報告を受け、OpenAIが調査用のwarroomを置いたと報じていました。利用上限は、AIに使える計算量の枠です。

AIエージェントは速い。でも、無限前提で設計すると詰まる。
あなたなら先に決めるのは、1日の上限・並列数・手動に戻す線引きのどれですか？

- ステータス: pending

---
