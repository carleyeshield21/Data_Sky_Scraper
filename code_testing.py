import sqlite3
import pandas

dataframe = pandas.read_csv('Family Income and Expenditure.csv')
# print(dataframe.columns.values)

for index, item in enumerate(dataframe):
    print(f'Index {index}\n {item}')

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
    print(item[30])
    print('======')