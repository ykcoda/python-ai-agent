from math import e
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


question = input("Ask any question: ")

client = OpenAI(api_key=openai_api_key)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"developer", "content":"You are football expect"},
        {"role":"user", "content":question}
    ],
    stream=True
)

# print(response.choices[0].message.content)

for chuck in stream:
    print(chuck.choices[0].delta.content, end="", flush=True)