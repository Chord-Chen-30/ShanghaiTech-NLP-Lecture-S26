from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

response = client.chat.completions.create(
    model="/path/to/weights",
    messages=[
        {"role": "user", "content": "你好，请简单介绍一下你自己。"}
    ],
    temperature=0.7,
    max_tokens=512
)

print(f"模型回复: {response.choices[0].message.content}")
