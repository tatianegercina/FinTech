# Stock Price Forecasting

In this activity, Harold's manager wants Harold to take a look at one year's worth of `TSLA` stock prices and plot a potential stock trajectory for where `TSLA` stock prices could go in the next `3` years. In addition, he would like to know how a `$10,000` investment would perform given the simulated results.

Help Harold by creating a Monte Carlo simulation that simulates the next `252 * 3` trading days using one year's worth of `TSLA` stock data to perform a normally distributed random selection based on the sample mean and standard deviation of historical `TSLA` daily returns. Plot the simulated results of `TSLA` stock prices over the next `3` years as well as the corresponding cumulative returns.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Write a Monte Carlo simulation that loops through `10` free throws for every simulation of `1000` simulations and saves the results:

    * Set variables for the desired number of simulations and free throws.

    * Create a list `throw` consisting of the strings `made` and `missed`

    * Create an empty `pandas` DataFrame to hold the results of each simulation.

    * Create a nested for loop to loop through `10` free throws for every simulation of `1000` simulations.

    * Use the `choice` function from the `random` class of the `numpy` library to randomly choose between the list elements `made` and `missed` of the `throw` list. Use the `p` parameter for the `choice` function to specify the probabilities of making a free throw and missing a free throw; set the `p` parameter to `[0.7,0.3]`.

    * Append the results to the DataFrame, with each column set as the series of free throw results for every simulation.

  * Loop through every column of the DataFrame and use the `value_counts` function to count the number of made free throws per simulation. Select only the values of the `made` key from the Series object that the `value_counts` function returns. Save results to another DataFrame.

  * Create a frequency distribution histogram from the DataFrame of made free throws per simulation. Make sure to manually set the bin edges using the `bin` parameter.

  * Create a probability distribution histrogram from the DataFrame of made free throws per simulation. Set the `density` parameter to `True`.

  * Using the probability distribution histogram, assess the likelihood of the player making `9-10` free throws in a single session (results may vary with each run of the program).

## Hints

* To learn more about histograms and probability distributions, read more [here](https://learnche.org/pid/univariate-review/histograms-and-probability-distributions)  