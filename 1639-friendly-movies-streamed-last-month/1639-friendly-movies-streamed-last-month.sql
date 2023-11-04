# Write your MySQL query statement below
SELECT DISTINCT c.title FROM Content c JOIN TVProgram t 
ON t.content_id = c.content_id 
WHERE c.Kids_content = 'Y' AND c.content_type = 'Movies' AND MONTH(t.program_date) = '06'
AND YEAR(t.program_date) = '2020'