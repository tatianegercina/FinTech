SELECT * FROM owners;
SELECT * FROM estates;

--
INSERT INTO estates
(estate_id, owner_id, address, city, state, zip_code)
VALUES
(1, 10, '23 Delafield Avenue', 'New Brunswick', 'NJ', 08901),

-- Select all columns from joined table
SELECT *
FROM owners
INNER JOIN estates ON owners.owner_id = estates.owner_id;

-- select explicit columns from joined table
SELECT
  owners.first_name,
  owners.last_name,
  estates.address,
  estates.city,
  estates.state,
  estates.zip_code
FROM owners
INNER JOIN estates ON owners.owner_id = estates.owner_id;

-- BONUS
SELECT * FROM estate_type
SELECT * FROM estates_new

-- Join all three tables
SELECT *
FROM owners
INNER JOIN estates_new ON owners.owner_id = estates_new.owner_id
INNER JOIN estate_type ON estates_new.estate_type_id = estate_type.estate_type_id;
