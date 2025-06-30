import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="rental_movie_store",
    user="postgres",
    password="berger"
)

# 🧩 Business Problems to Solve:
# Who are the top 3 customers by total rental spend?

# Which movie genres are the most popular by number of rentals?

# What is the average rental duration per genre?

# Which customers have not rented anything in the past 30 days?

# Which movie has the highest return rate (rented the most times)?
###################################################################
# Who are the top 3 customers by total rental spend?
top_3_customers_query = '''select
sum(r.price) as total_rental_spent,
c.first_name ||' '|| c.last_name as name
from rentals r
left join customers c on r.customer_id = c.customer_id
group by r.customer_id, name
order by total_rental_spent desc
limit 3;
'''
top_3c_df = pd.read_sql(top_3_customers_query, conn)
print(top_3c_df)

plt.figure(figsize=(8, 5))
plt.bar(top_3c_df['name'], top_3c_df['total_rental_spent'], color='skyblue')
plt.title("Top 3 Customers by Rental Spend", fontsize=14, fontweight='bold')
plt.xlabel("Customer Name")
plt.ylabel("Total Rental Spent")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Which movie genres are the most popular by number of rentals?
top_genres_query = '''select
m.genre as genre,
sum(r.movie_id) as count
from movies m
left join rentals r on m.movie_id = r.movie_id
group by genre
order by count desc
limit 3;'''
top_genres_df = pd.read_sql(top_genres_query,conn)
print(top_genres_df)

# What is the average rental duration per genre?
avg_rental_duration_query = '''with rental_duration as(
select
	r.movie_id,
	extract(epoch from (r.return_date::timestamp - r.rental_date::timestamp)) / 86400 as duration_days
from rentals r
where r.return_date is not null
)
select
m.genre,
round(avg(rd.duration_days),2) as average_rental_duration
from rental_duration rd
left join movies m on rd.movie_id = m.movie_id
group by m.genre
order by average_rental_duration desc;
'''
avg_rental_duration_df = pd.read_sql(avg_rental_duration_query,conn)
print(avg_rental_duration_df)

# Which customers have not rented anything in the past 30 days?
#'2024-07-15' I am going to use it as reference date, otherwise, is I use now, no one rented for over a year!
who_doesnt_rent_query = '''
WITH rental_durations AS (
    SELECT
        c.first_name || ' ' || c.last_name AS full_name,
        extract(epoch FROM ('2024-07-15'::timestamp - r.rental_date::timestamp)) / 86400 AS duration_days
    FROM customers c
    LEFT JOIN rentals r ON c.customer_id = r.customer_id
)
SELECT *
FROM rental_durations
WHERE duration_days > 30;
'''
who_doesnt_rent_df = pd.read_sql(who_doesnt_rent_query,conn)
print(who_doesnt_rent_df)

# Which movie has the highest return rate (rented the most times)?
best_renting_query='''
select m.title, sum(r.movie_id) as number_of_rent
from movies m
left join rentals r on m.movie_id = r.movie_id
group by m.title
order by number_of_rent desc
limit 1;
'''
best_renting_df = pd.read_sql(best_renting_query,conn)
print(best_renting_df)

conn.commit()
conn.close()
