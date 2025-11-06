import json
from pprint import pprint

with open("./sample.json", "r") as f:
    config = json.load(f)

print(config)

pretty_json = json.dumps(config, indent=4)
print(pretty_json)


print(config["model"])
