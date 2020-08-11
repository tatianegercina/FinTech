## 15.2 Lesson Plan: Egad! It's Alive!

---

### Overview

Today's class will expand upon students' component knowledge of algorithmic trading and abstract one level higher to create a full-fledged trading framework encapsulated in a single application. In particular, students will learn how to wrap their previous code (data collection, signal generation, backtesting, evaluation, and dashboard creation) into functions that will be called via a single workflow. In other words, students will automate the manual component calculations done in the previous class to produce an end-to-end trading dashboard containing all relevant metrics and functionality.

Students will learn how to "go live" with their trading frameworks by establishing a connection to a financial trading API, such as the Kraken or Bitfinex Cryptocurrency Exchange API, which both provide 24-hour market access and generous API request privileges.

### Class Objectives

By the end of class, students will be able to:

* Design an end-to-end workflow for a trading framework (data collection > signal generation > backtesting > evaluation > dashboard creation).

* Abstract their previous day's algorithmic trading calculations into functions and execute an end-to-end implementation of a working trading framework.

* Utilize live financial data by connecting their trading frameworks to the Kraken or Bitfinex Cryptocurrency Exchange API.

* Perform asynchronous tasks and loops using asyncio.

* Implement asyncio with their trading frameworks to fetch data and update the dashboard in parallel.

### Instructor Notes

* Today's lesson will tie together the concepts and coding solutions from the previous day into a single robust trading framework that can produce an end-to-end implementation of a trading dashboard with working metrics.

* This lesson will primarily focus on developing the *infrastructure* of the trading framework and, therefore, will not contain as much domain-specific trading knowledge.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [15.2 Lesson Slides](https://docs.google.com/presentation/d/1j96VQ9ZJF1O6N1hIXBzGu65yHNxvBshk3Ev8mPZbhNM/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to file, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to file and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [15.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ca743d57-d2a0-43eb-a7e6-aafe00f8d9cc) Note that this video may not reflect the most recent lesson plan.

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

  **Answer:** Metrics that showcase information such as the overall portfolio or per-trade performance. Examples include cash balance, total portfolio value, per-trade profits and losses, and dates of entry and exit trades.

* What is a trading dashboard?

  **Answer:** Like other dashboards, a *trading dashboard* consolidates and presents multiple facets of information about the performance of an algorithmic trading application, allowing a user to interact with the data via tables and plots (visualizations).

Then, create some excitement around the day by mentioning the following points:

* The goal of today's lesson is to take what students learned in day one and put the concepts together to build an end-to-end full-stack trading application that is capable of pulling financial data, generating signals, backtesting, executing a trading strategy, evaluating results, and generating dashboard visualizations in a single workflow.

* Creating a trading application from scratch should hopefully dispel the esoteric nature of developing algorithmic trading applications similar to those offered from commercial services, and allows for the ability to add additional features in the future, should students desire to do so.

* By the end of today's lesson, students should have a working trading application that they can demo to future employers, as well as use as the foundation for their custom trading application if they decide to further expand upon it.

Answer any questions before moving on.

---

### 2. Student Do: Trading Functions (10 min)

**Corresponding Activity:** [01-Stu_Trading_Functions](Activities/01-Stu_Trading_Functions)

In this activity, students will be given a random sequence of trading function names. They will be asked to propose the correct order of the functions if they were to be implemented in an algorithmic trading application. Note that there is not a single precise order, so treat this as a thought exercise to help drive engagement and discussion around the use of frameworks to encapsulate and abstract code.

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

* The true order of this solution may change once the code and behavior of each function are provided, but even without code, the call order will typically follow a pattern of initializing data containers, fetching data, transforming, or using the data, and displaying the data.

* By placing the call order in the main function, it can be easy to control and update the function call order in a single place in the program.

Ask any questions before moving on.

---

### 4. Everyone Do: Algorithmic Trading Framework (20 min)

**Corresponding Activity:** [02-Evr_Algo_Trading_Framework](Activities/02-Evr_Algo_Trading_Framework)

In this activity, students will code along with the instructor and port over their previous algorithmic trading code into the new algorithmic trading framework.

**Files:**

* [algorithmic_trading_code.ipynb](Activities/02-Evr_Algo_Trading_Framework/Resources/trading_dashboard.ipynb)

* [jarvis.py](Activities/02-Evr_Algo_Trading_Framework/Unsolved/jarvis.py)

Explain to students that the algorithmic trading code from the previous day can also be abstracted and ported over to the new trading framework. By abstracting the code, it makes it easier to change and adapt the algorithms and strategies used.

Open the Jupyter Notebook with the source code to be ported and highlight the following:

* Jupyter naturally provides a method of chunking code into cells, which can make the code more readable and reusable; in programming, a better practice is to chunk code together into functions. This provides a layer of abstraction that makes the code easier to modify and reuse.

Ask students what code cells might be good candidates for the different functions in the trading framework.

Then, ask students to open the starter code in VScode and follow along as you port the original code into the algorithmic trading framework.

Explain that we do not need to complete every function right now, but we can leave these as placeholders to expand later as the functionality of the code grows.

```python
def initialize():
    """Initialize the dashboard, data storage, and account balances."""
    # @TODO: We will complete this later!
    pass

def execute_trade_strategy():
    """Makes a buy/sell/hold decision."""
    # @TODO: We will complete this later!
    pass
```

Explain that we can abstract the data fetching portion of the code to make it easier to change the source of our data. In this example, we can fetch data from a local CSV file, but later, we can also change this to use another database or API.

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

Complete the `generate_signals` function and discuss the following points:

```python
def generate_signals(data_df):
    """Generates trading signals for a given dataset."""
    # Grab just the `date` and `close` from the dataset
    signals_df = data_df.loc[:, ["date", "close"]].copy()

    # Set the `date` column as the index
    signals_df = signals_df.set_index("date", drop=True)

    # Set the short window and long windows
    short_window = 50
    long_window = 100

    # Generate the short and long moving averages (50 and 100 days, respectively)
    signals_df["SMA50"] = signals_df["close"].rolling(window=short_window).mean()
    signals_df["SMA100"] = signals_df["close"].rolling(window=long_window).mean()
    signals_df["Signal"] = 0.0

    # Generate the trading signal 0 or 1,
    # where 0 is when the SMA50 is under the SMA100, and
    # where 1 is when the SMA50 is higher (or crosses over) the SMA100
    signals_df["Signal"][short_window:] = np.where(
        signals_df["SMA50"][short_window:] > signals_df["SMA100"][short_window:],
        1.0,
        0.0,
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals_df["Entry/Exit"] = signals_df["Signal"].diff()

    return signals_df
```

* It is helpful to encapsulate all of the signal generation into a single function. Signal generation may occur separately from the data fetching process, depending on the interval or amount of data needed to generate the signals. For example, in a live trading scenario, you may need to fetch a single record of data multiple times before there is enough data to generate the signals. Separating these functions makes it easier to manage that process.

Prompt students to help complete the `execute_backtest` and `evaluate_metrics` sections and explain the following:

* Backtesting and evaluating a trading algorithm is sometimes used only in the initial design of an algorithmic trading system. Therefore, it is helpful to separate these into their own functions.

* Backtesting may also be done outside of the trading framework as a separate function. By encapsulating backtesting into a function, it can be added or removed as needed.

Next, complete the `build_dashboard` function and discuss the following:

```python
def build_dashboard(signals_df, portfolio_evaluation_df):
    """Build the dashboard."""
    # Create hvplot visualizations
    price_df = signals_df[["close", "SMA50", "SMA100"]]
    price_chart = price_df.hvplot.line().opts(xaxis=None)
    portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(
        columns=["index", "Backtest"]
    )

    # Build the dashboard
    dashboard = pn.Column(
        "# Trading Dashboard", price_chart, portfolio_evaluation_table
    )
    return dashboard
```

* Similar to the backtesting section, the actual dashboard used in an algorithmic trading platform may be different when backtesting and when live trading. By encapsulating the code into this function, any number of dashboard changes can be made and adapted over time.

Finally, code the `main` function and highlight the following:

```python
def main():
    """Main Event Loop."""
    data_df = fetch_data()
    signals_df = generate_signals(data_df)
    tested_signals_df = execute_backtest(signals_df)
    portfolio_evaluation_df = evaluate_metrics(tested_signals_df)
    dashboard = build_dashboard(tested_signals_df, portfolio_evaluation_df)
    dashboard.servable()
    return


main()
```

* The `main` function is the heart of the framework. This function controls the flow of data through the framework.

* The sequence/function call order of the framework may change and adapt over time, but by collecting these in a single function, it makes it easy to see how the elements of the framework are connected.

As a final recap of this activity, explain to students that abstraction and encapsulation are techniques that every good programmer uses to make their code more readable and reusable. Striving to write code in this manner will make it easier to share code, and it shows a level of programming self-mastery that senior developers will recognize.

Explain that the next several activities will continue to build and iterate on the trading framework until everyone has a live algorithmic trading application working that can be used for real trading!

---

### 5. Instructor Do: Trading with CCXT (15 min)

**Corresponding Activity:** [03-Ins_Going_Live](Activities/03-Ins_Going_Live)

In this section, students will become familiar with the expansive CCXT library, which provides an API for over 120 cryptocurrency exchanges. In particular, students will work with the Kraken or Bitfinex API and extract both historical and current price data.

**File:** [ccxt_demo.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt_demo.ipynb)

Open the solution file and review the following:

* CCXT provides a common API for over 120 cryptocurrency exchanges.

* To use a specific exchange, the API keys for that exchange must be set. In this example, the Kraken exchange is used and requires those keys to be exported before running the notebook. If you are ever having problems with kraken requests not going through you can also leverage the bitfinex API as a drop-in alterative.

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

* The Kraken exchange requires a list of markets and trading symbols to be loaded to use the API functions. This can be done manually using the `load_markets` function or implicitly upon the first call to the API.

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

  **Note:** The following functions return minimal/empty datasets due to the fact that the Kraken account used in this lesson is not funded with capital. The same would be true for using another API such as Bitfinex.

  ![additional-functions](Images/additional-functions.png)

Answer any remaining questions before moving on.

---

### 6. Everyone Do: Going Live with CCXT (15 min)

**Corresponding Activity:** [04-Evr_Going_Live](Activities/04-Evr_Going_Live)

In this activity, students will code along with the instructor to update a version of the algorithmic trading framework to use the Kraken or Bitfinex exchange from the CCXT API.

**File:**

* [jarvis.py](Activities/04-Evr_Going_Live/Unsolved/jarvis.py)

Live code the solution to this activity with the entire class. Use the code to explain new concepts to students, and engage the class with questions when appropriate. Be sure to go slow and give students plenty of time to keep up.

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

* A conditional statement is used to make sure there is enough data to generate a signal for the strategy before calling those functions. In this case, the strategy uses a 20-day window for the moving average crossover, so we want a minimum of 20 data points before we generate signals.

Move to the `initialize` function definition and highlight the following points:

```python
def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Initializing Account and DataFrame")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize dataframe
    df = fetch_data()

    # @TODO: We will complete the rest of this later!
    return account, df
```

* The initialize function is used to create all of the initial variables and data containers that the function may need. By initializing all of the functions in a single function, it makes it easy to update and change the initial values or data types used.

* The account balance is a simple Python dictionary to keep track of the cash balance and the number of shares owned.

* The `df` DataFrame is initialized using the `fetch_data` function.

Move to the `fetch_data` function and prompt the class to help complete the function definition. Highlight the following points:

```python
def fetch_data():
    """Fetches the latest prices."""
    print("Fetching data...")
    load_dotenv()
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

Explain that the beauty of a robust application framework is that the abstraction and encapsulation of code make it easy to make additional changes. Explain that the remainder of the class will be used to iterate and improve on this platform to make it even better!

---

### 7. Instructor Do: Asyncio (10 min)

**Corresponding Activity:** [05-Ins_Asyncio](Activities/05-Ins_Asyncio)

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

* The `fetch_data` function simulates a data fetch that takes a long time. In practice, any request to an external API may take a long time to fetch and return the data.

* The serve_dashboard function serves up a simple dashboard of text.

* Python is a synchronous language. That means that it runs one line of code and waits on that code to finish before moving on to run the next line of code. In this example, the `fetch_data` function takes 5 seconds to run before the code that serves the dashboard can run. This effectively blocks the page from loading until the data returns.

* In practice, fetching data can take a lot longer than expected. Database queries, network delays, and other factors can create delays in the request. With code like this, the user experience suffers because the page cannot load until the data returns.

Open `asyncio_demo.ipynb` and highlight the following points about the asyncio library:

* Python provides a library called `asyncio` to write concurrent or asynchronous code.

* Asynchronous code means that Python doesn't have to wait on that line to finish running before moving on to the next line of code.

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

* The `async` keyword in the function definition tells asyncio that this function is something called a [coroutine](https://docs.python.org/3/glossary.html#term-coroutine). A coroutine is just code that can be executed differently (asynchronously) from the normal code.

* The `await` keyword indicates which line of code can be waited for asynchronously. This is what suspends the coroutine until this line of code finishes running. In other words, the sleep statement can run asynchronously while Python continues to run the remaining code in the program.

* Asyncio uses an event loop to run code asynchronously. The event loop can be thought of as a loop that sits off to the side and just periodically checks to see if the async code has finished running yet. When it does finish running, it can rejoin the main program. Meanwhile, Python is free to continue running other code.

* The asyncio provides several functions for using the event loop. This example runs the `fetch_data` function as a task in the event loop. It then immediately moves on to run the `serve_dashboard` code in the main program while fetch_data continues to run in the event loop. Once fetch_data finishes, it rejoins the main program.

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

### 8. BREAK (15 min)

---

### 9. Everyone Do: Async Trading (15 min)

**Corresponding Activity:** [06-Evr_Async_Trading](Activities/06-Evr_Async_Trading)

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

### 10. Instructor Do: Structured Review (1 hour)

Use this review time to touch base on any knowledge-gaps that the students may have. Feel free to utilize previous activities and homeworks for this purpose.

Suggested format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to work on homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### 11. Instructor Do: Reflect (15 min)

This activity will conclude today's lesson and provide a chance for students to reflect on what they've learned throughout the day.

The purpose of this activity is to allow students a chance to take a step back and digest the concepts that have been taught today by engaging students in such a way that students drive the conversation, thereby reinforcing their learning by "teaching" the class.

Recap the skills and concepts learned throughout the lesson, and engage students by having them lead the discussion as much as possible:

* Ask if any students would like to volunteer to summarize any of the following concepts.

  * What is the purpose of an algorithmic trading framework? What does it look like?

    **Answer:** The purpose of an algorithmic trading framework is to abstract and encapsulate the code into easily modifiable functions. The result is a customizable, end-to-end implementation of robust and fully functional financial trading application.

  * What is the CCXT library, and what does it do? Why is it a convenient library to have in terms of trading?

    **Answer:** The CCXT library is a Cryptocurrency Exchange Trading API that provides a common developer interface to many of the cryptocurrency exchanges.

  * What is the asyncio library? Why was it important for our algorithmic trading applications?

    **Answer:** The asyncio library is a framework for writing asynchronous code. Using asyncio in the trading framework allows the dashboard page to load while the data is fetched and updated asynchronously.

  * What is data persistence? Why is it important?

    **Answer:** Data persistence is the concept of storing or "persisting" data in a reliable location such as a database. It is often important for failure prevention/disaster recovery in the event that an application fails, meaning that an application can pick up where it last failed due to the most recent "save" point. In today's trading framework, it also allows us to offload some of the memory requirements to the database.

* Ask if any volunteers would like to add anything that has not been previously stated.

Then, get students reflecting on what they've learned so far:

* Ask students how might they apply what they've learned so far in Unit 15. Will they go on to manage their investments through automation?

* Ask students how they now feel regarding algorithmic trading (comfortable or uncomfortable?).

* Ask students to identify two potential things they'd like to practice more from today's lesson that they might have struggled with conceptually.

Finish the recap with a few statements of encouragement:

* Tell students they should give themselves another round of applause. Students now have the tools necessary to engage in live algorithmic trading!

* Remind students that should they choose, they can continue to build out their trading applications to make them even more robust and scalable. In particular, this will be especially impressive to potential employers as not many individuals have an algorithmic trading application under their belts!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
