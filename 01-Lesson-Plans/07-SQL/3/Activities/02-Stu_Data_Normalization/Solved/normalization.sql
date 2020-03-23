DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
  customer_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255)
);

INSERT INTO customer
(customer_id, first_name, last_name, email)
VALUES
(123, 'Robert', 'Bale', 'robert.bale51231@gmail.com'),
(123, 'Robert', 'Bale', 'robbieman512@gmail.com'),
(456, 'Anya', 'Strensa', 'anya.strensa1412@gmail.com'),
(456, 'Anya', 'Strensa', 'soccergirl4251@gmail.com'),
(789, 'Arnold', 'Tolenski', 'arnold.tolenski5121@gmail.com');


select * from customer;