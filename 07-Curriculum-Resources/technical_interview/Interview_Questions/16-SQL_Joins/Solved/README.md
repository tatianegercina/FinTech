# SQL Joins

## Part 1

* Describe the different types of join clauses supported in SQL.

## Part 2

* Consider the following tables:

  * vendor_table
  ![vendor_table](../Images/vendor_table.png)

  * yarn_table
  ![yarn_table](../Images/yarn_table.png)

* Which join was used to create the final view below?

  ![table_join.png](../Images/table_join.png)

## Solutions

* Part 1:

  * An inner join will return records at the intersection between two tables.

  * A left join will return all records from Table A and the matching records from Table B.

  * A right join returns all records from Table B and the matching records from Table A.

  * A full join returns a list of all records from both tables.

* Part 2: There are two ways to join these tables.

  * A `Left Join` is performed with the vendor table as the first table referenced (Table A in the explanation above) and the yarn table as the second (Table B).

    ```sql
    SELECT vendors.vendor_name, vendors.vendor_country, yarn.yarn_name, yarn.yarn_type
    FROM vendors
    LEFT JOIN yarn ON
    vendors.id = yarn.vendor_id;
    ```

  * Alternatively, a `Right Join` can also be performed. The difference is that the order of the tables referenced is reversed.

    ```sql
    SELECT vendors.vendor_name, vendors.vendor_country, yarn.yarn_name, yarn.yarn_type
    FROM yarn
    RIGHT JOIN vendors ON
    yarn.vendor_id = vendors.id;
    ```
