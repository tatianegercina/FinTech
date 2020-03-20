
-- Find the count of payments per customer in descending order
select customer_id, COUNT(*) as payment_count
from payment
group by customer_id
ORDER BY COUNT(*) DESC;

-- Find the top 5 customers who have spend the most money
select customer_id, SUM(amount) as total_payment_amount
from payment
group by customer_id
ORDER BY SUM(amount) DESC
LIMIT 5;

-- Find the bottom 5 customers who have spend the least money
select customer_id, SUM(amount) as total_payment_amount
from payment
group by customer_id
ORDER BY SUM(amount) ASC
LIMIT 5;

-- Find the top 10 customers with the highest average payment
-- rounded to two decimal places
select customer_id, ROUND(AVG(amount), 2) as average_payment_amount
from payment
group by customer_id
ORDER BY AVG(amount) DESC
LIMIT 5;

-- BONUS 1
select first_name, last_name, COUNT(customer_id) as customer_count
from payment as a
JOIN staff as b ON a.staff_id = b.staff_id
GROUP BY first_name, last_name
ORDER BY COUNT(customer_id) DESC;


-- BONUS 2
select CAST(payment_date AS DATE), COUNT(*)
from payment
GROUP BY CAST(payment_date AS DATE)
ORDER BY COUNT(*) DESC;


