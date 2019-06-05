# Free Throw Simulation

In this activity, a coach wants to know how one of his players may perform in the long-run when it comes to free throws. The player has a free throw accuracy of approximately `70%` and therefore makes on average `7` free throws for every `10` shots. The coach wants to know the likelihood of the player making `10` straight free throws in a single session.

Create a Monte Carlo simulation with `1000` simulations of `10` free throws to analyze the player's frequency distribution of made free throws and the corresponding probability distribution of made free throws to determine the likelihood of the player making `10` straight free throws.

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

## Hints

* To learn more about diversification and how correlation amongst stocks in portoflios play a factor to minimizing risk, read more [here](https://www.investopedia.com/terms/d/diversification.asp)  