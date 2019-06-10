# Probable Stock Price Forecasting

In this activity, Harold was praised for his projection of `TSLA` stock price over the next `3` trading years; however, now his manager wants to investigate deeper and ask the following questions:

  * What is the *probable* outcome of where `TSLA` stock price could end up?
  * What are the probabilities of `20` ranges (or bins) that `TSLA` stock price could end up?
  * What range of ending stock price are we `95%` certain that `TSLA` stock price will result in?

Help Harold by creating a Monte Carlo simulation that performs `1000` simulations of `TSLA` stock over the next `252 * 3` trading days using one year's worth of `TSLA` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `TSLA` daily returns. Plot the frequency and probability distribution of `20` bins/ranges of simulated ending prices for `TSLA` stock over the next `3` years and determine the `95%` confidence interval of ending `TSLA` prices.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Use the `get_symbols` function to confirm that `TSLA` is an available ticker on the `IEX Cloud` API.

  * Use the `get_historical` function to retrieve `1` year's worth of daily prices for `TSLA` stock as a `pandas` DataFrame. Use the `datetime` library to specify a `start_date` and `end_date`.

  * Drop extraneous columns, keep only the `close` column of the resulting DataFrame.

  * Use the `pct_change` function to calculate the daily returns of `TSLA` stock.

  * Use the `mean` and `std` functions to calculate the average and volatility of historical `TSLA` daily returns.

  * Write a Monte Carlo simulation that loops through `252 * 3` trading days and saves the results:

    * Set a variable for `252 * 3` trading days.

    * Create a list to hold simulated `TSLA` closing prices with the last closing price of the sample (data from IEX API call) as its first element. 

    * For every trading day, calculate a simulated price using the preceding day's closing price multipled by ```(1 + np.random.normal(avg_daily_return, std_dev_daily_return)```. In other words, multiply the preceding closing price by a randomly generated daily return based off of a normal probability distribution of historical `TSLA` daily returns. Save the results to a `pandas` DataFrame.

    * Plot the simulated daily closing prices of `TSLA` stock over the next `3` trading years.

    * Calculate the daily returns and cumulative returns of simulated daily closing prices of `TSLA` stock over the next `3` trading years.

    * Plot the cumulative profits/losses for a `$10,000` investment in TSLA given the simulated cumulative returns. 

## Hints

* Remember that a normal probability distribution is just a diagram illustrating the probability of potential outcomes as outcomes deviate closer or away from the expected average.