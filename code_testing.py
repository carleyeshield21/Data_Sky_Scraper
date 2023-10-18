import sqlite3

connection = sqlite3.connect('Fam_Inc_Exp_database')
cursor = connection.cursor()

# Selecting all rows
cursor.execute("SELECT * FROM 'Family Income and Expenditure'")
result = cursor.fetchall()
print(result)