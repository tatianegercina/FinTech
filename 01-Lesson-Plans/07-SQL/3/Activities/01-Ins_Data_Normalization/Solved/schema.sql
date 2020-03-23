-- Drop tables
DROP TABLE IF EXISTS family_children;
DROP TABLE IF EXISTS first_nf_family_children;
DROP TABLE IF EXISTS second_nf_family;
DROP TABLE IF EXISTS second_nf_child;
DROP TABLE IF EXISTS owner_store;
DROP TABLE IF EXISTS third_nf_owner;
DROP TABLE IF EXISTS third_nf_store;

-- Create raw data
CREATE TABLE family_children 
(
	family VARCHAR(255),
	children VARCHAR(255)
);

-- Create first normal form table
CREATE TABLE first_normal_form 
(
	family VARCHAR(255),
	children VARCHAR(255)
);

CREATE TABLE second_nf_family
(
	family_id INT PRIMARY KEY,
	family VARCHAR(255)
);

CREATE TABLE second_nf_child
(
	child_id INT PRIMARY KEY,
	family_id INT
);

INSERT INTO second
