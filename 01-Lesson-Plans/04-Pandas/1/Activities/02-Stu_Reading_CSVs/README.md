# Reading Stock Data from a CSV File

Now that you've seen how easy it is to work with spreadsheet data in Pandas vs. Excel, let's try it out on some real financial data! In this activity, you will create a DataFrame from a CSV file and explore its contents using the DataFrame's built-in functions.

## Instructions

Using the starter file provided, complete the following steps.

1. Import the Pandas library using its most common acronym: _pd_

2. Create a DataFrame by reading the provided CSV file that contains the last 10 years of historical price data for AMD.

3. Perform an initial data exploration by getting the top rows of the DataFrame.

4. Oh no! There are no columns names on the DataFrame, fix the problem by recreating the DataFrame and setting the columns names as: date, close, volume, open, high, low.

5. Once the columns names are fixed get the first then rows from the DataFrame.

## Challenge

* Google how you can get the _n_ bottom rows from a DataFrame and get the bottom 10 rows.

## Hint

* You may take a look to the Pandas [`head()` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html).
