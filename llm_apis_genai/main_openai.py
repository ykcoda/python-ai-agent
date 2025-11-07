import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")


question = input("Ask any question: ")

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": "You a python teacher and programmer"},
        {"role": "user", "content": question},
    ],
    stream=True,  # this enables streaming
)

# to get streams out
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")


# print(response.choices[0].message.content)


# for model in client.models.list():
#     print(model.id)
