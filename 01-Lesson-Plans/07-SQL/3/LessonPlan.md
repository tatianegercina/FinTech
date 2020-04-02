## 7.3 Lesson Plan: Data Modeling

### Overview

Today's class will focus on data modeling and best practices for designing a database. Students will learn how to normalize data and how tables in a database are related, as well as how to create visualizations of databases using entity relationship diagrams (ERDs).

### Class Objectives

By the end of today's class, students will be able to:

* Apply data modeling techniques to database design.

* Normalize data.

* Identify data relationships.

* Create visual representations of a database through entity relationship diagrams.

### Instructor Notes

* If you experience any issues importing data as CSV files via pgAdmin, please refer to the SQL troubleshooting [guide](../Supplemental/SQL_troubleshooting_guide.md).

* This lesson is less heavy on pure SQL, which will be used mainly to supplement the ideas presented today. If students continue to struggle with SQL basics, encourage them to practice on their own while still focusing on the concepts in this lesson.

* The TAs should be ready to help explain and break down concepts for students struggling to grasp the material.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [7.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b512f6ac-ee8f-441e-8f26-aac6015c140c) Note that this video may not reflect the most recent lesson plan.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1PNx_qkrRTq-5wmpMXD5DeHXbfaGs5ogLdPa2Ee9GqmQ/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students and explain that today's lesson will dive into data modeling techniques such as normalization, relationships, and how to conceptualize database design using entity relationship diagrams (ERDs).

Open the Class Objectives slide and review the objectives for today's class.

### 2. Instructor Do: Data Normalization (15 min)

In this activity, students will be introduced to the three normal forms of data normalization.

**Note:** The data normalization procedures represented in the following slideshow are provided in the .sql files below. Use them as necessary if students have questions pertaining to the data itself or just want to have the code on hand.

**Files:**

* [normalization.md](Activities/01-Ins_Data_Normalization/Solved/normalization.md)

* [schema.sql](Activities/01-Ins_Data_Normalization/Solved/schema.sql)

* [seed.sql](Activities/01-Ins_Data_Normalization/Solved/seed.sql)

* [query.sql](Activities/01-Ins_Data_Normalization/Solved/query.sql)

Review the slides on data normalization, explaining the following:

* Data normalization is the process of restructuring data to a set of defined "normal forms."

* The process of data normalization eliminates data redundancy and inconsistencies.

* We will be covering the three main forms of normalization, though additional forms exist.

* In **first normal form**, or 1NF, each row contains a single value, and each row is unique. In this example, each family's children are all listed in one row. The data is normalized into 1NF by creating a new row for each child.

* In **second normal form**, or 2NF, the data is in 1NF. Additionally, all non-key columns are dependent on the primary key for the table. In this example, there are two tables. The Family table has the primary key `parent_id`, and the Child table has the primary key `child_id`.

* Notice that `family_id` is added to the Child table. Since this is not a primary key, there can be non-unique values that relate to the Family table.

* **Transitive dependency** is a column value's reliance on another column through a third column. The transitive property states that if X > Y and Y > Z, then we can infer that X > Z. Dependence means that one value relies on another, such as city on ZIP code, or age on birthday.

* For example, let's say that a table has three columns: `StoreName`, `OwnerAddress`, and `OwnerName`.

  * `OwnerName` and `OwnerAddress` rely on `StoreName`. `OwnerAddress` also depends on `OwnerName`.

  * Therefore, `OwnerAddress` is transitively dependent on `StoreName` through `OwnerName`.

* **Third normal form**, or 3NF, has the data normalized to second form and contains non-transitively-dependent columns.

* In the previous example, two tables are created:

  * The Owners table has the `OwnerName` and `OwnerAddress`, both of which depend only on the `owner_id`.

  * The Stores table contains the `store_name`, which is dependent on the primary key `store_id`.

  * The Stores table also contains an `owner_id` that creates a relationship with the Owners table.

Note that students may find 3NF a bit confusing. Encourage students to learn more about 3NF on their own. Today's lesson will mainly focus on 1NF and 2NF.

Slack out [normalization.md](Activities/01-Ins_Data_Normalization/Solved/normalization.md) as a cheat sheet for students before moving on.

### 3. Student Do: Employee Normalizer (15 min)

In this activity, students will practice their data normalization skills using the provided data.

**File:** [employee_normalization.csv](Activities/02-Stu_Data_Normalization/Resources/employee_normalization.csv)

**Instructions:** [README.md](Activities/02-Stu_Data_Normalization/README.md)

### 4. Instructor Do: Review Employee Normalizer (5 min)

**Files:**

* [schema.sql](Activities/02-Stu_Data_Normalization/Solved/schema.sql)

* [seed.sql](Activities/02-Stu_Data_Normalization/Solved/seed.sql)

* [query.sql](Activities/02-Stu_Data_Normalization/Solved/query.sql)

Open [employee_normalization.csv](Activities/02-Stu_Data_Normalization/Resources/employee_normalization.csv) and explain the first step of normalization:

* To achieve first normal form, multiple data points should not be included in the same column. For columns containing multiple emails, a new row will need to be created for each email.

Next, using the code from the schema.sql and seed.sql files, create and populate the tables in pgAdmin. Then use the query.sql file to explain the following:

* The `first_nf_employee` table separates out the data from `employee_normalization` into records with atomic or single column values.

  ```sql
  INSERT INTO employee_normalization
    (employee_id, name, age, address, city, state, zip_code, email)
  VALUES
    (123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robert.bale51231@gmail.com, robbieman512@gmail.com'),
    (456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'anya.strensa1412@gmail.com, soccergirl4251@gmail.com'),
    (789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016, 'arnold.tolenski5121@gmail.com');

  INSERT INTO first_nf_employee
    (employee_id, name, age, address, city, state, zip_code, email)
  VALUES
    (123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robert.bale51231@gmail.com'),
    (123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002, 'robbieman512@gmail.com'),
    (456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'anya.strensa1412@gmail.com'),
    (456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami', 'FL', 33101, 'soccergirl4251@gmail.com'),
    (789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016, 'arnold.tolenski5121@gmail.com');
  ```

* In order to achieve second normal form, the data in `first_nf_employee` should be separated out to the `second_nf_employee` and `second_nf_employee_email` tables. Each table should represent a specific contextual domain, such as employee and email attributes, and should contain unique primary keys in which all non-ID columns are dependent. Note that the two tables are still connected by the common `employee_id` column.

  ```sql
  INSERT INTO second_nf_employee
    (employee_id, name, age, address, city, state, zip_code)
  VALUES
    (123, 'Robert Bale', 32, '31 Pelham Drive', 'Houston', 'TX', 77002),
    (456, 'Anya Strensa', 25, '142 Sunshine Road', 'Miami',' FL', 33101),
    (789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 'San Francisco', 'CA', 94016);

  INSERT INTO second_nf_employee_email
    (email_id, employee_id, email)
  VALUES
    (1, 123, 'robert.bale51231@gmail.com'),
    (2, 123, 'robbieman512@gmail.com'),
    (3, 456, 'anya.strensa1412@gmail.com'),
    (4, 456, 'soccergirl4251@gmail.com'),
    (5, 789, 'arnold.tolenski5121@gmail.com');
  ```

* In order to achieve third normal form, the data in `second_nf_employee` should be separated out to the `third_nf_employee` and `third_nf_zipcode` tables. The reason for this is that the data within the `second_nf_employee` table contains dependencies on non-primary key attributes. In other words, the `city` and `state` columns are dependent on the `zip_code` column and therefore should be separated out into their own table.

  ```sql
  INSERT INTO third_nf_employee
    (employee_id, name, age, address, zip_code)
  VALUES
    (123, 'Robert Bale', 32, '31 Pelham Drive', 77002),
    (456, 'Anya Strensa', 25, '142 Sunshine Road', 33101),
    (789, 'Arnold Tolenski', 43, '15 Silicon Avenue', 94016);

  INSERT INTO third_nf_zipcode
    (zip_code, city, state)
  VALUES
    (77002, 'Houston', 'TX'),
    (33101, 'Miami', 'FL'),
    (94016, 'San Francisco', 'CA');
  ```

Explain the bonus section of the activity:

* Data normalization separated our initial unorganized data into several tables; however, if we needed to retrieve information represented from the initial dataset, we can perform JOINs on the normalized tables.

  ```sql
  SELECT *
  FROM third_nf_employee AS a
  LEFT JOIN second_nf_employee_email AS b ON a.employee_id = b.employee_id
  LEFT JOIN third_nf_zipcode AS c ON a.zip_code = c.zip_code;
  ```

### 5. Instructor Do: Intro to Foreign Keys (15 min)

In this activity, students will be introduced to the concept of foreign keys -- columns designated as matching links or relations to another table.

**Files:**

* [schema.sql](Activities/03-Ins_Foreign_Keys/Solved/schema.sql)

* [seed.sql](Activities/03-Ins_Foreign_Keys/Solved/seed.sql)

* [query.sql](Activities/03-Ins_Foreign_Keys/Solved/query.sql)

Use the slides on foreign keys to explain the concept of foreign keys and how they are used to connect tables:

* A foreign key is a link between tables. The foreign key in the first table points to or is linked to, the primary key in a second table.

* A foreign key also prevents invalid data from being entered into a column. The data being entered MUST be a value from the referenced column.

Slack out the schema.sql, seed.sql, and query.sql files for students to follow along. Review the code, explaining the following steps:

* Use the `CASCADE` modifier in addition to the `DROP TABLE IF EXISTS` clause to drop any existing tables that may include foreign key constraints to other tables.

  ```sql
  DROP TABLE IF EXISTS customer CASCADE;
  DROP TABLE IF EXISTS customer_email CASCADE;
  DROP TABLE IF EXISTS customer_phone CASCADE;
  ```

* Create a table named `customer` and set the primary key to `customer_id`, which will be auto-populated and incremented with each new entry.

  ```sql
  CREATE TABLE customer (
    customer_id SERIAL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (customer_id)
  );
  ```

* Insert data into the `customer` table, and then run a `SELECT` query to double-check that data has been inserted.

  ```sql
  INSERT INTO customer
    (first_name, last_name)
  VALUES
    ('Bob', 'Smith'),
    ('Jane', 'Davidson'),
    ('Jimmy', 'Bell'),
    ('Stephanie', 'Duke');

  SELECT * FROM customer;
  ```

* Point out that a new table is created, and its primary key is labeled `customer_id`. As a result, the `customer_id` will be unique to this table.

  ![customer_table](Images/Foreign_Keys11.png)

* The `customer_email` table references the `customer` table in its column definition `FOREIGN KEY (customer_id) REFERENCES customer(customer_id)` where it establishes the `customer_id` column as a foreign key relationship to the `customer_id` column in the `customer` table.

  ```sql
  CREATE TABLE customer_email (
    email_id SERIAL,
    customer_id INTEGER NOT NULL,
    email VARCHAR(30) NOT NULL,
    PRIMARY KEY (email_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  );
  ```

* Similarly, the `customer_phone` table references the `customer` table in its column definition `FOREIGN KEY (customer_id) REFERENCES customer(customer_id)` where it establishes the `customer_id` columns as a foreign key relationship to the `customer_id` column in the `customer` table.

  ```sql
  CREATE TABLE customer_phone (
      customer_phone_id SERIAL,
      phone VARCHAR(30) NOT NULL,
      customer_id INTEGER NOT NULL,
      PRIMARY KEY (customer_phone_id),
      FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
  );
  ```

* Populating the tables respectively and querying the tables exemplifies the foreign key relationship.

  ```sql
  INSERT INTO customer_email
    (customer_id, email)
  VALUES
    (1, 'bobsmith@email.com'),
    (2, 'jdavids@email.com'),
    (3, 'jimmyb@email.com'),
    (4, 'sd@email.com');
  ```

  ![customer_email_table](Images/Foreign_Keys22.png)

  ```sql
  INSERT INTO customer_phone
    (customer_id, phone)
  VALUES
    (1, '435-344-2245'),
    (2, '332-776-4678'),
    (3, '221-634-7753'),
    (4, '445-663-5799');
  ```

  ![customer_phone_table](Images/Foreign_Keys33.png)

Recap the following:

* The `customer_id` column is the primary key of the `customer` table, while `customer_id` is a foreign key in the `customer_email` and `customer_phone` tables.

* The `customer_id` column in both the `customer_email` and `customer_phone` tables are designed to contain the same `customer_id` data in the `customer` table. This is due to the foreign key relationship in which the `customer_id` of the `customer` table is linked.

* SQL will throw an error if an attempt is made to change a `customer_id` in one table but not the other.

* Foreign key columns need to be named appropriately in order to clarify the data they are referring to.

Students should now understand how to create foreign keys, as well as how to use them to reference data in other tables. Use the following example to illustrate the importance of foreign keys:

* Foreign keys allow tables to be consistent and avoid issues caused by inserting, deleting, or updating one table without making those same changes in the other tables.

* When attempting to insert a row into the new table with a `customer_id` that does not exist in the other table, an error will be returned.

  ```sql
  INSERT INTO customer_email
    (email, customer_id)
  VALUES
    ('lucystern@gmail.com', 5);
  ```

  ![fk-constraint-error](Images/fk-constraint-error.png)

* Explain that the `customer_id` column is a foreign key that is assigned to the `customer_id` column in the `customer` table. The `customer_id` 5 doesn't exist in the `customer` table and therefore can't be referenced in the `customer_email` table.

* Next, a new row is inserted into `customer` that will have a `customer_id` of 5 (due to `customer_id` being a serial or incremental primary key). Now a row can be inserted into `customer_email` with a `customer_id` of 5 because it corresponds with a `customer_id` in the `customer` table.

  ```sql
  INSERT INTO customer
    (first_name, last_name)
  VALUES
    ('Lucy', 'Stern');

  INSERT INTO customer_email
    (email, customer_id)
  VALUES
    ('lucystern@gmail.com', 5);
  ```

* Check that the row was inserted using a `SELECT * FROM customer_email` query.

  ![fk-constraint-error-resolved](Images/fk-constraint-error-resolved.png)

Answer any questions students have about foreign keys. Then ask students if they can think of other real-world cases in which the use of foreign keys makes sense. Here are two examples:

* States and countries in addresses: Think back to the `rental` database, where streets, addresses, cities, and countries were stored in different tables. So, for example, if a change occurs to the address of a customer, all information across all tables would need to change. This is called maintaining the **referential integrity**.

* ID number of employees: In a database where the ID number of an employee is used in multiple tables, what happens if the employee's ID number changes? The ID number would need to be changed across all the tables that contain it.

Emphasize that using foreign keys to build relationships across data is a feature of relational databases, hence the name.

### 6. Student Do: Foreign Keys (15 min)

In this activity, students will create tables with foreign keys.

**Files**:

* [owners.csv](Activities/04-Stu_Foreign_Keys/Resources/owners.csv)

* [estates.csv](Activities/04-Stu_Foreign_Keys/Resources/estates.csv)

**Instructions:** [README.md](Activities/04-Stu_Foreign_Keys/README.md)

### 7. Instructor Do: Review Foreign Keys (5 min)

**Files**:

* [schema.sql](Activities/04-Stu_Foreign_Keys/Solved/schema.sql)

* [seed.sql](Activities/04-Stu_Foreign_Keys/Solved/seed.sql)

* [query.sql](Activities/04-Stu_Foreign_Keys/Solved/query.sql)

Using the `schema.sql`, `seed.sql` files in pgAdmin, walk through the code and explain the following:

* The `owner` and `estates` tables are linked via a foreign key relationship from the `owner_id` of the `estates` table to the `owner_id` of the `owner` table.

  ```sql
  -- Create owners table and insert values
  CREATE TABLE owners (
    owner_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
  );

  -- Create estates table and insert values
  CREATE TABLE estates (
    id INT NOT NULL PRIMARY KEY,
    owner_id INT NOT NULL,
    address VARCHAR(255),
    city VARCHAR (255),
    state VARCHAR(255),
    zip_code VARCHAR(255)
  );
  ```

* Foreign keys should enforce **referential integrity**, therefore if we attempt to insert a record into the `estates` table with an `owner_id` of 10, the following error will output as there is no record in the `owners` table where `owner_id` is `10`.

  ```sql
  INSERT INTO estates
    (estate_id, owner_id, address, city, state, zip_code)
  VALUES
    (9, 10, '23 Delafield Avenue', 'New Brunswick', 'NJ', 08901);
  ```

  ![student-fk-constraint-error](Images/student-fk-constraint-error.png)

* To alleviate the issue, a new record with an `owner_id` of 10 should first be added to the `owner` table. Then, re-attemping the insert into the `estates` table should succeed.

  ```sql
  INSERT INTO owners
    (owner_id, first_name, last_name)
  VALUES
    (10, 'David', 'Stone')
  ```

* Explain that the `owners` and `estates` tables can be joined together by their mutual `owner_id` columns.

  ```sql
  SELECT *
  FROM owners
  INNER JOIN estates ON owners.owner_id = estates.owner_id;
  ```

* For the bonus, the `estate_type` and `estates_new` tables are linked by the mutual `estate_type_id`.

  ```sql
  CREATE TABLE estate_type (
  estate_type_id INT NOT NULL PRIMARY KEY,
  estate_type VARCHAR(255)
  );

  CREATE TABLE estates_new (
    estate_id INT NOT NULL PRIMARY KEY,
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id),
    address VARCHAR(255),
    city VARCHAR (255),
    state VARCHAR(255),
    zip_code VARCHAR(255),
    estate_type_id INT,
    FOREIGN KEY (estate_type_id) REFERENCES estate_type(estate_type_id)
  );
  ```

* Lastly, the `owners`, `estates_new`, and `estate_type` tables can be joined together by the mutual `owner_id` and `estate_type_id`, respectively.

  ```sql
  SELECT *
  FROM owners
  INNER JOIN estates_new ON owners.owner_id = estates_new.owner_id
  INNER JOIN estate_type ON estates_new.estate_type_id = estate_type.estate_type_id;
  ```

### 8. Instructor Do: Intro to Data Relationships (10 min)

In this activity, students will learn the many different types of data modeling relationships that one table can have with another: one-to-one, one-to-many, and many-to-many.

**Files:**

* [schema.sql](Activities/05-Ins_Data_Relationships/Solved/schema.sql)

* [seed.sql](Activities/05-Ins_Data_Relationships/Solved/seed.sql)

* [query.sql](Activities/05-Ins_Data_Relationships/Solved/query.sql)

Use the `Data Relationships` slides to explain that we will now cover one-to-one, one-to-many, and many-to-many relationships between data, which is an essential part of data modeling.

Begin by discussing one-to-one relationships. This example will use members of the Simpson family to illustrate the concept.

* In a one-to-one relationship, each name is associated with one and only one Social Security number. In other words, each item in a column is linked to only one item from another column.

  ![Images/one-to-one.png](Images/one-to-one.png)

Next, discuss one-to-many relationships. We'll continue with our Simpsons example, but add Sherlock Holmes and his sidekick Watson to the database.

  ![Images/one-to-many1.png](Images/one-to-many1.png)

* This example has two tables. The first table lists only addresses. The second table lists each person's social security number and address id.

* As before, one Social Security number is unique to one individual.

Discuss one-to-many relationships.

* Each individual has one address; however, a single address can be shared between multiple individuals. The Simpson family has a shared address at `742 Evergreen Terrace`, while Sherlock and Watson share the `221B Baker Street` address.

* In a one-to-many relationship, the data from one table can be repeated for items in another table.

Ask students to think of another example of real-life one-to-many relationships.

* One possible example is a purchase order with an internet company. Each order has a unique identifying number.

* A customer might be associated with multiple orders, but each order is associated with one and only one customer.

Discuss many-to-many relationships.

* Continuing with our Simpsons example, there are three children (Lisa, Bart, and Maggie), and two parents (Homer and Marge).

  ![Images/many-to-many1.png](Images/many-to-many1.png)

* In this case, there are two tables: one for children and another for parents.

* Each child here has many parents, and each parent has many children. Each child has a separate row for each parent and vice versa.

  ![Images/many-to-many2.png](Images/many-to-many2.png)

* Many-to-many relationships require a separate table, called a **junction table**, to show the relationships.

Ask the class what many-to-many relationships might be found in an online retailer database such as Amazon's: A customer can order many different items, and many different customers can order each item.

Demonstrate the creation of a junction table in Postgres.

* First, open the [schema.sql](Activities/05-Ins_Data_Relationships/Solved/schema.sql) and [seed.sql](Activities/05-Ins_Data_Relationships/Solved/seed.sql) files and paste in the queries to create and insert data into the `children` and `parents` tables, respectively. There are two separate tables:

  ![Images/modeling01.png](Images/modeling01.png)

  ![Images/modeling02.png](Images/modeling02.png)

Now walk through the junction table schema:

  ```sql
  CREATE TABLE child_parent (
    child_id INTEGER NOT NULL,
    FOREIGN KEY (child_id) REFERENCES children(child_id),
    parent_id INTEGER NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES parents(parent_id),
    PRIMARY KEY (child_id, parent_id)
  );
  ```

* The `child_id` and `parent_id` columns are both linked to the previously created tables as foreign keys.

* Additionally, the primary key in this table is a **composite key**, made up of both the `child_id` and `parent_id` keys.

* This means that the unique identifier for a row is not a single column, but rather the composite of both columns.

Show the junction table:

  ![Images/modeling03.png](Images/modeling03.png)

Finally, go through the `JOIN` query to display the data in full:

  ![Images/modeling04.png](Images/modeling04.png)

  ```sql
  SELECT children.child_name, child_parent.child_id, parents.parent_name, child_parent.parent_id
  FROM children
  LEFT JOIN child_parent
  ON child_parent.child_id = children.child_id
  LEFT JOIN parents
  ON child_parent.parent_id = parents.parent_id;
  ```

* The `children` table has a left join with the junction table, the results of which then have a left join with the `parents` table.

Take a moment to summarize the major points of the activity:

* Data can be modeled as one-to-one, one-to-many, and many-to-many relationships.

* Many-to-many relationships require a junction table.

* Junction tables use foreign keys to reference the keys in the original tables.

Ask if there are any questions before moving on.

### 9. Student Do: Data Relationships (10 min)

In this activity, students will create table schemata for agents and regions, and then create a junction table to display all regions assigned to agents.

**Files:**

* [agents.csv](Activities/06-Stu_Data_Relationships/Resources/agents.csv)

* [regions.csv](Activities/06-Stu_Data_Relationships/Resources/regions.csv)

* [agent_region_junction](Activities/06-Stu_Data_Relationships/Resources/agent_region_junction.csv)

**Instructions:** [README.md](Activities/06-Stu_Data_Relationships/README.md)

### 10. Instructor Do: Review Data Relationships (5 min)

**Files:**

* [schema.sql](Activities/06-Stu_Data_Relationships/Solved/schema.sql)

* [seed.sql](Activities/06-Stu_Data_Relationships/Solved/seed.sql)

* [query.sql](Activities/06-Stu_Data_Relationships/Solved/query.sql)

Explain that this activity required creating separate tables for agents and regions as well as creating a junction table to reflect the many-to-many relationship between the two tables.

Use the schema.sql and seed.sql files to walk through the creation and population of the `agents` and `regions` tables. Explain the following:

* The `agents` and `regions` tables each have their own respective IDs as their primary key.

* The `agents` and `regions` tables have additional columns or fields that pertain to the specific context of the table. For example, the `first_name` and `last_name` columns relate to the `agent_id` and represent the real estate agent's first and last name.

  ```sql
  CREATE TABLE agents (
    agent_id INT PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
  );

  CREATE TABLE regions (
    region_id INT NOT NULL PRIMARY KEY,
    region_name VARCHAR NOT NULL
  );
  ```

* Unlike the `agents` and `regions` tables, the `agent_region_junction` table defines foreign key relationships (to the `agents` and `regions` tables) and sets a composite or multi-value key as its primary key.

  ```sql
  CREATE TABLE agent_region_junction (
    agent_id INT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
    region_id INTEGER NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(region_id),
    PRIMARY KEY (agent_id, region_id)
  );
  ```

* New agent or regions data cannot be inserted into the `agent_region_junction` table that does not currently exist in the `agents` or `regions` tables.

* This table bridges the two previous tables and shows all regions managed by each agent.

* The primary key will be a composite key of both IDs.

Query the table to display the result.

  ![Images/modeling07.png](Images/modeling07.png)

To reinforce the many-to-many relationship, point out that many agents can be assigned many regions.

For the bonus, briefly explain that two left outer joins can be performed to retrieve complete data on each agent.

  ```sql
  SELECT *
  FROM agents a
  LEFT JOIN agent_region_junction b ON a.agent_id = b.agent_id
  LEFT JOIN regions c ON b.region_id = c.region_id;
  ```

  ![Images/modelingfpng](Images/modeling08.png)

---

### 11. BREAK (40 min)

---

### 12. Instructor Do: Connecting Pandas with PostgreSQL (10 min)

In this activity, students will learn how to create a connection from Python to PostgreSQL using [SQLAlchemy](https://www.sqlalchemy.org/) to load data into a Pandas DataFrame.

**Files:**

* [connecting_pandas_sql.ipynb](Activities/07-Ins_Connecting_Pandas_SQL/Solved/connecting_pandas_sql.ipynb)

* [schema.sql](Activities/07-Ins_Connecting_Pandas_SQL/Solved/schema.sql)

* [seed.sql](Activities/07-Ins_Connecting_Pandas_SQL/Solved/seed.sql)

* [query.sql](Activities/07-Ins_Connecting_Pandas_SQL/Solved/query.sql)

Tell students that the SQLAlchemy library allows interaction between PostgreSQL and Python. Students should install this library on their virtual environment by executing the following command in the terminal:

```bash
conda install -c anaconda sqlalchemy
```

Make sure all students have installed SQLAlchemy. Then open the unsolved Jupyter Notebook file and live code the solution while highlighting the following:

* SQLAlchemy offers several functionalities to interact with databases from Python.

* This activity is focused on retrieving data from a PostgreSQL database to create a DataFrame for data analysis and visualization in Python.

* To create a connection to the database, import the [`create_engine` function](https://docs.sqlalchemy.org/en/13/core/engines.html) from `sqlalchemy`.

  ```python
  from sqlalchemy import create_engine
  ```

* We can connect to the database by calling the `create_engine` function and passing the database URL. In this example, we use the `estate_db` database that was created earlier, along with the default database username and password.

  ```python
  engine = create_engine("postgresql://postgres:postgres@localhost:5432/estate_db")
  ```

* The structure of the database URL is defined as follows:

  ![SQLAlchemy URL structure](Images/sqlalchemy_url.png)

* To retrieve data from the database, we first need to define a SQL query that fetches the data we want.. In this example, all the rows from the `owners` table are retrieved.

  ```python
  query = "SELECT * FROM owners;"
  ```

* The DataFrame is created by using the [`read_sql()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) in Pandas. This function reads a SQL query or database table into a DataFrame. Two parameters are passed: the `query` and the `engine` instance that were defined earlier.

  ```python
  owners_df = pd.read_sql(query, engine)
  ```

Explain to students that once the data from the database is in a DataFrame, we can perform any data processing, analysis, or visualization task.

* The data from the `owners` DataFrame is shown. You can see that the data from the `owners` table is now loaded into the DataFrame.

  ![Sample DataFrame records](Images/owners_df.png)

* A new query is defined to count the number of estates per owner. The query performs a left join to the `estates_new` and `estate_type` tables and uses the `CONCAT` function to concatenate or combine the `first_name` and `last_name` columns of the `owner` table. This allows us to group by the full name of the owner, and makes for viewing the results more aesthetically pleasing (rather than just an `owner_id`).

  ```python
  query = """
  SELECT CONCAT(owners.first_name, ' ', owners.last_name) as owner_name, COUNT(estate_id) as estate_count
  FROM owners
  LEFT JOIN estates_new ON owners.owner_id = estates_new.owner_id
  LEFT JOIN estate_type ON estates_new.estate_type_id = estate_type.estate_type_id
  GROUP BY CONCAT(owners.first_name, ' ', owners.last_name)
  """
  ```

* The `estate_count_df` DataFrame is created to read the query, and a bar chart is created using `hvplot` to present the results.

  ```python
  estate_count_df = pd.read_sql(query, engine)
  ```

  ![Sample bar chart](Images/sample_bar_char_sqlalchemy.png)

Answer any questions before moving on.

### 13. Student Do: Feeding Pandas with SQL (5 min)

In this activity, students will read data into a Pandas DataFrame from a PostgreSQL database using SQLAlchemy.

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/08-Stu_Feeding_Pandas_SQL/Unsolved/stu_feeding_pandas_sql.ipynb)

**Instructions:**

* [README.md](Activities/08-Stu_Feeding_Pandas_SQL/README.md)

### 14. Instructor Do: Feeding Pandas with SQL Review (5 min)

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/08-Stu_Feeding_Pandas_SQL/Solved/stu_feeding_pandas_sql.ipynb)

* [schema.sql](Activities/08-Stu_Feeding_Pandas_SQL/Solved/schema.sql)

* [seed.sql](Activities/08-Stu_Feeding_Pandas_SQL/Solved/seed.sql)

* [query.sql](Activities/08-Stu_Feeding_Pandas_SQL/Solved/query.sql)

Walk through the solution and highlight the following:

* In order to create the connection to the PostgreSQL database, the `create_engine` function is imported from `sqlalchemy`.

  ```python
  from sqlalchemy import create_engine
  ```

* The database URL is defined in the `db_url` variable, and then it's passed as a parameter to the `create_engine` function.

  ```python
  # Define the database URL
  db_url = "postgresql://postgres:postgres@localhost:5432/agent_db"

  # Create the engine object
  engine = create_engine(db_url)
  ```

* The `agents_df` DataFrame is created by reading a SQL query that fetches all the records from the `agents` table.

  ```python
  # Write the SQL query
  query = "SELECT * FROM agents"

  # Read the SQL query into a DataFrame
  agents_df = pd.read_sql(query, engine)
  ```

* A DataFame called `agent_region_df` is created to fetch the count of regions per agent_id.

  ```python
  # Write the SQL query
  query = """
  SELECT agent_id, COUNT(region_id) as region_count
  FROM agent_region_junction
  GROUP BY agent_id
  """

  # Read the SQL query into a DataFrame
  agent_region_df = pd.read_sql(query, engine)
  ```

* The bar chart is created using `hvplot` and the `agent_region_df` DataFrame.

  ```python
  # Create the bar chart usig hvplot
  agent_region_df.hvplot.bar(
    x="agent_id",
    y="region_count",
    xlabel="Agent ID",
    ylabel="Region Count",
    title="Number of Regions per Agent",
    color="region_count",
  )
  ```

  ![regions_per_agent](Images/regions_per_agent.png)

* For the first bonus, in order to get the number of regions per agent full name, we will need to join to the `agents` table from the `agent_region_junction` table and use the `CONCAT` function to combine the agent `first_name` and `last_name` to form the agent full name. Then group by the concatenated agent full name.

  ```python
  query = """
  SELECT CONCAT(a.first_name, ' ', a.last_name) as agent_name, COUNT(region_id) as region_count
  FROM agents as a
  LEFT JOIN agent_region_junction as b ON a.agent_id = b.agent_id
  GROUP BY CONCAT(a.first_name, ' ', a.last_name)
  """
  ```

  ![regions-per-agent-full-name](Images/regions-per-agent-full-name.png)

* For the second bonus, in order to get the number of agents per region name, we will need to join all three tables to then group by the region name and count the number of agents.

  ```python
  query = """
  SELECT region_name, COUNT(a.agent_id) as agent_count
  FROM agents a
  LEFT JOIN agent_region_junction b ON a.agent_id = b.agent_id
  LEFT JOIN regions c ON b.region_id = c.region_id
  GROUP BY c.region_name
  """
  ```

  ![agents-per-region](Images/agents-per-region.png)

Answer any questions before moving on.

### 15. Instructor Do: Entity Relationship Diagrams (10 min)

In this activity, students will learn how to interpret and create an Entity Relationship Diagram (ERD) -- an asset that delineates the relationship among tables in a database.

**Files:**

* [pagila-erd.png](Images/pagila-erd.png)

* [schema.txt](Activities/09-Ins_ERD/Solved/schema.txt)

Use the ERD slides and begin the discussion of entity relationship diagrams (ERDs). Explain the following points:

* An **entity relationship diagram**, or **ERD**, is a visual representation of entity relationships within a database.

* ERDs are commonly interchanged with the term **data model**, as an ERD describes the relationships of tables within a database and therefore describes a model of a potential database.

* An ERD defines entities, their attributes, and data types, as well as illustrates the overall design of a database.

* There are three types of ERDs or data models: **conceptual**, **logical**, and **physical**. As the following image demonstrates, a conceptual data model is the simplest form, describing only entity names and relationships; a logical database model further expands upon the conceptual data model by additionally describing attributes or column names as well as primary and foreign key definitions; a physical data model expands upon the logical data model to additionally include column data types and specific naming conventions.

  ![conceptual-vs-logical-vs-physical](Images/conceptual-vs-logical-vs-physical.png)

* The following break-down should provide a better understanding of the differences between the three data models.

  ```
  |----------------------|------------|---------|----------|
  | Feature              | Conceptual | Logical | Physical |
  |----------------------|------------|---------|----------|
  | Entity Names         | X          | X       |          |
  | Entity Relationships | X          | X       |          |
  | Attributes           |            | X       |          |
  | Primary Keys         |            | X       |          |
  | Foreign Keys         |            | X       |          |
  | Table Names          |            |         | X        |
  | Column Names         |            |         | X        |
  | Column Data Types    |            |         | X        |
  |----------------------|------------|---------|----------|
  ```

Further expand upon the concepts of ERDs by discussing the following example.

* In a database, the table is an entity; the data contained within the table are attributes; and the data type specified could be one of many things, such as Booleans, integers, or varying characters.

* In an entity relationship diagram, the relationships between entities are given a visual representation. This allows clear and concise joins between tables as well as a deeper understanding of the data contained within a database as a whole.

* ERDs are used both to document existing databases and to aid in the creation of new databases.

Open [Quick Database Diagrams (Quick DBD)](https://app.quickdatabasediagrams.com/#/) and briefly explain its components.

**Note:** If this is the first time you are visiting the site, exit from the tour and clear the text on the left. If the site requires a sign-in, do so using your GitHub account.

* The pane on the left of the window is where users insert the text used to create the entities of a database.

* The blue text signifies the name of the table containing the entities in a database.

* The white pane to the right is where the diagram is drawn, based on the text entered in the left pane.

  ![QDB-demo.png](Images/QDB-demo.png)

* Once a diagram has been finalized, it can be exported in many formats from the **Export** tab at the top of the page.

  ![QDB-export.png](Images/QDB-export.png)

  **Note**: When exporting the diagram as **PostgreSQL**, the table schemata are automatically generated.

With the design tool open in your browser, demonstrate how to begin setting up a simple conceptual data model based on today's activities:

  ```sql
  Employee
  -

  Zipcode
  -

  Employee_Email
  -

  Owners
  -

  Estates
  -

  Estate_Type
  -

  Agents
  -

  Regions
  -

  Agent_Region_Junction
  -
  ```

* The result should appear as follows:

  ![conceptual-erd.png](Images/conceptual-ERD.png)

  **Note**: The tables' locations can be physically adjusted by clicking and dragging them in the browser.

* Explain to the class that at this point, the conceptual data model contains entities; however, it does not have any entity relationships. In order to create the relationships between tables, use the `rel <entity-name>` syntax to create abstract relationships between tables.

  ```sql
  Employee
  rel Zipcode
  -

  Zipcode
  -

  Employee_Email
  rel Employee
  -

  Owners
  -

  Estates
  rel Owners
  rel Estate_Type
  rel Zipcode
  -

  Estate_Type
  -

  Agents
  -

  Regions
  -

  Agent_Region_Junction
  rel Agents
  rel Regions
  -
  ```

* The results should now appear as follows:

  ![conceptual-data-model-entities](Images/conceptual-data-model-entities.png)

Begin transitioning from the conceptual ERD to a logical ERD. Using the following lines, update your current entities with column names using the Quick Database Diagrams tool.

  ```sql
  Employee
  rel Zipcode
  -
  employee_id
  name
  age
  address
  zip_code

  Zipcode
  -
  zip_code
  city
  state

  Employee_Email
  rel Employee
  -
  email_id
  employee_id
  email

  Owners
  -
  owner_id
  first_name
  last_name

  Estates
  rel Owners
  rel Estate_Type
  rel Zipcode
  -
  estate_id
  owner_id
  estate_type
  address
  zip_code

  Estate_Type
  -
  estate_type_id
  estate_type

  Agents
  -
  agent_id
  first_name
  last_name

  Regions
  -
  region_id
  region_name

  Agent_Region_Junction
  rel Agents
  rel Regions
  -
  agent_id
  region_id
  ```

* The result should appear as follows:

  ![logical-erd-column-names](Images/logical-erd-column-names.png)

* The data model now contains column names but is not yet quite a full-fledged logical data model. This is because we need to continue to add in the foreign key relationships to represent the *types* of entity relationships in the diagram, as well as defining the primary keys for the tables. As of this point, the `rel <entity-name>` syntax only describes abstract relationships between tables.

* Primary and foreign keys can be defined in the online diagram tool by using the `PK` and `FK` syntax after the attribute names of a table.

  ```sql
  Employee
  -
  employee_id PK
  name
  age
  address
  zip_code FK
  ```

* The following syntax should be added to point the foreign key definition to the specific column of another table.

  ```sql
  Employee
  -
  employee_id PK
  name
  age
  address
  zip_code FK - Zipcode.zip_code
  ```

* In the line containing `FK - `, the hyphen signifies a one-to-one relationship between the `Employee` and `Zipcode` tables, where each zip code in the `Employee` table is linked to one zip code in the `Zipcode` table.

* Many types of relationships between entities can be illustrated with various symbols. For example, the `Employee_Email` table has a many-to-one relationship with the `Employee` table via the common employee_id (an employee can have multiple email addresses). Therefore, the symbol describing the relationship is `>-`.

  ![entity-relationships.png](Images/entity-relationships.png)

  ```sql
  Employee_Email
  -
  email_id PK
  employee_id FK >- Employee.employee_id
  email
  ```

* The complete schema for the logical data model should be as follows:

  ```sql
  Employee
  -
  employee_id PK
  name
  age
  address
  zip_code FK - Zipcode.zip_code

  Zipcode
  -
  zip_code PK
  city
  state

  Employee_Email
  -
  email_id PK
  employee_id FK >- Employee.employee_id
  email

  Owners
  -
  owner_id PK
  first_name
  last_name

  Estates
  -
  estate_id PK
  owner_id FK - Owners.owner_id
  estate_type FK - Estate_Type.estate_type_id
  address
  zip_code FK - Zipcode.zip_code

  Estate_Type
  -
  estate_type_id PK
  estate_type

  Agents
  -
  agent_id PK
  first_name
  last_name

  Regions
  -
  region_id PK
  region_name

  Agent_Region_Junction
  -
  agent_id FK >- Agents.agent_id
  region_id FK >- Regions.region_id
  ```

* In addition, with the added datatypes, primary keys, and foreign key relationships, the diagram should now look like the following.

  ![logical-erd.png](Images/logical-ERD.png)

Lastly, transition the logical data model to a physical data model. Using the following lines, update your current entities with data types using the Quick Database Diagrams tool.

```sql
Employee
-
employee_id INT PK
name VARCHAR(255)
age INT
address VARCHAR(255)
zip_code INT FK - Zipcode.zip_code

Zipcode
-
zip_code INT PK
city VARCHAR(255)
state VARCHAR(255)

Employee_Email
-
email_id PK INT
employee_id INT FK >- Employee.employee_id
email VARCHAR(255)

Owners
-
owner_id INT PK
first_name VARCHAR(255)
last_name VARCHAR(255)

Estates
-
estate_id INT PK
owner_id INT FK - Owners.owner_id
estate_type VARCHAR(255) FK - Estate_Type.estate_type_id
address VARCHAR(255)
zip_code INT FK - Zipcode.zip_code

Estate_Type
-
estate_type_id INT PK
estate_type VARCHAR(255)

Agents
-
agent_id INT PK
first_name VARCHAR(255)
last_name VARCHAR(255)

Regions
-
region_id INT PK
region_name VARCHAR(255)

Agent_Region_Junction
-
agent_id INT FK >- Agents.agent_id
region_id INT FK >- Regions.region_id
```

* Point out that the diagram is pretty much the same as the logical data model; however, datatypes are now listed.

  ![physical-erd.png](Images/physical-erd.png)

If students need a refresher on data relationships, direct them to the documentation on the Quick Database Diagrams website following these steps.

* Click the Docs tab at the top of the page.

  ![docs.png](Images/docs.png)

* Select Relationships from the drop-down menu. From this pane, an explanation of relationships and their symbols is provided.

  ![relationships.png](Images/relationships.png)

Slack out [pagila-erd.png](Images/pagila-erd.png) to the class and open it on your computer. Point out how each table has a connection to at least one other table. For example:

* The `customer` and `customer_list` tables both contain `customer id` values.

* The `customer` table and `staff` table both contain `staff id` values.

* Understanding where and how entities are related allows developers to create more cohesive join operations.

Answer any questions before moving on.

### 16. Student Do: Designing an ERD, Part 1 (15 min)

In this activity, students will create a conceptual ERD for mortgage lending.

**Files:**

* [customer.csv](Activities/10-Stu_Designing_ERD/Resources/customer.csv)

* [banks.csv](Activities/10-Stu_Designing_ERD/Resources/banks.csv)

* [sales.csv](Activities/10-Stu_Designing_ERD/Resources/sales.csv)

* [payments.csv](Activities/10-Stu_Designing_ERD/Resources/payments.csv)

* [mortgage.csv](Activities/10-Stu_Designing_ERD/Resources/mortgage.csv)

**Instructions:** [README.md](Activities/10-Stu_Designing_ERD/README.md)

### 17. Instructor Do: Review Designing an ERD, Part 1 (5 min)

**File:** [schema.txt](Activities/10-Stu_Designing_ERD/Solved/schema.txt)

Open the [Quick Database Diagrams (Quick DBD)](https://app.quickdatabasediagrams.com/#/) webpage and demonstrate the solution, using the code in the [`schema.txt`](Activities/10-Stu_Designing_ERD/Solved/schema.txt) file. Live code while explaining the following:

* A logical ERD contains only basic information, such as the names of the tables and their attributes. In addition, a logical ERD can also define primary keys and foreign key relationships among tables; however, unlike a physical data model, the data types of column names have yet to be defined.

* Creating a diagram looks similar to writing code. For example, in the following image, `Customer` followed by the hyphen, creates the table name within the diagram.

  ![customer.png](Images/customer.png)

* When defining the *type* of entity relationship (one-to-one, one-to-many, many-to-many), it's important to think about how the data should interact with each other. For example, there can be multiple sales tied to a single payment record representing multiple mortgage contracts tied to a single bank account (many-to-one). However, a particular sale should only reference a single mortgage (one-to-one).

  ```sql
  Sales
  -
  sales_id PK
  payment_id FK >- Payments.payment_id
  mortgage_id FK - Mortgage.mortgage_id
  loan_amount
  loan_date
  ```

Copy and paste the remaining text from `schema.txt` to create the additional tables. Then export the logical data model as a .png image file. The final product should appear as follows:

  ![stu-logical-ERD.png](Images/stu-logical-ERD.png)

Ask students if they created any other tables or connections, as there are many possible solutions in addition to those included here.

Answer any questions before moving on.

### 18. Student Do: Designing an ERD, Part 2 (10 min)

In this activity, students will transition their mortgage lending logical ERD to a physical ERD.

**Files:**

* [customer.csv](Activities/11-Stu_ERD/Resources/customer.csv)

* [banks.csv](Activities/11-Stu_ERD/Resources/banks.csv)

* [sales.csv](Activities/11-Stu_ERD/Resources/sales.csv)

* [payments.csv](Activities/11-Stu_ERD/Resources/payments.csv)

* [mortgage.csv](Activities/11-Stu_ERD/Resources/mortgage.csv)

**Instructions:** [README.md](Activities/11-Stu_ERD/README.md)

### 19. Instructor Do: Review Designing an ERD, Part 2 (5 min)

**Files:**

* [schema.txt](Activities/11-Stu_ERD/Solved/schema.txt)

* [schema.sql](Activities/11-Stu_ERD/Solved/schema.sql)

Open the [Quick Database Diagrams (Quick DBD)](https://app.quickdatabasediagrams.com/#/) webpage. Copy and paste the solution using the code in the [`schema.txt`](Activities/11-Stu_ERD/Solved/schema.txt) file and explain the following:

* Transitioning a logical ERD to a physical ERD is fairly simple. Assuming the tables, column names, primary keys, and foreign key relationships have already been set, all that is left for transitioning a logical data model to a physical data model is adding the appropriate column data types.

  ![stu-physical-erd](Images/stu-physical-erd.png)

Export the full schema from Quick Database Diagrams as a PostgreSQL file to demonstrate how schema creation code is converted to PostgreSQL code.

* From the Export tab, select PostgreSQL from the drop-down menu. A file named `QuickDBD-export.sql` or something similar will appear in your Downloads folder.

  ![saving-schema.png](Images/saving-schema.png)

  **Note:** The contents of the downloaded file are included in `query.sql` if needed.

* Open the new file with VS Code to view the SQL code. Note how the table and column names are enclosed in quotation marks. These quotation marks will need to be included in queries (for example ,`SELECT * FROM "Members";`) or removed from the code, if preferred.

  ```sql
  CREATE TABLE "Customer" (
    "customer_id" INT   NOT NULL,
    "first_name" VARCHAR(255)   NOT NULL,
    "last_name" VARCHAR(255)   NOT NULL,
    "gender" VARCHAR(255)   NOT NULL,
    "age" INT   NOT NULL,
    "address" VARCHAR(255)   NOT NULL,
    "city" VARCHAR(255)   NOT NULL,
    "state" VARCHAR(255)   NOT NULL,
    "zip_code" INT   NOT NULL,
    CONSTRAINT "pk_Customer" PRIMARY KEY (
        "customer_id"
     )
  );
  ```

* The `CONSTRAINT` line contained in the table creation code is automatically generated upon exporting the diagram and sets the associated primary and foreign keys. The `CONSTRAINT` syntax is just another way to define primary and foreign key relationships.

  ```sql
  CONSTRAINT "pk_Customer" PRIMARY KEY (
        "customer_id"
  ```

* Note that each table has an `ALTER TABLE` statement. This adds a foreign key to each table.

  ```sql
  ALTER TABLE "Sales" ADD CONSTRAINT "fk_Sales_payment_id" FOREIGN KEY("payment_id")
  REFERENCES "Payments" ("payment_id");

  ALTER TABLE "Sales" ADD CONSTRAINT "fk_Sales_mortgage_id" FOREIGN KEY("mortgage_id")
  REFERENCES "Mortgage" ("mortgage_id");

  ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_bank_routing_number" FOREIGN KEY("bank_routing_number")
  REFERENCES "Banks" ("bank_routing_number");

  ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_customer_id" FOREIGN KEY("customer_id")
  REFERENCES "Customer" ("customer_id");
  ```

Return to pgAdmin in the browser and create a new database called `mortgage_db`.

* Open a query tool and paste in the newly downloaded SQL code to create the tables defined in the diagram. Then execute the code.

* The following lines of code will give the error `there is no unique constraint matching given keys for referenced table "Banks"`. This is because the `bank_routing_number` in the `Banks` table is not a unique primary key and therefore cannot be referenced. To resolve the issue, the `bank_routing_number` in the Payments table should be converted to a `bank_id` instead; however, in order to avoid changing the underlying data for simplicity, we can just remove these lines.  

  ```sql
  ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_bank_routing_number" FOREIGN KEY("bank_routing_number")
  REFERENCES "Banks" ("bank_routing_number");
  ```

* Lastly, execute the code and verify that the tables have been created using a `SELECT` statement for each table.

  ```sql
  SELECT * FROM "Customer";
  SELECT * FROM "Banks";
  SELECT * FROM "Sales";
  SELECT * FROM "Payments";
  SELECT * FROM "Mortgage";
  ```

Answer any questions before moving on.

### 20. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
