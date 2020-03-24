# Employee Normalizer

In this activity, you will be organizing improperly stored employee data into the three normal forms.

## Instructions

* In pgAdmin, create a new database called `normalization_db`.

* Create a new table `customer_email` according to the provided [customer_email.csv](Resources/customer_email.csv), then import the csv into the `customer_email` table.

* Create a new table `first_nf_customer_email` and insert the `customer_email` data according to 1NF data normalization standards.

* Create two new tables `second_nf_customer` and `second_nf_customer_email` 

* Using SQL, create the following tables with continued normalized practices:

  * A table for owners that has an ID and the owner's name

  * A table for pet names that has two IDs (one being the owner's name) and the pet's name.

* Using the CSV file as guide, insert the data into respective tables.

  **Hint:** Be sure that each table has a *unique primary key*.

### Bonus

* Create a `service` table that displays the different types of services that are offered.

* Create a `pet_names_updated` table that takes an ID that will connect to the `services` table.

* Join all three tables.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
