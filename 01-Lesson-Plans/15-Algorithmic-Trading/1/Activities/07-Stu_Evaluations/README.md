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

1. Set an `initial_capital` variable to 100000, representing the simulated starting portfolio value.

2. Set a negative `share_size` value of -500.

3. Create a new column `Position` by multiplying the `share_size` by the values in the `Signal` column.

4. Create a new column `Entry/Exit Position` by using the `diff` function on the `Position` column.

5. Create a new column `Portfolio Holdings` by multiplying the `Close` prices of VNQ by the cumulative sum of the values of the `Entry/Exit Position` column.

6. Create a new column `Portfolio Cash` by subtracting the `initial_capital` by cumulative sum of the product of the `Close` prices of VNQ and the values of the `Entry/Exit Position` column.

7. Create a new column `Portfolio Total` by adding the values of the `Portfolio Cash` and `Portfolio Holdings` columns.

8. Create a new column `Portfolio Daily Returns` by using the `pct_change` function on the `Portfolio Total` column.

9. Create a new column `Portfolio Cumulative Returns` by using the `cum_prod` function on the `Portfolio Daily Returns` column.

10. Use the `figure` and `axes` objects of the `matplotlib` library to plot the Short Position Dual Moving Average Crossover trading strategy against its backtesting results.

## Hint

Remember that shorting a stock means to sell shares of a stock and then buy or cover the shares at a later point in time. Therefore, in particular, share sizes relative to backtesting calculations should be negative.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.





## Evaluations

Evaluate the backtesting results by calculating the annual return, cumulative returns, annual volatility, Sharpe ratio, and Sortino ratio for your portfolio. These evaluation metrics will provide insight into how well the trading algorithm performed in terms of maximizing returns and minimizing risk and volatility.

### Instructions

1. Open the starter file, and begin by calculating cumulative returns using the `signals_df` DataFrame.

2. Calculate annualized returns. Remember to multiply by the number of trading days.

3. Measure annual volatility.

4. Calculate the Sharpe ratio.

5. Calculate the downside deviation/return.

6. Calculate the Sortino ratio by dividing the average downside deviation by the average daily return.

7. Wrap all of these calculations into a single function called `calculate_eval_metrics`. The function should accept the `signals_df` DataFrame as a parameter, and it should return the `portfolio_evaluation_df` DataFrame.

8. Call the `calculate_eval_metrics` function with `signals_df` as the argument

9. Calculate the per-trade evaluation metrics by calculating the difference between exit and entry portfolio holding values.

### Hint

Consult the [evaluations calculation guide](../../../Supplemental/EvaluationsCalculationGuide.md) for the above calculations/formulas.
