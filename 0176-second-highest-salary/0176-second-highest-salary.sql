# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary FROM Employee 
WHERE salary <> (SELECT max(salary) FROM employee)