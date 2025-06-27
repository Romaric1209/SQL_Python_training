import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="rental_movie_store",
    user="postgres",
    password="*"
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
order by total_rental_spent desc;
'''
top_3c_df = pd.read_sql(top_3_customers_query, conn)
print(top_3c_df)

# Which movie genres are the most popular by number of rentals?
top_genres_query = '''select
m.genre as genre,
sum(r.movie_id) as count
from movies m
left join rentals r on m.movie_id = r.movie_id
group by genre
order by count desc
limit 3;'''
top_genre_df = pd.read_sql(top_genres_query,conn)
print(top_genre_df)

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

conn.commit()
conn.close()
