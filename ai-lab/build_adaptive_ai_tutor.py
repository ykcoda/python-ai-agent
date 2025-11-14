from asyncio import streams
from dis import Instruction
from cgitb import text
import sched
import sre_parse
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded successfully...")
print(openai_api_key[:8])

client = OpenAI(api_key=openai_api_key)


def get_ai_tutor_response(user_question):
    """
    send a question to the OpenAI API, asking it to respond as an AI Tutor.

    Args:
        user_question (str): The question asked by the user

    Returns:
        str: The AI's response, or an error message
    """
    system_prompt = "You are a helpful and patient AI Tutor. Explain concepts clearly and concisely."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question},
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occured: {e}")
        return f"Sorry, I encounted an error trying to get an answer: {e}"


explanation_level = {
    1: "like I'm 5 years old",
    2: "like I'm 10 years old",
    3: "like a high school student",
    4: "like a colledge student",
    5: "like an expert in the field",
}


def get_ai_tutor_stream(user_question, explanation_level_value):
    level_description = explanation_level.get(
        explanation_level_value, "clearly and concisely"
    )

    system_prompt = (
        f"You are a helpful and patient AI Tutor. Explain concepts {level_description}."
    )
    print(f"DEBUG: Using system prompt: '{system_prompt}'")

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question},
            ],
            temperature=0.7,
            stream=True,
        )

        full_response = ""

        for chunk in stream:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                text_chunk = chunk.choices[0].delta.content
                full_response += text_chunk
                yield full_response

    except Exception as e:
        print(f"An error occured during streaming: {e}")
        yield f"Sorry, I encounted an error: {e}"


if __name__ == "__main__":
    ask_question = input("As you AI tutor a question: ")
    print("AI is thinking......")
    print("")
    stream = get_ai_tutor_stream(ask_question)
    print(stream, end="", flush=True)
