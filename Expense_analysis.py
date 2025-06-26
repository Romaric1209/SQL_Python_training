import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="Personal_Expenses_project",
    user="postgres",
    password="*"
)


## Total spent this month?
#############################################################################
#sqlite3
# spent_this_month_df = '''
#     SELECT SUM(amount) AS money_spent
#     FROM expenses
#     WHERE strftime('%Y-%m', date) == strftime('%Y-%m', 'now);'''

#postgres SQL
spent_this_month_query = '''
    SELECT SUM(amount) AS money_spent
    FROM expenses
    WHERE EXTRACT(year FROM date) = EXTRACT(year FROM now())
    AND EXTRACT(month FROM date) = EXTRACT(month FROM now());
    '''
spent_this_month_df = pd.read_sql(spent_this_month_query,conn)
print(spent_this_month_df)

# Top 3 categories this year?

top_3_cat_query = '''
    select
        c.name,
        COUNT(e.category_id) as quantity
    from categories c
    left join expenses e on c.category_id = e.category_id
    group by c.name
    order by quantity desc
    limit 3;
    '''
top_3_cat_df = pd.read_sql(top_3_cat_query,conn)
print(top_3_cat_df)


# Average monthly expenses?

avg_monthly_expense_query ='''
    select
        CAST(EXTRACT(YEAR FROM date) AS INTEGER)  AS year,
        CAST(EXTRACT(MONTH FROM date) AS INTEGER) AS month,
        ROUND(AVG(amount),2)
    from expenses
    group by year,month
    order by year,month desc;
'''
avg_monthly_expense_df = pd.read_sql(avg_monthly_expense_query,conn)
print(avg_monthly_expense_df)


# How does this month compare to last month?

diff_with_last_month_query = '''
with monthly_sums as (
	select
		sum(case when extract(year from date) = extract(year from now())
				and extract(month from date) = extract(month from now())
			then amount else 0
			end) as this_month,
		sum(case when extract(month from now()) != 1
				and extract(year from date) = extract(year from now())
				and extract(month from date) = extract(month from now())-1
			then amount
			when extract(month from now()) = 1
				and extract(year from date) = extract(year from now())-1
				and extract(month from date) = 12
			then amount else 0
		end) as last_month
		from expenses
)
select ROUND((this_month - last_month)) as difference_with_last_month
from monthly_sums;
'''
diff_with_last_month_df = pd.read_sql(diff_with_last_month_query,conn)
print(diff_with_last_month_df)

conn.close()
