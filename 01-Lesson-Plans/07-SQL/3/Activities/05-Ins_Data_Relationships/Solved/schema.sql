DROP TABLE IF EXISTS simpsons CASCADE;
DROP TABLE IF EXISTS address CASCADE;
DROP TABLE IF EXISTS people CASCADE;
DROP TABLE IF EXISTS children CASCADE;
DROP TABLE IF EXISTS parents CASCADE;
DROP TABLE IF EXISTS child_parent CASCADE;

-- One to one
-- Simpson table
CREATE TABLE simpsons(
  id SERIAL,
  name VARCHAR,
  "Social Security" INTEGER
);

-- One to Many
-- Address Table
CREATE TABLE address (
  id INTEGER PRIMARY KEY,
  address VARCHAR
);

-- People Table
CREATE TABLE people (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  social_security INTEGER,
  address_id INTEGER
);

-- Many to Many
-- Table schema for the Simpsons children
CREATE TABLE children(
  child_id SERIAL,
  child_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (child_id)
);

-- Table schema for the Simpsons parents
CREATE TABLE parents(
  parent_id INTEGER NOT NULL,
  parent_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (parent_id)
);

-- Table schema for the junction table
CREATE TABLE child_parent (
  child_id INTEGER NOT NULL,
  FOREIGN KEY (child_id) REFERENCES children(child_id),
  parent_id INTEGER NOT NULL,
  FOREIGN KEY (parent_id) REFERENCES parents(parent_id),
  PRIMARY KEY (child_id, parent_id)
);
