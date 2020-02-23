-- Query all fields from the table
SELECT *
FROM people;

-- Query only the `pet_name` field
SELECT pet_name
FROM people;

-- Filter the query to show only dogs under the age of 5
SELECT pet_type, pet_name
FROM people
WHERE pet_type = 'dog'
AND pet_age < 5;
