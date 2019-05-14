# Returns Over Date Ranges

In this activity, Harold's manager wants Harold to analyze the last 10 years of historical price data for AMD and plot the daily returns over the last 1, 3, 5, and 10 year time periods. In addition, Harold's manager wants to see the differences in average daily returns for each time period to perhaps understand whether a short or long term perspective should be used in prospecting AMD as a potential candidate.

Help Harold analyze the last 10 years of AMD stock data.  

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
