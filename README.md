# Simple Code Reviewer

Google Gemini API を使用した Gradio ベースの AI チャットアプリケーション。

## 必要条件

- Python 3.10 以上
- [uv](https://github.com/astral-sh/uv)
- Google Cloud Gemini API キー

## セットアップと実行方法

1. uv を使用して依存関係をインストール:

```bash
uv sync
```

2. Gemini API キーの設定:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

3. アプリケーションの実行:

```bash
uv run src/app.py
```

アプリケーションが起動すると、ブラウザで自動的に Gradio のインターフェースが開きます。

## プロジェクト構成

```
.
├── src/
│   ├── app.py          # メインアプリケーション
│   ├── ai_response.py  # Gemini API 応答処理
│   └── mock_response.py # モックレスポンス処理
├── README.md
├── pyproject.toml      # 依存関係の定義
└── .python-version     # Python バージョン設定
```

## 機能

- マルチライン入力に対応したチャットインターフェース
- Google Gemini API を使用した AI 応答
- 日本語での対話に対応
- 使用例付き

## API キーの取得方法

1. [Google AI Studio](https://makersuite.google.com/app/apikey)にアクセス
2. API キーを作成
3. 作成した API キーを環境変数`GEMINI_API_KEY`に設定
