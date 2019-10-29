### 3. Everyone Do: Algorithmic Trading Framework (15 mins)

In this activity, students will code along with the instructor and port over their previous algorithmic trading code into the new algorithmic trading framework.

**Files:**

* [algorithmic_trading_code.ipynb](Activities/02-Evr_Algo_Trading_Framework/Solved/algorithmic_trading_code.ipynb)

* [jarvis_v2.py](Activities/02-Evr_Algo_Trading_Framework/Solved/jarvis_v2.py)

* [jarvis_v1.py](Activities/02-Evr_Algo_Trading_Framework/Unsolved/jarvis_v1.py)

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

* Lastly, the `main` function wraps the rest of the functions in a single workflow--allowing the application to perform a single call of the `main` function to then kick off the totality of the framework.

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

Ask if there are any questions before moving on.
