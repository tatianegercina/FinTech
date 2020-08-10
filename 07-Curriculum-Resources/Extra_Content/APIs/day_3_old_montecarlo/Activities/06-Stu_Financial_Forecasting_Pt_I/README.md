# Financial Forecasting Part I

In this three-part activity, Harold's manager wants Harold to take a look at one year's worth of `TSLA` stock prices and plot a potential stock trajectory for where `TSLA` stock prices could go in the next `3` years. In addition, he would like to know how a `$10,000` investment would perform given the simulated results.

Help Harold by creating a Monte Carlo simulation that simulates the next `252 * 3` trading days using one year's worth of `TSLA` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `TSLA` daily returns. Plot the simulated results of `TSLA` stock prices over the next `3` years as well as the corresponding cumulative returns.

## Part 1 Instructions: Stock Price Forecasting

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Use the `list_assets()` function to confirm that `TSLA` is an available ticker on the `Alapca` API.

  * Use the `get_barset()` function to retrieve `1` year's worth of daily prices for `TSLA` stock as a `pandas` DataFrame. Use the `datetime` library to specify a `start_date` and `end_date`.

  * Drop extraneous `levels` and `columns`, keep only the `close` column of the resulting DataFrame.

  * Use the `pct_change` function to calculate the daily returns of `TSLA` stock.

  * Use the `mean` and `std` functions to calculate the average and volatility of historical `TSLA` daily returns.

  * Write a Monte Carlo simulation that loops through `252 * 3` trading days and saves the results:

    * Set a variable for `252 * 3` trading days.

    * Create a list to hold simulated `TSLA` closing prices with the last closing price of the sample (data from Alpaca API call) as its first element.

    * For every trading day, calculate a simulated price using the preceding day's closing price multiplied by ```(1 + np.random.normal(avg_daily_return, std_dev_daily_return)```. In other words, multiply the preceding closing price by a randomly generated daily return based on a normal probability distribution of historical `TSLA` daily returns. Save the results to a `pandas` DataFrame.

    * Plot the simulated daily closing prices of `TSLA` stock over the next `3` trading years.

    * Calculate the daily returns and cumulative returns of simulated daily closing prices of `TSLA` stock over the next `3` trading years.

    * Plot the cumulative profits and losses for a `$10,000` investment in TSLA given the simulated cumulative returns.

## Part 2 Instructions: Probable Stock Price Forecasts

You'll complete this in the next student activity! Get ready!

## Part 3 Instructions: Portfolio Forecasting

The culminating activity—by this point, you'll be stock price fortune tellers!

## Hints

* Remember that a normal probability distribution is just a diagram illustrating the probability of potential outcomes as outcomes deviate closer to or away from the expected average.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
