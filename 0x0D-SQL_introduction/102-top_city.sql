-- displays top 3 cty temp during July and Aug ordered by temp in descending order

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
