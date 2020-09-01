## 5.3 Lesson Plan: Track to the Future!

---

### Overview

Today's class will focus on the notion of using Monte Carlo simulations to forecast results and make confident predictions supported by statistical evidence. A Monte Carlo simulation is an essential tool for emulating a real-world use case that involves a degree of randomness surrounding an event or outcome. It seeks to iterate `n` a number of times to find the most probable result of a variable event, as well as the range of effects and their corresponding probabilities of occurring.

For example, stock prices fluctuate, so there are varying probabilities as to where the price may deviate from its average (daily, weekly, monthly). This lesson will teach students how to apply Monte Carlo simulations to predict future stock prices, thus forecasting the potential returns of an initial investment, either as a single stock or as a portfolio.

### Class Objectives

By the end of class, students will be able to:

* Define what a simulation is and why it's used.

* Identify the components of the Monte Carlo simulation process: probability distributions and iterations.

* Interpret probability distributions (normal, bell curve) and random number generators.

* Comprehend the use of confidence intervals and what they suggest.

* Implement a single Monte Carlo simulation on the price trajectory of a stock.

* Execute multiple Monte Carlo simulations on the price trajectories of a stock.

* Break down portfolio forecasting in the context of Monte Carlo simulations on stock price trajectories and portfolio returns.

* Implement multiple Monte Carlo simulations on the potential returns of a stock portfolio.

### Instructor Notes

* As a reminder, slack out the [PyViz Installation Guide](../../06-PyViz/Supplemental/PyVizInstallationGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class.

* Today's lesson deals heavily with statistical concepts, especially probability. Be as transparent as possible and mindful of students who may become confused, as this lesson pushes the boundaries of most students' comfort levels when it comes to statistics.

* When overviewing the concept of probability distributions, make sure to stress the notion of randomness. Probability merely implies that there is a chance that a specific result or event may occur, but makes no guarantees, which is why results can differ with each iteration.

* Once they're comfortable with probability distributions (namely, normal distributions), students should be able to process the idea that Monte Carlo simulations on stock investments seek to chart the different paths and probabilities in which a stock can vary about its average daily return. Overview the code in detail so that this becomes more apparent.

* Toward the end of class, students will begin applying Monte Carlo simulations to portfolio returns. Therefore, they will need to combine the concepts of portfolio optimization (taught in the Pandas unit) with the concept of portfolio forecasting (taught in today's lesson). Walk through the steps in detail, as students could easily get lost in this myriad of technical concepts!

* Note that the results from Monte Carlo simulations may vary from the lesson plan and a new execution in class since stock data is fetched `90` days before the current date.

* In this class, the concept of random numbers and random numbers generators is introduced and applied using `numpy.random`. A random seed (`random.seed(3)`) has been set for all the Instructor's activities to ensure reproducibility. Be aware of this during your coding demos, and explain the purpose of using a random seed for prototyping but not for deploying models.

* In the student activities using `numpy.random`, there a random seed is not set to allow students to experience randomness.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [5.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=629c0f35-efd0-4081-a916-aab4015c80e0) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 5.3 Slides](https://docs.google.com/presentation/d/11PFU8hncU5UGCjVueij74_HANBwRRU77TYfsVCy4XsE/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class and Intro to Monte Carlo Simulations (10 min)

Energize your students and welcome them to the third day of APIs! Today is the day where students move from historical to future-oriented analysis. Time to look into the crystal ball!

Cover the following points:

* The previous lessons focused on API calls and showcased the Alpaca API to exemplify that you can leverage the power of external datasets and functionality.

* Today you will combine what you've learned so far on using Alpaca to pull in stock data and forecast single stock and portfolio returns using Monte Carlo simulations.

* Today's focus is on using APIs to access stock data that can be manipulated to serve individual needs. You should feel empowered as you are learning how you can use other curated datasets to analyze and generate insights on their own.

* You should be prepared to push your mindset from historically analyzing portfolio returns and their performances to charting the possible paths a portfolio may move in the future, thereby making educated predictions on where the portfolio could end up.

Open the lesson slides, move to the "Monte Carlo Simulations" section and highlight the following:

* Today, we will combine what we’ve learned so far on using APIs to pull in stock data and forecast single stock/portfolio returns using Monte Carlo simulations.

* Simulations will require a switch from historical analysis to predicting the future.

* By the end of the lesson, Monte Carlo simulations will have predicted future stock prices and therefore forecast the potential stock's returns of an initial investment, either as a single stock investment or as an investment in a portfolio.

Continue with the slides switching to the "Simulations" section, ease students into the notion of this type of simulation by presenting the following questions and answers:

* What are simulations?

  * At its core, a simulation is a running instance of a model that seeks to emulate an existing process or system.

* What are Monte Carlo simulations?

  * A Monte Carlo simulation is a specific type of simulation that uses probability and variables to predict the future potential outcomes of a randomly occurring process.

* Why use Monte Carlo simulations?

  * Monte Carlo simulations provide a method of testing the range of values and corresponding probabilities that a random process can generate over time—specifically, how far results may deviate from the expected average. Monte Carlo simulations help to understand the risk of uncertainty in prediction and forecasting models, which is particularly helpful when dabbling in the domain of capital investments and stock price uncertainty!

Ask the students if they can think of any other examples of Monte Carlo simulations. Be sure to have all the students on the same page before moving on.

---

### 2. Instructor Do: Understanding Probability and Probability Distributions (15 min)

In this activity, you will explain to students how Monte Carlo simulations seek to explain the probability of potential outcomes for a randomly occurring event.

Open the lesson slides, move to the "Understanding Probability and Probability Distributions" section, and highlight the following:

* Imagine you are a scientist who wants to know how often a coin could land on heads for `5` trials of `10` coin flips. Flipping a coin has a `50%` chance of landing on heads and a `50%` chance of landing on tails.

* Because of the randomly occurring nature of flipping a coin, results could vary: for example, a coin could produce `6` heads and `4` tails; `3` heads and `7` tails; `8` heads and `2` tails, `5` heads and `5` tails, or `4` heads and `6` tails.

In short words, probability is the chance of an event happening. Probability merely implies that there is a chance that a specific result or event may occur but makes no guarantees; there will always be a risk of the event not occurring. Probability can be calculated whenever an outcome is uncertain, such as picking the specific color of a candy in its bag, the behavior of a stock, or the outcome of a bet.

* Therefore, an example Monte Carlo simulation would be to flip a coin `10` times to determine the resulting number of heads and tails and then do that same process another `5` times to determine the frequency distribution of landing on heads (how many times the coin landed a specific number of heads). The frequency distribution of heads can then be used to calculate the corresponding probability distribution that determines how likely it is for varying numbers (or ranges) of heads to land.

* Monte Carlo simulations help us visualize the effect of a probability distribution over time. But what is a probability distribution?

* A probability distribution is a mathematical function that describes the likelihood of possible outcomes for a given range of values. For example, we can define a function to calculate the likelihood of getting `7` heads on `10` coin flips.

* The most common probability distribution is the *normal distribution*, and it's found throughout the real-world. A normal distribution is commonly referred to as “the bell curve” and describes a dataset where values farther from its mean occur less frequently than values closer to its mean.

* When numerical data is considered to be normally distributed, the probability of any data point follows the `68-95-99.7` rule, stating that 68.27%, 95.45%, and 99.73% (effectively 100%) of possible values lie within one, two, and three standard deviations of the mean, respectively.

  ![normal-distribution](Images/normal-distribution.png)

* Normal distributions are particularly useful in finance because they adequately approximate the volatility of stock prices, forex rates, and other commodities. For example, the daily price change (in percent) from a high volatility stock such as Tesla and a low volatility stock such as Coca-Cola can both demonstrate normal distributions despite the differences in company size, customer base, stock price, and market share. We can visualize the normal distribution of these stocks using Pandas as follows.

Explain to students that we are going to use probability distributions to visually analyze the outcomes forecasted by Monte Carlo simulations, but first, it's time to learn how to fetch stock data and visualize its distribution using Python.

Answer any questions before moving on.

---



### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
