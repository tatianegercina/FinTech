--1. What is the average payment amount?
select AVG(amount) as "avg_payment_amount"
from payment;

--2. What is the total payment amouht?
select SUM(amount) as "total_payment_amount"
from payment;

--3. What is the minimum payment amouht?
select MIN(amount) as "min_payment_amount"
from payment;

--4. What is the maxiumum payment amouht?
select MAX(amount) as "max_payment_amount"
from payment;

--5. What is the count of payments for each customer?
select customer_id, COUNT(*) as "payment_count"
FROM payment
GROUP BY customer_id;

--6. How many customers has each staff serviced?
select staff_id, COUNT(customer_id) as "customer_count"
FROM payment
GROUP BY staff_id;