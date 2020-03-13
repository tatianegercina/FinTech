-- Query inserted rows from the banks table
SELECT *
FROM banks;

-- Query the rows with bank name equal to "Capital One"
SELECT *
FROM banks
WHERE bank_name = 'Capital One';

-- Drop the duplicate Capital One row
DELETE FROM banks
WHERE bank_id = 7;

-- Query all rows to see change
SELECT *
FROM banks;

-- Add additional data
INSERT INTO banks
(bank_name, bank_routing_number)
VALUES
('Ally Bank', 316289502),
('Discover Bank', 639893944),
('Bank of New York Mellon', 8734569384);

-- Query all rows to see change
SELECT *
FROM banks;

-- Update "JS" to "JavaScript"
UPDATE banks
SET bank_name = 'PNC Bank'
WHERE bank_id = 4;

-- Query all rows to see change
SELECT *
FROM banks;

-- Change HTML's rating to 90
UPDATE banks
SET bank_routing_number = 1995826182
WHERE bank_id = 2;

-- Query all rows to see change
SELECT *
FROM banks;

-- BONUS
-- Add a "mastered" column with the boolean default of true
ALTER TABLE banks
ADD COLUMN mortgage_lender BOOLEAN default true;
