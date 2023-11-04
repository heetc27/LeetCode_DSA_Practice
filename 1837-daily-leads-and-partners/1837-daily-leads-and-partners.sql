# Write your MySQL query statement below
SELECT  d1.date_id, d1.make_name, COUNT(DISTINCT d1.lead_id) AS unique_leads, COUNT(DISTINCT d1.partner_id) AS unique_partners
FROM DailySales d1
GROUP BY d1.date_id, d1.make_name