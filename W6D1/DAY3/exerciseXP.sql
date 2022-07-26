-- Get a list of all film languages.
-- select p.film_id,p.title,d.name
-- from film as p
-- inner join language as d
-- on p.language_id = d.language_id
-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:

-- Get all films, even if they don’t have languages.
-- select p.film_id,p.title,p.description , d.name
-- from film as p
-- full join language as d
-- on p.language_id = d.language_id

-- Get all languages, even if there are no films in those languages.
-- select p.film_id,p.title,d.name
-- from film as p
-- right join language as d
-- on p.film_id = d.language_id


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- create table new_film (
-- id serial primary key,
-- name varchar(100)
-- );
-- insert into new_film(name)
-- values('Terminator'),
-- ('Impossible mission'),
-- ('Titanic');
-- select * from new_film


-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- create table customer_review(
-- review_id serial  primary key not NULL,
-- film_id int , 
-- language_id smallint,
-- title varchar(50),
-- score smallint,
-- review_text varchar,
-- last_update date,
-- foreign key (review_id) references new_film(id) on delete cascade
-- )
-- insert into customer_review(film_id,language_id,title,score,review_text,last_update)
-- values (1 , 1,'Terminator',8, 'A wonderful movie that will passionate you','2022-06-01'),
-- (2,1,'Shark is high',4,'The history of a baby shark that want to become the king sharks by controling telekinesis','2021-06-01'),
-- (3 ,2,'Titanic',6, 'The history of a sacrifice to save an old woman sat on his chair','2012-04-01');

-- select * from customer_review


-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.



-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- delete from new_film where name = 'Terminator'
-- select * from customer_review
-- It removed terminator from the child table too


-- Exercise 2 DVD RENTAL

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- UPDATE film set language_id= 1 where film_id < 50

-- select p.film_id,p.title,d.name
-- from film as p
-- inner join language as d
-- on p.language_id = d.language_id

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- The foreign key are defines as the foreign key of new_film. It doesnt affect the parent table 

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- DROP TABLE customer_review
-- select * from customer_review, its an easy step and just a select all from customer_review is enough to check that is not existing

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- select count(*) from rental where return_date is null
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- select p.amount,d.customer_id,d.return_date
-- from payment as p
-- inner join rental as d
-- on p.customer_id = d.customer_id
-- and return_date is null
-- order by amount desc limit 30

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- select d.title,d.description,g.first_name , g.last_name
-- from (film_actor as p join actor as g on p.actor_id = g.actor_id)
-- full join film as d
-- on p.film_id = d.film_id
-- where d.description ilike '%sumo%' and g.first_name ilike 'penelope' and g.last_name ilike 'monroe'
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- select p.film_id,p.title,p.description,d.name,p.length , p.rating
-- from (category as d join film_category as g on d.category_id = g.category_id)
-- full join film as p
-- on p.film_id = g.film_id
-- where rating = 'R' and length <60 and d.name = 'Documentary'


-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- select p.first_name, p.last_name , d.return_date ,g.amount
-- from (rental as d join payment as g on d.rental_id = g.rental_id)
-- full join customer as p
-- on p.customer_id = g.customer_id
-- where g.amount>4 and p.first_name ilike 'matthew' and d.return_date between '2005-07-28' and '2005-08-01'
-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select d.first_name, d.last_name ,g.amount,p.description,p.title,s.return_date
from customer as d
full join payment as g on d.customer_id = g.customer_id
full join rental as s on g.rental_id = s.rental_id
full join inventory as h  on s.inventory_id = h.inventory_id
full join film as p on h.film_id = p.film_id
where d.first_name ilike 'Matthew'and p.description ilike '%boat%' and amount >5


