# Archery Target Hits

In this activity, a beginner archer has a shot accuracy of approximately `20%` and therefore on average hits the target `1` time for every `5` shots. His archery master wants to assess the beginner archer's *long-term performance* of hitting the target, and therefore wants to simulate and predict the beginner archer's performance over many trials. Specifically, the archery master wants to know what the range of hit targets (out of `5` shots) the beginner archer is likely to make for a `95%` confidence interval. In other words, what is the range of targets that the beginner archer will hit out of `5` shots if he is `95%` certain of the outcome?

Create a Monte Carlo simulation with `1000` simulations of `5` shots to analyze the beginner archer's frequency distribution and corresponding probability distribution of hit targets to determine the `95%` confidence interval of hit targets.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Write a Monte Carlo simulation that loops through `5` shots for every simulation of `1000` simulations and saves the results:

    * Set variables for the desired number of simulations and shots.

    * Create a list `shot` consisting of the strings `hit` and `missed`.

    * Create an empty `pandas` DataFrame to hold the results of each simulation.

    * Create a nested for loop to loop through `5` shots for every simulation of `1000` simulations.

    * Use the `choice` function from the `random` class of the `numpy` library to randomly choose between the list elements `hit` and `missed` of the `shot` list. Use the `p` parameter for the `choice` function to specify the probabilities of hitting a shot and missing a shot; set the `p` parameter to `[0.2, 0.8]`.

    * Append the results to the DataFrame, with each column set as the series of free throw results for every simulation.

  * Loop through every column of the DataFrame and use the `value_counts` function to count the number of hit targets per simulation. Select only the values of the `hit` key from the Series object that the `value_counts` function returns. Save the results to another DataFrame.

  * Create a frequency distribution histogram from the DataFrame of hit targets per simulation. Make sure to manually set the bin edges using the `bin` parameter.

  * Create a probability distribution histogram from the DataFrame of hit targets per simulation. Set the `density` parameter to `True`.

  * Use the `quantile` function and create a `95%` confidence interval range from the DataFrame of hit targets per simulation.

  * Plot the upper and lower bounds of the `95%` confidence interval over the probability distribution histogram of hit targets.

## Hints

* To learn more about confidence intervals, read more [here](https://www.khanacademy.org/math/ap-statistics/estimating-confidence-ap/introduction-confidence-intervals/a/interpreting-confidence-levels-and-confidence-intervals).

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
