## 4.3 Lesson Plan - Stock Portfolios

---

### Overview

Today's class will focus on the notion of analyzing the performance of not just a single stock, but groups of stocks together -- otherwise known as a portfolio of stocks. Stock portfolios are an important strategy in the realm of investing as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma. However, in order to create an optimal portfolio that maximizes returns while minimizing risk, it's necessary to not only analyze the average return and risk of the portfolio overall, but also the correlation between stocks as well (how much one stock price changes with or against another). This lesson will teach students how to analyze the correlations of stocks against one another, calculate rolling statistics and volatility (beta) of stocks together, and optimize the composition of a portfolio and compare its performance against other portfolios.

### Class Objectives

By the end of class, students will be able to:

* Describe the benefits of investing in stock portfolios over a single stock.
* Explain what correlation is and how to calculate it in Pandas.
* Visualize trends through rolling statistics that minimize data noise.
* Compare the volatility of a portfolio against the overall market.
* Calculate expected returns of a portfolio utilizing custom weights
* Build and optimize a portfolio by factoring in risk, correlation, and returns
* Compare a portfolio's performance to other portfolios.

### Instructor Notes

* This lesson brings the heat on two fronts: math/statistics and financial domain knowledge. Not everyone will have extensive experience with either subject so be clear, visualize code/charts, and refer to the examples and notes if you need help!

* Remember that correlation does not imply causation. While two variables may move in tandem, or conversely, opposite to one another, it does not mean that one variable necessarily impacts the other. 

* Showcase the benefits of rolling statistics by comparing the original data trend against the smoothed trend of the rolling statistic (mean or standard deviation).

* When dealing with portfolios and its characteristics - risk, return, correlation - try to speak in terms of money. If you started with $10,000, how would a poorly optimized portfolio compare with one that is not?

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students to the third day of Pandas. Today they will combine what they've learned so far on using Pandas to analyze individual stock returns and risk, and incorporate the notion of grouping stocks together and factoring in their relationships to each other and other portfolios to choose the optimal group of stocks, and therefore, the optimal portfolio with the best risk/reward.  

Mention to the class that today's focus is on using Pandas to make more informed (and better) investments! Students should feel invigorated as they are learning the techniques used by real financial analysts, traders, and portfolio managers.

Explain that Pandas provides many advantages over Excel through it's data structures and built-in functions for analyzing data.

Explain to students that they have already installed Pandas through Anaconda, so they don't need to install additional libraries by now. However, if they have issues running Pandas then they can use a free notebook by [Google Colab](https://colab.research.google.com/) and troubleshoot their installation with a TA during a break or office hours.
