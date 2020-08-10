# Financial Forecasting Part II

In this three-part activity, Harold was praised for his projection of `TSLA` stock price over the next `3` trading years; however, now his manager wants to investigate deeper and ask the following questions:

  * What are the probabilities of `20` ranges (or bins) that `TSLA` stock price could end up?
  * What range of ending stock price are we `95%` certain that `TSLA` stock price will result in?

Help Harold by creating a Monte Carlo simulation that performs `1000` simulations of `TSLA` stock over the next `252 * 3` trading days using one year's worth of `TSLA` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `TSLA` daily returns. Plot the frequency and probability distribution of `20` bins/ranges of simulated ending prices for `TSLA` stock over the next `3` years and determine the `95%` confidence interval of ending `TSLA` prices.

## Part 1 Instructions: Stock Price Forecasting

You completed this in the last activity, nice job!

## Part 2 Instructions: Probable Stock Price Forecasts

* Using the starter file provided, walk through the following steps.

  * Data preparation has been done for you to conserve time. Proceed to executing the Monte Carlo simulation.

  * Rewrite the Monte Carlo simulation to include a `for` loop for number of simulations and append the results of each simulation as a column to a `pandas` DataFrame.

  * Plot the DataFrame containing `252 * 3` results of each simulation to chart `1000` possible trajectories of `TSLA` stock price. Set the `legends` parameter to `None`.

  * Filter the DataFrame and take the last row, which represents the closing prices of simulated `TSLA` stock price trajectories on their last day.

  * Use the Series object containing the price outcomes of `TSLA` stock to plot a frequency distribution histogram with `20` bins/data ranges.

  * Use the `value_counts` function and set the `bins` parameter to `20`. Divide each bin by the `len` of values in the series of simulated ending prices for `TSLA` (should be `1000`) to plot the probability distribution of each bin/data range.

  * Use the `quantile` function to calculate a `95%` confidence interval of `TSLA` stock price outcomes.

  * Plot the probability distribution histogram of `20` bins of `TSLA` stock price outcomes and mark the upper and lower bounds of the `95%` confidence interval.

  * Calculate the cumulative return of the lower and upper bounds of `TSLA` stock prices to determine the percentage change of stock price from the first simulated trading day to the last. Multiply `$10,000` by the cumulative returns of the lower and upper bounds to calculate a `95%` confidence interval in terms of a `$10,000` investment based on the simulated `TSLA` stock performance.

## Part 3 Instructions: Portfolio Forecasting

Almost there! Get ready!

## Hints

* The basis of this activity is the idea of nested `for` loops for multiple simulations of stock price trajectories, and analyzing the frequency or probability distribution of simulated stock price outcomes to make better and more thoughtful predictions about where `TSLA` stock price could end up.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
