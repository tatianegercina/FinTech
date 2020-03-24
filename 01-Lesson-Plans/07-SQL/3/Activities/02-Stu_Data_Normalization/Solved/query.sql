DROP TABLE IF EXISTS employee_normalization;
DROP TABLE IF EXISTS first_nf_employee;
DROP TABLE IF EXISTS second_nf_employee;
DROP TABLE IF EXISTS second_nf_employee_email;
DROP TABLE IF EXISTS third_nf_employee;
DROP TABLE IF EXISTS third_nf_zipcode;

CREATE TABLE employee_normalization (
	employee_id INT,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT,
	email VARCHAR(255)
);

INSERT INTO employee_normalization
(employee_id, name, age, address, city, state, zip_code, email)
VALUES
(123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robert.bale51231@gmail.com, robbieman512@gmail.com'),
(456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'anya.strensa1412@gmail.com, soccergirl4251@gmail.com'),
(789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016, 'arnold.tolenski5121@gmail.com');

CREATE TABLE first_nf_employee
(
	employee_id INT,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT,
	email VARCHAR(255)
);

INSERT INTO first_nf_employee
(employee_id, name, age, address, city, state, zip_code, email)
VALUES
(123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robert.bale51231@gmail.com'),
(123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robbieman512@gmail.com'),
(456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'anya.strensa1412@gmail.com'),
(456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'soccergirl4251@gmail.com'),
(789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016, 'arnold.tolenski5121@gmail.com');

CREATE TABLE second_nf_employee
(
	employee_id INT PRIMARY KEY,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT
);

INSERT INTO second_nf_employee
(employee_id, name, age, address, city, state, zip_code)
VALUES
(123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002),
(456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami',' FL', 33101),
(789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016);


CREATE TABLE second_nf_employee_email
(
	email_id INT PRIMARY KEY,
	employee_id INT,
	email VARCHAR(255)
);

INSERT INTO second_nf_employee_email
(email_id, employee_id, email)
VALUES
(1, 123, 'robert.bale51231@gmail.com'),
(2, 123, 'robbieman512@gmail.com'),
(3, 456, 'anya.strensa1412@gmail.com'),
(4, 456, 'soccergirl4251@gmail.com'),
(5, 789, 'arnold.tolenski5121@gmail.com');

CREATE TABLE third_nf_employee
(
	employee_id INT PRIMARY KEY,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	zip_code INT
);

INSERT INTO third_nf_employee
(employee_id, name, age, address, zip_code)
VALUES
(123, 'Robert Bale', 32, '31 Pelham Drive', 77002),
(456, 'Anya Strensa', 25, '142 Sunshine Road', 33101),
(789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 94016);

CREATE TABLE third_nf_zipcode
(
	zip_code INT PRIMARY KEY,
	city VARCHAR(255),
	state VARCHAR(255)
);

INSERT INTO third_nf_zipcode
(zip_code, city, state)
VALUES
(77002, 'Houston', 'TX'),
(33101, 'Miami', 'FL'),
(94016, 'San Francisco', 'CA');