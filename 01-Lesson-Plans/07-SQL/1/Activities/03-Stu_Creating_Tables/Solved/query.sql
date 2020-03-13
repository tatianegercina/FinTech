-- View the table data
SELECT *
FROM states;

-- Use a query to view only the state_name
SELECT state_name
FROM states;

-- Bonus 1:
-- Create a query to view cities in Arizona
SELECT city, state
FROM cities
WHERE state = 'Arizona';

-- Bonus 2:
-- Create a query to view cities and states
-- with a population less than 100,000
SELECT *
FROM cities
WHERE population < 100000;

-- Bonus 3:
-- Create a query to view the city in California
-- with a population of less than 100,000
SELECT *
FROM cities
WHERE population < 100000
AND state = 'California';
