SELECT *
FROM sales;

SELECT *
FROM sales
WHERE loan_amount < 300000;

SELECT AVG(loan_amount)
FROM sales;

UPDATE sales
SET loan_amount = 423212
WHERE sales_id = 33;

-- Insert new data
INSERT INTO sales
(sales_id, payment_id, mortgage_id, loan_amount, loan_date)
VALUES (101, 101, 2, 734544, '10/5/1995');

DELETE FROM sales
WHERE sales_id = 72;