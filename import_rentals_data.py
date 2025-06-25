import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="rental_movie_store",
    user='postgres',
    password='*'
)

cur = conn.cursor()
rental_df = pd.read_csv("csv/rentals.csv").drop(columns='rental_id')
data_rental = rental_df.values.tolist()

cur.executemany("""insert into rentals (customer_id, movie_id, rental_date,return_date,price)
                values (%s, %s, %s, %s, %s)""", data_rental)

conn.commit()
print(f'{len(data_rental)} rows added to the rental table!')

cur.close()
conn.close()
