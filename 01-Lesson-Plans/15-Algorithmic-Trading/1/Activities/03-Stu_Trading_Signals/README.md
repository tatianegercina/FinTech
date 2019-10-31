# The Big Short Part I

The real estate bubble that led to the financial crisis in 2008 resulted in one of the worst economic disasters since the Great Depression of 1929. During this period, housing prices fell precipitously, causing massive ripples throughout the U.S. economy and ultimately causing the stock market to crash. Some keen investors profited off of the recession by *shorting* the market or placing bets that the market would fall. Most, however, lost substantial value from their investment portfolios, including much-needed retirement accounts and savings accounts.

If you had an algorithm to monitor and *short* the market in 2008, could you have possibly *made* money? Create a dual moving average crossover strategy that would have shorted VNQ (Real Estate ETF) stock during the years between 2007 and 2009.

## Instructions

Using the [starter file](Unsolved/the_big_short.ipynb), complete the following steps:

* Create a Dual Moving Average Crossover Trading Signal that indicates shorting opportunities.

  * Create a filtered DataFrame containing just the `Date` and `Close` columns of the VNQ stock data.

  * Set the `Date` column as the index to the DataFrame.

  * Set a `short_window` and `long_window` to `50` and `100`, respectively.

  * Create a 50-day moving average and a 100-day moving average from the VNQ closing prices using the `rolling` and `mean` functions.

  * Initialize a new DataFrame column `Signal` and set the values to 0.

  * Use the numpy `where` function to set the signal column to `1.0` when the SMA50 is less than SMA100 and `0.0` otherwise.

  * Use the `diff` function on the `Signal` column and assign the values to a `Entry/Exit` column to indicate trade entry and exit points in time.

* Plot the entry and exit points of your Short Dual Moving Average Crossover signal.

  * Create scatter plots for the entry and exit points. Use the color green to indicate the entry points. Use a second scatter plot with red markers to indicate the exit points.

  * Create line plots for the VNQ closing prices, the 50-day moving average, and the 100-day moving average.

  * Create a composite plot that overlays all of the above into a single plot.

---

## Hints

* Remember that taking a short position (profiting off of selling) is the inverse of taking a long position (profiting off of buying), therefore make sure the decision logic regarding your trading signal reflects this!

* To read more on what a short position is, click [here!](https://www.investopedia.com/terms/s/short.asp)

* Refer to the Holoviews or Hvplot documentation to see how to [compose plots](https://holoviz.org/tutorial/Composing_Plots.html).

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
