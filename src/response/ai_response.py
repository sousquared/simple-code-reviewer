import google.generativeai as genai

from client.secret_manager import get_secret
from config.settings import PROJECT_ID, GEMINI_API_KEY_SECRET_ID

# システムプロンプト
SYSTEM_PROMPT = """あなたはコードレビュワーです。返信は日本語で返してください。
あなたの目的は、非常に経験豊富なソフトウェアエンジニアとして機能し、コードの一部を徹底的にレビューし、
以下のような観点で改善するためのコードスニペットを提案することです：
- コードの品質と可読性
- コードのシンプルさ
- パフォーマンスの最適化
- セキュリティの脆弱性
- ベストプラクティスの適用
- エラーハンドリングの改善
- テスタビリティの向上
- ドキュメンテーションの充実
- コードの再利用性と保守性
- ベストプラクティス: DRY, SOLID, KISS, YAGNI
些細なコードスタイルの問題や、コメント・ドキュメントの欠落についてはコメントしないでください。
重要な問題を特定し、解決して全体的なコード品質を向上させることを目指してください。
細かい問題は意図的に無視してください。
"""

# Geminiの設定
api_key = get_secret(project_id=PROJECT_ID, secret_id=GEMINI_API_KEY_SECRET_ID)
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_ai_response(message: str, system_prompt: str = SYSTEM_PROMPT) -> str:
    """Get response from Gemini AI"""
    try:
        if not message.strip():
            return "メッセージを入力してください"

        # システムプロンプトとユーザーの入力を組み合わせる
        prompt = f"{system_prompt}\n\nユーザー: {message}\n\n応答:"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"エラーが発生しました: {str(e)}\nAPI KEYが正しく設定されているか確認してください"
