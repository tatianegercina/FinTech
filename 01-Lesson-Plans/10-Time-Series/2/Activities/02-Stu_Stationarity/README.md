# Stationarize It

## Instructions

In this activity, you will stationarize a non-stationary time series. The dataset is a time series of Amazon stock prices from years 2009 through 2011.

As you can see from the initial plot of the closing stock price, this time series is not stationary (it trends upwards). Perform the techniques below to stationarize your time series.

When adding new columns to the DataFrame, work with the closing stock prices. Don't forget to drop `NaN` values!

1. Determine if the series is stationary or not by applying the Augmented Dickey-Fuller test (`adfuller` method from `statsmodels').

2. Create a column named `Returns` in the DataFrame using the `pct_change()` function. Its values will be the return, or the change of the stock price in percentage points from one day to the next. Plot the returns.

3. Create a column named `Diff` in the DataFrame using the `diff()` function. Its values will be the difference in stock price from one day to the next. Plot this column.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
