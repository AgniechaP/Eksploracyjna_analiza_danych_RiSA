import pandas as pd
import numpy as np
from pandasgui import show
import matplotlib.pyplot as plt

# Wczytanie dostarczonego pliku
df_population = pd.read_csv("population_by_country_2019_2020.csv", index_col=0)

# Wyswietlenie zawartosci w GUI
# show(df_population, settings={'block': True})

# Podsumowanie w konsoli
df_population_summary = df_population.describe()
print(df_population_summary)

# Bezwględna zmiana populacji
df_population["Net population change"] = df_population["Population (2020)"] - df_population["Population (2019)"]
print(df_population["Net population change"])
# Względna zmiana populacji
df_population["Population change [%]"] = (df_population["Net population change"]/df_population["Population (2019)"])
print(df_population["Population change [%]"])

# Sortowanie danych pod wzgledem wzglednej zmiany populacji
df_population.sort_values("Population change [%]",  axis=0, inplace=True, ascending=False)

min_population = df_population["Population change [%]"].min()
print(df_population[df_population["Population change [%]"] == min_population].index.values)

max_population = df_population["Net population change"].max()
print(df_population[df_population["Net population change"] == max_population].index.values)
#
df_population['Density (2020)'] = "Low"
df_population.loc[df_population["Population (2020)"] / df_population["Land Area (Km²)"] > 500, "Density (2020)"] = "High"
# df_population.loc[df_population["Population (2020)"] / df_population["Land Area (Km²)"] < 500, "Density (2020)"] = df_population["Population (2020)"] / df_population["Land Area (Km²)"]
high_density_count = (df_population["Density (2020)"] == "High").sum()
lowdensity_count = (df_population["Density (2020)"] == "Low").sum()

print('high density: ', high_density_count)
print('low density: ', lowdensity_count)

print(df_population)

most_population_change = df_population.filter(regex=r"Population \(20\d\d\)").iloc[:10, :]
print(most_population_change)
most_population_change.plot(kind='bar')
plt.show()

to_save = df_population.iloc[::2, :]
to_save.to_csv("population_output.csv")


