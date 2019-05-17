### 2. Instructor Do: Really Important Demo (10 mins) (Critical)

**Files:**

* [portfolio_returns.py](Activities/01-Ins_Portfolio_Returns/Solved/portfolio_returns.py)

Explain that portfolios of stocks are used by investors to manage and diversify risk. They can choose a portfolio of different percentages of stocks to control and adjust their risk.

Walk through the solution and highlight the following:

* To calculate portfolio returns, each stock's closing prices are added as a column to the final portfolio DataFrame.

  ![portfolio-dataframe.png](Images/portfolio-dataframe.png)

* Portfolio Daily Returns are first calculated individually with `pct_change`, but the total portfolio return is calculated using the weighted average (how much of each stock contributes to the total portfolio).

  ![portfolio-returns.png](Images/portfolio-returns.png)

* The portfolio returns can also be calculated using a dot product which is just a shortcut for the previous calculation. This can be handy for large portfolios with a lot of weights.

  ![dot-product.png](Images/dot-product.png)

* The purpose of a portfolio is to control the amount of risk and diversity in an investment. In the following example, AMD has more volatility than MU, so changing the weights of the portfolios (how much of each stock in invested in) may affect the returns.

  ![risk-management.png](Images/risk-management.png)
