### XX. Instructor Do: Connecting Pandas with PostgreSQL (10 mins)

In this activity, students will learn how they can create a connection to PostgreSQL from Python using [SQLAlchemy](https://www.sqlalchemy.org/) to load data into a Pandas DataFrame.

**Files:**

* [connecting_pandas_sql.ipynb](Activities/Ins_Connecting_Pandas_SQL/Solved/connecting_pandas_sql.ipynb)

* [schema.sql](Activities/Ins_Connecting_Pandas_SQL/Solved/schema.sql)

Comment to students that it's possible to interact between PostgreSQL and Python using the SQLAlchemy library. Ask students to install this library on their virtual environment by executing the following command form the terminal:

```bash
conda install -c anaconda sqlalchemy
```

Be sure that all students have installed SQLAlchemy, open the unsolved Jupyter notebook and live code the solution by highlighting the following:

* SQLAlchemy offers several functionalities to interact with databases from Python.

* This activity is focused on retrieving data from a PostgreSQL database to create a DataFrame for data analysis and visualization in Python.

* To create a connection to a database the [`create_engine` function](https://docs.sqlalchemy.org/en/13/core/engines.html) is imported from `sqlalchemy`.

  ```python
  from sqlalchemy import create_engine
  ```

* Creating a connection to the database is as simple as calling the `create_engine` function passing the database URL. In this example, the `animals` database created before is used, the default database user name and password are used.

  ```python
  engine = create_engine("postgresql://postgres:postgres@localhost:5432/animals")
  ```

* The structure of the database URL is defined as follows:

  ![SQLAlchemy URL structure](Images/sqlalchemy_url.png)

* To retrieve data from the database the first step is to define a SQL query that fetches the data we want. In this example, all the rows from the `animals_all` table are retrieved.

  ```python
  query = "SELECT * FROM animals_all"
  ```

* The DataFrame is created using the [`read_sql()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) from Pandas, this function reads a SQL query or database table into a DataFrame. Two parameters are passed, the `query` and the `engine` instance defined before.

  ```python
  animals_df = pd.read_sql(query, engine)
  ```

Explain to students that once that the data from the database is on a DataFrame, they can perform any data processing, analysis or visualization task.

* The `head()` from the `animals_df` DataFrame is shown, it can be seen that the data from the `animals_all` table is now loaded into the DataFrame.

  ![Sample DataFrame records](Images/animals_df_head.png)

* A new query is defined to count the number of animals per owner.

  ```python
  query = """
  SELECT owner_name, COUNT(owner_name) AS animals
  FROM animals_all
  GROUP BY owner_name
  """
  ```

* The `animals_count_df` DataFrame is created to read the query and a bar chart is created using `hvplot` to present the results.

  ```python
  animals_count_df = pd.read_sql(query, engine)
  ```

  ![Sample bar chart](Images/sample_bar_char_sqlalchemy.png)

Answer any additional question from students before moving forward.
