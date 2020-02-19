# SQL Troubleshooting Guide

This troubleshooting guide contains common issues and fixes pertaining to the use of pgAdmin and postgreSQL.

## Unable to Import/Export CSV via pgAdmin

Issues sometimes arise when using the built-in data import/export tool provided by pgAdmin, either due to slow read/write performance or complete operational failure. Thankfully, in the case of such events there are several alternative methods for importing data to your desired postgreSQL database and corresponding tables.

### Execute .sql file via pgAdmin Query Editor

Throughout the activities, CSV data files have been purposely accompanied by data equivalent .sql files that contain `INSERT` statements to populate a table with specified `VALUE` records. This allows a user to copy and paste the contents of the .sql file and run it through the pgAdmin query editor, effectively performing a manual insert of records to the specified postgreSQL table.

![sql-file-manual-insert](Images/sql-file-manual-insert.png)

### Execute .sql file via postgreSQL CLI

PostgreSQL additionally provides a Command Line Interface (CLI) to not only access and query SQL databases/tables, but also execute .sql files as well. This method has the advantage of being a native operation in which the data import operation is done entirely within the postgreSQL environment, often providing both reliability and speed.

In order to access the postgreSQL CLI, you'll have to first set the `PATH` environment variable to point to the postgreSQL binaries. Therefore run the following command: `export PATH=$PATH:/Library/PostgreSQL/12/bin`.

**Note:** At the time of this writing, PostgreSQL has been updated to version 12, your path may be `/Library/PostgreSQL/11/bin` instead.

![export-psql-path](Images/export-psql-path.png)

Now navigate to the folder containing the .sql file and run the following command: `psql -U postgres -d animals_db -f bird_song.sql`.

* `psql`: The postgreSQL CLI
* `-U` : The username of the postgreSQL account.
* `-d` : The specified database.
* `-f` : The filepath to the .sql file.

![sql-file-CLI](Images/sql-file-CLI.png)

### SQLAlchemy, Psycopg2, and Pandas DataFrames

Data can also be written from a Pandas DataFrame directly to a PostgreSQL table using the in-built `to_sql` function. In order to make the connection to the PostgreSQL database, additional libraries such as `sqlalchemy` and `psycopg2` must be installed; `sqlalchemy` acts as the connection manager while `psycopg2` acts as the PostgreSQL drivers needed to connect specifically to a PostgreSQL DB.

In order to import the `sqlalchemy` and `psycopg2` libraries, they will first need to be installed into the Python environment.

```pip install sqlalchemy` 

```pip install psycopg2-binary```

