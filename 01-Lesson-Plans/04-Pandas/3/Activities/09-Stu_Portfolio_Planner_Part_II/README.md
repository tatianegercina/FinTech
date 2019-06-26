# Portfolio Planner, Part 2

Harold has been asked to revisit the 10 stocks that were researched in Part 1 of this activity: 

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

Specifically, upper management wants Harold to go beyond just evaluating stocks by volatility/risk and create a more optimized portfolio with the following characteristics:

* Equal-weighted allocations

* Only non-correlated stocks

* Only postive return-to-risk ratio stocks (Sharpe ratios)

Then, they want to visualize the returns of a hypothetical $10,000 investment in such a constructed portfolio over time, as well as how such a portfolio compares to $10,000 investments in less optimized portfolios. 

Use the Pandas library to help Harold construct an optimized portfolio of stocks, and then plot and compare the returns of a $10,000 investment in the portfolio over time to less optimized portfolios. 

## Instructions

Using the starter file, complete the following steps:

1. Reset the DataFrame for daily returns of the 10 stocks. Use the `pct_change` function to calculate and reassign a new DataFrame of daily returns.

1. Use the `corr` function and the `heatmap` function from the `seaborn` library to calculate and visualize the stock return correlations for each stock pair.

1. Drop highly correlated stocks and keep only non-correlated stocks from the DataFrame. (2 stocks should be dropped.) 

1. Use the `mean` and `std` functions to calculate the annualized Sharpe ratio and assess the reward-to-risk ratio of the non-correlated stocks.

1. Drop stocks with negative Sharpe ratios from the DataFrame. (3 stocks should be dropped.)

1. Assess the investment potential of a non-correlated (diversified) and return-to-risk (Sharpe ratio) optimized portfolio:

    * Set an equal weight for each stock in the optimized portfolio (5 stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the optimized portfolio's daily returns.

    * Calculate the optimized portfolio's cumulative returns, and then multiply the initial investment of $10,000 against the portfolio's series of cumulative returns. Plot the trend.

1. Assess the investment potential of a non-correlated (diversified) portfolio:

    * Set an equal weight for each stock in a non-correlated stock portfolio (8 stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the non-correlated stock portfolio's daily returns.

    * Calculate the non-correlated stock portfolio's cumulative returns, and then multiply the initial investment of $10,000 against the portfolio's series of cumulative returns. Plot the trend.

1. Assess the investment potential of the original unoptimized portfolio:

    * Set an equal weight for each stock in an unoptimized portfolio (all 10 stocks). Use the `dot` function to multiply weights by each stock's daily returns to output the unoptimized portfolio's daily returns.

    * Calculate the unoptimized stock portfolio's cumulative returns, and then multiply the initial investment of `$10,000` against the portfolio's series of cumulative returns. Plot the trend.

1. Overlay the investment trend of every portfolio on a single chart, including the portfolio constructed in Part 1.

## Hint

Breathe easy! Take this activity one step at a time. Remember that this is the culminating activity of the unit. Think about the bigger picture in terms of what makes a particular stock portfolio a good investment. 

- - - 
© 2019 Trilogy Education Services