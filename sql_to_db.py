
import sqlite3
conn = sqlite3.connect("Personal_Expenses_project.db")

cur = conn.cursor()
with open("Personal_Expenses_project.sql", "r") as f:
    sql_script = f.read()

cur.executescript(sql_script)
conn.commit()
conn.close()

print("Database created !")
