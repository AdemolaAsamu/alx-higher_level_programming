-- Displays the temperatur
SELECT city, AVR(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
