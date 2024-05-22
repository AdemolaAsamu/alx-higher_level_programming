-- This identifies pairs twins and lists
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
