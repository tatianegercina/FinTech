INSERT INTO simpsons (name, "Social Security")
VALUES
  ('Homer', 111111111),
  ('Marge', 222222222),
  ('Lisa', 333333333),
  ('Bart', 444444444),
  ('Maggie', 555555555);

-- Insertion query for address table
INSERT INTO address (id, address)
VALUES
  (11, '742 Evergreen Terrace'),
  (12, '221b Baker Streer');

-- Insertion query for people table
INSERT INTO people (id, name, social_security)
VALUES
  (1, 'Homer', 111111111),
  (2, 'Marge', 222222222),
  (3, 'Lisa', 333333333),
  (4, 'Bart', 444444444),
  (5, 'Maggie', 555555555),
  (6, 'Sherlock', 666666666),
  (7, 'Watson', 777777777);

-- Insertion queries for the Simpsons children
INSERT INTO children (child_name)
VALUES
  ('Bart'),
  ('Lisa'),
  ('Maggie');

-- Insertion queries for the Simpsons parents
INSERT INTO parents (parent_id, parent_name)
VALUES
  (11, 'Homer'),
  (12, 'Marge');

-- Insertion queries for the junction table
INSERT INTO child_parent (child_id, parent_id)
VALUES
  (1, 11),
  (1, 12),
  (2, 11),
  (2, 12),
  (3, 11),
  (3, 12);
