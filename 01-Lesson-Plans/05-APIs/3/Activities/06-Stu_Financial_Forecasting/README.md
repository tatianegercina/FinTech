# Financial Forecasting

In this activity, Harold's manager wants Harold to take a look at one year's worth of `TSLA` stock prices and plot a potential stock trajectory for where `TSLA` stock prices could go in the next `3` years. In addition, he would like to know how a $10,000 investment would perform given the simulated results.

Help Harold by creating a Monte Carlo simulation that simulates the next `252 * 3` trading days using three years worth of `TSLA` stock data. Plot the simulated results of `TSLA` daily returns over the next `3` years as well as the corresponding simulated outcomes.

## Instructions

Using the starter file provided, walk through the following steps.

* Import dependencies and create the Alpaca API environment.

* Use the `get_barset()` function to retrieve `3` year's worth of daily prices for `TSLA` stock as a `pandas` DataFrame.

* Build a Monte Carlo simulation that runs `1000` times through `252 * 3` trading days to determine the simulated daily returns.

* Create a new DataFrame to hold the summary statistics for the simulated daily returns.  **Hint:** You will need to calculate the _mean_, _median_, _min_ and _max_ using the `axis=1` parameter.
    
* Generate a line plot to visualize the summary statistics for the simulated daily returns.

* Create a new DataFrame to hold the summary statistics for the simulated daily returns assuming an initial investment of `$10,000`.

* Generate a line plot to visualize the updated summary statistics for simulated daily returns using a `$10,000` initial investment.

* Calculate the range of the possible outcomes for our $10,000 investment in `TSLA` stocks with a `95%` confidence interval

## Hints

* Remember that a normal probability distribution is just a diagram illustrating the probability of potential outcomes as outcomes deviate closer to or away from the expected average.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
