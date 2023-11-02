# Write your MySQL query statement below
SELECT left_operand, operator, right_operand,
    CASE WHEN operator = '=' AND Vleft.value = Vright.value THEN 'true'
    WHEN operator = '>' AND Vleft.value > Vright.value THEN 'true'
    WHEN operator = '<' AND Vleft.value < Vright.value THEN 'true'
    ELSE 'false' 
    END AS value
FROM Expressions E
JOIN Variables Vleft
    ON E.left_operand = Vleft.name
JOIN Variables Vright
    ON E.right_operand = Vright.name
