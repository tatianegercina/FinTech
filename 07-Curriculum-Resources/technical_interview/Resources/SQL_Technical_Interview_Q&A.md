# SQL Technical Interview Questions and Answers

## Joins Are From Descartes, Rows Are From Schemas

### Part 1: Joins

* The outputs of following queries are 25 and 10, respectively.

  ```sql
  SELECT COUNT(*)
  FROM first_table;

  SELECT COUNT(*)
  FROM second_table;
  ```

* What will be the number of rows in the output of the following query?

  ```sql
  SELECT *
  FROM first_table, second_table;
  ```

### Part 2: Joins

* The query `SELECT * FROM table_one;` returns the following:

  ![Images/descartes01.png](Images/descartes01.png)

* And the query `SELECT * FROM table_two;` returns the following:

  ![Images/descartes01.png](Images/descartes02.png)

* What will the query `SELECT * FROM table_one, table_two;` look like?

### Solutions: Joins

* Part 1: The query will return a Cartesian Join, and it will return 250 rows.

* Part 2:

  ![Images/descartes03.png](Images/descartes03.png)

- - -

## Foreign Keys

* The following are a query and output involving two tables. Notice that `department_id` and `id` columns match.

  ```sql
  SELECT * FROM employees e
  JOIN departments d
  ON (e.department_id = d.id)
  WHERE e.department_id = 45;
  ```

  ![Images/foreign01.png](Images/foreign01.png)

* Based on the above, reconstruct the table schemata for `employees` and `departments` tables.

### Solution: Foreign Keys

```sql
CREATE TABLE departments (
  id integer(11) UNIQUE NOT NULL,
  dept_name VARCHAR (255) NOT NULL,
  primary key (id)
);

CREATE TABLE employees (
  employee_id INTEGER(11) UNIQUE NOT NULL,
  first_name VARCHAR (255) NOT NULL,
  last_name VARCHAR (255) NOT NULL,
  department_id INTEGER (11) NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (department_id) REFERENCES departments(id)
);


INSERT INTO departments (id, dept_name) VALUES (25, "data");
INSERT INTO departments (id, dept_name) VALUES (45, "webdev");

INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (3, "Chris", "Christian", 25);
INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (14, "Jan", "Jansson", 45);
INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (17, "Sam", "Samuels", 45);


SELECT * FROM employees e
JOIN departments d
ON (e.department_id = d.id)
WHERE e.department_id = 45;
```

- - -

## ACID

* What are the ACID properties of SQL transactions? If possible, explain each property with an illustration of an example.

### Solution: ACID

* ACID stands for Atomicity, Consistency, Isolation, and Durability.

* Atomicity: each transaction must be all-or-nothing. That is, a transaction takes place if it's only partly completed. In a bank transfer from person A to person B, for example, person B's account cannot be credited unless withdrawal takes place from person A's account.

* Consistency: all constraints are followed for each transaction. Constraints such as keys, data types, uniqueness are followed. The database should remain in a consistent state before and after the transaction.

* Isolation: no transaction affects another transaction. If there are multiple bank transfers, for example, only one can be carried out at the same time, before another one can begin.

* Durability: the transaction will persist in the database after a transaction. For example, after a bank transfer, even if a power outage should take place, the record of the transaction remains intact.

* For another analogy, see [https://stackoverflow.com/questions/3740280/acid-and-database-transactions#3741079](https://stackoverflow.com/questions/3740280/acid-and-database-transactions#3741079).

- - -

## Alter vs. Update

### Part 1: Alter vs. Update

* Explain the difference between `alter` and `update` in SQL statements.

### Part 2: Alter vs. Update

* You are given the following table:

  ![Images/alter_update01.png](Images/alter_update01.png)

* Change the name of the column from `department_id` to `dept_id`.

* Add a column named `annual_salary` to the table.

### Solutions: Alter vs. Update

```sql
-- MySQL
ALTER TABLE employees
CHANGE department_id dept_id VARCHAR(125);

ALTER TABLE employees
ADD annual_salary INT(11);

UPDATE employees
SET annual_salary = 80000
WHERE employee_id = 17;
```

- - -

## The Thrill of the Case

* Change each animal's species to the correct species.

  ![Images/case01.png](Images/case01.png)

### Solution: The Thrill of the Case

```sql
-- MySQL code
CREATE TABLE animals (
  id integer(11) auto_increment not null,
  animal_name varchar(255) not null,
  species varchar(255),
  primary key(id)
);

INSERT INTO animals (animal_name, species) VALUES ("Mickey Mouse", "duck");
INSERT INTO animals (animal_name, species) VALUES ("Minnie Mouse", "duck");
INSERT INTO animals (animal_name, species) VALUES ("Donald Duck", "mouse");

UPDATE animals
SET species =
CASE species
    WHEN "duck" THEN "mouse"
    WHEN "mouse" THEN "duck"
END;
```

- - -

## SQL Joins

### Part 1: SQL Joins

* Describe the different types of join clauses supported in SQL.

### Part 2: SQL Joins

* Consider the following tables:

  * vendor_table

  ![vendor_table](Images/vendor_table.png)

  * yarn_table

  ![yarn_table](Images/yarn_table.png)

* Which join was used to create the final view below?

  ![table_join.png](Images/table_join.png)

### Solutions: SQL Joins

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

- - -

## DML & DDL

### Part 1: DML & DDL

* What is the difference between `DML` and `DDL` in SQL?

### Part 2: DML & DDL

* Demonstrate the use of `DDL` in the following table:

  * vendor_table

    ![vendor_table](Images/vendor_table.png)

### Solutions: DML & DDL

* Part 1: `DML` refers to `Data Manipulation Language`. There are several DML statements used to update, insert, or delete data in a table. `DDL` stands for `Data Definition Language`, which deals with the structure of the data.

  * Examples of `DDL` include `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `COMMENT`, and `RENAME`.

  * `DML` commands include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

* Part 2: several different `DDL` commands are available for use on the table.

  * `DROP` to drop the table altogether.

  * `ALTER` will add one or more columns, modify an existing column, drop a column, rename a column, or rename a table.

  * `CREATE` creates a new table.

  * `DROP` will drop or remove an existing table from a database.

  * `TRUNCATE` will remove all records from an existing table within a database.

  * `COMMENT` is used to add a comment to a data dictionary.

  * `RENAME` can be used to rename existing tables and columns in a database.

- - -

## Index

### Part 1: Index

* Explain an index in SQL.

### Part 2: Index

* What are the different types of `index`? If possible, explain each type with an illustration.

### Solutions: Index

* Part 1: an `index` is used to create indexes in tables. They aid in quick data retrieval by speeding up searches and queries. When creating an index, table data is not changed. Instead, a new data structure is created that refers to the table.

* Part 2: There are three types of index:

  * Unique: if a column is uniquely indexed, no duplicate values will be allowed in the field. If a primary key is already defined, then a unique index is automatically applied.

  * Clustered: this type of index will reorder the physical order of the table and searches based off the key values. Only one clustered index is allowed per table.

  * Non-Clustered: a non-clustered index will not alter the physical form of the table. More than one non-clustered indexes are allowed per table.

- - -

## Duplicates

### Part 1: Duplicates

* How do you locate a duplicate record with one field? Using the table below, write a query to demonstrate.

  * Yarn table with duplicates:

    ![duplicated_yarn.png](Images/duplicated_yarn.png)

### Part 2: Duplicates

* How do you find duplicate records using more than one field? Using the table from Part 1, write a query to demonstrate.

### Solutions: Duplicates

* Part 1:

  ```sql
  SELECT yarn_name, COUNT(vendor_id)
  FROM yarn
  GROUP BY yarn_name
  HAVING COUNT (vendor_id) > 1;
  ```

  * Result:

    ![single_field.png](Images/single_field.png)

* Part 2:

  ```sql
  SELECT yarn_name, vendor_id, COUNT(*)
  FROM yarn
  GROUP BY yarn_name, vendor_id
  HAVING COUNT(*) > 1;
  ```

  * Result:

    ![multi_field.png](Images/multi_field.png)

- - -

## Groupby, Don't Cry

* The below are a pandas data frame preview and a query for the total duration (in seconds) of UFO sightings by state, respectively.

  ![Images/grouby01.png](Images/groupby01.png)

  ![Images/grouby02.png](Images/groupby02.png)

* What is an equivalent SQL query? Instead of the sum, find the mean duration by state.

### Solution: Groupby, Don't Cry

  ```sql
  SELECT state, AVG(duration)
  FROM usa_ufo
  GROUP BY state;
  ```
