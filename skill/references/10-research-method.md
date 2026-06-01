# 10-research-method: Threads バズ調査の標準プロセス

このファイルは Threads の **バズパターン・トレンド・競合分析を行うときの標準プロセス** を定義する。
2026-05-27 のセッションで実証した方法を再利用可能な形に整理。

## 調査の目的別フロー

### A. 直近1週間のバズパターン調査

**目的**: ネタ仕入れ前に、いま実際に伸びている投稿の構造を把握する

**ステップ**:
1. WebSearch（英語・日本語混合、4-6クエリを並列）
2. grok-search（X 経由で日本語圏の Threads 言及を取得）
3. パターン抽出（複数ソースの共通項）
4. ひろ｜AI実業家への適用案

### B. 競合アカウント分析

**目的**: 同ニッチ（AI / Claude Code / 個人事業）の伸びてるアカウントの投稿構成を分析

**ステップ**:
1. grok-search で具体アカウント名（@kudooo_ai など）を深掘り
2. WebSearch でブログ・note 記事の二次分析
3. （権限あれば）公式 API でキーワード検索

### C. 自分の過去投稿のパターン抽出

**目的**: 自アカウントの伸びてるパターンを Claude Code に学習させる

**ステップ**:
1. `me/threads` で過去投稿取得（Threads API・既に動作）
2. インプレッション・エンゲージ取得（要権限）
3. Claude Code にパターン抽出依頼

## 利用可能な調査ツール

### 1. WebSearch（最も汎用）

**メリット**:
- 無料
- 即実行
- 複数クエリ並列可能（4-5本同時に投げられる）

**デメリット**:
- 二次情報中心（ブログ・分析記事経由）
- Threads 本体の生投稿は取れない

**良いクエリ例（英語）**:
```
"Threads viral posts examples late [month] [year]"
"Threads algorithm what type of post wins engagement"
"why do users use Threads vs Twitter behavior research [year]"
"Threads viral posts what makes them go viral case studies"
"Threads top creators [country] viral hook patterns"
```

**良いクエリ例（日本語）**:
```
"Threads 日本 バズ投稿 種類 構成 パターン [年]"
"Threads AI [製品名] バズ 日本語 [月] [年]"
"Threads 日本 フォロワー 増やし方 バズる 投稿 [月] [年]"
```

### 2. grok-search（Hermes 経由・X検索）

**メリット**:
- X 上の **実投稿** が取れる（URL・反応数つき）
- 日本語圏に強い
- within_time:7d などで期間絞り込み
- API課金なし（SuperGrok サブスク内）

**デメリット**:
- Threads 本体の投稿は直接取れない（X上の二次言及のみ）
- 件数は少なめ（10件前後）

**良いプロンプト例**:
```
直近1週間（within_time:7d）で、X(Twitter) 上で
『Threads でバズった』と言及されている日本語投稿、
または Threads でバズった日本語投稿そのものを紹介・分析している投稿を、
[ジャンル名] のテーマに絞って10件、URL付き・いいね数付きで教えて。
投稿者・投稿日も含めて。特に Threads でバズった投稿の構成・フック・
問いかけパターンを抽出したい。
```

### 3. Threads 公式 API（要権限）

**メリット**:
- 公式・無料
- リアルタイム
- レート制限 500クエリ/7日（十分）

**デメリット**:
- `threads_keyword_search` 権限が **App 単位で必要**（要申請・承認）
- 申請から承認まで数日〜数週間

**現状（2026-05-27 時点）**:
- atelierbase の App には未付与
- エラー: "Application does not have permission for this action" (code 10)

**取得済みエンドポイント（自分の投稿のみ）**:
- `GET /v1.0/me/threads` ✅ 自分の投稿リスト
- `GET /v1.0/me/threads_publishing_limit` ✅ 投稿制限残量

**権限申請の手順**:
1. https://developers.facebook.com/apps/ にアクセス
2. atelierbase の Threads アプリを選択
3. App settings → Permissions and Features
4. `threads_keyword_search` を Request
5. ビジネス利用目的を入力
6. 承認待ち

### 4. サードパーティスクレイピング（即実行・有料）

**サービス**:
- **Apify**: `futurizerush/threads-keyword-search` Actor。Pay-per-use
- **EnsembleData**: `/threads/keyword/search` エンドポイント。月額制
- **Bright Data**: スクレイピングサービス

**メリット**:
- 設定不要・即使える
- 公式 API より詳細なメトリクス取得可能

**デメリット**:
- 有料（数百円〜数千円/月）
- Meta 利用規約のグレーゾーン（法的にはhiQ判例で公開データのスクレイプは合法寄り）

**用途**:
- 公式 API 承認待ちの期間
- 競合の細かいエンゲ分析

### 5. Threads アプリでのユーザー手動共有

**手段**:
- ユーザーが Threads アプリで検索 → スクショ
- Claude に画像で共有 → 内容を文字起こし・パターン抽出

**メリット**:
- 完全合法・即実行
- 一次データ取得可能

**デメリット**:
- 手動・スケールしない

## 調査結果から抽出すべきもの

各バズ投稿を見るときの **チェックポイント**：

1. **フック（1行目）**: どんな型？
   - 数字スタート
   - 失敗開示
   - 「90%が知らない」型
   - 「実は」型
   - 個人的気づき

2. **構造**: シングルアイデアか、リスト型か、ストーリーか

3. **文字数**: 200-400字内か

4. **感情語**: 「悔しい」「びっくり」「迷った」の有無

5. **問いかけ**: 形式的か、意見対立を呼ぶ型か

6. **絵文字**: 何個・どんな種類

7. **エンゲージ**: いいね数より **リプライ数** が重要（Threads アルゴ的に）

## 調査結果の保存場所

調査結果は以下に蓄積（運用しながら更新）：

- 一時的なリサーチノート: `~/atlier-base-v1/projects/sns-auto-post/threads/storage/research/YYYY-MM-DD-research.md`
- 抽出されたパターン: `templates/voice-guide.md` の「良い例」セクション
- 競合アカウントメモ: `references/competitors.md`（必要に応じて新設）

## よくある失敗パターン

1. **WebSearch だけで満足する**
   → ブログ記事の二次情報になりがち。grok-search で実投稿も必ず見る

2. **英語クエリだけで調査する**
   → 日本語圏の Threads は別文化。日本語クエリも必ず混ぜる

3. **古い記事を「最新」と勘違いする**
   → 必ず「[year] 月」で期間絞り込み

4. **公式 API の権限不足で詰まる**
   → 即実行したいなら grok-search + WebSearch、長期は権限申請

5. **「90%が知らない」型に固執する**
   → 日本語圏 AI 系では「失敗→AI逆転型」「マイルストーン型」のほうが伸びる傾向（2026-05時点）

## 履歴

- v1（2026-05-27）: 初版（実証されたプロセスを記録）
