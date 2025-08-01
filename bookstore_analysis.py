import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'bookstore',
    user = 'postgres',
    password = '*'
    )

cur = conn.cursor()

orders_df = pd.read_csv('csv/bookstore_orders.csv')
orders_data = orders_df.values.to_list()

cur.executemany("insert into orders (customer_id,book_id,quantity,order_date)values(%s,%s,%s,%s)", orders_data)
conn.commit()
print(f'{len(orders_data)} added to table.')
conn.close()
