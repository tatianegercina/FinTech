-- Insert mortgage data
INSERT INTO "mortgage" 
(mortgage_name, mortgage_rate)
VALUES
    ('10-Year Fixed Loan',0.03),
    ('15-Year Fixed Loan',0.035),
    ('20-Year Fixed Loan',0.04),
    ('30-Year Fixed Loan',0.045),
    ('40-Year Fixed Loan',0.05);

-- Insert sales data
INSERT INTO "sales"
(payment_id, mortgage_id, loan_amount, loan_date)
VALUES
    (1,4,281156,'1995-10-05'),
    (2,2,281353,'2006-05-06'),
    (3,3,217156,'2011-04-01'),
    (4,1,196579,'2001-05-11'),
    (5,3,302332,'2017-06-09'),
    (6,2,317515,'2011-04-27'),
    (7,1,315360,'2006-01-28'),
    (8,1,283313,'1996-06-09'),
    (9,4,220254,'2009-09-10'),
    (10,3,140502,'2009-04-03'),
    (11,4,247224,'1994-10-15'),
    (12,4,328978,'2003-08-26'),
    (13,2,301668,'2003-06-02'),
    (14,2,223999,'2014-02-25'),
    (15,4,465346,'2002-11-06'),
    (16,1,331112,'2017-02-04'),
    (17,1,310641,'2002-03-27'),
    (18,1,279250,'1999-02-08'),
    (19,4,257968,'2007-11-17'),
    (20,1,197662,'1991-09-16'),
    (21,4,382576,'2000-04-01'),
    (22,2,404106,'2001-04-04'),
    (23,3,291396,'2009-04-18'),
    (24,1,474243,'2008-11-11'),
    (25,3,265941,'2015-12-18'),
    (26,1,281625,'1996-04-28'),
    (27,3,277796,'1998-04-03'),
    (28,1,328039,'2012-06-12'),
    (29,1,386537,'2015-05-17'),
    (30,2,348675,'1990-05-05'),
    (31,3,224163,'1994-03-22'),
    (32,4,331043,'2004-08-21'),
    (33,4,145149,'2013-02-21'),
    (34,3,225232,'1991-10-11'),
    (35,3,268393,'2013-10-10'),
    (36,2,327828,'2015-06-16'),
    (37,3,442343,'1998-12-17'),
    (38,2,150825,'2011-11-18'),
    (39,4,335725,'2016-05-10'),
    (40,3,363086,'2010-06-17'),
    (41,3,263832,'2014-07-16'),
    (42,3,357059,'2011-06-27'),
    (43,3,347346,'2019-05-27'),
    (44,3,279861,'2006-10-18'),
    (45,2,256965,'1996-09-03'),
    (46,4,349580,'1993-11-26'),
    (47,2,443228,'1993-06-18'),
    (48,2,331976,'2005-07-11'),
    (49,4,329333,'2000-09-25'),
    (50,2,279504,'2001-02-09'),
    (51,1,308276,'2015-06-19'),
    (52,3,120548,'1994-11-01'),
    (53,2,239104,'2004-12-08'),
    (54,3,180242,'2017-04-06'),
    (55,3,233883,'1997-03-15'),
    (56,2,236943,'2014-09-12'),
    (57,1,203883,'2014-10-24'),
    (58,1,469486,'2013-05-13'),
    (59,1,291974,'2018-09-20'),
    (60,4,272553,'2001-11-23'),
    (61,3,362433,'1991-11-02'),
    (62,2,206713,'2018-01-02'),
    (63,3,275105,'1993-03-30'),
    (64,1,325828,'1999-02-06'),
    (65,2,145085,'2011-09-12'),
    (66,4,296104,'1995-04-13'),
    (67,3,232930,'2000-05-18'),
    (68,2,160209,'1996-12-25'),
    (69,1,278108,'2009-06-23'),
    (70,1,255423,'2003-11-01'),
    (71,1,314265,'2016-10-16'),
    (72,2,192334,'2003-05-19'),
    (73,4,371194,'1990-05-24'),
    (74,2,347872,'2007-01-09'),
    (75,3,383102,'2012-12-30'),
    (76,3,449836,'1993-06-13'),
    (77,1,363430,'1997-05-31'),
    (78,3,322059,'2006-01-03'),
    (79,3,284419,'1995-06-03'),
    (80,2,266850,'1992-11-02'),
    (81,1,343490,'2017-01-08'),
    (82,1,491435,'2011-03-25'),
    (83,4,351067,'2009-07-04'),
    (84,3,387039,'2003-10-14'),
    (85,1,241737,'2012-04-24'),
    (86,1,253503,'2004-11-02'),
    (87,4,486098,'2015-05-06'),
    (88,3,412952,'1996-04-25'),
    (89,4,157722,'2008-09-24'),
    (90,2,426505,'2003-08-13'),
    (91,4,229424,'1992-03-24'),
    (92,2,474692,'2009-11-10'),
    (93,2,323300,'1998-09-06'),
    (94,4,386080,'2011-04-28'),
    (95,4,211860,'2010-12-23'),
    (96,2,191138,'2003-03-13'),
    (97,1,223548,'1996-02-04'),
    (98,2,150804,'2004-10-05'),
    (99,2,377724,'2015-03-28'),
    (100,4,187826,'2018-05-28');

INSERT INTO payments 
(bank_number, bank_routing_number, customer_id)
VALUES
    (9269877403,905192010,1),
    (82888733522,629873495,2),
    (20862689216,905192010,3),
    (87342300762,890123900,4),
    (32016806394,629873495,5),
    (89178109018,890123900,6),
    (11398000774,2340903984,7),
    (22787074845,890123900,8),
    (60706346980,890123900,9),
    (12654009617,184619239,10),
    (51632282614,629873495,11),
    (68456483309,905192010,12),
    (73015643543,2340903984,13),
    (66653098136,905192010,14),
    (73639983258,184619239,15),
    (68191577695,890123900,16),
    (1130813569,890123900,17),
    (46731417034,2340903984,18),
    (69004996851,184619239,19),
    (75032806086,905192010,20),
    (65612468052,890123900,21),
    (76163431193,629873495,22),
    (31125785634,629873495,23),
    (64250427325,184619239,24),
    (7284515287,198491827,25),
    (36243682622,2340903984,26),
    (6802893682,629873495,27),
    (48975373191,2340903984,28),
    (55317680318,629873495,29),
    (6957425936,905192010,30),
    (87596526571,2340903984,31),
    (32237372412,2340903984,32),
    (50668921877,2340903984,33),
    (31905656087,629873495,34),
    (76887338713,2340903984,35),
    (53202638817,890123900,36),
    (48862241090,629873495,37),
    (16179523315,890123900,38),
    (31525433090,890123900,39),
    (86346682262,905192010,40),
    (94169987556,198491827,41),
    (15257433300,629873495,42),
    (89793281199,890123900,43),
    (61899463671,905192010,44),
    (15097116063,2340903984,45),
    (14287899182,905192010,46),
    (50466419650,2340903984,47),
    (13036169817,905192010,48),
    (99461190391,890123900,49),
    (46824584329,905192010,50),
    (98733625849,2340903984,51),
    (54406399670,890123900,52),
    (23337525652,890123900,53),
    (99135542058,905192010,54),
    (79382904819,198491827,55),
    (51891860969,629873495,56),
    (967477448,890123900,57),
    (43950731817,198491827,58),
    (83587629692,2340903984,59),
    (50677857318,2340903984,60),
    (30030690448,2340903984,61),
    (24846297310,890123900,62),
    (97451406215,2340903984,63),
    (76772259664,184619239,64),
    (40622611365,184619239,65),
    (22259674175,890123900,66),
    (68396653143,184619239,67),
    (30665947105,2340903984,68),
    (64854709670,905192010,69),
    (50770824681,184619239,70),
    (77586925062,629873495,71),
    (63409835848,184619239,72),
    (48199192552,198491827,73),
    (81986012181,184619239,74),
    (25129785289,629873495,75),
    (1895042747,198491827,76),
    (84383348363,890123900,77),
    (28339725980,2340903984,78),
    (84018214168,905192010,79),
    (76687857530,905192010,80),
    (56872804020,629873495,81),
    (81600174551,184619239,82),
    (45952835629,629873495,83),
    (76348348196,890123900,84),
    (53314019780,2340903984,85),
    (31145283096,905192010,86),
    (21794275834,184619239,87),
    (90101392782,905192010,88),
    (56801480654,184619239,89),
    (76630743188,905192010,90),
    (74801502311,890123900,91),
    (58818848296,905192010,92),
    (53453433797,890123900,93),
    (41788548337,905192010,94),
    (44728748510,905192010,95),
    (51737126284,890123900,96),
    (5848472535,629873495,97),
    (48749064404,198491827,98),
    (93467025920,905192010,99),
    (72002809830,890123900,100);


INSERT INTO "customer" VALUES
    ('Michael','Meyer','Male',24,'1021 Eddie Knolls Apt. 087','South Geraldton','RI',43709),
    ('Cindy','Stephens','Female',23,'838 Brown Street','East Christina','MT',7829),
    ('John','Jackson','Male',34,'5319 Candice Motorway','Adkinstown','AZ',89721),
    ('Alexander','Martinez','Male',32,'USNS Mosley','FPO','AA',24673),
    ('John','Pugh','Male',36,'175 Sullivan Isle Suite 666','Brendanshire','KY',25231),
    ('Ashley','Chan','Female',34,'108 Lee Parkway','Deborahberg','OK',20955),
    ('Matthew','Kramer','Male',34,'Unit 5957 Box 6186','DPO','AP',74424),
    ('Tammy','Soto','Female',27,'23071 Renee Land','Jamieville','MO',40734),
    ('Christopher','Kirby','Male',18,'1052 Edward Knoll Suite 288','New Regina','WY',50805),
    ('Krystal','Huang','Female',21,'811 Linda Ridge Suite 074','Port Andrea','WY',79992),
    ('Sandra','Jimenez','Female',34,'Unit 8878 Box 9370','DPO','AA',47704),
    ('Dawn','Black','Female',26,'253 Emily Union Apt. 809','Port Wendyside','NE',10784),
    ('Christina','Henderson','Female',33,'2407 Gavin River','South Brittneyton','MT',62396),
    ('Sheila','Foster','Female',33,'5360 Rebecca Circles','Josephchester','AZ',51015),
    ('Marvin','Cruz','Male',25,'8667 Henderson Isle Suite 805','East Robertview','AR',14934),
    ('Shannon','Thompson','Female',30,'49367 Perkins Burg Apt. 845','Michaelburgh','IA',43200),
    ('Jessica','Brown','Female',33,'72547 John Village','Estesstad','ID',41957),
    ('George','Scott','Male',36,'8882 Morales Mews','South Courtneybury','NH',18411),
    ('Gregory','Green','Male',36,'4148 Mullen Mountain','Lake Mollychester','MD',26998),
    ('Brooke','Armstrong','Female',33,'PSC 4729, Box 2681','APO','AP',65043),
    ('Bethany','Williams','Female',27,'4886 Mills Dale Suite 147','Justinmouth','AZ',50230),
    ('Sherry','Mooney','Female',28,'PSC 9039, Box 7200','APO','AP',47690),
    ('Stephen','Guerrero','Male',20,'14009 Robin Burgs','Michaelborough','NV',41397),
    ('Brandon','Lewis','Male',30,'9514 Andrea Heights','Port Williemouth','NJ',10383),
    ('William','Morris','Male',20,'10016 Brianna Corners','Spencerborough','HI',30578),
    ('Meredith','Turner','Female',34,'85625 Amanda Rest Apt. 602','Jessicamouth','VT',79948),
    ('Dawn','Meyers','Female',29,'74311 Sandra Fork','Danielhaven','NJ',74384),
    ('Frank','Morales','Male',30,'106 Jacobson Cape Suite 271','East Darren','OH',22376),
    ('Rebecca','Robertson','Female',39,'630 Gallagher Springs Suite 091','Martinezton','CO',97611),
    ('Nicholas','Brown','Male',29,'75960 Mcguire Prairie','Aprilhaven','AL',80265),
    ('Vernon','Johnston','Male',24,'1410 Stevens Underpass Suite 213','Jefferymouth','NY',51400),
    ('Sandra','Rodriguez','Female',28,'5761 Leslie Islands','Mendozachester','HI',79939),
    ('Jennifer','Cooper','Female',26,'85295 Baker Loop Suite 699','Jonesland','NH',72283),
    ('Adam','Jones','Male',32,'99630 Martin Throughway','West Timothybury','OH',1931),
    ('Thomas','Hart','Male',19,'USNV Henderson','FPO','AA',89241),
    ('Keith','Thomas','Male',37,'705 Lisa Oval','Port Manuel','DC',80060),
    ('Willie','Morris','Male',33,'5428 Kevin Ports Suite 214','New Stephanieborough','ID',78160),
    ('Kelly','Joyce','Female',32,'165 Miller Crossing','Mariafurt','GA',90387),
    ('Victoria','Romero','Female',19,'637 Greg Street','Robertton','CT',49369),
    ('Denise','Hamilton','Female',30,'43956 Manuel Key','East Lindachester','AL',86491),
    ('Mary','Rosales','Female',30,'50398 Chase Springs','North Nicholas','MD',61035),
    ('Gregory','Myers','Male',36,'33233 Phillips Inlet Apt. 376','South Joshuafurt','TX',34411),
    ('Kyle','Dean','Male',30,'92016 Allison Mission Apt. 998','New Tony','MD',13709),
    ('Allison','Keith','Female',28,'4493 Erica Shore','North Travisshire','MD',34943),
    ('Marisa','Schmitt','Female',31,'467 Durham Trafficway Apt. 930','Cristianhaven','ME',48819),
    ('Mrs.','Abigail','Female',25,'1171 Boyd Manors','Tuckertown','WI',77834),
    ('Randy','Johnson','Male',24,'58221 Jennifer Corners Apt. 264','Williamside','OH',23487),
    ('Michelle','Becker','Female',21,'0665 Robert Track','Port Anthonystad','MI',48071),
    ('Taylor','Hill','Female',25,'700 John Hollow Apt. 501','Port Thomasland','WV',26738),
    ('Amy','Dorsey','Female',38,'5695 Jacobs Streets Apt. 364','East Dennisfort','VT',16334),
    ('Michael','Hendrix','Male',29,'74752 Baker Brooks Apt. 675','Brentstad','ID',40066),
    ('Nancy','Bowman','Female',27,'32735 Smith Port Suite 901','New Jeffreyshire','TN',88996),
    ('Andrea','Myers','Female',41,'8048 Nielsen Crescent','West Douglas','DE',43315),
    ('Mike','Ward','Male',35,'8228 Lisa Hill','Port Ericbury','AK',39672),
    ('Steven','Flores','Male',28,'33769 West Throughway Suite 135','Jamesport','FL',11413),
    ('John','Rogers','Male',25,'3369 Todd Manors','North Amanda','KS',64441),
    ('Angela','Johnson','Female',33,'97838 Ethan Crossroad','South Jacquelineside','VT',39949),
    ('Meredith','Crawford','Female',30,'7293 Kristen Center Apt. 916','East Lisa','SD',9925),
    ('Jon','Smith','Male',33,'698 Mcgee Dale','Jerryside','HI',94831),
    ('Eugene','Klein','Male',36,'79575 Bennett Inlet','Davishaven','AK',77171),
    ('Russell','Smith','Male',37,'4308 Leonard Islands','Matthewview','GA',57971),
    ('Maria','Bennett','Female',23,'676 Jeffery Land','Courtneyberg','CA',5181),
    ('Rebecca','Deleon','Female',36,'6546 Mark Pines','East Jacqueline','VA',48381),
    ('Tiffany','Cook','Female',43,'80543 Tracy Spring Suite 371','Rodriguezshire','KY',75101),
    ('Dr.','Joseph','Male',33,'017 Morton Bypass','Kaitlyntown','WI',39081),
    ('Annette','Mcguire','Female',41,'55949 Anthony Trafficway Suite 183','Bakerhaven','IL',94252),
    ('Jessica','Griffin','Female',27,'34521 Jamie Ports','South Michaelborough','MA',50024),
    ('Susan','Campbell','Female',33,'PSC 5128, Box 4968','APO','AP',74933),
    ('Kyle','Thomas','Male',35,'4238 Ford Trail Apt. 072','Port Stephaniechester','MO',81588),
    ('Valerie','Fisher','Female',33,'28669 Ruth Extensions','Lake Joseph','WV',67044),
    ('Paul','Gonzales','Male',30,'86582 Michelle Canyon Apt. 962','South Alexander','NJ',2064),
    ('Michele','Jones','Female',25,'Unit 5247 Box 7057','DPO','AE',78128),
    ('Rodney','Jennings','Male',36,'30710 Thomas Hollow','Stoneville','DE',52909),
    ('Ray','Brown','Male',35,'3875 Ellen Lights Suite 733','North Gabriellafurt','MI',67003),
    ('Amy','Castro','Female',40,'583 Rhonda Ranch Suite 447','New Billybury','ND',34700),
    ('Blake','Williams','Male',26,'1656 Schultz Landing','Alexanderhaven','ND',82448),
    ('James','Morales','Male',21,'937 Tammy Cliffs','Munozmouth','IN',44121),
    ('Tracy','Pham','Female',27,'1849 Christian Way Suite 078','Hillshire','KY',93291),
    ('William','Berger','Male',35,'506 Katrina Stravenue','East Michelle','AL',9882),
    ('Suzanne','Miller','Female',31,'49737 Danielle Underpass Suite 871','Randallshire','MA',88845),
    ('Michael','Miranda','Male',25,'4701 Cruz Springs Suite 485','South Ryanmouth','MI',60410),
    ('Nancy','Andrews','Female',26,'300 Buckley Fall','Port Paulside','MI',25420),
    ('Steven','Proctor','Male',35,'331 David Spur Apt. 611','South Lisa','KS',54849),
    ('Madison','Murphy','Female',18,'58864 David Village','Port Kenneth','VA',11644),
    ('Benjamin','Barry','Male',29,'2638 David Center','North Staceyshire','NH',57682),
    ('Alexandra','Barton','Female',22,'1622 Anthony Bypass','Jasmineview','KY',83980),
    ('April','Kim','Female',27,'68886 Sarah Locks Suite 156','New Jennifer','NM',76605),
    ('Christopher','Baker','Male',30,'85213 Austin Harbors','Keyfurt','SD',69451),
    ('Randall','Dean','Male',27,'2917 Sarah Rue','Smithchester','KS',24349),
    ('Oscar','Flores','Male',35,'352 Nelson Ford','Houseport','GA',94961),
    ('Mitchell','Spencer','Male',27,'4565 Harris Curve Suite 744','Richardshire','AL',84498),
    ('Gary','Snyder','Male',30,'48040 Smith Ramp Suite 509','East Francesmouth','MA',38003),
    ('Lisa','Armstrong','Female',32,'5083 Justin Cliffs','West Amy','WY',8481),
    ('Jeremy','Norris','Male',32,'22734 Rivera Knolls Suite 040','Port Thomas','MO',1673),
    ('Michael','Wheeler','Male',29,'403 Glenn Ville Suite 118','East Ericbury','OH',11320),
    ('April','Ross','Female',34,'076 James Rapid Suite 654','West Jessica','MO',42331),
    ('Jessica','Lynch','Female',30,'USNS Andrews','FPO','AA',17102),
    ('Donna','Bray','Female',34,'58964 April Knoll','Hendrixchester','MI',31600),
    ('Carolyn','Williams','Female',34,'875 Rivas Alley','Butlerton','MA',81141),
    ('Lee','Sweeney','Male',25,'USCGC Caldwell','FPO','AA',30090);

