-- 1. Find the customer first and last names of those who have made payments.
SELECT first_name, last_name
FROM customer
WHERE customer_id IN
  (
  SELECT customer_id
  FROM payment
  );

-- 2. Find the staff email addresses of those who have helped customers make payments.
SELECT email
FROM staff
WHERE staff_id IN
  (
  SELECT staff_id
  FROM payment
  );

-- 3. Find the rental records of all films that have been rented out and paid for.
SELECT *
FROM rental
WHERE rental_id IN
  (
  SELECT rental_id
  FROM payment
  );

-- BONUS
SELECT title
FROM film
WHERE film_id IN
  (
  SELECT film_id
  FROM inventory
  WHERE inventory_id IN
    (
    SELECT inventory_id
    FROM rental
    WHERE rental_id IN
      (
      SELECT rental_id
      FROM payment
      )
    )
  );

















-- Question 1

SELECT city, city_id
FROM city
WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes');


-- Question 2

SELECT district
FROM address
WHERE city_id IN
(
  SELECT city_id
  FROM city
  WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
);


-- Bonus

SELECT first_name, last_name
FROM customer cus
WHERE address_id IN
(
  SELECT address_id
  FROM address a
  WHERE city_id IN
  (
    SELECT city_id
    FROM city
    WHERE city LIKE 'Q%'
  )
);
