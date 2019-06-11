### 13. Instructor Demo: Portfolio Forecasting (0:10 mins)

In this activity, students ascend to the final step and learn to project not one, but many, future stock prices using Monte Carlo simulations to calculate the daily/cumulative returns of a multi-weighted portfolio. Then analyze and plot the frequency and probability distributions of potential ending cumulative returns to assess the investment risk of the portfolio.

**Files:**

* [portfolio_forecasting.ipynb](Activities/09-Ins_Portfolio_Forecasting/Solved/portfolio_forecasting.ipynb)

Walk through the solution and highlight the following:

* The `get_historical_data` function of the `iexfinance` SDK can provide stock price data for more than one ticker in a single API call. Supplying a list of tickers with the `output_format` parameter set to `pandas` returns a multi-level index DataFrame.

  ![iex-multi-level-index](Images/iex-multi-level-index.png)

* To drop specific columns of a multi-level index DataFrame, use the `drop` function with the `level` parameter to specify the *level* of the DataFrame.

  ![drop-multi-level-index-columns](Images/drop-multi-level-index-columns.png)

* Access the Series of values of each multi-level index column using additional square bracket key notation to represent the additional levels.

  ![multi-level-index-key-notation](Images/multi-level-index-key-notation.png)