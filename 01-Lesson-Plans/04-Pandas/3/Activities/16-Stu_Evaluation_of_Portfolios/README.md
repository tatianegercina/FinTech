# Constructing Portfolios

In this activity, upper management has narrowed down their candidate stocks for a portfolio down to 10 stocks: 

* Bank of New York Mellon (BK)
* Diamondback Energy (FANG)
* Johnson & Johnson (JNJ)
* Southwest Airlines Co (LUV)
* Micron Technologies (MU)
* Nike (NKE)
* Starbucks (SBUX)
* AT&T (T)
* Western Digital (WDC)
* Westrock (WRK) 

Harold has been asked to research the candidate stocks and narrow the list down further to create an optimized portfolio. Specifically, upper management wants to create an optimized portfolio with the following characteristics:

* Equal-weighted allocations
* Only uncorrelated stocks
* Only postive return-to-risk ratio stocks (sharpe ratios)

Then, they want to visualize what the returns of a hypothetical `$10,000` investment would be if invested in such a constructed portfolio over time as well as how such a portfolio compares to `$10,000` investments in other lesser-optimized portfolios. 

Use the Pandas library to help Harold construct an optimized portfolio of stocks and plot and compare the returns of a `$10,000` investment in such a portfolio over time.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the `v_data.csv`, `ma_data.csv`, `gs_data.csv`, and `jpm_data.csv` as Pandas DataFrames and set the `date` column as a datetime index for each DataFrame.

  * Combine the DataFrames so that the closing prices from each DataFrame are stacked column-by-column.

  * Use the `sort_index` function to sort the combined DataFrame by datetime index in ascending order (past to present)

  * Rename the columns to reflect the corresponding stock.

  * Use the `pct_change` function to calculate daily returns for each stock.

  * Use the `std` function and multiply by `sqrt(252)` to calculate annualized volatility.

  * Set portfolio weights of `0.6`, `0.2`, `0.1`, and `0.05` from the least risky stock to the most risky stock.

  * Use the `dot` function to multiply the weights by each column of daily returns to calculate the daily returns of the constructed portfolio.

  * Use the `cumprod` function to calculate the cumulative returns of the constructed portfolio.

  * Plot the returns of a hypothetical `$10,000` investment in the constructed portfolio.

## Hints

* To plot the returns of a `$10,000` investment, multiple the initial investment by the portfolio's cumulative returns over time.