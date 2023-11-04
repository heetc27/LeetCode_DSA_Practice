# Write your MySQL query statement below
SELECT co.name AS country FROM Person p LEFT JOIN 
Country co ON
SUBSTRING(p.phone_number, 1, 3) = co.country_code
JOIN
calls c
ON p.id IN (c.caller_id, c.callee_id)
GROUP BY co.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM calls)