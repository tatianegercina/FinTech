### 9. Instructor Do: Streaming Dashboard (15 min)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to showcase the need for a pipeline or buffer that manages incoming streaming data, as doing so allows for a more robust and scalable dashboard in which streaming data is handled at the visual component level rather than done via a re-draw of the entire dashboard each time.

**File:** [nanotrader_v2.py](Activities/08-Ins_Streaming_Dashboard/Solved/nanotrader_v2.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is Streamz?

  **Answer:** Streamz is a library that helps to build pipelines that manage continuous streams of data such as Pandas Dataframes containing tabular data.

* Why should you use Streamz?

  **Answer:** When creating a dashboard, oftentimes it is necessary to be able to have multiple tabs with other visualizations running in parallel; however, re-drawing a full dashboard each time (as is currently done) will "refresh" the dashboard and redirect users to the home screen (or tab) each time. Therefore, in order to have visualizations running in separate tabs in parallel, it is essential to separate the streaming data layer from the dashboard creation layer.

* In a modified version of [nanotrader.py](Activities/08-Ins_Streaming_Dashboard/Unsolved/nanotrader.py) which includes an additional tab for the Panel dashboard, it can be seen that when attempting to navigate to the second tab in the dashboard, the user is sent back to the dashboard homepage after each refresh of the BTC/USD closing price. This is because the dashboard is re-drawn with every refresh and therefore initializes back to its starting point (the main tab) each time.

  ![dashboard-redraw](Images/dashboard-redraw.gif)

Open the solution file and review the following:

* In order to incorporate the Streamz library into our trading dashboards, we must first import the necessary libraries and dependencies.

  ```python
  from streamz import Stream
  from streamz.dataframe import DataFrame
  import hvplot.streamz
  ```

* Instead of initializing a DataFrame to later be used as a global variable for the asyncio event loop, the trading framework now initializes a Stream object that manages the data pipeline, serving as an input to a Stream DataFrame object, of which the dashboard utilizes to build the plot.

  ```python
  def initialize(cash):
      """Initialize the dashboard, data storage, and account balances."""
      # Initialize Account
      account = {"balance": cash, "shares": 0}

      # Initialize Database
      db = sqlite3.connect("algo_trader_history.sqlite")

      # Initialize Streaming DataFrame for Signals
      signals_stream = Stream()
      columns = ["close", "sma10", "sma20"]
      data = {"close": [],  "sma10": [], "sma20": []}
      signals_example = pd.DataFrame(data=data, columns=columns, index=pd.DatetimeIndex([]))
      signals_stream_df = DataFrame(signals_stream, example=signals_example)

      # Initialize Streaming DataFrame for the signals
      dashboard = build_dashboard(signals_stream_df)
      return account, db, signals_stream, dashboard
  ```

* In particular, notice that the Stream DataFrame object `signals_stream_df` takes in two parameters: the Stream object as its first parameter which will contain the incoming streaming data, and two, an example Pandas DataFrame that defines the structure of the Stream DataFrame.

  ```python
  # Initialize Streaming DataFrame for Signals
      signals_stream = Stream()
      columns = ["close", "sma10", "sma20"]
      data = {"close": [],  "sma10": [], "sma20": []}
      signals_example = pd.DataFrame(data=data, columns=columns, index=pd.DatetimeIndex([]))
      signals_stream_df = DataFrame(signals_stream, example=signals_example)
  ```

* Because the trading dashboard no longer needs to re-draw itself each time, the previous `update_dashboard` function can be taken out. Instead, all that needs to be done is to initialize the dashboard once with the corresponding Stream DataFrame object updating the hvplot line chart continuously.

  ```python
  def build_dashboard(signals):
    """Build the dashboard."""
    column = pn.Column(signals.hvplot.line())
    column_test = pn.Column()

    dashboard = pn.Tabs(("Summary", column), ("Tab 2", column_test))
    return dashboard
  ```

* Lastly, when running the application, the `emit` function is used to continuously push data through the streaming data pipeline managed by the Stream object. Only a single record should be passed to the `emit` function.

  ```python
  async def main():

    while True:
        global db
        global account
        global signals_stream

        # Fetch and save new data
        new_df = await loop.run_in_executor(None, fetch_data)
        new_df.to_sql('data', db, if_exists='append', index=True)

        # Generate Signals and execute the trading strategy
        min_window = 30
        max_window = 1000
        df = pd.read_sql(f"select * from data limit {max_window}", db)
        if df.shape[0] >= min_window:
            signals = generate_signal(df)
            signals_stream.emit(signals[['close', 'sma10', 'sma20']].tail(1))
            account = execute_trade_strategy(signals, account)
            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

        # Update the Dashboard
        await asyncio.sleep(1)


  account, db, signals_stream, dashboard = initialize(100000)
  dashboard.servable()

  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

* The results of the changes show a trading dashboard that no longer requires a re-draw of its visualizations each time, but instead manages the updates to the visualizations at the data level. This allows a user to navigate to other tabs while continuously streaming data in the main tab.

  ![dashboard-streaming](Images/dashboard-streaming.gif)

Answer any questions before moving on.
