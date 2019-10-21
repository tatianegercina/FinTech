### 9. Instructor Do: Streaming Dashboard (15 min)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to showcase the need for a pipeline or buffer that manages incoming streaming data, as doing so allows for a more robust and scalable dashboard in which streaming data is handled at the visual component level rather than done via a re-draw of the entire dashboard each time.

**File:** [nano_trader_v2.py](Activities/08-Ins_Streaming_Dashboard/Solved/nano_trader_v2.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is Streamz?

  **Answer:** Streamz is a library that helps to build pipelines that manage continuous streams of data such as Pandas Dataframes containing tabular data.

* Why should you use Streamz?

  **Answer:** When creating a dashboard, oftentimes it is necessary to be able to have multiple tabs with other visualizations running in parallel; however, re-drawing a full dashboard each time (as is currently done) will "refresh" the dashboard and redirect users to the home screen (or tab) each time. Therefore, in order to have visualizations running in separate tabs in parallel, it is essential to separate the streaming data layer from the dashboard creation layer.

* In a modified version of `nanotrader.py` which includes an additional tab for the Panel dashboard, it can be seen that when attempting to navigate to the second tab in the dashboard, the user is sent back to the dashboard homepage after each refresh of the BTC/USD closing price. This is because the dashboard is re-drawn with every refresh and therefore initializes back to its starting point (the main tab) each time.

  ![dashboard-redraw](Images/dashboard-redraw.gif)

Open the solution file and review the following:

* In order to incorporate the Streamz library into our trading dashboards, we must first import the necessary libraries and dependencies.

  ```python
  from streamz import Stream
  from streamz.dataframe import DataFrame
  import hvplot.streamz
  ```

* Instead of initializing a DataFrame to later be used as a global variable for the asyncio event loop, the trading framework now initializes a Stream object that serves as an input to a Stream DataFrame object, of which the dashboard utilizes to build the plot.

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

* 

Answer any questions before moving on.
