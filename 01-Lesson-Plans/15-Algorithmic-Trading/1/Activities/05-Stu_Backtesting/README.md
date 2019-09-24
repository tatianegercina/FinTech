# The Big Short Part II

The real estate bubble that led to the financial crisis in 2008 resulted in one of the worst economic disasters since the Great Depression of 1929. During this period, housing prices fell precipitously, causing massive ripples throughout the U.S. economy and ultimately causing the stock market to crash. Some keen investors profited off of the recession by *shorting* the market or placing bets that the market would fall. Most, however, lost substantial value from their investment portfolios, including much-needed retirement accounts and savings accounts.

Now that you have developed a Short Position Dual Moving Average Crossover Trading Strategy and determined that the algorithm could have *made* money during the 2008 financial recession, it is now time to determine *how much* money could have been made.

## Part 1 Instructions: The Big Short Part I

You completed this in the last activity, nice job!

## Part 2 Instructions: The Big Short Part II

Using the [starter file](Unsolved/the_big_short_part_2.ipynb.ipynb), complete the following steps:

1. Import the `pandas`, `numpy`, `matplotlib`, and `pathlib` libraries. Optionally, set the pandas DataFrame settings to display more rows and columns.

2. Create a DataFrame by reading in the `vnq.csv` file containing stock data for VNQ from 2007 to 2009.

3. Create a Dual Moving Average Crossover Trading Signal that indicates shorting opportunities.

    1. Create a filtered DataFrame containing just the `Date` and `Close` columns of the VNQ stock data.

    2. Set the `Date` column as the index to the DataFrame and convert the datetime strings to datetime objects.

    3. Set a `short_window` and `long_window` to `50` and `100`, respectively.

    4. Create a 50-day moving average and a 100-day moving average from the VNQ closing prices using the `rolling` and `mean` functions.

    5. Initialize a new DataFrame column `Signal` and set the values to 0.

    6. Use the numpy `where` function to specify that when the short window MA is less than the long window MA, set the value to the `Signal` column as 1 or 0, respectively.

    7. Use the `diff` function on the `Signal` column and assign the values to a `Entry/Exit` column to indicate trade entry and exit points in time.

4. Plot the entry and exit points of your Short Dual Moving Average Crossover signal.

    1. Use the `figure` and `axes` objects from the matplotlib library to create the figure layout and the x and y coordinates, respectively.

    2. Plot the VNQ closing prices as well as the 50-day moving average and 100-day moving average.

    3. Plot the entry and exit points and mark the coordinates with marker symbols.

## Hint

Remember that shorting a stock means to sell shares of a stock and then buy or cover the shares at a later point in time. Therefore, in particular, share sizes relative to backtesting calculations should be negative.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
