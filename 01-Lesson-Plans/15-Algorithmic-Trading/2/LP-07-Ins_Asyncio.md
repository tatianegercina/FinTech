### 7. Instructor Do: Real-Time Data with Asyncio (15 min)

In this activity, students will use a simplified version of their trading frameworks to learn how to use a real-time data load paradigm (data retrieved continuously) rather than a batch processing data load paradigm (data retrieved all at once) with the help of asyncio, a library to write concurrent or asynchronous code that mitigates the issue of *blocking code* or code that halts the further execution of a program.

The purpose of this activity is to not only demonstrate what processing real-time data looks like, but also showcase the role asyncio plays in preventing the issue of blocking code.

**File:** [nano_trader.py](Activities/05-Ins_Asyncio/Solved/nano_trader.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is batch data processing vs. real-time data processing?

  **Answer:** Batch data processing refers to the concept of processing data that represents a duration of time that has already occurred, such as historical daily closing price data. In contrast, real-time data processing refers to the concept of processing data that is continually flowing, such as a new up-to-date closing price record every second.

* What are the advantages/disadvantages of batch data processing vs. real-time data processing?

  **Answer:** Batch data processing works well for efficiently processing large volumes of data collected over a period of time, but lacks the granular control of processing data at the record-level. Real-time data processing, however, works well for processing a continual flow of data at the record-level, but is generally less efficient and adds more complexity.

* What is asyncio?

  **Answer:** Asyncio is a library to write concurrent code using the async/await syntax. Specifically, asyncio provides the concept of asynchrony, which unlike multi-threading, implements asynchronous events as independent schedules that are "out of sync" with one another while contained within a single thread.

* What is multi-threading?

  **Answer:** Multi-threading is another method of implementing concurrent code, and uses multiple threads or scheduled tasks that run in the same allocated memory context of a process.

* What is the difference between asynchrony and multi-threading?

  **Answer:** While both can achieve concurrency, asynchrony prevents much of the downsides associated with multi-threading such as memory safety and race conditions by providing control over when a program shifts from one task to the next. In addition, asychrony tends to use less memory as operations are kept on a single thread.

Open the solution file and review the following:

* This program is an over-simplified version of students' trading frameworks to more easily focus on the implementation changes required to use a real-time data load paradigm; this program is less than 100 lines of code.

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

  def initialize_dashboard():
      """Build the dashboard."""
      loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
      dashboard = pn.Column(loading_text)
      print("init dashboard")
      return dashboard

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

  def update_dashboard(account, data, dashboard):
      """Updates the dashboard with widgets, plots, and financial tables"""
      # Reset DataFrame index
      data.reset_index

      # Create price plot of closing, SMA10, and SMA20
      price_plot = data.hvplot.line(x='index', y=['close'], value_label='Price', width=1000, height=400, rot=90)

      # Create rows, columns, and tabs
      row_two = pn.Row(price_plot)
      column = pn.Column(row_two)
      tabs = pn.Tabs(("Summary", column))

      # Assign tab to dashboard object
      dashboard[0] = tabs
      return

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

          # Update the dashboard
          update_dashboard(account, data_df, dashboard)
          await asyncio.sleep(1)

  account, data_df, dashboard = initialize(100000)
  dashboard.servable()

  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

* The `fetch_data` function has been modified to now use the `fetch_ticker` function from the ccxt library, which grabs the latest pricing data for BTC/USD rather than data spanning a period of time, and imports the resulting data into a DataFrame that can be returned.

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

* The `initialize` function has also been slightly modified to initialize an empty DataFrame, so as to hold the contents of the continuous data flow fetched from the Kraken exchange.

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

* The `update_dashboard` function has been modified to only display the price plot of the closing price of BTC/USD for simplicity purposes.

  ```python
  def update_dashboard(account, data, dashboard):
      """Updates the dashboard with widgets, plots, and financial tables"""
      # Reset DataFrame index
      data.reset_index

      # Create price plot of closing, SMA10, and SMA20
      price_plot = data.hvplot.line(x='index', y=['close'], value_label='Price', width=1000, height=400, rot=90)

      # Create rows, columns, and tabs
      row_two = pn.Row(price_plot)
      column = pn.Column(row_two)
      tabs = pn.Tabs(("Summary", column))

      # Assign tab to dashboard object
      dashboard[0] = tabs
      return
  ```

* The newly constructed `main` function houses the workflow for processing data in real-time. By wrapping the code within a continuous while loop, the `main` function constantly fetches new pricing data for BTC/USD from the Kraken exchange, checks and appends the new record to a global DataFrame, updates the dashboard with the new data, and repeats the loop after waiting 1 second.

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

        # Update the dashboard
        update_dashboard(account, data_df, dashboard)
        await asyncio.sleep(1)

  account, data_df, dashboard = initialize(100000)
  dashboard.servable()

  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

* The 

Answer any questions before moving on.
