### 5. Instructor Do: Backtesting (10 mins)

In this activity, students will learn how to test the performance of an algorithmic trading strategy using historical stock data, a process otherwise known as backtesting. In particular, students will use historical stock data to measure the profit/loss of executed trades for a given trading strategy and visualize the overall change in portfolio value over time.

**Files:**

* [backtesting.ipynb](Activities/04-Ins_Backtesting/Solved/backtesting.ipynb)

First, present the following questions and answers:

* What is backtesting?

  **Answer:** Backtesting is the process for measuring the overall performance of a trading strategy using historical stock prices to simulate executed trades dictated by the calculated trading signals and trade decision logic.

* Why is backtesting important?

  **Answer:** Backtesting helps to assess the validity or profitability of a trading strategy over time and provides a benchmark for how it may perform going forward.

* How reliable is backtesting?

  **Answer:** While backtesting is important, the results of the backtest correspond to historical prices and not future prices. Therefore, backtesting may provide a reliable benchmark for the stock prices that have already occurred, but may prove to be less reliable as new stock data arises.

Next, open the solution file and present the following:

* Because backtesting requires an initial trading strategy, here we start off again with our Long Position Dual Moving Average Crossover strategy. Going forward, we will want to measure the performance of each trade (entry position followed by exit position) as well as the overall increase/decrease in a simulated portfolio value.

  ![strategy-to-backtest](Images/strategy-to-backtest.png)

* Oftentimes, backtesting is a functionality already provided by algorithmic trading frameworks such as Quantopian's `zipline` library; however, performing manual backtesting can be just as easy if we understand the steps. Notice the minimal lines of code to achieve this functionality!

  ![manual-backtesting](Images/manual-backtesting.png)

* First, we will want to set an initial capital allocation for our backtesting simulation. More often than not, an arbitrary value of $100,000 is chosen as the starting value.

  ```python
  # Set initial capital
  initial_capital = float(100000)
  ```

* Here, we create a new `Position` column by multiplying an arbitrarily chosen `share_size` of 500 shares and multiplying it by the values in the `Signal` column. As a result, periods of time in the dataset where there is an active signal of 1 will now show an active trade position of 500 shares for the backtesting simulation.

  ```python
  # Set the share size
  share_size = 500

  # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
  signals_df['Position'] = share_size * signals_df['Signal']
  ```

  ![active-positions](Images/active-positions.png)

* Similar to using the `diff` function on the `Signal` column to calculate entry and exit points, using the `diff` function on the `Position` column calculates the entry and exit points for the specified share size, in this case 500 shares. 

  ```python
  # Find the points in time where a 500 share position is bought or sold
  signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
  ```

  ![entry-exit-positions](Images/entry-exit-positions.png)

* In the next step, a new column `Portfolio Holdings` is created by multiplying the closing prices of AAPL by the cumulative sum for entry and exit positions of 500 shares--indicating the value of the investment made for each trade over time.

  ```python
  # Multiply share price by entry/exit positions and get the cumulatively sum
  signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()
  ```

  ![portfolio-holdings](Images/portfolio-holdings.png)

* Interestingly enough, at first glance the following code looks like it should have parentheses around the product of closing prices and entry/exit share size positions; however, doing so causes the calculated portfolio holdings to remain static, and is therefore erroneous.

  ```python
  # Multiply share price by entry/exit positions and get the cumulatively sum
  signals_df['Portfolio Holdings'] = (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![erroneous-portoflio-holdings.png](Images/erroneous-portfolio-holdings.png)

* Next, another new column `Portfolio Cash` is created by subtracting the initial capital allocation of $100,000 by the product of APPL closing prices and entry/exit share size positions--indicating the remaining cash value of the simulated portfolio relative to the performance of trades over time. Notice that now parenthesis are used around the product of AAPL closing prices and entry/exit share size positions.

  ```python
  # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
  signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![portfolio-cash](Images/portfolio-cash.png)

*

Ask if there are any questions before moving on.
