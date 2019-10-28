### 4. Instructor Do: Trading Signals (10 mins)

In this activity, students will learn what differentiates technical analysis from fundamental analysis, what a technical indicator is, what trading signals are, and how to use these signals to devise a trading strategy (actions based on the occurrence of a trading signal). In particular, students will learn how to generate a dual moving average crossover trading signal, implement the logic/strategy to perform the buy or sell orders, and overlay the points at which the algorithm places the buy and sell orders on top of the plot for closing prices of AAPL stock.

**Files:** [dual_ma_crossover.ipynb](Activities/02-Ins_Trading_Signals/Solved/dual_ma_crossover.ipynb)

Navigate to the 15.1 trading signals section of the slides, and highlight the following:

* Explain to students that technical analysis is an (often) short-term trading discipline in which investments (such as stocks) are evaluated on the basis of their price action or movement.

* Contrast technical analysis with fundamental analysis by explaining that fundamental analysis is an investment discipline in which investments (such as stocks) are evaluated on the basis of their intrinsic qualities such as financial (income statement, balance sheet, and cash flow statement) or economic data pertaining to the underlying company.

Engage students by asking if anyone has any guesses or knowledge of what the following terms are. Make sure to communicate to students that they are not not expected to have the answers yet.

* What is a technical indicator?

  **Answer:** Falling under the umbrella of technical analysis, a technical indicator is a data-driven metric that uses trading data such as closing price and volume to analyze the short or long-term price movements occurring over a specified period of time. For example, a 20-day simple moving average is technical indicator representing a rolling 20-day mean of a stock's closing prices.

* What is a trading signal?

  **Answer:** A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

Transition to explaining to students how technical indicators and trading signal are used in practice, particularly as it relates to the dual moving average crossover trading strategy.

* Emphasize to students that technical indicators and trading signals are used when implementing trading strategies. The goal of a trading signal is to identify opportunities to get ahead of the trend.

  * An example trading strategy is the dual moving average crossover strategy, which leverages two types of simple moving averages (short term and long term) in order to flag when an investment should be bought or sold.

    * Use this as an opportunity to remind students that moving averages are calculated using historical quote data. Moving averages are just the average security price over/for a given time period.

* Explain the difference between short term and long term moving averages. Highlight that short term moving average sand long term moving averages both track the average price of a security over time; however, long term moving averages are tracked with a greater window than short term.

* Underscore that short term and long term moving averages, when plotted, will travel in the same direction. At some point, they will cross. The value at the time of the crossover is considered the crossover point. Crossover points are a type of technical indicator.

  * If the STMA goes above the LTMA, it is understood that the security price will be rising in the short term, greater than the historical average for that time period.

  * If the STMA goes below the LTMA, it is understood that the security price will be dropping in the short term, less than the historical average for that time period.

* Indicate to students that once technical indicators are available, actual trading strategies can be used to approach buying and selling strategies. These strategies are determined by trading signals.

Elaborate on the role of trading signals in placing trades. Emphasize how buy and sell decisions are determined.

* Explain that when a short window moving average (ex. 50-day MA) crosses over a long window moving average (ex. 100-day MA) and continues to be greater than the long window moving average, then:

  * The technical indicator would suggest that the underlying stock price will rise in the short-term. The trading signal would signal to buy.

* Ask students the following: if **dual moving average crossover** is used, what would be the trading signal for the following scenario:

  * The short window moving average crosses under a long window moving average and continues to be less than the long window moving average (stock will fall in the short-term).

  * **Answer** The signal would be to issue a sell order. Sell orders would be issued at the points in which the short window moving average crosses under the long window moving average.

Open the solution file and provide a dry walk through following:

* By default, a Pandas DataFrame shows a limited number of rows and columns in order to conserve screen space (ex. the `...`); however, because we'll need to see the specific points at which a trading signal is active and the corresponding trade entry and exit points, it is a good idea to increase the Pandas DataFrame display size to show all of it's contents.

  ![dataframe-options](Images/dataframe-options.png)

* When working with dual moving averages, one of the key components is the duration or the short and long term windows. Data needs to be sampled using the Pandas `rolling` function for these particular time periods. Once data is sampled for both short term and long term windows, the average can be calculated (using close price).

    ```python
    short_window = 50
    long_window = 100
    signals_df['SMA50'] = signals_df['close'].rolling(window=short_window).mean()
    signals_df['SMA100'] = signals_df['close'].rolling(window=long_window).mean()
    ```

* After the averages have been identified, logic has to be defined to return an active/inactive trade signal 1 or -1 when the short MA crosses above/under the long MA. and calculating the points at which a entry or exit position should be made 1 or -1.

  ![dual-ma-signal](Images/dual-ma-signal.png)

* The `where` function can be used to define the logic for when to buy and sell.

  * When a short moving average is greater than the long moving average, the technical indicator will have a value of 1, for sell.

  * When a short moving average is less than the long moving average, the technical indicator be a value of 0, for buy.

  * These values are assigned to data points starting from an offset equal to the length of the short moving average window, as moving average calculations will be null prior to that point (not enough data points to perform the rolling mean calculation).

  ```python
  # Generate the trading signal 0 or 1,
  # where 0 is when the SMA50 is under the SMA100, and
  # where 1 is when the SMA50 is higher (or crosses over) the SMA100
  signals_df['Signal'][short_window:] = np.where(
      signals_df['SMA50'][short_window:] > signals_df['SMA100'][short_window:],
      1.0,
      0.0
  )
  ```

* The `diff` function is used to calculate the difference in active vs. non-active trading periods suggested by the trading signal, 1 or 0. The output from the `diff` function represents the specific entry and exit points for when a position should be taken (1 or -1).

    ```python
    # Calculate the points in time at which a position should be taken, 1 or -1
    signals_df['Entry/Exit'] = signals_df['Signal'].diff()
    ```

  ![entry](Images/entry.png)

  ![exit](Images/exit.png)

* By plotting entry/exit positions, security close price, and the moving averages, each entry/exit position can be visualized in relationship to close price.

    ```python
    # Visualize exit position relative to close price
    exit = signals_df[signals_df['Entry/Exit'] == -1.0]['close'].hvplot.scatter(
        color='red',
        legend=False,
        ylabel='Price in $',
        width=1000,
        height=400)

    # Visualize entry position relative to close price
    entry = signals_df[signals_df['Entry/Exit'] == 1.0]['close'].hvplot.scatter(
        color='green',
        legend=False,
        ylabel='Price in $',
        width=1000,
        height=400)

    # Visualize close price for the investment
    security_close = signals_df[['close']].hvplot(
        line_color='lightgray',
        ylabel='Price in $',
        width=1000,
        height=400)

    # Visualize moving averages
    moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
        ylabel='Price in $',
        width=1000,
        height=400)

    # Overlay plots
    entry_exit_plot = security_close * moving_avgs * entry * exit
    entry_exit_plot
    ```

  ![trading-strategy-visual](Images/trading-strategy-visual.gif)

Ask if there are any questions before moving on.
