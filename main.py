import requests
import smtplib
import sqlite3

connection = sqlite3.connect('sample')
cursor = connection.cursor()

cursor.execute("SELECT * FROM roundtable WHERE knight = 'arthur'")
result = cursor.fetchall()
print(result)