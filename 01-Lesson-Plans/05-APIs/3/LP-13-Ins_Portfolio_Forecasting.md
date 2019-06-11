### 13. Instructor Demo: Portfolio Forecasting (0:10 mins)

In this activity, students ascend to the final step and learn to project not one, but many, future stock prices using Monte Carlo simulations to calculate the daily/cumulative returns of a multi-weighted portfolio. Then analyze and plot the frequency and probability distributions of potential ending cumulative returns to assess the investment risk of the portfolio.

**Files:**

* [probable_outcomes_of_stock_price.ipynb](Activities/07-Ins_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Solved/probable_outcomes_of_stock_price.ipynb)

Walk through the solution and highlight the following:

* Simulating a single potential price trajectory for a stock with respect to its average growth and volatility is not enough when it comes to attemping to analyze the possible ranges of where a stock price might end up. That is why multiple simulations of stock price trajectories need to be run.

  ![multiple-stock-simulation](Images/multiple-stock-simulation.PNG)

* The plot of the DataFrame containing the `1000` simulations of `252` trading day price records showcases the potential pathways that a stock price can take.

  ![multiple-stock-simulation-plot](Images/multiple-stock-simulation-plot.PNG)

* The last row of the DataFrame containing the results of each simulation represents the closing stock prices of `AAPL` on the `252nd` simulated trading day. In other words, the last row of the DataFrame represents the potential outcomes of `AAPL` stock price over the next `252` trading days.

  ![stock-price-frequency-distribution](Images/stock-price-frequency-distribution.PNG)

* Calculating a `95%` confidence interval of potential outcomes for projected `AAPL` stock prices over the next `252` trading days showcases a range in which there is a `95%` chance that `AAPL` stock price will end up within the range of `$99.12 - $357.69`

  ![stock-price-confidence-interval](Images/stock-price-confidence-interval.PNG)

* Multiplying an initial investment of `$10,000` by the percentage change in stock price for the lower and upper bounds of the `95%` confidence interval produces a confidence interval in terms of investment. 

  ![stock-price-investment-confidence-interval](Images/stock-price-investment-confidence-interval.PNG)