# Portfolio Planner Part II

In this activity, Harold has been asked to revisit the 10 stocks he previously researched: 

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

Specifically, upper management wants to go beyond just evaluating stocks by volatility/risk, they now want to create a more optimized portfolio with the following characteristics:

* Equal-weighted allocations
* Only non-correlated stocks
* Only postive return-to-risk ratio stocks (sharpe ratios)

Then, they want to visualize what the returns of a hypothetical `$10,000` investment would be if invested in such a constructed portfolio over time as well as how such a portfolio compares to `$10,000` investments in other lesser-optimized portfolios. 

Use the Pandas library to help Harold construct an optimized portfolio of stocks and plot and compare the returns of a `$10,000` investment in the portfolio to other less-optimized portfolios over time.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the the following CSVs as Pandas DataFrames and set the `date` column as a datetime index for each DataFrame:

    * `bk_data.csv`
    * `fang_data.csv` 
    * `jnj_data.csv` 
    * `luv_data.csv`
    * `mu_data.csv` 
    * `nke_data.csv`
    * `sbux_data.csv`
    * `t_data.csv`
    * `wdc_data.csv`
    * `wrk_data.csv`

  * Combine the DataFrames so that the closing prices from each DataFrame are stacked column-by-column.

  * Use the `sort_index` function to sort the combined DataFrame by datetime index in ascending order (past to present)

  * Rename the columns to reflect the corresponding stock.

  * Use the `pct_change` function to calculate daily returns for each stock.

  * Use the `corr` function and the `heatmap` function from the `seaborn` library to calculate and visualize the correlations for each stock pair, respectively.

  * Drop highly correlated stocks (5 stocks should be dropped) and keep only non-correlated stocks from the DataFrame.

  * Use the `std` function and multiply by `sqrt(252)` to calculate annualized volatility and assess the riskiness of the uncorrelated stocks.

  * Use the `mean` and `std` function to calculate the annualized sharpe ratio and assess the reward-to-risk of the non-correlated stocks.

  * Drop stocks with negative sharpe ratios (3 stocks should be dropped) from the DataFrame.

  * Set an equal weight for each stock in the optimized portfolio (only stocks that are non-correlated and have positive sharpe ratios) and use the `dot` function to multiply weights by each stock's daily returns to output the optimized portfolio's daily returns.

  * Calculate the optimized portfolio cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Set an equal weight for each stock in an non-correlated stock portfolio (only stocks that are non-correlated but have positive and negative sharpe ratios) and use the `dot` function to multiply weights by each stock's daily returns to output the non-correlated stock portfolio's daily returns.

  * Calculate the non-correlated stock portfolio's cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Set an equal weight for each stock in an unoptimized portfolio (all 10 stocks) and use the `dot` function to multiply weights by each stock's daily returns to output the optimized portfolio's daily returns.

  * Calculate the unoptimized stock portfolio's cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Overlay the investment trend of every portfolio on a single chart.

## Hints

* Breathe easy! Take this activity step-by-step and remember that this activity is a culminating activity, therefore try to think about the big picture about what makes a particular stock portfolio a good investment.