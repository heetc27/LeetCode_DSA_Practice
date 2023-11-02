SELECT S.seller_name
FROM Seller AS S
LEFT JOIN Orders AS O
ON S.seller_id = O.seller_id
AND YEAR(sale_date) = '2020'
WHERE O.seller_id IS NULL
ORDER BY seller_name