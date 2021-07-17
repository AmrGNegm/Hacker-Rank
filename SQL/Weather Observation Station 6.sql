/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/

SELECT DISTINCT CITY 
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]';


/*
Summary
Regular expressions use patterns to match strings.
Regex provides a way to query databases to find a smaller subset of data.
The POSIX comparators are:
~ : Case-sensitive, compares two statements, returns true if the first is contained in the second
~* : Case-insensitive, compares two statements, returns true if the first is contained in the second
!~ : Case-sensitive, compares two statements, returns false if the first is contained in the second
!~* : Case-insensitive, compares two statements, return false if the first is contained in the second

https://dataschool.com/how-to-teach-people-sql/how-regex-works-in-sql/
*/
