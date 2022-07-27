-- create table product_orders (
-- id_item serial primary key,
-- items varchar(100),
-- id_order serial,
-- command_date date
-- );
-- create table items(
-- id_item serial primary key,
-- price float,
-- foreign key (id_item) references product_orders(id_item)
-- );
-- insert into product_orders (items,command_date)
-- values ('Bougie de hannouca','2012-04-14'),
-- ('table' , '2021-07-12'),
--  ('cigars', '2017-08-23');
--  insert into items (price )
--  values(250),
--  (34),
--  (543);
-- select *
-- from product_orders as f
-- inner join items as e 
-- on f.id_item = e.id_item

select sum(e.price)
from product_orders as f
inner join items as e 
on f.id_item = e.id_item

-- create function sum_order(sum(price))
-- returns price from items as sum_order
-- begin 
-- return (select sum(e.price)
-- from product_orders as f
-- inner join items as e 
-- on f.id_item = e.id_item)
-- end;