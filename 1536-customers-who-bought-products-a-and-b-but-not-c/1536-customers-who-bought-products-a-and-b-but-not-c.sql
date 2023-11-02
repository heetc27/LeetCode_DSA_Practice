# Write your MySQL query statement below
SELECT Customers.customer_id, customer_name FROM Customers JOIN Orders 
ON Customers.customer_id = Orders.customer_id
WHERE (Orders.product_name = 'A')
INTERSECT DISTINCT
SELECT Customers.customer_id, customer_name FROM Customers JOIN Orders 
ON Customers.customer_id = Orders.customer_id
WHERE (Orders.product_name = 'B')
EXCEPT
SELECT Customers.customer_id, customer_name FROM Customers JOIN Orders 
ON Customers.customer_id = Orders.customer_id
WHERE (Orders.product_name = 'C')
