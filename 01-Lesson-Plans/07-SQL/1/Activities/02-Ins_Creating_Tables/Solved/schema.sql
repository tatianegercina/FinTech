-- Create a new table
CREATE TABLE customer (
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30),
  gender VARCHAR(30),
  age INT,
  address VARCHAR(50),
  city VARCHAR(50),
  province CHAR(2),
  postal_code CHAR(6)
);

-- Query all fields from the table
SELECT * FROM customer;
