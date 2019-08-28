## 15.1 Lesson Plan: Algorithmic Trading

---

### Overview

Today's class will focus on using last unit's topics of deep neural networks to implement machine learning based trading, otherwise known as *algorithmic trading*. In particular, students will use deep neural nets to predict stock returns of multiple assets within a portfolio and trigger signal-based strategies for trading multiple assets at the same time.

### Class Objectives

By the end of class, students will be able to:

* Delineate what algorithmic trading is and who does it.

* Implement deep neural networks to predict stock returns of multiple assets.

* Construct signal-based trading strategies from predicted stock returns such as momentum and mean reversion.

* Rank multiple signal-based trading strategies by potential alpha generation.

* Backtest signal-based trading strategies to calculate the earning potential of the algorithm using historical data.

* Automate the purchase and sale of multiple assets using the recommended or best-ranked trading strategy.

* Build portfolios with specific allocations to each underlying asset based on the predicted alpha generation of each stock.

### Instructor Notes

* Today's lesson will consist of elements taught in the Pandas and Machine Learning.

* Not everyone will have a background in trading. Therefore, be thorough when explaining specific trading strategies and key terms.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 15.1 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, you teach students what exactly algorithmic trading is and explain why it's useful for FinTech professionals.

Welcome students to the first day of algorithmic trading and explain the following:

* Algorithmic trading is the concept of utilizing machine-learning to automate the process of buying and selling assets; models incorporating mathematic models are used to predict future stock returns and perform an action based on specific criteria, such as the ratio of risk to reward for the given scenario.

* Signals are created when specific criteria match up according to the machine learning model. Often, there are multiple signals that appear during trading activity, and therefore an algorithmic trading model should rank the multiple signals by potential alpha generation and choose the best one for the right scenario.

* Backtesting is the process of applying algorithmic trading models to historical trading data, making it possible to test the accuracy of the model (at least on data that has already happened).

* Using algorithmic trading models in conjunction with portfolio management allows for automatic re-balancing of assets (capital) within the portfolio, thereby aiding in portfolio optimization; algorithmic trading models automatically buy and sell assets within the portfolio according to the optimal weights for each asset calculated by the model.

Answer any questions before moving on.
