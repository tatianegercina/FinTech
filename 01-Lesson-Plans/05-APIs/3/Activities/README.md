# Portfolio Planner Part II

In this two-part activity, Harold has been asked to re-visit the 10 stocks he previously researched: 

* Bank of New York Mellon (BK)
* Diamondback Energy (FANG)
* Johnson & Johnson (JNJ)
* Southwest Airlines Co (LUV)
* Micron Technologies (MU)
* Nike (NKE)
* Starbucks (SBUX)
* AT&T (T)
* Western Digital (WDC)
* Westrock (WRK) 

Specifically, upper management wants to go beyond just evaluating stocks by volatility/risk, they now want to create a more optimized portfolio with the following characteristics:

* Equal-weighted allocations
* Only non-correlated stocks
* Only postive return-to-risk ratio stocks (sharpe ratios)

Then, they want to visualize what the returns of a hypothetical `$10,000` investment would be if invested in such a constructed portfolio over time as well as how such a portfolio compares to `$10,000` investments in other lesser-optimized portfolios. 

Use the Pandas library to help Harold construct an optimized portfolio of stocks and plot and compare the returns of a `$10,000` investment in the portfolio to other less-optimized portfolios over time.

## Part I Instructions

You completed this in the last activity, nice job!

## Part II Instructions

Using the starter file provided, pick up where part 1 left off and walk through the following steps:

  * Reset the DataFrame for daily returns of the 10 stocks. Use the `pct_change` function again to calculate and re-assign a new DataFrame of daily returns.

  * Use the `corr` function and the `heatmap` function from the `seaborn` library to calculate and visualize the stock return correlations for each stock pair, respectively.

  * Drop highly correlated stocks (2 stocks should be dropped) and keep only non-correlated stocks from the DataFrame.

  * Use the `mean` and `std` function to calculate the annualized sharpe ratio and assess the reward-to-risk of the non-correlated stocks.

  * Drop stocks with negative sharpe ratios (3 stocks should be dropped) from the DataFrame.

  * Assess the investment potential of a non-correlated (diversified) and return-to-risk (sharpe ratio) optimized portfolio:

    * Set an equal weight for each stock in the optimized portfolio (5 stocks) and use the `dot` function to multiply weights by each stock's daily returns to output the optimized portfolio's daily returns.

    * Calculate the optimized portfolio's cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Assess the investment potential of a non-correlated (diversified) portfolio:

    * Set an equal weight for each stock in an non-correlated stock portfolio (8 stocks) and use the `dot` function to multiply weights by each stock's daily returns to output the non-correlated stock portfolio's daily returns.

    * Calculate the non-correlated stock portfolio's cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Assess the investment potential of the original/unoptimized portfolio:

    * Set an equal weight for each stock in an unoptimized portfolio (all 10 stocks) and use the `dot` function to multiply weights by each stock's daily returns to output the unoptimized portfolio's daily returns.

    * Calculate the unoptimized stock portfolio's cumulative returns and multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

  * Overlay the investment trend of every portfolio on a single chart, including the portfolio constructed in part 1.

## Hints

* Breathe easy! Take this activity step-by-step and remember that this activity is a culminating activity, therefore try to think about the big picture about what makes a particular stock portfolio a good investment.