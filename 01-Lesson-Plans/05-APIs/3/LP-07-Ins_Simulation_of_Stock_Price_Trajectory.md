### 7. Instructor Demo: Simulation of Stock Price Trajectory (0:10 mins)

This activity exemplifies the use case where a Monte Carlo simulation can be applied to a historical dataset such as daily closing stock prices, given the assumption that daily closing stock prices have a normal probability distribution. Stock datasets will be pulled in from the IEX API and used to generate a Monte Carlo simulation based off of a normally distributed random process using the dataset's calculated average and standard deviation of daily returns.

**Files:**

* [stock_price_simulation.ipynb](Activities/05-Ins_Simulation_of_Stock_Price_Trajectory/Solved/stock_price_simulation.ipynb)

Walk through the solution and highlight the following:

* Monte Carlo simulations can be executed not just on random processes with *discrete probabilities* (ex. `70%` to make a free throw and `30%` to miss a free throw), but also on *continuous probabilities* such as normal probability distributions.

* Normal probability distributions showcase the various probabilities of returning a value based on the number of standard deviations it is from the mean (how far the value may lie plus or minus from the average expected value); values far away from the mean are less common while values near the mean are more common. Monte carlo simulation use this characteristic to simulate a random process' potential outcomes with respect to the variability around its mean.

  ![example-normal-distribution](Images/example-normal-distribution.png)

* The daily closing stock price data will be pulled using the `iexfinance` SDK that connects to the `iex` API. Therefore, make sure to import the necessary libraries and dependencies before proceeeding.

  ```python
  # Import libraries and dependencies
  import numpy as np
  import pandas as pd
  from datetime import datetime, timedelta
  from iexfinance.stocks import get_historical_data
  import iexfinance as iex
  import matplotlib.pyplot as plt
  %matplotlib inline
  ```

* Use the `get_symbols` function from the `refdata` class of the `iex` SDK to check the available stock ticker data that can be pulled from the `iex` API.

  ![iex-check-tickers](Images/iex-check-tickers.png)

* The `get_historical_data` function from the `iexfinance` SDK takes in a `ticker`, `start_date`, and `end_date` parameter with an `output_format` option set to `pandas` to return a DataFrame of `AAPL` daily stock prices. The `start_date` and `end_date` variables in this case are set to `365` days from the current date and the current date, respectively.

  ![iex-get-data](Images/iex-get-data.png)

* The Monte carlo simulation of stock price trajectory involves closing prices of `AAPL`. Therefore, it's best to drop the extraneous columns.

  ![dataframe-drop-columns](Images/dataframe-drop-columns.png)

* In order to simulate `AAPL` stock prices for the next `252` trading days, it is important that the simulation is framed in the context of a stock's *growth*. Therefore, the `pct_change` function is used to calculate the last year of daily returns for `AAPL`, and the `mean` and `std` functions are used to calculate the average daily return and the volatility of daily returns.

  ![aapl-daily-returns](Images/aapl-daily-returns.png)

  ![aapl-daily-return-mean-and-std](Images/aapl-daily-return-mean-and-std.png)