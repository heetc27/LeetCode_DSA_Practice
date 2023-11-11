# Write your MySQL query statement below
select b.customer_id, b.product_id, p.product_name
from (
    select customer_id, product_id, count(*) as ct
    from orders
    group by customer_id, product_id
    order by customer_id, product_id)b
join products p on p.product_id = b.product_id    
where (customer_id, ct) in (select customer_id,max(Ct)
                            from(
                                 select customer_id, product_id, count(*) as ct
                                 from orders
                                 group by customer_id, product_id
                                 order by customer_id, product_id) a
                                 group by customer_id)