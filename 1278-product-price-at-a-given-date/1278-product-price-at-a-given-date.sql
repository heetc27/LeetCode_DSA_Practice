# Write your MySQL query statement below
SELECT T.product_id , COALESCE( P.new_price , 10 ) AS price 
FROM (
    SELECT product_id , MAX(
        CASE WHEN 
          STR_TO_DATE( change_date, '%Y-%m-%d') <= 
          STR_TO_DATE('2019-08-16', '%Y-%m-%d')
        THEN change_date END
    ) AS dt
    FROM Products
    GROUP BY product_id
) AS T 
LEFT JOIN Products P
ON P.product_id = T.product_id AND T.dt = P.change_date;