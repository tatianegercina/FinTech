# Portfolio Allocations

In this activity, Harold has been asked to research the following 10 stocks: 

* AT&T (T)
* Starbucks (SBUX)
* Bank of New York Mellon (BK)
* Nike (NKE)
* Southwest Airlines Co (LUV)
* Westrock (WRK)
* Diamondback Energy (FANG)
* Johnson & Johnson (JNJ)
* Western Digital (WDC)
* Micron Technologies (MU)

Specifically, upper management wants to sort the stocks by risk profile/volatility, filter out the top 5 stocks with the highest volatility, and assign the remaining stocks portfolio weights of `0.5`, `0.2`, `0.15`, `0.10`, and `0.05` from the least risky stock to the most risky stock, respectively. Then, they want to see what the returns of a hypothetical `$10,000` investment would be if invested in such a constructed portfolio over time.  

Use the Pandas library to help Harold determine the risk profile of the 10 stocks, drop the top 5 highly volatile stocks, assign portfolio weights to each corresponding stock, and plot the returns of a `$10,000` investment if invested in such a portfolio over time.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the following CSVs:

    * `t_data.csv`
    * `sbux_data.csv`
    * `bk_data.csv`
    * `nke_data.csv`
    * `luv_data.csv`
    * `wrk_data.csv`
    * `fang_data.csv` 
    * `jnj_data.csv` 
    * `wdc_data.csv`
    * `mu_data.csv` 

  * Combine the DataFrames so that the closing prices from each DataFrame are stacked column-by-column.

  * Use the `sort_index` function to sort the combined DataFrame by datetime index in ascending order (past to present)

  * Rename the columns to reflect the corresponding stock.

  * Use the `pct_change` function to calculate daily returns for each stock.

  * Use the `std` function and multiply by `sqrt(252)` to calculate annualized volatility. Use the `sort_values` function to quickly sort by volatility values.

  * Drop the top 5 stocks with the highest volatility from the DataFrame of daily returns.

  * Set portfolio weights of `0.5`, `0.2`, `0.15`, `0.10`, and `0.05` to the remaining stocks, from the least risky stock to the most risky stock.

  * Use the `dot` function to multiply the weights by each column of daily returns to calculate the daily returns of the constructed portfolio.

  * Use the `cumprod` function to calculate the cumulative returns of the constructed portfolio.

  * Plot the returns of a hypothetical `$10,000` investment in the constructed portfolio.

## Hints

* To plot the returns of a `$10,000` investment, multiply the initial investment by the portfolio's cumulative returns over time.