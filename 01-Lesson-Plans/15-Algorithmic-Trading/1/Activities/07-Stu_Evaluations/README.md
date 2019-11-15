# The Big Short Part III

The real estate bubble that led to the financial crisis in 2008 resulted in one of the worst economic disasters since the Great Depression of 1929. During this period, housing prices fell precipitously, causing massive ripples throughout the U.S. economy and ultimately causing the stock market to crash. Some keen investors profited off of the recession by *shorting* the market or placing bets that the market would fall. Most, however, lost substantial value from their investment portfolios, including much-needed retirement accounts and savings accounts.

Now that you have developed a Short Position Dual Moving Average Crossover Trading Strategy, determined that the algorithm could have *made* money during the 2008 financial recession as well as how much, it is now time to evaluate the performance of the overall portfolio and corresponding trades.

## Part 1 Instructions: The Big Short Part I

You already completed this activity, amazing!

## Part 2 Instructions: The Big Short Part II

You completed this in the last activity, nice job!

## Part 3 Instructions: The Big Short Part III

Evaluate the backtesting results by calculating the annual return, cumulative returns, annual volatility, Sharpe ratio, and Sortino ratio for your portfolio. These evaluation metrics will provide insight into how well the trading algorithm performed in terms of maximizing returns and minimizing risk and volatility. In addition, evaluate the performance of each trade by grabbing the relevant entry and exit values, and calculate the profit/loss for each trade.

The pre-requisite steps for developing the Short Position Dual Moving Average Crossover trading strategy and backtesting against historical prices have already been provided for you. Therefore, continue onwards to the evaluation parts of the notebook file.

Using the [starter file](Unsolved/the_big_short_part_3.ipynb), complete the following steps:

1. Initialize a Portfolio Evaluation DataFrame with an index set to `['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio']` and columns as `['Backtest']`.

2. Calculate and assign the following portfolio metrics to the portfolio evaluation DataFrame:

    1. Cumulative Return

    2. Annual Return

    3. Annual Volatility

    4. Sharpe Ratio

    5. Sortino Ratio

3. Initialize a Trade Evaluation DataFrame with columns set to `['Stock', 'Entry Date', 'Exit Date', 'Shares', 'Entry Share Price', 'Exit Share Price', 'Entry Portfolio Holding', 'Exit Portfolio Holding', 'Profit/Loss']`.

4. Iterate over the backtested signals DataFrame and pull the relevant entry and exit data values to calculate the per-trade profit/loss and append each record to the Trade Evaluation DataFrame.

## Hints

* Because this is a short strategy, in order to calculate the profit/loss for each trade, the difference should be the inverse of a long strategy. In other words the profit/loss should be calculated using the entry holding value minus the exit holding value.

* Consult the [evaluations calculation guide](../../../Supplemental/EvaluationsCalculationGuide.md) for the above calculations/formulas.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
