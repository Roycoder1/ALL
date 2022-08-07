CREATE or REPLACE FUNCTION total_price(ui int) 
RETURNS float AS $$
declare
    total_sum float;
   
BEGIN
   total_sum := (select sum(price) from (select i.name, i.price, po.id 
		from items as i
		inner join 
		(select * from product_orders where user_id = ui) as po 
		on i.order_id = po.id) as t
		order by sum(price))
		;
   RETURN total_sum;
   
END;
$$ LANGUAGE plpgsql;



select * from total_price(1);