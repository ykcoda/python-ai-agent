from httpxx.main import HttpService
import asyncio
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"
client = HttpService(url=url, timeout=2)

data = asyncio.run(client.get_request())
if data:
    json_data = json.loads(data)
    print(json_data["hourly"])
