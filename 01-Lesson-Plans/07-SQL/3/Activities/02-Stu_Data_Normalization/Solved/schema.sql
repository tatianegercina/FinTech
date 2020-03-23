-- Create owners table and insert values
CREATE TABLE owners (
  id INT PRIMARY KEY NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

INSERT INTO owners 
(owner_id, first_name, last_name) 
VALUES
(141, 'Sally', 'Bell'),
(232, 'Charles', 'Javier'),
(353, 'Angela', 'Mackeral'),
(424, 'Kelly', 'Delovan'),
(551, 'Samuel', 'Hamgee'),
(612, 'Cassie', 'Oberton');

SELECT * FROM owners;

-- Create pet name table and insert values
CREATE TABLE estates (
  id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255),
  type VARCHAR (255)
);

INSERT INTO estates 
(id, owner_id, address, city, state, zip_code) 
VALUES
(1, 141, '147 Jupiter Lane Apartment 2F', 'Pasadena', 'CA', 91101),
(2, 232, '5 Calina Drive', 'Allentown', 'PA', 18101),
(3, 353, '918 Sinclaire Court', 'Phoenix', 'AZ', 85004),
(4, 353, '1727 Kalimar Road', 'Eugene' 'OR' 97401),
(5, 424, '128 Sandy Beach Road', 'Avalon', 'NJ', 08202),
(6, 551, '14 Honey Road', 'Lawrence', 'KS', 66044),
(7, 612, '19 Stockton Avenue', 'Austin', 'TX' 78701),
(8, 612, '323 Silamento Lane Apartment 4122', 'Rockville', 'MD', 20847);

SELECT * FROM estates;

-- Select all columns from joined table
SELECT *
FROM owners
INNER JOIN estates ON owners.id = estates.owner_id;

-- select explicit columns from joined table
SELECT 
  owners.first_name, 
  owners.last_name, 
  estates.address, 
  estates.city, 
  estates.state, 
  estates.zip_code
FROM owners
INNER JOIN estates ON owners.id = estates.owner_id;

-- BONUS
-- Create estate_type table and insert data
CREATE TABLE estate_type (
  id INT NOT NULL PRIMARY KEY,
  type VARCHAR(255)
);

INSERT INTO estate_type
(id, service_type)
VALUES
(11, 'House'),
(22, 'Condo'),
(33, 'Townhouse'),
(44, 'Multi-Family'),
(55, 'Land');

-- Create new pet tables that takes a service id
CREATE TABLE estates_new (
  estate_id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  type_id INT NOT NULL,
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255)
);

-- Insert data with service id
INSERT INTO estates_new 
(estate_id, owner_id, type_id, address, city, state, zip_code)
VALUES
(1, 141, 22, '147 Jupiter Lane Apartment 2F', 'Pasadena', 'CA', 91101),
(2, 232, 11, '5 Calina Drive', 'Allentown', 'PA', 18101),
(3, 353, 11, '918 Sinclaire Court', 'Phoenix', 'AZ', 85004),
(4, 353, 55, '1727 Kalimar Road', 'Eugene' 'OR' 97401),
(5, 424, 44, '128 Sandy Beach Road', 'Avalon', 'NJ', 08202),
(6, 551, 11, '14 Honey Road', 'Lawrence', 'KS', 66044),
(7, 612, 33, '19 Stockton Avenue Unit 201', 'Austin', 'TX' 78701),
(8, 612, 22, '323 Silamento Lane Apartment 4122', 'Rockville', 'MD', 20847);

-- Join all three tables
SELECT *
FROM owners
INNER JOIN estates_new ON owners.ID = pet_names_new.owner_id
INNER JOIN service ON service.id = pet_names_new.service_id;
