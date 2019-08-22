## 5.3 Lesson Plan: Track to the Future!

---

### Overview

Today's class will focus on the notion of using Monte Carlo simulations to forecast future results and make confident predictions supported by statistical evidence. Monte Carlo simulations are an important tool in emulating a real-world use case that involves a degree of randomness surrounding an event or outcome. It seeks to iterate `n` number of times to find the most probable result of a variable event as well as the range of results and their corresponding probabilities of occurring.

In particular, stocks prices tend to move in such a way that there are varying probabilities to where the price may go or deviate from its average (daily, weekly, monthly). Therefore, this lesson will teach students how to apply the concept of Monte Carlo simulations to predict future stock prices and therefore forecast the potential returns of an initial investment, either as a single stock or as a portfolio.

### Class Objectives

By the end of class, students will be able to:

* Define what a simulation is and why it's used.

* Deconstruct the components of the Monte Carlo simulation process: probability distributions and iterations.

* Interpret probability distributions (normal, bell curve) and random number generators.

* Comprehend the use of confidence intervals and what they suggest.

* Implement a single Monte Carlo simulation on the price trajectory of a stock.

* Execute multiple Monte Carlo simulations on the price trajectories of a stock.

* Break down portfolio forecasting in the context of Monte Carlo simulations on stock price trajectories and portfolio returns.

* Implement multiple Monte Carlo simulations on the potential returns of a stock portfolio.

### Instructor Notes

* As a reminder, slack out the [PyViz Installation Guide](../../06-PyViz/Supplemental/PyVizInstallationGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class.

* Today's lesson deals heavily with statistical concepts, particularly probability. Try to be as clear as possible and be mindful of students who may become easily confused, as this lesson will  push the boundaries of most students' comfort levels when it comes to statistics.

* When overviewing the concept of probability distributions, also make sure to stress the notion of randomness. Probability merely implies that there is a chance that a specific result or event may occur but makes no guarantees, which is why results can differ with each iteration.

* Once students are comfortable with probability distributions, namely normal distributions, students should be able to process the idea that Monte Carlo simulations on stock investments seeks to chart the different paths (and probabilities) in which a stock can vary about its average daily return. Overview the code in detail so that this becomes more apparent.

* Toward the end of class, students will begin applying Monte Carlo simulations to portfolio returns. Therefore, they will need to combine the concepts of portfolio optimization (taught in the Pandas unit) with the concept of portfolio forecasting (taught in today's lesson). Walk through the steps in details as students can easily get lost in this myriad of technical concepts!

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

**Files:**

* [Slideshow](https://docs.google.com/presentation/d/1AqrhqULvquRO1W6WdUrYBKp5jcLLngN989DItBr_IBQ/edit?usp=sharing)

Welcome students to the third day of APIs! Cover the following points:

* The previous lessons focused on API calls and showcased the Plaid API to exemplify that students can leverage the power of external datasets and functionality. Today students will combine what they've learned so far on using APIs to pull in stock data and forecast single stock and portfolio returns using Monte Carlo simulations.

* Mention to the class that today's focus is on using APIs to access stock data that can be manipulated to serve individual needs. Students should feel empowered as they are learning the ways in which they can use other curated datasets to analyze and generate insights on their own.

* Students should be prepared to push their mindset from historically analyzing portfolio returns and their performances to charting the possible paths a portfolio may move in the future, thereby making educated predictions on where the portfolio could end up.

* Energize your students! Today is the day where students move from historical to future-oriented analysis. Time to look into the crystal ball!

---

### 2. Instructor Do: Intro to Monte Carlo Simulations (10 min)

Ease students into the notion of Monte Carlo simulations by presenting the following questions and answers:

* What is a simulation?

  > At its core, a simulation is a running instance of a model that seeks to emulate an existing process or system.

* What is a Monte Carlo simulation?

  > A Monte Carlo simulation is a specific type of simulation that uses probability and variables to predict the future potential outcomes of a randomly occurring process.

* What is probability?

  > The chance of an event happening. For example, the chance of a coin landing on heads is `50%`.

* Why use Monte Carlo simulations?

  > Monte Carlo simulations provide a method of testing the range of values and corresponding probabilities that a random process can generate over time—specifically, how far results may deviate from the expected average. Monte Carlo simulations help to understand the risk of uncertainty in prediction and forecasting models, which is particularly helpful when dabbling in the domain of capital investments and stock price uncertainty!

* What would be an example of a Monte Carlo simulation?

  > Imagine a scientist wanted to know how often a coin could land on heads for `5` trials of `10` coin flips. Flipping a coin has a `50%` chance of landing on heads and a `50%` chance of landing on tails. Because of the randomly occurring nature of flipping a coin, results could vary: for example, a coin could produce `6` heads and `4` tails; `3` heads and `7` tails; `8` heads and `2` tails, `5` heads and `5` tails, or `4` heads and `6` tails. Therefore, an example Monte Carlo simulation would be to flip a coin `10` times to determine the resulting number of heads and tails, and then do that same process another `5` times to determine the frequency distribution of landing on heads (how many times the coin landed a specific number of heads). The frequency distribution of heads can then be used to calculate the corresponding probability distribution that determines how likely it is for varying numbers (or ranges) of heads to land.

Ask the students if they can think of any other examples of Monte Carlo simulations. Be sure to have all the students on the same page before moving on.

---

### 3. Instructor Do: Probability Distribution of Potential Outcomes (10 min)

Monte Carlo simulations seek to explain the probability of potential outcomes for a randomly occurring event. Therefore, this activity provides a hands-on approach to introducing students to what a simple Monte Carlo simulation could look like and how to interpret the results.

**Files:**

* [coin_flip_simulation.ipynb](Activities/01-Ins_Probability_Distributions_of_Potential_Outcomes/Solved/coin_flip_simulation.ipynb)

Walk through the solution and highlight the following:

* This solution represents a technical example to the Monte Carlo simulation use case presented in the previous activity (coin flip simulation). Therefore, the program flips a coin `10` times for `5` simulations to determine the frequency distribution of heads landed per simulation and the corresponding probability distribution of landing varying numbers (or ranges) of heads.

* Make sure to import the `random` class from the `numpy` library which allows for randomizing a particular code process.

  ```python
  # Import libraries and dependencies
  from numpy import random
  import pandas as pd
  %matplotlib inline
  ```

* The `choice` function from the `random` class, combined with the `p` parameter for setting the probability of random events, is used to randomly choose between the two outcomes of a coin: heads or tails. Therefore in this case, the `p` parameter is set to `[0.5, 0.5]` to represent a `50%` chance of a coin landing on heads and a `50%` chance of a coin landing on tails.

  ```python
  # Print simulation iteration
  print(f"Running Simulation {n+1}...")

  # Set an empty list to hold flip results
  flips = []

  # Set probability of events
  probability = [0.5, 0.5]

  # Flip the coin several times
  for i in range(num_flips):
      # Random int: 0 or 1
      coin_flip = random.choice(coin, p=probability)

      # Print flip result
      print(f"  Flip {i+1}: {coin_flip}")

      # Append flip result to list
      flips.append(coin_flip)
  ```

  ![coin-flip-results](Images/coin-flip-results.png)

* The resulting heads and tails outputs for each simulation of `10` coin flips are saved as individual columns to a Pandas DataFrame.

  ```python
  # Append column for each simulation and flip results
  monte_carlo[f"Simulation {n}"] = pd.Series(flips)
  ```

  ![coin-flip-dataframe](Images/coin-flip-dataframe.png)

* The following is a holistic view of the example Monte Carlo simulation program—see, it's not that bad!

  ```python
  # Set number of simulations and coin flips
  num_simulations = 5
  num_flips = 10

  # Set a list object acting as a coin: heads or tails
  coin = ["heads", "tails"]

  # Set probability of events
  probability = [0.5, 0.5]

  # Create an empty DataFrame to hold simulation results
  monte_carlo = pd.DataFrame()

  # Run n number of simulations
  for n in range(num_simulations):

      # Print simulation iteration
      # print(f"Running Simulation {n+1}...")

      # Set an empty list to hold flip results
      flips = []

      # Flip the coin several times
      for i in range(num_flips):

          # Random int: 0 or 1
          coin_flip = random.choice(coin, p=probability)

          # Print flip result
          # print(f"  Flip {i+1}: {coin_flip}")

          # Append flip result to list
          flips.append(coin_flip)

      # Append column for each simulation and flip results
      monte_carlo[f"Simulation {n}"] = pd.Series(flips)

  # Print the DataFrame
  monte_carlo
  ```

* Looping through the DataFrame containing the coin flip results while leveraging the `value_counts` function allows for counting the occurrences of the different heads-to-tails combinations of every simulation.

  ![coin-flip-value-counts](Images/coin-flip-value-counts.png)

* The conditional statements check to make sure that both the `heads` and `tails` keys are present in the series object returned from the `value_counts` function. If one or the other key is not present, the missing key gets a `0` to account for the fact that the event did not occur at all during the simulation (flipped 10 heads or flipped 10 tails).

  ```python
  # Append results of heads and tails to respective lists
  # If `heads` and `tails key is present in the Series, append both results
  if 'heads' in value_count.index and 'tails' in value_count.index:
      heads.append(value_count['heads'])
      tails.append(value_count['tails'])

  # If `heads` key is not present in the Series, append heads list with 0
  # And append tails list with tails result (simulation must have returned all tails)
  elif 'heads' not in value_count.index:
      heads.append(0)
      tails.append(value_count['tails'])

  # If `tails` key is not present in the Series, append tails list with 0
  # And append heads list with heads result (simulation must have returned all heads)
  elif 'tails' not in value_count.index:
      tails.append(0)
      heads.append(value_count['heads'])
  ```

* Creating a DataFrame from the list of heads per simulation and using the `plot` function with the `kind` parameter set to `hist` produces a histogram that showcases the frequency distribution of landed heads.

  ![coin-flip-5-simulations](Images/coin-flip-5-simulations.png)

* Remember that a histogram is not a bar graph; frequency values in histogram bars are determined by the area (length times width) of the bar, not by the height of the bar. Histograms deal with the frequency of values associated with *ranges* of numbers or *bins* rather than a single data point.

* Without manually setting the `bins` parameter for a histogram, the plot defaults to `10` bars between the minimum and maximum data points provided. Sometimes this creates ranges deviating from what is being simulated. Therefore, manually setting the `bins` parameter ensures that the histogram properly represents the edges of each bin, in this case bin edges of `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`.

  ![coin-flip-5-simulations-bins-off](Images/coin-flip-5-simulations-bins-off.png)

  ![coin-flip-5-simulations-bins](Images/coin-flip-5-simulations-bins.png)

* Setting the `density` parameter to `True` for the histogram plot function creates a frequency density histogram which can be used to showcase the probability distribution of potential outcomes. In this case, it can be interpreted that for an experiment of `5` simulations of `10` coin flips, we can expect approximately `40%` of our simulations to land between 4 and 5 heads and another `40%` of our simulations to land between 5 and 6 heads. In addition, it could be said that `80%` of our simulations could land between 4 and 6 heads.

  ![coin-flip-density-histogram](Images/coin-flip-density-histogram.png)

* Unfortunately, the probability distribution of potential outcomes generated for a small number of simulations should not be trusted. This is because a small number of simulations cannot test every possible outcome and therefore may generate biased results that are not indicative of the true nature of the random process in the long term. Therefore, increasing the simulation count to `100` provides a more reliable and continuous range of probable outcomes.

  ![coin-flip-100-simulations](Images/coin-flip-100-simulations.png)

* Increasing the simulation count yet again to `1000` produces even more potential outcomes and should be considered even more reliable in the long term. It can be seen that landing heads `5-6` times is the most likely outcome in the long term.

  ![coin-flip-1000-simulations](Images/coin-flip-1000-simulations.png)

* Notice that with an even larger number of simulations, the random process of flipping a coin begins to exhibit a bell-curve nature to the probability of its potential outcomes. This distribution is one in which probability is maximized at the middle of the distribution and decreases in probability as outcomes deviate left and right from the mean, otherwise known as the *mean* and *standard deviation*. This well-known phenomenon is called the *normal distribution* or continuous probability distribution of a range of potential outcomes.

  ![normal-distribution](Images/normal-distribution.png)

---

### 4. Students Do: Free Throw Simulation (15 min)

In this activity, students execute a Monte Carlo simulation to analyze the probability distribution of free throws made out of 10 shots for a player with a `70%` accuracy and determine the likelihood of the player making `9-10` free throws in a single session.

Circulate with TAs during this activity to provide students with assistance. Below are a couple scenarios to watch out for.

* Students might face difficulty working with the histograms. Histogram bins have a default value, so if the bins are not configured properly, the charts might not look as expected (the bin edges will be off) and the ranges may deviate from what is being simulated.

* Also keep an eye out for any student issues related to missing data; if heads or tails data is missing, this is most likely because 0 was not appended for the missing values. This could visually result in one side of the distribution being cut off (producing a non-normal distribution with no values for the first coin flip).

**Instructions:**

* [README.md](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/README.md)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Unsolved/free_throw_simulation.ipynb)

### 5. Instructor Do: Review Free Throw Simulation (5 min)

**Files:**

* [free_throw_simulation.ipynb](Activities/02-Stu_Probability_Distribution_of_Potential_Outcomes/Solved/free_throw_simulation.ipynb)

Open the solution and explain the following:

* The process of executing a Monte Carlo simulation remains similar even for a different use case (free throws vs. coin flips). At its core, the basis of Monte Carlo simulations is iteration (running tests and simulations) and saving the results of a random process. Thus, expect the programmatic structure of `for` loops and potentially nested `for` loops.

  ```python
  # Set number of simulations and free throws
  num_simulations = 1000
  num_throws = 10

  # Set a list object acting as a throw: made basket or missed basket
  throw = ["made", "missed"]

  # Set probability of events
  probability = [0.7, 0.3]

  # Create an empty DataFrame to hold simulation results
  monte_carlo = pd.DataFrame()

  # Run n number of simulations
  for n in range(num_simulations):

      # Print simulation iteration
      # print(f"Running Simulation {n+1}...")

      # Set an empty list to hold throw results
      throws = []

      # Shoot the ball `10` times
      for i in range(num_throws):

          # Randomly choose between `made` and `missed` with a `70%` chance to make the throw and a `30%` chance the throw is missed
          free_throw = random.choice(throw, p=probability)

          # Print throw result
          # print(f"  Throw {i+1}: {free_throw}")

          # Append throw result to list
          throws.append(free_throw)

      # Append column for each simulation and throw results
      monte_carlo[f"Simulation {n}"] = pd.Series(throws)

  # Print the DataFrame
  monte_carlo
  ```

* The `choice` function from the `random` class of the `numpy` library has a `p` parameter that allows for setting a nonuniform probability to events. In this case, a player has a `70%` chance of making a shot and consequently a `30%` chance of missing the shot. Therefore, the `choice` function below reflects this.

  ```python
  # Randomly choose between `made` and `missed` with a `70%` chance to make the throw and a `30%` chance the throw is missed
  free_throw = random.choice(throw, p=probability)
  ```

* Because the random process has nonuniform probability (`70%` chance to make a shot and `30%` chance to miss a shot) the corresponding frequency and probability distributions of made free throws show that a majority of the distribution lies within the `7, 8, 9, and 10` range, while the rest of the distribution is spread out within the `0, 1, 2, 3, 4, 5, 6` range. Unlike the bell curve of a normal distribution, this is called a skewed (in this case left-skewed) distribution.

  ![free-throws-frequency-distribution](Images/free-throws-frequency-distribution.png)

  ![free-throws-probability-distribution](Images/free-throws-probability-distribution.png)

* The probability distribution of free throws made will change slightly with every run of the program; however, in this current run, the probability distribution shows that the likelihood of the player making `9-10` shots in a single session is approximately `15%`.

  ![free-throws-probability-distribution-focus](Images/free-throws-probability-distribution-focus.png)

---

### 6. Instructor Do: Confidence Intervals (10 min)

In this activity, students are introduced to confidence intervals, which in the context of Monte Carlo simulations, are value ranges of potential outcomes with a particular probability of occurring. Confidence intervals in combination with Monte Carlo simulations are useful when trying to predict the likelihood of an outcome falling within a specific range.

**Files:**

* [coin_flip_confidence_intervals.ipynb](Activities/03-Ins_Confidence_Intervals/Solved/coin_flip_confidence_intervals.ipynb)

Walk through the solution and highlight the following:

* Often in statistics, there is a disconnect between the results of a sample dataset and attempting to apply the results of a sample to the overall population. For example, analyzing the average height of `20` students at a school to assume the exact average height of the entire population of students at the school would be an erroneous assumption. Therefore, confidence intervals suggest a range of values where there is a `X%` chance that the true expected value would lie within the specified range. In this case, a `95%` confidence interval may suggest that there is a `95%` chance that the true average height of students would range in height between `4` ft and `6 ft`, or in other words, the `95%` of the expected height of students should lie within the range of `4` ft and `6 ft`.

  ![confidence-interval-probability-distribution](Images/confidence-interval-probability-distribution.png)

* There is a tradeoff between the confidence, or likelihood of occurrence, of the expected result and the range of the upper and lower bounds of the confidence interval; the `X%` of the confidence interval suggests how wide or narrow the value range is. A `90%` confidence interval will have a narrower range, and therefore is less confident than a `95%` confidence interval with a larger range.

  ![confidence-interval-comparison](Images/confidence-interval-comparison.png)

* In the context of Monte Carlo simulations, a confidence interval is a value range of a frequency distribution that contains a specific percentage of all potential outcomes. For example, a `90%` confidence interval would be a range of values of which `90%` of all potential outcomes of the Monte Carlo simulation are contained. Therefore, confidence intervals used with frequency distributions of Monte Carlo simulations calculate the range of potential outcomes and their probabilities of occurring. For example, one could analyze the frequency distribution of potential stock price trajectories and determine that "there is a `90%` chance that the stock price will be between `$10` and `$20` next week."

* In order to create a confidence interval, the upper and lower bounds of the confidence interval need to be set as a quantile or percentile range of the frequency distribution.

* A quantile is a measurement in which a frequency distribution is divided into equal groups, thus each group contain an equal fraction of the total sample. Often times, quantiles are expressed in `100` equal parts, otherwise known as *percentiles*. For example, a student in the 95th percentile of height for his school is as tall as or taller than `95%` of the students at the school.

* The `quantile` function for `pandas` DataFrames takes in a range of values that represent the lower and upper bounds of the confidence interval. The `numeric_only` parameter set to `True` ensures the quantiles are computed on numeric only values. In this case, quantiles of `0.05` and `0.95` are values where landing `2` heads is only greater than `5%` of all simulated outcomes, whereas landing `8` heads is greater than `95%` of all simulated outcomes.

  ![coin-flip-quantile-function](Images/coin-flip-quantile-function.png)

* The `pyplot` class from the `matplotlib` library contains a `axvline` function that allows for setting upper and lower bounds to a confidence interval on a plot. The `color` parameter sets the color of the line.

  ![coin-flip-confidence-interval](Images/coin-flip-confidence-interval.png)

* The `90%` confidence interval calculated suggests that if a coin were to be flipped 10 times, there is a `90%` chance of the coin landing somewhere between 2 and 8 heads. This is because the confidence interval encapsulates `90%` of the frequency distribution (the area of the bars in the histogram) of simulated results.

---

### 7. Students Do: Archery Target Hits (15 min)

In this activity, students execute a Monte Carlo simulation to analyze the probability distribution of potential hits (out of `5` shots) of a target for a beginner archer with a `20%` accuracy and determine the range of hits for the archer that has a `95%` chance of happening in a single session.

**Instructions:**

* [README.md](Activities/04-Stu_Confidence_Intervals/README.md)

**Files:**

* [archery_target_hits.ipynb](Activities/04-Stu_Confidence_Intervals/Unsolved/archery_target_hits.ipynb)

### 8. Instructor Do: Review Archery Target Hits (5 min)

**Files:**

* [archery_target_hits.ipynb](Activities/04-Stu_Confidence_Intervals/Solved/archery_target_hits.ipynb)

Open the solution and explain the following:

* The `pandas` library comes built-in with certain matplotlib functions such as `plot`; however, the standalone `matplotlib` library provides the robustness required for altering a plot and setting the lower and upper bounds of a confidence interval. Therefore, make sure to import the `pyplot` class from the `matplotlib` library.

  ```python
  # Import libraries and dependencies
  import matplotlib.pyplot as plt
  from numpy import random
  import pandas as pd
  %matplotlib inline
  ```

* To know the range of data points that contain a specific percentage of all data points in the sample, generating a frequency distribution is a prerequisite to defining a confidence interval.

  ![archery-probability-distribution](Images/archery-probability-distribution.png)

* Because the mean of a normal distribution is considered to be at the `50th` quantile, confidence intervals are usually set around the mean or `0.50` quantile. Therefore, a `95%` confidence interval would have quantiles set at `0.025` and `0.975` rather than something like `0.05` and `1.00`.

  ![archery-quantiles](Images/archery-quantiles.png)

* The `95%` confidence interval suggests that there is about a `95%` chance of the archer hitting the target `0-3` times out of `5` shots. Marking the confidence interval over the probability distribution histogram shows that the area of the bars within the lower and upper bounds approximate to about `95%`.

  ![archery-confidence-interval](Images/archery-confidence-interval.png)

---

### 9. Instructor Do: Simulation of Stock Price Trajectory (10 min)

This activity exemplifies the use case where a Monte Carlo simulation can be applied to a historical dataset such as daily closing stock prices, given the assumption that daily closing stock prices have a normal probability distribution. Stock datasets will be pulled in from the IEX API and used to generate a Monte Carlo simulation based off  a normally distributed random process using the dataset's calculated average and standard deviation of daily returns.

**Files:**

* [stock_price_simulation.ipynb](Activities/05-Ins_Simulation_of_Stock_Price_Trajectory/Solved/stock_price_simulation.ipynb)

Walk through the solution and highlight the following:

* Monte Carlo simulations can be executed not just on random processes with *discrete probabilities* (ex. `70%` to make a free throw and `30%` to miss a free throw), but also on *continuous probabilities* such as normal probability distributions.

* Normal probability distributions showcase the various probabilities of returning a value based on the number of standard deviations it is from the mean (how far the value may lie plus or minus from the average expected value); values far away from the mean are less common while values near the mean are more common. Monte carlo simulation use this characteristic to simulate a random process' potential outcomes with respect to the variability around its mean.

  ![example-normal-distribution](Images/example-normal-distribution.png)

* The daily closing stock price data will be pulled using the `iexfinance` SDK that connects to the `iex` API. Therefore, make sure to import the necessary libraries and dependencies before proceeding.

  ```python
  # Import libraries and dependencies
  import numpy as np
  import pandas as pd
  from datetime import datetime, timedelta
  from iexfinance.stocks import get_historical_data
  import iexfinance as iex
  import matplotlib.pyplot as plt
  %matplotlib inline
  ```

* Use the `get_symbols` function from the `refdata` class of the `iex` SDK to check the available stock ticker data that can be pulled from the `iex` API.

  ![iex-check-tickers](Images/iex-check-tickers.png)

* The `get_historical_data` function from the `iexfinance` SDK takes in a `ticker`, `start_date`, and `end_date` parameter with an `output_format` option set to `pandas` to return a DataFrame of `AAPL` daily stock prices. The `start_date` and `end_date` variables in this case are set to `365` days from the current date and the current date, respectively.

  ![iex-get-data](Images/iex-get-data.png)

* Simulating stock price trajectory involves analyzing the closing prices of a stock. Therefore, it's best to drop the extraneous columns for the `AAPL` price data received from the `iex` API.

  ![dataframe-drop-columns](Images/dataframe-drop-columns.png)

* In order to simulate `AAPL` stock prices for the next `252` trading days, it is important that the simulation is framed in the context of a stock's *growth*. Therefore, the `pct_change` function is used to calculate the last year of daily returns for `AAPL`, and the `mean` and `std` functions are used to calculate the average daily return and the volatility of daily returns.

  ![aapl-daily-returns](Images/aapl-daily-returns.png)

  ![aapl-daily-return-mean-and-std](Images/aapl-daily-return-mean-and-std.png)

* The following code snippet exemplifies the simulation of stock price trajectory. The simulation calculates the next day's simulated closing price by multiplying the preceding day's closing price by a random selection of a range of values defined by the normal probability distribution of `AAPL` daily returns, given by the *mean* and *standard deviation* of daily returns.

  ```python
  # Simulate the returns for 252 days
  for i in range(num_trading_days):
      # Calculate the simulated price using the last price within the list
      simulated_price = simulated_aapl_prices[-1] * (1 + np.random.normal(avg_daily_return, std_dev_daily_return))
      # Append the simulated price to the list
      simulated_aapl_prices.append(simulated_price)
  ```

* Plotting the DataFrame of simulated `AAPL` closing prices for the next `252` trading days shows one potential pathway for how `AAPL` stock prices may behave in the next year.

  ![appl-simulated-prices-plot](Images/appl-simulated-prices-plot.png)

* Calculating the daily returns and cumulative returns of `AAPL` simulated prices allow for plotting the profits and losses of a potential investment in `AAPL` over the next trading year.

  ![aapl-cumulative-pnl.png](Images/aapl-cumulative-pnl.png)

  ![aapl-cumulative-pnl-plot.png](Images/aapl-cumulative-pnl-plot.png)

---

### 10. Students Do: Financial Forecasting Part 1 (15 min)

In this activity, students execute a Monte Carlo simulation to forecast stock price by multiplying each preceding day by a randomly generated daily return of normal probability distribution, approximated by a mean and standard deviation of historical `TSLA` daily returns.

**Instructions:**

* [README.md](Activities/06-Stu_Financial_Forecasting_Pt_I/README.md)

**Files:**

* [financial_forecasting_part_1.ipynb](Activities/06-Stu_Financial_Forecasting_Pt_I/Unsolved/financial_forecasting_part_1.ipynb)

### 11. Instructor Do: Review Financial Forecasting Part 1 (5 min)

**Files:**

* [financial_forecasting_part_1.ipynb](Activities/06-Stu_Financial_Forecasting_Pt_I/Solved/financial_forecasting_part_1.ipynb)

Open the solution and explain the following:

* Make sure that the `IEX_TOKEN` environment variable is properly set so that the `iexfinance` SDK can communicate to the `IEX Cloud` API. Navigate [here](https://addisonlynch.github.io/iexfinance/stable/configuration.html) for more details on how to do so.

  ![missing-api-key](Images/missing-api-key.PNG)

* The `get_historical_data` function in conjunction with the `datetime` library pulls stock data from the `IEX Cloud` API using a dynamic datetime range. Specifically, `start_date` and `end_date` variables are not hard-coded.

  ![datetime-range](Images/datetime-range.PNG)

* Applying a Monte Carlo simulation to forecasting the future daily closing prices of `TSLA` stock involves multiplying the closing price of each preceding trading day by a randomly generated daily return approximated by a normal probability distribution given the historical average and standard deviation of `TSLA` daily returns.

* In other words, each `TSLA` closing price of the preceding trading day is multiplied by a randomly chosen daily return where values closer to the expected daily return have a higher probability of occurring while values farther away from the expected daily return have a lesser probability of occurring.

  ![tsla-normal-distribution](Images/tsla-normal-distribution.PNG)

* Simulations for the next `252` trading shows that `TSLA` stock is forecast to continue to decline, with a `$10,000` investment facing brutal negative cumulative returns if invested in `TSLA` over the next 3 years.

  ![tsla-simulated-price-plot](Images/tsla-simulated-price-plot.PNG)

  ![tsla-cumulative-pnl](Images/tsla-cumulative-pnl.PNG)

* It should be stated that although the forecast for the next `3` years of `TSLA` stock prices show considerable declines, it does not mean that it is guaranteed. A forecast/prediction is only as good as the foundation of information from which it was made, and even then, by the nature of random events -- *anything* can happen.

---

### 12. BREAK (40 min)

---

### 13. Instructor Do: Predicting Probable Outcomes of Stock Price Trajectory (10 min)

In this activity, students go one step further to produce not just a single potential price trajectory for a stock over the next `252` trading days, but many potential price trajectories. So that it's possible to analyze the probability distribution of where a stock's price can go, and therefore an interval to which confident predictions can be made regarding future stock price.

**Files:**

* [probable_outcomes_of_stock_price.ipynb](Activities/07-Ins_Predicting_Probable_Outcomes_of_Stock_Price_Trajectory/Solved/probable_outcomes_of_stock_price.ipynb)

Walk through the solution and highlight the following:

* Simulating a single price trajectory for a stock, with respect to its average daily return and volatility, is but one pathway of which the stock price could move over time. Therefore, in order to analyze the possible ranges of where a stock price might end up, multiple simulations of stock price trajectories need to be run.

  ![multiple-stock-simulation](Images/multiple-stock-simulation.PNG)

  * The outer loop controls the total number of simulations. The more simulations that we have, the more accurate the model.

    ```python
    for n in range(num_simulations):
    ```

  * For each simulation run, the calculations for stock price growth are based on the last known closing price. The simulation will  vary the data from this starting point to see how the data might change in the future.

    ```python
    simulated_aapl_prices = [aapl_last_price]
    ```

  * The inner loop determines how many future days of stock prices we are simulating. In this case, we are simulating the returns for `252` trading days.

    ```python
    for i in range(num_trading_days):
    ```

  * We can use `random.normal` function from the `numpy` library to simulate future stock price growth and fluctuations by using its historical average daily return and volatility. Future stock price growth is calculated by multiplying each preceding trading day's closing price by a randomly selected daily return based on a normal probability distribution of `AAPL` daily returns, derived from its historical average daily return value (mean) and its volatility (standard deviation).

    ```python
    simulated_price = simulated_aapl_prices[-1] * (1 + np.random.normal(avg_daily_return, std_dev_daily_return))
    simulated_aapl_prices.append(simulated_price)
    ```

  * After each inner loop runs, we add all of the simulated daily returns as a new column to the Monte Carlo DataFrame.

    ```python
    simulated_price_df[f"Simulation {n+1}"] = pd.Series(simulated_aapl_prices)
    ```

* The plot of the DataFrame containing the `1000` simulations of `252` trading day price records showcases the potential pathways that a stock price can take.

  ![multiple-stock-simulation-plot](Images/multiple-stock-simulation-plot.PNG)

* The last row of the DataFrame containing the results of each simulation represents the closing stock prices of `AAPL` on the `252nd` simulated trading day. In other words, the last row of the DataFrame represents the potential outcomes of `AAPL` stock price over the next `252` trading days.

  ![stock-price-frequency-distribution](Images/stock-price-frequency-distribution.PNG)

* Calculating a `95%` confidence interval of potential outcomes for projected `AAPL` stock prices over the next `252` trading days showcases a range in which there is a `95%` chance that `AAPL` stock price will end up within the range of `$106.22 - $329.27`.

  ![stock-price-confidence-interval](Images/stock-price-confidence-interval.PNG)

* Multiplying an initial investment of `$10,000` by the percentage change in stock price for the lower and upper bounds of the `95%` confidence interval produces a confidence interval in terms of investment.

  ![stock-price-investment-confidence-interval](Images/stock-price-investment-confidence-interval.PNG)

---

### 14. Students Do: Financial Forecasting Part 2 (15 min)

In this activity, students execute a Monte Carlo simulation to forecast the many different possibilities of simulated stock price trajectories, thereby analyzing the frequency and probability of potential `TSLA` stock price outcomes.

**Instructions:**

* [README.md](Activities/08-Stu_Financial_Forecasting_Pt_II/README.md)

**Files:**

* [financial_forecasting_part_2.ipynb](Activities/08-Stu_Financial_Forecasting_Pt_II/Unsolved/financial_forecasting_part_2.ipynb)

### 15. Instructor Do: Review Financial Forecasting Part 2 (5 min)

**Files:**

* [financial_forecasting_part_2.ipynb](Activities/08-Stu_Financial_Forecasting_Pt_II/Solved/financial_forecasting_part_2.ipynb)

Open the solution and explain the following:

* Performing a Monte Carlo simulation on potential stock price outcomes involves simulating the stock price of `TSLA` over `253 times 3` trading days using a randomly selected normal distribution of daily returns and then doing the same process `n` number of times. Therefore, the code reflects another `for` loop to account for the extra iteration.

  ![nested-tsla-monte-carlo-simulation](Images/nested-tsla-monte-carlo-simulation.png)

* The plot for `1000` simulations of `TSLA` stock price trajectory over the next `252 * 3` trading days provides a visual representation of where `TSLA` stock price could possibly end up. Notice the volatility!

  ![tsla-multiple-stock-trajectories](Images/tsla-multiple-stock-trajectories.png)

* The last row of the DataFrame containing the `252 * 3` records of closing prices for each simulation contains the closing prices of `1000` different stock price trajectories on the last day of the project `252 * 3` trading days or a three-year trading period.

  ![tsla-last-row](Images/tsla-last-row.png)

* The frequency distribution histogram showcases the distribution of potential stock price outcomes for `TSLA` on the last day of the projected three-year trading period. Notice that the distribution is skewed to the right and has a rather large range of values on the tail of the distribution.

  ![tsla-frequency-distribution](Images/tsla-frequency-distribution.png)

* The `value_counts` function with its `bin` parameter set to `20`, used in conjunction with the `len` function, can be used to confirm the probability distribution of particular ranges of `TSLA` stock price outcomes.

  ![tsla-value-counts-probability-distribution](Images/tsla-value-counts-probability-distribution.png)

* The `95%` confidence interval suggests an interval in which 95% of stock price projections for `TSLA` are likely to lie. The lower and upper bounds suggest that there is a 95% chance that `TSLA` stock price over the next thee trading years will fall within the range of `$6.47–$402.74`.

  ![tsla-confidence-interval](Images/tsla-confidence-interval.png)

* Calculating the cumulative returns of the ending lower and upper bound prices for `TSLA` stock over the next three years and multiplying by an initial investment of `$10,000` provides a `95%` confidence interval in terms of capital investment.

  ![tsla-investment-confidence-interval](Images/tsla-investment-confidence-interval.png)

---

### 16. Instructor Do: Intro to Portfolio Forecasting (10 min)

At this point, students have executed Monte Carlo simulations; learned to interpret frequency distributions, probability distributions, and confidence intervals; and realized how to apply Monte Carlo simulations to forecast the future prices (and corresponding returns) of individual stocks. Now, students will take their journey one step further and learn how to apply Monte Carlo simulations to forecast the returns of a portfolio, which can be comprised of either all stocks or a combination of multiple asset classes such as stocks and bonds.

Present the following questions and answers regarding portfolio forecasting:

* What is portfolio forecasting?

  > Portfolio forecasting is the process of projecting the future performance of a portfolio and attempting to analyze its most probable outcome, or in this case, cumulative return as well as the portfolio's range of potential cumulative returns and their corresponding probabilities of occurring.

* How is portfolio forecasting done?

  > Similar to the forecasting of a stock's price trajectory, Monte Carlo simulations are applied to forecast the potential price trajectories of the individual stocks that comprise the portfolio. Then the series of returns (for example, daily, weekly, monthly) of each stock is calculated and multiplied by the corresponding weights within the portfolio to output the portfolio's series of returns. Finally, the series of returns for the portfolio are used to generate the cumulative returns, which can then be multiplied by an investment amount to determine the portfolio performance in terms of capital.

* Why is portfolio forecasting performed?

  > Similar to forecasting an individual stock's price trajectory to get a sense of the possibilities and corresponding probabilities of where its price could move, forecasting a portfolio is of the same reasoning. Doing so helps to analyze the potential risk and likelihood that a portfolio's performance can deviate from the expected result.

* Who is performing portfolio forecasting?

  > Portfolio managers, quantitative analysts, retirement planners are just some of many who need to forecast the future performance of a portfolio to gauge the potential risk of investment.

Ask the students if they have any questions or concerns before moving on.

---

### 17. Instructor Do: Portfolio Forecasting (10 min)

In this activity, students ascend to the final step and learn to project not one, but many, future stock prices using Monte Carlo simulations to calculate the daily and cumulative returns of a multiweighted portfolio. Then analyze and plot the frequency and probability distributions of potential ending cumulative returns to assess the investment risk of the portfolio.

**Files:**

* [portfolio_forecasting.ipynb](Activities/09-Ins_Portfolio_Forecasting/Solved/portfolio_forecasting.ipynb)

Walk through the solution and highlight the following:

* The `get_historical_data` function of the `iexfinance` SDK can provide stock price data for more than one ticker in a single API call. Supplying a list of tickers with the `output_format` parameter set to `pandas` returns a multilevel index DataFrame.

  ![iex-multi-level-index](Images/iex-multi-level-index.png)

* To drop specific columns of a multilevel index DataFrame, use the `drop` function with the `level` parameter to specify the *level* of the DataFrame.

  ![drop-multi-level-index-columns](Images/drop-multi-level-index-columns.png)

* Access the Series of values of each multilevel index column using additional square bracket key notation to represent the additional levels.

  ![multi-level-index-key-notation](Images/multi-level-index-key-notation.png)

* The Monte Carlo simulation projects the stock price trajectory for `JNJ` and `MU` over the course of `252` trading days and returns a DataFrame of `252` records representing each simulated day's closing price. Simulated stock prices are projected by randomly selecting a daily return based off of a normal probability distribution, derived from sample means and standard deviations, and multiplying `1 + np.random.normal(avg_daily_return, std_dev_daily_return)` by the preceding day's closing price. A DataFrame of `252` simulated trading days is returned and the daily returns are calculated using the `pct_change` function.

  ```python
  # Set number of simulations and trading days
  num_simulations = 1000
  num_trading_days = 252

  # Set last closing prices of `JNJ` and `MU`
  jnj_last_price = df['JNJ']['close'][-1]
  mu_last_price = df['MU']['close'][-1]

  # Initialize empty DataFrame to hold simulated prices for each simulation
  simulated_price_df = pd.DataFrame()
  portfolio_cumulative_returns = pd.DataFrame()

  # Run the simulation of projecting stock prices for the next trading year, `1000` times
  for n in range(num_simulations):

      # Initialize the simulated prices list with the last closing price of `JNJ` and `MU`
      simulated_jnj_prices = [jnj_last_price]
      simulated_mu_prices = [mu_last_price]

      # Simulate the returns for 252 days
      for i in range(num_trading_days):

          # Calculate the simulated price using the last price within the list
          simulated_jnj_price = simulated_jnj_prices[-1] * (1 + np.random.normal(avg_daily_return_jnj, std_dev_daily_return_jnj))
          simulated_mu_price = simulated_mu_prices[-1] * (1 + np.random.normal(avg_daily_return_mu, std_dev_daily_return_mu))

          # Append the simulated price to the list
          simulated_jnj_prices.append(simulated_jnj_price)
          simulated_mu_prices.append(simulated_mu_price)

      # Append a simulated prices of each simulation to DataFrame
      simulated_price_df["JNJ prices"] = pd.Series(simulated_jnj_prices)
      simulated_price_df["MU prices"] = pd.Series(simulated_mu_prices)

      # Calculate the daily returns of simulated prices
      simulated_daily_returns = simulated_price_df.pct_change()
  ```

* The portfolio weights are multiplied against the values of each column and totaled for each index of the DataFrame. For example, a `0.01` or `1%` daily return in `JNJ` and a `0.005` or `0.5%` daily return in `MU` on the `1st` simulated trading day would constitute a portfolio return of `(0.6 * 0.01) + (0.4 * 0.005) = 0.008` or `0.8%` daily return for that day.

  ```python
      # Set the portfolio weights (60% JNJ; 40% MU)
      weights = [0.60, 0.40]

      # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
      portfolio_daily_returns = simulated_daily_returns.dot(weights)
  ```

* After portfolio daily returns are calculated, cumulative returns are then determined by using the `cumprod` function; the `fillna` function applies a specified number to any instances of `NaN` values within the DataFrame. Cumulative portfolio returns are then added to each column of a DataFrame to represent the simulated cumulative portfolio returns for each simulation.

  ```python
      # Calculate the normalized, cumulative return series
      portfolio_cumulative_returns[n] = (1 + portfolio_daily_returns.fillna(0)).cumprod()

  # Print records from the DataFrame
  portfolio_cumulative_returns.head()
  ```

  ![monte-carlo-results](Images/monte-carlo-results.png)

* Plotting the cumulative portfolio return trajectories for each simulation displays the many possibilities of how the portfolio could perform over the next `252` trading days.

  ![portfolio-returns-simulation-plot](Images/portfolio-returns-simulation-plot.png)

* The last row of the DataFrame containing simulated cumulative portfolio returns represents the total (or cumulative) performance of the portfolio on the 252nd trading day of each simulation.

  ![portfolio-cumulative-returns-last-row](Images/portfolio-cumulative-returns-last-row.png)

* Plotting a frequency distribution histogram of `10` bins and calculating a probability distribution of `10` bins displays the potential outcomes of ending cumulative portfolio returns.

  ![portfolio-cumulative-returns-frequency-distribution](Images/portfolio-cumulative-returns-frequency-distribution.png)

* Calculating a confidence interval of cumulative portfolio returns and multiplying the lower and upper bounds by an investment amount outputs a confidence interval of ending investment performance in the portfolio.

  ![portfolio-cumulative-returns-confidence-interval](Images/portfolio-cumulative-returns-confidence-interval.png)

---

### 18. Students Do: Financial Forecasting Part 3 (15 min)

In this activity, students execute a Monte Carlo simulation to forecast the potential ranges of cumulative returns for a portfolio, based on the simulated closing prices of the stocks that comprise it, to determine the investment risk of the portfolio.

**Instructions:**

* [README.md](Activities/10-Stu_Financial_Forecasting_Pt_III/README.md)

**Files:**

* [financial_forecasting_part_3.ipynb](Activities/10-Stu_Financial_Forecasting_Pt_III/Unsolved/financial_forecasting_part_3.ipynb)

### 19. Instructor Do: Review Financial Forecasting Part 3 (5 min)

**Files:**

* [financial_forecasting_part_3.ipynb](Activities/10-Stu_Financial_Forecasting_Pt_III/Solved/financial_forecasting_part_3.ipynb)

Open the solution and explain the following:

* This following Monte Carlo simulation is a culmination of all of the previous activities regarding financial forecasting: simulating a single instance of a stock price trajectory, simulating multiple stock price trajectories to determine probable outcomes of future stock price, and simulating calculated cumulative portfolio returns to analyze the probability of potential future performance assess investment risk.

  ```python
  # Set number of simulations and trading days
  num_simulations = 1000
  num_trading_days = 252 * 3

  # Set last closing prices of `TSLA` and `SPHD`
  tsla_last_price = df['TSLA']['close'][-1]
  sphd_last_price = df['SPHD']['close'][-1]

  # Initialize empty DataFrame to hold simulated prices for each simulation
  simulated_price_df = pd.DataFrame()
  portfolio_cumulative_returns = pd.DataFrame()

  # Run the simulation of projecting stock prices for the next trading year, `1000` times
  for n in range(num_simulations):

      # Initialize the simulated prices list with the last closing price of `TSLA` and `SPHD`
      simulated_tsla_prices = [tsla_last_price]
      simulated_sphd_prices = [sphd_last_price]

      # Simulate the returns for 252 * 3 days
      for i in range(num_trading_days):

          # Calculate the simulated price using the last price within the list
          simulated_tsla_price = simulated_tsla_prices[-1] * (1 + np.random.normal(avg_daily_return_tsla, std_dev_daily_return_tsla))
          simulated_sphd_price = simulated_sphd_prices[-1] * (1 + np.random.normal(avg_daily_return_sphd, std_dev_daily_return_sphd))

          # Append the simulated price to the list
          simulated_tsla_prices.append(simulated_tsla_price)
          simulated_sphd_prices.append(simulated_sphd_price)

      # Append a simulated prices of each simulation to DataFrame
      simulated_price_df["TSLA prices"] = pd.Series(simulated_tsla_prices)
      simulated_price_df["SPHD prices"] = pd.Series(simulated_sphd_prices)

      # Calculate the daily returns of simulated prices
      simulated_daily_returns = simulated_price_df.pct_change()

      # Set the portfolio weights (75% TSLA; 25% SPHD)
      weights = [0.25, 0.75]

      # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
      portfolio_daily_returns = simulated_daily_returns.dot(weights)

      # Calculate the normalized, cumulative return series
      portfolio_cumulative_returns[n] = (1 + portfolio_daily_returns.fillna(0)).cumprod()

  # Print records from the DataFrame
  portfolio_cumulative_returns.head()
  ```

  ![portfolio-monte-carlo-simulation-results](Images/portfolio-monte-carlo-simulation-results.png)

* The plot shows the different potential performances of the `25–75` weighed portfolio of `TSLA` and `SPHD` over the next three trading years.

  ![portfolio-monte-carlo-simulation-plot](Images/portfolio-monte-carlo-simulation-plot.png)

* The last row of the DataFrame containing the cumulative portfolio returns of each simulation represents the ending cumulative returns of the portfolio of each simulation. Plotting a frequency distribution and calculating a probability distribution shows the most expected range of cumulative returns for the portfolio.

  ![portfolio-frequency-distribution](Images/portfolio-frequency-distribution.png)

* Calculating a `95%` confidence interval of potential cumulative portfolio returns as well as potential investment performance showcases the range of cumulative portfolio returns and investment results that have a `95%` likelihood of occurring.

  ![portfolio-confidence-interval](Images/portfolio-confidence-interval.png)

---

### 20. Recap (25 min)

Is this the end, or is it just another iteration of a simulation? It's actually the end! Welcome to today's finish line.

The content in this lesson is probably the most difficult material students have digested so far. Students were required to whip out every FinTech skill and asset they've learned. This lesson was involved, including portfolio optimization (calculation of returns, standard deviation, risk, etc.) and portfolio forecasting (Monte Carlo, probability distributions, confidence trajectories, and forecasting). And this doesn't even include the Python and Pandas skills they had to leverage!

Make sure students can recognize and acknowledge their accomplishments. Communicate that

* They've added another tool to their API-SDK tool belt: the IEX SDK, which is a great resource for historical stock data and financial functions.

* They've taken yet another deep dive into statistics, learning how to create, calculate, and interpret probability distributions. This includes using mean, standard deviation**, **daily returns, Numpy's random data generators, and histograms in order to implement and visualize portfolio simulations.

* They've plotted the price trajectory of a stock prices and returns using single and multiple Monte Carlo simulations.

* They've forecast average daily return volatility at the stock and portfolio level.

* They've assessed the risk of investing in a stock by predicting the probability of stock prices rising or falling over time.

* They've put the Fin in FinTech, and they're just getting started!

Give students a space to emotionally release. Use this activity as a way to gauge student confidence, frustration, and stress levels.

* Ask students to summarize how they're feeling with a one-word emotion. Ask for volunteers first. If no one volunteers, initiate the activity by using one word to convey how you're feeling, and then go round-robin. Gauge students for verbal and nonverbal cues of stress and confusion (e.g., withdrawal from the activity or isolation, irritability or impatience, chronic worrying, pessimistic attitude, and restlessness).

  **Answer**: Relieved

  **Answer**: Excited

  **Answer:** Confused

  **Answer:** Empowered

  **Answer:** Stressed

  **Answer:** Doubtful

* Indicate to students that no matter what they're feeling, either excited and empowered or stressed and doubtful, they've come a long way. Also underscore that they're not alone in their feelings or the journey. Portfolio simulations are no joke, and results can easily be misinterpreted or corrupted, which is why the best of the best are the ones executing simulations.

* Emphasize that students can reach out individually or attend office hours to ask questions, discuss the activities in the lesson, or just release emotionally.

Use the remaining time to get a head start on office hours. Allow students to ask questions about this lesson, the overall unit, or the homework.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
