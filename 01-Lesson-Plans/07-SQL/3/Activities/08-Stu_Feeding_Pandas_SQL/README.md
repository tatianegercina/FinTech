# Feeding Pandas with SQL

In this activity you will read data into a Pandas DataFrame from the `university` database you created before.

## Instructions

As database consultant, you are asked to create a report to identify how many brothers are among the students on the university, so you decided to combine your Python and SQL skills.

Using the `university` database that you created before, perform the following tasks:

* Create a connection to the `university` database on your local PostgreSQL instance.

* Create a Pandas DataFrame by reading all the records from the `students` table.

* Create a bar chart using `hvplot` that shows the number of students with the same last name, those are the potential brothers o the university.

Your bar chart should look like this.

![Sample brothers bart chart](Images/brothers_bar_chart.png)
