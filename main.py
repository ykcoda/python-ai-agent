# PROJECT: USING A CLASS DEFINITION TO INTERACT WITH OPENAI API
from openai import OpenAI
from dotenv import load_dotenv
import os
import logging
import json


load_dotenv()
api_key = os.getenv("API_KEY")


#############################################
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="./chat-bot/logs.txt",
    level=logging.INFO,
)
#############################################
# Class Blueprint:
# - API Key Attribute: Store the API key for Authentication
# ask() Method: Sends User messages to the OpenAI and retrieves responses
# Model and Temperature Attributes: Allows control over the model type and response randomness


class ChatBot:

    # initialize with api_key, model and temperature
    def __init__(self, api_key, model="gpt-4o", temperature=0.5):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.response_file = "./chat-bot/responses.txt"
        self.json_file = "./chat-bot/responses.json"

    # make call to openai api
    def ask(self, user_message):
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": user_message},
                ],
                temperature=self.temperature,
            )
            logging.info(f"{user_message}")
            return response.choices[0].message.content
        except Exception as e:
            logging(f"{e}")

    # save openai response to file
    def save_response_to_file(self, response: str):
        try:
            with open(self.response_file, "a") as file:
                file.write(f"{response}\n")
                logging.info(f"Response written to: {self.response_file}")
        except Exception as e:
            logging.error(f"{e}")

    # load conversation history
    def load_convertion_history(self):
        try:
            with open(self.response_file) as file:
                logging.info("Conversation history retrieved....")
                return file.read()
        except Exception as e:
            logging.error(f"{e}")

    # export response to json
    def export_to_json(self, question, response):
        try:

            if os.path.exists(self.json_file):

                with open(self.json_file, "r") as file:
                    data = json.load(file)
            else:
                data = []

            data.append({"question": question, "message": response})

            with open(self.json_file, "w") as file:
                json.dump(data, file, indent=4)
                logging.info("Response exported as json")
        except Exception as e:
            logging.error(f"{e}")


# create a chat that queries openai chatgpt model
bot = ChatBot(api_key=api_key, temperature=0.7)

# question to send to api
question = input("Ask anything: ")
response = bot.ask(question)

# save response to a file
bot.save_response_to_file(response)

# retrieve conversation history
convo_history = bot.load_convertion_history()

bot.export_to_json(question, response)
# 1 ** Save responses to a File ---- DONE
# 2 ** Load conversation History ---- DONE
# 3 ** Log errors to a file --- DONE
# 4 ** Enable contextual conversation
# 5 ** Export responses to json --- DONE
# 6 ** Integrate with external API (eg weather etc..)
