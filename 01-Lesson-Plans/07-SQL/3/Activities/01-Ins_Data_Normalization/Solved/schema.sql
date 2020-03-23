DROP TABLE IF EXISTS family_children;
DROP TABLE IF EXISTS first_nf_family_children;
DROP TABLE IF EXISTS second_nf_family;
DROP TABLE IF EXISTS second_nf_child
DROP TABLE IF EXISTS owner_store;
DROP TABLE IF EXISTS third_nf_owner;
DROP TABLE IF EXISTS third_nf_store;

CREATE TABLE raw_data 
(
	family VARCHAR(255),
	children VARCHAR(255)
);

INSERT INTO raw_data
(family, children)
VALUES
('Smith', 'Chris, Abby, Susy'),
('Jones', 'Steve, Mary, Dillion');

CREATE TABLE first_normal_form 
(
	family VARCHAR(255),
	children VARCHAR(255)
);

INSERT INTO first_normal_form
(family, children)
VALUES
('Smith', 'Abby'),
('Smith', 'Susy'),
('Jones', 'Mary'),
('Smith', 'Chris'),
('Jones', 'Dillion'),
('Jones', 'Mary');

CREATE TABLE second_nf_family
(
	family_id INT PRIMARY KEY,
	family VARCHAR(255)
);

INSERT INTO second_nf_family
(family_id, family)
VALUES
(1, 'Smith'),
(2, 'Jones');

CREATE TABLE second_nf_child
(
	child_id INT PRIMARY KEY,
	family_id INT
);

INSERT INTO second
