# Write your MySQL query statement below
SELECT customer_id FROM Customer
GROUP BY customer_id
HAVING Count(distinct product_key) = (SELECT COUNT(product_key) FROM Product)

# SELECT customer_id, Count(distinct product_key) FROM Customer
# GROUP BY customer_id
