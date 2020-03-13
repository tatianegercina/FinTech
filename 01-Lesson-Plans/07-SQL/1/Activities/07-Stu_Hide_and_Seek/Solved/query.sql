-- Drop table if exists
DROP TABLE customer;

-- Create table and view column datatypes
CREATE TABLE customer (
   first_name VARCHAR(30) NOT NULL,
   last_name VARCHAR(30),
   gender VARCHAR(30),
   age INT,
   address VARCHAR(50),
   city VARCHAR(50),
   state CHAR(2),
   zip_code CHAR(5)
);

SELECT *
FROM wordassociation;

-- Collect all rows with the word "stone" in the "word1" column
SELECT *
FROM wordassociation
WHERE word1 = 'stone';

-- Collect all rows where the author is within the 0-10 range
SELECT *
FROM wordassociation
WHERE
	author >= 1
	AND author <= 10;

-- Search for the word "pie" in both "word1" and "word2" columns
SELECT *
FROM wordassociation
WHERE
	word1 = 'pie'
	OR word2 = 'pie';

-- BONUS
-- Select all rows with a source of "BC"
SELECT *
FROM wordassociation
WHERE source = 'BC';

-- Collect all rows where the author is within the 333-335 range and has a source of "BC"
SELECT *
FROM wordassociation
WHERE
	SOURCE = 'BC'
	AND author >= 333
	AND author <= 335;
