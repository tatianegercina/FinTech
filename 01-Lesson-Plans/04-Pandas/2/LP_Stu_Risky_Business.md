### 17. Students Do: Risky Business (20 mins)

In this activity, students will participate in a bet with Harold to identify who has made the most rewarding investments in their cryptocurrency portfolios.Students will also identify which cryptos have had the greatest return once adjustments have been made for risk.

**Files:**

* [risky_business.ipynb](Activities/17-Stu_Risky_Business/Unsolved/Core/risky_business.ipynb)

**Instructions:**

* [README.md](Activities/17-Stu_Risky_Business/README.md)

### 18. Instructor Do: Review Risky Business (5 mins)

**Files:**

* [risky_business.ipynb](Activities/17-Stu_Risky_Business/Solved/Core/risky_business.ipynb)

Walk through the solution and highlight the following:

* The `concat` function can be used to combine portfolio returns. This enables analysis (i.e. standard deviation) to be performed on an entire portfolio rather than an individual stock. This allows data from investments/portfolio `A` to be compared with investments/portfolio `B`. Harold's portfolio returns are combined with student returns in order to later calculate `standard deviation` and `sharpe ratio` for across the board.

  ```python
  # Concat returns DataFrames
  all_returns = pd.concat([harold_returns,my_returns], axis='columns', join='inner')
  all_returns.head()
  ```

  ![stu_concat_compare.png](Images/stu_concat_compare.png)

* `Standard deviation` is required to calculate `sharpe ratios`. `Standard Deviation` calculates the average value and compares the distribution of values to that average. The `std` function can be used to compute standard deviation. The output from the function is a Series that indicates how far the value is from the mean, in the same units as the base data. The greater the value/deviation, the greater the risk and volatility.

  ```python
  # Calculate std dev
  all_portfolio_std = all_returns.std()
  all_portfolio_std.head()
  ```

  ```
  BTC     0.049189
  BTT     0.006185
  DOGE    0.062264
  ETH     0.050074
  LTC     0.048783
  dtype: float64
  ```

* `Sharpe ratios` are used to examine investment performance based off of the risk to reward ratio. `Sharpe ratio` calculates the risk associated with a return and then divides that by the standard deviation of a return. The higher the `sharpe ratio`, the greater the reward associated with the risk. A high `sharpe ratio` indicates a smart investment. Calculating the `sharpe ratio` for Harold's and the students' portfolios reveals who's portfolio has the greatest reward associated with the risk.

  ```python
  # Calculate sharpe ratio
  sharpe_ratios = (all_returns.mean() * 252) / (all_portfolio_std * np.sqrt(252))
  sharpe_ratios.head()
  ```

  ```
  BTC    -0.269714
  BTT    -0.878716
  DOGE    0.105533
  ETH    -0.214963
  LTC    -0.222482
  dtype: float64
  ```

* `Sharpe ratios` can be visually represented with a bar chart. This allows users to easily see which investments have high and low sharpe ratios.

  ```python
  # Plot
  sharpe_ratios.plot.bar(title='Sharpe Ratios')
  ```

  ![sharpe_plot.png](Images/sharpe_plot.png)

* How many smart investments did Harold make compared to risky investments? How many did you make?

  ```
  Out of his 10 investments, Harold only made 4 good investments. Out of the students' 6 investments, 3 of them were smart investments.
  ```

* Which cryptos have been the smartest investment?

    ```
    DOGE, TRON, and XML have been the smartest crypto investments.
    ```
