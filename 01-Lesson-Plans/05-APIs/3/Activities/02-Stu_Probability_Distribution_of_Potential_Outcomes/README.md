# Free Throw Simulation

In this activity, a coach wants to know how one of his players may perform in the long-run when it comes to free throws. The player has a free throw accuracy of approximately `70%` and therefore makes on average `7` free throws for every `10` shots. The coach wants to know the likelihood of the player making `10` straight free throws in a single session.

Create a Monte Carlo simulation with `1000` simulations of `10` free throws to analyze the player's frequency distribution of made free throws and the corresponding probability distribution of made free throws to determine the likelihood of the player making `10` straight free throws.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the following as Pandas DataFrames:

    * `HD.csv`
    * `JNJ.csv`
    * `INTC.csv`
    * `AMD.csv`
    * `MU.csv`
    * `NVDA.csv`
    * `TSM.csv`

  * Use the `concat` function to combine the 7 DataFrames into a single combined DataFrame.

  * Use the `corr` function on the combined DataFrame to calculate and output a correlation table of each stock-to-stock pair.

  * Use the `heatmap` function from the seaborn library to create a heatmap of correlation values.

  * Use the `vmin` and `vmax` parameters to the `heatmap` function to adjust the correlation scale. Set `vmin` equal to -1 and `vmax` to 1.

  * From the heatmap, choose the stock with the least correlation to `JNJ` and `HD` that should be added to the existing portfolio.

## Hints

* To learn more about diversification and how correlation amongst stocks in portoflios play a factor to minimizing risk, read more [here](https://www.investopedia.com/terms/d/diversification.asp)  