CREATE VIEW customer_revenues AS
select first_name, last_name, COUNT(payment_id) as payment_count, SUM(amount) as total_amount
from payment as a
JOIN customer as b ON a.customer_id = b.customer_id
GROUP BY first_name, last_name
ORDER BY SUM(amount) DESC;

select *
from customer_revenues
where first_name = 'THERESA'
AND last_name = 'WATSON';

-- BONUS
CREATE VIEW staff_sales AS
select staff_id, CAST(payment_date as DATE), COUNT(payment_id) as payment_count, SUM(amount) as total_amount
FROM payment
WHERE staff_id IN
(
	select staff_id
	FROM staff
	WHERE first_name = 'Mike'
	AND last_name = 'Hillyer'
)
GROUP BY staff_id, CAST(payment_date as DATE)
ORDER BY CAST(payment_date as DATE) DESC;
