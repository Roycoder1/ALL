create table public(
items varchar,
price float
);
create table customer(
lName varchar,
Fname varchar
);

insert into customer(Fname,lName)
values('Greg','Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');





insert into public(items,price)
values('Small Desk' , 100),
('Large desk' , 300),
('Fan' , 80);


-- select * from customer
-- select * from public
-- select items  from public where price>80
-- select items  from public where  price <300
-- select lName from customer where lName = 'Smith'
-- select lName from customer where lName = 'Jones'
select * from customer WHERE Fname != 'Scott'

