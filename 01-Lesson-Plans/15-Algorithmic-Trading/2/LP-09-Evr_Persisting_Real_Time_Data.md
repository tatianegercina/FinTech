### 7. Everyone Do: Persisting Real-Time Data (15 mins)

In this activity, students will learn how to persist their real-time data to a sqlite database.

The purpose of this activity is to showcase the value in persisting data as doing so allows an application to pick up where it left off should a failure occur.

**Files:** [ninja_trader_v3.py](Activities/05-Evr_Persisting_Real_Time_Data/Solved/ninja_trader_v3.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is data persistence?

  **Answer:** Data persistence is the concept of saving data to a database so as to have a reliable copy of data that is *persisted* rather than transiently stored as in-memory data structures.

* Why is it important to persist data?

  **Answer:** Persisting data is generally a best practice as it provides a method for data recovery should an application ever fail; data stored in transient in-memory data structures will be lost forever if the application itself terminates. In addition, persisting data to a database allows for separate data analysis to be done at a later time, if desired.

Open the solution file and walk through the following with the class:

* First things first, the sqlite3 library will need to be imported into students' trading applications before moving on.

  ```python
  import sqlite3
  ```

* Because data will now be persisted to a sqlite database, there is no need for a global DataFrame to hold transient data in-memory. Therefore, the `initialize` function can be modified to remove the declaration of the empty DataFrame and instead create a connection to a sqlite database using the `connect` function of the sqlite3 library.

  ```python
  def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize Database
    db = sqlite3.connect("ninja_trader_db.sqlite")

    # Initialize Streaming DataFrame for the signals
    dashboard = initialize_dashboard()
    return account, db, dashboard
  ```

* In addition, now that there is no longer a need for a global DataFrame to hold fetched data from Kraken, the previous conditional statements within the `main` function can be deprecated with the following one-liner, in which each new record DataFrame is exported to the sqlite database using the `to_sql` Pandas DataFrame function.

  ```python
  # Save latest pricing data to a global DataFrame
  if data_df.empty:
      data_df = new_record_df.copy()
  else:
      data_df = data_df.append(new_record_df, ignore_index=False)
  ```

  ```python
  # Save latest pricing data to a global DataFrame
  if data_df.empty:
      data_df = new_record_df.copy()
  else:
      data_df = data_df.append(new_record_df, ignore_index=False)
  ```

* Putting everything together, 

  ```python
  async def main():

    while True:
        global account
        global db
        global dashboard

        # Fetch latest pricing data
        new_record_df = fetch_data()

        # Save latest pricing data to a global DataFrame
        new_record_df.to_sql('data', db, if_exists='append', index=True)

        # Generate Signals and execute the trading strategy
        min_window = 10
        max_window = 1000
        data_df = pd.read_sql(f"select * from data limit {max_window}", db)
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
  account, db, dashboard = initialize(100000)
  dashboard.servable()

  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

Ask if there are any questions before moving on.
