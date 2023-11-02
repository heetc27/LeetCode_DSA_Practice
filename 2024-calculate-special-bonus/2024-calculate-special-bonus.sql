# Write your MySQL query statement below
SELECT employee_id, 
    CASE WHEN name LIKE "M%" OR NOT(employee_id % 2 != 0) THEN salary = 0 ELSE salary
    END AS bonus
FROM Employees
ORDER BY employee_id;