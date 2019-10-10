## 15.2 Lesson Plan: An Algorithmic Trading Framework

---

### Overview

Today's class will expand upon students' component knowledge of algorithmic trading and abstract one level higher to create a full-fledged trading framework encapsulated in a single application. In particular, students will learn how to wrap their previous code (data collection, signal generation, backtesting, evaluation, and dashboard creation) into functions that will be called via a single workflow. In other words, students' trading framework applications will automate the manual component calculations done in the previous class to produce an end-to-end trading dashboard containing all relevant metrics and functionality.

In addition, students will not only learn how to "go live" with their trading frameworks by establishing a connection to an actual financial API such as the Kraken Cryptocurrency Exchange (which provides 24-hour market access and generous API request privileges), but also further their understanding of dataflows by implementing asynchronous tasks and streaming capabilities that allows for a more robust trading dashboard that can update its underlying data without having to re-draw the overall dashboard each time.

### Class Objectives

By the end of class, students will be able to:

* Design an end-to-end workflow for a trading framework (data collection > signal generation > backtesting > evaluation > dashboard creation).

* Abstract their previous day's algorithmic trading calculations into functions and execute an end-to-end implementation of a working trading framework.

* Utilize live financial data by connecting their trading frameworks to the Kraken Cryptocurrency Exchange API.

* Persist or save their trading data to a database such as sqlite.

* Perform asynchronous tasks and loops using asyncio.

* Implement asyncio with their trading frameworks to fetch data and update the dashboard in parallel.

* Enhance their trading dashboards with data streaming capabilities.

* Deploy their algorithmic trading application online via Heroku.

### Instructor Notes

* Today's lesson will consist of elements taught in the Pandas, PyViz, and Machine Learning units. The lesson will include data analysis and querying, utilization of trading APIs for automated trade execution, and the visualization of trading performance and transaction analysis using a Panel dashboard.

* The goal of this unit is to educate students on trading, as well as how to use code to automate trading. Trading may be new for many students, so it is important that adequate information is provided regarding what trading is and all of the steps involved in creating entry and exit strategies, as well as which FinTech APIs integrate well with Python for automated trading.

* Not everyone will have a background in trading, so be thorough when explaining specific trading terminology, concepts, and strategies. Instead of painting the entire picture for students, focus on the individual steps required to execute a trade, and then apply coding concepts (i.e. iterations) to illustrate how the step can be automated using Python code. Definitions for key trading terminology will be provided.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

  * Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 15.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, students are introduced to algorithmic trading is and explain why it's useful for FinTech professionals. This section is a key opportunity to build excitement about creating a process to automate trades, evaluate risk, and make participating in the market as easy as running a program.

Welcome students to the first day of algorithmic trading and explain the following:

* Introduce students to algorithmic trading first by explaining how cumbersome it can be to manually make trades. Explain that a typical day for traders involves:

  * Tracking the transactional history of many stocks

  * Identify the best opportunity to buy, sell, and hold

  * Maintain knowledge about the highs and lows for each individual stock, as well as their overall portfolio value and profit/loss

  * Keeping emotions in check

* Also explain that human emotions play a key role in the success or failure of a trade/trader. Because the market is constantly changing with varying degrees of volatility, it's easy for humans to get emotional when trading. The trades that traders make have the ability to drastically impact their own profitability and livelihood. Furthermore, because traders are dealing with other people's money, such as retirement funds, every decision has the ability to disrupt the economical foundation of countless lives.

* The sheer number of moving parts and details that need to be considered can make it difficult for the human mind to consistently make performant trades. This is where **algorthmic trading** comes in.

* Algorithmic trading is the concept of utilizing machine-learning to automate the process of buying and selling assets. Machine learning algorithms can make predictions about ROI, risk, and analyze transactions much faster than a human brain. Because computers run off of logic rather than emotions, traders don't have to worry about their emotions getting in the way.

  * Underscore to students that there are a number of different algorthmic trading strategies that leverage machine learning. An algorithmic doesn't have to perform every action involved trading: algorithmic trading can be used just to predict the best investments, determine risk, or kick-off end-to-end trade execution and portfolio management.

* Using algorithmic trading models in conjunction with portfolio management also allows for automatic re-balancing of assets (capital) within the portfolio, thereby aiding in portfolio optimization. Algorithmic trading models automatically buy and sell assets within the portfolio according to the optimal weights for each asset calculated by the model.

* If time remains, summarize to students that all **algorithmic trading** involves is the prediction of future stock returns and execution of specific trading actions based on specific criteria, such as the ratio of risk to reward for the given scenario. In this regard, all a human has to do is click a button to execute the algorithm. The key difference between human traders and algorithmic trading is that computers can make decisions and predictions much more efficiently and effectively than humans, and they can do so without human emotions getting in the way.

* Lastly, if there is time, explain to students that the use of machine learning has given certain firms a competitive advantage compared to those still using manual, human labor. They're able to make smarter, more agile decisions based off of real time predictions and historical analysis, not to mention that less time is wasted on implementing and repeating manual processes.

Answer any questions before moving on.
