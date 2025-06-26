import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="local",
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
