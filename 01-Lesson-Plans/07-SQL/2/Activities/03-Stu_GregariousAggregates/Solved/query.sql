--1. What is the average payment amount?
SELECT AVG(amount) AS "avg_payment_amount"
from payment;

--2. What is the total payment amouht?
SELECT SUM(amount) AS "total_payment_amount"
from payment;

--3. What is the minimum payment amouht?
SELECT MIN(amount) AS "min_payment_amount"
from payment;

--4. What is the maxiumum payment amouht?
SELECT MAX(amount) AS "max_payment_amount"
from payment;

--5. What is the count of payments for each customer?
SELECT customer_id, COUNT(*) AS "payment_count"
FROM payment
GROUP BY customer_id;

--6. How many customers has each staff serviced?
SELECT staff_id, COUNT(customer_id) AS "customer_count"
FROM payment
GROUP BY staff_id;
