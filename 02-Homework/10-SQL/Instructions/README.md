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

* TBD

## Instructions

### Data Modeling

In this section you have to create an Entity Relationship Diagram (ERD) by inspecting the given CSV files. Part of the challenge on this activity is to figure out how many tables you should create, as well as what kind of relationships you believe you have to define among the tables. Feel free to comment with your classmates your database model design ideas. You can use a tool like [Quick Database Diagrams](https://www.quickdatabasediagrams.com) to create your model.

### Data Engineering

Using your database model as blueprint, in this activity you should create a database schema for each of your tables and relationships. Remember to specify data types, primary keys, foreign keys, and any other constraints you defined.

After creating the database schema, import the data from the corresponding CSV files.

### Data Analysis

Once you have your brand new database perform the following data analysis tasks:


    - Find anomalous transactions amounts
        - Higher amounts
        - Very tiny amounts
        - Shopping patterns by time
    - Group by possible fraudulent accounts / customers
    - Create views for reporting fraudulent transactions
    - Data Visualization
        - Step 1: How Pandas read SQL directly to a DataFrame
        - Step 2: Plot data
