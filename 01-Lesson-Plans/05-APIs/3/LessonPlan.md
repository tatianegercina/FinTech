## 5.3 Lesson Plan: Track to the Future!

---

### Overview

Today's class will focus on the notion of using Monte Carlo simulations to forecast results and make confident predictions supported by statistical evidence. A Monte Carlo simulation is an essential tool for emulating a real-world use case that involves a degree of randomness surrounding an event or outcome. It seeks to iterate `n` number of times to find the most probable result of a variable event, as well as the range of effects and their corresponding probabilities of occurring.

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

* Note that, due to the random numbers used in Monte Carlo simulations, a new execution of Monte Carlo simulations in class may produce different results than what you see in the lesson plan.  Selecting different dates than those used in the lesson plan will also produce different results, as the stock data fetched will be different.

* In this class, the concept of random numbers and random number generators is introduced and applied using `numpy.random`. A random seed (`random.seed(3)`) has been set for all the Instructor's activities to ensure reproducibility. Be aware of this during your coding demos, and explain the purpose of using a random seed for prototyping but not for deploying models.

* In the student activities using `numpy.random`, the random seed is not set to allow students to experience randomness.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [5.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=629c0f35-efd0-4081-a916-aab4015c80e0) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 5.3 Slides](https://docs.google.com/presentation/d/1gTBrh_ac0HgXx91UFS3YUiWrSUuv3lorKJZja5qc5p0/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class and Intro to Monte Carlo Simulations (10 min)

Energize your students and welcome them to the third day of APIs! Today is the day where students move from historical to future-oriented analysis. Time to look into the crystal ball!

Cover the following points:

* The previous lessons focused on API calls and showcased the Alpaca API to exemplify that you can leverage the power of external datasets and functionality.

* Today's focus is on using APIs to access stock data that can be manipulated to serve individual needs. You should feel empowered as you are learning how you can use other curated datasets to analyze and generate insights on their own.

* You should be prepared to push your mindset from historically analyzing portfolio returns and their performances to charting the possible paths a portfolio may take in the future, thereby making educated predictions on where the portfolio could end up.

Open the lesson slides, move to the "Monte Carlo Simulations" section and highlight the following:

* Today, we will combine what we’ve learned so far on using APIs to pull in stock data, to forecast single stock/portfolio returns using Monte Carlo simulations.

* Simulations will require a switch from historical analysis to predicting the future.

* By the end of the lesson, Monte Carlo simulations will have predicted future stock prices and therefore forecast the potential stock's returns of an initial investment, either as a single stock investment or as an investment in a portfolio.

Continue with the slides by moving to the "Simulations" section. Ease students into the notion of this type of simulation by presenting the following questions and answers:

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

* Normal distributions are particularly useful in finance because they adequately approximate the volatility of stock prices, forex rates, and other commodities. For example, the daily price change (in percent) from a high volatility stock such as Tesla and a low volatility stock such as Coca-Cola can both demonstrate normal distributions despite the differences in company size, customer base, stock price, and market share. We can visualize the normal distribution of these stocks using Pandas as follows:

```python
# Visualize the distribution of percent change in closing price for both stocks using a density plot
df_daily_returns.plot.density()
```
![Density_Distribution.plot](Images/Density_Distribution.png)

Explain to students that we are going to use probability distributions to visually analyze the outcomes forecasted by Monte Carlo simulations, but first, it's time to learn how to fetch stock data and visualize its distribution using Python.

Answer any questions before moving on.

---

### 3. Instructor Do: Getting into Probability Distributions Using Python (15 min)

**Corresponding Activity:** [01-Ins_Getting_into_Probability_Distributions](Activities/01-Ins_Getting_into_Probability_Distributions)

In this activity, students will learn how to retrieve historical stock data using Alpaca and visualize its distribution.

**Files:**

* [stock_price_normal_distribution.ipynb](Activities/01-Ins_Getting_into_Probability_Distributions/Solved/stock_price_normal_distribution.ipynb)

Open the unsolved version of the Jupyter notebook, live code the solution, and highlight the following:

* Before getting started with Monte Carlo simulations, it's important to learn how you can visually analyze the distribution of data using Python.

* Today, we will work with stock data to forecast possible outcomes using Monte Carlo simulations. As a first step, let's learn how to use histograms and density plots to see the probability distributions in action.

* Let's start by importing the required libraries and loading our Alpaca keys from the environment variables stored in the `.env.` file.

  ```python
  # Import libraries and dependencies
  import os
  import pandas as pd
  import alpaca_trade_api as tradeapi

  # Load .env environment variables
  from dotenv import load_dotenv
  load_dotenv()

  %matplotlib inline
  ```

* Next, we create the Alpaca API object.

  ```python
  # Set Alpaca API key and secret
  alpaca_api_key = os.getenv("ALPACA_API_KEY")
  alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

  # Create the Alpaca API object
  alpaca = tradeapi.REST(
      alpaca_api_key,
      alpaca_secret_key,
      api_version="v2"
  )
  ```

* Let's continue by fetching stock price data over one year for Tesla (`TSLA`) and Coca-Cola (`KO`) using the Alpaca SDK.

**Note:** Analysis and results may vary if you change these dates.  If you decide to run the code with different dates during class, we recommend that you validate the results prior.

  ```python
  # Set the Tesla and Coca-Cola tickers
  ticker = ["TSLA","KO"]

  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes of 1 year, between now and 365 days ago.
  start_date = pd.Timestamp("2019-05-01", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-01", tz="America/New_York").isoformat()

  # Get 1 year's worth of historical data for Tesla and Coca-Cola
  df_ticker = alpaca.get_barset(
      ticker,
      timeframe,
      start=start_date,
      end=end_date
  ).df

  # Display sample data
  df_ticker.head(10)
  ```

  ![tsla-ko-yearly-stock-prices](Images/tsla-ko-yearly-stock-prices.png)

* To analyze the probability distribution of these stock prices, we will create a new DataFrame containing only the closing prices over one year, and we will compute the daily returns.

  ```python
  # Create and empty DataFrame for closing prices
  df_closing_prices = pd.DataFrame()

  # Fetch the closing prices of KO and TSLA
  df_closing_prices["KO"] = df_ticker["KO"]["close"]
  df_closing_prices["TSLA"] = df_ticker["TSLA"]["close"]

  # Drop the time component of the date
  df_closing_prices.index = df_closing_prices.index.date

  # Compute daily returns
  df_daily_returns = df_closing_prices.pct_change().dropna()

  # Display sample data
  df_daily_returns.head(10)
  ```

  ![tsla-ko-closing-prices](Images/tsla-ko-closing-prices.png)

* At a glance, we can get an idea of how the values are distributed by generating the descriptive statistics of a DataFrame using the `describe()` function.

  ```python
  # Generate descriptive statistics
  df_daily_returns.describe()
  ```

  ![descriptive-stats](Images/descriptive-stats.png)

* Observing the standard deviation (`std`), you can verify how far the values are from the mean. A bigger standard deviation indicates that values are further away from the mean, so the stock prices tend to be more volatile. On the contrary, with lower standard deviation, values are closer to the mean, and stock prices would be less volatile.

* We can also visually analyze the probability distribution by plotting a histogram.

  ```python
  # Visualize distribution of Tesla percent change in closing price using a histogram plot
  df_daily_returns["TSLA"].plot.hist()
  ```

  ![Tesla Closing Pct Change Distribution](Images/Tesla_Closing_Distribution.png)

  ```python
  # Visualize distribution of Coca-Cola percent change in closing price using a histogram plot
  df_daily_returns["KO"].plot.hist()
  ```

  ![Coca-Cola Closing Pct Change Distribution](Images/CCola_Closing_Distribution.png)

* Notice how in both histogram plots, the distributions resemble our "bell curve" shape of a normal distribution? That's because the percent change in daily price for both companies have similar probability distributions - smaller changes in daily price are *far* more likely than large swings in daily price (although they are not impossible!).

* Besides a histogram, we can use a density plot to visualize a smoother shape of the probability distribution.

  ```python
  # Visualize the distribution of percent change in closing price for both stocks using a density plot
  df_daily_returns.plot.density()
  ```

  ![Density Distribution of both stocks](Images/Density_Distribution.png)

* A density plot is a variation of the histogram that uses a statistical technique called [kernel smoother](https://en.wikipedia.org/wiki/Kernel_smoother) to plot values in the form of a smooth shape. An advantage of density plots over histograms is that they allow a more straightforward determination of the distribution shape since they are not affected by the number of bins.

* When we overlay the two distributions together using the density plot, we can see that Coca-Cola's distribution has a higher frequency of small daily changes compared to Tesla. This is due to the volatility of a stock - the less volatile the stock, the smaller the standard deviation value. A smaller standard deviation means that the stock is less likely to have large (positive or negative) changes in value.

* Probability distributions such as the normal distribution help us make educated guesses about what might happen to a stock or commodity in the future. When it comes to the Monte Carlo simulations, the model will randomly select changes that fit within the normal distribution to simulate real-world data best!

Explain to students that despite most pricing distributions not being perfectly normal, as a FinTech professional it's important to understand what a normal distribution is since it's the most common type of distribution assumed in technical analysis of a stock, commodity, or other assets.

Answer any questions before moving on.

---

### 4. Students Do: Decisive Distributions (20 min)

**Corresponding Activity:** [02-Stu_Decisive_Distributions](Activities/02-Stu_Decisive_Distributions)

In this activity, students will gain hands-on experience fetching historical stock data and plotting distributions to make investment decisions.

**Instructions:**

* [README.md](Activities/02-Stu_Decisive_Distributions/README.md)

**Files:**

* [Decisive_Distributions.ipynb](Activities/02-Stu_Decisive_Distributions/Unsolved/Decisive_Distributions.ipynb)

---

### 5. Instructor Do: Review Decisive Distributions (10 min)

**Files:**

* [Decisive_Distributions.ipynb](Activities/02-Stu_Decisive_Distributions/Solved/Decisive_Distributions.ipynb)

Open the solved version of the Jupyter notebook and explain the following:

* After importing the required libraries and the Alpaca keys, the next step is to read stock data from over one year.

  **Note:** Analysis and results may vary if you change these dates.  If you decide to run the code with different dates during class, we recommend that you validate the results prior.

  ```python
  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes of 1 year, between now and 365 days ago.
  start_date = pd.Timestamp("2019-05-01", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-01", tz="America/New_York").isoformat()

  # Set the stock tickers
  tickers = ["SPY", "LUV", "DIS", "AAPL", "SBUX", "WORK"]

  # Get 1 year's worth of historical data for all stocks
  df_ticker = api.get_barset(
      tickers,
      timeframe,
      start=start_date,
      end=end_date,
  ).df
  ```

* Until now, we retrieved stock data from one or two tickers; note that it's possible to fetch data from several tickers just by adding the symbols to the `tickers` list.

* Next, we create a new DataFrame containing only closing prices since we want to analyze their distribution to compare stock volatility.

  ```python
  # Create and empty DataFrame for closing prices
  df_closing_prices = pd.DataFrame()

  # Fetch the closing prices for all the tickers
  for ticker in tickers:
      df_closing_prices[ticker] = df_ticker[ticker]["close"]

  # Drop the time component of the date
  df_closing_prices.index = df_closing_prices.index.date

  # Display sample data
  df_closing_prices.head()
  ```

  ![tickers-closing-prices](Images/tickers-closing-prices.png)

* In this analysis, the key to visually assess stock volatility is to compute the daily returns of closing prices, so we use the `pct_change()` function.

  ```python
  # Compute daily returns
  df_daily_returns = df_closing_prices.pct_change().dropna()
  ```

* The first tool we use to analyze stock volatility is a histogram. This plot will allow us to have a picture of the probability distribution. We set the argument `alpha=06` in the histogram to make the plot more comfortable to read.

  ```python
  # Visualize the distribution of daily returns across all stocks using a histogram plot
  df_daily_returns.plot.hist(alpha=0.5)
  ```

  ![tickers-histogram](Images/tickers-histogram.png)

* By observing the histogram, you can note that stock data for all the tickers is normally distributed, however, it's a bit hard to read this plot to decide the most and the least volatile stock.

* Let's create a density plot to have a better understanding of stock volatility.

  ```python
  # Visualize the distribution of daily returns across all stocks using a density plot
  df_daily_returns.plot.density()
  ```

  ![tickers-density-plot](Images/tickers-density-plot.png)

* This is much better, right!? From the density plot, we can observe that the most volatile stock is `WORK`, and the least volatile stock is `SPY`. Using these two plots, we can start planning an investing strategy by setting different weights for each ticker in a portfolio.

* It would be great to forecast the future outcomes of a portfolio, right? That's where Monte Carlo simulations come into action.

Answer any questions before moving on.

---

### 6. Instructor Do: Portfolio Forecasting Using Monte Carlo Simulations (20 min)

**Corresponding Activity:** [03-Ins_Portfolio_Forecasting_Monte_Carlo](Activities/03-Ins_Portfolio_Forecasting_Monte_Carlo)

Now that students understand what a probability distribution is and how to recognize a normal distribution in financial data, in this activity, students will learn about Monte Carlo simulations. Although there are many use-cases for Monte Carlo simulations, in finance, we use Monte Carlo simulations for portfolio forecasting.

**Files:**

* [portfolio_forecasting.ipynb](Activities/03-Ins_Portfolio_Forecasting_Monte_Carlo/Solved/portfolio_forecasting.ipynb)

* [MCForecastTools.py](Activities/03-Ins_Portfolio_Forecasting_Monte_Carlo/Solved/MCForecastTools.py)

Open the lesson slides, move to the "Portfolio Forecasting Using Monte Carlo Simulations" section, and highlight the following:

* Portfolio forecasting is the process of projecting a portfolio's future performance and attempting to analyze its most probable outcome.

* Portfolio forecasting can be done using Monte Carlo simulations to forecast the potential price trajectories of the individual stocks that comprise the portfolio. In our case, we will estimate the cumulative return, as well as the portfolio's range of potential cumulative returns, including their corresponding probabilities of occurring. Doing so helps to analyze the potential risk and likelihood that a portfolio's performance can deviate from the expected result.

* Portfolio forecasting is utilized across the FinTech industry - portfolio managers, quantitative analysts, and retirement planners are just some of many who need to forecast the future performance of a portfolio to gauge the potential risk of investment. Regardless if a portfolio contains stocks, bonds, cryptocurrencies or any other commodities, as long as we can retrieve historical price data, we can use the Monte Carlo simulation to project future performance.

Explain to students, that in order to perform portfolio forecasting in Python, we will need two things, historical financial data from our portfolio to input into the simulation and a framework to run our Monte Carlo simulation. Highlight the following:

* For our historical portfolio data, we can either read in spreadsheet data into a Pandas DataFrame using the `pd.read_csv()` method, or query historical price information using a financial API. For this lesson, we will query our historical financial data using the Alpaca API.

* As for the Monte Carlo framework, you can go through its algorithm and implement it manually using Python. You can also use a library that encapsulates the logic of the Monte Carlo method and focuses your efforts on analyzing the predicted outcomes.

* To carry out portfolio forecasting, we provide you with a library called `MCForecastTools` that contains functions to help build Monte Carlo simulations and will allow you to test several future scenarios by setting different parameters.

Since the waiting time for running the Monte Carlo simulation could be long, open the solved version of the Jupyter notebook, follow the code in each cell and highlight the following.

* Let's pretend that we are looking to add Microsoft (`MSFT`) and Coca-Cola (`KO`) stock to our portfolio. If we were to invest $10,000 worth of stock today, how much would it be worth in `5` years? `10` years? Let's find out.

* After importing our dependencies and setting up the Alpaca API instance, our next step is to query the Alpaca API to retrieve the closing stock price of Microsoft and Coca-Cola over the past `3` years.

  ```python
  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes between now and 3 years ago.
  start_date = pd.Timestamp("2017-05-01", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-01", tz="America/New_York").isoformat()

  # Set the ticker information
  tickers = ["MSFT","KO"]

  # Get 3 year's worth of historical price data for Microsoft and Coca-Cola
  df_ticker = api.get_barset(
      tickers,
      timeframe,
      start=start_date,
      end=end_date
  ).df

  # Display sample data
  df_ticker.head()
  ```

  ![Alpaca 3-year query](Images/Alpaca_query.png)

* If we look at the index of our DataFrame, we can see that we correctly queried daily stock price from May of 2017 through May of 2020. Now that we have the historical stock information, it is time to build our Monte Carlo simulation instance. Let's take a look at the documentation of the `MCSimulation` module of the `MCForecastTools` library by executing the following command in our notebook:

  ```python
  # Print the documentation of the MCSimulation module of the MCForecastTools library
  ?MCSimulation
  ```

  ![MCSimulation docstring](Images/MCSimulation_docstring.png)

* The `MCSimulation` module contains multiple functions and parameters that help us easily configure, run, and evaluate a Monte Carlo simulation using the stock information we previously queried from Alpaca.

* According to the documentation, the `MCSimulation` module requires us to provide a few parameters to configure it properly:

  * **portfolio_data** - our Pandas DataFrame containing historical stock information from our *potential* stock portfolio.

  * **weights** - a list of weights that tell the `MCSimulation` what percentage of our investment goes to each stock.

    * For example, if `weights = [.75,.25]`, than the `MCSimulation` assumes that $7,500 of our $10,000 investment will go to Coca-Cola stock, while $2,500 will go to Microsoft stock.

  * **num_simulation** - the number of simulated samples we want to create.

    * At a minimum, we should try to use `500` samples. However, if we have the computational resources and time, we should try to simulate `1000` samples to ensure that our analysis results are more reliable.

  * **num_trading_days** - the number of trading days to simulate

    * For example, if we wanted to simulate stock price returns after `5` years, we need to multiply 252 (the number of trading days in a year) times five (`252*5`).

* Knowing this information, let's try to create our first instance of `MCSimulation` using a `60/40` split of our $10,000 investment (60% of our $10,000 for buying Coca-Cola stock, 40% for buying Microsoft stock):

  ```python
  # Configuring a Monte Carlo simulation to forecast five years cumulative returns
  MC_fiveyear = MCSimulation(
      portfolio_data = df_ticker,
      weights = [.60,.40],
      num_simulation = 500,
      num_trading_days = 252*5
  )
  ```

* After creating the `MCSimulation` instance, the daily returns are computed. A new DataFrame is created where the instance automatically created a `daily_return` column that calculates the percent change of closing prices for each stock. The `daily_return` column will be the normally distributed variable we use as input for the Monte Carlo simulation. We can preview this new DataFrame using the `portfolio_data` attribute and linking it to the `head()` function.

  ```python
  # Printing the simulation input data
  MC_fiveyear.portfolio_data.head()
  ```

  ![MCSimulation input data](Images/MCSimulation_input_data.png)

**Note:** If you ever get an error when trying to create your `MCSimulation` instance, make sure to read the error message and ensure that your Alpaca API query was successful.

* Using our `MCSimulation` instance, we can run the Monte Carlo simulation using the `calc_cumulative_return()` function.

  ```python
  # Running a Monte Carlo simulation to forecast five years cumulative returns
  MC_fiveyear.calc_cumulative_return()
  ```

  ![5.4-Running-Monte-Carlo-Simulation](Images/Running-Monte-Carlo-Simulation.gif)

* After running all the simulations, a new DataFrame is created.

  ![Monte Carlo simulation output](Images/MCSimulation_simoutput.png)

* At first glance, this DataFrame may not look like anything special, and that is okay. We want to check if the dimensions of the DataFrame make sense to confirm the simulation worked as intended. The `1261` rows represent our `252` trading days times `5` years (plus a starting value of 1), and the `500` columns represent the `500` simulated samples - it looks like the simulation ran correctly!

**Important:** The simulation process includes using a random number generator, so your simulated values will vary from this example. However, the functions in the code and the interpretations of the data will be the same.

Explain to students that in order to visualize and analyze the data generated by the Monte Carlo simulation, we can use the other built-in functions of the `MCSimulation` module. First, we take a look at the `500` samples across the entire simulated time using the `plot_simulation()` function.

```python
# Plot simulation outcomes
line_plot = MC_fiveyear.plot_simulation()

# Save the plot for future usage
line_plot.get_figure().savefig("MC_fiveyear_sim_plot.png", bbox_inches="tight")
```

![MC five year simulation plot](Images/MC_fiveyear_sim_plot.png)

Highlight to students that if they want to use this plot for a report or presentation, they can save it as an image using the `get_figure()` function and linking the `savefig()` function.

Continue the demo by highlighting the following about the analysis of the Monte Carlo simulation results.

* Looking at our line plot, we see the trajectory of each and every sample across all of the simulated trading days. The x-axis of our plot shows the trading days, while the y-axis is the portfolio's cumulative return. When we are looking at cumulative returns, a value of `1` indicates no change in the portfolio value.

* According to our plot, we can see there are some cumulative returns of `2`, `6`, or even `12` times the original value, but it is hard for us to tell what the distribution of values looks like from this perspective. Alternatively, we can look at the distribution of cumulative returns using the `plot_distribution()` function.

  ```python
  # Plot probability distribution and confidence intervals
  dist_plot = MC_fiveyear.plot_distribution()

  # Save the plot for future usage
  dist_plot.get_figure().savefig('MC_fiveyear_dist_plot.png',bbox_inches='tight')
  ```

  ![MC five year distribution plot](Images/MC_fiveyear_dist_plot.png)

* Our new plot visualizes the final cumulative return across all the `500` simulated samples using a histogram. In this plot, our x-axis represents the final cumulative return values. In contrast, the y-axis represents the frequency of each "bin" of final cumulative values out of the total `500` simulations.

* The red bars in this plot help us to visualize the **95% confidence interval**. The **95% confidence interval** represents the range of values we can expect to observe `95%` of the time. When it comes to our Monte Carlo simulations, we simulated a normal distribution; therefore the `95%` confidence interval approximates that most of our simulated returns will come from the center of the bell curve rather than the far tail ends.

* According to our plot, we can see that `95%` of the time, we can expect a cumulative return of approximately one to seven times our original investment amount. To calculate these approximate returns directly, we can use the following code.

* First, we compute the summary statistics from the Monte Carlo simulation results using the `summarize_cumulative_return()` function.

  ```python
  # Fetch summary statistics from the Monte Carlo simulation results
  tbl = MC_fiveyear.summarize_cumulative_return()

  # Print summary statistics
  print(tbl)
  ```

  ![MCSimulation calc table](Images/MCSimulation_calc_tbl.png)

* Next, we use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $10,000 investments in Coca-Cola and Microsoft stocks.

  ```python
  # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $10,000 investments in Coca-Cola and Microsoft stocks
  ci_lower = round(tbl[8]*10000,2)
  ci_upper = round(tbl[9]*10000,2)

  # Print results
  print(f"There is a 95% chance that an initial investment of $10,000 in the portfolio"
        f" over the next 5 years will end within in the range of"
        f" ${ci_lower} and ${ci_upper}")
  ```

  ![MCSimulation print statement](Images/MCSimulation_calc_result.png)

* Looking at our calculated portfolio values, we see that there is a `95%` chance that our investment will grow over the next `5` years at a fairly substantial rate. Although this is fantastic news, it is important to note that stocks have observed historical growth and volatility from `2017` to `2020`. As a result, our input data (and subsequent probability distribution) may be overestimating the `95%` confidence interval of final cumulative return when simulating data over a more extended period of time. Therefore a good rule of thumb is to query and provide `1` year of historical portfolio data for every `1` or `2` years of simulated data.

Explain to students that as they become more familiar with programming and running Monte Carlo simulations in Python, they can tweak the code provided in the `MCForecastTools` library to create more robust simulations and more powerful visualizations!

Answer any questions before moving on.

---

### 7. BREAK (40 min)

---

### 8. Students Do: Three Stock Monte (30 min)

**Corresponding Activity:** [04-Stu_Three_Stock_Monte](Activities/04-Stu_Three_Stock_Monte)

In this activity students will use the `MCForecastTools` toolkit to determine how much of each stock is worth purchasing in a portfolio in order to maximize the chances of profit.

You can have students working in pairs for this activity.

**Instructions:**

* [README.md](Activities/04-Stu_Three_Stock_Monte/README.md)

**Files:**

* [Three_Stock_Monte.ipynb](Activities/04-Stu_Three_Stock_Monte/Unsolved/Three_Stock_Monte.ipynb)

* [MCForecastTools.py](Activities/04-Stu_Three_Stock_Monte/Unsolved/MCForecastTools.py)

---

### 9. Instructors Do: Review Three Stock Monte (10 min)

**Files:**

* [Three_Stock_Monte.ipynb](Activities/04-Stu_Three_Stock_Monte/Solved/Three_Stock_Monte.ipynb)

* [MCForecastTools.py](Activities/04-Stu_Three_Stock_Monte/Solved/MCForecastTools.py)

Congratulate students on having successfully built, analyzed, and visualized their own Monte Carlo simulation data!

Open the solved version of the Jupyter notebook and explain the following:

* After importing our dependencies and setting up the Alpaca API instance, our next step is to query the Alpaca API to retrieve the closing stock price of AT&T (`T`), Nike (`NKE`), and Exxon Mobil (`XOM`) over the past five years.

  ```python
  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes between now and 3 years ago.
  start_date = pd.Timestamp("2015-05-01", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-01", tz="America/New_York").isoformat()

  # Set the ticker information
  tickers = ["T","NKE","XOM"]

  # Get 3 year's worth of historical price data for Microsoft and Coca-Cola
  df_ticker = api.get_barset(
      tickers,
      timeframe,
      start=start_date,
      end=end_date
  ).df
  ```

* Next, we forecast five-year portfolio growth with evenly-distributed stock investments using the `MCForecastTools` library. Note that we set the argument `weights = [.33,.33,.33]` to have the same proportion of each stock in the portfolio.

  ```python
  # Configure a Monte Carlo simulation to forecast five years cumulative returns
  MC_even_dist = MCSimulation(
      portfolio_data = df_ticker,
      weights = [.33,.33,.33],
      num_simulation = 1000,
      num_trading_days = 252*5
  )
  ```

* Once we set the parameters for our Monte Carlo simulation, we forecast five years of cumulative returns running `1000` simulations using the `calc_cumulative_return()` function.

  ```python
  # Run a Monte Carlo simulation to forecast five years cumulative returns
  MC_even_dist.calc_cumulative_return()
  ```

* After running the simulation, we can visually analyze the forecasted outcomes for the next five years (`1260` trading days). We can also visualize the probability distribution to have an idea of the range of the possible outcomes.

  ![three-monte-plots](Images/three-monte-plots.png)

* After observing the `95%` confidence intervals in the probability distribution plot, we can deduce that our initial investment will drop by `50%` or increase by `320%`. 

  ![three-monte-confidence-intervals](Images/three-monte-confidence-intervals.png)

* To have an accurate estimate of the range of the possible outcomes, we use the `summarize_cumulative_return()` function to fetch the summary statistics.

  ```python
  # Fetch summary statistics from the Monte Carlo simulation results
  even_tbl = MC_even_dist.summarize_cumulative_return()

  # Print summary statistics
  print(even_tbl)
  ```

  ```text
  count           1000.000000
  mean               1.248977
  std                0.654414
  min                0.260045
  25%                0.807732
  50%                1.102806
  75%                1.503041
  max                4.605321
  95% CI Lower       0.441835
  95% CI Upper       3.108547
  Name: 1260, dtype: float64
  ```

* We use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investment.

  ```python
  # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $15,000 investments in stocks
  even_ci_lower = round(even_tbl[8]*15000,2)
  even_ci_upper = round(even_tbl[9]*15000,2)

  # Print results
  print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
        f" over the next 5 years will end within in the range of"
        f" ${even_ci_lower} and ${even_ci_upper}.")
  ```

  ```text
  There is a 95% chance that an initial investment of $15,000 in the portfolio over the next five years will end within the range of $6627.52 and $46628.21.
  ```

Remind students that the simulation process includes using a random number generator, so their simulated values will vary from this example.

The remainder of steps for this activity consist of simulating different scenarios by changing the proportion of stocks in each scenario. One essential part of these simulations is to set the `weights` argument of the `MCSimulation()` function to the correct values.

For example, to simulate five-year portfolio growth with `60%` AT&T stock, you need to set-up the `MCSimulation` function as follows.

```python
# Configure a Monte Carlo simulation to forecast five years cumulative returns with 60% AT&T stock
MC_att = MCSimulation(
    portfolio_data = df_ticker,
    weights = [.20,.60,.20],
    num_simulation = 1000,
    num_trading_days = 252*5)
```

We set `0.60` in the second position of the array since `T` is the second top column in the `portfolio_data` DataFrame.

Another important aspect of the solution is to create a variable to store the summary statistics for each scenario and the lower and upper `95%` confidence intervals. In the solution file, you will see that we created the following variables.

1. `even_tbl`, `even_ci_lower`, `even_ci_upper`: Stores the statistics of the Monte Carlo simulation with the evenly-weighted stocks.

2. `att_tbl`, `att_ci_lower`, `att_ci_upper`: Stores the statistics of the Monte Carlo simulation with `60%` AT&T stock.

3. `nike_tbl`, `nike_ci_lower`, `nike_ci_upper`: Stores the statistics of the Monte Carlo simulation with `60%` Nike stock.

4. `exxon_tbl`, `exxon_ci_lower`, `exxon_ci_upper`: Stores the statistics of the Monte Carlo simulation with `60%` Exxon Mobil stock.

Finally, to summarize the findings across all four simulations, we use the variables created for each scenario to print the resulting range of the possible outcomes of our $15,000 investment in stocks.

```python
# Even weighted stocks
print("Even weighted stocks")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${even_ci_lower} and ${even_ci_upper}.")
print("*"*50)

# 60% for AT&T
print("60% for AT&T")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${att_ci_lower} and ${att_ci_upper}.")
print("*"*50)

# 60% for Nike
print("60% for Nike")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${nike_ci_lower} and ${nike_ci_upper}.")
print("*"*50)

# 60% for Exxon
print("60% for Exxon")
print(f"There is a 95% chance that an initial investment of $15,000 in the portfolio"
      f" over the next 5 years will end within in the range of"
      f" ${exxon_ci_lower} and ${exxon_ci_upper}.")
print("*"*50)
```

```text
Even weighted stocks
There is a 95% chance that an initial investment of $15,000 in the portfolio over the next 5 years will end within in the range of $6627.52 and $46628.21.
**************************************************
60% for AT&T
There is a 95% chance that an initial investment of $15,000 in the portfolio over the next 5 years will end within in the range of $6834.9 and $33414.49.
**************************************************
60% for Nike
There is a 95% chance that an initial investment of $15,000 in the portfolio over the next 5 years will end within in the range of $4652.03 and $94005.81.
**************************************************
60% for Exxon
There is a 95% chance that an initial investment of $15,000 in the portfolio over the next 5 years will end within in the range of $5184.4 and $27741.01.
**************************************************
```

Explain to students that after looking across all four simulations, the portfolio breakdown with the highest chance of success seems to be the portfolio with a majority of Nike stock. Although all four portfolios have a chance to lose money, the Nike portfolio is roughly the same level of risk with far more upside potential.

Get your students excited about the fact that in this activity, they had an opportunity to use one of the data modeling tools used throughout the FinTech industry for price forecasting and stocks' performance. Highlight that as they progress through the course, they will learn about even more robust models and analytic techniques to help them throughout their careers as FinTech professionals!

Answer any questions before moving on.

---

### 10. Instructor Do: Simulation of Stock Price Trajectory (10 min)

**Corresponding Activity:** [05-Ins_Simulation_of_Stock_Price_Trajectory](Activities/05-Ins_Simulation_of_Stock_Price_Trajectory)

This activity exemplifies the use case where a Monte Carlo simulation can be applied to a historical dataset such as daily closing stock prices, given the assumption that daily closing stock prices have a normal probability distribution. Stock datasets will be pulled in from the Alpaca API and used to generate a Monte Carlo simulation based off a normally distributed random process using the dataset's calculated average and standard deviation of daily returns.

**Files:**

* [stock_price_simulation.ipynb](Activities/05-Ins_Simulation_of_Stock_Price_Trajectory/Solved/stock_price_simulation.ipynb)

* [MCForecastTools.py](Activities/05-Ins_Simulation_of_Stock_Price_Trajectory/Solved/MCForecastTools.py)

Walk through the solution and highlight the following:

* As we learned before, Monte Carlo simulations can be executed on *continuous probabilities* such as normal probability distributions.

* Normal probability distributions showcase the various probabilities of returning a value based on the number of standard deviations it is from the mean (how far the value may lie plus or minus from the average expected value); values far away from the mean are less common while values near the mean are more common. A Monte Carlo simulation uses this characteristic to simulate a random process's potential outcomes with respect to its mean variability.

  ![example-normal-distribution](Images/normal-distribution.png)

* In this demo, we will run a Monte Carlo simulation using a historical dataset of daily closing stock prices, given the assumption that daily closing stock prices have a normal probability distribution.

* The daily closing stock price data will be pulled using the `alpaca-trade-api` SDK. Therefore, we need to import the necessary libraries and dependencies before proceeding.

  ```python
  # Import libraries and dependencies
  import os
  import numpy as np
  import pandas as pd
  import alpaca_trade_api as tradeapi

  %matplotlib inline
  ```

* We use the `get_barset()` function from the `Alpaca` SDK to retrieve a DataFrame of `AAPL` daily stock prices. The `start_date` and `end_date` variables, in this case, are a span of five years - the start date and five years from the start date, respectively. To fetch the stock data correctly, the Alpaca SDK works with dates in ISO format, so we transform the `start_date` and the `end_date` using the `Timestamp` and `isoformat` functions from Pandas.

  ```python
  # Set the ticker
  ticker = "AAPL"

  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes of 5 years from Today
  start_date = pd.Timestamp("2019-05-04", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-04", tz="America/New_York").isoformat()

  # Get 1 year's worth of historical data for AAPL
  df = api.get_barset(
      ticker,
      timeframe,
      start=start_date,
      end=end_date,
  ).df
  ```

* Next, we configure and run `500` Monte Carlo simulations to forecast the stock's daily returns over the next `252` trading days.

  ```python
  # Set number of simulations
  num_sims = 500

  # Configure a Monte Carlo simulation to forecast one year daily returns
  MC_AAPL = MCSimulation(
      portfolio_data = ticker_data,
      num_simulation = num_sims,
      num_trading_days = 252
  )

  # Run Monte Carlo simulations to forecast one year daily returns
  MC_AAPL.calc_cumulative_return()
  ```

* Plotting the DataFrame of simulated `AAPL` daily returns for the next `252` trading days shows all the potential pathways for how `AAPL` stock prices may behave in the next year. We use the `plot_simulation()` function to visually analyze the `500` possible scenarios that we may have over the next `252` trading days.

  ```python
  # Plot simulation outcomes
  line_plot = MC_AAPL.plot_simulation()
  ```

  ![aapl-simulation-plot](Images/aapl-simulation-plot.png)

* Plotting the best and worst-case scenario for cumulative returns makes a lot of intuitive sense from an investment standpoint. We create a DataFrame with the mean, median, minimum, and maximum daily return value to generate a plot to summarize the behavior of the `AAPL` stock in the simulated future. Note that we used the argument `axis=1` to compute the statistics by column.

  ```python
  # Compute summary statistics from the simulated daily returns
  simulated_returns_data = {
      "mean": list(MC_AAPL.simulated_return.mean(axis=1)),
      "median": list(MC_AAPL.simulated_return.median(axis=1)),
      "min": list(MC_AAPL.simulated_return.min(axis=1)),
      "max": list(MC_AAPL.simulated_return.max(axis=1))
  }

  # Create a DataFrame with the summary statistics
  df_simulated_returns = pd.DataFrame(simulated_returns_data)

  # Display sample data
  df_simulated_returns.head()
  ```

  ![aapl-stats-df](Images/aapl-stats-df.png)

  ```python
  # Use the `plot` function to visually analyze the trajectory of AAPL stock daily returns on a 252 trading day simulation
  df_simulated_returns.plot(title="Simulated Daily Returns Behavior of AAPL Stock Over the Next Year")
  ```

  ![aapl-daily-returns-plot](Images/aapl-daily-returns-plot.png)

* It is also interesting to visually analyze what would be the possible outcomes of an initial investment. Let's calculate the simulated profits and losses of an initial investment of $10,000 in `AAPL` stocks.

  ```python
  # Set initial investment
  initial_investment = 10000

  # Multiply an initial investment by the daily returns of simulative stock prices to return the progression of daily returns in terms of money
  cumulative_pnl = initial_investment * df_simulated_returns

  # Display sample data
  cumulative_pnl.head()
  ```

  ![aapl-outcomes-df](Images/aapl-outcomes-df.png)

* After computing the possible outcomes, we can create a line plot to analyze their behavior visually.

  ```python
  # Use the 'plot' function to create a chart of the simulated profits/losses
  cumulative_pnl.plot(title="Simulated Outcomes Behavior of AAPL Stock Over the Next Year")
  ```

  ![aapl-outcomes-plot](Images/aapl-outcomes-plot.png)

* Finally, we calculate the range of the possible outcomes of our $10,000 investment in `AAPL` stocks with a `95%` confidence interval by fetching the summary statistics from the Monte Carlo simulation results.

```python
# Fetch summary statistics from the Monte Carlo simulation results
tbl = MC_AAPL.summarize_cumulative_return()

# Print summary statistics
print(tbl)
```

```text
count           500.000000
mean              1.231607
std               0.362491
min               0.546586
25%               0.970280
50%               1.160347
75%               1.443191
max               2.859506
95% CI Lower      0.687664
95% CI Upper      2.052604
Name: 252, dtype: float64
```

```python
# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $10,000 investments in AAPL stocks
ci_lower = round(tbl[8]*10000,2)
ci_upper = round(tbl[9]*10000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $10,000 in the portfolio"
      f" over the next year will end within in the range of"
      f" ${ci_lower} and ${ci_upper}.")
```

```text
There is a 95% chance that an initial investment of $10,000 in the portfolio over the next year will end within in the range of $6876.64 and $20526.04.
```

Answer any questions before moving on.

---

### 11. Students Do: Financial Forecasting (15 min)

**Corresponding Activity:** [06-Stu_Financial_Forecasting](Activities/06-Stu_Financial_Forecasting)

In this activity, students execute a Monte Carlo simulation to forecast stock price behavior of historical `TSLA` daily returns.

**Instructions:**

* [README.md](Activities/06-Stu_Financial_Forecasting/README.md)

**Files:**

* [financial_forecasting.ipynb](Activities/06-Stu_Financial_Forecasting/Unsolved/financial_forecasting.ipynb)

* [MCForecastTools.py](Activities/06-Stu_Financial_Forecasting/Unsolved/MCForecastTools.py)

---

### 12. Instructor Do: Review Financial Forecasting (10 min)

**Files:**

* [financial_forecasting.ipynb](Activities/06-Stu_Financial_Forecasting/Solved/financial_forecasting.ipynb)

* [MCForecastTools.py](Activities/06-Stu_Financial_Forecasting/Solved/MCForecastTools.py)

Open the solution and explain the following:

* Make sure that the `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` environment variables are properly set in your projects `.env` file so that the `alpaca-trade-api` SDK can communicate to the `Alpaca` API.

* The `get_barset()` function pulls three years worth of stock data from the Alpaca API.

  ```python
  # Set the ticker
  ticker = "TSLA"

  # Set timeframe to '1D'
  timeframe = "1D"

  # Set start and end datetimes of 3 years from Today
  start_date = pd.Timestamp("2017-05-04", tz="America/New_York").isoformat()
  end_date = pd.Timestamp("2020-05-04", tz="America/New_York").isoformat()

  # Get 1 year's worth of historical data for TSLA
  ticker_data = api.get_barset(
      ticker,
      timeframe,
      start=start_date,
      end=end_date
  ).df
  ```

* Next, we configure and run `1000` Monte Carlo simulations to forecast the future daily closing prices of `TSLA`.

  ```python
  # Set number of simulations
  num_sims = 1000

  # Configure a Monte Carlo simulation to forecast three years daily returns
  MC_TSLA = MCSimulation(
      portfolio_data = ticker_data,
      num_simulation = num_sims,
      num_trading_days = 252*3
  )
  ```

* Simulations for the next `252` trading days show that `TSLA` stock is forecast to continue to decline, with a `$10,000` investment facing brutal negative returns if invested in `TSLA` over the next three years.

  ![tsla-simulated-outcomes](Images/tsla-simulated-outcomes.png)

* It should be stated that although the forecast for the next `3` years of `TSLA` stock prices show considerable declines, it does not mean that it is guaranteed.

* As you can observe, the range of the possible outcomes of our $10,000 investments in `TSLA` stocks drops to around $3,000 and jumps over $200,000. A forecast/prediction is only as good as the foundation of information from which it was made, and even then, by the nature of random events -- *anything* can happen.

```python
# Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of our $10,000 investments in AAPL stocks
ci_lower = round(tbl[8]*10000,2)
ci_upper = round(tbl[9]*10000,2)

# Print results
print(f"There is a 95% chance that an initial investment of $10,000 in the portfolio"
      f" over the next year will end within in the range of"
      f" ${ci_lower} and ${ci_upper}.")
```

```text
There is a 95% chance that an initial investment of $10,000 in the portfolio over the next year will end within in the range of $2851.84 and $251789.23.
```

Answer any questions before moving on.

---

### 13. Instructor Do: Structured Review (35 min)

Is this the end, or is it just another iteration of a simulation? It's actually the end! Welcome to today's finish line.

The content in this lesson is probably the most challenging material students have digested so far. Students were required to whip out every FinTech skill and asset they've learned. This lesson was involved, including portfolio optimization (calculation of returns, standard deviation, risk, etc.) and portfolio forecasting (Monte Carlo, probability distributions, confidence trajectories, and forecasting). Furthermore, this doesn't even include the Python and Pandas skills they had to leverage!

Make sure students can recognize and acknowledge their accomplishments. Communicate and highlight the following:

* You've added another tool to your API-SDK tool belt: the Alpaca Trade API SDK, which is an excellent resource for historical stock data and financial functions.

* You've taken yet another deep dive into statistics, learning how to create, calculate, and interpret probability distributions. This includes using **mean**, **standard deviation**, **daily returns**, and charts to implement and visualize portfolio simulations.

* You've plotted the price trajectory of stock prices and returns using multiple Monte Carlo simulations.

* You've forecast average daily return volatility at the stock and portfolio level.

* You've assessed the risk of investing in stock by predicting the probability of stock prices rising or falling over time.

* You've put the **Fin** in FinTech, and you're just getting started!

Give students space to emotionally release. Use this activity as a way to gauge student confidence, frustration, and stress levels.

Ask students to summarize how they're feeling with a one-word emotion. Ask for volunteers first. If no one volunteers initiate the activity by using one word to convey how you're feeling, and then go round-robin. Gauge the students' verbal and nonverbal cues of stress and confusion (e.g., withdrawal from the activity or isolation, irritability or impatience, chronic worrying, pessimistic attitude, and restlessness).

  **Answer**: Relieved

  **Answer**: Excited

  **Answer:** Confused

  **Answer:** Empowered

  **Answer:** Stressed

  **Answer:** Doubtful

Indicate to students that no matter what they're feeling, either excited and empowered or stressed and doubtful, they've come a long way. Also, underscore that they're not alone in their feelings or the journey. Portfolio simulations are no joke, and results can easily be misinterpreted or corrupted, which is why the best of the best are the ones executing simulations.

Emphasize that students can reach out individually or attend office hours to ask questions, discuss the activities in the lesson, or just release emotionally.

Use the remaining time for a structured review or to get a head start on office hours. Allow students to ask questions about this lesson, the overall unit, or the homework.

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
