### 3. Everyone Do: Algorithmic Trading Framework (15 mins)

In this activity, instructors will guide students on how to begin encapsulating their trading calculations into trading functions that can be used in an algorithmic trading framework. The purpose of this activity is to port the functionality that was achieved in the previous class into an end-to-end implementation of an algorithmic trading application.

**Files:** [ninja_trader.py](Activities/02-Evr_Algo_Trading_Framework/Solved/ninja_trader.py)

Quickly discuss the following before proceeding onward to the walk through:

* Now that students have completed their workflow design for their new algorithmic trading applications, it is now time to take what they've learned in the previous day and assemble the code together in a single framework/application.

* Students should keep in mind the concepts of inputs and outputs (I/O). This is because as data within the algorithmic trading application flows from start to finish, the underlying functions called therein will require inputs and return outputs according to their specific purposes.

Open the solution file and walk through the following with the class:

* In accordance with the workflow showcased in the previous activity, the trading framework executes the following progression: initialize the account and build the dashboard; fetch data and generate signals; backtest signal data and evaluate metrics; and update the dashboard.

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

* Going in order, the first function is the `initialize` function, which initiates an `account` dictionary and executes another function `initialize_dashboard` to produce a dashboard object representing a loading screen for the trading framework. 

  **Note**: Keep in mind that depending on the execution time of the trading application, users may not see the loading screen and instead with simply see the end result of the dashboard where financial metrics and visualizations are displayed.

  ```python
  def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize account
    account = {"balance": cash, "shares": 0}

    # Initialize dashboard
    dashboard = initialize_dashboard()

    return account, dashboard
  ```

  ```python
  def initialize_dashboard():
    """Build the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")

    return dashboard
  ```

* Next, the trading application executes the `fetch_data` function to read a CSV from a local file and returns a DataFrame containing historical stock data.

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

* After data has been fetched, the `generate_signal` function uses the DataFrame from the `fetch_data` function as its own input, generating a signal based off a dual moving average crossover strategy and returns a DataFrame containing signal data.

  ```python
  def generate_signal(data_df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10
    long_window = 20

    # Set up the signals DataFrame
    signals = data_df.copy()
    signals["date"] = pd.to_datetime(signals["date"], infer_datetime_format=True)
    signals = signals.set_index("date", drop=True)
    signals["signal"] = 0.0

    # Generate the short and long moving averages
    signals["SMA10"] = signals["close"].rolling(window=short_window).mean()
    signals["SMA20"] = signals["close"].rolling(window=long_window).mean()

    # Generate the trading signal 0 or 1,
    signals["signal"][short_window:] = np.where(
        signals["SMA10"][short_window:] > signals["SMA20"][short_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"] = signals["signal"].diff()

    # Print the DataFrame
    print(signals)

    return signals
  ```

* Using the DataFrame containing signal data, the `execute_backtest` function backtests the signal data and returns a DataFrame of running portfolio balances for a proposed initial capital allocation and share size.

  ```python
  def execute_backtest(signals_df):
    """Executes a backtest on trading signal data."""
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500

    # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
    signals_df['Position'] = share_size * signals_df['signal']

    # Find the points in time where a 500 share position is bought or sold
    signals_df['Entry/Exit Position'] = signals_df['Position'].diff()

    # Multiply share price by entry/exit positions and get the cumulatively sum
    signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()

    # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
    signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()

    # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
    signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']

    # Calculate the portfolio daily returns
    signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

    # Calculate the cumulative returns
    signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1

    # Print the DataFrame
    print(signals_df)

    return signals_df
  ```

* 

Ask if there are any questions before moving on.
