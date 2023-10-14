import sqlite3

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

conn = sqlite3.connect("Chinook_Sqlite.sqlite")  # połączenie do bazy danych - pliku
conn.row_factory = dict_factory

for row in conn.execute('SELECT Invoice.InvoiceId AS invoice, Invoice.CustomerId AS customer, Invoice.BillingCity AS city, Invoice.Total AS total FROM Invoice WHERE Invoice.BillingCountry = "USA" ORDER BY Invoice.BillingCity desc'):
    print(row)

conn.close()