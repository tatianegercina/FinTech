# Reading Stock Data from a CSV File

Now that you see how easy it is to work with spreadsheet data in Pandas, let's practice on some real financial data! In this activity, you will create a DataFrame from a CSV file and then explore its contents using the DataFrame's built-in functions. 

## Instructions

Using the [starter file](Unsolved/reading_stock_data.ipynb), complete the following steps.

1. Import the Pandas library by typing `import pandas as pd` on the command line. 

2. Create a DataFrame by reading in the CSV file containing the last 10 years of historical price data for AMD.

3. Perform an initial data exploration by getting the top rows of the DataFrame.

4. Oh no! There are no columns names on the DataFrame. Fix this problem by recreating the DataFrame and setting the columns names to Date, Close, Volume, Open, High, Low.

5. When the columns names are fixed, get the first 10 rows from the DataFrame.

## Challenge

Google how to get _n_ bottom rows from a DataFrame and get the bottom 10 rows.

## Hint

Consult the Pandas [`head()` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html).

- - - 

© 2019 Trilogy Education Services
