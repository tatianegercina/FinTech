-- Drop table if exists
DROP TABLE banks;

-- Create new programming_languages table
CREATE TABLE banks (
  bank_id SERIAL PRIMARY KEY,
  bank_name VARCHAR(50),
  bank_routing_number BIGINT
);