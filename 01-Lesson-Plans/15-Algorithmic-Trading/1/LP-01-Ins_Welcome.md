## 15.1 Lesson Plan: Algorithmic Trading

---

### Overview

Today's class will introduce students to the concept of **algorithmic trading** in Python. Traditional trading, or the manual purchase and sale of assets such as stocks, has begun to shift to more automated methods due to the advancements in network speed, computing power, and available financial trading APIs. Therefore, students will learn the fundamentals of algorithmic trading and deconstruct the process of producing a functional algorithmic trading model.

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

* Quantify evaluation metrics pertaining to overall portfolio and per-trade performance.

* Build a trading dashboard to visualize the multiple components of algorithmic trading.

### Instructor Notes

* Today's lesson will consist of elements taught in the Pandas and PyViz units. The lesson will include data analysis and querying, utilization of trading APIs for automated trade execution, and the visualization of trading performance and transaction analysis using a Panel dashboard.

* The goal of this unit is to educate students on trading, as well as how to use code to automate trading. Trading may be new for many students, so it is important that adequate information is provided regarding what trading is and all of the steps involved in creating entry and exit strategies, as well as which FinTech APIs integrate well with Python for automated trading.

* Not everyone will have a background in trading, so be thorough when explaining specific trading terminology, concepts, and strategies. Instead of painting the entire picture for students, focus on the individual steps required to execute a trade, and then apply coding concepts (i.e. iterations) to illustrate how the step can be automated using Python code. Definitions for key trading terminology will be provided.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 15.1 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this activity, students are introduced to what algorithmic trading is and why it's useful for FinTech professionals. In particular, this section is a key opportunity to build excitement about creating a process to automate trades, evaluate risk, and simplify participation in the market through the execution of a single program.

Welcome students to the first day of algorithmic trading and explain the following:

* Introduce students to algorithmic trading first by explaining how cumbersome it can be to manually make trades. Explain that a typical day for traders involves:

  * Tracking the transactional history of many stocks.

  * Identifying the best opportunity to buy, sell, and hold.

  * Maintaining knowledge about the highs and lows for each individual stock, as well as their overall portfolio value and profit/loss.

  * Keeping emotions in check.

* Also explain that human emotions play a key role in the success or failure of a trade/trader. Because the market is constantly changing with varying degrees of volatility, it's easy for humans to get emotional when trading. The trades that traders make have the ability to drastically impact their own profitability and livelihood. Furthermore, because traders often deal with other people's money, such as retirement funds, impulsive trading decisions can have the ability to disrupt the economical foundation of countless lives.

* The sheer number of moving parts and details that need to be considered can make it difficult for the human mind to consistently make profitable trades. This is where **algorithmic trading** comes in.

* Algorithmic trading is the concept of utilizing machines to automate the process of buying and selling assets. Machines running algorithms can make predictions about ROI, risk, and analyze transactions much faster than a human brain. Because computers run off of logic rather than emotions, traders don't have to worry about their emotions getting in the way.

  * Underscore to students that there are a number of different algorithmic trading strategies, even ones that can leverage machine learning. In addition, an algorithm does not necessarily have to evaluate the basis of a candidate trade in the same way: algorithms can be used to predict the best investments based off of profit-to-risk ratios, volume and volatility, or any number of varying attributes.

* Using algorithmic trading models in conjunction with portfolio management also allows for automatic re-balancing of assets (capital) within the portfolio, thereby aiding in portfolio optimization. Algorithmic trading models automatically buy and sell assets within the portfolio according to the optimal weights for each asset calculated by the model.

* If time remains, summarize to students that all **algorithmic trading** involves is the execution of specific trading actions based on specific criteria, such as the ratio of profit-to-risk for the given scenario. In this regard, all a human has to do is click a button to execute the algorithm.

* Lastly, if there is time, explain to students that the use of algorithmic trading has given certain firms a competitive advantage compared to those still using manual, human labor. They're able to make smarter, more agile decisions based off of real time predictions and historical analysis, not to mention that less time is wasted on implementing and repeating manual processes.

Answer any questions before moving on.
