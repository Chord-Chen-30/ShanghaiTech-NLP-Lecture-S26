# Ref: https://openrouter.ai/docs/quickstart

import requests
import json
from dotenv import load_dotenv
import os
from rich import print as rprint
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "openai/gpt-oss-120b:free"
# MODEL_NAME = "qwen/qwen3.6-plus"


response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    data=json.dumps({
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": """介绍一下上海科技大学的李时珍老师，简短点。"""
            }
        ]
    })
)

rprint(response.json())
breakpoint()



response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    data=json.dumps({
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": """介绍一下上海科技大学的李时珍老师，简短点。"""
            },
            {
                "role": "assistant",
                "content": """李时珍老师是上海科技大学的一位教授，专注于中医药学的研究和教学。他在中医药领域有着丰富的经验和深厚的学术造诣，致力于推动中医药的发展和创新。"""
            },
            {
                "role": "user",
                "content": """你编的吧？我觉得不太对啊。"""
            }
        ]
    })
)
rprint(response.json())
breakpoint()


