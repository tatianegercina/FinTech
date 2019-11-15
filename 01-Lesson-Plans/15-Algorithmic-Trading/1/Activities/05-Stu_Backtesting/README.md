# The Big Short Part II

The real estate bubble that led to the financial crisis in 2008 resulted in one of the worst economic disasters since the Great Depression of 1929. During this period, housing prices fell precipitously, causing massive ripples throughout the U.S. economy and ultimately causing the stock market to crash. Some keen investors profited off of the recession by *shorting* the market or placing bets that the market would fall. Most, however, lost substantial value from their investment portfolios, including much-needed retirement accounts and savings accounts.

Now that you have developed a Short Position Dual Moving Average Crossover Trading Strategy and determined that the algorithm could have *made* money during the 2008 financial recession, it is now time to determine *how much* money could have been made.

## Part 1 Instructions: The Big Short Part I

You completed this in the last activity, nice job!

## Part 2 Instructions: The Big Short Part II

The pre-requisite steps for developing the Short Position Dual Moving Average Crossover trading strategy have already been provided for you. Therefore, continue onwards to the backtesting parts of the notebook file.

Using the [starter file](Unsolved/the_big_short_part_2.ipynb), complete the following steps:

* Set an `initial_capital` variable to 100000, representing the simulated starting portfolio value.

* Set a negative `share_size` value of -500.

* Create a new column `Position` by multiplying the `share_size` by the values in the `Signal` column.

* Create a new column `Entry/Exit Position` by using the `diff` function on the `Position` column.

* Create a new column `Portfolio Holdings` by multiplying the `Close` prices of VNQ by the cumulative sum of the values of the `Entry/Exit Position` column.

* Create a new column `Portfolio Cash` by subtracting the `initial_capital` by cumulative sum of the product of the `Close` prices of VNQ and the values of the `Entry/Exit Position` column.

* Create a new column `Portfolio Total` by adding the values of the `Portfolio Cash` and `Portfolio Holdings` columns.

* Create a new column `Portfolio Daily Returns` by using the `pct_change` function on the `Portfolio Total` column.

* Create a new column `Portfolio Cumulative Returns` by using the `cum_prod` function on the `Portfolio Daily Returns` column.

* Use the `figure` and `axes` objects of the `matplotlib` library to plot the Short Position Dual Moving Average Crossover trading strategy against its backtesting results.

## Hint

Remember that shorting a stock means to sell shares of a stock and then buy or cover the shares at a later point in time. Therefore, share sizes relative to backtesting calculations should be negative.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
