import json
import requests
import pandas as pd
import sqlite3

pokedex_history = pd.read_hdf('pokedex_history.hdf5')


def collect_data_of_pokemons(data):
    pokemon_names = data['name'].str.lower()
    # print(pokemon_names)

    pokemon_from_api = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    pokemon_from_api = json.loads(pokemon_from_api.text)
    pokemon_names_from_api = [name["name"] for name in pokemon_from_api["results"]]
    pokemon_names_and_urls = [(data["name"], data["url"]) for data in pokemon_from_api["results"]]

    pokemon_data = []
    pokemon_types = []
    type_1 = None
    type_2 = None

    for name in pokemon_names:
        if name in [data[0] for data in pokemon_names_and_urls]:
            url = [data[1] for data in pokemon_names_and_urls if data[0] == name][0]
            # print(f"Name: {name}, URL: {url}")
            pokemon_stats_from_api = requests.get(f"{url}")
            pokemon_stats_from_api = json.loads(pokemon_stats_from_api.text)

            for types in pokemon_stats_from_api["types"]:
                type_name = types["type"]["name"]
                if types["slot"] == 1:
                    type_1 = type_name
                if types["slot"] == 2:
                    type_2 = type_name

            for statistic in pokemon_stats_from_api["stats"]:
                stat_name = statistic["stat"]["name"]
                base_stat = statistic["base_stat"]
                # print(f"Base stat: {base_stat}, Name: {stat_name}")
                pokemon_data.append([name, stat_name, base_stat])
                pokemon_types.append([name, type_1, type_2])

    pokemon_data_df = pd.DataFrame(pokemon_data, columns=["Name", "Stat Name", "Base Stat"])
    # print(pokemon_data_df)
    pokemon_data_pivot = pd.pivot_table(pokemon_data_df, values='Base Stat', columns='Stat Name', index='Name',
                                        fill_value=None)
    pokemon_data_pivot.reset_index(inplace=True)
    # print(pokemon_data_pivot)

    pokemon_types_df = pd.DataFrame(pokemon_types, columns=["Name", "type_1", "type_2"])
    pokemon_types_df_unique = pokemon_types_df.drop_duplicates(subset=['Name', 'type_1'])
    # pokemon_types_df_unique.reset_index(drop=True, inplace=True)
    # print(pokemon_types_df_unique)

    merged_data = pokemon_data_pivot.merge(pokemon_types_df_unique[['Name', 'type_1', 'type_2']], on='Name', how='left')
    # Displaying all columns not "..."
    pd.set_option('display.max_columns', None)
    # print(merged_data)

    # Merging data_against_table
    conn = sqlite3.connect("pokemon_against.sqlite")
    c = conn.cursor()
    query = f'SELECT * FROM against_stats'
    data_against_table = c.execute(query)
    headers = [header[0] for header in data_against_table.description]
    data_against_df = pd.DataFrame(data=data_against_table, columns=headers)
    data_against_df['name'] = data_against_df["name"].str.lower()
    # Add against_ columns to already merged table
    merged_data_with_additional_columns = merged_data.merge(data_against_df, left_on='Name', right_on='name',
                                                            how='left')
    return merged_data_with_additional_columns


# attacker power = attack + special_attack + against_{type1} + against_{type2}
# attacked power = defense + special_defense + hp
def attack_against(attacker: str, attacked: str, database: pd.DataFrame):
    attacker_row = database.loc[database['Name'] == attacker]
    attacked_row = database.loc[database['Name'] == attacked]
    if attacker_row.empty or attacked_row.empty:
        return None

    attacked_type_1 = attacked_row.iloc[0]['type_1']
    attacked_type_2 = attacked_row.iloc[0]['type_2']

    attacker_attack = attacker_row['attack'].values[0]
    attacker_special_attack = attacker_row['special-attack'].values[0]
    attacker_against_type_1 = attacker_row[f'against_{attacked_type_1}'].values[0]
    attacker_hp = attacker_row['hp'].values[0]
    if attacked_row.iloc[0]['type_2'] is not None:
        attacker_against_type_2 = attacker_row[f'against_{attacked_type_2}'].values[0]
        attacker_sum = attacker_attack + attacker_special_attack + attacker_against_type_1 + attacker_against_type_2 + attacker_hp
    else:
        attacker_sum = attacker_attack + attacker_special_attack + attacker_against_type_1 + attacker_hp

    attacked_defense = attacked_row['defense'].values[0]
    attacked_special_defense = attacked_row['special-defense'].values[0]
    attacked_hp = attacked_row['hp'].values[0]
    attacked_sum = attacked_defense + attacked_special_defense + attacked_hp

    if attacker_sum > attacked_sum:
        print(f"{attacker} points: {attacker_sum}, {attacked} points: {attacked_sum}, {attacker} wins")
    elif attacked_sum > attacker_sum:
        print(f"{attacker} points: {attacker_sum}, {attacked} points: {attacked_sum}, {attacked} wins")
    elif attacked_sum == attacker_sum:
        print(f"{attacker} points: {attacker_sum}, {attacked} points: {attacked_sum}, It's a draw!")



def main():
    attack_against('klang', 'wingull', collect_data_of_pokemons(pokedex_history))

    # Show whole data of met pokemons
    # print(collect_data_of_pokemons(pokedex_history))


if __name__ == "__main__":
    main()
