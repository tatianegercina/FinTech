-- Insert data into the table (if empty)
INSERT INTO customer
(first_name, last_name, gender, age, address, city, province, postal_code)
VALUES
  ('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'NL', 'A1A0A4'),
  ('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'QC', 'G1A0B1'),
  ('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AB', 'T2P1B4'),
  ('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'NU', 'X0A0H0');

-- Insert duplicate records
INSERT INTO customer
(first_name, last_name, gender, age, address, city, province, postal_code)
VALUES
  ('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'NL', 'A1A0A4'),
  ('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'NU', 'X0A0H0');

-- Verify changes
SELECT *
FROM customer;

-- Insert duplicated data into the table after re-creating with an incremental primary key
INSERT INTO customer
(first_name, last_name, gender, age, address, city, province, postal_code)
VALUES
  ('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'NL', 'A1A0A4'),
  ('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'QC', 'G1A0B1'),
  ('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AB', 'T2P1B4'),
  ('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'NU', 'X0A0H0'),
  ('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'NL', 'A1A0A4'),
  ('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'NU', 'X0A0H0');
