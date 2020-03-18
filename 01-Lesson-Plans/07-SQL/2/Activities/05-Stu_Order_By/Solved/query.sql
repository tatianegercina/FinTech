
-- Find the count of payments per customer in descending order
select customer_id, COUNT(*) as payment_count
from payment
group by customer_id
ORDER BY COUNT(*);

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

-- BONUS
select CAST(payment_date AS DATE), COUNT(*)
from payment
GROUP BY CAST(payment_date AS DATE)
ORDER BY COUNT(*) DESC;