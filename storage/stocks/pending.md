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
## 2026-07-06-702
- 種類: 画像付き
- 投稿想定時刻: 昼（image2生成済み・GitHub Actions配信）
- 想定日: 2026-07-06（月）
- 軸: サブ軸1（自分の実例）
- ソース: The Verge: OpenAI is teasing new hardware that's probably for Codex (https://www.theverge.com/ai-artificial-intelligence/959174/openai-codex-hardware-work-louder)
- 画像プロンプト: Use case: infographic-diagram Asset type: Japanese Threads insight card, square PNG 1024x1024. Primary request: Create a Threads-stopping Japanese insight card that summarizes this practical realization: before buying or optimizing new Codex hardware shortcuts, first choose which recurring AI-agent task is worth turning into a one-touch workflow. This must be a post summary card, not an atmosphere image. The viewer should understand the conclusion, background, and practical action from the image alone. Visible text: use ONLY these exact Japanese text blocks, no other visible words, no English, no dates, no source names, no research labels, no footer, no watermark: 1. Main headline, very large: 「ボタンより先に 任せる仕事」 2. Small subheadline: 「道具の前に、反復タスクを決める」 3. Small label: 「迷う」 4. Small label: 「選ぶ」 5. Small label: 「押す」 Visual structure: an emotional decision flow, not a fixed 3-column research card. Show a cluttered pile of possible AI-agent tasks on the left as abstract sticky notes and small task chips, a clear narrowing funnel or spotlight in the center, and a calm single-action button/workflow tile on the right. It should read as 「迷う」→「選ぶ」→「押す」, but avoid looking like an academic slide or a generic process diagram. The card should feel practical, warm, and businesslike. Style/medium: modern Japanese business infographic, crisp vector-like raster illustration, high legibility, large typography, generous spacing. Color palette: off-white background, deep charcoal headline, restrained teal for selected workflow, soft amber for decision tension, small muted red accents only for hesitation, plenty of white space. Avoid dominant purple/blue gradients and avoid beige-only palette. Composition/framing: square 1024x1024, strong first-viewport readability on Threads mobile, maximum 5 text blocks, sub-elements limited to three. Constraints: Japanese text must be correctly spelled with no garbling, especially 「ボタンより先に 任せる仕事」「反復タスク」「迷う」「選ぶ」「押す」. Do not make source name, date, or research label the focus. Avoid: generic AI atmosphere, random laptop, decorative-only scene, robot mascot, dense UI, tiny explanatory text, fixed three-column report card, academic research summary, source/date labels, malformed Japanese text.
- 画像ファイル: storage/images/2026-07-06-702.png
- 文面:

正直、Codex用の専用ハードという話を見て、少し欲しくなりました。

でも、自分の作業を振り返ると、先に決めるべきは「何をボタン化するか」なんですよね。

The Vergeは6月30日、OpenAIがWork Louderと組んでCodex向け小型デバイスを予告したと報じていました。Codexは、コード生成や修正を任せられるAI開発エージェントです。

気づきは、道具を増やす前に、毎週くり返す依頼を1つ選ぶこと。

あなたなら最初にボタン化するのは、テスト実行ですか？それともレビュー依頼ですか？

- ステータス: pending

---
