# in config.py there is api_key saved and not pushed to GitHub
import config
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.api_key
# latitude and longitude of Bydgoszcz
latitude = 52.409538
longitude = 16.931992
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
    dt.append(pd.to_datetime(line['dt']+7200, unit='s'))
    weather_dict['temp'].append((line['temp']))
    weather_dict['feels_like'].append((line['feels_like']))
    weather_dict['humidity'].append((line['humidity']))
    weather_dict['wind_speed'].append((line['wind_speed']))

df = pd.DataFrame(data=weather_dict, index=dt)
print(df)
df.plot.line()
plt.show()

# zamiast json.loads mozna uzyc df = pd.DataFrame(req.json())

# df_krzychu=pd.DataFrame(index=np.arange(len(bydgoszcz_weather_json['hourly'])),data=bydgoszcz_weather_json['hourly'],columns=["temp", "feels_like", "humidity","wind_speed","dt"])