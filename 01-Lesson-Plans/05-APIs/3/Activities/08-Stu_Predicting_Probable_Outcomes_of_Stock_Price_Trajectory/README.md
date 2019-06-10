# Probable Stock Price Forecasts

In this activity, Harold was praised for his projection of `TSLA` stock price over the next `3` trading years; however, now his manager wants to investigate deeper and ask the following questions:

  * What are the probabilities of `20` ranges (or bins) that `TSLA` stock price could end up?
  * What range of ending stock price are we `95%` certain that `TSLA` stock price will result in?

Help Harold by creating a Monte Carlo simulation that performs `1000` simulations of `TSLA` stock over the next `252 * 3` trading days using one year's worth of `TSLA` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `TSLA` daily returns. Plot the frequency and probability distribution of `20` bins/ranges of simulated ending prices for `TSLA` stock over the next `3` years and determine the `95%` confidence interval of ending `TSLA` prices.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Data preparation has been done for you to conserve time. Proceed to executing the Monte Carlo simulation.

  * Re-write the Monte Carlo simulation to include a `for` loop for number of simulations and append the results of each simulation to a `pandas` DataFrame.

  * 

## Hints

* Remember that a normal probability distribution is just a diagram illustrating the probability of potential outcomes as outcomes deviate closer or away from the expected average.