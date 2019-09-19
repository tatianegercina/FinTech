### 3. Everyone Do: Demystifying Algorithmic Trading (10 min)

In this activity, instructors will walk students through the mindset and steps of developing a basic trading algorithm. While the trading strategy of this particular example may not be effective at scale, the purpose of this activity is to show that the complexity associated with a trading algorithm more so derives from the sophistication of the particular trading strategy (how to handle stock data and initiate buy/sell/hold decision logic) rather than the actual steps to produce and execute a trading algorithm, which can be very simple.

**Files:**

* [basic_trading_algorithm.ipynb](Activities/01-Evr_Basic_Trading_Algorithm/Solved/basic_trading_algorithm.ipynb)

Open the solution file and discuss the following:

* Trading algorithms are often misconstrued to be highly complex and esoteric, left only for the quantitative analysts/traders of prominent big banks and hedge funds; however, when breaking down the core components of a trading algorithm, there are three fundamental parts: obtaining the data, handling the data, and initiating the decision logic to buy, sell, or hold.

* Oftentimes, stock data is provided from brokerage services than can be obtained via API calls. For this particular example, however, we've produced a hard-coded DataFrame consisting of 10 trading days worth of closing prices for AMD.

  ![amd-closing-prices-dataframe](Images/amd-closing-prices-dataframe.png)

* As can be seen, a trading algorithm can be much simpler than we thought! Here we can see the handling of data and the decision logic for the trading algorithm, namely the looping through of data using the for loop and the conditional statements defining the actions to buy or sell. This particular trading strategy performs a buy and sell every two days, in other words the first day performs a buy, the second day performs a sell, the third day performs a buy, and the fourth day performs a sell, and so on.

  ![simple-trading-algorithm](Images/simple-trading-algorithm.png)

* Trading algorithms often produce metrics on a per trade basis. Thus, in order to emulate the same effect in our simple trading algorithm, only a few changes are required--such as implementing order containers for buys and sells to record the stock prices of the buy-sell trading pairs.

  ![profit-loss-trading-algorithm](Images/profit-loss-trading-algorithm.png)

* Lastly, it is important to evaluate the performance of a trading algorithm. Here we multiply the per share profit/loss by a share size of 500 to simulate the performance of the trading algorithm if it were to execute its trades using share sizes of 500. Results show that the trading algorithm profited $170, and produced a return on investment of 17.0% for an initial capital allocation of $1000.

  ![simple-trading-algo-performance](Images/simple-trading-algo-performance.png)
