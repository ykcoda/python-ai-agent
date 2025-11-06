# Project: Making an API Request to OpenAPI
import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Give me the most interesting question you have ever been asked.",
        },
    ],
    "temperature": 0.7,
}


response = httpx.post(url=url, headers=headers, json=data)
if response.status_code == 200:
    result = response.json()
    pretty_json = json.dumps(result, indent=4)
    print(pretty_json)
    print("\n")
    reply = result["choices"][0]["message"]["content"]

    print(reply)
else:
    print(response.status_code, response.text)
