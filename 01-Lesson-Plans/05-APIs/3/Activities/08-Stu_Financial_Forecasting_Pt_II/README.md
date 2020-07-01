# Financial Forecasting Part II

In this three-part activity, Harold was praised for his projection of `BB` stock price over the next `3` trading years; however, now his manager wants to investigate deeper and ask the following questions:

* What are the probabilities of `20` ranges (or bins) for `BB` stock price outcomes?

* What range of ending stock price are we `95%` certain that `BB` stock price will result in?

Help Harold by creating a Monte Carlo simulation that performs `1000` simulations of `BB` stock over the next `252 * 3` trading days using one year's worth of `BB` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `BB` daily returns. Plot the frequency and the probability distribution of `20` bins/ranges of simulated ending prices for `BB` stock over the next `3` years and determine the `95%` confidence interval of ending `BB` prices.

## Part 1 Instructions: Stock Price Forecasting

You completed this in the last activity, nice job!

## Part 2 Instructions: Probable Stock Price Forecasts

* Using the starter file provided, walk through the following steps.

  * Data preparation has been done for you to conserve time. Proceed to executing the Monte Carlo simulation.

  * Rewrite the Monte Carlo simulation to include a `for` loop for the number of simulations and append the results of each simulation as a column to a `Pandas` DataFrame.

  * Plot the DataFrame containing `252 * 3` results of each simulation to chart `1000` possible trajectories of `BB` stock price. Set the `legends` parameter to `None`.

  * Filter the DataFrame and take the last row, which represents the closing prices of simulated `BB` stock price trajectories on their last day.

  * Use the Series object containing the price outcomes of `BB` stock to plot a frequency distribution histogram with `20` bins/data ranges.

  * Use the `value_counts` function and set the `bins` parameter to `20`. Divide each bin by the `len` of values in the series of simulated ending prices for `BB` (should be `1000`) to plot the probability distribution of each bin/data range.

  * Use the `quantile` function to calculate a `95%` confidence interval of `BB` stock price outcomes.

  * Plot the probability distribution histogram of `20` bins of `BB` stock price outcomes and mark the upper and lower bounds of the `95%` confidence interval.

  * Calculate the cumulative return of the lower and upper bounds of `BB` stock prices to determine the percentage change of stock price from the first simulated trading day to the last. Multiply `$10,000` by the cumulative returns of the lower and upper bounds to calculate a `95%` confidence interval in terms of a `$10,000` investment based on the simulated `BB` stock performance.

## Part 3 Instructions: Portfolio Forecasting

We're amost there, so get ready!

## Hints

* This activity's basis rests in the idea of nested `for` loops, for multiple simulations of stock price trajectories and analyzing the frequency (or probability distribution) of simulated stock price outcomes, to make better predictions on where `BB` stock price could end up.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
