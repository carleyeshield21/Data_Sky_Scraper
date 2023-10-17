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

