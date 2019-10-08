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

**File:** [Normalization.md](Activities/01-Ins_Data_Normalization/Solved/Normalization.md)

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

Slack out [Normalization.md](Activities/01-Ins_Data_Normalization/Solved/Normalization.md) as a cheat sheet for students before moving on.

### 3. Student Do: Pet Normalizer (15 min)

In this activity, students will practice their data normalization skills using the provided data.

**File:** [pets.csv](Activities/02-Stu_Data_Normalization/Resources/pets.csv)

**Instructions:** [README.md](Activities/02-Stu_Data_Normalization/README.md)

### 4. Instructor Do: Review Pet Normalizer (5 min)

Open [pets.csv](Activities/02-Stu_Data_Normalization/Resources/pets.csv) and explain the first step of normalization:

* Make sure multiple data points are not included in the same column. For columns containing multiple pets, a new row will need to be created for each pet.

* The final product will look like [pets_cleaned.csv](Activities/02-Stu_Data_Normalization/Resources/pets_cleaned.csv).

Next, open [schema.sql](Activities/02-Stu_Data_Normalization/Solved/schema.sql) in pgAdmin. Walkthrough the code and explain the following:

* Second normal form requires the data to be in first normal form, which was accomplished in the previous step.

* All non-ID columns are dependent on the primary key.

* The `owners` table will include each owner's name once, which is dependent on the primary key for the table.

* Next, a `pet_names` table is created, with each pet given a name and two IDs: one unique `id` for the pet itself and an `owner_id` that will link each pet to its correct owner.

* Each table has values that depend on the primary key and are not repeated in the other table.

* Finally, the two tables can be joined by connecting the `owners` table on `id` and the `pet_names` table on `owner_id`.

Explain the bonus section of the activity:

* A `service` table is created and data is inserted, each with a unique `service_type` and `id`.

* A new `pets_name_new` table is created, this time adding a `service_id` for each animal.

* All three tables can be joined to replicate a view of the cleaned CSV.

### 5. Instructor Do: Intro to Foreign Keys (15 min)

In this activity, students will be introduced to the concept of foreign keys -- columns designated as matching links or relations to another table.

**File:** [schema.sql](Activities/03-Ins_Foreign_Keys/Solved/schema.sql)

Use the slides on foreign keys to explain the concept of foreign keys and how they are used to connect tables:

* A foreign key is a link between tables. The foreign key in the first table points to or is linked to, the primary key in a second table.

* A foreign key also prevents invalid data from being entered into a column. The data being entered MUST be a value from the referenced column.

Slack out [schema.sql](Activities/03-Ins_Foreign_Keys/Solved/schema.sql) for students to follow along. Review the code, explaining the following steps:

* Create a table named `animals_all` and set the primary key to `id`, which will be auto-populated and incremented with each new entry.

  ```sql
  CREATE TABLE animals_all (
    id SERIAL PRIMARY KEY,
    animal_species VARCHAR(30) NOT NULL,
    owner_name VARCHAR(30) NOT NULL
  );
  ```

* Insert data into the `animals_all` table, and then run a `SELECT` query to double-check that data has been inserted.

  ```sql
  INSERT INTO animals_all (animal_species, owner_name)
  VALUES
  ("Dog", "Bob"),
  ("Fish", "Bob"),
  ("Cat", "Kelly"),
  ("Dolphin", "Aquaman");

  SELECT * FROM animals_all;
  ```

* Point out that a new table is created, and its primary key is labeled `id`. The `id` will be unique to this table and has no relation to the previously created table.

  ![animals table](Images/Foreign_Keys1.png)

* A new table named `animals_location` is created. The `FOREIGN KEY (animal_id)` identifies the `animal_id` column as a foreign key.

* After the foreign key has been identified, `REFERENCES animals_all(id)` tells the table that `animal_id` references, or is linked to, the `id` column in the `animals_all` table.

  ```sql
  CREATE TABLE animals_location (
  id INTEGER(11) AUTO_INCREMENT NOT NULL,
  location VARCHAR(30) NOT NULL,
  animal_id INTEGER(10) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (animal_id) REFERENCES animals_all(id)
  );
  ```

* The table is then populated with data and checked with a `SELECT ALL` query.

  ![animals table](Images/Foreign_Keys2.png)

Recap the following:

* The `id` column is the primary key of the `animals_all` table, while `animal_id` is a foreign key in the `animals_location` table.

* Both the `id` column in `animals_all` and the `animal_id` in `animals_location` are designed to contain the same data (the ID), even though the names are different.

* SQL will throw an error if an attempt is made to change an `id` in one table but not the other.

* Foreign key columns need to be named appropriately in order to clarify the data they are referring to.

Students should now understand how to create foreign keys, as well as how to use them to reference data in other tables. Use the following example to illustrate the importance of foreign keys:

* Foreign keys allow tables to be consistent and avoid issues caused by inserting, deleting, or updating one table without making those same changes in the other tables.

* When attempting to insert a row into the new table with an `id` that does not exist in the other table, an error will be returned.

  ```sql
  INSERT INTO animals_location (location, animal_id)
  VALUES ('River', 5);
  ```

* Explain that the `animal_id` column is a foreign key that is assigned to the `id` column in the `animals_all` table. The `id` 5 doesn't exist in the `animals_all` table and therefore can't be referenced in the `animals_location` table.

* Next, a new row is inserted into `animals_all` that will have an `id` of 5. Now a row can be inserted into `animals_location` with an `id` of 5 because it corresponds with an `id` in the `animals_all` table.

  ```sql
  INSERT INTO animals_all (animal_species, owner_name)
  VALUES
    ('Fish', 'Dave');

  INSERT INTO animals_location (location, animal_id)
  VALUES
    ('River', 5);
  ```

* Check that the row was inserted using a `SELECT * FROM animal_location` query.

  ![Foreign keys 3](Images/Foreign_Keys3.png)

Answer any questions students have about foreign keys. Then ask students if they can think of other real-world cases in which the use of foreign keys makes sense. Here are two examples:

* States and countries in addresses: Think back to the `rental` database, where streets, addresses, cities, and countries were stored in different tables. So, for example, if a change occurs to the address of a customer, all information across all tables would need to change. This is called maintaining the **referential integrity**.

* ID number of employees: In a database where the ID number of an employee is used in multiple tables, what happens if the employee's ID number changes? The ID number would need to be changed across all the tables that contain it.

Emphasize that using foreign keys to build relationships across data is a feature of relational databases, hence the name.

### 6. Student Do: Foreign Keys (15 min)

In this activity, students will create tables with foreign keys.

**File**: [schema.sql](Activities/04-Stu_Foreign_Keys/Unsolved/schema.sql)

**Instructions:** [README.md](Activities/04-Stu_Foreign_Keys/README.md)

### 7. Instructor Do: Review Foreign Keys (5 min)

**File**: [schema.sql](Activities/04-Stu_Foreign_Keys/Solved/schema.sql)

Open `schema.sql` in pgAdmin and walk through the code, explaining the following:

* Create a table named `customer`.

  ```sql
  CREATE TABLE customer (
      id SERIAL,
      first_name VARCHAR(30) NOT NULL,
      last_name VARCHAR(30) NOT NULL,
      PRIMARY KEY (id)
  );
  ```

* Data is inserted that takes only `first_name` and `last_name` as values because the `id` will automatically be added.

* Create a table named `customer_email`.

  ```sql
  CREATE TABLE customer_email (
      id SERIAL,
      email VARCHAR(30) NOT NULL,
      customer_id INTEGER NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (customer_id) REFERENCES customer(id)
  );
  ```

* The `customer_id` is a foreign key that references the `id` of the `customer` table. All data inserted must have an `id` that is in the `customer` table.

* The `customer_phone` table is also created and references the same column as its foreign key:

  ```sql
  CREATE TABLE customer_phone (
      id SERIAL,
      phone VARCHAR(30) NOT NULL,
      customer_id INTEGER NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (customer_id) REFERENCES customer(id)
  );
  ```

* Data is inserted into the `customer_phone` table. Like the `customer_email` table, the `customer_id` is a foreign key that references the `id` of the `customer` table.

* To test if we have the correct foreign keys, we can attempt to insert a value with an `id` of 10. This returns an error because that `id` does not exist in the `customer` table.

* Finally, all tables can be joined together by their respective IDs.

### 8. Instructor Do: Intro to Data Relationships (10 min)

In this activity, students will learn the many different types of data modeling relationships that one table can have with another: one-to-one, one-to-many, and many-to-many.

**Files:**

* [schema.sql](Activities/05-Ins_Data_Relationships/Solved/schema.sql)

* [query.sql](Activities/05-Ins_Data_Relationships/Solved/query.sql)

Use the `Data Relationships` slides to explain that we will now cover one-to-one, one-to-many, and many-to-many relationships between data, which is an essential part of data modeling.

Begin by discussing one-to-one relationships. This example will use members of the Simpson family to illustrate the concept.

* In a one-to-one relationship, each name is associated with one and only one Social Security number. In other words, each item in a column is linked to only one item from another column.

  ![Images/one-to-one.png](Images/one-to-one.png)

Next, discuss one-to-many relationships. We'll continue with our Simpsons example, but add Sherlock Holmes and his sidekick Watson to the database.

  ![Images/one-to-many1.png](Images/one-to-many1.png)

* This example has two tables. The first table lists only addresses. The second table lists each person's Social Security number and address.

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

* First, open [schema.sql](Activities/05-Ins_Data_Relationships/Solved/schema.sql) and paste in the queries to create and insert into the `children` and `parents` tables. There are two separate tables:

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
  SELECT children.child_name, child_parent_junction.child_id,
  parents.parent_name, child_parent_junction.parent_id
  FROM children
  LEFT JOIN child_parent_junction
  ON child_parent.child_id = children.child_id
  LEFT JOIN parents
  ON child_parent_junction.parent_id = parents.parent_id;
  ```

* The `children` table has a left join with the junction table, the results of which then have a left join with the `parents` table.

Take a moment to summarize the major points of the activity:

* Data can be modeled as one-to-one, one-to-many, and many-to-many relationships.

* Many-to-many relationships require a junction table.

* Junction tables use foreign keys to reference the keys in the original tables.

Ask if there are any questions before moving on.

### 9. Student Do: Data Relationships (10 min)

In this activity, students will create table schemata for students and available courses, and then create a junction table to display all courses taken by students.

**Instructions:** [README.md](Activities/06-Stu_Data_Relationships/README.md)

### 10. Instructor Do: Review Data Relationships (5 min)

**Files:**

* [schema.sql](Activities/06-Stu_Data_Relationships/Solved/schema.sql)

* [query.sql](Activities/06-Stu_Data_Relationships/Solved/query.sql)

Explain that this activity required creating separate tables for students and courses, and then creating a junction table to reflect the many-to-many relationship between the two tables.

Paste in the schemata for the `students` and `courses` tables and explain the following:

* Each table is given the ID as the primary key.

* Fields are added for required attributes for the table.

* Populate the tables with the `INSERT` queries, and then display the tables.

  ![Images/modeling05.png](Images/modeling05.png)

  ![Images/modeling06.png](Images/modeling06.png)

Next, do the same for the junction table, named `student_courses_junction`, and explain the code.

  ```sql
  -- Create a junction table.
  CREATE TABLE student_courses_junction (
    student_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    course_id INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    course_term VARCHAR NOT NULL,
    PRIMARY KEY (student_id, course_id)
  );
  ```

* The table takes both a `student_id` and a `course_id`, which are references to the previously created tables.

* Since `student_id` and `course_id` reference those tables, they become the foreign key.

* New student or course data cannot be inserted into the `student_courses_junction` table that does not currently exist in the `students` or `courses` tables.

* This table bridges the two previous tables and shows all courses taken by each student.

* The primary key will be a composite of both IDs.

* Additionally, this table includes a new field, `course_term`, which is the term in which a course was taken by a student.

Query the table to display the result.

  ![Images/modeling07.png](Images/modeling07.png)

To reinforce the many-to-many relationship, point out that many students can take many courses.

For the bonus, briefly explain that two outer joins can be performed to retrieve complete data on each student.

  ```sql
  SELECT s.id, s.last_name, s.first_name, c.id, c.course_name, j.course_term
  FROM students s
  LEFT JOIN student_courses_junction j
  ON s.id = j.student_id
  LEFT JOIN courses c
  ON c.id = j.course_id;
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

* We can connect to the database by calling the `create_engine` function and passing the database URL. In this example, we use the `animals` database that was created earlier, along with the default database username and password.

  ```python
  engine = create_engine("postgresql://postgres:postgres@localhost:5432/animals")
  ```

* The structure of the database URL is defined as follows:

  ![SQLAlchemy URL structure](Images/sqlalchemy_url.png)

* To retrieve data from the database, we first need to define a SQL query that fetches the data we want.. In this example, all the rows from the `animals_all` table are retrieved.

  ```python
  query = "SELECT * FROM animals_all"
  ```

* The DataFrame is created by using the [`read_sql()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) in Pandas. This function reads a SQL query or database table into a DataFrame. Two parameters are passed: the `query` and the `engine` instance that were defined earlier.

  ```python
  animals_df = pd.read_sql(query, engine)
  ```

Explain to students that once the data from the database is in a DataFrame, we can perform any data processing, analysis, or visualization task.

* The `head()` from the `animals_df` DataFrame is shown. You can see that the data from the `animals_all` table is now loaded into the DataFrame.

  ![Sample DataFrame records](Images/animals_df_head.png)

* A new query is defined to count the number of animals per owner.

  ```python
  query = """
  SELECT owner_name, COUNT(owner_name) AS animals
  FROM animals_all
  GROUP BY owner_name
  """
  ```

* The `animals_count_df` DataFrame is created to read the query, and a bar chart is created using `hvplot` to present the results.

  ```python
  animals_count_df = pd.read_sql(query, engine)
  ```

  ![Sample bar chart](Images/sample_bar_char_sqlalchemy.png)

Answer any questions before moving on.

### 13. Student Do: Feeding Pandas with SQL (5 min)

In this activity, students will read data into a Pandas DataFrame from a PostgreSQL database using SQLAlchemy.

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/08-Stu_Feeding_Pandas_SQL/Unsolved/stu_feeding_pandas_sql.ipynb)

* [schema.sql](Activities/08-Stu_Feeding_Pandas_SQL/Unsolved/schema.sql)

**Instructions:**

* [README.md](Activities/08-Stu_Feeding_Pandas_SQL/README.md)

### 14. Instructor Do: Feeding Pandas with SQL Review (5 min)

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/08-Stu_Feeding_Pandas_SQL/Solved/stu_feeding_pandas_sql.ipynb)

* [schema.sql](Activities/08-Stu_Feeding_Pandas_SQL/Solved/schema.sql)

Walkthrough the solution and highlight the following:

* In order to create the connection to the PostgreSQL database, the `create_engine` function is imported from `sqlalchemy`.

  ```python
  from sqlalchemy import create_engine
  ```

* The database URL is defined in the `db_url` variable, and then it's passed as a parameter to the `create_engine` function.

  ```python
  # Define the databaser URL
  db_url = "postgresql://postgres:postgres@localhost:5432/university"

  # Create the engine object
  engine = create_engine(db_url)
  ```

* The `students_df` DataFrame is created by reading a SQL query that fetches all the records from the `students` table.

  ```python
  # Write the SQL query
  query = "SELECT * FROM students"

  # Read the SQL query into a DataFrame
  students_df = pd.read_sql(query, engine)
  ```

* A DataFame called `lastname_df` is created to fetch the count of the last names.

  ```python
  # Write the SQL query
  query = """
  SELECT last_name, count(last_name)
  FROM students
  GROUP BY last_name
  """

  # Read the SQL query into a DataFrame
  lastname_df = pd.read_sql(query, engine)
  ```

* The bar chart is created using `hvplot` and the `lastname_df` DataFrame.

  ![Brothers counting bar chart](Images/brothers_counting_chart.png)

Answer any questions before moving on.

### 15. Instructor Do: Entity Relationship Diagrams (10 min)

In this activity, students will learn how to interpret and create an Entity Relationship Diagram (ERD) -- an asset that delineates the relationship among tables in a database.

**File:** [pagila-erd.png](Images/pagila-erd.png)

Use the ERD slides and begin the discussion of entity relationship diagrams (ERDs). Explain the following points:

* An **entity relationship diagram**, or **ERD**, is a visual representation of entity relationships within a database.

* There are three types of ERDs: conceptual, logical, and physical. These will be covered more in-depth as we advance through today's lesson.

* An ERD defines entities, their attributes, and data types, as well as illustrates the overall design of a database.

To break down these concepts further, discuss the following example.

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

With the design tool open in your browser, demonstrate how to create a simple conceptual ERD using the following text:

  ```sql
  Gym
  -
  Gym_Name
  Address
  City
  Zipcode

  Trainers
  -
  First_Name
  Last_Name

  Members
  -
  First_Name
  Last_Name
  Address
  City

  Payments
  -
  CreditCard_Info
  Billing_Zip
  ```

* The result should appear as follows:

  ![conceptual-erd.png](Images/conceptual-ERD.png)

  **Note**: The tables' locations can be physically adjusted by clicking and dragging them in the browser.

* Explain to the class that creating a conceptual model is the first step of designing an ERD.

* When a conceptual model is created, the overall goals of creating a database are taken into account by defining entities and their relationships to each other.

Transition from the conceptual ERD to a logical ERD. Using the following lines, update your current entities with data types using the Quick Database Diagrams tool.

  ```sql
  Gym
  -
  ID INTEGER PK
  Gym_Name VARCHAR
  Address VARCHAR
  City VARCHAR
  Zipcode VARCHAR

  Trainers
  -
  ID INTEGER PK
  First_Name VARCHAR
  Last_Name VARCHAR

  Members
  -
  ID INTEGER PK
  First_Name VARCHAR
  Last_Name VARCHAR
  Address VARCHAR
  City VARCHAR

  Payments
  -
  ID INTEGER PK
  CreditCard_Info INTEGER
  Billing_Zip INTEGER
  ```

* By defining the column types, this model has become more complex and is now considered a **logical model**.

* Note that in addition to adding the data types for each column, an `ID` column has been included and designated as a primary key with the `PK` acronym.

    ![logical-erd.png](Images/logical-ERD.png)

* IDs are added because when designing a **physical model**, the physical relationships between entities are constructed and linked. This is often done with the use of primary keys.

Using the Quick Database Diagrams tool, include the physical relationships in the entities by updating them as follows:

  ```sql
  payment
  -
  id INT PK
  customer_id INT FK - customer.id
  amount DEC
  payment_date DATE

  customer
  -
  id INT PK
  payment_id INT FK - payment.id
  first_name VARCHAR
  last_name VARCHAR
  ```

* In the lines containing `FK - `, the hyphen signifies a one-to-one relationship between the tables, where each payment is linked to one customer using foreign keys.

* Many types of relationships between entities can be illustrated with symbols, such as:

  ![entity-relationships.png](Images/entity-relationships.png)

* Point out that the diagram now has arrows connecting the entities, and that the connecting entities' text is now bold.

  ![physical-erd.png](Images/physical-erd.png)

* Two additional lines have been added: `customer_id` to the payment table and `payment_id` to the customer table. This was done to create unique relationships between the entities.

* In the `payment` table, the section `FK - customer.id` signifies the physical connection between the `customer` table and its `id` column to the `payment` table and the `customer_id` column.

* The added `FK` and `PK` abbreviations signify foreign key (FK) and primary key (PK). Note the key icon added to the specified entities in the diagram.

* Note that this is the method used with the Quick Database Diagrams tool. Other ERD design tools may employ different techniques.

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

In this activity, students will create a conceptual ERD for a gym owner.

**File:** [schema.txt](Activities/10-Stu_Designing_ERD/Unsolved/schema.txt)

**Instructions:** [README.md](Activities/10-Stu_Designing_ERD/README.md)

### 17. Instructor Do: Review Designing an ERD, Part 1 (5 min)

**File:** [schema.txt](Activities/10-Stu_Designing_ERD/Solved/schema.txt)

Open the [Quick Database Diagrams (Quick DBD)](https://app.quickdatabasediagrams.com/#/) webpage and demonstrate the solution, using the code in the [`schema.txt`](Activities/10-Stu_Designing_ERD/Solved/schema.txt) file. Live code while explaining the following:

* A conceptual diagram has only basic information, such as the names of the tables and their attributes.

* Creating a diagram looks similar to writing code. For example, in the following image, `Gym` followed by the hyphen, creates the table name within the diagram.

  ![gym.png](Images/gym.png)

* Transitioning a conceptual diagram to a logical diagram requires more information. Data types are defined, and primary keys are established by adding ID rows to the tables, such as in the `Trainers` table:

  ![trainers.png](Images/trainers.png)

  **Note**: Remember that the `PK` acronym stands for primary key.

Copy and paste the remaining text from `schema.txt` to create the additional tables. The final product should appear as follows:

  ![logical-ERD.png](Images/logical-ERD.png)

Ask students if they created any other tables or connections, as there are many possible solutions in addition to those included here.

Answer any questions before moving on.

### 18. Student Do: Designing an ERD, Part 2 (10 min)

In this activity, students will further improve the ERD by creating a physical ERD.

**File:** [schema.txt](Activities/11-Stu_ERD/Unsolved/schema.txt)

**Instructions:** [README.md](Activities/11-Stu_ERD/README.md)

### 19. Instructor Do: Review Designing an ERD, Part 2 (5 min)

**Files:**

* [schema.txt](Activities/11-Stu_ERD/Solved/schema.txt)

* [query.sql](Activities/11-Stu_ERD/Solved/query.sql)

Open the [Quick Database Diagrams (Quick DBD)](https://app.quickdatabasediagrams.com/#/) webpage. Copy and paste the solution using the code in the [`schema.txt`](Activities/11-Stu_ERD/Solved/schema.txt) file and explain the following:

* Transitioning a logical ERD to a physical ERD involves adding appropriate entities to tables and mapping their relationships.

* For example, in the `Members` table, several rows were added to demonstrate data relationships. A row named `Gym_ID` was added as a foreign key (`FK`), establishing a one-to-many relationship by using the `>-` symbol.

* A row containing the `Trainer_ID` was also added to demonstrate the one-to-many relationship between the members and trainers. While one member will have no more than one trainer, one trainer may instruct many members.

  ```sql
  Gym_ID INTEGER FK >- Gym.Gym_ID
  Trainer_ID INTEGER FK >- Trainers.Trainer_ID
  ```

* The `Trainers` table also has a one-to-many relationship (`>-`) created by adding a `Gym_ID` row to the table. While a trainer will be employed at a single gym, the gym will employ many trainers.

  ```sql
  Gym_ID INTEGER FK >- Gym.Gym_ID
  ```

* In the `Payments` table, a one-to-one relationship (`-`) is demonstrated by adding a `Member_ID` row and linking it to the `Members` table.

  ```sql
  Member_ID INTEGER FK - Members.Member_ID
  ```

Export the full schema from Quick Database Diagrams as a PostgreSQL file to demonstrate how schema creation code is converted to PostgreSQL code.

* From the Export tab, select PostgreSQL from the drop-down menu. A file named `QuickDBD-export.sql` will appear in your Downloads folder.

  ![saving-schema.png](Images/saving-schema.png)

  **Note:** The contents of the downloaded file is included in `query.sql`, if needed.

* Open the new file with VS Code to view the SQL code. Note how the table and column names are enclosed in quotation marks. These quotation marks will need to be included in queries (for example ,`SELECT * FROM "Members";`) or removed from the code, if preferred.

* Note that each table has an `ALTER TABLE` statement. This adds a foreign key to each table.

* The `CONSTRAINT` line contained in the table creation code is automatically generated upon exporting the diagram and does not need to be altered.

Return to pgAdmin in the browser and create a new database called `gym`.

* Open a query tool and paste in the newly downloaded SQL code to create the tables defined in the diagram.

* Execute the code, and then check the table creation using a `SELECT` statement for each table.

  ```sql
  SELECT * FROM "Trainers";
  SELECT * FROM "Members";
  SELECT * FROM "Gym";
  SELECT * FROM "Payments";
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
