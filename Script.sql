--create table customers(
--	customer_id SERIAL primary key,
--	first_name VARCHAR(50),
--	last_name VARCHAR(50),
--	email VARCHAR(100) unique,
--	date DATE
--	);
----create table movies(
--	movie_id SERIAL primary key,
--	title VARCHAR,
--	genre VARCHAR(50),
--	duration_mins NUMERIC(3)
--	);
--create table rental(
--	rental_id SERIAL primary key,
--	curstomer_id integer references customers(customer_id),
--	movie_id integer references movies(movie_id),
--	rental_date DATE,
--	return_date DATE,
--	price NUMERIC(2,2)
--	);
--alter table customers rename column date to signup_date;
--insert into customers(customer_id,first_name,last_name,email,signup_date)
--VALUES
--	(1,'John','Doe','john@example.com','2023-01-12'),
--	(2,'Jane','Smith','jane@example.com','2023-03-15'),
--	(3,'Bob','Johnson','bob@example.com','2023-04-01'),
--	(4,'Alice','Wong','alice@example.com','2023-02-28'),
--	(5,'Charlie','Brown','charlie@example.com','2023-05-05'),
--	(6,'Eva','Martinez','eva@example.com','2023-06-01');
--insert into movies(movie_id,title,genre,duration_mins)
--values
--	(1,'The Matrix','Sci-Fi',136),
--	(2,'Finding Nemo','Animation',100),
--	(3,'Inception','Sci-Fi',148),
--	(4,'The Godfather','Crime',175),
--	(5,'Toy Story','Animation',81),
--	(6,'Titanic','Romance',195),
--	(7,'The Dark Knight','Action',152),
--	(8,'Shrek','Animation',90);

	