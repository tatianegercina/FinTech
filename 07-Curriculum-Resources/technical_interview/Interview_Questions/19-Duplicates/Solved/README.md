# Duplicates

## Part 1

* How do you locate a duplicate record with one field? Using the table below, write a query to demonstrate.

  * Yarn table with duplicates:

    ![duplicated_yarn.png](../Images/duplicated_yarn.png)

## Part 2

* How do you find duplicate records using more than one field? Using the table from Part 1, write a query to demonstrate.

## Solutions

* Part 1:

  ```sql
  SELECT yarn_name, COUNT(vendor_id)
  FROM yarn
  GROUP BY yarn_name
  HAVING COUNT (vendor_id) > 1;
  ```

  * Result:

    ![single_field.png](../Images/single_field.png)

* Part 2:

  ```sql
  SELECT yarn_name, vendor_id, COUNT(*)
  FROM yarn
  GROUP BY yarn_name, vendor_id
  HAVING COUNT(*) > 1;
  ```

  * Result:

    ![multi_field.png](../Images/multi_field.png)
