## 7.1 Lesson Plan: Introduction to SQL

### Overview

In today's class, students are introduced to SQL databases and will learn how to create databases, tables, and simple data queries.

### Class Objectives

By the end of class, students will be able to:

* Install and run PostgreSQL (SQL) and pgAdmin (GUI) on their computers.

* Create a database and tables using pgAdmin.

* Define SQL data types, primary keys, and unique values.

* Load CSV files into a database and query the data.

* Articulate and apply the four basic functions of persistent storage: Create, Read, Update, and Delete (CRUD).

* Combine data from multiple tables using joins.

### Instructor Notes

* **Important:** [Instructions](../Supplemental/InstallationGuides) for installing PostgreSQL and pgAdmin should have already been slacked-out prior to today's class, as students needed to install these before class to conserve time for lessons and activities rather than for initial setup.

* If you experience any issues importing data as CSV files via pgAdmin, please refer to the SQL troubleshooting [guide](../Supplemental/SQL_troubleshooting_guide.md).

* Today's class will be challenging. In this lesson, a series of activities will introduce students to programming with SQL using PostgreSQL and pgAdmin. The pace of today's class will be quick as students absorb learning a new UI and programming language simultaneously.

* Because this lesson introduces more than one new concept, circulate through the class during student activities to assist those who appear frustrated or stuck. Some students may already have experience with SQL; embrace these students' knowledge of the language, and have them assist students who are not yet familiar with SQL.

* This lesson introduces new content rapidly. Students may express frustration at learning a new interface and programming language simultaneously. Explain to students that while the learning curve may be steep at first, SQL experience is highly sought-after and well worth the effort required to become comfortable with it.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [7.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c6264b7e-e1bb-41d4-be84-aac3016512d0) Note that this video may not reflect the most recent lesson plan.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1xv6ebYYBpDpQAlB4EOxWeRcdOdZPDSp5oe8d27baU-w/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to class and congratulate them on making it this far in the course! At this point, students are only one unit away from their first project, and so they should feel proud of what they have accomplished so far!

Open the slideshow and overview the learning outcomes, class objectives, and a brief background of the SQL unit:

* Today's lesson will introduce students to the most popular database management language: SQL.

* SQL allows us to connect to a database and store, manipulate, and analyze the (often large amounts of) data within.

* As companies continue to store data and leverage the insights derived from data analysis, SQL programmers continue to be in high demand. Therefore, SQL is also an economically valuable skill.

---

### 2. Instructor Do: Introduction to SQL (5 min)

In this activity, instructors introduce students to PostgreSQL and pgAdmin, a database management language and GUI, respectively.

Open the slideshow to the Postgres section and take some time to go over the purpose of PostgreSQL and pgAdmin:

* SQL (often pronounced "sequel") stands for Structured Query Language. It is a powerful programming language designed to allow programmers to create, populate, manipulate, and access databases, as well as provide the ability to leverage scalable server-side storage for large volumes of data.

* With SQL, data is stored in tables on the server; much like spreadsheets, you would create in Microsoft Excel. This makes the data easy to visualize and search.

* PostgreSQL (usually referred to as "Postgres") is an object-relational database system that uses the SQL language. PostgreSQL is one of the many *vendors* that utilize the underlying SQL technology -- similar to other well-known vendors such as MySQL, Microsoft SQL Server, and Oracle SQL.

* pgAdmin is the database management tool used for working with Postgres. It simplifies the creation, maintenance, and use of database objects by providing a Graphical User Interface (GUI).

Slack out the following resources:

* [Student Guide](../StudentGuide.md) containing this week's objectives as well as resource links.

* [SQL Reference Guide](../Supplemental/SQL_reference_guide.pdf) for students to use as a reference during the activities this week.

* [SQL Installation Guides](../Supplemental/InstallationGuides) outlining how to install PostgreSQL and pgAdmin for either Mac or Windows (if not done already).

### 3. Instructor Do: Create a Database (5 min)

In this activity, the instructor walks students through the process of creating a database in PostgreSQL.

Begin by verifying that everyone has successfully installed pgAdmin and PostgreSQL. Everyone should have completed this step prior to today's class.

* Open pgAdmin in a new browser window and ensure that everyone is able to follow along and view their new server in the browser.

  ![browser-view.png](Images/browser-view.png)

Walk the class through the steps to create a database using pgAdmin.

* In the pgAdmin editor, right-click the newly established server to create a new database.

* From the menu, select Create, and then select Database to create a new database.

  ![create_database.png](Images/create_database.png)

* Enter "example_db" as the database name. Make sure the owner is set as the default Postgres, and then click Save.

  ![example_db.png](Images/example_db.png)

At this point, show students that there is a new database listed in the left-hand menu. Explain that the new database, `example_db`, is not yet connected to the server. Simply clicking on the database will create a connection to Postgres.

![new_db.png](Images/new_db.png)

Answer any questions before moving on.

### 4. Instructor Do: Create a Table (10 min)

In this activity, the instructor walks students through the process of creating a table and manipulating its contents in PostgreSQL.

Now that there is a database on the server, it's time to dig into the real meat of SQL and start creating tables within the new database!

From the left-hand menu in pgAdmin, right-click "example_db" and select Query Tool.

**Note:** You can also select Query Tool from the Tools drop-down menu at the top of the screen. (See the second screenshot below.)

![query_tool.png](Images/query_tool.png)

![tools_dropdown.png](Images/tool_dropdown.png)

Explain to students that this is how to access the code editor.

Type the following lines of code, explaining each line:

 ```sql
 CREATE TABLE customer (
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30),
    gender VARCHAR(30),
    age INT,
    address VARCHAR(50),
    city VARCHAR(50),
    state CHAR(2),
    zip_code CHAR(5)
 );
 ```

* `CREATE TABLE customer (<COLUMNS>);` creates a table called `customer` with the columns listed within the parentheses.

* `first_name VARCHAR(30) NOT NULL` creates a `first_name` column that represents the first name of a customer. The column values can hold character strings of up to 30 characters and does not allow NULL values; The `NOT NULL` constraint requires the `first_name` column to have a value specified.

* `last_name VARCHAR(30)` creates a `last_name` column that represents the last name of a customer. The column values can hold character strings of up to 30 characters, and unlike the `first_name` column, allows NULL values.

* `gender VARCHAR(30)` creates a `gender` column that represents the gender of the customer. The column values can hold character strings of up to 30 characters.

* `age INT` creates an `age` column that represents the age of a customer. The column values must be integers.

* `address VARCHAR(50)` creates an `address` column that represents the street address of a customer. The column values can which can hold character strings of up to 50 characters.

* `city VARCHAR(50)` creates a `city` column that represents the city in which the customer lives. The column values can hold character strings of up to 50 characters.

* `state VARCHAR(10)` creates a `state` column that represents the state ticker in which the customer lives. The column values must be character strings of 2 characters.

* `zip_code CHAR(5)` creates `zip_code` column which represents the postal zip code of the customer. The column values must be character strings of 5 characters.

 **Note:** Be sure to point out the semicolon at the end of the statement, which tells pgAdmin that this line of code has concluded.

After reviewing the code, click the play icon to run the script. Make a note of the Messages tab at the bottom of the screen.

 ![play_icon.png](Images/play_icon.png)

Demonstrate that the structure of a table can be visualized by appending the script with `SELECT * FROM <table name>;`. Point out the "table already exists" error message that now appears at the bottom of the page.

* SQL data is persistent; it is not deleted or overwritten when identical commands are run unless specifically commanded.

* This means that when a database or table is created with a name identical to one that already exists, an error will occur, telling the user that the database or table already exists.

Ask the class how to avoid this kind of error. Students may respond that they can simply delete the offending line of code and then run the commands again. Explain that while this method would work, deleting the working code is not the best practice.

Show the class an alternative method:

* Highlight the lines of code to run, and then click the lightning bolt icon to run only the highlighted selection. This method of running SQL code is preferable to deleting the previous code.

  ![Select.png](Images/Select.png)

* The structure of a table can be visualized using `SELECT * FROM <table name>;`.

* Using the asterisk in this manner tells pgAdmin to select all fields from the table.

* In the future, students will be able to view the structure of their table, and all of the values contained within it, using this same line of code.

Type the following code while explaining what it does line by line.

```sql
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'MT', 07829),
('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AZ', 89721),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673);

SELECT *
FROM customer;
```

* This code operates as it reads: it inserts data into the `customer` table and then specifies the columns in which data will be entered.

* The `VALUES` line places the data contained in the parentheses into the corresponding columns listed after the `INSERT INTO` statement.

* Single quotations must be used for insert strings; otherwise, an error will result.

Use the following code to query the table, extracting only the `first_name`.

 ```sql
 SELECT first_name
 FROM customer;
 ```

Explain that specifying a column name in the `SELECT` statement will return only the data contained in that field.

Filter the queried data to display only male customers younger than 34.

 ```sql
 SELECT first_name, last_name
 FROM customer
 WHERE gender = 'Male'
 AND age < 34;
 ```

Explain the following points:

* The `SELECT` clause can specify more than one column.

* Data is filtered by using additional clauses such as `WHERE` and `AND`.

* The `WHERE` clause will extract only the data that meets the condition specified. `AND` adds a second condition to the original clause, further refining the query.

Answer any questions before moving on.

### 5. Student Do: Creating Tables (15 min)

In this activity, students will use pgAdmin to recreate and query a table from an image provided.

**Instructions:** [README.md](Activities/03-Stu_Creating_Tables/README.md)

### 6. Instructor Do: Review Creating Tables (5 min)

**Files:**

* [schema.sql](Activities/03-Stu_Creating_Tables/Solved/schema.sql)

* [seed.sql](Activities/03-Stu_Creating_Tables/Solved/seed.sql)

* [query.sql](Activities/03-Stu_Creating_Tables/Solved/query.sql)

Create a new database named `state_info` in pgAdmin. Then use the the schema.sql and seed.sql files to create and populate the `states` table. Use the query.sql file to walk through the correct queries.

* To create a new table, specify the data type for each column.

  ```sql
  CREATE TABLE states (
    state_name VARCHAR(50),
    state_abbreviation CHAR(2),
    population INT,
    state_property_tax_rate FLOAT
  );
  ```

* Insert multiple rows of data into the new table.

* Each column is specified in the `INSERT INTO` clause, and the values are inserted in the same order.

* To make the code easier to read, each row of values is on its line, separated by a comma.

  ```sql
  INSERT INTO states
  (state_name, state_abbreviation, population, state_property_tax_rate)
  VALUES
  ('Florida', 'FL', 21477737, 0.0093),
  ('Alabama', 'AL', 4903185, 0.0042),
  ('Texas', 'TX', 28995881, 0.0181),
  ('Kentucky', 'KY', 4467673, 0.0086),
  ('Virginia', 'VA', 8535519, 0.0081),
  ('Louisiana', 'LA', 4648794, 0.0053),
  ('Utah', 'UT', 3205958, 0.0064),
  ('Vermont', 'VT', 623989, 0.0188);
  ```

* Create a query to view the data using the `SELECT` clause.

  ```sql
  SELECT *
  FROM states;
  ```

* Note the syntax here. Even though the code can fit on a single line, it's good practice to split it up over two lines instead. This way, the code is easier to read when more advanced queries are created.

Using the `SELECT` clause again, query the data to return only the state names in the table.

  ```sql
  SELECT state_name
  FROM states;
  ```

* The first bonus question is very similar to the previous query executed in that it displays only the values of a single column.

  ```sql
  SELECT state_abbreviation
  FROM states;
  ```

* The second bonus question incorporates a `WHERE` clause, which further filters the data.

* The `WHERE` clause is used to search for specific data within a database. In this case, we are extracting only the records that meet the specified condition.

* In the line `WHERE population > 5000000;` we are filtering for records that have a value that is greater than 5000000 in the population column.

  ```sql
  SELECT *
  FROM states
  WHERE population > 5000000;
  ```

* Note that the `WHERE` clause is highly customizable, and can use several operators like `<` (less than), `>` (greater than), and `=` (equals to).

Walk through the solution to the third and final bonus question.

* Queries can be filtered even further with the `AND` clause. This clause allows users to specify more than one condition in their query.

  ```sql
  SELECT *
  FROM states
  WHERE population > 5000000
  AND state_property_tax_rate < 0.01;
  ```

Answer any questions before moving on.

### 7. Instructor Do: The Value of Unique Values (5 min)

In this activity, students are introduced to the concept of duplicate and unique values and how to properly remove duplicate records through the use of unique identifiers.

**Files:**

* [schema.sql](Activities/04-Ins_Values_of_Uniques/Solved/schema.sql)

* [seed.sql](Activities/04-Ins_Values_of_Uniques/Solved/seed.sql)

* [query.sql](Activities/04-Ins_Values_of_Uniques/Solved/query.sql)

Using the `customer` table from the `example_db` database, insert the duplicate data below into the table, and then visualize the table with the new information.

 ```sql
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709);

 SELECT *
 FROM customer;
 ```

Explain that duplicate data is a real-world occurrence (and an eyesore). Demonstrate how to remove the rows containing the string `Michael` in the `first_name` column.

 ```sql
DELETE FROM customer
WHERE first_name = 'Michael';
 ```

* The duplicate was deleted, but so was the original row. That's a little annoying. Make sure the class understands why this happened.

* Because the name Michael appears twice in the table, SQL assumes that the user wants to delete every column containing that name; it doesn't understand that the user is simply trying to remove the duplicate row.

* To prevent this kind of thing from occurring, programmers will often want to create a column that automatically populates each new row with unique data. This allows them to select and modify that row more easily.

Remove the `customer` table by running the following line of code:

 ```sql
 -- Delete the table "customer"
 DROP TABLE customer;
 ```

Copy the following code from `schema.sql`, `seed.sql`, and `query.sql` file and paste it in the pgAdmin editor.

 ```sql
 -- Re-create the table "customer" within example_db
CREATE TABLE customer (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30),
  gender VARCHAR(30),
  age INT,
  address VARCHAR(50),
  city VARCHAR(50),
  state CHAR(2),
  zip_code CHAR(5)
);

 -- Insert data into the table
INSERT INTO customer
(first_name, last_name, gender, age, address, city, state, zip_code)
VALUES
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709),
('Cindy', 'Stephens', 'Female', 23, '838 Brown Street', 'East Christina', 'MT', 07829),
('John', 'Jackson', 'Male', 34, '5319 Candice Motorway', 'Adkinstown', 'AZ', 89721),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673),
('Alexander', 'Martinez', 'Male', 32, 'USNS Mosley', 'FPO', 'AA', 24673),
('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709);

 -- Query all fields from the table
 SELECT *
 FROM customer;
 ```

Explain the following points:

* A **primary key** uniquely identifies a row.

* `SERIAL` generates a new value for each inserted record in the table.

* By default, the starting value is 1, and it will increase by 1 for each new record. When using `SERIAL` with our unique `PRIMARY KEY`, we automatically get unique, incrementing values for each table row.

* Because values will automatically increment, each row's ID is guaranteed to be unique. This ensures that SQL does not identify and update the wrong row when CRUD (Create, Read, Update, Delete) statements are implemented (will cover in the following activities).

* The `INSERT` statements have not changed, as they do not need to insert data specifically into the `customer_id` column. SQL automatically provides value for this column, fulfilling the uniqueness constraint by automatically incrementing the last value used as a customer ID.

* The data type for the `customer_id` column is automatically assigned as an integer.

* One entry in the table is incorrect: one of the Michaels has the wrong `first_name` and `age`. We need to update the `first_name` from Michael to Brian and the `age` from 24 to 20.

* To avoid issues with updating multiple rows, it's best to update by the customer ID. First, query by name to find the ID for the row we want to update.

  ```sql
  SELECT customer_id, first_name, last_name, age
  FROM customer
  WHERE first_name = 'Michael';
  ```

* This will return all rows that contain the name Michael, including the `customer_id`, `first_name`, `last_name`, and `age` columns.

* Next, we can select and update the `first_name` from Michael to Brian and the `age` from 24 to 20 based on the row's unique ID.

  ```sql
  UPDATE customer
  SET first_name = 'Brian', age = 20
  WHERE customer_id = 6;
  ```

* Note that similar to a query, the `WHERE` statement is used to pinpoint the data we want to change. In this case, the `customer_id` column is used to select the unique row we want to affect.

* Duplicate data is also easier to remove with the use of a unique ID. With the following code, remove the duplicate data:

  ```sql
  DELETE FROM customer
  WHERE customer_id = 5;
  ```

* This does precisely what was desired: duplicate data is deleted, and original data is preserved.

Answer any remaining questions before moving on.

### 8. Student Do: Making and Using an ID (10 min)

In this activity, students will recreate a table and then query, insert, and update data.

**Instructions:** [README.md](Activities/05-Stu_Making_IDs/README.md)

### 9. Instructor Do: Review Making and Using an ID (10 min)

**Files:**

* [schema.sql](Activities/05-Stu_Making_IDs/Solved/schema.sql)

* [seed.sql](Activities/05-Stu_Making_IDs/Solved/seed.sql)

* [query.sql](Activities/05-Stu_Making_IDs/Solved/query.sql)

Open [query.sql](Activities/05-Stu_Making_IDs/Solved/query.sql) and copy the code into pgAdmin.

Go over the lines of code used to create the ID and set it as the primary key. Make sure the class understands how this works, and explain how useful this will be in this week's homework.

Review how to create a new column using the `ALTER TABLE` and `ADD COLUMN` statements. Explain that adding the column name and data type is completed in the same manner as creating a new table.

Answer any questions before moving on.

---

### 10. BREAK (15 min)

---

### 11. Instructor Do: Import Data (10 min)

In this activity, students learn how to import data (CSV) into an existing table in a database using the Import/Export tool in pgAdmin.

**Note:** For students having issues using the pgAdmin Import/Export tool, there is an included [seed.sql](Activities/06-Ins_Importing_Data/Solved/query.sql) file for each activity in the remaining half of the day. Have students refer to the SQL troubleshooting [guide](../Supplemental/SQL_troubleshooting_guide.md) for more information on how to use the file.

**Files:**

* [mortgage.csv](Activities/06-Ins_Importing_Data/Resources/mortgage.csv)

* [schema.sql](Activities/06-Ins_Importing_Data/Solved/query.sql)

* [seed.sql (optional)](Activities/06-Ins_Importing_Data/Solved/seed.sql)

* [query.sql](Activities/06-Ins_Importing_Data/Solved/query.sql)

So far, the class has created its tables and values manually using SQL code. As one might imagine, this process can be tedious when translating large datasets from external sources. Thankfully, pgAdmin includes a built-in import tool that can take CSV files and easily import their data into tables.

Return to pgAdmin and create a new database called `mortgage_db`.

Open the CSV file within an integrated development environment, such as Excel, to show the dataset that will be imported. Be sure to point out that the first row of this dataset includes headers.

* Open a query tool within `mortgage_db` and create a table named `mortgage`. Point out that the columns created match the data in the CSV file.

* Once the table has been created, right-click Miscellaneous_DB from the left-hand menu and select Refresh.

* Scroll down to Schemas and expand that menu, and then expand the Tables menu.

  ![table-expand.png](Images/table-expand.png)

* Right-click the new table and select Import/Export from the menu.

  ![import-export.png](Images/import-export.png)

In the Options tab, complete the following steps:

* Slide the Import/Export tab to Import.

* Click on the dot menu to navigate to the `mortgage.csv` file on your computer.

* Slide the Header tab to Yes.

* Select the comma from the drop-down menu to set it as the Delimiter.

* Leave the other fields as they are, and then click OK.

  ![import.png](Images/import.png)

In the query tool, rerun `SELECT * FROM mortgage` to verify that data has been imported.

Let the class know that the larger a dataset is, the longer it will take for pgAdmin to import values.

### 12. Student Do: Hide and Seek (10 min)

In this activity, students will create a new table and import data from a CSV file.

**Files:**

* [customer.csv](Activities/07-Stu_Hide_and_Seek/Resources/customer.csv)

**Instructions:** [README.md](Activities/07-Stu_Hide_and_Seek/README.md)

### 13. Instructor Do: Review Hide and Seek (5 min)

**Files:**

* [schema.sql](Activities/07-Stu_Hide_and_Seek/Solved/schema.sql)

* [seed.sql](Activities/07-Stu_Hide_and_Seek/Solved/seed.sql)

* [query.sql](Activities/07-Stu_Hide_and_Seek/Solved/query.sql)

Open pgAdmin and paste the code from [query.sql](Activities/07-Stu_Hide_and_Seek/Solved/query.sql) into the editor. Explain the following:

* Although the CSV data does not contain an `id` column, when we specify `SERIAL PRIMARY KEY` while creating the table, IDs will automatically be assigned to each row.

* To view a range of data, we can use a combination of `WHERE` and `AND` statements.

* To collect data that exists in either one column or another, the `OR` statement is included in the query.

Walkthrough the solutions to the bonus questions, touching on the following points:

* After importing the second table, we can specify a source with the `WHERE` statement.

* `AND` statements can be used more than once for more specific results.

Answer any questions before moving on.

### 14. Instructor Do: CRUD (5 min)

In this activity, students are introduced to the concept of Create, Read, Update, and Delete statements in SQL.

Return to the `CRUD` section of the slides and begin to explain CRUD operations.

* **CRUD**, while an unusual acronym, is a set of tools that are persistently used throughout programming.

* CRUD stands for Create, Read, Update, and Delete.

Engage the class in a discussion by asking them to provide examples of CRUD operations.

In today's class, each of the operations has been in use. Students have:

* Created data in a table with the `INSERT` statement.

  ```sql
  INSERT INTO customer
  (first_name, last_name, gender, age, address, city, state, zip_code)
  VALUES
  ('Michael', 'Meyer', 'Male', 24, '1021 Eddie Knolls Apt. 087', 'South Geraldton', 'RI', 43709);
  ```

* Read data with the use of `SELECT`.

  ```sql
  SELECT *
  FROM customer;
  ```

* Updated a table's data using `UPDATE`.

  ```sql
  UPDATE customer
  SET first_name = 'Brian', age = 20
  WHERE customer_id = 6;
  ```

* Deleted data using `DELETE`.

  ```sql
  DELETE FROM customer
  WHERE customer_id = 5;
  ```

Introduce the class to an additional method of reading the data: wildcards.

* A **wildcard** is a character—either a percentage sign or an underscore—that takes the place of one or more characters in a query.

* The keyword `LIKE` indicates the use of a wildcard in a query.

* The percentage sign (%) signifies that zero, one, or multiple characters will be substituted in a query. For example, in the query `WHERE last_name LIKE 'Will%';` all names in the database beginning with "Will" will be returned, no matter the length.

* When using the underscore as a wildcard, only a single character is replaced in the query.

* In the line `WHERE first_name LIKE '_AN';`, only three-lettered names ending with "an" will be returned.

Answer any questions before moving on.

### 15. Student Do: Using CRUD (20 min)

In this activity, students will utilize CRUD operations (Create, Read, Update, Delete) on the provided data.

**Files:**

* [sales.csv](Activities/08-Stu_CRUD/Resources/sales.csv)

**Instructions:** [README.md](Activities/08-Stu_CRUD/README.md)

Let the class know that they will be using the `WHERE` clause in this activity.

This activity will require students to do some research. Links are provided to help them search for solutions to problems they are likely to encounter.

### 16. Instructor Do: Review Using CRUD (5 min)

**Files:**

* [schema.sql](Activities/08-Stu_CRUD/Resources/schema.sql)

* [seed.sql](Activities/08-Stu_CRUD/Resources/seed.sql)

* [query.sql](Activities/08-Stu_CRUD/Solved/query.sql)

Open a query tool in `sales_db` and copy and paste the code from schema.sql to create a new table named `sales`. Go over the following:

* Refresh the table list, and then import the data from `sales.csv` into the new table.

* First, alter the table to add an `id`.

* Deletions and updates are made where the conditions are met.

* Multiple averages can be selected at once.

* Values can be inserted into the table even though not every value is filled out.

* Finally, select all values to show the newly added country.

### 17. Instructor Do: Joins (15 min)

In this activity, students are introduced to the concept of joins -- the combination of multiple related datasets into a single dataset.

**Files:**

* [sales.csv](Activities/09-Ins_Joins/Resources/sales.csv)

* [mortgage.csv](Activities/09-Ins_Joins/Resources/mortgage.csv)

* [schema.sql](Activities/09-Ins_Joins/Solved/schema.sql)

* [seed.sql (optional)](Activities/09-Ins_Joins/Solved/seed.sql)

* [query.sql](Activities/09-Ins_Joins/Solved/query.sql)

Students may recall working with merges and joins to combine datasets during the Pandas unit. While SQL is a vastly different language than Python, it also includes the functionality to merge tables.

Create two new tables in `mortgage_db` in pgAdmin named `sales` and `mortgage`.

* Copy the code from [query.sql](Activities/09-Ins_Joins/Solved/query.sql) to create the tables, and then import the corresponding data from `sales.csv` and `mortgage.csv`.

* Remember to refresh the database; newly created tables will not immediately appear.

* Point out that both tables have matching values within the `mortgage_id` column of the `sales` table and the `mortgage_id` of the `mortgage` table. Because there are common values, it is possible to join these tables together.

* From the [query.sql](Activities/09-Ins_Joins/Solved/query.sql) file, copy and paste the code performing an `inner join` on the two tables:

  ```sql
  SELECT sales.sales_id,
         sales.payment_id,
         sales.mortgage_id,
         sales.loan_amount,
         sales.loan_date,
         mortgage.mortgage_id,
         mortgage.mortgage_name,
         mortgage.mortgage_rate
  FROM sales
  INNER JOIN mortgage ON sales.mortgage_id = mortgage.mortgage_id;
  ```

**Note:** Some students may have advanced knowledge of SQL queries and use aliases in their solutions. Using aliases is not necessary for today's activities; they will be covered more comprehensively in the next class.

  ```sql
  -- Advanced INNER JOIN solution
  SELECT a.sales_id,
         a.payment_id,
         a.mortgage_id,
         a.loan_amount,
         a.loan_date,
         b.mortgage_id,
         b.mortgage_name,
         b.mortgage_rate
  FROM sales as a
  INNER JOIN mortgage as b ON a.mortgage_id = b.mortgage_id;
  ```

Point out one significant difference between SQL joins and Python joins:

* In SQL joins, the columns that should be viewed after the join must be declared in the initial `SELECT` statement.

  ![join-columns.png](Images/join-columns.png)

* There are five primary types of joins that can be used with PostgreSQL:

  * `INNER JOIN` returns records that have matching values in both tables.

    ![inner-join](Images/inner-join.png)

  * `LEFT JOIN` returns all records from the left table and the matched records from the right table.

    ![left-join](Images/left-join.png)

  * `RIGHT JOIN` returns all records from the right table and the matched records from the left table.

    ![right-join](Images/right-join.png)

  * `CROSS JOIN` returns records that match every row of the left table with every row of the right table. This type of join has the potential to make very large tables.

    ![cross-join](Images/cross-join.png)

  * `FULL OUTER JOIN` places null values within the columns that do not match between the two tables after an inner join is performed.

    ![full-outer-join](Images/full-outer-join.png)

Slack out the link to this explanation of Postgres [joins](https://www.tutorialspoint.com/postgresql/postgresql_using_joins.htm) for students to study.

Demonstrate a couple of different joins that can be performed. Then answer any questions before moving on to the next activity.

### 18. Student Do: Joining the Big Banks (20 min)

In this activity, students will be using joins to query payment information and associated bank information via a common bank routing number.

**Files:**

* [banks.csv](Activities/10-Stu_Joins/Resources/banks.csv)

* [payments.csv](Activities/10-Stu_Joins/Resources/payments.csv)

**Instructions:** [README.md](Activities/10-Stu_Joins/README.md)

### 19. Instructor Do: Review Joining the Big Banks (5 min)

**Files:**

* [schema.sql](Activities/10-Stu_Joins/Solved/schema.sql)

* [seed.sql](Activities/10-Stu_Joins/Solved/seed.sql)

* [query.sql](Activities/10-Stu_Joins/Solved/query.sql)

Using the schema.sql file and the query tool, create two new tables named `players` and `seasons_stats` using the data in `Players.csv` and `Seasons_Stats.csv`.

Open query.sql and copy the code. Then open a new query tool and paste the solution into the editor. Review the solution, explaining the following:

* Since the selected data comes from two different tables, the naming convention is `table_name.column_name`.

* Next, determine which table to select from and which table to `INNER JOIN` with. Remember, the inner join only selects data that has matching values in both tables.

* Finally, determine the key both tables will join on. For example, to join the two tables by using the `id` and an `INNER JOIN`, select the data columns to be viewed from both tables, and then specify which columns the tables will be connected by.

  ```sql
  select *
  from sales
  INNER JOIN payments ON sales.payment_id = payments.payment_id
  ```

Answer any questions before ending the class.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
