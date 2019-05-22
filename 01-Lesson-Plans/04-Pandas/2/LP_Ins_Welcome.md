## 4.2 Lesson Plan - Risk and Returns over Time

### Overview

Today's class will introduce students to the basics of time series analysis using Pandas to calculate risks and returns over time; learning Pandas time-series functionality will allow students to manage all of the financial data they will inevitably come across in FinTech. In this lesson, students will learn how to group data and apply multi-indexing on a DataFrame to analyze stock exchange data. Students will sort data, group data, leverage multi-indexing, calculate Sharpe Ratios, and compute standard deviation and risk.

### Class Objectives

By the end of class, students will be able to:

* Demonstrate the ability to group data on a DataFrame to perform calculations over the grouped data.

* Demonstrate the ability to manipulate datetime data on its different formats (single variables, dataframe columns, and series).

* Identify the calculations that can be done with datetime data.
Declare and use datetime indexes

* Calculate standard deviation, mean and median with Pandas.

* Interpret the meaning of standard deviation on risk use cases.

* Describe how stocks deviate from the mean to determine risk.

* Describe what sharpe ratios are.

* Calculate sharpe ratios using Pandas and datframes.

* Recognize what a benchmark portfolio is.

* Interpret the how the S&P500 benchmark operate.

* Conduct a benchmark using Pandas series and dataframes.

* Calculate correlation and beta using Pandas series and dataframes.

* Identify how to measure stock volatility with beta to compare volatility to the market.

### Instructor Notes

* Today's class is a quantum leap for students since they will move beyond the basics of Pandas to start learning some advance concepts to be used on risk analysis use cases.

* This class introduces new financial concepts and how they can be coded and applied using Pandas, so spend enough time to understand them. Many of these will be foreign for some students. It is important that students are able to understand what they're doing and why they are doing it, from a financial point of view. Prepare by running the code examples before class.

* Using `MultiIndex` and `groupby()` on Pandas is not trivial. Students will learn these concepts on a practical way by analyzing crypto currencies and stock exchange data, so make sure to underscore and reiterate how Pandas is lessening the burden of analysis by providing financial functions.

* Multi-indexing and grouping are pretty abstract concepts without visual representation. When discussing these two concepts, make sure visuals are available so that students can negotiate the conceptual information with the visual representation.

Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. Also encourage students to work with partners.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome (5 mins)

Welcome the students to the second day of Pandas. The focus for this class will be learning how to sort, group, multi-index, and concatenate DataFrames. Students will also learn how to use Pandas functions to calculate standard deviation and risk and sharpe ratios.

**Files:**

* [welcome-slides]()

Kick the class off with a returns refresher activity. This activity will be two fold. The focus is on teaching students how to extract historical ticker data from NASDAQ.com as a CSV, as well as calculate daily returns.

* Navigate to the [NASDAQ](https://nasdaq.com) website. Use the search bar to enter in the name or ticker of a stock. This example uses Facebook.

  ![nasdaq_search.png](Images/nasdaq_search.png)

* Use the left-hand navigation pane to select `Historical Quote`. This link will open a web UI that can be used to select the time range of data that is desired.

  ![launch_historical.png](Images/launch_historical.png)

* NASDAQ provides a simplified view into ticker prices with the `NASDAQ Official Close Price` page. This page provides access to ticker close prices. NASDAQ also provides flexibility in extracting additional data elements as well (i.e. open, high, etc.). Choose the `NASDAQ Official Close Price` page for this assignment.

  ![nasdaq_layout.png](Images/nasdaq_layout.png)

* Select `3 months` as the desired timeframe.

  ![select_timeframe.png](Images/select_timeframe.png)

* Scroll down to the `Download All Available Data` link, and right click. Click `Save Link As`. Choose a folder and name the file `fb_nasdaq.csv`. Click save.

  ![fb_nasdaq.png](Images/fb_nasdaq.png)

* Load the saved file into Pandas. Use the `index_col`, `parse_dates`, and `infer_datetime_format` attributes to create a DatetimeIndex (based off of `Trader DATE`) for date range manipulation. Emphasize to students that these attributes are used to ensure Pandas interprets the date index as a date object.

  ```python
  # Read in CSV data
  csv_path = Path('../Resources/fb_nasdaq.csv')
  fb_ticker_data = pd.read_csv(csv_path, index_col='Trade DATE', parse_dates=True, infer_datetime_format=True)
  fb_ticker_data.head()
  ```

* Drop `Symbol` Series.

  ```python
  # Drop Trade DATE and symbol column
  fb_ticker_data = fb_ticker_data.drop(columns='Symbol')
  fb_ticker_data.head()
  ```

* Slice data and calculate daily returns for Feb 2019.

  ```python
  # Calculate daily returns
  fb_slice = fb_ticker_data.loc['2019-03-01':'2019-02-01']
  fb_quarter_returns = fb_slice.pct_change()
  fb_quarter_returns
  ```

After the refresher is complete, ask students if they have any questions.

Proceed to finish reviewing the agenda for today's class. Communicate that today's activities will provide the foundation needed for students to begin grouping and aggregating data. Foreshadow what's to come by explaining that it is common to group and aggregate financial data by a number of different metrics, including dates, tickers, categories, etc. Example use cases include determining the average close price for a list of stock tickers and aggregating data (summing, adding, averaging) across time three month intervals.
