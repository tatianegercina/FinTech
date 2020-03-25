-- Populate that table
INSERT INTO customer (first_name, last_name)
VALUES
  ('Bob', 'Smith'),
  ('Jane', 'Davidson'),
  ('Jimmy', 'Bell'),
  ('Stephanie', 'Duke');

-- Populate that table
INSERT INTO customer_email (customer_id, email)
VALUES
  (1, 'bobsmith@email.com'),
  (2, 'jdavids@email.com'),
  (3, 'jimmyb@email.com'),
  (4, 'sd@email.com');

-- Populate that table
INSERT INTO customer_phone (customer_id, phone)
VALUES
  (1, '435-344-2245'),
  (2, '332-776-4678'),
  (3, '221-634-7753'),
  (4, '445-663-5799');
