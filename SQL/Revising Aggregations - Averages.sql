/*
Query the average population of all cities in CITY where District is California.
*/

SELECT AVG(population)
from CITY
where District = 'California';
