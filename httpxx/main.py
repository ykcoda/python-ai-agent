import httpx
import asyncio
import logging
import json
import os
from dotenv import load_dotenv

######################################################################################################
load_dotenv()
api_key = os.getenv("API_KEY")
######################################################################################################
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
######################################################################################################


class HttpService:
    """HttpService will accept a URL and make an API call."""

    def __init__(
        self,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        timeout: int = 5,
    ):
        """Accepts url and timeout"""
        self.url = url
        self.headers = headers
        self.data = data
        self.timeout = timeout

    async def get_request(self):
        """Make an asynchronous http get request and return: JSON"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url=self.url, headers=self.headers, timeout=self.timeout
                )
                response.raise_for_status()
                return json.dumps(response.json(), indent=4)
            except httpx.RequestError as e:
                logging.error(f"{e}")
            except httpx.HTTPError as e:
                logging.error(f"{e}")
            except Exception as e:
                logging.error(f"{e}")
            return None

    async def post_request(self):
        """Post an asynchronous http request"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url=self.url,
                    headers=self.headers,
                    json=self.data,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                logging.error(f"{e}")
            except httpx.HTTPError as e:
                logging.error(f"{e}")
            except Exception as e:
                logging.error(f"{e}")
            return None


if __name__ == "__main__":

    while True:
        try:
            question = input("Ask anything: ")

            url = "https://api.openai.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }

            data = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "developer", "content": "You are a heplful assistant."},
                    {"role": "user", "content": question},
                ],
                "temperature": 0.7,
            }

            http_client = HttpService(url=url, headers=headers, data=data, timeout=20)
            data = asyncio.run(http_client.post_request())

            if data:
                print(data["choices"][0]["message"]["content"])  # type: ignore
                print()
                print("#" * 110)
        except Exception as e:
            logging.error(f"{e}")
        except KeyboardInterrupt as e:
            logging.warning(f"You existed the app....! {e}")
