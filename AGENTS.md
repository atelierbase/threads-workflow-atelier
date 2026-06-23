# AGENTS.md - Threads image2 queue automation (@atelierbase_own)

このrepoでのCodex Automationの役割は、**投稿を生成してimage2画像を作り、GitHub Actionsが投稿できる状態でcommit & pushすること**。
Codex Automation自身はThreadsへ投稿しない。配信は `.github/workflows/scheduled-post.yml` が定刻に行う。

アカウント: **ひろ｜AI実業家**（Threads=@atelierbase_own / 屋号 Atelier Base）
Threadsは共感・気づき・問いかけを重視する。

## 実行タイミング

推奨Automation発火:

| 投稿枠 | Codex Automation目安 | GitHub Actions投稿 |
|---|---:|---:|
| 朝 | 06:45 JST | 07:20 JST |
| 昼 | 11:45 JST | 12:20 JST |
| 夜 | 18:45 JST | 19:20 JST |

JST現在時刻からスロットを決める:

- 06:00-10:59 = 朝
- 11:00-14:59 = 昼
- それ以外 = 夜

## 絶対ルール

- 画像生成は **Codexのimage2のみ**。OpenAI Images API、Canva、HTML/CSS、SVG、ダミー画像は使わない。
- Codex Automationは **Threadsへ直接投稿しない**。`scripts/threads_poster.py` も実行しない。
- やることは `storage/images/<ID>.png` と `storage/stocks/pending.md` を作ってcommit & pushするところまで。
- 画像生成・保存・検査に失敗したら `pending.md` に積まない。
- 本文のみ投稿は禁止。`pending.md` に積む投稿は必ず `種類: 画像付き`。
- 本文は必ず問いかけで締める。
- 本名「石井」「ミライ塾」「アトリエの店主」は出さない。
- Threads用画像をx repoへ置かない。

## 1. 文脈を読む

必ず読む:

- `skill/references/00-context.md`
- `skill/templates/voice-guide.md`
- `skill/agents/writer.md`
- `storage/analytics/learnings.md`

ネタはWebSearch等で、直近1週間の海外Claude Code / Codex / AI開発エージェント関連情報を確認する。Threadsでは、最新情報を「私の体験・気づき・読者への問い」に接続する。

## 2. 投稿IDを決める

形式: `YYYY-MM-DD-NNN`

| 投稿枠 | suffix |
|---|---:|
| 朝 | 701 |
| 昼 | 702 |
| 夜 | 703 |

同じIDの画像やpending/postedが既にあれば、704以降へ1つずつずらす。

## 3. 投稿文を作る

- 200-400字目安、最大500字。
- 必ず問いかけで締める。
- 一人称「私」。
- 絵文字0-1個。
- 体験・失敗・気づきを主役にする。
- 投稿タイプは常に `画像付き`。

## 4. image2で画像を作る

image2に渡す画像プロンプトには以下を必ず含める:

- 一目で伝える気づき
- 投稿文をサマる情報カードであること（イメージ画像・雰囲気画像ではない）
- 画像だけ見て「結論」「背景」「実務アクション」または「気づき」が把握できること
- 視覚構造（悩み→気づき、Before/After、3ステップ、比較、因果フローなど）
- 具体要素（機能名、変化、実務効果、問い）
- 避けるもの（generic AI atmosphere, random laptop, decorative-only scene）

画像仕様:

- PNG
- 推奨サイズ: 正方形 `1024x1024`
- 5MB以下
- 保存先: `storage/images/<ID>.png`
- メイン見出しは投稿の結論・気づきを短く強く出す（例: `AIは止まる。だから備える`）
- サブ要素は3つまでに絞る（例: `気づく` / `切り替える` / `戻す`）
- 日本語テキストは短いラベル中心。長文は禁止。
- 年・日付・固有名詞・主要ラベルに誤記や強い文字化けがあれば不採用にして再生成する。

Threadsは投稿時に `raw.githubusercontent.com/.../main/storage/images/<ID>.png` をThreads APIへ渡す。したがって、画像は必ずcommit & push済みにする。

## 5. queueスクリプトでpendingに積む

本文を一時ファイルに保存し、必要なら画像プロンプトも一時ファイルに保存してから実行する。

```bash
python scripts/queue_image2_post.py \
  --post-id "<ID>" \
  --slot "<朝|昼|夜>" \
  --axis "<軸>" \
  --source "<一次ソースURLまたはタイトル>" \
  --image "storage/images/<ID>.png" \
  --text-file "/tmp/threads-post.txt" \
  --image-prompt-file "/tmp/threads-image-prompt.txt"
```

このスクリプトが検査するもの:

- ID形式
- 画像パスが `storage/images/<ID>.png`
- PNG実在、PNG形式、5MB以下
- Threads文字数
- 問いかけで締めていること
- 禁止語
- 同じslotがpendingに重複していないこと

## 6. 最終確認

```bash
git diff -- storage/stocks/pending.md
python scripts/queue_image2_post.py --help >/dev/null
```

`pending.md` に1件だけ追加され、画像ファイルが存在することを確認する。

## 7. commit & push

投稿はしない。GitHubへ積むだけ。

```bash
git add storage/stocks/pending.md storage/images/<ID>.png
git commit -m "queue: Threads <SLOT> image2 post <ID>"
git push origin main
```

GitHub Actionsが投稿時刻に `pending.md` を読み、`REQUIRE_IMAGE=1` で画像付き投稿する。投稿後はActionsが `posted.md` へ移動してcommitする。

## 失敗時

失敗したら本文だけを積まない。可能なら `storage/analytics/routine.log` に理由を追記してcommitする。

例:

```text
2026-06-17T18:45:00+09:00 [codex-image2-queue] skip: image2 generation failed for <ID>
```
