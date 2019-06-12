### 10. Instructor Demo: Predicting Probable Outcomes of Stock Price Trajectory (0:10 mins)

In this activity, students go one step further to produce not just a single potential price trajectory for a stock over the next `252` trading days, but many potential price trajectories. So that it's possible to analyze the probabilitiy distribution of where a stock's price can go, and therefore an interval to which confident predictions can be made regarding future stock price.

**Files:**

* [probable_outcomes_of_stock_price.ipynb](Activities/07-Ins_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Solved/probable_outcomes_of_stock_price.ipynb)

Walk through the solution and highlight the following:

* Simulating a single price trajectory for a stock, with respect to its average daily return and volatility, is but one pathway of which the stock price could move over time. Therefore, in order to analyze the possible ranges of where a stock price might end up, multiple simulations of stock price trajectories need to be run.

  ![multiple-stock-simulation](Images/multiple-stock-simulation.PNG)

* The following code snippet contains the core of the Monte Carlo simulation and the process of stock price forecasting. For every simulation, the program runs `252` iterations of stock price growth by multiplying each preceding trading day's closing price by a randomly selected daily return based off of a normal probability distribution of `AAPL` daily returns, derived from it's average daily return value (mean) and its volatility (standard deviation). The results of each simulation are then added as a column to a DataFrame.

  ```python
  # Run the simulation of projecting stock prices for the next trading year, `1000` times
  for n in range(num_simulations):

      # Initialize the simulated prices list with the last closing price of AAPL
      simulated_aapl_prices = [aapl_last_price]
    
      # Simulate the returns for 252 days
      for i in range(num_trading_days):
          # Calculate the simulated price using the last price within the list
          simulated_price = simulated_aapl_prices[-1] * (1 + np.random.normal(avg_daily_return, std_dev_daily_return))
          # Append the simulated price to the list
          simulated_aapl_prices.append(simulated_price)
    
      # Append a simulated prices of each simulation to DataFrame
      simulated_price_df[f"Simulation {n+1}"] = pd.Series(simulated_aapl_prices)

  # Print head of DataFrame
  simulated_price_df.head()
  ```

* The plot of the DataFrame containing the `1000` simulations of `252` trading day price records showcases the potential pathways that a stock price can take.

  ![multiple-stock-simulation-plot](Images/multiple-stock-simulation-plot.PNG)

* The last row of the DataFrame containing the results of each simulation represents the closing stock prices of `AAPL` on the `252nd` simulated trading day. In other words, the last row of the DataFrame represents the potential outcomes of `AAPL` stock price over the next `252` trading days.

  ![stock-price-frequency-distribution](Images/stock-price-frequency-distribution.PNG)

* Calculating a `95%` confidence interval of potential outcomes for projected `AAPL` stock prices over the next `252` trading days showcases a range in which there is a `95%` chance that `AAPL` stock price will end up within the range of `$99.12 - $357.69`

  ![stock-price-confidence-interval](Images/stock-price-confidence-interval.PNG)

* Multiplying an initial investment of `$10,000` by the percentage change in stock price for the lower and upper bounds of the `95%` confidence interval produces a confidence interval in terms of investment. 

  ![stock-price-investment-confidence-interval](Images/stock-price-investment-confidence-interval.PNG)