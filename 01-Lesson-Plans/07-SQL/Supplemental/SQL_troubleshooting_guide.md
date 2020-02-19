# SQL Troubleshooting Guide

This troubleshooting guide contains common issues and fixes pertaining to the use of pgAdmin and postgreSQL.

## Unable to Import/Export CSV via pgAdmin

Issues sometimes arise when using the built-in data import/export tool provided by pgAdmin, either due to slow read/write performance or complete operational failure. Thankfully, in the case of such events there are several alternative methods for importing data to your desired postgreSQL database and corresponding tables.

### Execute .sql file via pgAdmin Query Editor

Throughout the activities, CSV data files have been purposely accompanied by data equivalent .sql files that contain `INSERT` statements to populate a table with specified `VALUE` records. This allows a user to copy and paste the contents of the .sql file and run it through the pgAdmin query editor, effectively performing a manual insert of records to the specified postgreSQL table.

![sql-file-manual-insert](Images/sql-file-manual-insert.png)

### Execute .sql file via postgreSQL CLI

PostgreSQL additionally provides a Command Line Interface (CLI) to not only access and query SQL databases/tables, but also execute .sql files as well. This method has the advantage of being a native operation in which the data import operation is done entirely within the postgreSQL environment, often providing both reliability and speed.

* In order to access the postgreSQL CLI, you'll have to first set the `PATH` environment variable to point to the postgreSQL binaries. The postgreSQL binaries were located at the following path `/Library/PostgreSQL/12/bin`.

  ![export-psql-path](Images/export-psql-path.png)

* Now run the SQL file

![sql-file-CLI](Images/sql-file-CLI.png)

### Sqlalchemy & Pandas DataFrames
