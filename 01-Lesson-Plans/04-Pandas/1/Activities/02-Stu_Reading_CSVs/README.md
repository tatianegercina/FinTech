# Reading Stock Data from a CSV File

Now that you've seen how easy it is to work with spreadsheet data in Pandas vs. Excel, let's try it out on some real financial data! In this activity, you will create a DataFrame from a CSV file and explore its contents using the DataFrame's build-in functions.

## Instructions

Using the starter file provided, walk through the following steps.

* Import the Pandas library using its most common acronym: _pd_
* Create a dataframe by reading the provided CSV file that contains the last 10 years of historical price data for AMD.
* Perform an initial data exploration by getting the top rows of the dataframe.
* Oh no! There are no columns names on the dataframe, fix the problem by recreating the dataframe and setting the columns names as: date, close, volume, open, high, low.
* Once the columns names are fixed get the first then rows from the dataframe.

## Challenge

* Google how you can get the _n_ bottom rows from a dataframe and get the bottom 10 rows.

## Hint

* You may take a look to the Pandas [`head()` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html).
