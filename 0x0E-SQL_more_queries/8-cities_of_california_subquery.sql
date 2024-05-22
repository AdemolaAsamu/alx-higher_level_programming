-- List all the cities of california that can be found in database
-- result may be sorted inascending order
SELECT id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
