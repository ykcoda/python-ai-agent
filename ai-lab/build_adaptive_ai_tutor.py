from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded successfully...")
print(openai_api_key[:8])

client = OpenAI(api_key=openai_api_key)


def get_ai_tutor_response(user_qustion):
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
                {"role": "user", "content": user_qustion},
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occured: {e}")
        return f"Sorry, I encounted an error trying to get an answer: {e}"

ask_question = input("As you AI tutor a question: ")
print("")
print("AI is thinking......")
print("")
question = get_ai_tutor_response(ask_question)
print(question)