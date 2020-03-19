
CREATE VIEW customer_revenues AS
select customer_id, COUNT(payment_id) as payment_count, SUM(amount) as total_amount
from payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC;

CREATE VIEW daily_revenues AS
select CAST(payment_date as DATE), COUNT(payment_id) as payment_count, SUM(amount) as total_amount
FROM payment
GROUP BY CAST(payment_date as DATE)
ORDER BY CAST(payment_date as DATE) DESC;