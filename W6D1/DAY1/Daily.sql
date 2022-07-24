create table actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);
insert into actors(actor_id,first_name,last_name,age,number_oscars)
values
(1,'Gal', 'Gadot',23,2),
(2,'Nataly', 'Portman',34,4);
-- select * from actors
insert into actors(actor_id,first_name,last_name,age,number_oscars)
values
(3,'Jean', 'Dujardin',46,2),
(4,'Gerard', 'Depardieu',68,4),
(5,'Francois', 'Damiens',43,1);
-- select * from actors
-- select count(first_name) from actors
insert into actors(actor_id,first_name,last_name,age,number_oscars) VALUES (NULL,NULL,NULL,NULL,NULL) 
-- creating an error



