# Beta Comparisons

In this activity, Harold has been asked to calculate and plot the 30-day rolling betas for social media stocks Facebook (FB), Twitter (TWTR), and Snapchat (SNAP). Upper management is looking to potentially invest in a social media stock; however, they want to stay somewhat conservative and look toward the social media stock with the lowest beta comparatively. 

Use the Pandas library to help Harold calculate and plot the 30-day rolling betas for social media stocks and determine the social media stock with the lowest beta value.

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
