import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
os.getenv("OPENAI_API_KEY")

question = input("Ask and question: ")

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": ""},
        {"role": "user", "content": question},
    ],
)


print(response.choices[0].message.content)
