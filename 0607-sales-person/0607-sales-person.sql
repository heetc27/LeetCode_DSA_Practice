# Write your MySQL query statement below
SELECT s.name 
FROM SalesPerson s
where s.name not in 
    (SELECT s.name 
    FROM SalesPerson s
    LEFT JOIN Orders o ON s.sales_id = o.sales_id
    LEFT JOIN Company c ON c.com_id  = o.com_id 
  WHERE c.name = 'RED')

