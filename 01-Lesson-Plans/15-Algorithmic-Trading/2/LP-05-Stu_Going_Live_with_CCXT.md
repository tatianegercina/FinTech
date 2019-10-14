### 5. Student Do: Going Live with CCXT (15 mins)

In this activity, students will now get the chance to connect their algorithmic trading applications to the Kraken cryptocurrency exchange. In particular, rather than read data locally from a CSV file, students will modify their `fetch_data` functions to connect to Kraken via the CCXT library and read historical pricing data for BTC/USD.

The purpose of this activity is to showcase the "plug-and-play" feature of a framework. In other words, as long as the work flow of the overall framework remains consistent, individual components of the framework, such as the `fetch_data` function, can be modified to fit distinct needs.

**File:**

* [ninja_trader_v2.py](Activities/04-Stu_Going_Live/Unsolved/ninja_trader_v2.py)

**Instructions:** [README.md](Activities/04-Stu_Going_Live/README.md)

---

### 6. Instructor Do: Going Live with CCXT Review (10 mins)

**File:** [ninja_trader_v2.py](Activities/04-Stu_Going_Live/Solved/ninja_trader_v2.py)

Open the solution file and review the following:

* The beauty of a robust application framework is that as long as the high-level input/output workflow of the framework remains consistent, the underlying "parts" or functions can be modified to fit multiple use cases. In this case, the `fetch_data` function will be modified to instead read live data from Kraken rather than a static local CSV file; however, the overall execution of the framework remains the same.

  ```python
  # Initialize account and dashboard objects
  account, dashboard = initialize(100000)
  dashboard.servable()

  # Fetch data and generate signals
  data_df = fetch_data()
  signals_df = generate_signal(data_df)

  # Backtest signal data, execute trade strategy, and evaluate metrics from backtested results
  tested_signals_df = execute_backtest(signals_df)
  portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(tested_signals_df)

  # Update the dashboard with all metrics
  update_dashboard(account, tested_signals_df, portfolio_evaluation_df, trade_evaluation_df)
  ```

* Specifically, notice how both versions of the `fetch_data` function obtain data in separate ways (local vs. API); however, the output of either function (a DataFrame) remains the same, thereby maintaining the overall workflow of the framework itself.

  **Note:** While out of the scope of today's lesson, rather than replace the local CSV functionality of the `fetch_data` function with the ability to read data from Kraken, the `fetch_data` function could be modified to use a parameter that flags whether or not to choose to read from a CSV or connect to Kraken, thereby creating a more robust framework.

  ```python
  def fetch_data():
    """Fetches the latest prices."""
    # Set the file path
    filepath = Path("../Resources/aapl.csv")

    # Read the CSV located at the file path into a Pandas DataFrame
    data_df = pd.read_csv(filepath)

    # Print the DataFrame
    print(data_df)

    return data_df
  ```

  ```python
  def fetch_data():
    """Fetches the latest prices."""
    # Import Kraken environment variables
    exchange = ccxt.kraken(
        {"apiKey": os.getenv("KRAKEN_PUBLIC_KEY"), "secret": os.getenv("KRAKEN_SECRET_KEY")}
    )
    # Fetch daily candlestick bar data from `BTC/USD`
    historical_prices = exchange.fetch_ohlcv('BTC/USD', '1d')

    # Import the data as a Pandas DataFrame and set the columns
    historical_prices_df = pd.DataFrame(historical_prices, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    historical_prices_df

    # Convert epoch timestamp to date using the `to_datetime` function and `unit` parameter
    historical_prices_df['date'] = pd.to_datetime(historical_prices_df['timestamp'], unit='ms')
    historical_prices_df

    return historical_prices_df
  ```

* While the execution of the trading framework continues to be successful, one might notice that the account value metrics now appear wrong. This is because the code within the `execute_backtest` function arbitrarily uses a share size of 500 rather than properly calculating the correct share size based off of an available cash balance.

  ![trading-dashboard-off-metrics](Images/trading-dashboard-off-metrics.png)

* In order to calculate the correct share size, the running cash balance should be divided by the running closing price of BTC/USD and rounded *down* to the nearest integer; however, due to the current batch processing paradigm of the framework (data retrieved and processed all at once), the best that can be done is to calculate the share size based off of the initial capital divided by the first closing price of BTC/USD. The `int` function by default converts and rounds down the float data type to the nearest integer.

  ```python
  # Set the share size
    share_size = 500
  ```

  ```python
  # Set the share size
    share_size = int(initial_capital / signals_df['close'][0])
  ```

* Close but no cigar! Modifying the share size calculation looks to have improved the account value metrics but unfortunately are still slightly off. This is noted by the fact that an initial account cash balance of $100,000 should not be able to afford a trade with an entry portfolio holding of greater than $100,000. Therefore, in order to obtain the correct share sizes, the framework will need to shift from a batch processing paradigm (data retrieved and processed all at once) to a real-time or streaming paradigm (data retrieved and processed every second) so as to access the running account cash balance and BTC/USD closing prices. 

  ![trading-dashboard-improved-metrics](Images/trading-dashboard-improved-metrics.png)
