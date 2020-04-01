-- Drop table if exists
DROP TABLE IF EXISTS mortgage;

-- Create new table
CREATE TABLE mortgage (
	mortgage_id SERIAL PRIMARY KEY,
	mortgage_name VARCHAR(50),
	mortgage_rate FLOAT
);

-- View table columns and datatypes
SELECT * FROM mortgage;
