# To be added back to the 15.2 LP

### 8. Everyone Do: Async Trading (15 min)

In this activity, students will code along with the instructor to update their live trading code to fetch data asynchronously with [asyncio](https://docs.python.org/3/library/asyncio.html).

**Files:** [jarvis.py](Activities/06-Evr_Async_Trading/Unsolved/jarvis.py)

Open the starter code and live code the solution with the class. Explain any new concepts as you go, and be sure to proceed slowly and frequently pause to make sure that students can keep up.

Start by skimming the code with the class and showing the `# @TODO:` comments where the code will need to be updated. Explain that the goal is to use asyncio so that the dashboard can be loaded and updated without blocking the page from loading.

Import the necessary libraries to use asyncio, hvplot, and panel.

```python
import asyncio

import hvplot.pandas
import panel as pn

pn.extension()
```

Update the code for the `initialize`, `build_dashboard`, and `update_dashboard` functions and highlight the following:

```python
# Initialize the dashboard
    dashboard = build_dashboard()

    # @TODO: We will complete the rest of this later!
    return account, df, dashboard


def build_dashboard():
    """Build the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")
    return dashboard
```

* The `initialize` function uses the `build_dashboard` function to build and return a simple dashboard that initially contains static text.

* The `update_dashboard` function is used to update the Panel dashboard with a line chart. It uses new data that is available after fetching from the CCXT API.

* Because the dashboard is just a container for plots, the dashboard contents can be replaced with new plots using `dashboard[0] = dv.hvplot()`.

Complete the main function and explain the following to the class:

```python
account, df, dashboard = initialize(10000)
dashboard.servable()


async def main():
    loop = asyncio.get_event_loop()

    while True:
        global account
        global df
        global dashboard

        new_df = await loop.run_in_executor(None, fetch_data)
        df = df.append(new_df, ignore_index=True)

        min_window = 22
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            account = execute_trade_strategy(signals, account)

        update_dashboard(df, dashboard)

        await asyncio.sleep(1)


# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

* The dashboard is initialized as Static text and then served immediately. Afterward, we can use an asynchronous main function to fetch new data and update the dashboard without blocking the page from loading.

  ```python
  account, df, dashboard = initialize(10000)
  dashboard.servable()
  ```

* In this example, we choose to make the main function async so that it does not block the dashboard from loading. The code awaits both the `fetch_data` function and the `asyncio.sleep` function.

  * **Note:** The `requests` library that is used in the `fetch_data` function is considered a blocking library. Blocking libraries like this must be called using a special function called `run_in_executor`. More information about this can be found in the official [asyncio documents](https://docs.python.org/3/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools), but this code can be used anytime that the requests library is used. Alternatively, there is an asyncio-compatible library called [aiohttp-requests](https://pypi.org/project/aiohttp-requests/) that can be used instead.

* Once the new data is fetched, the `update_dashboard` function is called to update the plots. This function replaces the dashboard plots for now, but this will be improved later in class.

* Finally, the main function is executed with a special asyncio function called `run_until_complete`. This is just one way to run the asynchronous code in the event loop.

  ```python
  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

Wrap up this activity by acknowledging that asynchronous code is very challenging to write. However, the code provided in this example can be used as a template that can be reused for many different algorithmic trading applications.

---

### 9. Everyone Do: Persisting Real-Time Data (15 min)

In this activity, students will learn how to persist their real-time data to a database. Students will code along with the instructor to update the trading framework to persist data with a SQLite database.

The purpose of this activity is to showcase the value in persisting data as doing so allows an application to pick up where it left off should a failure occur.

**File:**
* [jarvis.py](Activities/07-Evr_Persisting_Real_Time_Data/Unsolved/jarvis.py)

Explain to the class that the next enhancement to make to the trading algorithm is to persist the live data to a database. Persisting the live data allows the framework to recover from data errors, and it allows us to collect and use historical data without running into memory issues.

Quickly discuss the following before proceeding onward to the walkthrough:

* What is data persistence?

  **Answer:** Data persistence is the concept of saving data to a database to have a reliable copy of data that is *persisted* rather than transiently stored as in-memory data structures.

* Why is it important to persist data?

  **Answer:** Persisting data is generally a best practice as it provides a method for data recovery should an application ever fail; data stored in transient in-memory data structures will be lost forever if the application itself terminates. Also, persisting data to a database allows for separate data analysis to be done at a later time, if desired.

With the class, update the starter code to use an SQLite database to persist the data. Be sure to highlight the following points about SQLite:

* `sqlite` is a database system that is provided with Python through the `sqlite3` library.

* `sqlite` is very useful for fast, lightweight database applications.

* Because it is included with Python and uses a file-based database, it is a popular choice for testing and prototyping code that requires a database.

* The same code shown today with SQLite can also be used with any database connector in Python, including `postgresql`.

Import the sqlite3 library and show how the database connector is initialized in the code:

```python
def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Initializing account, database, and DataFrame")

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")
```

* In Python, a SQLite database can be created using `sqlite3.connect` with a filename for the database. The entire database is contained locally on disk in this file.

* With the database connection `db`, a cursor can be used to execute raw SQL directly on the database. In this example, a cursor is used to drop the table called `data` if it already exists.

  ```python
  with db:
      cur = db.cursor()
      cur.execute("DROP TABLE IF EXISTS data")
  ```

Next, update the main loop to use the database connector. Explain the following points:

```python
db, account, df, dashboard = initialize(10000)
dashboard.servable()


async def main():
    loop = asyncio.get_event_loop()

    while True:
        global db
        global account
        global df
        global dashboard

        new_df = await loop.run_in_executor(None, fetch_data)
        new_df.to_sql("data", db, if_exists="append", index=True)

        # Generate Signals and execute the trading strategy
        min_window = 21
        max_window = 1000
        df = pd.read_sql(f"select * from data limit {max_window}", db)
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            account = execute_trade_strategy(signals, account)

        update_dashboard(df, dashboard)

        await asyncio.sleep(1)
```

* The database connector that is returned from the initialize function can be used with Pandas to read and write DataFrames. In this example, new data that is fetched can be written directly to the database with Pandas `to_sql`.

  ```python
  new_df.to_sql("data", db, if_exists="append", index=True)
  ```

* The database can then be ready back into the main Pandas DataFrame and used to generate signals and create visualizations.

  ```python
  max_window = 1000
  df = pd.read_sql(f"select * from data limit {max_window}", db)
  ```

Wrap up this demonstration with a quick recap of the advantage of using databases to persist the data:

* Appending live data to a Pandas DataFrame can eventually create memory issues when the amount of data collected is large enough. Offloading this data to a database can be very efficient.

* Many applications can share a common database. This allows you to create multiple trading applications that all share a common database.

* Capturing the live data makes it easier to choose how much data is selected for the trading strategy.

Ask if there are any questions before moving on.

---

### 10. BREAK (15 min)

---

### 11. Instructor Do: Streaming Data with Streamz (15 min)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to show students how to update a visualization as data continues to flow without the need for reconstructing the visual component each time.

**File:** [streamz.ipynb](Activities/08-Ins_Streaming/Solved/streamz.ipynb)

Begin this demonstration by asking the students if they noticed anything strange about the `update_dashboard` code. Point out that the dashboard is simply replaced with each new piece of data. While this approach is fine for a simple dashboard example, it can create problems for a complex dashboard.

Explain that a better approach to replacing the plots each time is to update the plots with new data. Explain that Panel, hvplot, and Plotly all provide tools to update plots in an efficient way using live data streams. In this example, we will use the `streamz` library with hvplot to update our plots to allow for live data streams.

Explain to students that hvplot uses the `Streamz` library to build a pipeline or buffer to manage continuous streams of data. A `Stream` can be thought of as a data reservoir that live data can be sent to. Hvplot can then connect to this Stream and update its plots when new data arrives.

Acknowledge that while data pipelines and buffers are very advanced subjects, the streamz library makes it very simple to create a use streamz with Pandas and hvplot.

Open the notebook and quickly show that hvplot has a special data streaming interface to the streamz library that can be imported:

```python
import os
from dotenv import load_dotenv
import ccxt
import pandas as pd
import hvplot.streamz
from streamz import Stream
from streamz.dataframe import DataFrame
```

Use the first section of the notebook to demonstrate how to create a streaming DataFrame and plot the data with streamz and hvplot. Highlight the following points:

* The streamz library provides a [DataFrame-like interface](https://streamz.readthedocs.io/en/latest/dataframes.html) that can accept Stream and an example to form a streaming DataFrame.

  ```python
  stream = Stream()
  example = pd.DataFrame({"x": [], "y": []}, columns=["x", "y"], index=[])
  sdf = DataFrame(stream, example=example)
  ```

* The `example` in the above code is just a template for what the live data will look like. In this example, the live data will have `x` and `y` columns of data.

* A streaming DataFrame has limited functions similar to a real Pandas DataFrame, but it uses a Stream to hold live streaming data. A streaming DataFrame can be considered a wrapper around a normal DataFrame that hvplot can use to update its plots with streaming data automatically. In this example, hvplot will update its scatter plot whenever it receives new live data that matches the format of the `example` DataFrame.

  ```python
  sdf.hvplot.scatter(x="x", y="y")
  ```

* Live data is added to the streaming DataFrame using `stream.emit`. In this example, a DataFrame is created 20 different times and each time emitted to the streaming DataFrame. Hvplot knows to update its scatter plot with each new data that is emitted.

  ```python
  def emit(i):
      df = pd.DataFrame({"x": [i], "y": [i]})
      stream.emit(df)

  for i in range(20):
      emit(i)
  ```

  ![streamz_demo_1.gif](Images/streamz_demo_1.gif)

Use the Rolling Window section to explain that a rolling window of data can be used with hvplot to make the plot more efficient. Highlight the following:

* You can specify the rolling window of data to plot using the `backlog` parameter. This is just how much total data the plot will remember and use at any given time.

  ```python
  sdf.hvplot.scatter(x="x", y="y", backlog=10)
  ```

* Even with 100 total emits, the backlog of 10 means that only the newest ten data points are remembered.

  ```python
  for i in range(100):
    emit(i)
  ```

  ![streamz_demo_2.gif](Images/streamz_demo_2.gif)

* Finally, show how streamz can be used with CCXT and Kraken to fetch data from an API and update a plot:

  ![streamz_demo_3.gif](Images/streamz_demo_3.gif)

* In this code, the `example` DataFrame consists of a closing price column.

  ```python
  stream = Stream()
  example = pd.DataFrame({"close": []}, columns=["close"], index=pd.DatetimeIndex([]))
  sdf = DataFrame(stream, example=example)
  ```

* New data is fetched from the Kraken exchange via the CCXT API and processed as a new DataFrame `df` that matches the format of the `example` DataFrame. This new DataFrame is then emitted to the Stream, and hvplot uses the streaming DataFrame to update the plot.

  ```python
  load_dotenv()
  kraken = ccxt.kraken(
      {"apiKey": os.getenv("kraken_key"), "secret": os.getenv("kraken_secret")}
  )

  while True:
      close = kraken.fetch_ticker("BTC/USD")['close']
      datetime = kraken.fetch_ticker("BTC/USD")['datetime']

      df = pd.DataFrame({"close": [close]})
      df.index = pd.to_datetime([datetime])
      stream.emit(df)
      time.sleep(1)
  ```

Ask any questions before moving on.

---

### 12. Everyone Do: Streaming Dashboard (20 min)

In this activity, students will code along with the instructor to update the trading framework to use streaming data visualizations.

**File:** [jarvis.py](Activities/09-Evr_Streaming_Dashboard/Unsolved/jarvis.py)

Explain to students that the previous iteration of the trading dashboard was replaced each time that new data arrived. For a single plot, this was ok, but for a complex dashboard, each replacement would reset the entire dashboard and negatively impact the user experience. Explain that we can avoid some of these issues by updating the example to use the streamz library with hvplot.

Open the starter code and highlight the sections that will be replaced or updated. Then, start by updating the imports and the initialize function:

```python
import hvplot.streamz
from streamz import Stream
from streamz.dataframe import DataFrame
import panel as pn

pn.extension()


def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize Streaming DataFrame for Raw Data
    data_stream = Stream()
    data_example = pd.DataFrame(
        data={"close": []}, columns=["close"], index=pd.DatetimeIndex([])
    )
    data_stream_df = DataFrame(data_stream, example=data_example)

    # Initialize Streaming DataFrame for Signals
    signals_stream = Stream()
    columns = ["close", "signal", "sma10", "sma20", "entry/exit"]
    data = {"close": [], "signal": [], "sma10": [], "sma20": [], "entry/exit": []}
    signals_example = pd.DataFrame(
        data=data, columns=columns, index=pd.DatetimeIndex([])
    )
    signals_stream_df = DataFrame(signals_stream, example=signals_example)

    # Initialize Streaming DataFrame for the signals
    dashboard = build_dashboard(data_stream_df, signals_stream_df)
    return db, account, data_stream, signals_stream, dashboard
```

* The initialize function creates a streaming DataFrame for both the raw data and for the generated signals. Both of these DataFrames will be used to update the final dashboard visualizations.

* The format for each `example` DataFrame can be worked out ahead of time using a normal DataFrame and Jupyter notebook with historical data.

* The trading framework will now initialize Stream objects to manage the data pipeline. These streaming data pipelines are then used to build the dashboard with streaming visualizations.

Show that the `update_dashboard` function can be removed and the `build_dashboard` code modified to use the streaming DataFrames:

```python
def build_dashboard(data, signals):
    """Build the dashboard."""

    signals_plot = (
        signals[signals["entry/exit"] == 1.0].hvplot.scatter(
            y="sma10", marker="^", size=200, c="g", label="buy", padding=0.1
        )
        * signals[signals["entry/exit"] == -1.0].hvplot.scatter(
            y="sma10", marker="v", size=200, c="r", label="sell", padding=0.1
        )
        * signals.hvplot.line(y="sma10", label="sma10")
        * signals.hvplot.line(y="sma20", label="sma20")
    )
    dashboard = pn.Column(
        "# JARVIS Algorithmic Trading Dashboard",
        data.hvplot(title="prices"),
        signals_plot.opts(title="signals plot", show_legend=False),
        "### Signals Table",
        signals.hvplot.table(
            title="signals table",
            columns=["close", "entry/exit", "sma10", "sma20"],
            backlog=10,
        ),
    )
    return dashboard
```

* The above code was adapted to use the limited streamz DataFrame interface with hvplot. Because of this, using streaming data may impact or limit the complexity of the final plots.

Show that the `generate_signals` function also needs to be modified slightly to convert the index to match the `example` DataFrame used in the initialize function.

```python
def generate_signals(df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10

    signals = df.copy()
    signals["index"] = pd.to_datetime(signals["index"])
    signals = signals.set_index("index", drop=True)
    signals["signal"] = 0.0

    # Generate the short and long moving averages
    signals["sma10"] = signals["close"].rolling(window=10).mean()
    signals["sma20"] = signals["close"].rolling(window=20).mean()

    # Generate the trading signal 0 or 1,
    signals["signal"][short_window:] = np.where(
        signals["sma10"][short_window:] > signals["sma20"][short_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"] = signals["signal"].diff()

    return signals
```

Finally, show how the main function can be updated to emit new data to the streaming DataFrames:

```python
async def main():
    loop = asyncio.get_event_loop()

    while True:
        global db
        global account
        global data_stream
        global signals_stream

        # Fetch and save new data
        new_df = await loop.run_in_executor(None, fetch_data)
        new_df.to_sql("data", db, if_exists="append", index=True)

        # Generate Signals and execute the trading strategy
        min_window = 21
        max_window = 1000
        df = pd.read_sql(f"select * from data limit {max_window}", db)
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            signals_stream.emit(signals)
            account = execute_trade_strategy(signals, account)
            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

        # Update the Dashboard
        data_stream.emit(new_df)
        await asyncio.sleep(1)
```

* The `emit` function is used to continuously inject data into the streaming data pipeline managed by the Stream object. These streaming DataFrames are connected to the dashboard visualizations and automatically update the charts when new data is emitted.

* The result of these changes is that the dashboard no longer has to replace each visualization from scratch. This allows users to scroll on the page and switch between tabs without losing their place. This would not have been possible without the streaming data visualizations that hvplot and streamz provides.

Congratulate students on completing the final dashboard! They now have a robust algorithmic trading framework that can be used to build and deploy a wide variety of trading algorithms!

---
