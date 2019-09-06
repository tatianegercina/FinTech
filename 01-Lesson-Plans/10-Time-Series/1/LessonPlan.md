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

Today's class will initiate this journey by introducing students to the basics of time series analytics. Students will:

* Learn what time series analysis is

* Use tools to work with time series data in Pandas

* Articulate the four components of a time series

* Identify trends in time series

* Create a linear regression model for time series data.

### Class Objectives

By the end of this class, students will be able to:

* Manipulate time series data sets in pandas.

* Identify the components of a time series.

* Use tools such as moving average, exponentially-weighted moving average, and the Hodrick-Prescott filter to identify long-term trends.

* Create a time series linear regression model using Scikit-learn.

* Analyze and predict seasonal effects using regression.

- - -

### Instructor Notes

* Today's class will be a fairly gentle ramp up to the rest of the week. It will provide students with the skills to work with time series data in pandas (e.g. slicing rows by date), and it will furnish them with necessary concepts for days 2 and 3. The first half of the day will focus on identifying what time series analysis is and how it is used. The second half will emphasize scaling time series analysis using machine learning algorithms.

* The mathematical details of tools such as Hodrick-Prescott filter and linear regression are discussed in some detail. They are provided to give students an understanding of what happens under the hood. However, do not get so bogged down in explaining the niceties that derails the pace of the class.

* The goal should be to transmit the mathematical and statistical concepts and approaches at a level required to complete the activity. Students should then independently research and reinforce the concepts outside of class.

* The next several units will teach students how to use data science tool kits and machine learning algorithms to automate financial analysis and predict future outcomes. By the end of unit, students will have designed and executed machine learning algorithms that leverage common time series analysis and linear aggression approaches to make robust predictions about investments. Students will also have become competent in using standard methods/approaches and tools to evaluate predictions, such as **train test data splitting** and **rolling out of sample method**.

* Slack out some of the following helpful links, and encourage students to conduct research and review supplementary resources outside of class.

  * [What is Time Series Forecasting?](https://machinelearningmastery.com/time-series-forecasting)

  * [7 Exciting Uses of Machine Learning in FinTech](https://rubygarage.org/blog/machine-learning-in-fintech)

  * [Understanding Self Learning Monte Carlo](https://www.analyticsindiamag.com/understanding-self-learning-monte-carlo-method/)

  * [Predictive Analytics for FinTech](https://www.prnewswire.com/news-releases/predictive-analytics-for-fintech-an-increasingly-necessary-tool-to-stay-competitive-says-frere-enterprises-300757420.html)

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson 10.1 Slides](https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5f3ad86fc3_0_82).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker.](TimeTracker.xlsx)

### 1. Instructor Do: Welcome (10 min)

The instructor will kick off the class by welcoming students and briefly introducing the concepts and skills for Unit 10 and today's class. The focus of this activity will be introducing students to **time series analysis**, **machine learning**, and how the two can be used together to create predict trends in various financial markets (i.e. stocks and real estate).

Welcome the students back to class. Communicate to them that this unit will commence their journey into the world of time series analysis and machine learning.

Open the slides, and highlight the following:

* Indicate that this unit and several of the units to follow will be focusing on the approaches to implementing **time series analysis** and **machine learning** pipelines. Congratulate students are making it this far into the course!

* Define **time series** data as a cluster of data points for a given variable/attributes ordered and sequenced over time with equal time intervals. Emphasize that **time series** data must be stored in equal time intervals.

* Explain that **time series analysis** is the use of statistical models to assess and evaluate **time series** data.

* Underscore that **time series analysis** is the foundation of advanced analytics for the financial sector. **Time series analysis** is used to:

  * Forecast investment portfolios and economic trends

  * Simulate the market

  * Analyze the market

  * Analyze corporate and personal budgets

  * Execute sales and investment projections

Explain to students that the mathematical and statistical content in this unit may seem heavy and difficult to digest at first. However, it's just a learning curve, which can be mastered with perserverance.

* Reassure students that supplementary guides and resources will be provided to ensure everyone understands the approaches and technologies being used.

* Remind students that they can reach out to TAs and yourself, attend office hours, and collaborate amongst themselves to review the material.

If time remains, engage students by asking the following question:

* So far, we've already forecasted trends in cumulative returns; simulated the market; and analyzed ticker prices, personal budgets, and sale prices. How will using machine learning be any different than the techniques we've already used (i.e. Monte Carlo)?

  * **Answer** Machine learning would eliminate the need for us to manage the configurations/parameters used when analyzing and simulating data for predictions. The simulation would use previous configurations to self learn and identify future configurations to use.

  * **Answer** The machine learning community has developed additional statistical models and algorithms that could be used to make the analysis we've already done more robust and accurate. Instead of using techniques we've already seen for tasks like sampling and linear regression (i.e. Monte Carlo), alternate machine learning ones can be leveraged.

  * **Answer** Machine learning models learn from each event. Machine learning models are able to make more accurate and precise predictions.

If there is time left over, illustrate that the marriage of **time series analysis** and **machine learning** by presenting the following scenario:

* Imagine working on an application that recommends the best investment opportunities for a portfolio based off of the trades made by a day trader. Time series analysis would be required to analyze the data based off of specific intervals, and a machine learning algorithm could be used to have the application learn from previous trades and predict what tickers would be of most interest to the trader.

  * Explain that this type of analysis is considered Predictive Analytics, a form of advanced analytics that leverages statistical models, machine learning, and artificial intelligence to enable data-driven decision making.

  * Communicate that predictive analytics can also be used to predict real estate prices, forecast economic trends and sentiment, predict sentiment and attrition, and a range of other future outcomes based off of historical data points.

Ask students if there are any questions before moving forward. Answer one or two, and then ask students to save and bring up any additional questions during the next review activity.

### 2. Instructor Do: Review Homework (5 min)

The instructor will provide a brief walk through of the homework solution. Time should be dedicated to allowing students ask a few questions about assignment.

**File:**

* [Homework Instructions](../../02-Homework/10-Time-Series/Instructions/README.md)

Open the homework instructions, and highlight the following:

* This week's homework will be a deep dive into the various methods and techniques of analyzing and forecasting time series data. Students will use the **Hodrick-Prescott** filter, as well as **GARCH** and **EGARCH** models to complete time-series return forecasting and volatility forcasting.

* Explain to students that this homework will consist of three parts:

  * Time-Series Return Forecasting

  * Volatility Forecasting

  * Out-of-Sample Predictions

* Communicate to students that by the end of the homework, they will have gained proficiency in using time series approaches and models to forecast financial data.

* Indicate to students that the homework will leverage the **Quandl** API. Remind students that **Quandl** requires an API key and that they will have to have the key stored, sourced, and exported as an environment variable.

Ask students if they have any questions before moving on.

### 3. Instructor Do: Time Series Basics (10 min)

**File:**

* [Activities/01-Ins_Time_Series_Basics/Solved/datetime_basics.ipynb](Activities/01-Ins_Time_Series_Basics/Solved/datetime_basics.ipynb)

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

### 4. Students Do: Time Series Basics (10 min)

In this activity, students will practice the basics of time series manipulation in pandas.

**Files:**

* [Activities/02-Stu_Time_Series_Basics/README.md](Activities/02-Stu_Time_Series_Basics/README.md)

* [Activities/02-Stu_Time_Series_Basics/Unsolved/amazon.csv](Activities/02-Stu_Time_Series_Basics/Unsolved/amazon.csv)

### 5. Instructor Do: Time Series Basics Activity Review (5 min)

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

### 6. Instructor Do: Time Series Decomposition (10 min)

* **File:**

* [Activities/03-Ins_Decomposition/Solved/decomposition.ipynb](Activities/03-Ins_Decomposition/Solved/decomposition.ipynb)

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

### 7. Instructor Do: EWMA and Hodrick-Prescott Filter (15 min)

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

### 8. Students Do: You've Got a FRED (15 min)

In this activity, students will use the Hodrick-Prescott filter to identify macroeconomic trends in the United States in the period from 2004 to 2010.

**Files:**

* [README.md](Activities/05-Stu_Hodrick_Prescott/README.md)

* [FRED.ipynb](Activities/05-Stu_Hodrick_Prescott/Unsolved/FRED.ipynb)

### 9. Instructor Do: Review You've Got a FRED (10 min)

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

- - -

### 10. BREAK (15 min)

- - -

### 11. Instructor Do: Introduction to Linear Regression (15 min)

**File:**

* [linear_regression.ipynb](Activities/06-Ins_Linear_Regression/Solved/linear_regression.ipynb)

In this activity, you will explain linear regression to the class and demonstrate using Scikit-learn to create a linear regression model.

Open the first [slide](https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5fe5cfc349_2_0) and explain the linear equation (Slide 11):

  ```
  y = mx + b
  ```

  * This equation describes, or models, the relationship between variables x and y.

  * As x increases, y increases.

  * How fast y increases in relation to x is called the slope.

  * Slope is represented by the letter `m` in the equation.

  * The value of `y` when `x` is 0 is called the y-intercept. It is represented by the letter `b`.

Open the next [https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5fe5cfc349_2_19](https://docs.google.com/presentation/d/1j_WwCLWxq3nscIXxXNcEGdJfwsiIVsuWWeLBfpzLyno/edit#slide=id.g5fe5cfc349_2_19) and ask whether, on visual inspection, a trend exists (Slide 12):

  ![Images/linear_regression01.png](Images/linear_regression01.png)

  * `y` increases as `x` increases.

Explain that a line that best fits the trend can be drawn:

  ![Images/linear_regression02.png](Images/linear_regression02.png)

  * This line is called the best fit line, and computing it is called linear regression.

  * The equation is simple but tedious, and is best solved by a computer.

Explain that, in other words, linear regresson identifies the line that best predicts `y` based on the value of `x`.

Explain the concept of residuals.

  * Even a best fit line that captures the data well is seldom, if ever, perfect.

  * A residual is the difference between the **predicted** value of `y` and its **actual** value.

  * Linear regression seeks to minimize the **square** value of residuals.

Summarize the key points of linear regression:

  * It models data with a linear trend. It is not useful when the data does not follow a linear trend, e.g. exponential trends.

  * Based on the X values, it predicts Y values.

  * It does not do a good job of describing non-linear patterns. We will cover techniques to model non-linear data later in the course.

Now that students understand linear regression conceptually, walk through the steps of performing linear regression in Python. Here are some introductory remarks:

  * The CSV contains data on years of job experience and salary.

  ![Images/linear_regression03.png](Images/linear_regression03.png)

  * We will use Scikit-learn, a machine learning library, to create a linear regression model.

Engage the class by asking, in a linear regression model, which column will be the dependent variable, and which the independent variable.

  * `YearsExperience` will be the independent variable, or `x`.

  * `Salary` will be the independent variable, or `y`.

Explain that in order to use Scikit-learn (sklearn) for regression, the independent variable (x) will need to be reformatted:

  ```python
  X = df.YearsExperience.values.reshape(-1, 1)
  ```

  * Scikit-learn cannot take in a pandas Series directly.

  * `reshape(-1, 1)` reshapes, or formats, the data.

  * `X.shape` returns `(30,1)`, meaning that `X` has 30 rows and 1 column of data.

  * The dependent variable can remain a pandas series, as seen by `y = df.Salary`.

Walk through the boiler plate code:

  ```python
  model = LinearRegression()
  model.fit(X,y)
  ```

  * A linear regression model is created (instantiated) using Scikit-learn, and the data are fit into the model.

Explain how to obtain the parameters of the model, its slope and y-intercept:

  ```python
  print(model.coef_)
  print(model.intercept_)
  ```

  * Again, Scikit-learn creates a linear equation model based on the data (y = mx + b).

  * `model.coef_` is the slope of the equation.

  * `model.intercept_` is the y-intercept.

Explain that the power of a linear regression model comes from its ability to describe and to predict.

  ```python
  predicted_y_values = model.predict(X)
  ```

  * This line creates an array of predicted y values based on x values.

  * In other words, if given an x-value (years of experience) that is not in the data set, the model will predict the corresponding y-value (salary).

Show the best fit line created by the regression model:

  ![Images/linear_regression04.png](Images/linear_regression04.png)

  * In this case, it describes the existing data very closely.

Do not dwell on the r-square value, but explain that there is a strong relationship between the two variables in the data set:

  ![Images/linear_regression05.png](Images/linear_regression05.png)

  * We will explore measures of accuracy in greater detail in an upcoming activity.

### 12. Students Do: House Regression (10 min)

In this activity, students will perform linear regression on number of rooms in houses versus their prices.

**Files:**

* [README.md](Activities/07-Stu_House_Regression/README.md)

* [USA_Housing.csv](Activities/07-Stu_House_Regression/data/USA_Housing.csv)

### 13. Instructors Do: House Regression Activity Review (10 min)

**Files:**

* [housing.ipynb](Activities/07-Stu_House_Regression/Solved/housing.ipynb)

Open the solution, and complete a dry walk through of the code:

* Linear regression models can be implemented using the Scikit-learn package. A LinearRegression module is included and can be imported into the Python environment.

  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  ```

  ![scikit-learn.png](Images/scikit-learn.png)

* In order to create a linear regression model, **x** and **y** values must be identified. In this case, **x** will be the number of rooms in the house, and it will be reshaped. This will ensure the model is fitted to the data.

  ```python
  X = df.index.values.reshape(-1,1)
  y = df['Price']

  model.fit(X,y)
  predicted_y_values = model.predict(X)
  ```

  ![model_predict.png](Images/model_predict.png)

* The `model.predict()` function can be used to implement predictive analysis. The function will return an array of predicted y-values. This data can then be plotted using a **scatter** plot to highlight the correlation.

  ```python
  # Plot the results. The best fit line is red.
  plt.scatter(X, y)
  plt.plot(X, predicted_y_values, color='red')
  ```

  ![scatter_plot.png](Images/scatter_plot.png)

* The `model` object can be used to then extract the model coefficient (slope), y intercept, and model score. This can be done using the `coef_`, `intercept_`, and `score` attributes/functions.

  ![model_attributes.png](Images/model_attributes.png)

If time remains, ask students some of the following review questions:

* What is the purpose behind a linear regression model?

  * **Answer** Linear regression is used to perform predictive analysis.

* What type of relationship does linear regression explore?

  * **Answer** The relationship between dependent and independent variables.

* What makes a **scatter** plot a good plot to use for visualizing linear regressions?

  * **Answer** Both linear regression models and scatter plots emphasize the relationships and impact of two or more variables.

Ask if students have any questions before moving forward.

### 14. Instructor Do: Time Series Linear Regression (15 min)

**Files:**

* [time_series_simple_regression.ipynb](Activities/08-Ins_Time_Series_Linear_Regression/Solved/time_series_simple_regression.ipynb)

Inform the class that the idea of linear regression for time series is the same as in the previous example, but that the implementation requires a few tweaks.

Open the notebook and show the data frame:

* This is a data frame of weather data in Austin, TX in 2010.

* The data frame has been sliced to contain data from May through July of 2010.

  ![Images/ts_regression01.png](Images/ts_regression01.png)

Show the Temperature column plotted against the date:

  ![Images/ts_regression02.png](Images/ts_regression02.png)

Explain that the goal is to perform linear regression of temperature and the date.

Explain the next two lines of code. As seen before, Scikit-learn's models require that the X variable be formatted in the correct shape.

  ```python
  X = df['Temperature'].to_frame()
  X.shape
  ```

* Converting the column into a data frame gives it 2208 rows and 1 column of data.

Explain that datetime objects have attributes, such as day of the year.

  ```python
  X['Day_of_Year'] = X.index.dayofyear
  ```

* This creates a new column, called `Day_of_Year`.

* `X.index` is in datetimeformat, and has attributes such as `dayofyear`, `weekofyear`, etc. that can be extracted from it.

* More attributes can be found in the [documentation](https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DatetimeIndex.html)

Explain creating dummy variables. The `pd.get_dummies()` method creates a column for each day of the year, and for each row assigns a numerical value for that day.

  ```python
  X_binary_encoded = pd.get_dummies(X, columns=['Day_of_Year'])
  ```

* Dummy variables are necessary because days are not continuous; they are categorical.

* As an example, the day 121 of the year is assigned 1 for day 121, but 0 for all other days.

  ![Images/ts_regression03.png](Images/ts_regression03.png)

Use the slides to show the regression equation that results from the process:

  ![Images/regression_equation01.gif](Images/regression_equation01.gif)

* Each day is given its own weight in the overall equation.

* Because each day is a separate variable in the equation, this is called multiple regression.

Additionally, explain that we delete the extraneous column in the data frame created by `pd_get_dummies()`. The argument `axis=1` specifies that it is the column that is dropped. (For rows, it would be `axis=0`.)

  ```python
  X_binary_encoded = X_binary_encoded.drop('Temperature', axis=1)
  ```

Explain that the rest of the code is familiar from previous examples:

  ```python
  y = df['Temperature'].copy()
  model = LinearRegression()
  results = model.fit(X_binary_encoded, y)
  predictions = model.predict(X_binary_encoded)
  ```

  * The `Temperature` column is specified as the dependent variable array.

  * A model is created, and fits the independent and dependent variables.

  * An array of predictions is created using `model.predict()`.

Explain that the metrics of the linear regression model are generated:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  import numpy as np
  r2 = r2_score(y, predictions)
  mse = mean_squared_error(y, predictions)
  rmse = np.sqrt(mse)
  ```

Note that the r-square value, at 0.23, is fairly low, and that we will cover the interpretation of these numbers in an upcoming activity.

Note also that the trend appears at least somewhat linear for the specified timeline, but that a longer timespan, say from January through December, will not be good for a linear regression model.

  * This underscores the important that linear regression, rather than a mechanical process, requires thinking about the variables.

  * It also highlights the importance of plotting the data before reaching a conclusion!

Take a moment to summarize the key points of this activity:

  * The idea is the same as before. We use Scikit-learn to create a model of the independent variable (X) and the dependent variable (y).

  * Because datetime data cannot be directly imported into a Scikit-learn model, we've had to create a binary encoding for each row, and drop an unnecessary column.

Finally, if time allows, quickly demonstrate an approximate visualization of the linear regression best fit line.

  ![Images/ts_regression04.png](Images/ts_regression04.png)

### 15. Students Do: Oil Futures (15 min)

In this activity, students will identify seasonal effects in oil futures prices with linear regression.

**Files:**

* [README.pdf](Activities/09-Stu_Time_Series_Linear_Regression/README.pdf)

* [oil_futures_starter.ipynb](Activities/09-Stu_Time_Series_Linear_Regression/Unsolved/oil_futures_starter.ipynb)

### 16. Instructor Do: Oil Futures Activity Review (10 min)

**Files:**

* [oil_futures.ipynb](Activities/09-Stu_Time_Series_Linear_Regression/Solved/oil_futures.ipynb)

Explain that, rather than the settle prices, we're working with returns, the daily change of the settle price in percentage terms. The returns are multiplied by 100 to make the numbers easier to work with.

  ```python
  returns = df.Settle.pct_change() *100
  ```

  ![seattle_returns.png](Images/seattle_returns.png)

Explain that we need a column of returns, and lagged returns, which will be regressed:

  ```python
  df['Return'] = returns.copy()
  df['Lagged_Return'] = returns.shift()
  df = df.dropna()
  ```

  * Here, unlike previous examples with two separate variables, `Return` values are regressed against `Lagged_Return` values. This is called auto-regression, and will be further discussed in day 2.

  * A column of lagged returns is created by shifting each value downward by 1 row.

  * NaN values must be dropped.

Go over the steps of preparing the data to use in Scikit-learn:

  ```python
  X = df['Lagged_Return'].to_frame()
  X['Week_of_year'] = X.index.weekofyear
  ```

  * Creating the `X` data frame with `to_frame()` shapes the data in requisite shape, and it returns a usable datetime index.

  * The `weekofyear` attribute is used to create a column for the week of the year.

Next, explain that dummy variables are created for each week of the year. Communiate that the function creates dummy variables for each week. That is, it assigns a value of 0 or 1 for each week. For a date that falls on week 7, for example, it will assign 1 for week 7 and 0 to all other weeks.

  ```python
  X_binary_encoded = pd.get_dummies(X, columns=['Week_of_year'])
  ```

  ![get_dummies.png](Images/get_dummies.png)

* Quickly go through the rest of the code, which is boiler plate and includes creating a regression model is created on lagged returns and returns, making predictions, and then generating r-square value.

  ```python
  y = df['Return']
  model = LinearRegression()
  res = model.fit(X_binary_encoded, y)
  predictions = model.predict(X_binary_encoded)
  r2 = r2_score(y, predictions)
  ```

  ![model_2.png](Images/model_2.png)

End the class by congratulating students on a tough day of linear regressions and statistics. Assure students that no one can master this content in a day; additional review and practice will be needed to reinforce the skills learned.

* Reiterate to students that the main goal linear regression models, especially within FinTech, is to predict and forecast prices and ROI. Like scatter plots, linear regression models focus on evaluating the relationship between dependent and independent variables.

Ask if there are any questions before moving on. Encourage students to attend office hours and to reach out to teaching staff for any additional questions or help.
