### 5. Student Do: Going Live with CCXT (15 mins)

In this activity, students will now get the chance to connect their algorithmic trading applications to the Kraken cryptocurrency exchange. In particular, rather than read data locally from a CSV file, students will modify their `fetch_data` functions to connect to Kraken via the CCXT library and read historical pricing data for BTC/USD.

The purpose of this activity is to showcase the "plug-and-play" feature of a framework. In other words, as long as the work flow of the overall framework remains consistent, individual components of the framework, such as the `fetch_data` function, can be modified to fit distinct needs.

**File:**

* [ninja_trader_v2.py](Activities/05-Stu_Backtesting/Unsolved/the_big_short_part_2.ipynb)

**Instructions:** [README.md](Activities/05-Stu_Backtesting/README.md)

---

### 6. Instructor Do: Going Live with CCXT Review (10 mins)

**File:** [the_big_short.ipynb](Activities/03-Backtesting/Solved/the_big_short_part_2.ipynb)

Open the solution file and review the following:

* The plot of the Short Position Dual Moving Average Crossover trading strategy showed that it was possible to *make* money from shorting VNQ (a real estate ETF) stock during the financial recession in 2008. Now, through backtesting the particular strategy, we will be able to see *how much* money can be made.

  ![short-dual-ma-crossover-plot2](Images/short-dual-ma-crossover-plot2.png)
