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

### 1. Instructor Do: Welcome Class (10 min)

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

### 2. Student Do: Trading Functions (10 min)

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

### 4. Everyone Do: Algorithmic Trading Framework (20 min)

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

### 5. Instructor Do: Trading with CCXT (15 min)

In this section, students will become familiar with the expansive CCXT library which provides an API for over 120 cryptocurrency exchanges. In particular, students will work with the Kraken API and extract both historical and current price data.

**File:** [ccxt.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt.ipynb)

Open the solution file and review the following:

* CCXT provides a common API for over 120 cryptocurrency exchanges.

* To use a specific exchange, the API keys for that exchange must be set. In this example, the Kraken exchange is used and requires those keys to be exported before running the notebook.

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

* The Kraken exchange requires a list of markets and trading symbols to be loaded in order to use the API functions. This can be done manually using the `load_markets` function or implicitly upon the first call to the API.

  ![kraken-cryptos](Images/kraken-cryptos.png)

* The columns of the DataFrame show the symbols available for trading on the Kraken exchange.

  ![kraken-crypto-symbols](Images/kraken-crypto-symbols.png)

* To view the list of available functions for an exchange, display the results of the `has` instance variable from the current exchange object. Functions are indicated as available based on a Boolean such as True or False.

  ![exchange-has](Images/exchange-has.png)

* The `fetch_ohlcv` function can be used to fetch the candlestick data (open, high, low, close, and volume prices) for `BTC/USD`.

  ```python
  historical_prices = exchange.fetch_ohlcv("BTC/USD", "1d")
  ```

* When loading this OHLC data into a Pandas DataFrame, the columns will also need to be specified.

  ![kraken-btc-usd-historical-prices](Images/kraken-btc-usd-historical-prices.png)

* CCXT provides all timestamps in milliseconds. This can be converted to a DatetimeIndex in Pandas using the `to_datetime` function.

  ```python
  historical_prices_df["date"] = pd.to_datetime(
      historical_prices_df["timestamp"], unit="ms"
  )
  ```

Take a moment to explain the differences in evaluating a trading strategy and going live with a strategy. Highlight the following points:

* Evaluating a trading strategy often requires backtesting the strategy using historical data and evaluating the strategy based on the performance of the model on historical prices.

* Once the strategy has been validated, the algorithm can be executed in a live trading environment. In this live trading environment, it is common to only fetch the prices at the minimal interval required to make a decision. Evaluation metrics and performance can then be updated with each incremental new data point.

* CCXT provides methods to fetch current prices and statistics for individual currencies. This current data can be used to make a trading decision in a live algorithmic trading environment.

* In this example, the `fetch_ticker` function is used to retrieve the latest pricing data for `BTC/USD`.

  ```python
  current_price = exchange.fetch_ticker('BTC/USD')
  ```

* The `info` column contains the original exchange API data that usually just be treated as duplicate information and deleted.

  ```python
  del current_price['info']
  ```

Explain that while today's lesson only focuses on fetching pricing data from the Kraken API, the CCXT library also allows a user to perform tasks such as checking account balances/status, fetching any open orders, or even placing and executing trades.

  **Note:** The following functions return minimal/empty datasets due to the fact that the Kraken account used in this lesson is not funded with capital.

  ![additional-functions](Images/additional-functions.png)

Answer any remaining questions before moving on.

---

### 6. Everyone Do: Going Live with CCXT (15 min)

In this activity, students will code along with the instructor to update a version of the algorithmic trading framework to use the Kraken exchance from the CCXT API.

**File:**

* [jarvis.py](Activities/04-Evr_Going_Live/Unsolved/jarvis.py)

Live code the solution to this activity with the entire class. Use the code to explain new concepts to students, and engage the class with questions when appropriate. Be sure to go slow and give students plenty of time to keep upp.

Start the activity with a brief overview of the framework to show which sections will need to be updated to "go live".

* **NOTE:** Each section that needs to be updated will have a `# @TODO:` comment to make it easier to find those sections.

Highlight the following points about the main function:

```python
print("Initializing account and DataFrame")
account, df = initialize(10000)
print(df)


def main():

    while True:
        global account
        global df

        # Fetch and save new data
        new_df = fetch_data()
        df = df.append(new_df, ignore_index=True)
        min_window = 22
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            print(signals)
            account = execute_trade_strategy(signals, account)
        time.sleep(1)
```

* The main function uses a loop to fetch new data every 1 second. This loop can easily be modified to fetch data at any interval required for the trading algorithm.

* The loop refers to `global` variables for the account and DataFrame. This is required because the `account` and `df` variables are initialized outside of the loop. We will see later in today's class why initializing certain variables like this will be advantageous.

* New data is fetched from the Kraken API using the `fetch_data` function and then appended to the main `df` DataFrame.

* A conditional statement is used to make sure there is enough data to generate a signal for the strategy before calling those functions. In this case, the strategy uses a 20 day window for the moving average crossover, so we want a minimum of 20 data points before we generate signals.

Move to the `initialize` function definition and highlight the following points:

```python
def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Intializing Account and DataFrame")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize dataframe
    df = fetch_data()

    # @TODO: We will complete the rest of this later!
    return account, df
```

* The initialize function is used to create all of the initial variables and data containers that the function may need. By initializing all of the functions in a single function, it makes it easy to update and change the initial values or data types used.

* The account balance is a simple Python dictionary to keep track of the cash balance and number of shares owned.

* The `df` DataFrame is initialized using the `fetch_data` function.

Move to the `fetch_data` function and prompt the class to help complete the function definition. Highlight the following points:

```python
def fetch_data():
    """Fetches the latest prices."""
    print("Fetching data...")
    kraken_public_key = os.getenv("KRAKEN_PUBLIC_KEY")
    kraken_secret_key = os.getenv("KRAKEN_SECRET_KEY")
    kraken = ccxt.kraken({"apiKey": kraken_public_key, "secret": kraken_secret_key})

    close = kraken.fetch_ticker("BTC/USD")["close"]
    datetime = kraken.fetch_ticker("BTC/USD")["datetime"]
    df = pd.DataFrame({"close": [close]})
    df.index = pd.to_datetime([datetime])
    return df
```

* This function will use the Kraken exchange. However, by abstracting and encapsulating the data fetching code with this function, it is very easy to use a different exchange or API to trade other currencies, equities, etc.

* The Kraken API keys need to be set from the environment variables.

* This particular example only needs the closing prices and timestamp for `BTC`. This data is returned as a DataFrame for convenience, but it could also have been returned as raw data.

Show that the code for the signal generation uses the same moving crossover strategy as in previous examples, but that could also be easily changed. Point out again that because this code uses a window of 20 prices, we need to ensure that we fetch at least 20 data points before any signals are generated.

```python
def generate_signals(df):
    """Generates trading signals for a given dataset."""
    print("Generating Signals")
    # Set window
    short_window = 10

    signals = df.copy()
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

Move on to the `execute_trade_strategy` and show how we can use the account balance and the latest data retrieved to make a trading decision.

```python
def execute_trade_strategy(signals, account):
    """Makes a buy/sell/hold decision."""

    print("Executing Trading Strategy!")

    if signals["entry/exit"].iloc[-1] == 1.0:
        print("buy")
        number_to_buy = round(account["balance"] / signals["close"].iloc[-1], 0) * 0.001
        account["balance"] -= number_to_buy * signals["close"].iloc[-1]
        account["shares"] += number_to_buy
    elif signals["entry/exit"].iloc[-1] == -1.0:
        print("sell")
        account["balance"] += signals["close"].iloc[-1] * account["shares"]
        account["shares"] = 0
    else:
        print("hold")

    return account
```

* This function only prints the trade decision, but an API call can be used here to place a real order.

Run the complete trading script in the terminal to show that the data being fetched until there is enough data collected to generate signals and execute the trading strategy.

```shell
python jarvis.py
```

Congratulate students on creating their first live trading platform!

Explain that the beauty of a robust application framework, is that the abstraction and encapsualtion of code makes it easy to make additional changes. Explain that the remainder of class will be used to iterate and improve on this platform to make it even better!

---

### 7. Instructor Do: Asyncio (10 min)

In this demonstration, students will learn how to create asynchronous functions that do not block the dashboard from loading.

Note that a complete explanation of asyncio is out-of-scope for this lesson, so refer students to the [official documents](https://docs.python.org/3/library/asyncio.html) and office hours if they want to learn more.

**Files:**

* [blocked_dashboard.py](Activities/05-Ins_Asyncio/Solved/blocked_dashboard.py)

* [asyncio_demo.ipynb](Activities/05-Ins_Asyncio/Solved/asyncio_demo.ipynb)

* [async_dashboard.py](Activities/05-Ins_Asyncio/Solved/async_dashboard.py)

Explain to students that now that we have a basic live trading script working, we want to include live visualizations as well. However, there are some problems with plotting live data that needs to be addressed first.

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

### 8. Everyone Do: Async Trading (15 min)

In this activity, students will code along with the instructor to update their live trading code to fetch data asynchronously with [asyncio](https://docs.python.org/3/library/asyncio.html).

**Files:** [jarvis.py](Activities/06-Evr_Async_Trading/Solved/jarvis.py)

Open the starter code and live code the solution with the class. Explain any new concepts as you go, and be sure to proceed slowly and pause frequently to make sure that students can keep up.

Start by skimming the code with the class and showing the `# @TODO:` comments where the code will need updated. Explain that the goal is to use asyncio so that the dashboard can be loaded and updated without blocking the page from loading.

Import the necessary libraries to use asyncio, hvplot, and panel.

```python
import asyncio

import hvplot.pandas
import panel as pn

pn.extension()
```

Update the code for the `initialize`, `build_dashboard`, and `update_dashboard` functions and highlight the following:

```python
# Intialize the dashboard
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

* The `initialize` function uses the `build_dashboard` function to build and return a simple dashboard that initially just contains static text.

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

* The dashboard is initialized as Static text and then served immediately. Afterwards, we can use an asynchronous main function to fetch new data and update the dashboard without blocking the page from loading.

  ```python
  account, df, dashboard = initialize(10000)
  dashboard.servable()
  ```

* In this example, we choose to make the main function async so that it does not block the dashboard from loading. The code awaits both the `fetch_data` function and the `asyncio.sleep` function.

  * **Note:** The `requests` library that is used in the `fetch_data` function is consdiered a blocking library. Blocking libraries like this must be called using a special function called `run_in_executor`. More information about this can be found in the official [asyncio documents](https://docs.python.org/3/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools), but this code can be used anytime that the requests library is used. Alternatively, there is a asyncio-compatible library called [aiohttp-requests](https://pypi.org/project/aiohttp-requests/) that can be used instead.

* Once the new data is fetched, the `update_dashboard` function is called to update the plots. This function simply replaces the dashboard plots for now, but this will be improved later in class.

* Finally, the main function is executed with a special asyncio function called `run_until_complete`. This is just one way to run the asynchronous code in the event loop.

  ```python
  # Python 3.7+
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  ```

Wrap up this activity by acknowledging that asynchronous code is very challenging to write. However, the code provided in this example can be used as a template that can be reused for many different algorithmic trading applications.

---

### 9. Everyone Do: Persisting Real-Time Data (15 min)

In this activity, students will learn how to persist their real-time data to a database. Students will code along with the instructor to update the trading framework to persist data with a sqlite database.

The purpose of this activity is to showcase the value in persisting data as doing so allows an application to pick up where it left off should a failure occur.

**File:**
* [jarvis.py](Activities/05-Evr_Persisting_Real_Time_Data/Unsolved/jarvis.py)

Explain to the class that the next enhancement to make to the trading algorithm is to persist the live data to a database. Persisting the live data allows the framework to recover from data errors, and it allows us to collect and use historical data without running into memory issues.

Quickly discuss the following before proceeding onward to the walk through:

* What is data persistence?

  **Answer:** Data persistence is the concept of saving data to a database so as to have a reliable copy of data that is *persisted* rather than transiently stored as in-memory data structures.

* Why is it important to persist data?

  **Answer:** Persisting data is generally a best practice as it provides a method for data recovery should an application ever fail; data stored in transient in-memory data structures will be lost forever if the application itself terminates. In addition, persisting data to a database allows for separate data analysis to be done at a later time, if desired.

With the class, update the starter code to use a sqlite database to persist the data. Be sure to highlight the following points about sqlite:

* `sqlite` is a database system that is provided with Python through the `sqlite3` library.

* `sqlite` is very useful for fast, lightweight database applications.

* Because it is included with Python and uses a file-based database, it is a popular choice for testing and prototyping code that requires a database.

* The same code shown today with sqlite can also be used with any database connector in Python including `postgresql`.

Import the sqlite3 library and show how the database connector is initialized in the code:

```python
def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Intializing account, database, and DataFrame")

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")
```

* In Python, a sqlite database can be created using `sqlite3.connect` with a filename for the database. The entire database is contained locally on disk in this file.

* With the database connection `db`, a cursor can be used to execute raw sql directly on the database. In this example, a cursor is used to drop the table called `data` if it already exists.

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

* Many appplications can share a common database. This allows you to create multiple trading applications that all share a common database.

* Capturing the live data makes it easier to choose how much data is selected for the trading strategy.

Ask if there are any questions before moving on.

---

### 10. BREAK (15 min)

---

### 11. Instructor Do: Streaming Data with Streamz (15 min)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to show students how to update a visualization as data continues to flow without the need for re-constructing the visual component each time.

**File:** [streamz.ipynb](Activities/08-Ins_Streaming/Solved/streamz.ipynb)

Begin this demonstration by asking the students if they noticed anything strange about the `update_dashboard` code. Point out that the dashboard is simply replaced with each new piece of data. While this approach is fine for a simple dashboard example, it can create problems for a complex dashboard.

Explain that a better approach to replacing the plots each time is to update the plots with new data. Explain that Panel, hvplot, and Plotly all provide tools to update plots in an efficient way using live data streams. In this example, we will use the `streamz` library with hvplot to update our plots to allow for live data streams.

Explain to students that hvplot uses the `Streamz` library to build a pipeline or buffer to manage continuos streams of data. A `Stream` can be thought of as a data reservoir that live data can be sent to. Hvplot can then connect to this Stream and update its plots when new data arrives.

Acknowledge that while data pipelines and buffers are very advanced subjects, the streamz library makes it very simple to create a use streamz with Pandas and hvplot.

Open the notebook and quickly show that hvplot has a special data streaming interface to the streamz library that can be imported:

```python
import os
import ccxt
import pandas as pd
import hvplot.streamz
from streamz import Stream
from streamz.dataframe import DataFrame
```

Use the first section of the notebook to demonstrate how to create a streaming DataFrame and plot the data with streamz and hvplot. Highlight the following points:

* The streamz library provides a [DataFrame-like interface](https://streamz.readthedocs.io/en/latest/dataframes.html) that can accept Stream and a example to form a streaming DataFrame.

  ```python
  stream = Stream()
  example = pd.DataFrame({"x": [], "y": []}, columns=["x", "y"], index=[])
  sdf = DataFrame(stream, example=example)
  ```

* The `example` in the above code is just a template for what the live data will look like. In this example, the live data will have `x` and `y` columns of data.

* A streaming DataFrame has limited functions similar to a real Pandas DataFrame, but it uses a Stream to hold live streaming data. A streaming DataFrame can be considered a wrapper around a normal DataFrame that hvplot can use to automatically update its plots with streaming data. In this example, hvplot will update its scatter plot whenever it receives new live data that matches the format of the `example` DataFrame.

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

* Even with 100 total emits, the backlog of 10 means that only the newest 10 datapoints are remembered.

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

* New data is fetched from the Kraken exchange via the CCXT API and processed as a new DataFrame `df` that matches the format of the `example` DataFrame. This new DataFrame is then emitted to the Stream and hvplot uses the streaming DataFrame to update the plot.

  ```python
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

**File:** [jarvis.py](Activities/09-Evr_Streaming_Dashboard/Solved/jarvis.py)

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

* The format for each `example` DataFrame can be worked out ahead of time using a normal DataFrame and jupyter notebook with historical data.

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

Show that the `generate_signals` function also needs modified slightly to convert the index to match the `example` DataFrame used in the initialize function.

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

### 13. Instructor Do: Reflect (10 min)

This activity will conclude today's lesson and provide a chance for students to reflect upon what they've learned throughout the day.

The purpose of this activity is to allow students a chance to take a step back and digest the concepts that have been taught today by engaging students in such a way that students drive the conversation, thereby reinforcing their learning by "teaching" the class.

Recap the skills and concepts learned throughout the lesson, and engage students by having them lead the discussion as much as possible:

* Ask if there are any students who would like to volunteer to summarize the any of the following concepts.

  * What is the purpose of an algorithmic trading framework? What does it look like?

    **Answer:** The purpose of an algorithmic trading framework is to abstract and encapsulate the code into easily modifiable functions. The result is a customizable, end-to-end implementation of robust and fully functional financial trading application.

  * What is the CCXT library and what does it do? Why is it a convenient library to have in terms of trading?

    **Answer:** The CCXT library is a Cryptocurrency Exchange Trading API that provides a common developer interface to many of the cryptocurrency exchanges.

  * What is the asyncio library? Why was it important for our algorithmic trading applications?

    **Answer:** The asyncio library is framework for writing asychronous code. Using asyncio in the trading framework allows the dashboard page to load while the data is fetched and updated asynchronously.

  * What is data persistence? Why is it important?

    **Answer:** Data persistence is the concept of storing or "persisting" data in a reliable location such as a database. It is often important for failure prevention/disaster recovery in the event that an application fails, meaning that an application can pick up where it last failed due to the most recent "save" point. In today's trading framework, it also allows us to offload some of the memory requirements to the database.

  * What is the streamz library? What benefit did it provide to our algorithmic trading application?

    **Answer:** The streamz library combined with hvplot allows streaming data visualizations for the dashboard, thereby mitigating the need to re-build the dashboard each time.

* Ask if there are any volunteers who would like to add anything that has not been previously stated.

Then, get students reflecting on what they've learned so far:

* Ask students how might they apply what they've learned so far in Unit 15. Will they go on to manage their own investments through automation?

* Ask students how they now feel regarding algorithmic trading (comfortable or uncomfortable?).

* Ask students to identify two potential things they'd like to practice more from today's lesson that they might have struggled with conceptually.

Finish the recap with a few statements of encouragement:

* Tell students they should give themselves another round of applause. Students now have the tools necessary to engage in live algorithmic trading!

* Remind students that should they choose, they can continue to build out their trading applications to make them even more robust and scalable. In particular, this will be especially impressive to potential employers as not many individuals have an algorithmic trading application under their belts!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
