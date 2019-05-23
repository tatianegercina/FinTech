### 10. Students Do: Portfolio Planner Part I (20 mins)

In this activity, students will work in pairs to research a group of 10 stocks, find the least to most volatile stocks, drop the top 5 highly volatile stocks, set portfolio weights to the remaining stocks according to risk profile, and perform an analysis of a `$10,000` investment in the portfolio over time. 

**Instructions:**

* [README.md](Activities/13-Stu_Portfolio_Planner_Part_I/README.md)

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/13-Stu_Portfolio_Planner_Part_I/Unsolved/portfolio_planner_part_1.ipynb)

### 11. Instructor Do: Portfolio Planner Part I (5 mins)

**Files:**

* [portfolio_planner_part_1.ipynb](Activities/13-Stu_Portfolio_Planner_Part_I/Solved/portfolio_planner_part_1.ipynb)

Open the solution and explain the following:

* Make sure to sort the DataFrame by index in ascending order when dealing with datetime indexes so as to start from the past to the present. This is particularly important when employing time-series functions such as `pct_change`.

  ![portfolio-allocations-combine-sort-df](Images/portfolio-allocations-combine-sort-df.png)

* Annualized volatility is calculated by multiplying standard deviation by the square root of the number of trading days in a year (252 days). Using the `sort_values` function quickly sorts each stock from least volatile to most volatile.

  ![assess-riskiness](Images/assess-riskiness.png)

* Portfolio weights represent the percentage of allocated capital to each stock. For example, a weight of `0.5` indicates that a single stock will be allocated `50%` of the capital within the portfolio. The sum of the weights should always equal `1`.

* The `dot` function multiples the weights by the daily return of each columns (4 weights, 4 stocks) and sums the total for each row.

  ![portfolio-allocations-weights](Images/portfolio-allocations-weights.png)

* Cumulative returns indicates the total return profit or loss from a percentage standpoint. Multiplying an initial investment of `$10,000` by the series of cumulative returns outputs a trend over time of cumulative profit or loss.

  ![portfolio-allocations-cumulative-returns](Images/portfolio-allocations-cumulative-returns.png)

  ![plot-cumulative-profit-loss](Images/plot-cumulative-profit-loss.png)