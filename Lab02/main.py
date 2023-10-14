# Returning a tuple - original behaviour of sqlite in Python
import sqlite3
conn = sqlite3.connect("Chinook_Sqlite.sqlite")  # połączenie do bazy danych - pliku
c = conn.cursor()

for row in c.execute('SELECT Invoice.InvoiceId, Invoice.CustomerId, Invoice.BillingCity, Invoice.Total FROM Invoice WHERE Invoice.BillingCountry = "USA" ORDER BY Invoice.BillingCity desc'):
    print(row)

conn.close()