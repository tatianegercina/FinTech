### 10. Instructor Demo: Predicting Probable Outcomes of Stock Price Trajectory (0:10 mins)

In this activity, students go one step further to produce not just a single potential price trajectory for a stock over the next `252` trading days, but many potential price trajectories. So that it's possible to analyze the probabilitiy distribution of where a stock's price can go, and therefore an interval to which confident predictions can be made regarding future price.

**Files:**

* [probable_outcomes_of_stock_price.ipynb](Activities/07-Ins_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Solved/probable_outcomes_of_stock_price.ipynb)

Walk through the solution and highlight the following:

* Simulating a single potential price trajectory for a stock with respect to its average growth and volatility is not enough when it comes to attemping to analyze the possible ranges of where a stock price might end up. That is why multiple simulations of stock price trajectories need to be run.

  ![multiple-stock-simulation](Images/multiple-stock-simulation.PNG)

* The plot of the DataFrame containing the `1000` simulations of `252` trading day price records showcases the potential pathways that a stock price can take.

  ![multiple-stock-simulation-plot](Images/multiple-stock-simulation-plot.PNG)