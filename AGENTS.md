# AGENTS.md — Threads 直投稿ルーチン（Codex クラウド用・@atelierbase_own）

> **このファイルは Codex への指示書**（Codexクラウドルーチンが repo を clone するとこれを読む）。
> 役割：**発火時に「今のスロット用の投稿を1本」生成し、必ず image2 / GPT-Image で画像を作り、画像付きで Threads に投稿してリポジトリを更新する**。
> アカウント：**ひろ｜AI実業家**（Threads=@atelierbase_own / 屋号 Atelier Base）。Threads は**共感のプラットフォーム**。

このルーチンは**生成も送信もすべて Codex が行う**（Claude ルーチンは無効化済み）。Codex は image2 / GPT-Image で画像も作れるので、**毎回の画像付き投稿をこのルーチンだけで完結**させる。

> **2026-06-04 現在の運用方針**：毎日 **7:10 / 12:10 / 19:10 JST** の3スロットで1本ずつ投稿する。各発火は「現在スロットの1本」だけを扱い、**本文のみ投稿は禁止**。

---

## 0. 必要な認証（Codexクラウドの環境変数に設定。リポジトリには絶対に置かない）

| 環境変数 | 用途 |
|---|---|
| `THREADS_ACCESS_TOKEN` | Threads Graph API アクセストークン |
| `THREADS_USER_ID` | Threads ユーザーID |
| `OPENAI_API_KEY` | image2 / GPT-Image 画像生成（毎回必須） |

> **キーをコミットしない**（public repo）。Codexの環境変数で渡す。
> ローカル運用時の保管先は `~/.config/threads-workflow/threads-credentials.json`（クラウドでは環境変数を使う）。

依存：`pip install requests openai`（poster は requests、画像生成は openai を使う）。未導入ならルーチン内でインストールしてよい。

---

## 1. 今のスロットを決める
JST 現在時刻から：**6:00–10:59=朝 / 11:00–14:59=昼 / それ以外=夜**。
`TZ=Asia/Tokyo date +%H` で時を取り `SLOT`（朝/昼/夜）を決める。

## 2. 投稿文を生成（1本だけ・このスロット用・必ず画像付き）
書く前に必ず読む（このリポジトリ内）：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md` / `skill/references/02-generate.md`
- `storage/analytics/learnings.md`（効くルールを反映）
- 型は `skill/agents/writer.md`

ネタは **WebSearch等で直近1週間の海外 Claude Code / Codex 情報**を、**Threads特性（共感・気づき・失敗成功に接続）で選ぶ**。
**Threads鉄則：必ず問いかけで締める**／「私の体験」主役＋最新情報セット／一人称「私」／絵文字1個・多様化／**200-400字（最大500字）**／同カテゴリ連続を避ける。
投稿タイプは**常に `画像付き`**。必要に応じて、画像付きのまま `コメント仕込み` を組み合わせてよい（本文中で `--- コメント1 ---` 区切り）。画像は共感・気づきを補助するビジュアルにする。

## 3. image2 / GPT-Image で画像生成（必須）
1. 画像プロンプトを作り、**image2 / `gpt-image-1` のみ**で **PNG・正方形 `1024x1024`・5MB以下**を生成（文字は入れない／クリーンな構図）。Canva、HTML/CSS、SVG、ダミー画像、手作業合成は使わない。
2. 保存先＝**`storage/images/<投稿ID>.png`**（ファイル名は投稿IDと完全一致・小文字 `.png`）。
3. 本文ブロックに **`- 画像ファイル: storage/images/<投稿ID>.png`** 行を必ず入れる。
4. 画像が壊れていないこと、投稿内容と整合していること、5MB以下であることを確認する。
5. **⚠️ Threads は画像を公開URL（`raw.githubusercontent.com/.../main/storage/images/<ID>.png`）で添付する。**
   → **poster を実行する前に、画像を commit & push して main に上げておくこと**（未pushだとURLが404になり本文のみで配信される）：
   ```bash
   git add storage/images/<ID>.png && git commit -m "add image for <ID>" && git push
   ```
6. push 後、公開URLが `200` で取得できることを確認する：
   ```bash
   curl -I -L https://raw.githubusercontent.com/atelierbase/threads-workflow-atelier/main/storage/images/<ID>.png
   ```
7. 画像生成・保存・公開URL確認のいずれかに失敗した場合は**投稿しない**。本文のみ投稿で妥協しない。

## 4. pending.md に1件だけ追記
`storage/stocks/pending.md` 末尾に1件 append（フォーマット厳守。既存は消さない）：

```
## {ID}
- 種類: 画像付き
- 投稿想定時刻: {SLOT}（自動・直投稿）
- 想定日: {YYYY-MM-DD（曜）}
- 軸: {軸/カテゴリ}
- ソース: {一次ソースURL}
- 画像ファイル: storage/images/{ID}.png
- 文面:

{本文（必ず問いかけで締める）}

- ステータス: pending

---
```
- **ID** = `YYYY-MM-DD-NNN`、NNN は **朝=701 / 昼=702 / 夜=703**。
- `投稿想定時刻:` は先頭が `朝`/`昼`/`夜`。
- 画像付きコメント仕込みにする場合も `種類` は `画像付き` のままにし、本文ブロック内で `--- コメント1 ---` 区切りを使う。

## 5. 自己チェック（必須・在庫が無いぶんの唯一の安全網）
全部満たすか確認。1つでもNGなら §2 へ戻って作り直す（最大2回）：
- [ ] 200-400字（最大500字）。コメント仕込みは各セグメントも500字以内
- [ ] **問いかけで締めている**
- [ ] 一人称「私」／絵文字1個まで／共感・対話トーン
- [ ] **禁止語なし**：本名「石井」「ミライ塾」「アトリエの店主」その他個人特定
- [ ] 直近1週間のフレッシュネタ・一次ソースと矛盾しない
- [ ] `種類: 画像付き` で、`画像ファイル` 行があり、PNGが実在する
- [ ] 画像が壊れていない・本文と整合・5MB以下
- [ ] 画像は poster 実行前に push 済みで、raw.githubusercontent.com の公開URLが `200`
- 2回ダメ → **投稿せず** `storage/analytics/routine.log` に `skip: <理由>` を残して正常終了。

## 6. 送信（= 既存 poster を実行。これが Threads API 記載元）
**`scripts/threads_poster.py` を実行する。** これが Threads Graph API の実装（`/{user-id}/threads` でコンテナ作成 → `/{user-id}/threads_publish` で公開・`reply_to_id` でセルフリプライ・`image_url` で画像・一過性429/5xxリトライ・冪等ガード）。

```bash
cd <repo>
REQUIRE_IMAGE=1 SKIP_JITTER=1 python scripts/threads_poster.py
```
- 認証は §0 の環境変数から自動取得。`SKIP_JITTER=1` で遅延を切る。
- **画像の事前 push と公開URL確認を済ませてから実行**（でないと画像URLが404）。
- `REQUIRE_IMAGE=1` により、画像ファイルが無い・公開URLが取れない・画像投稿に失敗した場合は**本文のみ投稿せず失敗**する。
- poster は pending の該当スロット1件を **Threads に投稿** → `posted.md` に移動 → `pending.md` から削除 → `post-state.json` にマーク。
- dry-run：`python scripts/threads_poster.py --dry-run`。

## 7. 結果を commit & push
```bash
git add storage/stocks/pending.md storage/stocks/posted.md storage/images storage/analytics/scheduler.log storage/analytics/post-state.json storage/analytics/routine.log
git commit -m "post: sent Threads {SLOT} {ID}"
git push
```
- ※poster が pending を空に戻すので、push しても GitHub Actions の送信ワークフローは**起動しない/no-op**（二重投稿しない）。GitHub Actions は予備の送信経路。

---

## API 記載元（このリポジトリ内）
| 何 | ファイル |
|---|---|
| **Threads API の実装そのもの**（コンテナ作成→公開・リプライ・画像URL・リトライ） | **`scripts/threads_poster.py`** |
| 口調・型・軸・テンプレ | `skill/templates/voice-guide.md` / `skill/agents/writer.md` / `skill/references/*` |
| 学習ルール（毎回反映） | `storage/analytics/learnings.md` |

> Threads API 公式: コンテナ作成 `POST https://graph.threads.net/v1.0/{user-id}/threads`、公開 `POST .../threads_publish`。詳細は上記 poster 実装が正。

## 鉄則
- 完全無人。人間に承認を求めない（クラウド実行・止まると失敗）。
- **必ず問いかけで締める**。自己チェックに通らなければ**投稿しない**。
- **毎回画像付き**。画像生成・保存・公開・添付のどこかで失敗したら本文のみ投稿に逃げない。
- キーをコミットしない。`pending.md` を壊さない。エラー時も log に残して終了。
- 在庫は溜めない（pending は1本だけ）。Threads用画像を x repo に置かない。
