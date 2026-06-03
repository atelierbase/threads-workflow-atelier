---
name: threads-post-now
description: Threads（@atelierbase_own / ひろ｜AI実業家）の「発火時にその場で1本生成して即配信」スキル。現在のスロット(朝/昼/夜)向けに researcher→writer で1本だけ生成し、自己チェックを通ってから pending.md に追記して commit & push する。push をトリガーに GitHub Actions が送信する（在庫レス・直投稿）。クラウドRoutineが定時に無人実行する用。トリガー：「Threadsを1本投稿」「threads-post-now」または /threads-post-now。
---

# threads-post-now — Threads 直投稿（在庫レス・無人）

このスキルは Threads アカウント @atelierbase_own（「ひろ｜AI実業家」/ 屋号 Atelier Base）の**直投稿マシン**。Threads は**共感のプラットフォーム**。
**クラウドRoutineが各スロットの時刻ちょうどに発火**して、このスキルを呼ぶ。
やることは「**今この瞬間のスロット用に1本だけ生成 → 自己チェック → pending.md に追記 → commit & push**」まで。

> **役割分担（重要）**
> - **このスキル（Routine側・正確な時計）＝生成だけ**。APIキーは持たない・投稿API は叩かない。
> - **送信は GitHub Actions（Secrets保持）**。pending.md への push をトリガーに Actions が投稿する。
> - だから「在庫(pending)」は溜めない。pending.md は **1件だけ積んで即送られて消える受け渡し場所**。
> - 旧 `threads-refill`（在庫補充）は使わない。配信タイマーは GitHub cron ではなく **このRoutine**。

## 完全無人の原則
- 途中で人間に承認を求めない（クラウド実行・止まると失敗扱い）
- **自己チェックに通らない投稿は push しない**（在庫という緩衝材が無いぶん、ここが唯一の安全網）。生成し直して2回ダメなら、その回は**何も投稿せず** `storage/analytics/routine.log` に理由を残して正常終了する（事故るより1本落とす方がマシ）

## 設定
| キー | 値 | 意味 |
|---|---|---|
| CHAR_RANGE | 200-400字（上限500字） | Threads 最適 |
| 生成本数 | 1 | このスロット用に1本だけ |
| 投稿タイプ | 単発 / コメント仕込み | **画像付きは禁止**（公開URL添付に commit が要り、配信時に間に合わないため） |

## 手順

### Step 0. 現在のスロットを決める
JST の現在時刻から判定する（Routine が正しい時刻に発火している前提）：
- **6:00–10:59 → 朝**
- **11:00–14:59 → 昼**
- **それ以外 → 夜**

`bash` が使えるなら `TZ=Asia/Tokyo date +%H` で時を取り、上の境界で `SLOT`（朝/昼/夜）を決める。

### Step 1. Researcher（ネタ仕入れ）
**`researcher` サブエージェントが使えるなら Task で委譲**、無ければメインが直接実行。
`skill/agents/researcher.md` に従い、**WebSearch のみ**で**直近1週間**の海外 Claude Code / Codex 情報を収集し、**Threads特性（共感・気づき・失敗成功に接続できるもの）で選別** → このスロットに最適な**ネタを1つ**選ぶ（発表時期を必ず確認）。

### Step 2. Writer（投稿生成・1本）
**`writer` サブエージェントが使えるなら Task で委譲**、無ければメインが直接実行。
書く前に必ず読む：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md` / `skill/references/02-generate.md`
- **`storage/analytics/learnings.md`**（効くルールを毎回反映＝学習の複利）

このスロット向けに**1本だけ**生成。**Threads鉄則**：
- **必ず問いかけで締める**／「私の体験」主役＋最新情報セット
- 一人称「私」／絵文字1個・多様化／**200-400字（最大500字）**
- 投稿タイプは `単発` を基本、たまに `コメント仕込み`（出典URLはセルフリプライのコメントへ）。**画像付きは作らない**。

### Step 3. 自己チェック（在庫の代わりの安全網・必須）
生成した文面が次を**すべて満たすか**自分で確認する。1つでもNGなら Step 2 に戻って作り直す（最大2回）：
- [ ] 200-400字（最大500字）。コメント仕込みなら各セグメントも500字以内
- [ ] **問いかけで締めている**
- [ ] 一人称「私」・絵文字1個まで・共感/対話トーン
- [ ] **禁止語が無い**：本名「石井」/「ミライ塾」/「アトリエの店主」/ その他個人特定
- [ ] **直近1週間のフレッシュなネタ**で、事実が一次ソースと矛盾しない（憶測で断定しない）
- 2回作り直してもNG → **push せず** routine.log に `skip: <理由>` を残して正常終了。

### Step 4. pending.md へ1件追記
`storage/stocks/pending.md` の末尾に**1件だけ**追記（既存は消さない。基本ヘッダのみで空のはず）。フォーマット厳守：

```
## {ID}
- 種類: 単発
- 投稿想定時刻: {SLOT}（自動・直投稿）
- 想定日: {YYYY-MM-DD（曜）}
- 軸: {軸/カテゴリ}
- ソース: {一次ソースURL}
- 文面:

{本文（問いかけで締める）}

- ステータス: pending

---
```

- **ID** は `YYYY-MM-DD-NNN`。NNN は **朝=701 / 昼=702 / 夜=703** 固定（日付プレフィックスで一意になるので衝突しない）。
- `投稿想定時刻:` の値は先頭が `朝`/`昼`/`夜` で始まること（送信側が前方一致で拾う）。
- コメント仕込みの場合は本文ブロック内で `--- コメント1 ---` 区切りを使う（writer.md 準拠）。

### Step 5. ログ → commit & push
1. `storage/analytics/routine.log` に `YYYY-MM-DD HH:MM JST | post {SLOT} | {ID}` を追記
2. コミットして push：
   ```
   git add -A
   git commit -m "post: generate {SLOT} {ID}"
   git push
   ```
   - **コミットメッセージに `[skip-send]` を絶対に入れない**（入れると送信ワークフローがスキップする）。
   - この push が GitHub Actions（送信専用ワークフロー）を起動し、Actions が pending の1件を Threads に投稿して posted.md に移す。

## チェックリスト（push 前）
- [ ] 生成は**1本だけ**・現在のスロット向け・問いかけで締めた
- [ ] Step 3 の自己チェック全項目クリア（NGなら push しない）
- [ ] 画像付きにしていない
- [ ] pending.md のフォーマットのキーが崩れていない
- [ ] routine.log を更新した
- [ ] コミットメッセージに `[skip-send]` が**入っていない**
