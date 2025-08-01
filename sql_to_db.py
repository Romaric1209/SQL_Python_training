
import sqlite3
conn = sqlite3.connect("Personal_Expenses_project.db")

cur = conn.cursor()
with open("Personal_Expenses_project.sql", "r") as f:
    sql_script = f.read()

cur.executescript(sql_script)
conn.commit()
conn.close()

print("Database created !")


import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Personal_Expenses_project",
    user="postgres",
    password="*"
)

cur = conn.cursor()

users_df = pd.read_csv("csv/users.csv")
data_users = users_df.values.tolist()


expenses_df = pd.read_csv("csv/expenses.csv")
data_expenses = expenses_df.values.tolist()
#### In the line below, I DID NOT FORGOT the SERIAL when creating users and expenses id columns, so I shouldn't add it in the export
# cur.executemany("INSERT INTO expenses (user_id, amount, date, category_id, description) VALUES(?, ?, ?,  ?, ?)", data) <-- ? SQL lite

cur.executemany("INSERT INTO users (user_id, name, email) VALUES (%s, %s, %s)", data_users) #<-- %s PostgreSQL
cur.executemany("INSERT INTO expenses (expenses_id, user_id, amount, date, category_id, description) VALUES (%s, %s, %s, %s, %s, %s)", data_expenses)

conn.commit()
print(f'{len(data_users)} rows added to the users table.')
print(f'{len(data_expenses)} rows added to the expenses table.')
conn.close()
