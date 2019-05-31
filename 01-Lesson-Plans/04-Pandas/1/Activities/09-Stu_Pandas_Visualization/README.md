# Market Analysis

In this activity, Harold has been asked to analyze the financial data of the companies on the S&P 500. Specifically, Harold has been asked to find and plot the following:

1. A pie chart of the S&P 500 company sector distribution.
2. A bar chart of the top 20 market cap companies.
3. A scatter plot of the price vs. earnings relationship.

Use the Pandas library to help Harold perform the above analysis and generate the above plots.

## Instructions

Using the starter file provided, walk through the following steps.

* Import the necessary libraries and dependencies.

* Read in the `sp500_companies.csv` as a pandas DataFrame.

* Use the `value_counts()` function on the `Sector` column of the DataFrame to count and return a Series object representing the frequency of unique values.

* Plot a pie chart of the S&P 500 company sector distribution.

* Create a subset DataFrame by selecting the `Symbol` and `Market Cap` columns. Use the `nlargest()` function on the subset DataFrame to return the top 20 rows of the `Market Cap` column.

* Plot a bar chart of the top 20 market cap companies.

* Create a subset DataFrame by selecting the `Price` and `Earnings/Share` columns.

* Plot a scatter plot of the price vs. earnings relationship.

## Hints

* Visit the [pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.17.0/index.html) for more information on the `value_counts()` and `nlargest()` functions.
