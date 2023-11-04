# Write your MySQL query statement below
# Write your MySQL query statement below
select t1.sale_date, t1.sold_num - t2.sold_num as diff  from 
    (select sale_date, sold_num from sales 
    where fruit = "apples") as t1 
        inner join 
    (select sale_date, sold_num from sales 
    where fruit = "oranges") as t2 
on t1.sale_date = t2.sale_date 
order by t1.sale_date ;