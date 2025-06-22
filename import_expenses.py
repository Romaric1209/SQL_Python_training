import pandas as pd
import sqlite3

conn = sqlite3.connect("Personal_Expenses_project.db")
df = pd.read_csv("csv/expenses.csv")
cur = conn.cursor()

columns = ['user_id', 'amount', 'date', 'category_id', 'description']
data = df[columns].values.tolist()

cur.executemany("INSERT INTO expenses (user_id, amount, date, category_id, description) VALUES(?, ?, ?,  ?, ?)", data)
conn.commit()
print(f'{len(data)} rows added to the expenses table.')
conn.close()
