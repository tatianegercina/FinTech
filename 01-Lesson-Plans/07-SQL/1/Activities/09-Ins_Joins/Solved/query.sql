
-- Check data import
SELECT *
FROM mortgage;

SELECT *
FROM sales;

-- Perform an INNER JOIN on the two tables
SELECT * 
FROM mortgage
INNER JOIN sales ON mortgage.mortgage_id = sales.mortgage_id;

-- Alternative solution:
-- Perform an INNER JOIN on the two tables
SELECT a.*, b.*
FROM mortgage as a
INNER JOIN sales as b ON a.mortgage_id = b.mortgage_id;

-- Perform a LEFT join
SELECT *
FROM mortgage as a
LEFT JOIN sales as b ON a.mortgage_id = b.mortgage_id;