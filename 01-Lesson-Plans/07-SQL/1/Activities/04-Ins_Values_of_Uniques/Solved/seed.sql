-- Insert data into the table (if empty)
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'MT', 07829),
('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AZ', 89721),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673);

-- Insert duplicate records
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673);

-- Verify changes
SELECT *
FROM customer;

-- Insert duplicated data into the table after re-creating with an incremental primary key
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'MT', 07829),
('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AZ', 89721),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673),
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673);
