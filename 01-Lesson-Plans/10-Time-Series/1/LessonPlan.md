## 10.1 Lesson Plan: An Introduction to Time Series

### Overview

Welcome to Unit 10! Everything students have learned up to this point--from data cleaning and wrangling to simulations and projected return on investments--has been to prepare students and give them the foundation needed for implementing advanced analytics pipelines using **time series** analysis and **machine learning**.

Unit 10 introduces students to the world of data science and **machine learning**. **Machine learning** is a form of programming that employs algorithms and statistical models to enable insights, predictions, and data-driven decision making. **Machine learning** involves the development of computer applications that have the ability to automatically learn from data and make adjustments to parameters and execution based off of experience, with little to no interaction from a developer.

For many students, this unit and the units to follow will be the bread and butter of the class. Advanced analytics is taking the data industry by storm, offering developers and companies a means to analyze thousands of large data sets and use computer predictions to drive investments and decision making. Machine learning especially benefits financial services, allowing banks and professionals to analyze large data sets and use technology to make investment recommendations and predictions, a process that typically requires multiple hands and hours/days of time. Machine learning has streamlined financial analysis; work that previously took hours for a single financial professional to complete can now be automated and completed within minutes using machine learning algorithms.

* Make sure to keep students engaged and excited about the content. Machine learning and data science skills are taking over the tech industry; the advanced analytics and machine learning content in these upcoming units will ensure students are competitive in the job market.

* Remember to emphasize the real world value and application of time series analysis, machine learning, sentiment analysis, and other advanced analytic concepts as they are discussed.

* Learning how to develop machine learning algorithms is what's required to take programming to the next level in the current day technological ecosystem. By the end of the course, students will have evolved from standard Python developers to FinTech data scientist, capable of designing and developing:

* Robo-advisors and chat-bots for algorithmic trading, product/investment recommendation, and customer service/support

* Sentiment analysis engines to assess and predict economical sentiment for stock and housing markets

* Models that predict and detect fraudulent financial transactions

Today's class will initiate this journey by introducing students to the basics of time series analytics.

### Class Objectives

By the end of this class, students will be able to:

* Manipulate time series data sets in pandas.

* Identify the components of a time series.

* Use tools such as moving average, exponentially-weighted moving average, and the Hodrick-Prescott filter to identify long-term trends.

* Perform auto-correlation on time series data.

- - -

### Instructor Notes

* Today's class will be a fairly gentle ramp up to the rest of the week. It will provide students with the skills to work with time series data in pandas (e.g. slicing rows by date), and it will furnish them with necessary concepts for days 2 and 3. The first half of the day will focus on identifying what time series analysis is and how it is used. The second half will emphasize scaling time series analysis using machine learning algorithms.

* It is important to emphasize the role of machine learning in time series analysis and advanced analytics (the application of advanced statistical models and intelligent algorithms). Today's class, and the unit in its entirety, will begin the students' journey into **machine learning**. For some students, machine learning is their reason for choosing the curriculum. For others, machine learning may be intimidating and unreachable. Remember to communicate concepts in simple terms, reminding students that machine learning is just the application of statistics using Python libraries in order to analyze data and make predictions regarding behavior and outcomes. Foster confidence and understanding by pacing explanations and demonstrations. Explanatory examples have been provided to assist with this.

* The mathematical details of tools such as Hodrick-Prescott filter are discussed in some detail. They are provided to give students an understanding of what happens under the hood. However, do not get so bogged down in explaining the niceties that derails the pace of the class.

* The goal should be to transmit the mathematical and statistical concepts and approaches at a level required to complete the activity. Students should then independently research and reinforce the concepts outside of class.

* The next several units will teach students how to use data science tool kits and machine learning algorithms to automate financial analysis and predict future outcomes. By the end of unit, students will have designed and executed machine learning algorithms that leverage common time series analysis and linear aggression approaches to make robust predictions about investments. Students will also have become competent in using standard methods/approaches and tools to evaluate predictions, such as **train test data splitting** and **rolling out of sample method**.

* Slack out some of the following helpful links, and encourage students to conduct research and review supplementary resources outside of class.

  * [What is Time Series Forecasting?](https://machinelearningmastery.com/time-series-forecasting)

  * [7 Exciting Uses of Machine Learning in FinTech](https://rubygarage.org/blog/machine-learning-in-fintech)

  * [Understanding Self Learning Monte Carlo](https://www.analyticsindiamag.com/understanding-self-learning-monte-carlo-method/)

  * [Predictive Analytics for FinTech](https://www.prnewswire.com/news-releases/predictive-analytics-for-fintech-an-increasingly-necessary-tool-to-stay-competitive-says-frere-enterprises-300757420.html)

  * [How Machines Learn](https://www.youtube.com/watch?v=R9OHn5ZF4Uo&start=0&end=72)

  * [A.I. Experiments: Visualizing High Dimensional Space](https://www.youtube.com/watch?v=wvsE8jm1GzE)

  * [Machine Learning and Human Agility](https://www.youtube.com/watch?v=sWNG3omofoM)

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5f3ad86fc3_0_82).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker.xlsx](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome (5 min)

The instructor will kick off the class by welcoming students and briefly introducing the concepts and skills for Unit 10 and today's class. The focus of this activity will be introducing students to **time series analysis**, **machine learning**, and how the two can be used together to create predict trends in various financial markets (i.e. stocks and real estate).

Welcome the students back to class. Communicate to them that this unit will commence their journey into the world of time series analysis and machine learning.

### 2. Instructor Do: Mysticism of Machine Learning (15 min)

Open the slides, and highlight the following:

* Define **machine learning** as an approach to programming that focuses on designing applications in a way that allows them to learn from their inputs and make adjustments based off of their outputs.

  * A very raw way of thinking about **machine learning** is automated configuration; instead of having to configure inputs and manually make changes to an algorithm, **machine learning** programs automatically adapt to improve outcomes and predictions, as well as accuracy and precision.

* Explain to students that because machine learning algorithms can learn on their own, developers do not need to worry about coding for every scenario.

  * For example, instead of creating a 500 line if-else decision structure in order to identify if a transaction is fraudulent, where every price range and product category is evaluated, a machine learning algorithm can review all transactions ever made by an account owner, classify and cluster transactions,and then predict whether or not the most recent transaction is fraudulent.

* Emphasize that machine learning, in a nutshell, is just developing a statistical or algorithmic model of the data that can be used to automatically make predictions or decisions about new data.

* Explain that machine learning algorithms have been transforming a range of industries, including finance, healthcare, agriculture, marketing, homeland security, and space exploration, just to name a few. **Machine learning** is being used to used to predict

  * Loan eligibility

  * Foreclosure rates

  * Fraud and money laundering

  * Disease diagnosis and prognosis

  * Consumer segmentation and clustering

  * Presidential election results

  * Occurrence/effects/impacts of natural storms and disasters

  * Planetary climate and atmosphere conditions/composition, etc.

* Underscore to students that the predictions made by **machine learning** algorithms are driving decision making at a global scale. Commercial and government leaders all leverage **machine learning** in some capacity: **machine learning** outcomes are helping industries become more proactive than reactive. Machine learning is at the forefront of all initiatives to make data driven decisions.

* Communicate to students that the world of **machine learning** is sometimes viewed as nebulous and enigmatic: a niche field of programming involving heavy statistical calculations, programming conundrums, and loaded words like **artificial intelligence**. Highlight that while **machine learning** can be challenging, it is just the application of algorithms, statistics, and statistical libraries to solve data and business problems.

  * Like all other functions, machine learning models are provided as libraries. Common machine learning libraries include **Scikit-Learn**, **TensorFlow**, and **SciPy**. Services like Amazon Web Services and Google Cloud Platform offer proprietary machine learning libraries that can be used within their cloud ecosystems. These libraries, as well as the open source community, make execution of machine learning models as simple as calling a Pandas functions.

  * Summarize the machine learning pipeline and explain to students that all machine learning pipelines follow a **Model -> Fit (Train) -> Predict** paradigm, where a data set/model of data is used to train the algorithm. Once the algorithm has been trained, the model and algorithm can be used to make actual predictions.

Ask students what they think machine learning can do? Ask what ideas they have as to why someone would go through the effort of using advanced statistical algorithms when a developer can just use Monte Carlo simulations to make predictions?

* **Answer** Typically when working with an algorithm, a developer has to tweak and configure the algorithm to create the most accurate and precise results for a given use case. This requires a lot of manual work.

  * Machine learning completely removes this need, as the program will continuously learn from data/its results and make adjustments on the fly.

  * This allows for the algorithm to perform more robustly and change dynamically based off of the data it is processing. These types of algorithms are classified as **intelligent algorithms**.

Define **intelligent algorithms** for students. Explain that **intelligent algorithms** use data to modify behavior. With **intelligent algorithms**, the behavior of the algorithm changes as data is processed and predictions are made.

* **Intelligent algorithms** use pre-existing data to learn and make decisions on how to configure and adapt its behavior for the most accurate and precise prediction.

* **Intelligent algorithms** are used to fuel **machine learning**, **predictive analytics**, and **artificial intelligence**.

Explain the similarities and differences between machine learning, predictive analytics, and artificial intelligence.

* Machine learning has two approaches to using  **intelligent algorithms**:

  * One approach is **supervised learning**, which involves a programmer feeding the algorithm valuable data to learn from and make predictions.

    * Categories of supervised learning include classification (classifying outcomes as classes/groups) and regression (fitting data to predict where a new data point lies), both of which are used for making predictions. With **supervised learning**, potential outcomes need to be known up front.

  * The other is **unsupervised learning**, where the **intelligent algorithm** learns on the fly without having seen any type of data before. The algorithm will identify all data points, cluster them, and then make predictions. Eventually, the algorithm will learn for itself.

    * Unsupervised learning includes dimensionality reduction and clustering approach (finding groups within a population).

* Predictive analytics is the use of advanced analytics paradigms (machine learning, intelligent algorithms, etc.) to analyze data and forecast outcomes and values. Machine learning is component of predictive analytics, and predictive analytics is an objective of machine learning.

* **AI** is the concept that machines can execute tasks and learn while doing so in order to perform more intelligently. Machine learning is a class of **AI**: an application of AI.

  * The general consensus is that instead of programming machines to perform specific tasks, program machines to learn what tasks to complete and how to complete them.

  * **Machine learning** is not the only application of **AI**. Deep learning is a comparative approach to programming that is distinct from **machine learning** but is still another class of **AI**.

If time remains, stimulate excitement by showing students some of the below example uses cases for machine learning. Show videos in the order they are provided. If time does not remain, slack these links out to students for review.

* [How Machines Learn](https://www.youtube.com/watch?v=R9OHn5ZF4Uo) - only play up until 1:11 marker.

* [A.I. Experiments: Visualizing High Dimensional Space](https://www.youtube.com/watch?v=wvsE8jm1GzE)

* [Machine Learning and Human Agility](https://www.youtube.com/watch?v=sWNG3omofoM)

Ask for any questions before moving forward. Assure students that each of these concepts will be explored in more detail over the next several weeks.

### 3. Instructor Do: Review Homework (10 min)

The instructor will provide a brief walk through of the homework solution. Time should be dedicated to allowing students ask a few questions about assignment.

**File:** [Homework Instructions](../../02-Homework/10-Time-Series/Instructions/README.md)

Open the homework instructions, and highlight the following:

* This week's homework will be a deep dive into the various methods and techniques of analyzing and forecasting time series data. Students will use the **Hodrick-Prescott** filter, as well as **GARCH** and **EGARCH** models to complete time-series return forecasting and volatility forecasting.

* Explain to students that this homework will consist of three parts:

  * Time-Series Return Forecasting

  * Volatility Forecasting

  * Out-of-Sample Predictions

* Communicate to students that by the end of the homework, they will have gained proficiency in using time series approaches and models to forecast financial data.

* Indicate to students that the homework will leverage the **Quandl** API. Remind students that **Quandl** requires an API key and that they will have to have the key stored, sourced, and exported as an environment variable.

Ask students if they have any questions before moving on.

### 4. Instructor Do: Time Series Basics (10 min)

**File:** [Activities/01-Ins_Time_Series_Basics/Solved/datetime_basics.ipynb](Activities/01-Ins_Time_Series_Basics/Solved/datetime_basics.ipynb)

Explain to students that over the next several weeks, we will be learning about many different machine learning models and techniques, but we will start with Time Series Models. Time Series Models are very prevalent in the financial world and are very useful models for analyzing time series data.

In this activity, you will introduce the basics of working with time series in Python.

Explain that we'll learn the following pandas techniques to work with time series data:

* Converting a column of dates from string to datetime format.

* Using the `loc[]` accessor to select rows with specified dates.

* Using the `resample()` method to group rows by day, week, month, year, or any datetime attribute.

* Accessing datetime attributes from the index.

Open the notebook and run the following lines of code:

  ```python
  df = pd.read_csv('liquor_sales.csv')
  df.head()
  df.info()
  ```

  ![Images/datetime00.png](Images/datetime00.png)

  ![Images/datetime01.png](Images/datetime01.png)

  * The CSV, a data set of liquor sales figures, is opened with pandas.

  * `df.info()` lists the number of rows, as well as the column data types.

  * The `datetime` column type is listed as `object`. In this case, this means that the datetime information is formatted as strings.

Explain how to read a time series data set:

  ```python
  df2 = pd.read_csv('liquor_sales.csv', parse_dates=True, index_col='datetime')
  ```

  * There are two additional arguments here. The first, `parse_dates=True`, formats the column containing the datetime information as `datetime`.

  * The next argument, `index_col='datetime'` sets this column as the data frame index.

Demonstrate that the data frame is now a true time series:

  ![Images/datetime01.png](Images/datetime02.png)

  ![Images/datetime01.png](Images/datetime03.png)

  * `df2.info()` shows that the index is a `DatetimeIndex`.

  * Plotting the `liquor_sales` column automatically formats the x-axis as dates.

Having properly formatted and indexed the time series, explain next how to select and slice the data frame with specified dates:

  ```python
  first_year = df2.loc['1980']
  ```

  * Using the `loc[]` accessor, only rows from the year 1980 can be selected.

  * The `loc[]` accessor can also be used to slice a date range: `two_year_period = df2.loc['1985': '1986']`.

Next, explain that the `resample()` method groups rows by a specified time frame:

  ```python
  yearly_average = df2.resample('A').mean()
  ```

* This line groups all the rows of a year together, then obtains their mean.

* `resample()` is quite similar to pandas's `groupby()` method. Once data has been aggregated, an aggregate function must be called. In this case, the mean was called, but quantities such as the sum, maximum value, or the minimum value can also be obtained with their respective functions.

* The argument `'A'` in `resample()` specifies the time frame. Here, it is grouping the rows into an annual time frame. Others, such as daily or weekly data, can also be used.

* Other arguments for this method can be found by consulting the documentation.

* Finally, explain that data formatted as datetime offer access to specific attributes.

  ```python
  df2.index.year
  df2.index.month
  df2.index.weekofyear
  ```

* For example, the index of the data frame, which is formatted as datetime, store information on the specific year, month, and even the week of the year for each row.

* More attributes can be found by consulting the documentation.

### 5. Students Do: Time Series Basics (15 min)

In this activity, students will practice the basics of time series manipulation in pandas.

**Files:**

* [Activities/02-Stu_Time_Series_Basics/README.md](Activities/02-Stu_Time_Series_Basics/README.md)

* [Activities/02-Stu_Time_Series_Basics/Unsolved/amazon.csv](Activities/02-Stu_Time_Series_Basics/Unsolved/amazon.csv)

### 6. Instructor Do: Review Time Series Basics (10 min)

**File:**

* [amazon_stock_prices.ipynb](Activities/02-Stu_Time_Series_Basics/Solved/amazon_stock_prices.ipynb)

Quickly walk through the basic steps of working with a time series in pandas. Use this as a refresher on indexing. Try not to dwell on any point for too long, as students will work with these methods repeatedly throughout the week.

* The `parse_dates` and `index_col` arguments are used to format the time series index as datetime. This allows data to be sliced from the DataFrame by date ranges.

  ```python
  df2 = pd.read_csv(
    'amazon.csv',
    parse_dates=True,
    index_col='Date')
  sep_2018 = df2.loc['2018-09']
  ```

* Slicing data by date ranges is key to time series analysis. Data will need to be sliced and diced by different time intervals.

  ```python
  df.loc['2018-09':'2018-10']
  ```

* Time series data can be grouped using the resample function. The `resample` function will group the data using the **DateTimeIndex** and the frequency provided (i.e. weekly). This will serve as a resampling of the data. Data can be grouped weekly, monthly, etc. The `resample` function works just like the `groupby` function; however, `resample` is specific for time series data.

  ```python
  weekly = df['Close'].resample('W').mean()
  ```

  ![resample.png](Images/resample.png)

Answer any remaining questions before moving on.

### 7. Instructor Do: Time Series Decomposition (10 min)

* **File:** [Activities/03-Ins_Decomposition/Solved/decomposition.ipynb](Activities/03-Ins_Decomposition/Solved/decomposition.ipynb)

Open [Slide 3](https://docs.google.com/presentation/d/1DSwXmlnnP2_TmhJlBB_95bdWm_m7xb0rACwK-usjfwk/edit#slide=id.g5f3ad86fc3_0_19) and define time series decomposition to the class:

* In a nutshell, it is separating time series data into useful and less useful components.

* The useful components can be used to observe patterns and to make predictions.

Open [Slide 4](https://docs.google.com/presentation/d/1DSwXmlnnP2_TmhJlBB_95bdWm_m7xb0rACwK-usjfwk/edit#slide=id.g5f3ad86fc3_0_19) and list the components of time series decomposition:

* Level: What is the average value of the series?

* Trend: Is there an overall direction of movement?

* Periodicity: Do patterns occur in cycles?

* Residual: How much noise exists in the data?

Open the notebook and explain that it is a chart of monthly liquor sales in the United States between 1980 and 2007.

  ![Images/decomposition01.png](Images/decomposition01.png)

Ask ask students to describe what they see:

* There is an overall increase in sales over the years.

* Spikes in sales also appear regularly.

* As expected, the pattern is not perfectly regular.

Show the next image in the notebook:

  ![Images/decomposition02.png](Images/decomposition02.png)

* It plots liquor sales data from a 26-month period.

* It shows a sales spike during each holiday season.

Next, explain that the code below decomposes the liquor sales data.

  ```python
  decomposed = seasonal_decompose(df['liquor_sales'], model='multiplicative')
  ```

* The model is specified as multiplicative because the seasonal fluctuation (the spikes) increases with the series.

Explain that the time series is decomposed visually by the library:

![Images/decomposition03.png](Images/decomposition03.png)

* The `observed data` panel is decomposed into the next three elements.

* An upward trend is observed in the data.

* A seasonality is also observed.

* The residual components are the leftovers when trend and seasonality are removed.

Finally, explain that the library used in the notebook is more useful as an illustrative tool than a predictive tool. We will cover such tools during this week.

- - -

### 8. BREAK (15 min)

- - -

### 9. Instructor Do: EWMA and Hodrick-Prescott Filter (15 min)

In this activity, you will introduce EWMA, or exponentially-weighted moving average. You will also introduce the Hodrick-Prescottt filter, a tool that captures trends by minimizing local fluctuations.

**Files:**

* [hodrick.ipynb](Activities/04-Ins_Hodrick_Prescott/Solved/hodrick.ipynb)

* [IVV.csv](Activities/04-Ins_Hodrick_Prescott/Solved/IVV.csv)

Open the notebook and describe the dataset:

* The data tracks the closing price during a two-year period of IVV, an exchange-traded fund (ETF) that tracks the S&P 500 index.

Begin the activity with a brief review of moving average:

![Images/ma01.png](Images/ma01.png)

* In a moving average (also called rolling average), each value is the average of a number of prior values.

* In pandas, it can be computed with the `rolling()` and `mean()` methods, with the `window` argument specifying the number of prior values to average.

Explain that an exponentially-weighted moving average (EWMA) is similar to a moving average, with a significant difference:

  ![Images/ma02.png](Images/ma02.png)

* In an EWMA, unlike an MA, recent values carry more weight than values from a more distant past.

* This strategy may better capture **trends** than a simple moving average.

* In pandas, it can be computed with the `ewm()` and `mean()` methods.

* In a rolling average, a `window` argument is supplied. In contrast, the `ewm()` method takes a `halflife` argument.

Introduce the topic of the Hodrick-Prescott filter:

* It is a mathematical function used to separate short-term fluctuations, such as ones that occur daily, from longer-term trends.

* It decomposes a time series into trend and non-trend components.

* Like rolling average and EWMA, it can be used to capture trends.

Open the [Slideshow](https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5f3ad86fc3_0_212) and briefly explain the overall mathematical idea of the Hodrick-Prescott filter (Slides 7-9):

  ![Images/hp01.png](Images/hp01.png)

* It is a function that minimizes the sum of two values.

* As discussed previously, a time series can be decomposed into trend, periodicity, and noise.

* If we temporarily disregard noise, then, time series data minus trend equals periodicity.

* The left side describes the cyclic element: time series (y) minus trend (tau).

* The right side basically describes the volatility in trend.

* The H-P filter essentially **minimizes** the aggregate values associated with non-trend (periodicity and volatility).

Next, explain the Python code used to run the Hodrick-Prescott filter:

  ```python
  import statsmodels.api as sm
  ts_noise, ts_trend = sm.tsa.filters.hpfilter(df['close'])
  ```

* `hpfilter` is a module from the `statsmodels` library.

* The `hpfilter()` function separates a column of closing prices into trend and noise (non-trend).

* The code is much simpler than the mathematical description!

Finally, show the plots of the trend and noise components after filtering:

  ![Images/hp03.png](Images/hp03.png)

  ![Images/hp04.png](Images/hp04.png)

* The first plot shows the trend, which is considerably smoother than the raw time series data.

* The second plot shows the noise (non-trend) that has been filtered out.

### 10. Students Do: You've Got a FRED (15 min)

In this activity, students will use the Hodrick-Prescott filter to identify macroeconomic trends in the United States in the period from 2004 to 2010.

**Files:**

* [README.md](Activities/05-Stu_Hodrick_Prescott/README.md)

* [FRED.ipynb](Activities/05-Stu_Hodrick_Prescott/Unsolved/FRED.ipynb)

### 11. Instructor Do: Review You've Got a FRED (10 min)

**Files:**

* [FRED.ipynb](Activities/05-Stu_Hodrick_Prescott/Solved/FRED.ipynb)

Open the solution file, and conduct a brief dry walk through of the code.

* Explain that pandas's `DataReader` function is used to retrieve data from FRED at specified starting and end points.

  ```python
  start = datetime.datetime(2004, 1, 1)
  end = datetime.datetime(2010, 1, 1)
  gdp = web.DataReader(['GDP'], 'fred', start, end)
  ```

  ![datareader.png](Images/datareader.png)

* Explain using the H-P filter in Python. It is a `statsmodels` module that requires a single line of code. The plots are created simply with pandas's `plot()` method.

  ```python
  import statsmodels.api as sm
  gdp_noise, gdp_trend = sm.tsa.filters.hpfilter(gdp['GDP'])
  ```

  ![hpfilter.png](Images/hpfilter.png)

If time allows, take a moment to compare and contrast the H-P filter:

* In this data set, for the most part, the EWMA seems to produce a fairly similar result as the H-P filter, though the latter is somewhat smoother.

### 12. Instructor Do: Auto Correlation (15 min)

**File:** [autocorrelation.ipynb](Activities/06-Ins_Auto_Correlation/Solved/autocorrelation.ipynb)

Open the notebook and briefly describe the data set:

  ![Images/ac01.png](Images/ac01.png)

* The data set is the familiar weather data.

* The temperature readings are hourly.

* Each hourly reading is fairly close to that of the previous hour.

Introduce the concept of auto correlation:

* Up to this point, when dealing with linear regression, we have tried to identify the relationship between two unrelated variables, such as date vs. weather, or years of experience vs. salary.

* Auto correlation, on the other hand, determines to what extent, for example, today's values correlate with yesterday's values.

To illustrate auto correlation, explain to students that the `Lag_Temperature` column is the result of shifting the `Temperature` column down by one:

  ![Images/ac02.png](Images/ac02.png)

* The temperature value from the first row is found in the `Lag_Temperature` column in the second row, for example.

* The temperature data has been shifted down by one time period--in this case an hour.

* The temperature from one hour to the next changes in relatively small increments.

* Auto correlation, again, is a measure of how closely current values correlate with past values.

Show the plot of the temperature data versus a lagged copy of itself:

  ![Images/ac06.png](Images/ac06.png)

* In this case, there appears to be an extremely close relationship.

* In other words, a temperature reading is close in value to the reading from an hour earlier.

Now show the plotting of temperature over a 48-hour period, with the following observations:

  ![Images/ac03.png](Images/ac03.png)

* The temperature, predictably, shows a cyclical pattern.

 * Despite significant swings seen in a day, the temperature change between one hour to the next is fairly small.

* For a given temperature reading, say 6 am on January 1st, the most similar temperature reading is seen again 24 hours later.

You may wish to draw on the following scenario to further illustrate autocorrelation:

* A pair of dice is thrown every minute. Their combined value and the time are recorded.

* Since it is a random activity, there will not be a strong relationship between the current value of the dice and the preceding one. Here, the auto correlation will not be significant.

Next, explain the code used to calculate the auto correlation:

  ```python
  df.Temperature.autocorr(lag=1)
  ```

* The `autocorr()` method here returns the autocorrelation of the `Temperature` column against a lagged copy of itself.

* Here, the lag is 1, meaning that the series of temperature readings is correlated against a series of temperature readings taken one hour previously.

* The correlation coefficient is 0.99, a very high number.

Explain that auto correlation can be computed at a different lag

  ```python
  df.Temperature.autocorr(lag=24)
  ```

* Here, each temperature reading is autocorrelated with a temperature reading 24 hours later.

* As expected, the auto correlation is very high at a lag of 24 as well.

Once again, if necessary, remind your students that auto correlation is simply the correlation of current data with past data.

Explain that the `plot_acf()` function visualizes what we have discussed so far:

  ```python
  sm.graphics.tsaplots.plot_acf(df.Temperature, lags=48)
  ```

  ![Images/ac04.png](Images/ac04.png)

* The plot nicely illustrates the periodicity of daily temperature patterns.

* This plot, in other words, shows autocorrelation at lags up to 48, which was specified in the argument `lags=48`.

* As pointed out previously, there is high auto correlation at a lag of 1, slightly lower at lag 2, and so on. Then a high auto correlation is found at a lag of 24, and multiples of 24, such as 48.

Next, explain that the band in light blue is the confidence interval.

* By default, the CI is set to 95%.

* In other words, if the data set were noisy, and there's no meaningful auto correlation, there is 5% chance that the auto correlation at a particular lag would be found outside the CI band by random chance.

* In this case, the auto correlation at all specified lags are outside the CI band, indicating a high likelihood that the auto correlation at each interval is **not** a random fluke.

* As lag time increases, the CI band widens. This makes intuitive sense: as lag is increased, more potential for noise is introduced, and the statistical burden of proof is higher.

Next, introduce partial auto correlation functions:

* The idea of PACF is different from auto correlation function.

* Whereas an auto correlation function measures auto correlation at all specified lags, PACF essentially reduces components of auto correlation that are explained by previous lags. The effect is that it gives heavier weight to lags that have components that are not explained by earlier lags.

Explain that a PACF plot will illustrate the idea in concrete terms:

  ```python
  sm.graphics.tsaplots.plot_pacf(df.Temperature, lags=48, zero=False)
  ```

  ![Images/ac05.png](Images/ac05.png)

* The `plot_pacf()` function creates a PACF plot with the same temperature data.

* In the PACF plot, there are significant lags at 1, 2, and 24 hours.

* The PACF estimates that lags at 1, 2, and 24 hours account for the other lags.

* In other words, PACF answers the question, if there's already one lag that has been identified as being significant, will the data be better explained by flagging a second lag as significant?

* In the ACF, there was high auto correlation at lags of 24 and 48 hours. This makes sense, as the temperature at the same time across three days would be expected to be very similar.

* In the PACF, however, we do not see a high partial auto correlation at a lag fo 48 hours, since that can be explained by the lag at 24 hours.

Finally, summarize the key points of the activity:

* Autocorrelation is a measure of high closely current values are correlated with past values.

* In the activities to come, ACF and PACF will help us select the correct **order** of models for forecasting.

* Doing so requires an understanding of how current values are affected by past values.

### 13. Students Do: Euro ETFs (15 min)

In this activity, students will examine a time series of bid-ask spreads of an ETF for autocorrelation.

**Files:**

* [README.md](Activities/07-Stu_ETF/README.md)

* [high_frequency_euro_ETF_bid_ask_spreads.csv](Activities/07-Stu_ETF/Resources/high_frequency_euro_ETF_bid_ask_spreads.csv)

* [autocorrelation.ipynb](Activities/07-Stu_ETF/Unsolved/autocorrelation.ipynb)

### 14. Instructor Do: Review Activity (10 min)

**File:**

* [autocorrelation.ipynb](Activities/07-Stu_ETF/Solved/autocorrelation.ipynb)

Walk through the solution code:

  ```python
  df=df.resample('10S').mean().dropna()
  df.bid_ask_spread.autocorr(1)
  ```

* The bid-ask spread data is sampled at a 10-second interval, and NaN values are dropped.

* The autocorrelation at a lag of 1 is 0.136.

Review the ACF and PACF plots:

  ```python
  from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
  plot_acf(df['bid_ask_spread'], lags=30, zero=False)
  plot_pacf(df['bid_ask_spread'], lags=30, zero=False)
  ```

  ![Images/etf01.png](Images/etf01.png)

  ![Images/etf02.png](Images/etf02.png)

  * The ACF and PACF plots here have a similar appearance, although that is not always the case.

  * The ACF and PACF both appear to be significant at a lag of 1.

### 15. Instructor Do: Reflect (10 min)

End the class by congratulating students on a tough day of time series analysis. Assure students that no one can master this content in a day; additional review and practice will be needed to reinforce the skills learned.

* Reiterate to students that the main goal time series and machine learning models, especially within FinTech, is to predict and forecast prices and ROI. Time series analysis helps us to analyze the data to determine the best way to model the data and ultimately forecast future events.

Ask if there are any questions before moving on. Encourage students to attend office hours and to reach out to teaching staff for any additional questions or help.

### 16. END Class
