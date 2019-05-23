# Unit 10 Assignment - Looking for Suspicious Transactions

![Credit card fraudster](Images/credit_card_fraudster.jpg)

*[Credit Card Fraudster by Richard Patterson](https://www.flickr.com/photos/136770128@N07/42252105582/) | [Creative Commons Licensed](https://creativecommons.org/licenses/by/2.0/)*

## Background

Harold has become so popular on the firm due to all the contributions of starting using python on his team, so that the Cybercrime Unit reached Harold to ask him for help to identify potential fraudulent transactions.

Craeg, the Cybercrime Unit Director, shown to Harold all the available data, and Harold realized that you can use your brand new SQL skills to address this challenge.

You have to create a series of SQL queries that analyzes historical credit card transactions to identify possible fraudulent transactions according to the consumption patterns of credit card holders.

In this homework assignment, you will be accomplishing three main tasks:

1. [Define a database model to store the credit card transactions data and create a new PostgreSQL database using your model.](#Data-Modeling)
2. [Create a database schema on PostgreSQL and populate your  database from the CSV files provided.](#Data-Engineering)
3. [Analyze the data to identify possible fraudulent transactions.](#Data-Analysis)

---

## Files

* [card_holder.csv](Data/card_holder.csv)
* [credit_card.csv](Data/credit_card.csv)
* [merchant.csv](Data/merchant.csv)
* [merchant_category.csv](Data/merchant_category.csv)
* [transaction.csv](Data/transaction.csv)

## Instructions

### Data Modeling

In this section you have to create an Entity Relationship Diagram (ERD) by inspecting the given CSV files. Part of the challenge on this activity is to figure out how many tables you should create, as well as what kind of relationships you believe you have to define among the tables. Feel free to comment with your classmates your database model design ideas. You can use a tool like [Quick Database Diagrams](https://www.quickdatabasediagrams.com) to create your model.

### Data Engineering

Using your database model as blueprint, in this activity you should create a database schema for each of your tables and relationships. Remember to specify data types, primary keys, foreign keys, and any other constraints you defined.

After creating the database schema, import the data from the corresponding CSV files.

### Data Analysis

Once you have your brand new database perform it's time to identify fraudulent transactions; on this part of the homework assignment you are asked to create a technical report (you can use a Jupyter notebook, a markdown file or a word processor) to present your results answering the following questions:

Use SQL to find an answer for the following questions and tasks:

* How can you isolate (or group) the transactions of each card holder?
* Normally one takes breakfast between 7am and 9am, What are to top 100 higher transactions between this time period? do you see some fraudulent or anomalous transactions? what is your rationale for considering that there are fraudulent transactions?
* Some fraudsters hack a credit card by making several small payments (let's say less than $2.00) that are normally ignored by cardholders, count the transactions that are less than $2.00 per card holder, is there some evidence to state that some credit card has been hacked? Explain you rationale.
* What are the top 5 merchants that are more prone to be hacked using small transactions?
* Once you have a query that can be reused, a good practice is to create a view for analyst. Create a view for each of the previous queries.

There are several ways to connect your python scripts with a database. `sqlalchemy` is one of the most popular packages to interact with databases from python. Install `sqlalchemy` by typing `pip install sqlalchemy` on your terminal (or Git Bash) and use the following code to create a connection to your PostgreSQL database and load data directly to a Pandas DataFrame.

```python
# initial imports
from sqlalchemy import create_engine
import pandas as pd

# create a connection to the database
engine = create_engine('postgresql://user:password@localhost:5432/your_db_name')

# load select query result into a DataFrame
data = pd.read_sql('SELECT * FROM helloworld', engine)
```

Once you have the data from PostgreSQL on a DataFrame you can visually analyze your data. Continue your analysis creating the following plots.

* Create a line plot showing a time series from the transactions on may 8th, 2018 from card holder `id` 1980 and 2015. What difference do you observe between the consumption patters? Does the difference could be a fraudulent transaction? Explain your rationale.

* Create a line plot showing four lines representing the daily transactions (from Sunday to Saturday) for card holder `id` 1978 on each week of march 2018. By observing the consumption patters, do you see any anomalies? Write your own conclusions about your insights.

### Challenge

Another approach to identify fraudulent transactions is looking for _outliers_ on the data. _Standard deviation_ or _quartiles_ are often used to detect _outliers_.

Read the following articles on outliers detection and code a function to identify weekly or daily anomalies for any card holder.

* [How to Calculate Outliers](https://www.wikihow.com/Calculate-Outliers)
* [Removing Outliers Using Standard Deviation in Python](https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html)
* [How to Use Statistics to Identify Outliers in Data](https://machinelearningmastery.com/how-to-use-statistics-to-identify-outliers-in-data/)

### Submission

* Create an image file of your ERD.

* Create a .sql file of your table schemata.

* Create a .sql file of your queries.

* Create and upload a repository with the above files to GitHub and post a link on BootCamp Spot.

### Hint

* For comparing time and dates take a look to the [date/time functions and operators](https://www.postgresql.org/docs/8.0/functions-datetime.html) at the PostgreSQL documentation.
