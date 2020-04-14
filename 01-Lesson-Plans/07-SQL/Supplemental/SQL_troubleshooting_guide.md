# SQL Troubleshooting Guide

This troubleshooting guide contains common issues and fixes pertaining to the use of pgAdmin and postgreSQL.

## Unable to Import/Export CSV via pgAdmin

In the event of an error when using pgAdmin's data import tool, the database tables can be created and populated using the provided .sql files. The following details two methods for manually creating and populating the tables.

### Execute .sql file via pgAdmin Query Editor

Each activity will contain schema.sql files that can be used to create the database tables. The table can then be populated using pgAdmin's data import tool and the CSV files provided. If the data import tool fails, a seed.sql file is also provided that will manually insert the data into the tables. Please run the seed.sql file after the schema.sql file to ensure that the table is properly configured before data is inserted.

![sql-file-manual-insert](Images/sql-file-manual-insert.png)

### Execute .sql file via postgreSQL CLI

PostgreSQL additionally provides a Command Line Interface (CLI) to access and query SQL databases/tables, and execute .sql files. This method has the advantage of being a native operation in which the data import operation is done entirely within the postgreSQL environment, providing reliability and speed.

In order to access the postgreSQL CLI, you'll have to first set the `PATH` environment variable to point to the postgreSQL binaries. Windows users will have to use the Command Prompt, as Git Bash has issues with the psql CLI. When ready, run one of the following commands, depending on your operating system:

* Mac OS: `export PATH=$PATH:/Library/PostgreSQL/12/bin`.
* Windows: `SET PATH=%PATH%;C:\Program Files\PostgreSQL\12\bin`

**Note:** At the time of this writing, PostgreSQL has been updated to version 12. Therefore, if your PostgreSQL version is still on 11, then your paths may be the following:

* Mac OS: `/Library/PostgreSQL/11/bin`
* Windows: `C:\Program Files\PostgreSQL\11\bin`

Make sure to check that the PATH changes have gone into effect; use the respective `ECHO` syntax for your operating system to query the contents of the environmental `PATH` variable. You may have to restart your terminal for changes to go into effect.

![export-psql-path](Images/export-psql-path.png)

![export-psql-path-windows](Images/export-psql-path-windows.PNG)

Now navigate to the folder containing the .sql file and run the following command:

`psql -U <username> -d <database> -f <sql-file>`.

In this case, the command should be the following:

`psql -U postgres -d mortgage_db -f seed.sql`.

* `psql`: The postgreSQL CLI
* `-U` : The username of the postgreSQL account.
* `-d` : The specified database.
* `-f` : The filepath to the .sql file.

![sql-file-CLI](Images/sql-file-CLI.png)

![psql-insert-windows](Images/psql-insert-windows.PNG)

### SQLAlchemy, Psycopg2, and Pandas DataFrames

Data can also be written from a Pandas DataFrame directly to a PostgreSQL table using the in-built `to_sql` function. In order to make the connection to the PostgreSQL database, additional libraries such as `sqlalchemy` and `psycopg2` must be installed; `sqlalchemy` acts as the connection manager, while `psycopg2` acts as the PostgreSQL drivers needed to connect specifically to a PostgreSQL DB.

In order to import the `sqlalchemy` and `psycopg2` libraries, they will first need to be installed into the Anaconda environment.

* `conda install -c anaconda psycopg2`

![sqlalchemy-psycopg2-import](Images/sqlalchemy-psycopg2-import.png)

In addition, the data residing within the CSV will need to be imported into a Pandas DataFrame. Therefore, the `read_csv` function should be used.

![dataframe-read-csv](Images/dataframe-read-csv.png)

Next, the connection to the PostgreSQL database will need to be established. In order to make the connection, a database URI or connection string should be provided.

Database connection strings often consist of the following parameters:

* `<connector>://<username>:<password>@<server>:<port>/<database>`

The database connection string in this case was the following:

* `postgresql://postgres:postgres@localhost:5432/mortgage_db`

Then, instantiate a connection to the database by using the newly created database connection string with the `create_engine` function.

![create-engine](Images/create-engine.png)

Finally, now that the connection to the PostgreSQL database has been established, the `to_sql` function can be used to write DataFrame contents to the specified PostgreSQL table. The `to_sql` function uses the following parameters:

* `name`: Name of the SQL table
* `con`: The SQLAlchemy engine loaded with DB drivers
* `if_exists`: How to behave if the table already exists.
  
  * fail: Raise a ValueError.
  * replace: Drop the table before inserting new values.
  * append: Insert new values to the existing table.
  
* `index`: Writes the DataFrame index as a column.
* `dtype`: Specifies the datatype for columns in dictionary format.

![sqlalchemy-pandas-write](Images/sqlalchemy-pandas-write.png)

Lastly, in order to check if the data was properly inserted, the in-built Pandas `read_sql_query` DataFrame function can be used to query a database and read the results as a Pandas DataFrame.

![sqlalchemy-pandas-read](Images/sqlalchemy-pandas-read.png)

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
