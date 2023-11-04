# Write your MySQL query statement below
# SELECT p.player_id, p.player_name, (COUNT(c.Wimbledon)+ COUNT(c.Fr_open)+ COUNT(c.US_open)+ COUNT(c.Au_open)) AS grand_slams_count
# FROM Players p, Championships c
# WHERE p.player_id IN (c.Wimbledon, c.Fr_open, US_open, c.Au_open)
# GROUP BY p.player_id

SELECT player_id, player_name, SUM(Wimbledon = player_id) + SUM(Fr_open = player_id) + SUM(US_open = player_id) + SUM(Au_open = player_id) AS grand_slams_count FROM Players, Championships
GROUP BY player_id
HAVING grand_slams_count != 0