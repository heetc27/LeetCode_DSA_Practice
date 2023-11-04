# Write your MySQL query statement below
SELECT DISTINCT page_id AS recommended_page FROM 
Friendship JOIN Likes 
ON 
Friendship.user2_id = Likes.user_id
WHERE Friendship.user1_id = '1' 
UNION
SELECT DISTINCT page_id AS recommended_page FROM 
Friendship JOIN Likes 
ON 
Friendship.user1_id = Likes.user_id
WHERE Friendship.user2_id = '1' 
EXCEPT
SELECT page_id FROM Likes WHERE user_id = '1' 