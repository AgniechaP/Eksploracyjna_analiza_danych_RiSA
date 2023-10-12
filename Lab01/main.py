import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasgui import show

num_days = 20
temperature = np.random.uniform(20, 28, size=(num_days, 1))
pressure = np.random.uniform(990, 1010, size=(num_days, 1))
rain = np.random.uniform(0, 20, size=(num_days, 1))
random_data = np.hstack((temperature, pressure, rain))
df_weather = pd.DataFrame(index=pd.date_range("20200501", periods=num_days, freq="1D"),
                          data=random_data, columns=["Temperature", "Pressure", "Rain"])

# print(df_weather)
# df_weather.plot()
# plt.show()
# show(df_weather, settings={'block': True})

# print(df_weather.filter(regex='P')) # Kolumna z literą P
# print(df_weather.filter(regex='\w{5,}'))

# Wybor wierszy
print(df_weather.index) # klucz, po nim mozna filtrowac kolumny

print(df_weather.loc['2020-05-09', ['Temperature', 'Rain']]) # loc zaklada, ze podaje nazwy indeksow i nazwy kolumn lub ,: gdy chce wszytskie

# mozemy tez iloc uzyc - wybor wierszy po ich numerze (0 do -1)
print(df_weather.iloc[0, :]) # zostanie wybrany pierwszy wiersz, w ilocu nie mozemy podawac nazw, wiec przy kolumnach tez liczby a nie po nazwie
print(df_weather.iloc[:10,: ])  #pierwsze 10 wierszy

# Chce znalezc dni gdzie temp byla wieksza niz 10 stopni (ich liczbe, jak wyswietle bez sum() to bedzie series True + daty)
print((df_weather['Temperature']>10).sum())
print(df_weather['Temperature']>10)


# Dataframe tabela zawierajaca wiecej niz 1 kolumne, gdy zawiera jedna kolumne to jest to series

view_df = df_weather.loc[df_weather['Temperature']>21, ['Temperature', 'Pressure']] # Referencja do pewnego widoku, nie jest to kopia, wiec bedzie to mialo wplyw na oryginalny dataset

df_weather.loc[df_weather['Temperature']<21, ['Temperature', 'Pressure']] = 0

df_weather['Temperature']*2-100 #operacja dla kazdego elementu osobno zostanie przeprowadzona

# Dodatkowa kolumna
df_weather['WIndex'] = df_weather['Temperature'] + df_weather['Pressure']

sub_set = df_weather.iloc[-10:,:].copy() # teraz pracujac na sub_set bo to kopia nie bedziemy zmieniac oryginalu

print(df_weather.describe())

# Kolumna indeksu moze miec swoja nazwe
df_weather.index.name = 'Date'

# Reset indeksu
df_weather.reset_index(['Temperature']) # Stary indeks jest nadpisywany

print(df_weather)

