### 9. Students Do: Stock Price Forecasting (15 mins)

In this activity, students execute a Monte Carlo simulation to forecast stock price by multiplying each preceding day by a randomly generated daily return of normal probability distribution, approximated by a mean and standard deviation of historical `TSLA` daily returns. 

**Instructions:**

* [README.md](Activities/06-Stu_Simulation_of_Stock_Price_Trajectory/README.md)

**Files:**

* [stock_price_forecasting.ipynb](Activities/06-Stu_Simulation_of_Stock_Price_Trajectory/Unsolved/stock_price_forecasting.ipynb)

### 10. Instructor Do: Review Stock Price Forecasting (5 mins)

**Files:**

* [stock_price_forecasting.ipynb](Activities/04-Stu_Simulation_of_Stock_Price_Trajectory/Solved/stock_price_forecasting.ipynb)

Open the solution and explain the following:

* Make sure that the `IEX_TOKEN` environment variable is properly set so that the `iexfinance` SDK can communicate to the `IEX Cloud` API. Navigate [here](https://addisonlynch.github.io/iexfinance/stable/configuration.html) for more details on how to do so.

  ![missing-api-key](Images/missing-api-key.PNG)

* The `get_historical_data` function in conjuntion with the `datetime` library pulls stock data from the `IEX Cloud` API using a dynamic datetime range. Specifically, `start_date` and `end_date` variables are not hard-coded.

  ![datetime-range](Images/datetime-range.PNG)

* Applying a Monte Carlo simulation to forecasting the future daily closing prices of `TSLA` stock involves multiplying the closing price of each preceding trading day by a randomly generated daily return approximated by a normal probability distribution given the historical average and standard deviation of `TSLA` daily returns.

* In other words, each `TSLA` closing price of the preceding trading day is multiplied by a randomly chosen daily return where values closer to the expected daily return have a higher probability of occurring while values farther away from the expected daily return have a lesser probability of occurring.

  ![tsla-normal-distribution](Images/tsla-normal-distribution.PNG)

* Simulations for the next `252` trading shows that `TSLA` stock is forecasted to continue to decline, with a `$10,000` investment facing brutal negative cumulative returns if invested in `TSLA` over the next 3 years. 

  ![tsla-simulated-price-plot](Images/tsla-simulated-price-plot.PNG)

  ![tsla-cumulative-pnl](Images/tsla-cumulative-pnl.PNG)

* It should be stated that although the forecast for the next `3` years of `TSLA` stock prices show considerable declines, it does not mean that it is guaranteed; A forecast/prediction can only be as good as the foundation of information from which it was made. Therefore, creating forecasts from too little data can also be a factor.