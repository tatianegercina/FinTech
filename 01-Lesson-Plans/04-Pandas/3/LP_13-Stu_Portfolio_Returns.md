### 10. Students Do: Portfolio Allocations (20 mins)

**Instructions:**

* [README.md](Activities/13-Stu_Portfolio_Returns/README.md)

**Files:**

* [beta_comparisons.ipynb](Activities/13-Stu_Portfolio_Returns/Unsolved/portfolio_allocations.ipynb)

### 11. Instructor Do: Review Portfolio Allocations (5 mins)

**Files:**

* [portfolio_allocations.ipynb](Activities/13-Stu_Portfolio_Returns/Solved/portfolio_allocations.ipynb)

Open the solution and explain the following:

* Make sure to sort the DataFrame by index in ascending order when dealing with datetime indexes so as to start from the past to the present. This is particularly important when employing time-series functions such as `pct_change`.

  ![combined-dataframe](Images/combined-dataframe.png)

* Annualized volatility is calculated by taking multiplying standard deviation by the square root of the number of trading days in a year (252 days). Using the `sort_values` function quickly sorts each stock from least volatile to most volatile.