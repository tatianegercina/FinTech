### 8. Everyone Do: Async Trading (15 mins)

In this activity, now that students understand how to transition their trading frameworks from performing batch processing data loads to real-time data loads with the help of asyncio, instructors will now guide students on how to execute trades based on the continual flow of data.

The purpose of this activity is to build upon the instructions from the previous activity to not only implement real-time data loads with the help of asyncio, but also to implement the trading logic required to make a decision to either buy, sell, or hold.

**Files:** [ninja_trader_v3.py](Activities/06-Evr_Async_Trading/Solved/ninja_trader_v3.py)

Open the solution file and walk through the following with the class:

* In much of the same fashion of the previous activity, in order to transition students' trading frameworks to use real-time data, the following functions need to be modified or added.

  ```python
  def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize DataFrame
    data_df = pd.DataFrame()

    # Initialize Streaming DataFrame for the signals
    dashboard = initialize_dashboard()
    return account, data_df, dashboard
  ```

  ```python
  def fetch_data():
    """Fetches the latest prices."""
    kraken = ccxt.kraken(
        {"apiKey": os.getenv("kraken_key"), "secret": os.getenv("kraken_secret")}
    )
    close = kraken.fetch_ticker("BTC/USD")['close']
    datetime = kraken.fetch_ticker("BTC/USD")['datetime']
    df = pd.DataFrame({'close': [close], 'date': [datetime]})
    df.index = pd.to_datetime([datetime])
    return df
  ```

  ```python
  async def main():

    while True:
        global account
        global data_df
        global dashboard

        # Fetch latest pricing data
        new_record_df = fetch_data()

        # Save latest pricing data to a global DataFrame
        if data_df.empty:
            data_df = new_record_df.copy()
        else:
            data_df = data_df.append(new_record_df, ignore_index=False)

        # Generate Signals and execute the trading strategy
        min_window = 10
        max_window = 1000
        if data_df.shape[0] >= min_window:
            signals = generate_signal(data_df)
            tested_signals = execute_backtest(signals)

            account = execute_trade_strategy(tested_signals, account)
            portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(tested_signals)

            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

            # Update the dashboard
            update_dashboard(account, signals, portfolio_evaluation_df, trade_evaluation_df, dashboard)

        await asyncio.sleep(1)


  # Initialize account and dashboard objects
  account, data_df, dashboard = initialize(100000)
  dashboard.servable()

  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

Ask if there are any questions before moving on.
