# Joining the Big Banks

In this activity, you will be using joins to query payment information and associated bank information via a common bank routing number.

## Instructions

1. Create a new database named `payments_db`.

2. Use the `schema.sql` and the pgAdmin Import/Export tool to create the following tables:

    * [payments.csv](Resources/payments.csv)

    * [banks.csv](Resources/banks.csv)

    **Note:** Remember to refresh the database; newly created tables will not immediately appear.

3. Perform the following JOINs between the sales and payments table via the common `bank_routing_number`.

    * INNER JOIN

      ![stu-inner-join](Images/stu-inner-join.png)

    * LEFT JOIN

      ![stu-left-join](Images/stu-left-join.png)

    * RIGHT JOIN

      ![stu-right-join](Images/stu-right-join.png)

    * FULL OUTER JOIN

## Bonus

Perform an INNER JOIN on the `banks` table via the already joined `payments` table to find the sales transactions connected to Wells Fargo bank accounts.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
