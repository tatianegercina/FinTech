# Portfolio Allocations

In this activity, Harold has been asked to research the following stocks: Visa (V), Mastercard (MA), Goldman Sachs (GS), and JP Morgan (JPM). Specifically, upper management wants to sort the stocks by risk profile/volatility and assign portfolio weights `0.6`, `0.2`, `0.1`, and `0.05` from the least risky stock to the most risky stock. Then, they want to see what the returns of a hypothetical $10,000 investment would be if invested in such a constructed portfolio over time.  

Use the Pandas library to help Harold determine the risk profile the 4 stocks, assign portfolio weights to the corresponding stock, and plot the returns of a $10,000 investment if invested in such a portfolio over time.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the `fb_data.csv`, `twtr_data.csv`, `snap_data.csv`, and `sp500_data.csv` as Pandas DataFrames and set the `date` column as a datetime index for each DataFrame.

  * Combine the DataFrames so that the closing prices from each DataFrame are stacked column-by-column.

  * Rename the columns to reflect the corresponding stock.

  * Use the `pct_change` function to calculate daily returns for each stock.

  * Calculate the overall covariances of each stock's daily returns to that of the S&P 500, and calculate the overall variance of S&P 500 daily returns.

  * Calculate the overall beta values of each social media stock.

  * Calculate the rolling 30-day covariances of each stock's daily returns to that of the S&P 500, and calculate the rolling 30-day variance of S&P 500 daily returns.

  * Calculate the rolling 30-day beta values of each social media stock.

  * Plot the rolling 30-day beta values of each social media stock on the same figure. Set the figure legend.

## Hints

* Remember to set the `ax` parameter when attempting to plot multiple datasets on a single chart figure.
