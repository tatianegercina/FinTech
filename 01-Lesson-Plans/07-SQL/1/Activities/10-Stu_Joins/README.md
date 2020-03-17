# Joining the NBA

In this activity, you will be using joins to query mortgage information.

### Instructions

1. Create a new database named `payments_db`.

2. Use the `schema.sql` and the pgAdmin Import/Export tool to create the following tables (if not already present):

    * [sales.csv](Resources/sales.csv)

    * [payments.csv](Resources/payments.csv)

    **Note:** Remember to refresh the database; newly created tables will not immediately appear.

3. Perform the following JOINs between the sales and payments table via the common `payment_id`.

    * INNER JOIN

    * LEFT JOIN

    * RIGHT JOIN

    * FULL OUTER JOIN

## Bonus

Perform an INNER JOIN on the `banks` table via the already joined `payments` table to find the sales transactions connected to Wells Fargo bank accounts.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
