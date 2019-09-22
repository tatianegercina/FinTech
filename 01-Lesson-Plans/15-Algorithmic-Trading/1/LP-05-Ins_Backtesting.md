### 5. Instructor Do: Backtesting (10 mins)

In this activity, students will learn what differentiates technical analysis from fundamental analysis, what a technical indicator is, what trading signals are, and how to use these signals to devise a trading strategy (actions based on the occurrence of a trading signal). In particular, students will learn how to generate a dual moving average crossover trading signal, implement the logic/strategy to perform the buy or sell orders, and overlay the points at which the algorithm places the buy and sell orders on top of the plot for closing prices of AAPL stock.

**Files:**

* [dual_ma_crossover.ipynb](Activities/02-Ins_Trading_Signals/Solved/dual_ma_crossover.ipynb)

First, present the following questions and answers:

* What is technical analysis?

  **Answer:** Technical analysis is an (often) short-term trading discipline in which investments (such as stocks) are evaluated on the basis of their price action or movement. In contrast, fundamental analysis is an investment discipline in which investments (such as stocks) are evaluated on the basis of their intrinsic qualities such as financial (income statement, balance sheet, and cash flow statement) or economic data pertaining to the underlying company.

* What is a technical indicator?

  **Answer:** Falling under the umbrella of technical analysis, a technical indicator is a data-driven metric that uses trading data such as closing price and volume to analyze the short or long-term price movements occurring over a specified period of time. For example, a 20-day simple moving average is technical indicator representing a rolling 20-day mean of a stock's closing prices.

* What is a trading signal?

  **Answer:** A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security such as a stock at that point in time.

* What is a dual moving average crossover trading strategy?

  **Answer:** A dual moving average crossover is the point at which a short window moving average and a long window moving average cross paths. In particular, when a short window moving average (ex. 50-day MA) crosses over a long window moving average (ex. 100-day MA) and continues to be greater than the long window moving average, then it suggests that the underlying stock price will rise in the short-term. Conversely, when a short window moving average crosses under a long window moving average and continues to be less than the long window moving average, then it suggests that the underlying stock price will fall in the short-term. Therefore, a trading strategy using a dual moving average crossover would issue buy orders at the points in which the short window moving average crosses over the long window moving average, and sell orders at the points in which the short window moving average crosses under the long window moving average.

Next, open the solution file and present the following:

* By default, a Pandas DataFrame shows a limited number of rows and columns in order to conserve screen space (ex. the `...`); however, because we'll need to see the specific points at which a trading signal is active and the corresponding trade entry and exit points, it is a good idea to increase the Pandas DataFrame display size to show all of it's contents.

  ![dataframe-options](Images/dataframe-options.png)

* Generating a dual moving average crossover trading signal involves calculating a short rolling window moving average and a long rolling window moving average of closing prices, defining logic for an active/inactive trade signal 1 or -1 when the short MA crosses above/under the long MA, and calculating the points at which a entry or exit position should be made 1 or -1.

  ![dual-ma-signal](Images/dual-ma-signal.png)

* The `where` function defines the logic that when a short moving average is greater than the long moving average, issue a value of 1; when a short moving average is less than the long moving average, issue a value of 0. Values are assigned to data points starting from an offset equal to the length of the short moving average window, as moving average calculations will be null prior to that point (not enough data points to perform the rolling mean calculation).

  ```python
  signals_df['Signal'][short_window:] = np.where(signals_df['SMA50'][short_window:] > signals_df['SMA100'][short_window:], 1.0, 0.0)
  ```

* The `diff` function calculates the difference in active vs. non-active trading periods suggested by the trading signal, 1 or 0. Therefore, values defined for specific entry and exit points become 1 or -1.

  ![entry](Images/entry.png)

  ![exit](Images/exit.png)

* Using the matplotlib library, it is possible to mark the coordinates at which entry (buy) and exit (sell) orders should be made. The `figure` object handles the figure layout and size and the `axes` object handles plotting coordinates on the x and y axes. In this example, coordinates are plotted with green `^` and red `v` marker symbols.

  ![trading-strategy-visual](Images/trading-strategy-visual.png)

Ask if there are any questions before moving on.
