### 10. Students Do: Beta Comparisons (20 mins)

**Instructions:**

* [README.md](Activities/10-Stu_Beta/README.md)

**Files:**

* [beta_comparisons.ipynb](Activities/10-Stu_Beta/Unsolved/beta_comparisons.ipynb)

### 11. Instructor Do: Beta Comparisons (5 mins)

**Files:**

* [beta_comparisons.ipynb](Activities/10-Stu_Beta/Solved/beta_comparisons.ipynb)

Open the solution and explain the following:

* Remember that combining the separate DataFrames for each social media stock and the S&P 500 into a single DataFrame makes it easier to calculate the daily returns for each stock by simply calling the `pct_change` function on the combined DataFrame.

  ![combined-dataframe](Images/combined-dataframe.png)

* The covariance quantifies the linear relationship between the each social media stock's returns and the returns of the overall market.

  ![social-media-covariance](Images/social-media-covariance.png)

* The variance quantifies the extent to which each data point tends to differ from the mean. In this case, variance describes the extent to which each daily return tends to differ from the overall average daily returns of the S&P 500.

  ![sp500-variance](Images/sp500-variance.png)

* The beta quantifies the relative volatility of each social media stock's returns to that of the overall market. For example, if the S&P 500 returns `10%` for the year, TWTR with a beta of `1.52` should expect to return approx. `15.2%` for the year.

  ![social-media-beta](Images/social-media-beta.png)

* Plotting multiple rolling beta values for each social media stock shows the progression of relative volatility to the market over time.

  ![rolling-social-media-beta](Images/rolling-social-media-beta.png)

* Based on the overall beta calculations and the plotted chart, it is evident that `SNAP` holds the lowest beta or relative volatility to the market. Interestingly enough as well, while `FB` and `TWTR` took a steep plunge in early 2019, `SNAP` rose dramatically.
