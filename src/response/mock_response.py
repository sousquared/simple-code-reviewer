import time


def get_mock_response(message: str) -> str:
    """Get mock response for development and testing"""
    time.sleep(3)  # 3秒間スリープ

    if not message.strip():
        return "## エラー\nコードを入力してください。"

    # モックの応答パターン
    responses = {
        "def example_function": """## コードレビュー結果

### 改善点
1. 関数の目的が不明確です
2. 戻り値の型が指定されていません
3. テストが容易ではありません

### 改善案
```python
def example_function() -> None:
    \"\"\"この関数の目的を記述してください\"\"\"
    print('test')
```""",
        "if x > 0": """## コードレビュー結果

### 改善点
1. 変数のスコープが不明確です
2. エラーハンドリングがありません
3. マジックナンバーの使用

### 改善案
```python
def check_positive(value: int) -> bool:
    \"\"\"Check if the given value is positive\"\"\"
    return value > 0

x = 10
if check_positive(x):
    print('positive')
```""",
        "for i in data": """## コードレビュー結果

### 改善点
1. リストの型が不明確です
2. イテレータ変数名が意味を持っていません
3. 処理の目的が不明確です

### 改善案
```python
from typing import List

def print_numbers(numbers: List[int]) -> None:
    \"\"\"Print each number in the list\"\"\"
    for number in numbers:
        print(number)

data = [1, 2, 3]
print_numbers(data)
```""",
    }

    # 入力に特定のキーワードが含まれているか確認
    for key, response in responses.items():
        if key in message:
            return response

    return """## コードレビュー結果

### 一般的な改善提案
1. 型ヒントの追加を検討してください
2. 関数やクラスのドキュメントを追加してください
3. エラーハンドリングを考慮してください
4. テストのしやすさを意識してください

### 参考リソース
- [Python公式ドキュメント](https://docs.python.org/)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
"""
