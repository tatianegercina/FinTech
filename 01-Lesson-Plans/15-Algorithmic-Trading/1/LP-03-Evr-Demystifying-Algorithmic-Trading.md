### 3. Everyone Do: Demystifying Algorithmic Trading (10 min)

In this activity, instructors will walk students through the mindset and steps of developing a basic trading algorithm. While the trading strategy of this particular example may not be effective at scale, the purpose of this activity is to show that the complexity associated with a trading algorithm more so derives from the sophistication of the particular trading strategy (how to handle stock data and initiate buy/sell/hold decision logic) rather than the actual steps to produce and execute a trading algorithm, which can be very simple.

**Files:**

* [basic_trading_algorithm.ipynb](Activities/01-Evr_Basic_Trading_Algorithm/Solved/basic_trading_algorithm.ipynb)

Open the solution file and discuss the following:

* Trading algorithms are often misconstrued to be highly complex and esoteric, left only for the quantitative analysts/traders of prominent big banks and hedge funds; however, when breaking down the core components of a trading algorithm, there are three fundamental parts: obtaining the data, handling the data, and initiating the decision logic to buy, sell, or hold.

* Oftentimes, stock data is provided from brokerage services than can be obtained via API calls. For this particular example, we have hard-coded a DataFrame of 10 trading days worth of closing prices for AMD.

  ![amd-closing-prices-dataframe](Images/amd-closing-prices-dataframe.png)
