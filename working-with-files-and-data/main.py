import httpx
import json


url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = httpx.get(url)
    response.raise_for_status()
    post_data = json.loads(response.text)
    print(post_data[0]["title"])

    for item in post_data:
        print(item)

    print(post_data[0]["title"])


except httpx.RequestError as e:
    print(f"{e}")
except httpx.HTTPError as e:
    print(f"{e}")


response1 = {
    "usage": {
        "total_tokens": 1000,
        "details": {"prompt_tokens": 300, "completion_tokens": 700},
    },
    "choices": [
        {"text": "The capital of France is Paris", "index": 0},
        {"text": "France capital is Paris", "index": 1},
    ],
}

choice_text = [choice for choice in response1["choices"]]
print(choice_text)
