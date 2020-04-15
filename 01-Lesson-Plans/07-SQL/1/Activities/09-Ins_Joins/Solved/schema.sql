-- Drop table if exists
DROP TABLE IF EXISTS mortgage;
DROP TABLE IF EXISTS sales;

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
