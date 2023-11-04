# # Write your MySQL query statement below
SELECT e.employee_id FROM Employees e LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE s.salary is NULL OR s.employee_id is NULL
UNION
SELECT s.employee_id FROM Employees e RIGHT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE e.employee_id is NULL OR e.name is NULL
ORDER BY employee_id

# SELECT * FROM Employees e RIGHT JOIN Salaries s
# ON e.employee_id = s.employee_id