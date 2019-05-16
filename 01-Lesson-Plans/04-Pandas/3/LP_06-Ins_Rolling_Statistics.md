### 6. Instructor Do: Rolling Statistics (10 mins)

**Files:**

* [rolling_statistics.ipynb](Activities/06-Ins_Rolling_Statistics/Solved/rolling_statistics.ipynb)

Walk through the solution and explain the following:

* To calculate portfolio returns, each stock's closing prices are added as a column to the final portfolio DataFrame.

  ![portfolio-dataframe.png](Images/portfolio-dataframe.png)

* Portfolio Daily Returns are first calculated individually with `pct_change`, but the total portfolio return is calculated using the weighted average (how much of each stock contributes to the total portfolio).

  ![portfolio-returns.png](Images/portfolio-returns.png)

* The portfolio returns can also be calculated using a dot product which is just a shortcut for the previous calculation. This can be handy for large portfolios with a lot of weights.

  ![dot-product.png](Images/dot-product.png)

* The purpose of a portfolio is to control the amount of risk and diversity in an investment. In the following example, AMD has more volatility than MU, so changing the weights of the portfolios (how much of each stock in invested in) may affect the returns.

  ![risk-management.png](Images/risk-management.png)
