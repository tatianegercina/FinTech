## 15.1 Lesson Plan: Algorithmic Trading

---

### Overview

Today's class will introduce students to **algorithmic trading** in Python. Traditional trading, or the manual purchase and sale of assets such as stocks, has begun to shift to more automated methods due to the advancements in network speed, computing power, and available financial trading APIs. Therefore, students will learn the fundamentals of algorithmic trading and deconstruct the process of producing a functional algorithmic trading model.

In particular, students will learn how to generate trading signals from raw data, backtest a trading strategy using such signals, produce evaluation metrics regarding overall portfolio and per-trade performance, and construct a trading dashboard similar to commercial online trading platforms. By the end of this unit, students will also incorporate machine learning to automate and improve portfolio management and trade performance for maximum profitability with minimal risk.

### Class Objectives

By the end of class, students will be able to:

* Delineate what algorithmic trading is, how it came to be, and why it's valuable.

* Deconstruct the process for algorithmic trading: obtaining the data, making a trading decision, and evaluating the results.

* Compare the differences between technical analysis and fundamental analysis.

* Define what a trading signal is, how it is used, and why it's important.

* Construct a dual moving average crossover trading signal.

* Define what backtesting is, how it is used, and why it's important.

* Backtest or validate a dual moving average crossover strategy with a capital allocation of $100,000.

* Quantify evaluation metrics on overall portfolio and per-trade performance.

* Build a trading dashboard to visualize the multiple components of algorithmic trading.

### Instructor Notes

* Today's lesson will consist of elements taught in the Pandas and PyViz units; the lesson will include data analysis, utilization of trading APIs for asset pricing data, and the visualization of trading performance and transaction analysis using a Panel dashboard.

* The goal of this unit is to educate students on trading, as well as how to use code to automate trading. Trading may be new for many students, so it is important that adequate information is provided regarding what trading is and all of the steps involved in creating entry and exit strategies, as well as which FinTech APIs integrate well with Python for automated trading.

* Not everyone will have a background in trading, so be thorough when explaining specific trading terminology, concepts, and strategies. Instead of painting the entire picture for students, focus on the individual steps required to execute a trade, and then apply coding concepts (i.e., iterations) to illustrate how the step can be automated using Python code. Definitions for key trading terminology will be provided.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1yKec68KGLenYiTEn3f8yUx3v230WCA6zdfbEcHmzNLU/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker.xlsx](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (10 min)

In this activity, students are introduced to what algorithmic trading is and why it's useful for FinTech professionals. In particular, this section is a key opportunity to build excitement about creating a process to automate trades, evaluate risk, and simplify participation in the market through the execution of a single program.

Welcome students to the first day of algorithmic trading and explain the following:

* Introduce students to algorithmic trading first by describing how cumbersome it can be to make trades manually. Explain that a typical day for traders involves:

  * Tracking the transactional history of many stocks.

  * Identifying the best opportunity to buy, sell, and hold.

  * Maintaining knowledge about the highs and lows for each individual stock, as well as their overall portfolio value and profit/loss.

  * Keeping emotions in check.

* Also explain that human emotions play a key role in the success or failure of a trade/trader. Because the market is constantly changing with varying degrees of volatility, it's easy for humans to get emotional when trading. The trades that traders make can drastically impact their profitability and livelihood. Furthermore, because traders often deal with other people's money, such as retirement funds, impulsive trading decisions can have the ability to disrupt the economic foundation of countless lives.

* The sheer number of moving parts and details that need to be considered can make it difficult for the human mind to make profitable trades consistently. This is where **algorithmic trading** comes in.

* Algorithmic trading is the concept of utilizing machines to automate the process of buying and selling assets. Machines running algorithms can make predictions about ROI, risk, and analyze transactions much faster than a human brain. Because computers run off of logic rather than emotions, traders don't have to worry about their emotions getting in the way.

  * Underscore to students that there are many different algorithmic trading strategies, even ones that can leverage machine learning. Also, an algorithm does not necessarily have to evaluate the basis of a candidate trade in the same way: algorithms can be used to predict the best investments based on profit-to-risk ratios, volume, and volatility, or any number of varying attributes.

* Using algorithmic trading models in conjunction with portfolio management also allows for automatic rebalancing of assets (capital) within the portfolio, thereby aiding in portfolio optimization. Algorithmic trading models automatically buy and sell assets within the portfolio according to the optimal weights for each asset calculated by the model.

* If time remains, summarize to students that all **algorithmic trading** involves is the execution of specific trading actions based on specific criteria, such as the ratio of profit-to-risk for the given scenario. In this regard, all a human has to do is click a button to execute the algorithm.

* Lastly, if there is time, explain to students that the use of algorithmic trading has given certain firms a competitive advantage compared to those still using manual, human labor. They're able to make smarter, more agile decisions based on real-time predictions and historical analysis, not to mention that less time is wasted on implementing and repeating manual processes.

Answer any questions before moving on.

---

### 2. Instructor Do: Intro to Algorithmic Trading (10 mins)

In this activity, students will learn the basics of what algorithmic trading is and how it came to be, how it is performed, and what kind of individuals and skillsets are required for potential participants looking to break into the field.

Navigate to the slideshow and present the following questions and answers about algorithmic trading:

* What is algorithmic trading?

  **Answer:** Algorithmic trading is simply using code to decide and execute a trade (buy/sell). For example, a simple algorithm could be to sell 100 shares of a stock when the intraday percentage return of a stock falls below -3%.

* Why is algorithmic trading so prevalent today?

  **Answer:** Advances in network technology and computing power, along with access to financial trading APIs, have made it possible for anyone to write code and automate their trading strategies. The result is that algorithmic trading can be orders of magnitude faster and more efficient than humans performing traditional trading.

* Why use algorithmic trading?

  **Answer:** While there are many benefits to using algorithmic trading over traditional/manual trading, the two main benefits are: one, algorithmic trading can be backtested using historical and real-time data to see if it is a profitable trading strategy and, two, it reduces the possibility of human error in which traders mistime trades based on emotional and psychological factors.

* Who performs algorithmic trading?

  **Answer:** Anyone that can code can create their own algorithmic trading bot. Traditionally, Quantitative analysts or quant traders create algorithmic trading models and are often required to have at least a master's or Ph.D. degree level with a familiar background in statistics. However, with human-friendly programming languages like Python, analytical tools, and machine learning libraries, anyone can learn to build a very powerful algorithmic trader.

Ask if there are any questions before moving on.

---

### 3. Everyone Do: Demystifying Algorithmic Trading (10 min)

The goal of this activity is to demystify algorithmic trading by showing a simplified trading strategy in code. While this particular strategy isn't something that anyone would want to trade with, it serves to show how a trading strategy can be written in code. The following lessons will build on this core concept using more realistic strategies.

**Files:** [simple_trading_algorithm.ipynb](Activities/01-Evr_Simple_Trading_Algorithm/Solved/simple_trading_algorithm.ipynb)

Open the solution file and discuss the following:

* Trading algorithms are often misconstrued to be highly complex and esoteric, left only for the quantitative analysts/traders of prominent big banks and hedge funds; however, when breaking down the core components of a trading algorithm, there are three fundamental parts: obtaining the data, making a trading decision, and evaluating the results.

* Often, stock data is provided from brokerage services than can be obtained via API calls. For this particular example, however, we've produced a hard-coded DataFrame consisting of 10 trading days worth of closing prices for AMD. The `bdate_range` function produces a datetime index using only "business day" datetime objects.

  ![amd-closing-prices-dataframe](Images/amd-closing-prices-dataframe.png)

* A trading algorithm can be as simple as a loop and a conditional. This trading strategy iterates through the data and compares the current price to the previous price to make a `buy`, `sell`, `hold` decision.

  ![simple-trading-algorithm](Images/simple-trading-algorithm.png)

* Trading algorithms often produce metrics on a per-trade basis. We can modify our algorithm to track trade decisions and profit/loss.

  ![profit-loss-trading-algorithm](Images/profit-loss-trading-algorithm.png)

* It is important to evaluate the performance of a trading algorithm. Here we multiply the per-share profit/loss by 1000 to simulate the performance of the trading algorithm if it were to execute its trades using a share size of 1000. Results show that the trading algorithm profited $3230, and produced a return on investment of 3.23% for an initial capital allocation of $100,000.

  ![simple-trading-algo-performance](Images/simple-trading-algo-performance.png)

End the discussion with the following:

* Ask the class if they would use this particular trading strategy with their own money and why they would or wouldn't use it. Call for a few volunteers to provide their answers.

* Ask how they might formally evaluate the algorithm and then share some of the following ideas for evaluation: risk metrics such as sharp ratios, performing quantitative analysis, using data visualizations.

* Acknowledge that further analysis may show that this particular strategy may not be very good, but the beauty of algorithmic trading is that we can come up with any number of trading strategies, code it up, and test it out. Explain that throughout the week, we will learn how to improve on this model of obtaining data, making a trading decision, and evaluating the results.

Answer any questions before moving on.

---

### 4. Instructor Do: Trading Signals (10 mins)

In this activity, students will learn what differentiates technical analysis from fundamental analysis, what a technical indicator is, what trading signals are, and how to use these signals to devise a trading strategy (actions based on the occurrence of a trading signal). In particular, students will learn how to generate a dual moving average crossover trading signal, implement the logic/strategy to perform the buy or sell orders, and overlay the points at which the algorithm places the buy and sell orders on top of the plot for closing prices of AAPL stock.

**Files:** [dual_ma_crossover.ipynb](Activities/02-Ins_Trading_Signals/Solved/dual_ma_crossover.ipynb)

Navigate to the trading signals section of the slides, and highlight the following:

* Technical analysis is an (often) short-term trading discipline in which investments (such as stocks) are evaluated based on their price action or movement.

* Fundamental analysis is an investment discipline in which investments (such as stocks) are evaluated based on their intrinsic qualities such as financial (income statement, balance sheet, and cash flow statement) or economic data about the underlying company.

Engage students by asking if anyone has any guesses or knowledge of what the following terms are. Make sure to communicate to students that they are not expected to have the answers yet.

* What is a technical indicator?

  **Answer:** Falling under the umbrella of technical analysis, a technical indicator is a data-driven metric that uses trading data such as closing price and volume to analyze the short or long-term price movements occurring over a specified period. For example, a 20-day simple moving average is a technical indicator representing a rolling 20-day mean of a stock's closing prices.

* What is a trading signal?

  **Answer:** A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

Transition to explaining to students how technical indicators and trading signals are used in practice, particularly as it relates to the dual moving average crossover trading strategy.

* Emphasize to students that technical indicators and trading signals are used when implementing trading strategies. The goal of a trading signal is to identify opportunities to get ahead of the trend.

  * An example trading strategy is the dual moving average crossover strategy, which leverages two types of simple moving averages (short term and long term) in order to flag when an investment should be bought or sold.

    * Use this as an opportunity to remind students that moving averages are calculated using historical quote data. Moving averages are just the average security price over/for a given time period.

* Explain the difference between short term and long term moving averages. Highlight that short term moving average and long term moving averages both track the average price of a security over time; however, long term moving averages are tracked with a greater window than short term.

* Underscore that short term and long term moving averages, when plotted, will travel in the same direction. At some point, they will cross. The value at the time of the crossover is considered the crossover point. Crossover points are a type of technical indicator.

  * If the STMA goes above the LTMA, it is understood that the security price will be rising in the short term, higher than the historical average for that period.

  * If the STMA goes below the LTMA, it is understood that the security price will be dropping in the short term, less than the historical average for that period.

* Indicate to students that once technical indicators are available, actual trading strategies can be used to approach buying and selling strategies. Trading signals determine these strategies.

Elaborate on the role of trading signals in placing trades. Emphasize how buy and sell decisions are determined.

* Explain that when a short window moving average (ex. 50-day MA) crosses over a long window moving average (ex. 100-day MA) and continues to be greater than the long window moving average, then:

  * The technical indicator would suggest that the underlying stock price will rise in the short-term. The trading signal would signal to buy.

* Ask students the following: if **dual moving average crossover** is used, what would be the trading signal for the following scenario:

  * The short window moving average crosses under a long window moving average and continues to be less than the long window moving average (stock will fall in the short-term).

  * **Answer** The signal would be to issue a sell order. Sell orders would be issued at the points in which the short window moving average crosses under the long window moving average.

Open the solution file and highlight the following points:

* By default, a Pandas DataFrame shows a limited number of rows and columns in order to conserve screen space (ex. the `...`); however, because we'll need to see the specific points at which a trading signal is active and the corresponding trade entry and exit points, it is a good idea to increase the Pandas DataFrame display size to show all of it's contents.

  ![dataframe-options](Images/dataframe-options.png)

* When working with dual moving averages, one of the key components is the duration of the short and long term windows. Data needs to be sampled using the Pandas `rolling` function for these particular time periods. Once data is sampled for both short term and long term windows, the average can be calculated (using close price).

    ```python
    short_window = 50
    long_window = 100
    signals_df['SMA50'] = signals_df['close'].rolling(window=short_window).mean()
    signals_df['SMA100'] = signals_df['close'].rolling(window=long_window).mean()
    ```

* After the averages have been identified, logic has to be defined to return an active/inactive trade signal 1 or -1 when the short MA crosses above/under the long MA. and calculating the points at which the entry or exit position should be made 1 or -1.

  ![dual-ma-signal](Images/dual-ma-signal.png)

* The `where` function can be used to define the logic for when to buy and sell.

  * When a short moving average is greater than the long moving average, the technical indicator will have a value of 1, for sell.

  * When a short moving average is less than the long moving average, the technical indicator is a value of 0, for buy.

  * These values are assigned to data points starting from an offset equal to the length of the short moving average window, as moving average calculations will be null before that point (not enough data points to perform the rolling mean calculation).

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

* By plotting entry/exit positions, security closing price, and the moving averages, each entry/exit position can be visualized in relationship to close price.

  ```python
  # Visualize exit position relative to close price
  exit = signals_df[signals_df['Entry/Exit'] == -1.0]['close'].hvplot.scatter(
      color='red',
      legend=False,
      ylabel='Price in $',
      width=1000,
      height=400
  )

  # Visualize entry position relative to close price
  entry = signals_df[signals_df['Entry/Exit'] == 1.0]['close'].hvplot.scatter(
      color='green',
      legend=False,
      ylabel='Price in $',
      width=1000,
      height=400
  )

  # Visualize close price for the investment
  security_close = signals_df[['close']].hvplot(
      line_color='lightgray',
      ylabel='Price in $',
      width=1000,
      height=400
  )

  # Visualize moving averages
  moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
      ylabel='Price in $',
      width=1000,
      height=400
  )

  # Overlay plots
  entry_exit_plot = security_close * moving_avgs * entry * exit
  entry_exit_plot
  ```

  ![trading-strategy-visual](Images/trading-strategy-visual.gif)

Ask if there are any questions before moving on.

---

### 5. Student Do: The Big Short (15 mins)

In this activity, students will take what they've learned about generating trading signals and implementing a corresponding trading strategy, and instead now perform the inverse: create a trading strategy that profits off of price declines by shorting (selling) and covering (buying) the stock.

**Files:**

* [the_big_short.ipynb](Activities/03-Stu_Trading_Signals/Unsolved/the_big_short.ipynb)

* [vnq.csv](Activities/03-Stu_Trading_Signals/Resources/vnq.csv)

**Instructions:** [README.md](Activities/03-Stu_Trading_Signals/README.md)

---

### 6. Instructor Do: The Big Short Review (10 mins)

**File:** [the_big_short.ipynb](Activities/03-Stu_Trading_Signals/Solved/the_big_short.ipynb)

Take a moment to explain that generating a short position dual moving average crossover trading signal involves:

* Calculating a short window rolling moving average and a long window rolling moving average of closing prices.

* Defining logic for an active trade signal as 1 when the short MA crosses under the long MA and 0 when the short MA crosses above the long MA.

* Calculating the points at which an entry or exit position should be made using 1 or -1.

Open the solution file and review the following:

* The first step in identifying entry/exit positions is to create a rolling window for moving averages. This can be done using the Pandas `rolling` function.

    ```python
    # Set the short window and long windows
    short_window = 50
    long_window = 100

    # Generate the short and long moving averages (50 and 100 days, respectively)
    signals_df['SMA50'] = signals_df['Close'].rolling(window=short_window).mean()
    signals_df['SMA100'] = signals_df['Close'].rolling(window=long_window).mean()
    ```

* Similar to a long position dual moving average crossover trading signal, the `where` function can be used to define the logic for a short position trading strategy. The goal of this strategy would be to short the market by selling high once the short moving average dips below the long moving average (to buy later at a lower rate).

  * When a short moving average is less than the long moving average, issue a value of 1.
  * When a short moving average is greater than the long moving average, issue a value of 0.

  * Values are assigned to data points starting from an offset equal to the length of the short moving average window, as moving average calculations will be null before that point (not enough data points to perform the rolling mean calculation).

    ```python
    # Generate the trading signal 0 or 1,
    # where 0 is when the SMA50 is under the SMA100, and
    # where 1 is when the SMA50 is higher (or crosses over) the SMA100
    signals_df['Signal'][short_window:] = np.where(
        signals_df['SMA50'][short_window:] < signals_df['SMA100'][short_window:],
        1.0,
        0.0)
    ```

    ![short-dual-ma-crossover](Images/short-dual-ma-crossover.png)

* The `diff` function calculates the difference in active vs. non-active trading periods suggested by the short position trading signal, 1 or 0. Therefore, values defined for specific entry and exit points become 1 or -1.

    ```python
    # Calculate the points in time at which a position should be taken, 1 or -1
    signals_df['Entry/Exit'] = signals_df['Signal'].diff()
    ```

    ![short-entry.png](Images/short-entry.png)

    ![short-exit.png](Images/short-exit.png)

* Plotting the closing prices of VNQ, a 50-day moving average, and a 100-day moving average overlaid with marker symbols indicating short position entry and exit trades shows that an algorithm utilizing a short position dual moving average crossover strategy during the 2008 recession would have **made** money rather than **lose** money like most other investors during that time.

  ![short-dual-ma-crossover-plot](Images/short-dual-ma-crossover-plot.png)

---

### 7. Instructor Do: Backtesting (10 mins)

In this activity, students will learn how to test the performance of an algorithmic trading strategy using historical stock data, a process otherwise known as backtesting. In particular, students will use historical stock data to measure the profit/loss of executed trades for a given trading strategy and visualize the overall change in portfolio value over time.

**Files:** [backtesting.ipynb](Activities/04-Ins_Backtesting/Solved/backtesting.ipynb)

First, present the following discussion points and use the questions below to elicit student engagement:

* Backtesting is the process for measuring the overall performance of a trading strategy using historical stock prices to simulate executed trades dictated by the calculated trading signals and trade decision logic.

* Ask students to guess why backtesting is important?

  **Answer:** Backtesting helps to assess the validity or profitability of a trading strategy over time and provides a benchmark for how it may perform going forward.

* Underscore to students that while backtesting is important, the results of the backtest correspond to historical prices and not future prices. Therefore, backtesting may provide a reliable benchmark for the stock prices that have already occurred but may prove to be less reliable as new stock data arises.

Next, open the solution file and present the following:

* Because backtesting requires an initial trading strategy, here we start again with our Long Position Dual Moving Average Crossover strategy. Going forward, we will want to measure the performance of each trade (entry position followed by an exit position) as well as the overall increase/decrease in simulated portfolio value.

  ![strategy-to-backtest](Images/strategy-to-backtest.png)

  ![strategy-to-backtest-plot](Images/strategy-to-backtest-plot.png)

* Backtesting is commonly implemented using third party libraries; however, performing manual backtesting can be just as easy if we understand the steps. Notice the minimal lines of code to achieve this functionality!

  ![manual-backtesting](Images/manual-backtesting.png)

Walk students through each step required to implement manual backtesting. Highlight the following:

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

* Similar to using the `diff` function on the `Signal` column to calculate entry and exit points, using the `diff` function on the `Position` column calculates the entry and exit points for the specified share size, in this case, 500 shares.

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

* Interestingly enough, at first glance, the following code looks like it should have parentheses around the product of closing prices and entry/exit share size positions; however, doing so causes the calculated portfolio holdings to remain static, and is therefore erroneous.

  ```python
  # Multiply share price by entry/exit positions and get the cumulatively sum
  signals_df['Portfolio Holdings'] = (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![erroneous-portoflio-holdings.png](Images/erroneous-portfolio-holdings.png)

* Next, another new column `Portfolio Cash` is created by subtracting the initial capital allocation of $100,000 by the product of APPL closing prices and entry/exit share size positions--indicating the remaining cash value of the simulated portfolio relative to the performance of trades over time. Notice that now, parentheses are used around the product of AAPL closing prices and entry/exit share size positions when calculating the remaining portfolio cash. This is because while the investment value of each trade changes over time, the *cost-basis* of each trade remains the same.

  ```python
  # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
  signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![portfolio-cash](Images/portfolio-cash.png)

* The `Portfolio Total` column adds the values of the `Portfolio Cash` columns by the values of the `Portfolio Holdings` columns, indicating the total portfolio value given the performance of trades over time.

  ```python
  # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
  signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
  ```

  ![portfolio-total](Images/portfolio-total.png)

* The `Portfolio Daily Returns` and the `Portfolio Cumulative Returns` are calculated using the `pct_change` and `cumprod` functions respectively, as done in the previous units of this course.

  ```python
  # Calculate the portfolio daily returns
  signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

  # Calculate the cumulative returns
  signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
  ```

  ![portfolio-daily-and-cumulative-returns](Images/portfolio-daily-and-cumulative-returns.png)

* Finally, once again using the `hvplot` library, we can plot the entry and exit positions of the backtesting results of a simulated portfolio of $100,000. Results show that the trading strategy increased the simulated portfolio of $100,000 to slightly above $130,000.

  ![backtest-code](Images/backtest-code.png)

  ![backtest-results-plot](Images/backtest-results-plot.png)

Ask if there are any questions before moving on.

---

### 8. Student Do: The Big Short Part II (15 mins)

In this activity, students will now take the Short Position Dual Moving Average Crossover trading strategy they made in the previous student activity and now run a backtest to quantify the performance of their trading strategy.

**Files:**

* [the_big_short.ipynb](Activities/05-Stu_Backtesting/Unsolved/the_big_short_part_2.ipynb)

* [vnq.csv](Activities/05-Stu_Backtesting/Resources/vnq.csv)

**Instructions:** [README.md](Activities/05-Stu_Backtesting/README.md)

---

### 9. Instructor Do: The Big Short Part II Review (10 mins)

**File:** [the_big_short.ipynb](Activities/05-Stu_Backtesting/Solved/the_big_short_part_2.ipynb)

Open the solution file and review the following:

* The plot of the Short Position Dual Moving Average Crossover trading strategy showed that it was possible to *make* money from shorting VNQ (a real estate ETF) stock during the financial recession in 2008. Now, through backtesting the particular strategy, we will be able to see *how much* money can be made.

  ![short-dual-ma-crossover-code2](Images/short-dual-ma-crossover-code2.png)

  ![short-dual-ma-crossover-plot2](Images/short-dual-ma-crossover-plot2.png)

* Because short positions involve selling shares and then buying them back later, the `share_size` should be a negative number rather than a positive number.

  ```python
  share_size = -500
  ```

* As a result of the negative `share_size` number, the following calculations show that an active share size position will be defined as -500, and that entry and exit positions in the short trading strategy will involve selling shares (a negative number) followed by purchasing shares (a positive number).

  ```python
  # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
  signals_df['Position'] = share_size * signals_df['Signal']

  # Find the points in time where a 500 share position is bought or sold
  signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
  ```

  ![short-dual-ma-backtesting-positions](Images/short-dual-ma-backtesting-positions.png)

* The calculations for portfolio holdings and show that as the stock price decreases, the value of the portfolio holdings increase (become less negative).

  ```python
  # Multiply share price by entry/exit positions and get the cumulatively sum
  signals_df['Portfolio Holdings'] = signals_df['Close'] * signals_df['Entry/Exit Position'].cumsum()
  ```

  ![short-portfolio-holdings](Images/short-portfolio-holdings.png)

* When shorting a stock, it is beneficial to sell the stock at a high price and buy (or cover as they say in the industry) the shares at a low price, resulting in a positive differential. This is why the portfolio cash increases when the algorithm shorts VNQ stock at a high and covers the shares at a low.

  ```python
  # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
  signals_df['Portfolio Cash'] = initial_capital - (signals_df['Close'] * signals_df['Entry/Exit Position']).cumsum()
  ```

  ![short-portfolio-cash](Images/short-portfolio-cash.png)

* After calculating the portfolio holdings and portfolio cash, calculating the total portfolio value is as simple as adding the portfolio holdings and portfolio cash together.

  ```python
  # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
  signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
  ```

  ![short-portfolio-total](Images/short-portfolio-total.png)

* The portfolio's daily returns can then be calculated using the `pct_change` function on the total portfolio value, while the portfolio's cumulative returns can then be calculated using the resulting portfolio daily returns and the `cumprod` function.

  ```python
  # Calculate the portfolio daily returns
  signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

  # Calculate the cumulative returns
  signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
  ```

  ![short-portfolio-returns](Images/short-portfolio-returns.png)

* Finally, plotting the Short Position Dual Moving Average crossover trading strategy against its backtesting results show that the algorithm would have *made* money by shorting VNQ stock during the 2008 financial crisis and by approximately $6,500 on an initial capital allocation of $100,000. Specifically, the ending portfolio value for the algorithm was $106,587.2295, and results in cumulative returns of 6.5872%.

  ![short-backtest-results-code](Images/short-backtest-results-code.png)

  ![short-backtest-results-plot](Images/short-backtest-results-plot.png)

---

### 10. BREAK (15 min)

---

### 11. Instructor Do: Evaluation Metrics (10 min)

Students will receive a dry walkthrough of the various evaluation metrics that can be used to evaluate their trading algorithms, namely portfolio and trade-related evaluation metrics. This will include revisiting metrics such as cumulative returns and Sharpe ratios, as well as new metrics such as the Sortino ratio. The instructor will explain how the metrics are calculated and how they are used.

**Files:** [trading_algorithm_evaluation.ipynb](Activities/06-Ins_Evaluations/Solved/trading_algorithm_evaluation.ipynb)

Navigate to the **evaluation** slide of the Unit 15.1 slideshow. Communicate the following:

* Evaluating the performance of a portfolio is of utmost importance, regardless if it is a human or an algorithm making trades. The following metrics can be used to evaluate a portfolio.

  * **Cumulative Return**- the total/aggregated amount of gains and losses for an investment. Cumulative return is measured across time and not for a given time period.

  * **Annual Return**- a time-weighted annual percentage representing the return on an investment over a period of time.

  * **Annual Volatility**- the annualized degree of variation in trading prices over time.

  * **Sharpe Ratio**- The return of investment compared to its risk, measured by the difference between the return on investment and the risk-free return.

  * **Downside Deviation/Return**- The measure of risk for returns that are below the minimum acceptable return.

  * **Sortino Ratio**-  The quotient of harmful volatility and overall volatility. The Sortino ratio focuses on downside deviation rather than the standard deviation.

* These metrics can be calculated for a portfolio through historical backtesting, or they can be used to measure the performances of specific securities before engaging in a trade.

Transition to a dry walkthrough of the code used to calculate each of these metrics. Open the solution and highlight the following:

* One of the advantages of using an algorithm for trading is that evaluation metrics can be calculated using the algorithm as well. This allows for each metric to be calculated within seconds. Having an algorithm calculate the evaluation metrics diminishes the chances of human error and improves the overall accuracy and time it takes to evaluate a portfolio/security/trade comprehensively.

* Point out to students the code to calculate cumulative returns.

  ```python
  cum_returns = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
  ```

* Show students the code to calculate annual returns. Highlight that when calculating annual returns, the average of daily return has to be calculated first, and then that value can be multiplied by the number of trading days within a year to derive an annualized value.

  **Note:** Sometimes it is more appropriate to use the formula for Compound Annual Growth Rate (CAGR) to account for compounding effects when dealing with investments over long durations of time. To get a better feel for what this means, visit the illustrative excel spreadsheet [here](../Supplemental/Simple_vs_Compound_Returns.xlsx)

  ```python
  annual_returns = signals_df['Portfolio Daily Returns'].mean() * 252
  ```

* Explain the code to calculate annual volatility. Emphasize that annual volatility involves calculating the standard deviation for each daily return. The standard deviation is then annualized by multiplying by the number of trading days in the year.

  ```python
  annual_volatility = signals_df['Portfolio Daily Returns'].std() * 252
  ```

* Ask students if anyone remembers how to calculate a Sharpe ratio.

  **Answer** Calculate the annual average daily return and then divide that by the standard deviation of daily returns. The standard deviation of daily returns will need to be multiplied by the square root of the number of trading days.

  ```python
  sharpe_ratio = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))
  ```

* Indicate that the downside returns or downside deviation metric is calculated by squaring daily returns less than 0.

  ```python
  sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
  ```

* Sortino ratios are calculated using the downside return. Sortino ratios are calculated by dividing the average daily return by the square root of the average downside return.

  ```python
  down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
  expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()

  sortino_ratio = expected_return/down_stdev
  portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio
  ```

  ![evluation_metrics.png](Images/evluation_metrics.png)

* Emphasize to students that they should dedicate time outside of class to conduct research on each individual metric to better understand how it can be applied to assess portfolio performance.

* Per-trade evaluation metrics can also be calculated by iterating over the DataFrame containing backtested signal data and grabbing related entry and exit trade values. Also, the profit for each trade can be calculated by finding the difference between the exit portfolio holding and the entry portfolio holding values. Each entry-exit trade record is then appended to the trade evaluation DataFrame.

  ![per-trade-evaluation-code](Images/per-trade-evaluation-code.png)

  ![per-trade-evaluation-dataframe](Images/per-trade-evaluation-dataframe.png)

If time remains, finish the walkthrough by reminding students that even when trading with an algorithm, trades and portfolios need to be evaluated. Algorithms are not infallible. Touch upon the following:

* Algorithms have to be tweaked and fine-tuned over time, especially as trading strategies evolve or are replaced. Because a machine will be handling the trading process, the algorithm must have metrics to use that will help measure performance, detect and mitigate risk, and track trends in returns on the fly.

* Evaluation metrics are also important for traders to have available, even if a machine is doing all of the trading and calculations. By analyzing evaluation metrics, humans can spot nuances in the data that the algorithm might not have been programmed/trained to detect. This could lead to new features for the algorithm, as well as an increased investment opportunity for the trader.

Ask if there are any questions before moving forward.

---

### 12. Students Do: The Big Short Part III (15 mins)

Now that students have developed a Short Dual Moving Average trading strategy and backtested their strategy against historical VNQ prices, students can now calculate the portfolio and trade evaluation metrics to ascertain the performance of their short strategy.

**Instructions:** [README.md](Activities/07-Stu_Evaluations/README.md)

**Files:** [the_big_short_part_3.ipynb](Activities/07-Stu_Evaluations/Unsolved/the_big_short_part_3.ipynb)

---

### 13. Instructor Do: The Big Short Part III Review (10 mins)

**Files:**

* [the_big_short_part_3.ipynb](Activities/07-Stu_Evaluations/Solved/the_big_short_part_3.ipynb)

Open the solution and explain the following:

* Portfolio evaluation metrics should be used to gauge algorithm performance. Commonly used metrics include cumulative returns, annualized returns, annual volatility, Sharpe ratio, and Sortino ratio.

  ![portfolio-evaluation-metrics.png](Images/portfolio-evaluation-metrics.png)

* Remind students that even though algorithms can perform more effectively and efficiently than humans (without emotional or mental fatigue), algorithms still need to be evaluated for performance. This will ensure the algorithm is trading with the most optimal configurations.

* Explain that the common practice is to have the algorithm calculate and monitor evaluation metrics to help make decisions regarding when to buy and sell. This removes the need for manual calculations, and it also provides the opportunity for the evaluation metrics to be tracked in real-time as stock prices fluctuate and trades are executed.

* Per-trade evaluation metrics show a more granular approach to assessing the performance of the overall portfolio. Previously, it was shown that the short strategy increased the initial capital allocation from $100,000 to $106,587.2295; by looking at the per-trade evaluation metrics, we can see how each trade propelled the total portfolio value to the ending value of $106,587.2295.

  ![per-trade-evaluation-code](Images/per-trade-evaluation-code2.png)

  ![per-trade-evaluation-dataframe](Images/per-trade-evaluation-dataframe2.png)

Dedicate the remaining time to student questions. Encourage students to ask any questions regarding the different evaluation metrics, how they're used, or why they are used.

* Pull up the [evaluations calculation guide](../Supplemental/EvaluationsCalculationGuide.md) as an anchor for the question session. This will give students the ability to call out specific aspects of the metrics that may be confusing or unclear.

Ask for any remaining questions before moving on.

---

### 14. Everyone Do: Trading Dashboard (15 min)

In this activity, instructors will walk students through creating a trading dashboard with Panel using the evaluation metrics generated from prior activities. At this point, students should already have exposure to creating dashboards using Panel.

The purpose of this activity is to show students how to create a trading dashboard using the already shown (Unit 6) Panel dashboard library. In particular, students will once again define rows, columns, and tabs, as well as serve the trading dashboard as an actual web application.

**Files:** [trading_dashboard.ipynb](Activities/08-Ins_Trading_Dashboard/Solved/trading_dashboard.ipynb)

Before moving onto the walkthrough, quickly review the following:

* What is Panel?

  **Answer:** Panel is a high-level dashboarding library that allows a user to create custom interactive web apps and dashboards by connecting user-defined widgets, plots, images, tables, or text. Also, Panel works with other visualization libraries such as Plotly Express or Hvplot via extensions.

* What is a dashboard?

  **Answer:** A dashboard is an information management tool that organizes, stores, and displays important information from multiple data sources into one, easy-to-access place.

* Why use a dashboard?

  **Answer:** Having a single interactive interface for key information and visualizations allows a user to monitor the health of an existing process, business function, or application, and therefore aids in measuring performance and identifying any discrepancies that may arise.

Open the solution file and highlight the following:

* Make sure to import the necessary libraries and dependencies to use the Panel dashboard and Hvplot visualizations. The `pn.extension()` function automatically detects the need for Panel to load additional extensions; in this case, Panel will load the extension for Hvplot.

  ```python
  import panel as pn
  import hvplot
  import hvplot.pandas
  pn.extension()
  ```

* Before creating the Panel dashboard, we will need first to define the visualizations that will be shown. Therefore, using the DataFrames containing evaluation metrics generated from previous activities, we can create interactive hvplot tables that allow for sorting of columns (ascending or descending) and row selection (selecting one or multiple rows).

  ![hvplot-price-chart](Images/hvplot-price-chart.png)

  ![hvplot-evaluation-metrics](Images/hvplot-evaluation-metrics.png)

* After generating the visualizations that will be added to the Panel dashboard, the next step is to assign the visualizations as rows, columns, and tabs to the Panel dashboard using the Panel `Row`, `Column`, and `Tabs` functions.

  ```python
  # Create rows
  price_chart_row = pn.Row(price_chart)
  portfolio_evaluation_row = pn.Row(portfolio_evaluation_table)
  trade_evaluation_row = pn.Row(trade_evaluation_table)

  # Create columns
  portfolio_column = pn.Column('# Portfolio Evaluation Metrics', price_chart_row, portfolio_evaluation_row)
  trade_column = pn.Column('# Trade Evaluation Metrics', trade_evaluation_row)

  # Create tabs
  trading_dashboard = pn.Tabs(
      ("Portfolio Metrics", portfolio_column),
      ("Trade Metrics", trade_column)
  )
  ```

* Lastly, the `servable` function then serves or initializes the dashboard. There are two ways to use the `servable` function, either in a Jupyter notebook file where the dashboard is displayed within the notebook file itself, or using the terminal command `panel serve --show trading_dashboard.ipynb` which creates a web application of the dashboard via the default localhost port 5006.

  ![panel-trading-dashboard-servable](Images/panel-trading-dashboard-servable.png)

  ![panel-trading-dashboard-servable-localhost](Images/panel-trading-dashboard-servable-localhost.png)

Ask if there are any questions before moving forward.

---

### 15. Instructor Do: Reflect (15 min)

This activity will conclude today's lesson on Algorithmic Trading Day 1 and provide a chance for students to reflect upon what they've learned throughout the day.

The purpose of this activity is to allow students a chance to take a step back and digest the concepts that have been taught today by engaging students in such a way that students drive the conversation, thereby reinforcing their learning by "teaching" the class.

Recap the skills and concepts learned throughout the lesson, and engage students by having them lead the discussion as much as possible:

* Ask if any students would like to volunteer to summarize any of the following concepts.

  * What is algorithmic trading? What does the process entail?

  * What are trading signals?

  * What is backtesting? Why is it important?

  * What kinds of portfolio evaluation metrics exist?

  * What kinds of trade evaluation metrics exist?

* Ask if any volunteers would like to anything that has not been previously stated.

Finish the recap with a few statements of encouragement:

* Tell students they should give themselves a round of applause. They are on their way to becoming their own investment fund managers!

* Remind students that by learning how to trade algorithmically, they are now already way ahead of those who only know how to invest manually. Therefore, they now have the tools to do both and can choose which method they prefer, either algorithmically, manually or a hybrid of both.

* The next step is to create an algorithmic trading framework on Day 2, in which students will take what they've learned today to create a full-fledged trading application that they can use in real-world scenarios. Students should be pumped for this!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
