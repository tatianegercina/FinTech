## 15.2 Lesson Plan: Egad! It's Alive!

---

### Overview

Today's class will expand upon students' component knowledge of algorithmic trading and abstract one level higher to create a full-fledged trading framework encapsulated in a single application. In particular, students will learn how to wrap their previous code (data collection, signal generation, backtesting, evaluation, and dashboard creation) into functions that will be called via a single workflow. In other words, students will automate the manual component calculations done in the previous class to produce an end-to-end trading dashboard containing all relevant metrics and functionality.

Furthermore, students will not only learn how to "go live" with their trading frameworks by establishing a connection to an actual financial API, such as the Kraken Cryptocurrency Exchange API (which provides 24-hour market access and generous API request privileges), but also further their understanding of dataflows by implementing asynchronous tasks and streaming capabilities that allows for a more robust trading dashboard that can update its underlying data without having to re-draw its overall dashboard each time.

### Class Objectives

By the end of class, students will be able to:

* Design an end-to-end workflow for a trading framework (data collection > signal generation > backtesting > evaluation > dashboard creation).

* Abstract their previous day's algorithmic trading calculations into functions and execute an end-to-end implementation of a working trading framework.

* Utilize live financial data by connecting their trading frameworks to the Kraken Cryptocurrency Exchange API.

* Persist or save their trading data to a database such as sqlite.

* Perform asynchronous tasks and loops using asyncio.

* Implement asyncio with their trading frameworks to fetch data and update the dashboard in parallel.

* Enhance their trading dashboards with data streaming capabilities.

* Deploy their algorithmic trading application online via Heroku.

### Instructor Notes

* Today's lesson will tie together the concepts and coding solutions from the previous day into a single robust trading framework that can produce an end-to-end implementation of a trading dashboard with working metrics.

* This lesson will primarily focus on developing the *infrastructure* of the trading framework and therefore will not contain as much domain-specific trading knowledge.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 15.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, students will review the algorithmic trading concepts taught in the previous class to prepare them for today's consolidation of multiple trading functions (signal generation, backtesting, trade evaluation, etc.) into a single trading framework. This section is a key opportunity to quickly re-visit the core components related to algorithmic trading before transitioning to the design of an algorithmic trading framework.

Welcome students to the second day of algorithmic trading and ask for any volunteers that can answer the following review questions:

* What is algorithmic trading?

  **Answer:** Algorithmic trading is the concept of utilizing a machine to automate the process of buying and selling assets based on specific trading signal criteria and decision-making logic.

* What is a trading signal?

  **Answer:** A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

* What is backtesting?

  **Answer:** Backtesting is the process for measuring the overall performance of a trading strategy using historical stock prices to simulate executed trades dictated by the calculated trading signals and trade decision logic.

* What are algorithmic trading evaluation metrics?

  **Answer:** Metrics that showcase information such as overall portfolio or per-trade performance. Examples include cash balance, total portfolio value, per-trade profits and losses, and dates of entry and exit trades.

* What is a trading dashboard?

  **Answer:** Like other dashboards, a *trading dashboard* consolidates and presents multiple facets of information pertaining to the performance of an algorithmic trading application, allowing a user to interact with the data via tables and plots (visualizations).

Then, create some excitement around the day by mentioning the following points:

* The goal of today's lesson is to take what students learned in day 1 and put the concepts together to formulate an end-to-end full stack trading application that is capable of pulling financial data, generating signals, backtesting, executing a trade strategy, evaluating results, and generating dashboard visualizations in a single workflow.

* Creating a trading application from scratch should hopefully dispel the esoteric nature of developing algorithmic trading applications similar to those offered from commercial services, and allows for the ability to add additional features in the future, should students desire to do so.

* By the end of today's lesson, students should have a working trading application that they can demo to future employers, as well as use as the foundation for their own custom trading application if they decide to further expand upon it.

Answer any questions before moving on.

---

### 2. Student Do: Trading Functions (5 min)

In this activity, students will be given a random sequence of trading function names and will be asked to propose the correct order of the functions if they were to be implemented in an algorithmic trading application. Note that there is not a single precise order, so treat this as a thought exercise to help drive engagement and discussion around the use of frameworks to encapsulate and abstract code.

**Files:**

* [Instructions](Activities/01-Stu_Trading_Functions/README.md)

* [jarvis.py](Activities/01-Stu_Trading_Functions/Unsolved/jarvis.py)

### 3. Instructor Do: Review Trading Functions (10 min)

Call on different students to describe their function call order and live code their solution directly into the unsolved Python script.

After displaying a few student solutions, explain the following points:

* Even without code, a framework provides an abstraction that is easy to read, understand, and use. This is a very powerful programming technique that is analogous to providing an API to the code.

* By encapsulating the code in functions, we can swap code out when necessary. For example, fetching data from a file or an API can easily be changed inside of the `fetch_data` function without affecting how the functions are called.

Open the solution and highlight the solution that was provided:

```python
initialize()
fetch_data()
generate_signals()
execute_backtest()
execute_trade_strategy()
evaluate_metrics()
build_dashboard()
```

* The true order of this solution may change once the code and behavior of each function is provided, but even without code, the call order will typically follow a pattern of initializing data containers, fetching data, transforming or using the data, and displaying the data.

* By placing the call order in a main function, it can be easy to control and update the function call order in a single place in the program.

Ask any questions before moving on.

---

### 3. Everyone Do: Algorithmic Trading Framework (15 mins)

In this activity, students will code along with the instructor and port over their previous algorithmic trading code into the new algorithmic trading framework.

**Files:**

* [algorithmic_trading_code.ipynb](Activities/02-Evr_Algo_Trading_Framework/Solved/algorithmic_trading_code.ipynb)

* [jarvis_v1.py](Activities/02-Evr_Algo_Trading_Framework/Unsolved/jarvis_v1.py)

* [jarvis_v2.py](Activities/02-Evr_Algo_Trading_Framework/Solved/jarvis_v2.py)

Quickly discuss the following before proceeding onward to the walk through:

* Now that students have completed their workflow design for their new algorithmic trading applications, it is now time to take what they've learned in the previous day and assemble the code together in a single framework/application.

Open the Jupyter Notebook with the original source code to be ported and highlight the following points:

* Jupyter naturally provides a method of chunking code into cells which can make the code more readable and reusable; in programming, a better practice is to chunk code together into functions. This provides a layer of abstraction that makes the code easier to modify and reuse.

* Ask students what code cells might be good candidates for the different functions in the trading framework.

Then, ask students to open the starter code in VScode and follow along as you port the original code into the algorithmic trading framework.

* Briefly mention that because we are porting original algorithmic code into the trading framework, there is currently no need to fill in the following functions; however, as features (and therefore complexity) to the framework grows, these functions will need to be defined.

  ```python
  def initialize():
    """Initialize the dashboard, data storage, and account balances."""
    return
  ```

  ```python
  def execute_trade_strategy():
      """Makes a buy/sell/hold decision."""
      return
  ```

* Explain that while the `fetch_data` function reads in the contents of a CSV file, abstracting the code for fetching data into a function allows for the possibility to swap out the definition so that any data or API can be used.

  ```python
  def fetch_data():
      """Fetches the latest prices."""
      # Set the file path and read CSV into a Pandas DataFrame
      filepath = Path("../Resources/aapl.csv")
      data_df = pd.read_csv(filepath)

      # Print the DataFrame
      print(data_df.head())
      return data_df
  ```

* Explain that the `generate_signal` function in the framework can be used to generate trading signals. Again, abstracting this code into its own function will make it easier to code up new signal generators later. The goal of the framework is to encapsulate each chunk of code so that it is easier to change later.

  ```python
  def generate_signals(data_df):
      """Generates trading signals for a given dataset."""
      # Set window
      short_window = 10
      long_window = 20

      # Set up the signals DataFrame
      signals_df = data_df.copy()
      signals_df["date"] = pd.to_datetime(signals_df["date"], infer_datetime_format=True)
      signals_df = signals_df.set_index("date", drop=True)
      signals_df["signal"] = 0.0

      # Generate the short and long moving averages
      signals_df["sma10"] = signals_df["close"].rolling(window=short_window).mean()
      signals_df["sma20"] = signals_df["close"].rolling(window=long_window).mean()

      # Generate the trading signal 0 or 1,
      signals_df["signal"][short_window:] = np.where(
          signals_df["sma10"][short_window:] > signals_df["sma20"][short_window:], 1.0, 0.0
      )

      # Calculate the points in time at which a position should be taken, 1 or -1
      signals_df["entry/exit"] = signals_df["signal"].diff()

      # Print the DataFrame
      print(signals_df.head())
      return signals_df
  ```

* Now that two of the original algorithmic trading code snippets have been ported over, ask students how they would grab the backtesting code and place it into its own function.

  ```python
  def execute_backtest(signals_df):
      """Backtests signal data."""
      # Set initial capital
      initial_capital = float(100000)

      # Set the share size
      share_size = 500

      # Calculate backtest metrics
      signals_df['Position'] = share_size * signals_df['signal']
      signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
      signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()
      signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
      signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
      signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()
      signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1

      # Print the DataFrame
      print(signals_df.head())
      return signals_df
  ```

* Explain that the original algorithmic code for evaluating metrics separates the calculation of the portfolio and trade evaluation metrics; however, the `evaluate_metrics` function can calculate and return both evaluation metrics at the same time.

  ```python
  def evaluate_metrics(signals_df):
      """Generates evaluation metrics from backtested signal data."""
      #### CALCULATE PORTFOLIO METRICS ####
      # Initialize index and columns
      metrics= ['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio']
      columns = ['Backtest']

      # Initialize the DataFrame with index set to evaluation metrics and column as `Backtest` (just like PyFolio)
      portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

      # Assign portfolio evaluation metrics for each index
      portfolio_evaluation_df.loc['Cumulative Returns'] = signals_df['Portfolio Cumulative Returns'][-1]
      portfolio_evaluation_df.loc['Annual Return'] = ((1 + signals_df['Portfolio Daily Returns'].mean())**252 - 1)
      portfolio_evaluation_df.loc['Annual Volatility'] = ((1 + signals_df['Portfolio Daily Returns'].std())** 252 - 1)
      portfolio_evaluation_df.loc['Sharpe Ratio'] = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))

      # Calculate sortino ratio
      sortino_ratio_df = signals_df[['Portfolio Daily Returns']]
      sortino_ratio_df['Downside Returns'] = 0
      target = 0
      sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
      down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
      expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()
      sortino_ratio = expected_return/down_stdev
      portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio

      # Print the DataFrame
      print(portfolio_evaluation_df.head())

      #### CALCULATE TRADE METRICS ####
      trade_evaluation_df = pd.DataFrame(
          columns=['Stock', 'Entry Date', 'Exit Date', 'Shares', 'Entry Share Price', 'Exit Share Price', 'Entry Portfolio Holding', 'Exit Portfolio Holding', 'Profit/Loss']
      )

      entry_date = ''
      exit_date = ''
      entry_portfolio_holding = 0
      exit_portfolio_holding = 0
      share_size = 0
      entry_share_price = 0
      exit_share_price = 0

      for index, row in signals_df.iterrows():
          if row['entry/exit'] == 1:
              entry_date = index
              entry_portfolio_holding = row['Portfolio Holdings']
              share_size = row['Entry/Exit Position']
              entry_share_price = row['close']

          elif row['entry/exit'] == -1:
              exit_date = index
              exit_portfolio_holding = abs(row['close'] * row['Entry/Exit Position'])
              exit_share_price = row['close']
              profit_loss = exit_portfolio_holding - entry_portfolio_holding
              trade_evaluation_df = trade_evaluation_df.append(
                  {'Stock': 'AAPL', 'Entry Date': entry_date, 'Exit Date': exit_date, 'Shares': share_size, 'Entry Share Price': entry_share_price, 'Exit Share Price': exit_share_price, 'Entry Portfolio Holding': entry_portfolio_holding, 'Exit Portfolio Holding': exit_portfolio_holding, 'Profit/Loss': profit_loss},
                  ignore_index=True)

      # Print the DataFrame
      print(trade_evaluation_df.head())
      return portfolio_evaluation_df, trade_evaluation_df
  ```

* Now that the previous functions have been ported over, the next step is to define the `build_dashboard` function and set its inputs as the backtested signal data, the portfolio evaluation metrics, and the trade evaluation metrics--from which to derive the resulting visualizations.

  ```python
  def build_dashboard(signals_df, portfolio_evaluation_df, trade_evaluation_df):
      """Build the dashboard."""
      # Create hvplot visualizations
      price_plot = signals_df.hvplot.line(x='date', y=['close', 'sma10', 'sma20'], value_label='Price', width=1000, height=400, rot=90)
      portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(columns=['index', 'Backtest'], width=300, height=400)
      trade_evaluation_table = trade_evaluation_df.hvplot.table()

      # Create rows, columns, and tabs
      row_one = pn.Row(price_plot)
      row_two = pn.Row(portfolio_evaluation_table, trade_evaluation_table)
      column = pn.Column(row_one, row_two)
      tabs = pn.Tabs(("Summary", column))

      # Assign dashboard
      dashboard = tabs
      return dashboard
  ```

* Lastly, the `main` function wraps the rest of the functions in a single workflow--allowing the application to perform a single call of the `main` function to then kick off the totality of the framework. Note the fact that the output of one function generally serves as the input to the next.

  ```python
  def main():
      """Main Event Loop."""
      data_df = fetch_data()
      signals_df = generate_signals(data_df)
      tested_signals_df = execute_backtest(signals_df)
      portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(tested_signals_df)
      dashboard = build_dashboard(tested_signals_df, portfolio_evaluation_df, trade_evaluation_df)
      dashboard.servable()
      return

  main()
  ```

* And that's it! Students now have an end-to-end implementation of the code that was produced from day 1! Going forward, students should also keep in mind that to enhance code readability, they should try to minimize the lines of code in their Python applications wherever possible (which is why the solved code looks more condensed than the Jupyter Notebook code).

Ask if there are any questions before moving on.

---

### 4. Instructor Do: Trading with CCXT (15 min)

In this section, students will become familiar with the expansive CCXT library which abstracts upon a collection of available cryptocurrency exchange APIs and provides unified functions to simplify API calls when switching from different cryptocurrency exchange APIs. In particular, students will work with the Kraken API and extract both historical and current price data.

**File:** [ccxt.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt.ipynb)

Open the solution file and review the following:

* Because CCXT is a collection of multiple APIs under the hood, when choosing to connect to a particular exchange such as Kraken, the credentials for that particular exchange must be set. In this case, the public and private keys for the Kraken API are imported from the `KRAKEN_PUBLIC_KEY` and `KRAKEN_SECRET_KEY` environment variables and set to the `kraken` class of the CCXT library.

  ```python
  # Import environment variables
  kraken_public_key = os.getenv('KRAKEN_PUBLIC_KEY')
  kraken_secret_key = os.getenv('KRAKEN_SECRET_KEY')
  ```

  ```python
  # Set the public and private keys for the API
  exchange = ccxt.kraken({
    'apiKey': kraken_public_key,
    'secret': kraken_secret_key,
  })
  ```

* In most cases, CCXT requires that a user must load the list available markets and trading symbols prior to accessing other API functions for an exchange. This can be set either explicitly or automatically by CCXT when it detects that a user has not initiated the `load_markets` function when the first unified API call is made.

  ![kraken-cryptos](Images/kraken-cryptos.png)

* After loading the market data for the Kraken exchange and importing the data as a Pandas DataFrame, a quick print of the column values shows that there are (as of this writing) 110 available cryptocurrencies for trading on the Kraken exchange.

  ![kraken-crypto-symbols](Images/kraken-crypto-symbols.png)

* The `fetch_ohlcv` function can be used to fetch the candlestick bar data for `BTC/USD`, which returns a list of lists containing records with `timestamp`, `open`, `high`, `low`, `close`, and `volume` data points. As a result of the lack of key-value pairs, when importing data into a Pandas DataFrame, column names will need to be specified according to the structure dictated by the CCXT documentation.

  ![kraken-btc-usd-historical-prices](Images/kraken-btc-usd-historical-prices.png)

  ```python
  [
    [
        1504541580000, // UTC timestamp in milliseconds, integer
        4235.4,        // (O)pen price, float
        4240.6,        // (H)ighest price, float
        4230.0,        // (L)owest price, float
        4230.7,        // (C)losing price, float
        37.72941911    // (V)olume (in terms of the base currency), float
    ],
    ...
  ]
  ```

* The `timestamp` data from the `fetch_ohlcv` function is returned in *Epoch time* or *Unix time* format, which is the number of seconds (or in this case milliseconds) since the origin point in time known as the *Unix epoch*. Therefore, in order to convert epoch timestamps to a readable date format, the `to_datetime` function with the `unit` parameter should be used.

  ![convert-epoch-timestamp-ms](Images/convert-epoch-timestamp-ms.png)

* In order to fetch the latest pricing data for `BTC/USD`, the `fetch_ticker` function should be used. Make sure to drop the `info` column as the subsequent import to a Pandas DataFrame will produce multiple records due to the nested object nature of the `info` column, and in this case only one record is desired.

  ![kraken-btc-usd-current-price](Images/kraken-btc-usd-current-price.png)

  ```python
  {
    'symbol':        string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
    'info':        { the original non-modified unparsed reply from exchange API },
    'timestamp':     int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
    'datetime':      ISO8601 datetime string with milliseconds
    'high':          float, // highest price
    'low':           float, // lowest price
    'bid':           float, // current best bid (buy) price
    'bidVolume':     float, // current best bid (buy) amount (may be missing or undefined)
    'ask':           float, // current best ask (sell) price
    'askVolume':     float, // current best ask (sell) amount (may be missing or undefined)
    'vwap':          float, // volume weighed average price
    'open':          float, // opening price
    'close':         float, // price of last trade (closing price for current period)
    'last':          float, // same as `close`, duplicated for convenience
    'previousClose': float, // closing price for the previous period
    'change':        float, // absolute change, `last - open`
    'percentage':    float, // relative change, `(change/open) * 100`
    'average':       float, // average price, `(last + open) / 2`
    'baseVolume':    float, // volume of base currency traded for last 24 hours
    'quoteVolume':   float, // volume of quote currency traded for last 24 hours
  }
  ```

* To view the list of available functions for an exchange, display the results of the `has` instance variable from the current exchange object. Functions are indicated as available based on a Boolean such as True or False.

  ![exchange-has](Images/exchange-has.png)

* While today's lesson only focuses on fetching pricing data from the Kraken API, the CCXT library also allows a user to perform tasks such as checking account balances/status, fetching any open orders, or even placing and executing trades.

  **Note:** The following functions return minimal/empty datasets due to the fact that the Kraken account used in this lesson is not funded with capital.

  ![additional-functions](Images/additional-functions.png)

Answer any questions before moving on.

---

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

  # Backtest signal data and evaluate metrics from backtested results
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

* Close but no cigar! Modifying the share size calculation looks to have improved the account value metrics but unfortunately remain slightly off. This is noted by the fact that an initial account cash balance of $100,000 should not be able to afford a trade with an entry portfolio holding of greater than $100,000. Therefore, in order to obtain the correct share sizes, the framework will need to shift from a batch processing paradigm (data retrieved and processed all at once) to a real-time or streaming paradigm (data retrieved and processed every second) so as to access the running account cash balance and BTC/USD closing prices.

  ![trading-dashboard-improved-metrics](Images/trading-dashboard-improved-metrics.png)

---

### 7. Instructor Do: Asyncio (10 min)

In this demonstration, students will learn how to create asynchronous functions that do not block the dashboard from loading.

Note that a complete explanation of asyncio is out-of-scope for this lesson, so refer students to the [official documents](https://docs.python.org/3/library/asyncio.html) and office hours if they want to learn more.

**Files:**

* [blocked_dashboard.py](Activities/05-Ins_Asyncio/Solved/blocked_dashboard.py)

* [asyncio_demo.ipynb](Activities/05-Ins_Asyncio/Solved/asyncio_demo.ipynb)

* [async_dashboard.py](Activities/05-Ins_Asyncio/Solved/async_dashboard.py)

Start by running the `blocked_dashboard.py` code to show the long loading time.

```shell
panel serve --log-level debug --show blocked_dashboard.py
```

Open the `blocked_dashboard.py` code and highlight the following points:

```python
def fetch_data():
    """Simulate a delayed fetch."""
    time.sleep(5)


def serve_dashboard():
    dashboard = pn.Column("# My Blocked Dashboard")
    return dashboard.servable()


fetch_data()
serve_dashboard()
```

* The `fetch_data` function simulates a data fetch that takes a long time. In practice, any request to an external API may actually take a long time to fetch and return the data.

* The serve_dashboard function simply serves up a simple dashboard of text.

* Python is a synchronous language. That means that it runs one line of code and waits on that code to finish before moving on to run the next line of code. In this example, the `fetch_data` function takes 5 seconds to run before the code that serves the dashboard can run. This effectively blocks the page from loading until the data returns.

* In practice, fetching data can actually take a lot longer than expected. Database queries, network delays, and other factors can create delays in the request. With code like this, the user experience suffers because the page cannot load until the data returns.

Open `asyncio_demo.ipynb` and highlight the following points about the asyncio library:

* Python provides a library called `asyncio` to write concurrent or asynchronous code.

* Asynchronous code just means that Python doesn't have to wait on that line to finish running before moving on to the next line of code.

Run the following cell to show the delay created by the default synchronous behavior:

```python
def fetch_data():
    time.sleep(3)
    print("data")

def serve_dashboard():
    print("dashboard")

fetch_data()
serve_dashboard()
```

Break down the asynchronous code cell and explain the following:

```python
async def fetch_data():
    await asyncio.sleep(3)
    print("data")

def serve_dashboard():
    print("dashboard")

loop = asyncio.get_event_loop()

loop.create_task(fetch_data())
serve_dashboard()
```

* Code can be defined as asynchronous using the keywords `async` and `await`. This tells Python to handle this code differently than the other code.

* The `async` keyword in the function definition tells asyncio that this function is something called a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) which is just code that can be executed differently (asynchronously) from the normal code.

* The `await` keyword indicates which line of code can be waited for asynchronously. This is what suspends the coroutine until this line of code finishes running. In other words, the sleep statement can run asynchronously while Python continues to run the remaining code in the program.

* Asyncio uses an event loop to run code asynchronously. The event loop can be thought of as a loop that sits off to the side and just periodically checks to see if the async code has finished running yet. When it does finish running, it can rejoin the main program. Meanwhile, Python is free to continue running other code.

* The asyncio provides several functions for using the event loop. This example just runs the `fetch_data` function as a task in the event loop. It then immediately moves on to run the `serve_dashboard` code in the main program while fetch_data continues to run in the event loop. Once fetch_data finishes, it rejoins the main program.

Show that the dashboard no longer has to wait on the fetch_data function:

```python
async def fetch_data():
    await asyncio.sleep(3)
    print("data")

def serve_dashboard():
    dashboard = pn.Column("# My Panel Dashboard")
    return dashboard.servable()

loop = asyncio.get_event_loop()

loop.create_task(fetch_data())
serve_dashboard()
```

Finally, run the `async_dashboard.py` code to show that the page can immediately load while the data is still being fetched.

```shell
panel serve --log-level debug --show async_dashboard.py
```

Explain that we can use these ideas to modify our trading dashboard so that the page can load while new data is collected asynchronously. The dashboard can then be updated with the new data once it returns.

---

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

* Because the trading framework is now using real-time data, data can now be evaluated at a more granular level. This allows decisions to be based at the record level.

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

* The result of the previous changes shows a trading dashboard that not only displays the real-time pricing data for BTC/USD (along with associated short and long window moving averages), but also makes buy, sell, or hold decisions in real-time.

  ![async-trading-dashboard](Images/async-trading-dashboard.gif)

Ask if there are any questions before moving on.

---

### 9. Everyone Do: Async Trading (15 mins)

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

* Because the trading framework is now using real-time data, data can now be evaluated at a more granular level. This allows decisions to be based at the record level.

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

* The result of the previous changes shows a trading dashboard that not only displays the real-time pricing data for BTC/USD (along with associated short and long window moving averages), but also makes buy, sell, or hold decisions in real-time.

  ![async-trading-dashboard](Images/async-trading-dashboard.gif)

Ask if there are any questions before moving on.

---

### 10. Everyone Do: Persisting Real-Time Data (15 mins)

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
  new_record_df.to_sql('data', db, if_exists='append', index=True)
  ```

* The data within the sqlite database is then queried, and if the number of rows returned is greater or equal to the minimum window, the program proceeds to executing the rest of its trading functions.

  ```python
  data_df = pd.read_sql(f"select * from data limit {max_window}", db)
  ```

* Putting everything together, it can be seen that the trading application now operates in such a way that new records are fetched and appended to the `data` table in a sqlite database, where they are later queried prior to the execution of later functions. The result is a trading application that stores its data and therefore can resume its operations in the event of a failure, as shown below.

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

  ![failure-recovery.gif](Images/failure-recovery.gif)

Ask if there are any questions before moving on.

---

### 11. Instructor Do: Streaming Data with Streamz (15 mins)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to show students how to update a visualization as data continues to flow without the need for re-constructing the visual component each time.

**File:** [streamz.ipynb](Activities/08-Ins_Streaming/Solved/streamz.ipynb)

Open the solution file and discuss the following:

* First and foremost, we will need to import the necessary libraries and dependencies in order to properly stream data.

  ```python
  import os
  import ccxt
  import pandas as pd
  import hvplot.streamz
  from streamz import Stream
  from streamz.dataframe import DataFrame
  ```

* The Streamz library supports streaming data from a Pandas DataFrame and includes a custom Stream DataFrame object that can bind Stream objects to itself. The `example` parameter sets the structure of the Stream DataFrame object, and similar to a normal DataFrame, hvplot can be called on the Stream DataFrame to generate a visualization such as a scatter plot.

  ![stream-dataframe](Images/stream-dataframe.png)

* In order to push data through to the scatter plot, the Stream object houses an `emit` function that pushes a DataFrame with similar structure to the bound Stream DataFrame object, which is then used to update the scatter plot. In this case, a loop from 1 to 20 is performed in which for every loop, a DataFrame is created with the value `i` and pushed via the Stream object to the scatter plot. The result is a scatter plot that streams its data points from 1 to 20.

  ![stream-emit](Images/stream-emit.gif)

* In addition, hvplot allows for a `backlog` parameter that creates a rolling window for streaming data. In this case, the data is streamed to the scatter plot ranging from 1 to 100; however, the use of the`backlog` parameter sets a rolling window of 10 data points in the scatter plot.

  ![stream-emit-rolling](Images/stream-emit-rolling.gif)

* Lastly, the Stream library can be used to stream data received from an external API, such as the Kraken exchange via the ccxt library. In this case, a Stream DataFrame object is created and bound to the Stream object with a structure set to a DataFrame with the column `close`. Then, in a continuous while loop, data is pulled from Kraken and a DataFrame with a similar structure to the Stream DataFrame object is pushed via the `emit` function. The result is a line chart that continually streams BTC/USD pricing data.

  ![stream-kraken-data](Images/stream-kraken-data.gif)

Ask any questions before moving on.

---

### 12. Student Do: Stream Trading (15 min)

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

* When running the application, the `emit` function is used to continuously push data through the streaming data pipeline managed by the Stream object. Only a single record should be passed to the `emit` function.

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

---

### 13. Instructor Do: Reflect (10 min)

This activity will conclude today's lesson on Algorithmic Trading Day 2 and provide a chance for students to reflect upon what they've learned throughout the day.

The purpose of this activity is to allow students a chance to take a step back and digest the concepts that have been taught today by engaging students in such a way that students drive the conversation, thereby reinforcing their learning by "teaching" the class.

Recap the skills and concepts learned throughout the lesson, and engage students by having them lead the discussion as much as possible:

* Ask if there are any students who would like to volunteer to summarize the any of the following concepts.

  * What is the purpose of an algorithmic trading framework? What does it look like?

    **Answer:** The purpose of an algorithmic trading framework is to create an end-to-end implementation of working full stack financial trading application. Namely, a framework works by abstracting code into functions, so that the underlying code can potentially be further modified in the future to include additional functionality or be completely replaced altogether.

  * What is the ccxt library and what does it do? Why is it a convenient library to have in terms of trading?

    **Answer:** The ccxt library is a Cryptocurrency Exchange Trading API that allows a developer to access the many cryptocurrency APIs, such as the Kraken API, through a single API interface.

  * What is the asyncio library? Why was it important for our algorithmic trading applications?

    **Answer:** The asyncio library is an asychronous framework that allows for producing concurrent code. Using asyncio allowed for us to bypass the blocking nature of the continuous while loop, thereby facilitating real-time data loads.

  * What is data persistence? Why is it important?

    **Answer:** Data persistence is the concept of storing or "persisting" data in a reliable location such as a database. It is often important for failure prevention/disaster recovery in the event that an application fails, meaning that an application can pick up where it last failed due to the most recent "save" point.

  * What is the streamz library? What benefits did it provide for our algorithmic trading applications?

    **Answer:** The streamz library allowed for streaming of data to our Panel dashboard and associated visualizations, thereby mitigating the need to re-build the dashboard each time.

* Ask if there are any volunteers who would like to add anything that has not been previously stated.

Then, get students reflecting on what they've learned so far:

* Ask students how might they apply what they've learned so far in Unit 15. Will they go on to manage their own investments through automation?

* Ask students how they now feel regarding algorithmic trading (comfortable or uncomfortable?).

* Ask students to identify two potential things they'd like to practice more from today's lesson that they might have struggled with conceptually.

Finish the recap with a few statements of encouragement:

* Tell students they should give themselves another round of applause. Students now have the tools necessary to engage in live algorithmic trading!

* Remind students that should they choose, they can continue to build out their trading applications to make them even more robust and scalable. In particular, this will be especially impressive to potential employers as not many individuals have an algorithmic trading application under their belts!

* The next step is to further enhance students' algorithmic trading frameworks with machine learning capabilities in Day 3. Students are on their way to not only managing their own trades better, but building a machine that can learn to do it better!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
