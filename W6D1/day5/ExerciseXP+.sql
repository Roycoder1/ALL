create table students(
id smallserial primary key,
first_name varchar,
last_name varchar,
birth_date date not null
);

-- DATE yyyy-mm-dd 

insert into students( first_name,last_name,birth_date)
values
('Marc', 'Benichou','1998-11-02'),
('Yoan','Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer','Simpson', '1980-10-03');

-- select * from students
insert into students(first_name,last_name,birth_date)
values('Roy','Benisti','1996-12-09');
-- select* from students
-- select * from students where first_name = 'Marc' and last_name = 'Benichou'
-- select * from students where first_name = 'Marc' or last_name = 'Benichou'
-- select * from students where first_name like '%a%'
-- select * from students where first_name like 'a%'
-- select * from students where first_name like '%a'
-- select * from students where first_name like 'Y%a%'
-- select * from students where id =1 or id = 3
select* from students where birth_date >= '2000-1-01'






