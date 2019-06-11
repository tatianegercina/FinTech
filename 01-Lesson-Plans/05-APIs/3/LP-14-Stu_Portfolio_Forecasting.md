### 14. Students Do: Financial Forecasting Part III (15 mins)

In this activity, students execute a Monte Carlo simulation to forecast the potential ranges of cumulative returns for a portfolio, based on the simulated closing prices of the stocks that comprise it, to determine the investment risk of the portfolio.

**Instructions:**

* [README.md](Activities/10-Stu_Portfolio_Forecasting/README.md)

**Files:**

* [financial_forcasting_part_3.ipynb](Activities/10-Stu_Portfolio_Forecasting/Unsolved/financial_forcasting_part_3.ipynb)

### 15. Instructor Do: Review Financial Forecasting Part III (5 mins)

**Files:**

* [financial_forcasting_part_3.ipynb](Activities/10-Stu_Portfolio_Forecasting/Solved/financial_forcasting_part_3.ipynb)

Open the solution and explain the following:

  * This following Monte Carlo simulation is a culmination of all of the previous activities regarding financial forecasting: simulating a single instance of a stock price trajectory; simulating multiple stock price trajectories to determine probable outcomes of future stock price; and simulating calculated cumulative portfolio returns to analyze the probability of potential future performance assess investment risk.

    ```python
    # Set number of simulations and trading days
    num_simulations = 1000
    num_trading_days = 252 * 3

    # Set last closing prices of `TSLA` and `SPHD`
    tsla_last_price = df['TSLA']['close'][-1]
    sphd_last_price = df['SPHD']['close'][-1]

    # Initialize empty DataFrame to hold simulated prices for each simulation
    simulated_price_df = pd.DataFrame()
    portfolio_cumulative_returns = pd.DataFrame()

    # Run the simulation of projecting stock prices for the next trading year, `1000` times
    for n in range(num_simulations):

        # Initialize the simulated prices list with the last closing price of `TSLA` and `SPHD`
        simulated_tsla_prices = [tsla_last_price]
        simulated_sphd_prices = [sphd_last_price]
    
        # Simulate the returns for 252 * 3 days
        for i in range(num_trading_days):
        
            # Calculate the simulated price using the last price within the list
            simulated_tsla_price = simulated_tsla_prices[-1] * (1 + np.random.normal(avg_daily_return_tsla, std_dev_daily_return_tsla))
            simulated_sphd_price = simulated_sphd_prices[-1] * (1 + np.random.normal(avg_daily_return_sphd, std_dev_daily_return_sphd))
        
            # Append the simulated price to the list
            simulated_tsla_prices.append(simulated_tsla_price)
            simulated_sphd_prices.append(simulated_sphd_price)
    
        # Append a simulated prices of each simulation to DataFrame
        simulated_price_df["TSLA prices"] = pd.Series(simulated_tsla_prices)
        simulated_price_df["SPHD prices"] = pd.Series(simulated_sphd_prices)
    
        # Calculate the daily returns of simulated prices
        simulated_daily_returns = simulated_price_df.pct_change()
    
        # Set the portfolio weights (75% TSLA; 25% SPHD)
        weights = [0.25, 0.75]

        # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
        portfolio_daily_returns = simulated_daily_returns.dot(weights)
    
        # Calculate the normalized, cumulative return series
        portfolio_cumulative_returns[n] = (1 + portfolio_daily_returns.fillna(0)).cumprod()

    # Print records from the DataFrame
    portfolio_cumulative_returns.head()
    ```

    ![portfolio-monte-carlo-simulation-results](Images/portfolio-monte-carlo-simulation-results.png)

  * The plot shows the different potential performances of the `25-75` weighed portfolio of `TSLA` and `SPHD` over the next `3` trading years.

    ![portfolio-monte-carlo-simulation-plot](Images/portfolio-monte-carlo-simulation-plot.png)

  * The last row of the DataFrame containing the cumulative portfolio returns of each simulation represents the ending cumulative returns of the portfolio of each simulation. Plotting a frequency distribution and calculating a probability distribution shows the most expected range of cumulative returns for the portfolio.

    ![portfolio-frequency-distribution](Images/portfolio-frequency-distribution.png) 

  * Calculating a `95%` confidence interval of potential cumulative portfolio returns as well as potential investment performance showcases the range of cumulative portfolio returns and investment results that have a `95%` likelihood of occurring.

    ![portfolio-confidence-interval](Images/portfolio-confidence-interval.png)