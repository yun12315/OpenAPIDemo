import requests

# Example for Claude 4.0 through laozhang.ai
response = requests.post(
    "https://api.laozhang.ai/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk-uFrGq0AZe5mrHIkS9d7d08166aD84c2cB813Aa20613966De",
        "Content-Type": "application/json"
    },
    json={
        "model": "gemini-2.5-pro-preview-05-06",
        "stream": False,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that provides concise answers."},
            {"role": "user", "content": "用一句话解释量子计算"}
        ],
        "max_tokens": 2048
    }
)

print(response.json())