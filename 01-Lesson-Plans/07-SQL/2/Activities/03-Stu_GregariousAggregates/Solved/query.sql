--1. What is the average payment amount?
select AVG(amount) AS "avg_payment_amount"
from payment;

--2. What is the total payment amouht?
select SUM(amount) AS "total_payment_amount"
from payment;

--3. What is the minimum payment amouht?
select MIN(amount) AS "min_payment_amount"
from payment;

--4. What is the maxiumum payment amouht?
select MAX(amount) AS "max_payment_amount"
from payment;

--5. What is the count of payments for each customer?
select customer_id, COUNT(*) AS "payment_count"
FROM payment
GROUP BY customer_id;