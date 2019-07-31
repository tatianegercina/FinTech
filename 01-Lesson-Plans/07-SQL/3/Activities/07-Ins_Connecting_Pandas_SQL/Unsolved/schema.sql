-- Create tables

CREATE TABLE animals_all (
  id SERIAL PRIMARY KEY,
  animal_species VARCHAR(30) NOT NULL,
  owner_name VARCHAR(30) NOT NULL
);

CREATE TABLE animals_location (
  id SERIAL PRIMARY KEY,
  location VARCHAR(30) NOT NULL,
  animal_id INTEGER NOT NULL,
  FOREIGN KEY (animal_id) REFERENCES animals_all(id)
);


-- Insert data

INSERT INTO animals_all (animal_species, owner_name)
VALUES
  ('Dog', 'Bob'),
  ('Fish', 'Bob'),
  ('Cat', 'Kelly'),
  ('Dolphin', 'Aquaman');

INSERT INTO animals_location (location, animal_id)
VALUES
  ('Dog House', 1),
  ('Fish Tank', 2),
  ('Bed', 3),
  ('Ocean', 4);