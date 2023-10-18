import json

import requests
import pandas as pd

read_hdf = pd.read_hdf('pokedex_history.hdf5')
pokedex = pd.DataFrame(read_hdf)
pokedex["name"] = pokedex["name"].str.lower()

pokemons_names_from_api = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000")
pokemons_names_from_api = json.loads(pokemons_names_from_api.text)
names = [name["name"] for name in pokemons_names_from_api["results"]]
# print(names)

for name in pokedex['name']:
    if name in names:
        pokemon_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        file = open("pokemon_example.txt", "w")
        file.write(pokemon_data.text)
        file.close()
        pokemon_data = json.loads(pokemon_data.text)
        for stat in pokemon_data["stats"]:
            pokedex.loc[pokedex["name"] == name, stat["stat"]["name"]] = stat["base_stat"]

        if len(pokemon_data["types"]) == 1:
            pokedex.loc[pokedex["name"] == name, "type_1"] = pokemon_data["types"][0]["type"]["name"]
            pokedex.loc[pokedex["name"] == name, "type_2"] = None
            pokedex["type_1"] = pokedex["type_1"].astype(str)
            pokedex["type_2"] = pokedex["type_2"].astype(str)
        elif len(pokemon_data["types"]) == 2:
            pokedex.loc[pokedex["name"] == name, "type_1"] = pokemon_data["types"][0]["type"]["name"]
            pokedex.loc[pokedex["name"] == name, "type_2"] = pokemon_data["types"][1]["type"]["name"]
            pokedex["type_1"] = pokedex["type_1"].astype(str)
            pokedex["type_2"] = pokedex["type_2"].astype(str)