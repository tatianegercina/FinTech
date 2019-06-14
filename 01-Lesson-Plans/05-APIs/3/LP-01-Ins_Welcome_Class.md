## 5.3 Lesson Plan - Track to the Future!

---

### Overview

Today's class will focus on the notion of using Monte Carlo simulations to forecast future results and make confident predictions supported by statistical evidence. Monte Carlo simulations are an important tool in emulating a real-world use case that involves a degree of randomness surrounding an event or outcome, and seeks to iterate `n` number of times to find the most probable result of a variable event as well as the range of results and their corresponding probabilities of occurring.

In particular, stocks prices also tend to move somewhat randomly in such a way that there are varying probabilities to where the price may go or deviate from its average return (daily, weekly, monthly). Therefore, this lesson will teach students how to apply the concept of Monte Carlo simulations to predict future stock prices and therefore forecast the potential stocks returns of an initial investment, either as a single stock investment or as an investment in a portfolio.  

### Class Objectives

By the end of class, students will be able to:

* Define what a simulation is and why it's used.
* Deconstruct the components of the Monte Carlo Simulation process: probability distributions and iterations.
* Interpret probability distributions (normal/bell curve) and random number generators.
* Comprehend the use of confidence intervals and what they suggest.
* Implement a single Monte Carlo simulation on the future price trajectory of a stock.
* Execute multiple Monte Carlo simulations on the future price trajectories of a stock.
* Break down Portfolio Forecasting in the context of Monte Carlo Simulations on stock price trajectories and portfolio returns.
* Implement multiple Monte Carlo simulations on the potential returns of a stock portfolio.

### Instructor Notes

* Today's lesson deals heavily with statistical concepts, particularly probability. Try to be as clear as possible and be mindful of students who may become easily confused as this lesson will surely push the boundaries of most students' comfort levels when it comes to statistics.

* When overviewing the concept of probability distributions, also make sure to stress the notion of randomness. Probability merely implies that there is a chance that a specific result or event may occur but makes no guarantees, which is why results can differ with each iteration.

* Once students are comfortable with probability distributions, namely normal distributions, students should be able to process the idea that Monte Carlo simulations on stock investments seeks to chart the different paths (and probabilities) in which a stock can vary about its average daily return. Overview the code in detail so that this becomes more apparent.

* Towards the end of class, students will begin applying Monte Carlo simulations to portfolio returns. Therefore, they will need to combine the concepts of portfolio optimization (taught in the Pandas unit) with the concept of portfolio forecasting (taught in today's lesson). Walk through the steps in details as students can easily get lost in this myriad of technical concepts!

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Slideshow](placeholder)

Welcome students to the third day of APIs! Cover the following points:

* The previous lessons focused on API calls and showcased the Plaid API to exemplify that students can leverage the power of external data sets and functionality. Today students will combine what they've learned so far on using APIs to pull in stock data and forecast single stock/portfolio returns using Monte Carlo simulations.

* Mention to the class that today's focus is on using APIs to access stock data that can be manipulated to serve individual needs. Students should feel empowered as they are learning the ways in which they can use other curated data sets to analyze and generate insights on their own.

* Students should be prepared to push their mindset from historically analyzing portfolio returns and their performances to charting the possible paths a portfolio may move in the future, thereby making educated predictions on where the portfolio could end up.  

* Energize your students! Today is the day where students move from historical to future-oriented analysis. Time to look into the crystal ball!
