### 9. Instructor Do: Returns (15 mins)

**Files:**

* [returns.ipynb](Activities/09-Ins_Returns/Solved/returns.ipynb)

Walk through the demo and explain the following:

* What is a return or Return on Investment (ROI)?

  > A Return on Investment (ROI) is a percentage calculation that signifies either a profit or loss relative to the initial cost of an investment. ROI calculations can be used to standardize and compare the investment performances of varying asset classes such as equities, bonds, real estate, etc.

  ```python
  # ROI = (Current Value of Investment - Cost of Investment) / Cost of Investment
  initial_investment = 100
  current_price = 110

  roi = (current_price - initial_investment) / initial_investment
  roi_pct = roi * 100
  print(f"ROI for an initial investment of ${initial_investment}"
        f"now priced at ${current_price}"
        f"is {roi} or {roi_pct}%")
  ```

  ```
  ROI for an initial investment of $100 now priced at $110 is 0.1 or 10.0%
  ```

* What are daily returns?

  > Daily returns are a series of returns calculated over the course of several days, with each daily return representing the relative increase or decrease in investment between days.

* The `shift()` function creates an offset of a DataFrame index by a specified amount. In this case, the index of the `sp500_csv` is offset by `1` to emulate the daily return formula.

  ![shift-function](Images/shift-function.png)

* The `pct_change()` function calculates the percentage difference between each element of a time series. Therefore, for time series data such as daily closing prices of a stock, using the `pct_change()` function conveniently produces a series of daily returns.

  ![pct-change-function](Images/pct-change-function.png)

* Plotting daily returns makes it easier to see overall variations in daily returns over a course of time. In particular, plotting daily returns make it easier to see high and low spikes compared to the general trend. Such spikes in daily returns may indicate a market event.

  ![Plot of Daily Returns](Images/daily-return-plot.png)   

* What are cumulative returns?

  > Cumulative returns are a series of returns, with each return representing the relative increase or drecrease in price of an asset at time `t` compared to the initial price of that asset at time `t0`. Cumulative returns describe the progression of the Return on Investment of an asset over time.

* The `cumprod()` function multiplies each number in a series with the next successive number until the end of the series.

* The equation `(1 + daily_returns).cumprod() - 1` therefore means that each daily return is expressed as a multiplier (ex. daily return of 0.5% is 1.005), the `cumprod()` function cumulatively multiplies each number with its successive number, and the `-1` brings the result from a multiplier expression back to a typical return value scale (ex. daily return of 0.5% is 0.005).

  ![cumprod-function](Images/cumprod-function.png)

* Plotting cumulative returns makes it easier to visualize the profitability of a single asset, and in particular, the profitabilites of several asset classes over time. In this case, the plot shows that the S&P 500 grew more than 50% from 2014 to 2019.

  ![Plot of Cumulative Returns](Images/cumulative-return-plot.png)
