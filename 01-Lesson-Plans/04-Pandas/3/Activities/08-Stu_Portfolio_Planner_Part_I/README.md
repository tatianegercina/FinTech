# Portfolio Planner, Part 1

Harold has been asked to research the following 10 stocks: 

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

Harold has been tasked with sorting stocks by risk/volatility; filtering out the top 5 stocks with the highest volatility; and assigning the remaining stocks portfolio weights of 0.5, 0.2, 0.15, 0.10, and 0.05 (from least risk to most risk). He also needs to show the returns over time of a hypothetical $10,000 investment in such a portfolio. 

Use the Pandas library to help Harold determine the risk profile of the 10 stocks, filter out the top 5 highly volatile stocks, assign portfolio weights to each corresponding stock, and plot the returns of a $10,000 investment in such a portfolio over time.

## Instructions

Using the starter file, complete the following steps.

1. Import libraries and dependencies. 

1. Read in the following CSV files:

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

  1. Combine the DataFrames so that the closing prices from each DataFrame are stacked column by column.

  1. Use the `sort_index` function to sort the combined DataFrame by datetime index in ascending order (past to present).

  1. Rename the columns to reflect the corresponding stock.

  1. Use the `pct_change` function to calculate daily returns for each stock.

  1. Use the `std` function and multiply by `sqrt(252)` to calculate annualized volatility. Use the `sort_values` function to quickly sort by volatility values.

  1. Drop the top 5 stocks with the highest volatility from the DataFrame of daily returns.

  1. Set portfolio weights of 0.5, 0.2, 0.15, 0.10, and 0.05 to the remaining stocks (from least risk to most risk). 

  1. Use the `dot` function to multiply the weights by each column of daily returns to calculate the daily returns of the constructed portfolio.

  1. Use the `cumprod` function to calculate the cumulative returns of the constructed portfolio.

  1. Plot the returns of a hypothetical $10,000 investment in the constructed portfolio.

## Hint

To plot the returns of a $10,000 investment, multiply the initial investment by the portfolio's cumulative returns over time.

- - - 

© 2019 Trilogy Education Services
