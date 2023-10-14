import requests
# in config.py there is api_key saved and not pushed to GitHub
import config
import json

# Brief of data
# req = requests.get(f"https://jug.dpieczynski.pl/lab-ead/_resources/lab_02/ow.dump.json")
# print(req.text)

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.api_key
latitude = 37.2431
longitude = -115.7930
req = requests.get(f"{url}?lat={latitude}&lon={longitude}&exclude=minutely&appid={api_key}")
print(req.text)

# Saving to json
with open("weather_forecast.json", "w") as outfile:
    json.dump(req.text, outfile)