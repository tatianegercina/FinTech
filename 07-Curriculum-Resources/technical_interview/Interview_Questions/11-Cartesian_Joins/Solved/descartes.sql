CREATE DATABASE career_module;
USE career_module;
CREATE TABLE table_one(id integer);
CREATE TABLE table_two(id integer);

INSERT INTO table_one(id) VALUES
(1),
(2),
(3),
(4);

INSERT INTO table_two(id) VALUES
(10),
(11),
(12);

SELECT *
FROM table_one, table_two;
