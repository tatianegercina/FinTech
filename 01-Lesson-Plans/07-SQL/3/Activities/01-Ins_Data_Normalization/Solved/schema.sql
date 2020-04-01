-- Drop tables
DROP TABLE IF EXISTS family_children;
DROP TABLE IF EXISTS first_nf_family_children;
DROP TABLE IF EXISTS second_nf_family;
DROP TABLE IF EXISTS second_nf_child;
DROP TABLE IF EXISTS owner_store;
DROP TABLE IF EXISTS third_nf_owner;
DROP TABLE IF EXISTS third_nf_store;

-- Create raw data for first and second normal form use cases
CREATE TABLE family_children 
(
	family VARCHAR(255),
	children VARCHAR(255)
);

-- Create first normal form table
CREATE TABLE first_nf_family_children
(
	family VARCHAR(255),
	children VARCHAR(255)
);

-- Create second normal form `family` table
CREATE TABLE second_nf_family
(
	family_id INT PRIMARY KEY,
	family VARCHAR(255)
);

-- Create second normal form `child` table
CREATE TABLE second_nf_child
(
	child_id INT PRIMARY KEY,
	family_id INT,
	children VARCHAR(255)
);

-- Create raw data for third normal form use case
CREATE TABLE owner_store
(
	owner_id INT,
	owner_name VARCHAR(255),
	owner_address VARCHAR(255),
	store_name VARCHAR(255)
);

-- Create third normal form `owner` table
CREATE TABLE third_nf_owner
(
	owner_id INT PRIMARY KEY,
	owner_name VARCHAR(255),
	owner_address VARCHAR(255)
);

-- Create third normal form `store` table
CREATE TABLE third_nf_store
(
	store_id INT PRIMARY KEY,
	store_name VARCHAR(255),
	owner_id INT
);