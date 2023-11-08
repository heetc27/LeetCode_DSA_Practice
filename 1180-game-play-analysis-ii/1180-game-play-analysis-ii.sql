# Write your MySQL query statement below
select player_id, device_id from activity 
WHERE (player_id, event_date ) IN (
    SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id)
