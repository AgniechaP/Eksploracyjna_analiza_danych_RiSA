import requests
import json
import pandas as pd

req = requests.get("https://blockchain.info/ticker")  # wysłanie zapytania GET pod odpowiedni adres, zapisanie odpowiedzi
bitcoin_dict = json.loads(req.text)
df = pd.DataFrame.from_dict(bitcoin_dict, orient='index')
print(df)
