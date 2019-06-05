# Free Throw Simulation

In this activity, a coach wants to know how one of his players may perform in the long-run when it comes to free throws. The player has a free throw accuracy of approximately `70%` and therefore makes a free throw about `7` out of `10` times. The coach wants to know the likelihood of the player making `10` straight free throws in a single session.

Create a Monte Carlo simulation 

Harold's company is looking to build a diversified stock portfolio. So far, they've added `JNJ` (Johnson & Johnson) and `HD` (Home Depot) which both reside with the the Healthcare and Consumer Discretionary sectors, respectively. However, now they want to add a third technology sector stock to the mix, in particular, a semiconductor stock. 

As a result, Harold has been asked by his manager to research a set of 5 semiconductor stocks to add to the currently existing portfolio. In order to properly create a diversified portfolio which tends to minimize long-term volatility/risk, stocks within the portfolio should be as uncorrelated as possible so as to create a counter-balance effect (when some stocks fall in price, others may rise in price). 

Therefore, use the Pandas library to help Harold analyze 5 semiconductor stocks -- `INTC`, `AMD`, `MU`, `NVDA`, `TSM` -- and choose the stock with the least correlation to `JNJ` and `HD`.

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