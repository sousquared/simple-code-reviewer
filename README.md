# Simple Code Reviewer

Google Gemini API を使用した Gradio ベースの AI チャットアプリケーション。

## 必要条件

- Python 3.10 以上
- [uv](https://github.com/astral-sh/uv)
- Google Cloud Platform プロジェクト
- Google Cloud Secret Manager に保存された Gemini API キー
- Docker (Docker を使用する場合)

## セットアップと実行方法

### 通常の実行方法

1. uv を使用して依存関係をインストール:

```bash
uv sync
```

2. 「API キーと設定方法」セクションの手順に従って、API の設定を行ってください。

3. アプリケーションの実行:

```bash
uv run src/app.py
```

### Docker を使用した実行方法

1. 「API キーと設定方法」セクションの手順に従って、Secret Manager の設定を行ってください。

2. Google Cloud 認証を設定:

   ```bash
   gcloud auth application-default login
   ```

3. Makefile を使用して Docker イメージをビルド:

```bash
make build
```

4. アプリケーションの実行:

```bash
make run
```

5. イメージの削除（必要な場合）:

```bash
make clean
```

アプリケーションが起動すると、ブラウザで自動的に Gradio のインターフェースが開きます（http://localhost:7860）。

## プロジェクト構成

```
.
├── src/
│   ├── app.py          # メインアプリケーション
│   └── response/       # レスポンス処理モジュール
│       ├── ai_response.py    # Gemini API 応答処理
│       └── mock_response.py  # モックレスポンス処理
├── README.md
├── pyproject.toml      # 依存関係の定義
└── .python-version     # Python バージョン設定
```

## 機能

- マルチライン入力に対応したチャットインターフェース
- Google Gemini API を使用した AI 応答
- 日本語での対話に対応
- 使用例付き

## API キーと設定方法

`src/config/settings.py` を開き、以下の設定を行ってください：

```python
# Google Cloud Platform のプロジェクトID
# GCPのコンソールで確認できるプロジェクトIDを設定
PROJECT_ID = "YOUR_GCP_PROJECT_ID"

# Secret Manager に保存された Gemini API キーのシークレットID
# Google Cloud Secret Manager で作成したシークレットのID
GEMINI_API_KEY_SECRET_ID = "YOUR_GEMINI_API_KEY_SECRET_ID"
```

## API キーの設定手順

1. [Google AI Studio](https://makersuite.google.com/app/apikey)にアクセスし、API キーを作成
2. [Google Cloud Console](https://console.cloud.google.com/)で Secret Manager を開く
3. 新しいシークレットを作成し、Gemini API キーを保存
   - シークレット ID を設定（例: "gemini-api-key"）
   - シークレットの値として Gemini API キーを以下の形式で設定:
     ```json
     {
       "api_key": "YOUR_GEMINI_API_KEY"
     }
     ```
4. `settings.py` の設定を更新
   - `PROJECT_ID` に GCP プロジェクト ID を設定
   - `GEMINI_API_KEY_SECRET_ID` に作成したシークレット ID を設定
