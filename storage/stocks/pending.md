# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- 2026-06-29 の伸び悩み対応で、古い未消化キューは `archive/pending-stale-growth-reset-2026-06-29.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---## 2026-07-01-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-01（水）
- 軸: サブ軸2（実業家視点）
- ソース: Business Insider: OpenAI Codex usage-limit war room fix
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese Threads insight card, square PNG 1024x1024. Primary request: Create a Threads-stopping Japanese insight card that summarizes this practical realization: when delegating work to AI coding agents like Codex, the hidden background work can grow beyond what the user feels they asked for, so make usage and limits visible before scaling delegation. This must be a post summary card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Visible text: use ONLY these exact Japanese text blocks, no other visible words, no English except the product-like term if it appears in small UI shapes, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「任せた分だけ 見えなくなる」 2. Small subheadline: 「速さの前に、使用量を見える化」 3. Left small label: 「小さな依頼」 4. Center small label: 「裏で増える」 5. Right small label: 「上限を決める」 Visual structure: a problem-to-action flow, not a fixed 3-column research card. Show a small task request on the left flowing into a larger hidden background-work loop in the center, then into a clear usage meter and stop-rule panel on the right. The center should feel slightly tense because work is growing invisibly; the right side should feel calm and controlled. Use a curved path or funnel so it reads as 「小さな依頼」→「裏で増える」→「上限を決める」 without looking like an academic paper. Design: modern Japanese business infographic, high legibility, off-white background, deep charcoal headline, restrained amber for hidden growth, blue for visibility/dashboard, green for controlled limit, small red stop marker. Large typography, generous spacing, maximum 5 text blocks, short labels only. No generic AI atmosphere, no random laptop, no decorative-only scene, no robot mascot, no research summary card, no dense UI, no tiny explanatory text. Ensure Japanese text is correctly spelled with no garbling, especially 「任せた分だけ 見えなくなる」「使用量」「見える化」「小さな依頼」「裏で増える」「上限を決める」.
- 画像ファイル: storage/images/2026-07-01-703.png
- 文面:

正直、AIに任せた作業量をあとから見て、少し焦ったことがあります。

自分では「小さな修正を頼んだだけ」のつもりでも、裏でレビューや再試行が走ると、気づかないうちに使用量が増えるんですよね。

Business Insiderは6月30日、Codexでauto-reviewやsubagentsが想定より多く動き、利用上限の消費が早まった問題と修正を報じていました。subagentは、裏で手伝う小さなAI担当のことです。

気づきは、AIの速さより先に「どこまで動いたか」を見える化すること。

あなたなら最初に整えるのは、使用量アラートですか？それとも作業ごとの上限ルールですか？

- ステータス: pending

---
## 2026-07-02-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-02（木）
- 軸: サブ軸1（自分の実例）
- ソース: arXiv: The Shift to Agentic AI: Evidence from Codex (https://arxiv.org/abs/2606.26959)
- 画像プロンプト: Create a square 1024x1024 PNG Japanese Threads insight card. This is a post summary information card, not an atmosphere image. It must communicate this realization from a personal Threads post about Codex and AI coding agents: when you run multiple agents in parallel, the bottleneck moves from producing work to reviewing and closing the work, so decide the exit before adding more parallel tasks. The viewer should understand the conclusion, background, and practical action from the image alone. Visible text: use ONLY these exact Japanese text blocks, no other visible words, no English letters anywhere, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「増やす前に 出口を決める」 2. Small subheadline: 「同時進行は、確認で詰まる」 3. Left label: 「同時に頼む」 4. Center label: 「確認が渋滞」 5. Right label: 「完了条件」 Important text rule: Do not put any letters, numbers, pseudo-text, English, or icons with words inside the small task cards or checklist lines. Use blank cards, dots, checkmarks, and simple shapes only. Do not write AI anywhere except no AI text at all. Visual structure: a before/after transformation with a bottleneck flow, not a fixed 3-column research card. Left side shows several blank task cards starting in parallel, flowing into a narrow center checkpoint where review items pile up slightly and feel tense. Right side opens into a clean blank checklist gate labeled 「完了条件」 with green checkmarks, showing that work moves smoothly once the endpoint is defined. The image should read as 「同時に頼む」 -> 「確認が渋滞」 -> 「完了条件」 but use a curved funnel/bottleneck path rather than three equal columns. Design: modern Japanese business infographic for Threads, high legibility, off-white background, deep charcoal headline, blue blank task cards, amber caution accents around the review bottleneck, green completion accent on the right. Large typography, generous spacing, maximum 5 text blocks, short labels only. Main headline should feel like a reader pain/realization, not a research title. Avoid generic AI atmosphere, random laptop, decorative-only scene, robot mascot, research summary card, dense UI, tiny explanatory text, source/date labels. Ensure Japanese text is correctly spelled with no garbling, especially 「増やす前に 出口を決める」「同時進行は、確認で詰まる」「同時に頼む」「確認が渋滞」「完了条件」.
- 画像ファイル: storage/images/2026-07-02-702.png
- 文面:

正直、AIを並列で走らせるほど、最後に私が詰まる日があります。

コードは速く出るのに、どれを先に見て、何をもって完了にするかが曖昧だと、確認だけが渋滞するんですよね。

6月25日のarXiv論文「The Shift to Agentic AI」は、Codex利用者の10%超が週に3つ以上のエージェントを同時管理していると分析していました。エージェントは、作業を自走するAI担当のことです。

増やす前に、出口を決める。
あなたは先に決めるなら、完了条件ですか？それとも確認する順番ですか？

- ステータス: pending

---
