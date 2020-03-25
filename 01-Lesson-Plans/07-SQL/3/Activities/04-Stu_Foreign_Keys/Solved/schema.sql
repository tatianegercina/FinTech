DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS estates;
DROP TABLE IF EXISTS estate_type;

-- Create owners table and insert values
CREATE TABLE owners (
  owner_id INT PRIMARY KEY NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

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

-- BONUS
-- Create estate_type table and insert data
CREATE TABLE estate_type (
  estate_type_id INT NOT NULL PRIMARY KEY,
  estate_type VARCHAR(255)
);

-- Create new pet tables that takes a service id
CREATE TABLE estates_new (
  estate_id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  estate_type_id INT NOT NULL,
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255)
);