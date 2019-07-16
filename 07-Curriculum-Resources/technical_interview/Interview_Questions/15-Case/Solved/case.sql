-- MySQL code
CREATE TABLE animals (
  id integer(11) auto_increment not null,
  animal_name varchar(255) not null,
  species varchar(255),
  primary key(id)
);

INSERT INTO animals (animal_name, species) VALUES ("Mickey Mouse", "duck");
INSERT INTO animals (animal_name, species) VALUES ("Minnie Mouse", "duck");
INSERT INTO animals (animal_name, species) VALUES ("Donald Duck", "mouse");

UPDATE animals
SET species = 
CASE species
    WHEN "duck" THEN "mouse"
    WHEN "mouse" THEN "duck"
END;
