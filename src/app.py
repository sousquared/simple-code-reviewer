import gradio as gr
from ai_response import get_ai_response, SYSTEM_PROMPT
from mock_response import get_mock_response

with gr.Blocks(
    title="AIコードレビュワー",
    css="""
    .orange-button {
        background-color: #FF6700 !important;
        border-color: #FF6700 !important;
        color: white !important;
    }
    .output-text {
        margin-top: 2em !important;
        margin-bottom: 2em !important;
    }
""",
) as demo:
    gr.Markdown("# AIコードレビュワー")

    with gr.Tabs():
        with gr.Tab("AI応答"):
            with gr.Column():
                gr.Markdown("### Gemini APIを使用したコードレビュー")
                gr.Markdown(
                    "環境変数 GEMINI_API_KEY に有効なAPIキーを設定してください。"
                )
                with gr.Accordion("システムプロンプトを編集", open=False):
                    system_prompt = gr.Textbox(
                        value=SYSTEM_PROMPT,
                        lines=15,
                        label="コードレビュワーの設定",
                        placeholder="コードレビュワーの役割や重視するポイントを指定できます",
                    )
                ai_input = gr.Textbox(
                    lines=5,
                    label="レビューしたいコードを入力してください",
                    placeholder="ここにコードを入力...",
                )
                ai_button = gr.Button(
                    "レビュー実行", variant="primary", elem_classes="orange-button"
                )
                ai_output = gr.Markdown(
                    label="レビュー結果", value="ここに結果が表示されます", elem_classes="output-text"
                )
                gr.Examples(
                    examples=[
                        ["def hello():\n    print('Hello, World!')"],
                        [
                            "class User:\n    def __init__(self, name):\n        self.name = name"
                        ],
                        ["def calculate_sum(numbers):\n    return sum(numbers)"],
                    ],
                    inputs=ai_input,
                )

        with gr.Tab("モック応答"):
            with gr.Column():
                gr.Markdown("### モックレビューを使用したテスト")
                gr.Markdown("開発とテスト用のモック応答です。APIキーは不要です。")
                mock_input = gr.Textbox(
                    lines=5,
                    label="レビューしたいコードを入力してください",
                    placeholder="ここにコードを入力...",
                )
                mock_button = gr.Button(
                    "レビュー実行", variant="primary", elem_classes="orange-button"
                )
                mock_output = gr.Markdown(
                    label="モックレビュー結果",
                    value="ここに結果が表示されます",
                    elem_classes="output-text",
                )
                gr.Examples(
                    examples=[
                        ["def example_function():\n    print('test')"],
                        ["x = 10\nif x > 0:\n    print('positive')"],
                        ["data = [1, 2, 3]\nfor i in data:\n    print(i)"],
                    ],
                    inputs=mock_input,
                )

    ai_button.click(
        get_ai_response,
        inputs=[ai_input, system_prompt],
        outputs=ai_output,
        show_progress="full",
    )
    mock_button.click(
        get_mock_response, inputs=mock_input, outputs=mock_output, show_progress="full"
    )

if __name__ == "__main__":
    demo.launch()
