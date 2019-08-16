# Diversification

Harold's company wants to build a diversified stock portfolio. So far, it has added `JNJ` (Johnson & Johnson) and `HD` (Home Depot), which reside within the Healthcare and Consumer Discretionary sectors, respectively. Now they want to add a third technology sector stock to the mix, in particular, a semiconductor stock.

Harold's manager has asked him to research a set of five semiconductor stocks to add to the existing portfolio. To create a diversified portfolio that tends to minimize long-term volatility/risk, stocks within the portfolio should be as uncorrelated as possible so as to create a counterbalance effect (i.e, when some stocks fall in price, others may rise in price).  

Use the Pandas library to help Harold analyze five semiconductor stocks—`INTC`, `AMD`, `MU`, `NVDA`, and `TSM`—and choose the stock with the least correlation to `JNJ` and `HD`.

## Instructions

Using the [starter file](Unsolved/diversification.ipynb), complete the following steps.

1. Import libraries and dependencies.

1. Read in the following CSV files as Pandas DataFrames:

    * `HD.csv`
    * `JNJ.csv`
    * `INTC.csv`
    * `AMD.csv`
    * `MU.csv`
    * `NVDA.csv`
    * `TSM.csv`

1. Use the `concat` function to combine the seven DataFrames into a single combined DataFrame.

1. Use the `corr` function on the combined DataFrame to calculate and output a correlation table of each stock-to-stock pair.

1. Use the `heatmap` function from the Seaborn library to create a heatmap of correlation values.

1. Use the `vmin` and `vmax` parameters with the `heatmap` function to adjust the correlation scale. Set `vmin` equal to -1 and `vmax` to 1.

1. From the heatmap, choose the stock with the least correlation to `JNJ` and `HD` that should be added to the existing portfolio.

## Hint

Go [here](https://www.investopedia.com/terms/d/diversification.asp) to learn more about diversification and how correlation among stocks in portfolios are a factor in minimizing risk.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
