### 13. Instructor Demo: Portfolio Forecasting (0:10 mins)

In this activity, students ascend to the final step and learn to project not one, but many, future stock prices using Monte Carlo simulations to calculate the daily/cumulative returns of a multi-weighted portfolio. Then analyze and plot the frequency and probability distributions of potential ending cumulative returns to assess the investment risk of the portfolio.

**Files:**

* [portfolio_forecasting.ipynb](Activities/09-Ins_Portfolio_Forecasting/Solved/portfolio_forecasting.ipynb)

Walk through the solution and highlight the following:

* The `get_historical_data` function of the `iexfinance` SDK can provide stock price data for more than one ticker in a single API call. Supplying a list of tickers with the `output_format` parameter set to `pandas` returns a multi-level index DataFrame.

  ![iex-multi-level-index](Images/iex-multi-level-index.png)

* To drop specific columns of a multi-level index DataFrame, use the `drop` function with the `level` parameter to specify the *level* of the DataFrame.

  ![drop-multi-level-index-columns](Images/drop-multi-level-index-columns.png)

* Access the Series of values of each multi-level index column using additional square bracket key notation to represent the additional levels.

  ![multi-level-index-key-notation](Images/multi-level-index-key-notation.png)

* The Monte Carlo simulation projects the stock price trajectory for `JNJ` and `MU` over the course of `252` trading days and returns a DataFrame of `252` records representing each simulated day's closing price. Simulated stock prices are projected by randomly selecting a daily return based off of a normal probability distribution, derived from sample means and standard deviations, and multiplying `1 + np.random.normal(avg_daily_return, std_dev_daily_return)` by the preceding day's closing price. A DataFrame of `252` simulated trading days is returned and the daily returns are calculated using the `pct_change` function.  

  ```python
  # Set number of simulations and trading days
  num_simulations = 1000
  num_trading_days = 252

  # Set last closing prices of `JNJ` and `MU`
  jnj_last_price = df['JNJ']['close'][-1]
  mu_last_price = df['MU']['close'][-1]

  # Initialize empty DataFrame to hold simulated prices for each simulation
  simulated_price_df = pd.DataFrame()
  portfolio_cumulative_returns = pd.DataFrame()

  # Run the simulation of projecting stock prices for the next trading year, `1000` times
  for n in range(num_simulations):

      # Initialize the simulated prices list with the last closing price of `JNJ` and `MU`
      simulated_jnj_prices = [jnj_last_price]
      simulated_mu_prices = [mu_last_price]
    
      # Simulate the returns for 252 days
      for i in range(num_trading_days):
        
          # Calculate the simulated price using the last price within the list
          simulated_jnj_price = simulated_jnj_prices[-1] * (1 + np.random.normal(avg_daily_return_jnj, std_dev_daily_return_jnj))
          simulated_mu_price = simulated_mu_prices[-1] * (1 + np.random.normal(avg_daily_return_mu, std_dev_daily_return_mu))
        
          # Append the simulated price to the list
          simulated_jnj_prices.append(simulated_jnj_price)
          simulated_mu_prices.append(simulated_mu_price)
    
      # Append a simulated prices of each simulation to DataFrame
      simulated_price_df["JNJ prices"] = pd.Series(simulated_jnj_prices)
      simulated_price_df["MU prices"] = pd.Series(simulated_mu_prices)
    
      # Calculate the daily returns of simulated prices
      simulated_daily_returns = simulated_price_df.pct_change()
  ```

* The portfolio weights are multiplied against the values of each column and totaled for each index of the DataFrame. For example, a `0.01` or `1%` daily return in `JNJ` and a `0.005` or `0.5%` daily return in `MU` on the `1st` simulated trading day would constitute a portfolio return of `(0.6 * 0.01) + (0.4 * 0.005) = 0.008` or `0.8%` daily return for that day.

  ```python
      # Set the portfolio weights (60% JNJ; 40% MU)
      weights = [0.60, 0.40]

      # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
      portfolio_daily_returns = simulated_daily_returns.dot(weights)
  ```

* After portfolio daily returns are calculated, cumulative returns are then determined by using the `cumprod` function; the `fillna` function applies a specified number to any instances of `NaN` values within the DataFrame. Cumulative portfolio returns are then added to each column of a DataFrame to represent the simulated cumulative portfolio returns for each simulation.

  ```python
      # Calculate the normalized, cumulative return series
      portfolio_cumulative_returns[n] = (1 + portfolio_daily_returns.fillna(0)).cumprod()

  # Print records from the DataFrame
  portfolio_cumulative_returns.head()
  ```

  ![monte-carlo-results](Images/monte-carlo-results.png)