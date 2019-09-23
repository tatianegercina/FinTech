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

* 

Ask if there are any questions before moving on.
