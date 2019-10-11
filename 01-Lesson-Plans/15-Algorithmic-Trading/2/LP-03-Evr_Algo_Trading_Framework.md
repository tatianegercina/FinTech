### 3. Everyone Do: Algorithmic Trading Framework (15 mins)

In this activity, instructors will guide students on how to begin encapsulating their trading calculations into trading functions that can be used in an algorithmic trading framework. The purpose of this activity is to port the functionality that was achieved in the previous class into an end-to-end implementation of an algorithmic trading application.

**Files:** [ninja_trader.py](Activities/02-Evr_Algo_Trading_Framework/Solved/ninja_trader.py)

Quickly discuss the following before proceeding onward to the walk through:

* Now that students have completed their workflow design for their new algorithmic trading applications, it is now time to take what they've learned in the previous day and assemble the code together in a single framework/application.

* Students should keep in mind the concepts of inputs and outputs (I/O). This is because as data within the algorithmic trading application flows from start to finish, the underlying functions called therein will require inputs and return outputs according to their specific purposes.

Open the solution file and walk through the following with the class:

* In accordance with the workflow showcased in the previous activity, the trading framework executes the following progression: initialize the account and dashboard objects; fetch data and generate signals; backtest signal data and evaluate metrics; and build the dashboard.

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

Ask if there are any questions before moving on.
