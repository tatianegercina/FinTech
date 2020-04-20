-- Query all fields from the table
SELECT *
FROM customer;

-- Query the data to return all the rows containing the name "Michael"
SELECT customer_id, first_name, last_name, age
FROM customer
WHERE first_name = 'Michael';

-- Update a single row to change the `first_name` and `age` column data
UPDATE customer
SET first_name = 'Brian', age = 20
WHERE customer_id = 5;

SELECT *
FROM customer;

-- Delete the duplicate "Alexander Martinez" entry using a unique id
DELETE FROM customer
WHERE customer_id = 6;

SELECT *
FROM customer;
