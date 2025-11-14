from openai import OpenAI
from dotenv import load_dotenv
import os

from requests.utils import stream_decode_response_unicode


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f"API_KEY: {OPENAI_API_KEY[:5]} loaded successfully")

print("Load OpenAI API")
client = OpenAI(api_key=OPENAI_API_KEY)


def talk_to_openai(client, question):

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You an IT Expect."},
                {"role": "user", "content": question},
            ],
            stream=True
        )
        return stream
    except Exception as e: 
        print(f"Error: {e}")




stream = talk_to_openai(client, input("Ask anything: "))

for chunk in stream: 
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
