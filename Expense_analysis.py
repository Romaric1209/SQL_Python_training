import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="Personal_Expenses_project",
    user="postgres",
    password="berger"
)

#Import expenses.csv
df = pd.read_csv("csv/expenses.csv")
cur = conn.cursor()

columns = ['user_id', 'amount', 'date', 'category_id', 'description']
data = df[columns].values.tolist()

cur.executemany("INSERT INTO expenses (user_id, amount, date, category_id, description) VALUES(?, ?, ?,  ?, ?)", data)
conn.commit()
print(f'{len(data)} rows added to the expenses table.')
conn.close()

## Total spent this month?
#############################################################################
#sqlite3
# spent_this_month_df = ''' 
#     SELECT SUM(amount) AS money_spent
#     FROM expenses
#     WHERE strftime('%Y-%m', date) == strftime('%Y-%m', 'now);''' 

#postgres SQL
spent_this_month_df = ''' 
    SELECT SUM(amount) AS money_spent
    FROM expenses
    WHERE EXTRACT(year FROM date) = EXTRACT(year FROM now())
    AND EXTRACT(month FROM date) = EXTRACT(month FROM now());
    '''

print(spent_this_month_df) 

# Top 3 categories this year?

# Average monthly expenses?

# How does this month compare to last month?
