### 3. Everyone Do: Demystifying Algorithmic Trading (10 min)

The goal of this activity is to demystify algorithmic trading by showing a simplified trading strategy in code. While this particular strategy isn't something that anyone would actually want to trade with, it serves to show how a trading strategy can be written in code. The following lessons will build on this core concept using more realistic strategies.

**Files:** [simple_trading_algorithm.ipynb](Activities/01-Evr_Simple_Trading_Algorithm/Solved/simple_trading_algorithm.ipynb)

Open the solution file and discuss the following:

* Trading algorithms are often misconstrued to be highly complex and esoteric, left only for the quantitative analysts/traders of prominent big banks and hedge funds; however, when breaking down the core components of a trading algorithm, there are three fundamental parts: obtaining the data, making a trading decision, and evaluating the results.

* Oftentimes, stock data is provided from brokerage services than can be obtained via API calls. For this particular example, however, we've produced a hard-coded DataFrame consisting of 10 trading days worth of closing prices for AMD. The `bdate_range` function produces a datetime index using only "business day" datetime objects.

  ![amd-closing-prices-dataframe](Images/amd-closing-prices-dataframe.png)

* A trading algorithm can actually be as simple as a loop and a conditional. This trading strategy iterates through the data and compares the current price to the previous price to make a `buy`, `sell`, `hold` decision.

  ![simple-trading-algorithm](Images/simple-trading-algorithm.png)

* Trading algorithms often produce metrics on a per trade basis. We can modify our algorithm to track trade decisions and profit/loss.

  ![profit-loss-trading-algorithm](Images/profit-loss-trading-algorithm.png)

* It is important to evaluate the performance of a trading algorithm. Here we multiply the per share profit/loss by 1000 to simulate the performance of the trading algorithm if it were to execute its trades using a share size of 1000. Results show that the trading algorithm profited $3230, and produced a return on investment of 3.23% for an initial capital allocation of $100,000.

  ![simple-trading-algo-performance](Images/simple-trading-algo-performance.png)

End the discussion with the following:

* Explain that while this particular trading strategy wasn't actually very good, we will keep improving our strategies throughout the week until we have some very robust trading algorithms.

* Ask the class if they would actually use this particular trading strategy with their own money and why they would or wouldn't use it. Call for a few volunteers to provide their answers.

* Ask how they might formally evaluate the algorithm and then share some of the following ideas for evaluation: risk metrics such as sharp ratios, performing quantitative analysis, using data visualizations.

* Acknowledge that further analysis may show that this particular strategy may not be very good, but the beauty of algorithmic trading is that we can come up with any number of trading strategies, code it up, and test it out. Explain that throughout the week, we will learn how to improve on this model of obtaining data, making a trading decision, and evaluating the results.

Answer any questions before moving on.
