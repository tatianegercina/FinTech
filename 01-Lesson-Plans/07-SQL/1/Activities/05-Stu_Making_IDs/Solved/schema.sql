-- Drop table if exists
DROP TABLE programming_languages;

-- Create new programming_languages table
CREATE TABLE programming_languages (
  id SERIAL PRIMARY KEY,
  language VARCHAR(20),
  rating INT
);
