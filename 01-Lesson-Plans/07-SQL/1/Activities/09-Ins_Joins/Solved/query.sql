-- Query all records from sales table
select *
from sales;

-- Query all records from mortgage table
select *
from mortgage;

-- Perform an INNER JOIN on the two tables
SELECT sales.sales_id,
       sales.payment_id,
       sales.mortgage_id,
       sales.loan_amount,
       sales.loan_date,
       mortgage.mortgage_id,
       mortgage.mortgage_name,
       mortgage.mortgage_rate
FROM sales
INNER JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;

-- Perform an INNER JOIN on the two tables with aliasing
SELECT a.sales_id,
       a.payment_id,
       a.mortgage_id,
       a.loan_amount,
       a.loan_date,
       b.mortgage_id,
       b.mortgage_name,
       b.mortgage_rate
FROM sales as a
INNER JOIN mortgage as b ON a.mortgage_id = b.mortgage_id;

-- Perform an INNER JOIN and return all columns
SELECT *
FROM sales
INNER JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;

-- Perform a LEFT JOIN and return all columns
SELECT *
FROM sales
LEFT JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;

-- Perform a RIGHT JOIN and return all columns
SELECT *
FROM sales
RIGHT JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;

-- Perform a FULL OUTER JOIN and return all columns
SELECT *
FROM sales
FULL OUTER JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;

-- Perform a CROSS JOIN and return all columns
SELECT *
FROM sales
CROSS JOIN mortgage;
