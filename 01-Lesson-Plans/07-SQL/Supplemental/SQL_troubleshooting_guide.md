# SQL Troubleshooting Guide

This troubleshooting guide contains common issues and fixes pertaining to the use of pgAdmin and postgreSQL.

Current list of issues is as follows:

* Unable to Import/Export CSV via pgAdmin

## Unable to Import/Export CSV via pgAdmin

Issues sometimes arise when using the built-in data import/export tool provided by pgAdmin, either due to slow read/write performance or complete operational failure. Thankfully, in the case of such events there are several alternative methods for importing data to your desired postgreSQL database and corresponding tables.

### Execute .sql file via pgAdmin

Throughout the activities, CSV data files have been purposely accompanied by data equivalent .sql files that contain `INSERT` statements to populate a table with specified `VALUE` records. This allows a user to copy and paste the contents of the .sql file and run it through the pgAdmin query editor, effectively performing a manual insert of records to the postgreSQL table.

![sql-file-manual-insert](Images/sql-file-manual-insert.png)

### Execute .sql file via postgreSQL CLI

### Sqlalchemy & Pandas DataFrames
