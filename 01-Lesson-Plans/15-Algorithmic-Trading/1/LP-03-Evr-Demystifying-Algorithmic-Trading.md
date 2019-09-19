### 3. Everyone Do: Demystifying Algorithmic Trading (10 min)

In this activity, instructors will walk students through the mindset and steps of developing a basic trading algorithm. While the trading strategy of this particular example may not be effective at scale, the purpose of this activity is to show that the complexity associated with a trading algorithm more so derives from the sophistication of the particular trading strategy (how to handle stock data and initiate buy/sell/hold decision logic) rather than the actual steps to produce and execute a trading algorithm, which can be very simple.

**Files:**

* [basic_trading_algorithm.ipynb](Activities/01-Evr_Basic_Trading_Algorithm/Solved/basic_trading_algorithm.ipynb)

Open the solution file and discuss the following:

* Trading algorithms are often misconstrued to be highly complex and esoteric, left only for the quantitative analysts/traders of prominent big banks and hedge funds; however, when breaking down the core components of a trading algorithm, there are three fundamental parts: obtaining the data, handling the data, and initiating the decision logic to buy, sell, or hold.

* Oftentimes, stock data is provided from brokerage services than can be obtained via API calls. For this particular example, however, we've produced a hard-coded DataFrame consisting of 10 trading days worth of closing prices for AMD. The `bdate_range` function produces a datetime index using only "business day" datetime objects.

  ![amd-closing-prices-dataframe](Images/amd-closing-prices-dataframe.png)

* As can be seen, a trading algorithm can be much simpler than we thought! Here we can see the handling of data and the decision logic for the trading algorithm, namely the looping of data using the for loop and the conditional statements defining the actions to buy, sell, or hold. This particular trading strategy performs a "buy low, sell high" strategy in which a buy order is made when the current day price is less than the previous day, a sell order is made when the current day price is greater than the previous day, and a hold is made when the current day price is equal to the previous day.

  ![simple-trading-algorithm](Images/simple-trading-algorithm.png)

* Trading algorithms often produce metrics on a per trade basis. Thus, in order to emulate the same effect in our simple trading algorithm, only a few changes are required--such as implementing containers for buy and sell orders to record the stock prices of the buy-sell trading pairs.

  ![profit-loss-trading-algorithm](Images/profit-loss-trading-algorithm.png)

* It is important to evaluate the performance of a trading algorithm. Here we multiply the per share profit/loss by 1000 to simulate the performance of the trading algorithm if it were to execute its trades using a share size of 1000. Results show that the trading algorithm profited $323, and produced a return on investment of 32.3% for an initial capital allocation of $100000.

  ![simple-trading-algo-performance](Images/simple-trading-algo-performance.png)

* Lastly, keep in mind that while the trading strategy in this example works, the trading strategy was designed to be oversimplified and may not work at scale. It is for this reason that we hard-coded the stock prices--in order simply focus on the process of creating a trading algorithm rather than dive into the complexities of a particular trading strategy.

Answer any questions before moving on.
