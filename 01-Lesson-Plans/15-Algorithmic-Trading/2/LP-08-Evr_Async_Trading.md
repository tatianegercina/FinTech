### 8. Everyone Do: Async Trading (15 mins)

In this activity, now that students understand how to transition their trading frameworks from performing batch processing data loads to real-time data loads with the help of asyncio, instructors will now guide students on how to execute trades based on the continual flow of data.

The purpose of this activity is to build upon the instructions from the previous activity to not only implement real-time data loads with the help of asyncio, but also to implement the trading logic required to make a decision to either buy, sell, or hold.

**Files:** [ninja_trader_v3.py](Activities/06-Evr_Async_Trading/Solved/ninja_trader_v3.py)

Open the solution file and walk through the following with the class:

* In much of the same fashion of the previous activity, in order to transition students' trading frameworks to use real-time data (make an API call every second), the following functions need to be modified or added.

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

* Notice, however, that the following snippet takes into account the fact that in order to generate a signal based on a short and long window dual moving average crossover strategy, there must be a sufficient amount of data that is at least equal to or greater than the number defined by the short window.

  ```python
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
  ```

* Furthermore, because students' trading frameworks are now using real-time data, data can now be evaluated at a more granular level such that students can now make decisions based at the record level.

  ```python
  account = execute_trade_strategy(tested_signals, account)
  ```

* In the new `execute_trade_strategy` function, the algorithmic trading framework makes a decision to either buy, sell, or hold based on the latest entry/exit values of the backtested signal results. In the case of either a buy or a sell, the account dictionary is updated to reflect the change in cash balance and active share count; however, this code could be modified to place real buy or sell orders via the Kraken exchange.

  ```python
  def execute_trade_strategy(signals, account):
    """Makes a buy/sell/hold decision."""

    if signals["entry/exit"][-1] == 1.0:
        print("buy")
        number_to_buy = round(account['balance'] / signals['close'][-1], 0) * .001
        account["balance"] -= (number_to_buy * signals['close'][-1])
        account["shares"] += number_to_buy
    elif signals["entry/exit"][-1] == -1.0:
        print("sell")
        account["balance"] += signals['close'][-1] * account['shares']
        account["shares"] = 0
    else:
        print("hold")

    return account
  ```

*

  ![async-trading-dashboard](Images/async-trading-dashboard.gif)


Ask if there are any questions before moving on.
