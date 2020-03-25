INSERT INTO owners
(owner_id, first_name, last_name)
VALUES
(141, 'Sally', 'Bell'),
(232, 'Charles', 'Javier'),
(353, 'Angela', 'Mackeral'),
(424, 'Kelly', 'Delovan'),
(551, 'Samuel', 'Hamgee'),
(612, 'Cassie', 'Oberton');

INSERT INTO estates
(estate_id, owner_id, address, city, state, zip_code)
VALUES
(1, 141, '147 Jupiter Lane Apartment 2F', 'Pasadena', 'CA', 91101),
(2, 232, '5 Calina Drive', 'Allentown', 'PA', 18101),
(3, 353, '918 Sinclaire Court', 'Phoenix', 'AZ', 85004),
(4, 353, '1727 Kalimar Road', 'Eugene', 'OR', 97401),
(5, 424, '128 Sandy Beach Road', 'Avalon', 'NJ', 08202),
(6, 551, '14 Honey Road', 'Lawrence', 'KS', 66044),
(7, 612, '19 Stockton Avenue', 'Austin', 'TX', 78701),
(8, 612, '323 Silamento Lane Apartment 4122', 'Rockville', 'MD', 20847);

INSERT INTO estate_type
(estate_type_id, estate_type)
VALUES
(11, 'House'),
(22, 'Condo'),
(33, 'Townhouse'),
(44, 'Multi-Family'),
(55, 'Land'),
(66, 'Business');

INSERT INTO estates_new
(estate_id, owner_id, estate_type_id, address, city, state, zip_code)
VALUES
(1, 141, 22, '147 Jupiter Lane Apartment 2F', 'Pasadena', 'CA', 91101),
(2, 232, 11, '5 Calina Drive', 'Allentown', 'PA', 18101),
(3, 353, 11, '918 Sinclaire Court', 'Phoenix', 'AZ', 85004),
(4, 353, 55, '1727 Kalimar Road', 'Eugene', 'OR', 97401),
(5, 424, 44, '128 Sandy Beach Road', 'Avalon', 'NJ', 08202),
(6, 551, 11, '14 Honey Road', 'Lawrence', 'KS', 66044),
(7, 612, 33, '19 Stockton Avenue Unit 201', 'Austin', 'TX', 78701),
(8, 612, 22, '323 Silamento Lane Apartment 4122', 'Rockville', 'MD', 20847);