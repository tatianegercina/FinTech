### 3. Everyone Do: Algorithmic Trading Framework (15 mins)

In this activity, students will code along with the instructor and port over their previous algorithmic trading code into the new algorithmic trading framework.

**Files:**

* [component_code.ipynb](Activities/02-Evr_Algo_Trading_Framework/Solved/component_code.ipynb)

* [ninja_trader_v2.py](Activities/02-Evr_Algo_Trading_Framework/Solved/ninjatrader_v2.py)

Quickly discuss the following before proceeding onward to the walk through:

* Now that students have completed their workflow design for their new algorithmic trading applications, it is now time to take what they've learned in the previous day and assemble the code together in a single framework/application.

Open the Jupyter Notebook with the original source code to be ported and highlight the following points:

* Jupyter naturally provides a method of chunking code into cells which can make the code more readable and reusable. 

* In programming, a better practice is to chunk code together into functions. This provides a layer of abstraction that makes the code easier to modify and reuse. 

* Ask students what code cells might be good candidates for different functions in the trading framework.

* Ask students to open the trading framework starter code in Vscode or Jupyter and follow along as you start to port over the original code into the algorithmic trading framework. 

* Ask students which code functions might belong in the initialize function. Start to copy code from the original source file into the trading framework starter for the initialize function. Be sure to explain that initializing accounts or data containers are all good candidates for the initialize function. 

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

Next, code the solution for the fetch_data function. Be sure to prompt students to guide you through the solution to keep the class engaged. 

* Explain that while they could potentially read the CSV file in the initialize function, the goal is to abstract the code for fetching data into a function so that any data or API can be used. 

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

* Explain that the `generate_signal` function in the framework can be used to generate trading signals. Again, abstracting this code into its own function will make it easier to code up new signal generators later. The goal of the framework is to encapsulate each chunk of code so that it is easier to change later. 

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

* Show students that they can also grab the backtesting code and place it into its own function.

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

* The `evaluate_metrics` function then takes the backtested signal data and calculates the corresponding portfolio and per-trade metrics.

  ```python
  def evaluate_metrics(signals_df):
    """Evaluates metrics from backtested signal data"""
    #### CALCULATE PORTFOLIO METRICS ####
    # Initialize index and columns
    metrics= ['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Alpha', 'Beta']
    columns = ['Backtest']

    # Initialize the DataFrame with index set to evaluation metrics and column as `Backtest` (just like PyFolio)
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

    # Assign evaluation metric values from backtest results
    portfolio_evaluation_df.loc['Cumulative Returns'] = signals_df['Portfolio Cumulative Returns'][-1]

    # Calculate annualized return
    portfolio_evaluation_df.loc['Annual Return'] = ((1 + signals_df['Portfolio Daily Returns'].mean())**252 - 1)

    # Calculate annual volatility
    portfolio_evaluation_df.loc['Annual Volatility'] = ((1 + signals_df['Portfolio Daily Returns'].std())** 252 - 1)

    # Calculate Sharpe Ratio
    portfolio_evaluation_df.loc['Sharpe Ratio'] = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))

    # Calculate Sortino Ratio
    sortino_ratio_df = signals_df[['Portfolio Daily Returns']]
    sortino_ratio_df['Downside Returns'] = 0
    target = 0
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
    down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
    expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()
    sortino_ratio = expected_return/down_stdev
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio

    # Print the DataFrame
    print(portfolio_evaluation_df)

    #### CALCULATE TRADE METRICS ####
    trade_evaluation_df = pd.DataFrame(
        columns=[
            'Stock',
            'Entry Date',
            'Exit Date',
            'Shares',
            'Entry Share Price',
            'Exit Share Price',
            'Entry Portfolio Holding',
            'Exit Portfolio Holding',
            'Profit/Loss'
        ]
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
                {
                    'Stock': 'AAPL',
                    'Entry Date': entry_date,
                    'Exit Date': exit_date,
                    'Shares': share_size,
                    'Entry Share Price': entry_share_price,
                    'Exit Share Price': exit_share_price,
                    'Entry Portfolio Holding': entry_portfolio_holding,
                    'Exit Portfolio Holding': exit_portfolio_holding,
                    'Profit/Loss': profit_loss
                },
                ignore_index=True)

    # Print the DataFrame
    print(trade_evaluation_df)

    return portfolio_evaluation_df, trade_evaluation_df
  ```

* Finally, show that we can also encapsulate the code for updating the dashboard. This will make it easier to update the dashboard later at whatever frequency we want. Explain that we often want to update the dashboard when new data arrives and/or at a specific time interval (seconds, minutes, hours, days, etc).

  ```python
  def update_dashboard(account, tested_signals_df, portfolio_evaluation_df, trade_evaluation_df):
    """Updates the dashboard with widgets, plots, and financial tables"""
    # Initialize static widgets
    account_balance = pn.widgets.StaticText(name="Cash Balance", value=tested_signals_df['Portfolio Cash'][-1])
    holding_value = pn.widgets.StaticText(name="Portfolio Holding", value=tested_signals_df['Portfolio Holdings'][-1])
    total_portfolio_value = pn.widgets.StaticText(name="Total Portfolio Value", value=tested_signals_df['Portfolio Total'][-1])

    # Create price plot of closing, SMA10, and SMA20
    price_plot = tested_signals_df.hvplot.line(x='date', y=['close', 'SMA10', 'SMA20'], value_label='Price', width=1000, height=400, rot=90)

    # Create portfolio metrics table
    portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(columns=['index', 'Backtest'], width=300, height=400)

    # Create trade metrics table
    trade_evaluation_table = trade_evaluation_df.hvplot.table(
        columns=[
            'Stock',
            'Entry Date',
            'Exit Date',
            'Shares',
            'Entry Share Price',
            'Exit Share Price',
            'Entry Portfolio Holding',
            'Exit Portfolio Holding',
            'Profit/Loss'
        ]
    )

    # Create rows
    row_one = pn.Row(account_balance, holding_value, total_portfolio_value)
    row_two = pn.Row(price_plot)
    row_three = pn.Row(portfolio_evaluation_table, trade_evaluation_table)

    # Create columns
    column = pn.Column(row_one,
                       row_two,
                       row_three)

    # Create tabs
    tabs = pn.Tabs(("Summary", column))

    # Assign tab to dashboard object
    dashboard[0] = tabs

    return
  ```

Ask if there are any questions before moving on.
