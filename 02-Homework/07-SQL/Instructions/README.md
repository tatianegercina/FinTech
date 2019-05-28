# Unit 10 Assignment - Looking for Suspicious Transactions

![Credit card fraudster](Images/credit_card_fraudster.jpg)

*[Credit Card Fraudster by Richard Patterson](https://www.flickr.com/photos/136770128@N07/42252105582/) | [Creative Commons Licensed](https://creativecommons.org/licenses/by/2.0/)*

## Background

Fraud is prevalent these days whether you are a small tacos shop or a large, international business. While there are emerging technologies that employ machine learning and artificial intelligence to detect fraud, many instances of fraud detection still require strong data analytics to find the abnormal charges within the normal.

In this assignment, you will apply your new SQL skills to analyze historical credit card transactions to identify possible fraudulent transactions according to the consumption patterns of credit card holders.

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

Now you are asked to create a report about fraudulent transactions of some top customers of the firm. To achieve this task you should perform a visual data analysis of fraudulent transactions using `pandas`, `Plot.ly`, `cufflinks` and `sqlalchemy` by creating the following plots:

* Your first mission is to verify if there are some fraudulent transactions on the history of two of the most important customers of the firm, for privacy reasons you only know that their card holders IDs are `18` ans `2`. Create a line plot showing a time series from the transactions along all the year for each card holder. In order to contrast the patters of both card holders, create a line plot containing both lines. What difference do you observe between the consumption patterns? Does the difference could be a fraudulent transaction? Explain your rationale.

* The CEO of the biggest customer of the firm suspects that someone has used her corporate credit card without authorization along the first semester of 2018 to pay quite high consumptions on restaurants; now you are asked to find any anomalous transaction along that period. Create a series of six box plots using `cufflinks`, one for each month, in order to identify how many outliers could be per month for card holder id `25`. By observing the consumption patters, do you see any anomalies? Write your own conclusions about your insights.

### Challenge

Another approach to identify fraudulent transactions is looking for _outliers_ on the data. _Standard deviation_ or _quartiles_ are often used to detect _outliers_.

Read the following articles on outliers detection and code a function using python to identify anomalies for any card holder.

* [How to Calculate Outliers](https://www.wikihow.com/Calculate-Outliers)
* [Removing Outliers Using Standard Deviation in Python](https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html)
* [How to Use Statistics to Identify Outliers in Data](https://machinelearningmastery.com/how-to-use-statistics-to-identify-outliers-in-data/)

### Submission

* Create an image file of your ERD.

* Create a .sql file of your table schemata.

* Create a .sql file of your queries.

* Create a Jupyter notebook for the visual data analysis and other the challenge.

* Create and upload a repository with the above files to GitHub and post a link on BootCamp Spot.

### Hint

* For comparing time and dates take a look to the [date/time functions and operators](https://www.postgresql.org/docs/8.0/functions-datetime.html) at the PostgreSQL documentation.
