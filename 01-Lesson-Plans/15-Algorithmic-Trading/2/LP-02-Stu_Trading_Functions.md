### 2. Student Do: Trading Functions (10 mins)

In this activity, students will be given a random sequence of trading function names and will be asked to propose the correct order of the functions if they were to be implemented in an algorithmic trading application.

**Files:**

* [Instructions](Activities/01-Stu_Trading_Functions/README.md)

* [Solution](Activities/01-Stu_Trading_Functions/Solved/ninjatrader_v1.py)

Open the slides and explain the following to students:

* Before designing an algorithmic trading framework, students need to first determine the order or workflow of the individual functions that constitute the holistic operation of the framework. Therefore, in this case, students will need to decide what is the proper order for a random sequence of trading functions if they were to be implemented in an algorithmic trading application.

* Doing this exercise helps students to mentally map out the process required for an end-to-end algorithmic trading application and should reinforce the importance of the core algorithmic trading concepts taught in day 1.

Then, slack out the instructions and review the solution when ready:

* The correct order of the trading functions is as follows: first set up the necessary data structures and dashboard objects, obtain the financial data, generate signals from such financial data, backtest the signal data, execute the trade strategy, evaluate the results of the trade strategy, update the dashboard, and wrap all the component functions into a single main event loop.

  ```python
  def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    return

  def build_dashboard():
      """Build the dashboard."""
      return

  def fetch_data():
      """Fetches the latest prices."""
      return

  def generate_signals():
      """Generates trading signals for a given dataset."""
      return

  def execute_backtest():
      """Backtests signal data."""
      return

  def execute_trade_strategy():
      """Makes a buy/sell/hold decision."""
      return

  def evaluate_metrics():
      """Generates evaluation metrics from backtested signal data."""
      return

  def update_dashboard():
      """Updates the dashboard."""
      return

  def main():
      """Main Event Loop."""
      return
  ```

Ask any questions before moving on.
