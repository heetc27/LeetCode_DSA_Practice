# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) as tiv_2016 FROM
(SELECT * FROM Insurance 
GROUP BY lat,lon 
HAVING COUNT(lat) = 1 and COUNT(lon)=1
AND 
tiv_2015 IN (SELECT tiv_2015 FROM Insurance 
GROUP BY tiv_2015 
HAVING COUNT(tiv_2015)>1)) as table1;