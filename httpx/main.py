import httpx
from pprint import pprint  # noqa
import asyncio
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def get_weather_info():
    url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.json()
        except httpx.RequestError as e:
            logging.error(f"{e}")
        except httpx.HTTPError as e:
            logging.error(f"{e}")
        except Exception as e:
            logging.error(f"{e}")


data = asyncio.run(get_weather_info())
pprint(data["hourly"]["temperature_2m"])
