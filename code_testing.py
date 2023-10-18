import sqlite3

connection = sqlite3.connect('Fam_Inc_Exp_database')
cursor = connection.cursor()

# Selecting all rows
# cursor.execute("SELECT * FROM 'Family Income and Expenditure'")
# result = cursor.fetchall()
# print(result)

# Selecting with specific values
cursor.execute("SELECT * FROM 'Family Income and Expenditure' WHERE Region = 'CAR'")
result = cursor.fetchall()
for item in result:
    print(item[1])
    print('======')