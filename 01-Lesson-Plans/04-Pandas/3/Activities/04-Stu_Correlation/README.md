# Diversification

In this activity, Harold's company is looking to build a diversified stock portfolio. So far, they've added `JNJ` (Johnson & Johnson) and `HD` (Home Depot) which both reside with the the Healthcare and Consumer Discretionary sectors, respectively. However, now they want to add a third technology sector stock to the mix, in particular, a semiconductor stock. 

As a result, Harold has been asked by his manager to research a set of 5 semiconductor stocks to add to the currently existing portfolio. In order to properly create a diversified portfolio which tends to minimize long-term volatility/risk, stocks within the portfolio should be as uncorrelated as possible so as to create a counter-balance effect (when some stocks fall in price, others may rise in price). 

Therefore, use the Pandas library to help Harold analyze the 5 semiconductor stocks and choose the stock with the least correlation to `JNJ` and `HD`.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the `amd_stock_data.csv` as a pandas DataFrame.

  * Display summary statistics of the input data, just to get a feel for your data.

  * Drop the `volume`, `open`, `high`, and `low` columns.

  * Set the `date` column as the DataFrame index.

  * Drop the extra 'date' column, as the index can now replaces it.

  * Calculate daily returns.

  * Use `loc()` to select subsets from the datetime index to create date ranges of 1, 3, 5, and 10 years. Remember that you can select date ranges using label indexing `loc[start_date:end_date]`

  * Output summary statistics for each 1, 3, 5, and 10 year subset.

  * Plot daily return charts for each 1, 3, 5, and 10 year subset. 

  * Formulate insights regarding the variation in average daily returns for each time period. 

## Hints

* Analyze average daily returns from a numerical standpoint. Which time period has the highest average daily return and which has the lowest? What would that mean?