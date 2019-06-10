### 10. Students Do: Probable Stock Price Forecasting (15 mins)

In this activity, students execute a Monte Carlo simulation to forecast the many different possibilities of simulated stock price trajectories, thereby analyzing the frequency/probability of potential `TSLA` stock price outcomes.

**Instructions:**

* [README.md](Activities/08-Stu_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/README.md)

**Files:**

* [probable_stock_price_forecasting.ipynb](Activities/08-Stu_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Unsolved/probable_stock_price_forecasting.ipynb)

### 11. Instructor Do: Review Probable Stock Price Forecasting (5 mins)

**Files:**

* [probable_stock_price_forecasting.ipynb](Activities/08-Stu_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Solved/probable_stock_price_forecasting.ipynb)

Open the solution and explain the following:

* Performing a Monte Carlo simulation on potential stock price outcomes involves simulating the stock price of `TSLA` over `253 * 3` trading days using a randomly selected normal distribution of daily returns and then doing the same process `n` number of times. Therefore, the code reflects another `for` loop to account for the extra iteration.

  ![nested-tsla-monte-carlo-simulation](Images/nested-tsla-monte-carlo-simulation.png)

* The plot for `1000` simulations of `TSLA` stock price trajectory over the next `252 * 3` trading days provides a visual repesentation of where `TSLA` stock price could possibly end up. Notice the volatility!

  ![tsla-multiple-stock-trajectories](Images/tsla-multiple-stock-trajectories.png)

* The last row of the DataFrame containing the `252 * 3` records of closing prices for each simulation contains the closing prices of `1000` different stock price trajectories on the last day of the project `252 * 3` trading day or `3` year trading period.

  ![tsla-last-row](Images/tsla-last-row.png)

* The frequency distribution histogram showcases the distribution of potential stock price outcomes for `TSLA` on the last day of the projected `3` year trading period. Notice that the distribution is skewed to the right and has a rather large range of values on the tail of the distribution.

  ![tsla-frequency-distribution](Images/tsla-frequency-distribution.png)

* The `value_counts` function with its `bin` parameter set to `20`, used in conjuction with the `len` function, can be used to confirm the probability distribution of particular ranges of `TSLA` stock price outcomes.

  ![tsla-value-counts-probabiliy-distribution](Images/tsla-value-counts-probabiliy-distribution.png)

* The `95%` confidence interval suggests an interval in which `95%` of stock price projections for `TSLA` are likely to lie. The lower and upper bounds suggest that there is a 95% chance that `TSLA` stock price over the next `3` trading years will fall within the range of `$6.47 - $402.74`.

  ![tsla-confidence-interval](Images/tsla-confidence-interval.png)

* Calculating the cumulative returns of the ending lower and upper bound prices for `TSLA` stock over the next `3` years and multiplying by an initial investment of `$10,000` provides a `95%` confidence interval in terms of capital investment.

  ![tsla-investment-confidence-interval](Images/tsla-investment-confidence-interval.png)