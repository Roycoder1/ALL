-- create table customer (
-- id serial primary key,
-- first_name varchar(100),
-- last_name varchar(100) not null
-- );
-- create table customerProfile(
-- id serial ,
-- isLoggedIn boolean default false,
-- primary key (id),
-- foreign key (id)references customer (id)
-- );
-- insert into customer(first_name,last_name)
-- values('John','Doe'),
-- ('Jerome','Lalu'),
-- ('Lea', 'Rive');
-- select * from customer
-- insert into customerProfile(isLoggedIn)
-- values (True),
-- (false),
-- (null);
-- select * from customerProfile
-- select p.first_name , f.isloggedin
-- from customer as p
-- join customerProfile as f
-- on p.id=f.id
-- where f.isloggedin = true

-- select p.first_name , f.isloggedin
-- from customer as p
-- join customerProfile as f
-- on p.id=f.id

-- select count(first_name)
-- from customer as p
-- join customerProfile as f
-- on p.id=f.id
-- where f.isloggedin != true

-- Part2:
-- create table Book(
-- book_id serial primary key,
-- title varchar (50)not null,
-- author varchar(50) not null
-- );
-- insert into Book(title,author)
-- values('Alice In Wonderland', 'J.K Rowling'),
-- ('To kill a mockingbird','Harper Lee');
-- select * from Book

-- create table student (
-- student_id serial primary key,
-- name varchar(100) not null unique ,
-- age smallint check(age< 15)
-- );
-- insert into student(name, age)
-- values('John', 12),
-- ('Lera' ,11 ),
-- ('Patrick', 10),
-- ('Bob',14);
-- select * from student

-- create table Library(
-- book_fk_id int,
-- student_id int ,
-- borrowed_date date,
-- primary key (book_fk_id,student_id),
-- foreign key (book_fk_id) references Book(book_id)ON DELETE CASCADE ON UPDATE CASCADE,
-- foreign key (student_id) references student (student_id)ON DELETE CASCADE ON UPDATE CASCADE
-- select * FROM STUDENT
-- select * from Book
-- );
-- insert into Library(book_fk_id,student_id,borrowed_date)
-- values((select book_id  from Book where title ='Alice In Wonderland'),(select student_id from student where name = 'John'),'2022-02-15'),
-- ((select book_id from Book where title = 'To kill a mockingbird'),(select student_id from student where name ='Lera' ),'2021-03-03'),
-- ((select book_id  from Book where title ='Alice In Wonderland'),(select student_id from student where name = 'Patrick'),'2021-05-23'),
-- ((select book_id from Book where title = 'To kill a mockingbird'),(select student_id from student where name ='Bob'),'2021-08-12');
-- select 	* FROM LIBRARY
-- select *
-- from library as d 
-- inner join Book as p on p.book_id = d.book_fk_id
-- inner join student as f on f.student_id = d.student_id;

-- select avg (f.age)
-- from library as d 
-- inner join Book as p on p.book_id = d.book_fk_id
-- inner join student as f on f.student_id = d.student_id
-- where title='Alice In Wonderland';

-- delete from student where name = 'Lera'
-- select * from student
select *
from library as d 
inner join Book as p on p.book_id = d.book_fk_id
inner join student as f on f.student_id = d.student_id;
-- It removed it from the child table


