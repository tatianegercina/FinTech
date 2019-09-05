# Financial Forecasting Part III

In this three-part activity, Harold has been asked to revisit the Monte Carlo simulation for future stock prices of `TSLA`. Given the volatility of projected future `TSLA` stock prices, upper management wants to test the returns of a portfolio containing both `TSLA` and `SPHD` — an S&P 500 High Dividend Low Volatility ETF — to buffer against `TSLA` stock's volatility; they are thinking of allocating `25%` of capital to `TSLA` and the other `75%` to `SPHD`. 

Upper management wants answers to the following questions:

  * What is the expected range of projected cumulative returns of the given portfolio?
  * What is the `95%` confidence interval of projected cumulative returns of the given portfolio?
  * What is the `95%` confidence interval of projected cumulative investment for the given portfolio?

Use the `pandas` library to help simulate the cumulative returns of a `25-75` weighted `TSLA-SPHD` portfolio over the next `3` trading years (`252 * 3` trading days).

## Part 1 Instructions: Stock Price Forecasting

You completed this already, nice job!

## Part 2 Instructions: Probable Stock Price Forecasts

You completed this in the last activity, you're killin' it!

## Part 3 Instructions: Portfolio Forecasting

Using the starter file provided, pick up where part II left off and walk through the following steps:

  * Rewrite the Monte Carlo simulation code to output a DataFrame of both `TSLA` and `SPHD` simulated stock prices over the next `252 * 3` trading days.

    * Create a for loop to simulate `252 * 3` trading days worth of future stock prices for `TSLA` and `SPHD`. Use a random selection of daily returns for each ticker based on a normal probability distribution of their means and standard deviations. Append results to a `pandas` DataFrame.

    * Use the `pct_change` function to calculate the daily returns of both `TSLA` and `SPHD`.

    * Set a list of weights `[0.25, 0.75]` and use the `dot` function on the DataFrame containing `TSLA` and `SPHD` simulated daily returns to calculate the simulated daily returns of a portfolio containing `25%` `TSLA` and `75%` `SPHD`.

    * Use the `cumprod` function to calculate the cumulative returns of the portfolio. Append the Series of simulated cumulative returns for the portfolio to a column of a DataFrame. Do this for each simulation in the Monte Carlo simulation.

  * Plot the simulated cumulative returns of the portfolio over the `252 * 3` trading day range.

  * Take the last row of the DataFrame containing cumulative portfolio returns for each simulation and plot a frequency distribution histogram. Set the `bins` parameter to `10`.

  * Use the `value_counts` and `len` functions to calculate the probability of cumulative return ranges for the portfolio. Set the `bins` parameter to `10`.

  * Use the `quantile` function to calculate the lower and upper bounds of a `95%` confidence interval of potential cumulative returns for the portfolio.

  * Plot the upper and lower bounds of the `95%` confidence interval on a probability distribution histogram. Set the `density` parameter for the histogram to `True`.

  * Answer the questions for upper management.

## Hints

* This is a culminating activity that should test all portions of today's class. Therefore, walk through the process step-by-step and review instructor activities for technical clues on how to complete the code.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
