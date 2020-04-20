DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS customer_email CASCADE;
DROP TABLE IF EXISTS customer_phone CASCADE;

-- 1. Create a Customer table
CREATE TABLE customer (
    customer_id SERIAL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (customer_id)
);

-- 2. Create Customer Email table
CREATE TABLE customer_email (
    email_id SERIAL,
    customer_id INTEGER NOT NULL,
    email VARCHAR(30) NOT NULL,
    PRIMARY KEY (email_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

-- Let's create a third table with a foreign key that references the first table
CREATE TABLE customer_phone (
    customer_phone_id SERIAL,
    phone VARCHAR(30) NOT NULL,
    customer_id INTEGER NOT NULL,
    PRIMARY KEY (customer_phone_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
