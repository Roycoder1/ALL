-- create table public(
-- items varchar,
-- price float
-- );
-- create table customer(
-- lName varchar,
-- Fname varchar
-- );
-- insert into customer(Fname,lName)
-- values('Greg','Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');
-- insert into public(items,price)
-- values('Small Desk' , 100),
-- ('Large desk' , 300),
-- ('Fan' , 80);
-- select * from customer
-- select * from public
-- select items  from public where price>80
-- select items  from public where  price <300
-- select lName from customer where lName = 'Smith'
-- select lName from customer where lName = 'Jones'
-- select * from customer WHERE Fname != 'Scott'

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)


-- select  items from public order by price asc
-- select  items from public where price >= 80 order by price desc
-- select Fname , lName from customer   order by Fname asc limit 3
select Fname , lName from customer   order by Lname desc limit 3
