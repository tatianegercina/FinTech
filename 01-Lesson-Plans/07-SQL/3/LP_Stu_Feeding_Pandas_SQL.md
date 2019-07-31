### XX. Student Do: Feeding Pandas with SQL (5 mins)

In this activity, students will read data into a Pandas DataFrame from a PostgreSQL database using SQLAlchemy.

**Instructions:**

* [README.md](Activities/Stu_Feeding_Pandas_SQL/README.md)

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/Stu_Stu_Feeding_Pandas_SQL/Unsolved/stu_feeding_pandas_sql.ipynb)

* [schema.sql](Activities/Stu_Stu_Feeding_Pandas_SQL/Unsolved/schema.sql)

---

### XX. Instructor Do: Feeding Pandas with SQL Review (5 mins)

**Files:**

* [stu_feeding_pandas_sql.ipynb](Activities/Stu_Stu_Feeding_Pandas_SQL/Solved/stu_feeding_pandas_sql.ipynb)

* [schema.sql](Activities/Stu_Stu_Feeding_Pandas_SQL/Solved/schema.sql)

Walk through the solution and highlight the following:

* In order to create the connection to the PostgreSQL database, the `create_engine` function is imported from `sqlalchemy`.

  ```python
  from sqlalchemy import create_engine
  ```

* The database URL is defined in the `db_url` variable and it's passed as parameter to the `create_engine` function.

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

* A DataFame called `lastname_df` is created to fetch the last names' counting.

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

Ask for any remaining questions before moving on.
