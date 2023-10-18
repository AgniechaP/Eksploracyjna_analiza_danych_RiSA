import sqlite3

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

conn = sqlite3.connect("Chinook_Sqlite.sqlite")  # połączenie do bazy danych - pliku
conn.row_factory = dict_factory

# for row in conn.execute('SELECT Album.Title AS title, Artist.Name AS artist FROM Album LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId'):
#     print(row)

i = 0
# for row in conn.execute('SELECT  Artist.Name AS artist, Album.Title AS title FROM Artist LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId'):
for row in conn.execute('SELECT  Artist.Name AS artist, Album.Title AS title FROM Album LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId'):
    print(row)
    i+=1
print(i)

conn.close()

# When we are left joining Album to Artist there sometimes are records such as {'artist': 'Whitesnake', 'title': None}, because artist exists but has no album in Album table