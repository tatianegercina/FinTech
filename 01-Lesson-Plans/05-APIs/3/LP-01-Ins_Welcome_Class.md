## 5.3 Lesson Plan - Track to the Future!

---

### Overview

Today's class will focus on the notion of using Monte Carlo simulations to forecast future results and make confident predictions supported by statistical evidence. Monte Carlo simulations are an important tool in emulating a real-world use case that involves a degree of randomness surrounding an event or outcome, and seeks to iterate `n` number of times to find the most probable result of a variable event. For example, flipping a coin has a 50% chance of landing on heads and a 50% chance of landing on tails. However, flipping a coin 10 times may have varying results: 6 heads and 4 tails; 3 heads and 7 tails; 8 heads and 2 tails, etc. Therefore, a simulation would flip a coin 10 times to determine the resulting combination of heads and tails, and then do that same process of flipping a coin 10 times another `n` number of times to determine the most probable combination of heads and tails if a coin were to be flipped 10 times. 

In particular, stocks prices also tend to move somewhat randomly in such a way that there are varying probabilities to where the price may go or deviate from its incremental return (daily, weekly, monthly). Therefore, this lesson will teach students how to apply the concept of Monte Carlo simulations to predict future stock prices and therefore forecast the potential stocks returns of an initial investment, either as a single stock investment or as an investment in a stock portfolio.  

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
