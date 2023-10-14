# in config.py there is api_key saved and not pushed to GitHub
import config
import requests
import json
import pandas as pd

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.api_key
# latitude and longitude of Bydgoszcz
latitude = 53.123482
longitude = 18.008438
# &units=metric - changing temperature from Fahrenheit to Celsius
req = requests.get(f"{url}?lat={latitude}&lon={longitude}&exclude=minutely&appid={api_key}&units=metric")
# print(req.text)
bydgoszcz_weather_json = json.loads(req.text)
weather_dict = {
    'temp': [],
    'feels_like': [],
    'humidity': [],
    'wind_speed': []
}
dt = []
for line in bydgoszcz_weather_json["hourly"]:
    dt.append(pd.to_datetime(line['dt'], unit='s'))
    weather_dict['temp'].append((line['temp']))
    weather_dict['feels_like'].append((line['feels_like']))
    weather_dict['humidity'].append((line['humidity']))
    weather_dict['wind_speed'].append((line['wind_speed']))

df = pd.DataFrame(data=weather_dict, index=dt)
print(df)