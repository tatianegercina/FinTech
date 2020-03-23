-- Create owners table and insert values
CREATE TABLE owners (
  id INT PRIMARY KEY NOT NULL,
  owner_name VARCHAR(255)
);

INSERT INTO owners 
(ID, owner_name) 
VALUES
(141, 'Sally'),
(232, 'Charles'),
(353, 'Angela'),
(424, 'Kelly'),
(551, 'Samuel'),
(612, 'Cassie');

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
SELECT first_name, last_name, address, city, state, zip_code
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
(33, 'Multi-Family'),
(44, 'Land');

-- Create new pet tables that takes a service id
CREATE TABLE estates_new (
  id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  type_id INT NOT NULL,
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255),
  type VARCHAR (255)
);

-- Insert data with service id
INSERT INTO estates_new 
(ID, owner_id, service_id, pet_name, type)
VALUES
(10, 1, 22, 'Zeus', 'Dog'),
(11, 1, 22, 'Fido', 'Dog'),
(12, 2, 22, 'Kevin', 'Dog'),
(13, 3, 33, 'Sprinkles', 'Cat'),
(14, 4, 33, 'Jumper', 'Cat'),
(15, 5, 44, 'Hoppy', 'Rabbit'),
(16, 6, 22, 'Rex', 'Dog'),
(17, 6, 44, 'Carrot', 'Rabbit');

-- Join all three tables
SELECT owners.owner_name,
pet_names_new.pet_name, pet_names_new.type, service.service_type
FROM owners
INNER JOIN pet_names_new ON owners.ID = pet_names_new.owner_id
INNER JOIN service ON service.id = pet_names_new.service_id;
