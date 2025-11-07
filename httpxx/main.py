import httpx
import asyncio
import logging
import json
from typing import Dict, Any

######################################################################################################
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
######################################################################################################


class HttpService:
    """HttpService will accept a URL and make an API call."""

    def __init__(self, url, timeout=5):
        """Accepts url and timeout"""
        self.url = url
        self.timeout = timeout

    @property
    async def make_http_request(self):
        """Make an asynchronous http request and returns a json"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url=self.url, timeout=self.timeout)
                response.raise_for_status()
                return json.dumps(response.json(), indent=4)
            except httpx.RequestError as e:
                logging.error(f"{e}")
            except httpx.HTTPError as e:
                logging.error(f"{e}")
            except Exception as e:
                logging.error(f"{e}")
            return None


if __name__ == "__main__":
    url = "https://api.open-meteo.com/v1/fore?latitude=35&longitude=139&hourly=temperature_2m"
    http_client = HttpService(url)
    data = asyncio.run(http_client.make_http_request)
    if data:
        print(data)
