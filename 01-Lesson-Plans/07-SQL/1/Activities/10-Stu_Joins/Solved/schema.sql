-- Create new table
CREATE TABLE mortgage (
  mortgage_id SERIAL PRIMARY KEY,
  mortgage_name VARCHAR(50),
  mortgage_rate FLOAT
);

-- Create new table to import data
CREATE TABLE sales (
  sales_id SERIAL PRIMARY KEY,
  payment_id INT,
  mortgage_id INT,
  loan_amount INT,
  loan_date DATE
);

CREATE TABLE payemnts (
  payment_id SERIAL PRIMARY KEY,
  bank_number BIGINT,
  bank_routing_number BIGINT,
  customer_id INT
);

-- BONUS
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