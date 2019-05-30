## 4.3 Lesson Plan - Investing Like the Pros

---

### Overview

Today's class will focus on the notion of analyzing the performance of not just a single stock, but groups of stocks together -- otherwise known as a portfolio of stocks. Stock portfolios are an important strategy in the realm of investing as total capital is proportioned among several stocks, thereby minimizing risk by preventing the "all eggs in one basket" dilemma.

However, in order to create an optimal portfolio that maximizes returns while minimizing risk, it's necessary to not only analyze the average return and risk of the portfolio overall, but also the correlation between stocks as well (how much one stock price changes with or against another). This lesson will teach students how to analyze the correlations of stocks against one another, calculate rolling statistics and volatility (beta) of stocks together, and optimize the composition of a portfolio and compare its performance against other portfolios.

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

* Be clear on the differences between correlation and beta. Both attempt to measure the relationship between one variable and another; however, correlation looks to measure the linear relationship between two variables while beta looks to measure the *unit-driven* relationship betweeen two variables (beta and stock returns).

* When explaining the notion of rolling statistics and how they benefit in identifying statistical trends, it may be helpful to provide a visual by comparing the original data trend against the smoothed trend of the rolling statistic (mean or standard deviation).

* When dealing with portfolios and its characteristics - risk, return, correlation - try to speak in terms of money. If you started with $10,000, how would a poorly optimized portfolio compare with one that is not?

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Slideshow](placeholder)

Welcome students to the third day of Pandas! Cover the following points:

* Previous classes focused on Pandas basics and single stock evaluation. Today students will combine what they've learned so far on using Pandas to analyze individual stock returns and risk, and move onto the notion of grouping stocks together to achieve the best risk/reward ratio for their investments.

* Mention to the class that today's focus is on using Pandas to make more informed (and better) investments! Students should feel invigorated as they are learning the techniques used by real financial analysts, quantitative traders, and portfolio managers.

* Since today's class focuses more on groups of stocks rather than an individual stock, students should be prepared to push their mindset from that of analyzing a single variable to analyzing an amalgamation of variables with relationships to one another.  

* Energize your students! Today is the day where students truly begin leveraging the power of Pandas to create truly insightful analyses that can benefit their skills in financial analysis/investing.
