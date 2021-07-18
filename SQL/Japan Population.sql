/*
Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
*/

SELECT SUM(population)
from CITY
where COUNTRYCODE = 'JPN';
