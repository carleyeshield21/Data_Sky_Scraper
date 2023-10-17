import requests
import smtplib
import sqlite3

connection = sqlite3.connect('sample')
cursor = connection.cursor()

# Selecting all rows
cursor.execute("SELECT * FROM roundtable")
result = cursor.fetchall()
print(result)

# Selecting with specific values
cursor.execute("SELECT * FROM roundtable WHERE knight = 'lancelot'")
result = cursor.fetchall()
print(result)

# Inserting new rows
neurow = [('perceival', 245), ('matahoti', 790)]
cursor.executemany("INSERT INTO roundtable VALUES(?, ?)", neurow)
connection.commit()