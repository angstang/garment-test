from google import genai
from google.genai.types import HttpOptions
import sys

PROJECT_ID = "gcp-lab-ai"
LOCATION = "global"
MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """你现在是服装研发经理助理。
请使用中文回答。
输出要求：
1. 结论先行
2. 结构清晰
3. 尽量贴近服装研发、打样、工艺、版型、面辅料、项目管理场景
4. 如适合，按“核心问题 / 风险点 / 待确认项 / 建议动作”输出
"""

def build_prompt(user_text: str) -> str:
    return f"{SYSTEM_PROMPT}\n\n用户问题：\n{user_text}"

def main():
    if len(sys.argv) < 2:
        print("用法：python3 askai.py \"你的问题\"")
        return

    user_text = sys.argv[1]

    client = genai.Client(
        vertexai=True,
        project=PROJECT_ID,
        location=LOCATION,
        http_options=HttpOptions(api_version="v1"),
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=build_prompt(user_text),
    )

    print(response.text)

if __name__ == "__main__":
    main()
