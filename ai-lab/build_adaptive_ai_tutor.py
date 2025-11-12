from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded successfully...")
print(openai_api_key[:8])

client = OpenAI(api_key=openai_api_key)


