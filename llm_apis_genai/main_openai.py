import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")


question = input("Ask any question: ")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": "You a python teacher and programmer"},
        {"role": "user", "content": question},
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)


# for model in client.models.list():
#     print(model.id)
