### 15. Instructor Do: Standard Deviation and Risk (5 mins)

**Files:**

* [std_dev_risk.ipynb](Activities/15-Ins_Std_Dev_Risk/Solved/std_dev_risk.ipynb)

Navigate to the 4.2 slides, and highlight the following:

* A key aspect of analyzing portfolio and stock data is determining risk. Pandas provides a series of functions that can be used to calculate risk. One component of risk is calculating the `mean` performance or price of a stock. The second is calculating the `standard deviation`.

* `Mean` can be used to determine the average value of a portfolio or stock overtime. This can serve as a baseline for measuring risk and value. A portfolio or stock doing better than average is more valuable. Investing in a portfolio or buying a stock doing below average is risky business.

* A common technique for measuring how far away an asset is from the `mean` is to calculate the `standard deviation`. `Standard deviation` identifies exactly how far away from the average price the value is. A low number indicates that the value is not far form the average. A high `standard deviation` means the value is an outlier.

* Risk can be assessed by evaluating the `standard deviation`.

Live code how to use Pandas to calculate `standard deviation` to evaluate risk:

* `Standard deviation` should be calculated using daily returns data. Calculating `standard deviation` against daily returns will help identify risk based off of return value rather than price volatility.

  ![std_dev.png](Images/std_dev.png)

* The `std` Pandas function can be used to determine the risk associated with a portfolio or stock. Behind the scenes, the `std` function calculates the mean/average, and then it evaluates how far away from the average the input is. The function returns a new DataFrame.

  ```python
  # Daily Standard Deviations
  daily_returns.std()
  ```

  ```
  AAPL    0.018106
  MSFT    0.017839
  GOOG    0.017724
  FB      0.023949
  AMZN    0.022768
  dtype: float64
  ```

* Portfolio and stock risk can be compared. Sorting the output from the `std` function in descending order (using `sort_values`) will display which portfolios/stocks have the most and least amounts of risk.

  ```python
  # Identify the stock with the most and least risk
  daily_std.sort_values(ascending=False)
  ```

  ![risk_sort.png](Images/risk_sort.png)

* It is common to need `standard deviation` at the yearly level. Calculating annualized standard deviation can be done by multiplying the the square root (`sqrt`) of the number of trading days in a year (`252`) with the standard deviation.

  ```python
  # Calculate the annualized standard deviation (252 trading days)
  annualized_std = daily_std * np.sqrt(252)
  annualized_std.head()
  ```

  ```
  AAPL    0.287428
  MSFT    0.283180
  GOOG    0.281354
  FB      0.380172
  AMZN    0.361434
  dtype: float64
  ```

* A key way to assess risk is to use the `plot.hist` function to create a chart of standard deviation trends. This will visually demonstrate the mean value, as well as the number and severity of any deviations.

  ```python
  portfolio_a_std = np.random.normal(scale=0.5, size=10000)
  portfolio_d_std = np.random.normal(scale=1.0, size=10000)
  portfolio_i_std = np.random.normal(scale=1.5, size=10000)

  portfolio_std = pd.DataFrame({
      "Aggressive": portfolio_a_std,
      "Defensive": portfolio_d_std,
      "Income": portfolio_i_std
  })

  portfolio_std.plot.hist(stacked=True, bins=100)
  ```

  ![std_plot.png](Images/std_plot.png)
