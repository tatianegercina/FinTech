## 4.2 Lesson Plan: Risk and Returns Over Time

### Overview

Last class, students got their hands dirty using Pandas to read, clean, and analyze financial data over time. Today's class will continue this trajectory by introducing students to the basics of using Pandas to conduct time Series analysis and calculate risks and returns over time. In today’s class, students will learn how to use Pandas to conduct time series analysis and calculate risks and returns over time. Learning this skill will allow students to manage all of the financial data they will inevitably encounter in FinTech. In this lesson students will also learn how to group data and apply multi-indexing on a DataFrame to improve the effectiveness of analyzing and visualizing of stock exchange data.

### Class Objectives

By the end of class, students will be able to:

* Group data on a DataFrame to perform calculations over the grouped data.

* Manipulate datetime data on its different formats: single variables, DataFrame columns, and Series.

* Identify the calculations that can be done with datetime data.

* Declare and use datetime indexes.

* Calculate standard deviation, mean, and median using Pandas.

* Interpret the meaning of standard deviation on risk use cases.

* Describe how stocks deviate from the mean to determine risk.

* Describe sharpe ratios and calculate them using Pandas and DataFrames.

### Instructor Notes

* Prepare for the lesson by running the code examples before class and reviewing the lectures. Today's lesson will be a quantum leap for students as they move beyond the basics of Pandas to more advanced concepts that can be applied to risk analysis use cases. You will need to clearly articulate what you are doing in each live demo and why, from a financial point of view. This is especially true for the standard deviation and sharpe ratio activities.

* Throughout the lesson, be sure to underscore how Pandas lessens the burden of analysis by providing financial functions such as `MultiIndex` and `groupby()`. Students will learn the practical applications of these concepts by analyzing cryptocurrencies and stock exchange data. For example, tell students they can use the `groupby` function to automatically consolidate data in order to calculate an average, rather than organizing two years’ worth of daily returns data for each cryptocurrency in an Excel file. Similarly, instead of having to create a `groupby` function themselves, students get to use the Pandas function for free.

* The sections on grouping and multi-indexing contain abstract concepts that can be difficult to grasp without visual representation. Therefore, be sure to show the slides before walking through the demo to give students a chance to absorb the conceptual information.

* Be sure to set the pace by checking for understanding, having TAs and yourself circulate during activities to assist student progress, and creating a sense of urgency without making students feel rushed. Stick to the time tracker as closely as possible, and encourage students to attend office hours if they feel lost or stuck. Lastly, encourage students to work as partners in-class on activities so that they can collaborate, troubleshoot, and discuss APIs as 2-person teams. Turn-and-teach, student led reviews, and group activities have been created to assist with this.

* Have your TAs keep the class on schedule with the [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome and Refresher Demo (5 min)

In this section, you will provide an overview of today's lesson and then get started with a warm-up activity focused on returns. Data for this activity was retrieved from [NASDAQ](http://nasdaq.com).

**File:** [Pandas Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g473a132ac1_0_7)

Welcome the students to the second day of Pandas and explain the focus of today's class.

* Students will leverage their data cleaning, indexing, and visualization skills from Day 1 in order to sort, group, multi-index, and concatenate multiple financial datasets for daily returns and investment risk analysis.

* By the end of the day, students will have used Pandas to compare two portfolios and identify which is the smarter investment.

Kick off the class with a refresher activity on returns. In this demo, you will show students how to extract historical ticker data from NASDAQ.com as a CSV. The goal is to get students to understand that all of the data they need to perform ROI analysis is just a few clicks away. Using NASDAQ.com, students can leverage historical stock data to keep a running tab on daily returns for specific stocks. Students will watch and follow along as you navigate the NASDAQ site.

Indicate to students that the class will begin with a demonstration of how to extract data from NASDAQ.com and a refresher activity on calculating daily returns.

* Navigate to the [NASDAQ](https://nasdaq.com) website. Use the search bar to enter in the name or ticker of a stock. This example uses Facebook.

  ![nasdaq_search.png](Images/nasdaq_search.png)

* Use the left-hand navigation pane to select Historical Quote. This link will open a web UI that can be used to select the time range of data that is desired.

  ![launch_historical.png](Images/launch_historical.png)

* Choose the NASDAQ Official Close Price page for this demo. Explain the following:

    * NASDAQ provides a simplified view of ticker prices with the NASDAQ Official Close Price page. This page provides access to ticker close prices.

    * NASDAQ also provides flexibility for extracting additional data elements as well (open price, high price, etc.).

  ![nasdaq_layout.png](Images/nasdaq_layout.png)

* Select 3 months as the desired timeframe.

  ![select_timeframe.png](Images/select_timeframe.png)

* Scroll to the "Download all available data" link and right click. Click "Save link as." Then, choose a folder and name the file *fb_nasdaq.csv*. Click Save.

  ![fb_nasdaq.png](Images/fb_nasdaq.png)

* Load the saved file into Pandas and output the data to the screen.

* Use the `index_col`, `parse_dates`, and `infer_datetime_format` attributes to create a DatetimeIndex (based on `Trader DATE`) for date range manipulation. Emphasize to students that these attributes are used to ensure that Pandas interprets the date index as a date object.

  ```python
  # Read in CSV data
  csv_path = Path('../Resources/fb_nasdaq.csv')
  fb_ticker_data = pd.read_csv(csv_path, index_col='Trade DATE', parse_dates=True, infer_datetime_format=True)
  fb_ticker_data.head()
  ```

* Instead of calculating daily returns, ask students to orally summarize the required steps to calculate daily returns for three months of data: "Now that we have the historical stock data, what are the necessary steps for calculating daily returns?"

* Write the steps on the board so they can be reinforced in students' visual memory:

    1. Clean the data.

    2. Execute `pct_change`.

Ask students if they have any questions.

If time remains, review the agenda for today's class. Communicate the following:

* Today's activities will provide the foundation needed for students to begin grouping and aggregating data.

* It's common to group and aggregate financial data by a number of different metrics, including dates, tickers, and categories.

* Example use cases include determining the average close price for a list of stock tickers and aggregating data (summing, adding, averaging) over time (e.g., three-month intervals).

- - -

### 2. Instructor Do: Sorting (5 min)

In this part of the lesson, you will demo how to sort DataFrame values in ascending and descending order.

**File:** [Sorting Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_35)

**File:** [sort_dataframe.ipynb](Activities/Ins_Sorting/Solved/sort_dataframe.ipynb)

Start by explaining that it is very common to sort values in ascending or descending order.

* Pandas provides a function for this called `sort_values` that will sort a DataFrame by a column.

* This function can be used to find the highest or lowest daily returns from our stock data.

Open the file `sort_dataframe.ipynb` and highlight the following:

* A DataFrame can be created from lists or dictionaries. In this example, a DataFrame of painting prices is supplied as a Python dictionary, which we convert to a DataFrame.

  ![creating-dataframes.png](Images/creating-dataframes.png)

* The DataFrame can be sorted by any column using `sort_values`. In this example, the DataFrame is sorted in ascending order (the default) by the price.

  ![sort-ascending.png](Images/sort-ascending.png)

* The DataFrame can also be sorted in descending order using the `ascending=False` parameter.

  ![sort-descending.png](Images/sort-descending.png)

Ask if there are any questions before moving on.
- - -

### 3. Student Do: Out of Sorts (15 min)

In this activity, students will extract data for a single ticker from [NASDAQ](https://nasdaq.com) and calculate daily returns for the year 2019. The data will then be sorted in descending order to identify the top 5 performing days for returns.

**File:** [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Unsolved/out_of_sorts.ipynb)

**Instructions:** [README.md](Activities/03-Stu_Sorting/README.md)

As students work on the activity, circulate the room (along with the TAs) to ensure students do not have any difficulty extracting data from the NASDAQ website.

If a student finishes the activity early, ask if they are willing to help present the solution to this activity in the next portion of the lesson. This will require the student to live code how to sort a DataFrame by more than one column.

If the student agrees, spend up to 5 minutes with them reviewing the following scenario, which is what the live-coding exercise will be based on.

**Scenario:**

There's a DataFrame named `df` that contains Olympic medal data (gold, silver, and bronze). The DataFrame has four columns:

* `country`
* `no_of_medals`
* `class_of_medal`
* `year_medal_won`

Sort the data alphabetically by country. Then, present the data so that the medal classes are sorted by number of medals awarded in descending order. (The medals awarded most should be at the top.)

- - -

### 4. Instructor Do: Review Sorting (5 min)

Review the sorting activity by having a student participate in a live-coding exercise in front of the class. This exercise should be completed only if the student feels comfortable and previously agreed to participate (and thus had some time to prepare).

Skip to the dry walk-through of the activity solution if you do not have a student who can live code this activity.

**File:** [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Solved/out_of_sorts.ipynb)

**Student Live Codes the Solution:**

Ask the student to live code a solution to the provided scenario.

If the student loses momentum or seems stuck while live coding, ask guided questions such as:

* How does one sort by more than one column?

    **Answer** List the columns to sort by in a comma separated list.

* Can I use a list to tell Pandas to sort some columns by ascending and others descending?

    **Answer** Yes. The **ascending** parameter can be used to do this. Default value is **True**. **False** will sort descending. THe **ascending** parameter accepts a list of boolean responses for when data is sorted by more than one column.

**Scenario:**

There's a DataFrame named `df` that contains Olympic medal data (gold, silver, and bronze). The DataFrame has four columns:

* `country`
* `no_of_medals`
* `class_of_medal`
* `year_medal_won`

Sort the data alphabetically by country. Then, present the data so that the medal classes are sorted by number of medals awarded in descending order. (The medals awarded most should be at the top.)

**Dry Walk-Through of the Solution:**

Do this dry walk-through if the live-coding exercise could not be completed.

Open [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Solved/out_of_sorts.ipynb) and explain the following:

* The `sort_values` function can be used to sort a DataFrame by a specific column.

    ```python
    # Sort data by `NOCP` in descending order
    tsla_sorted = tsla_daily_returns.sort_values("NOCP")
    tsla_sorted.head()
    ```

* The `sort_values` function has an attribute called `ascending` that can be configured as either `True` or `False`. Setting ascending to `True` sorts data in ascending order. `False` sorts data in descending order.

    ```python
    # Sort data by `NOCP` in descending order
    tsla_sorted = tsla_daily_returns.sort_values("NOCP", ascending=False)
    tsla_sorted.head()
    ```

    ![stu_sort_descending.png](Images/stu_sort_descending.png)

Ask if there are any questions before moving on.

- - -

### 5. Instructor Do: Groupby (10 min)

This section focuses on grouping and aggregating data. Grouping data is particularly valuable when dealing with data for multiple stocks. You will give an overview of grouping and then perform a live demo of how to use the `groupby` function in Pandas. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

**Files:**

* [Groupby Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_89)

* [groupby.ipynb](Activities/05-Ins_Groupby/Solved/groupby.ipynb)

* [starter-file.ipynb](Activities/05-Ins_Groupby/Unsolved/groupby.ipynb)

Introduce the `groupby` function by explaining:

* The `groupby` function is just as common as the `sort_values` function.

* Both of these functions are used to wrangle data into a state that is usable for analysis.

Open the [slideshow](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_89) and provide a brief overview of the `groupby` function.

* A common technique in data analysis is to summarize data by grouping similar values. One example is grouping sales data by country. In our case, we may want to group data by the stock ticker. Once the data is grouped, a count, sum, or average can be performed on the result.

* The `groupby` function segments data into groups. Once groups are created, a function or operation can be executed against each group (e.g., addition).

* Data must be grouped using `groupby` before the values in each group can be aggregated. This ensures data is aggregated at the group level rather than the column level.

Transition to providing students a demo of how to use the `groupby` function. Open the [starter file](Activities/05-Ins_Groupby/Unsolved/groupby.ipynb), and live code the following examples.

* To group data, use the `groupby` function against a non-unique column. The `groupby` function accepts a Series name as an argument. Users can also specify a return column with brackets, `[]`.

  ```python
  # Group by crypto data by cryptocurrency
  crypto_data_grp = crypto_data.groupby('cryptocurrency').count()
  crypto_data_grp
  ```

  ![group_count.png](Images/group_count.png)

* The `groupby` function requires that a function or aggregation proceed it. Whenever a function is not chained to a `groupby` function, the output will be a `DataFrameGroupBy` object rather than an actual DataFrame. `DataFrameGroupBy` objects have to be aggregated before they can be used.

  ```python
  # Group by crypto data by cryptocurrency
  crypto_data_grp = crypto_data.groupby('cryptocurrency')
  crypto_data_grp
  ```

  ```
  <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001CFF748A518>
  ```

* Example aggregate functions that can be applied against `DataFrameGroupBy` objects include `count`, `sum`, and `mean`, just to name a few. These functions will proceed a `groupby` function.

  ```python
  # Calculate average data_priceUsd for each crypto
  crypto_data_mean = crypto_data.groupby('cryptocurrency').mean()
  crypto_data_mean
  ```

  ![group_by_aggregate.png](Images/group_by_aggregate.png)

* DataFrames can be grouped by more than one column. This groups values across each specified column and summarizes the data into one record. This approach can be used as a way to identify if there are any duplicates within the data.

* In the following screenshot, each `cryptocurrency` and `data_priceUsd` combination occurs only once. The screenshots show the differences between grouping by one or multiple columns.

  ```python
  # Group by more than one column
  multi_group = crypto_data.groupby(['cryptocurrency','data_priceUsd'])['data_priceUsd'].count()
  multi_group
  ```

  ![multi_group_count.png](Images/multi_group_count.png)

  ```python
  # Group by one column
  single_group = crypto_data.groupby('cryptocurrency')['data_priceUsd'].count()
  single_group
  ```

  ![compare_single_multi.png](Images/compare_single_multi.png)

* Once data is grouped, each group can be plotted for comparison. This will plot multiple lines on a single plot. Each line is considered a subplot.

  ```python
  # Plot data_priceUsd for each crypto across time
  grouped_cryptos = crypto_data.groupby('cryptocurrency')['data_priceUsd'].plot(legend=True)
  grouped_cryptos
  ```

  ![plotting_groupby.png](Images/plotting_groupby.png)

Ask if there are any questions before moving on.

- - -

### 6. Student Do: Group Dynamics (15 min)

In this activity, students will work with historical cryptocurrency data. Specifically, they will load in cryptocurrency data, group data by each crypto, and then perform aggregations to analyze price trends. Students will then plot the results. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

**File:** [group_dynamics.ipynb](Activities/06-Stu_Groupby/Unsolved/group_dynamics.ipynb)

**Instructions:** [README.md](Activities/06-Stu_Groupby/README.md)

- - -

### 7. Instructor Do: Review Groupby (10 min)

The instructor engages students with a review of **grouping** by conducting a dry walkthrough of the student solution, in addition to asking several review questions.

**File:** [group_dynamics.ipynb](Activities/06-Stu_Groupby/Solved/group_dynamics.ipynb)

Open the solution, and complete a dry walkthrough of the student activity solution, covering the following points:

* The `groupby` function can be used to group a DataFrame by a column. This allows data to be aggregated and summarized in groups rather than all at once. DataFrames can be grouped by a single column or multiple columns.

* Data that has been grouped, known as a `DataFrameGroupByObject`, can be plotted.

    * Plotting a `DataFrameGroupByObject` will create a chart with multiple lines/bars. Each line/bar represents a respective group.

    * In order to ensure all groups are plotted on the same chart, the data/column with the data points must be specified (i.e., `data_priceUsd`). Otherwise, multiple charts will be created for each group.

  ```python
  # Determine average price across two years
  crypto_data_avg = crypto_data.groupby('cryptocurrency')['data_priceUsd'].mean()
  crypto_data_avg
  ```

  ![plot_group.png](Images/plot_group.png)

* Grouping data is valuable when aggregations need to be performed, especially across time periods. Using `groupby` with the `avg` function calculates the average price for each crypto over the two-year time period.

  ```python
  # Determine average price across two years
  crypto_data_avg = crypto_data.groupby('cryptocurrency')['data_priceUsd'].mean()
  crypto_data_avg
  ```

  ![group_average.png](Images/group_average.png)

* The `max` price for a cryptocurrency can also be calculated for a time period using the `groupby` function. This will return the highest price for the time period, per crypto.

    ```python
    # Determine max price across two years
    crypto_data_max = crypto_data.groupby('cryptocurrency')['data_priceUsd'].max()
    crypto_data_max
    ```

    ```
    cryptocurrency
    bitcoin         19339.922660
    bitcoin-cash     3476.844119
    ethereum         1346.037491
    litecoin          352.713468
    ripple              2.999459
    Name: data_priceUsd, dtype: float64
    ```

* `Min` is another common aggregate function used with grouped data. `Min` can be used to determine the lowest price in the two-year time period, per crypto.

  ```python
  # Determine min price across two years
  crypto_data_min = crypto_data.groupby('cryptocurrency')['data_priceUsd'].min()
  crypto_data_min
  ```

  ```
  cryptocurrency
  bitcoin         1714.964198
  bitcoin-cash      78.977344
  ethereum          84.374014
  litecoin          22.550468
  ripple             0.154144
  Name: data_priceUsd, dtype: float64
  ```

If time remains, end the review by calling on students to answer the following reflective questions:

* Does the concept of grouping to aggregate data make sense?

    **Answer:** Yes. When aggregating data without groups, all of the data is aggregated. Grouping and then aggregating allows calculations to be executed against groups (i.e. January's stock data would be grouped and computed separate from February's).

* How was working with more than one ticker in this activity?

    **Answer:** Working with more than one ticker accelerates processing. Instead of analyzing one ticker at a time, data for all stocks can be put into one file, analyzed as individual groups, and then combined to create a single `DataFrame` object.

* What are some examples of situations where data would need to be grouped and then aggregated?

    **Answer:** Calculating daily returns by quarter.

    **Answer:** Calculating final grades for each student per class.

    **Answer:** Calculating the number of horror movies released every decade between 1970 and 1990.

- - -

### 8. Instructor Do: Multi-Indexing (10 min)

Now that students have learned that indexes can be created by using the `groupby` key, it's important they know how to directly multi-index DataFrames. Multi-indexing is a direct way to create multiple indexes in a DataFrame. Like the `groupby` function, multi-indexing allows data to be grouped and accessed or manipulated by group. Data for this activity was retrieved from [NASDAQ](http://nasdaq.com).

**Files:**

* [Multi-Indexing Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_207)

* [multi_indexing.ipynb](Activities/08-Ins_Multi_Indexing/Solved/multi_indexing.ipynb)

* [starter-file](Activities/08-Ins_Multi_Indexing/Unsolved/multi_indexing.ipynb)

Open the [slideshow](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_207) and provide an overview of multi-indexing.

* Multi-indexing is the process of indexing a dataset by more than one value. Multi-indexing is like using two bookmarks in a book. Each bookmark is an index, and depending on which index you go to, you'll get different content.

* Multi-indexing is sometimes referred to as hierarchical indexing, as relationships can exist between indexes. For example, a state can be one index and a city can be another. Because a city belongs to a state, these indexes would be hierarchical.

* Multiple indexes are valuable because they enable dimensional data to be grouped and retrieved.

    * This is particularly valuable when working with financial data and dates. While dates are great to index, dates do not always provide all of the detail needed to manipulate and analyze data.

    * For example, when looking at stock prices and purchases over time, it is important to group data by both date and ticker. In this operation, both date and ticker can be indexes, and by specifying date and ticker, you can slice out the price of a particular stock at a specific point in time.

* Essentially, multi-indexing improves data storage, lookup, and manipulation/assignment.

Open the [starter-file](Activities/08-Ins_Multi_Indexing/Unsolved/multi_indexing.ipynb), and live code how to create and use multiple indexes, as well as how to access data using more than one index.

* Multi-indexing is commonly done when working with `Date` data.

* When used as an index, `Date` data is considered a `DatetimeIndex`. `DatetimeIndexes` have the ability to inherently create multi-indexing.

* A `DatetimeIndex` can be created by passing a `Date` field to the `index_col` attribute when using `read_csv`. `parse_dates` and `infer_datetime_format` should also be included.

    ```python
    # Read in data
    csv_path = Path("../Resources/stock_data_by_ticker.csv")
    ticker_data = pd.read_csv(csv_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
    ticker_data.head()
    ```

* `DatetimeIndexes` can be split into year, month, and day segments. The `DatetimeIndex` object includes the attributes `index.year`, `index.month`, and `index.day` for this. Passing these to a `groupby` statement will create multiple indexes based off of each attribute.

  ```python
  # Group by year, month, and day
  ticker_data_grp = ticker_data.groupby([ticker_data.index.year, ticker_data.index.month, ticker_data.index.day]).first()
  ticker_data_grp.head()
   ```

  ![multi_index_date.png](Images/multi_index_date.png)

* Multi-indexed data can be selected by using the `first` and `last` functions. `First` selects the first multi-index group, and `last` chooses the last.

  ```python
  # Group by year, month, and day
  ticker_data_grp_1 = ticker_data.groupby([ticker_data.index.year,ticker_data.index.month, ticker_data.index.day]).first()
  ticker_data_grp_1.head()
  ```

  ![multi_index_first.png](Images/multi_index_first.png)

* Because multi-indexing involves grouping data, an aggregation can be applied against the data. A common example is the `mean` function for calculating average. This is an alternative to using the `first` and `last` functions. Because aggregate functions are being used, outputs represent summarized/aggregated records.

  ```python
  # Group by year and month and calculate average
  ticker_data_grp_2 = ticker_data.groupby([ticker_data.index.year, ticker_data.index.month]).mean()
  ticker_data_grp_2.head()
  ```

  ![multi_index_agg.png](Images/multi_index_agg.png)

* The `loc` function can be used to slice data from a DataFrame with multiple indexes. While not all indexes are required to be passed, the top level index needs to be specified (e.g., `year`). When all indexes are passed to the `loc` function, only one record will be returned. If fewer than all indexes are provided, more than one record of data will be output. Essentially, indexes have to be accessed and used hierarchically (i.e., `year` > `month` > `day`).

    ```python
    # Slice data for 4/12/2019 from first group
    ticker_data_slice = ticker_data_grp.loc[2019,4,12]
    ticker_data_slice.head()
    ```

  ![multi_index_slice.png](Images/multi_index_slice.png)

  ```python
  # Slice data for April 2019
  ticker_data_slice = ticker_data_grp.loc[2019,4]
  ticker_data_slice.head()
  ```

  ![slice_by_month.png](Images/slice_by_month.png)

Ask if there are any questions before moving on.
- - -

### 9. Student Do: Indexing Fever (15 min)

In this activity, students will use hierarchical indexes to gain access to historical stock data. The objective of the assignment is for students to take their indexing skills to the next level by using DataFrames with multiple indices. Students will leverage [NASDAQ](https://nasdaq.com) data to perform data segmentation for a single ticker across multiple months in a year.

**File:** [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Unsolved/Core/indexing_fever.ipynb)

**Instructions:** [README.md](Activities/09-Stu_Multi_Indexing/README.md)

- - -

### 10. Instructor Do: Review Multi-Indexing (10 min)

In this activity, the instructor will perform a dry walkthrough of the student activity solution.

**File:** [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Solved/Core/indexing_fever.ipynb)

Open [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Solved/Core/indexing_fever.ipynb), and review the solution, covering the following points:

* The `read_csv` accepts arguments that make creating indexes easy. Passing a column name to the `read_csv` `index_col` parameter will create a DataFrame index based off of the values in that Series.

* When working with Dates as indexes, it is common to set the following two `read_csv` parameters to `True`: `parse_dates` and `infer_datetime_format`. These two date parameters for `read_csv` will eliminate the need to cast a date Series to a `datetime` object.

  ```python
  # Read csv data with dates
  csv_path = Path("../../Resources/nasdaq_data.csv")
  nasdaq_data = pd.read_csv(csv_path, parse_dates=True, index_col="Trade DATE", infer_datetime_format=True)
  ```

* Multi-indexing is used to create multiple lookup points for data, as well as hierarchal relationships between data elements.

* Multi-indexing will enable users to index data with more than one data element (e.g., `year` and `month`).

* Multi-indexing is valuable because it enables data to be indexed with more than one column. Using multi-indexing, especially with date Series, ensures financial data can be stored and accessed by date.

  ![Multi_Indexing_Relationship.png](Images/Multi_Indexing_Relationship.png)

* Grouping data is a way to naturally create indices. Grouping data by a `DatetimeIndex` creates two indices: one for the year and one for the month. Each of these can be accessed by using the `year` and `month` attributes. Grouped data can be selected by using the `first` and `last` functions. These will return the first group of grouped items and the last group, respectively.

  ```python
  # Set multi-index by grouping
  nasdaq_data_grp = nasdaq_data.groupby([nasdaq_data.index.year, nasdaq_data.index.month]).first()
  nasdaq_data_grp.head()
  ```

  ![Multi_Indexing_Groupby.png](Images/Multi_Indexing_Groupby.png)

* Once items have been grouped and indexed, data can be retrieved using those indices.

    ```python
    # Select GOOG NOCP for May 2019
    google_may_2019_data = nasdaq_data_grp.loc[2019,5]
    print(google_may_2019_data)
    ```

    ![Multi_Indexing_Lookup.png](Images/Multi_Indexing_Lookup.png)

* Changes in time can be calculated by using the `timedelta` Pandas function. The function accepts the number of days one wants to traverse as an argument, and then identifies the specific date. For example, the `timedelta` function can be used to determine what the date was 60 days from today. `Year` and `month` attributes are also available for `timedelta` objects.

  ```python
  # Calculating GOOG stock price for 30 days ago
  time_delta = date.today() - timedelta(days=30)
  goog_thirty_days_ago = nasdaq_data_grp.loc[(time_delta.year,time_delta.month)]
  print(goog_thirty_days_ago)
  ```

* In order to use the `timedelta` function, it needs to be imported. To access date functions that identify the current time and  day, the `date` object will also need to be imported from `datetime`. For example, `date.today()` can be used to determine today's date.

  ```python
  from datetime import datetime, date, timedelta
  ```

Ask if there are any questions before moving on.
- - -

### 11. BREAK (15 min)

- - -

### 12. Instructor Do: Concatenating DataFrames (5 min)

The instructor provides an overview of concatenation and then proceeds into live coding how to concatenate DataFrames. Data for this activity was retrieved from [Kaggle](http://kaggle.com).

**Files:**

* [Concatenation Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_252)

* [concat_dataframe.ipynb](Activities/12-Ins_Concat_DataFrame/Solved/concat_dataframes.ipynb)

Introduce the topic of concatenation by explaining the following:

* Indexing, grouping, and sorting datasets are all steps taken to prepare data for analysis. Another is combining, also known as concatenating, datasets. This is beneficial when more than one dataset needs to be combined.

* For example, multiple months of financial records or investment data from different markets can be consolidated into one dataset in order to streamline and centralize data analysis.

Open the [slideshow](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_252) and provide a brief overview of concatenation:

* Concatenation is the process of appending data from one object with another.

* Concatenation creates a new object that represents data from all concatenated objects.

* There are multiple ways to concatenate objects, including by column and row.

* DataFrames can be joined together, or `concatenated`, using the Pandas `concat` function. This function enables users to join and combine more than one DataFrame.

* The `concat` function accepts the following arguments:

    * a list of DataFrames to be joined

    * the `axis` to join on (by column or row)

    * the `join` operation (inner vs. outer)

Open the [starter-file](Activities/12-Ins_Concat_DataFrame/Unsolved/concat_dataframes.ipynb), and live code the following examples:

* DataFrames can be joined by either `column` or `row`. The `axis` argument can be configured to specify which to use.

* If a new dataset needs to be created where multiple columns from different DataFrames need to be reflected, the DataFrames should be joined on `column`. This will create a new, composite DataFrame that incorporates the columns from all DataFrames.

* If rows from one DataFrame simply need to be combined or added to another DataFrame, the DataFrames should be joined on `row`. Joining on the `row` axis would require all DataFrames being joined to have the same columns.

  ```python
  # Join UK, France, and Netherlands full datasets by axis
  joined_data_rows = pd.concat([france_data, uk_data, netherlands_data], axis="rows", join="inner")
  joined_data_rows
  ```

  ![concat_rows.png](Images/concat_rows.png)

  ```python
  # Join Customer and products by columns axis
  joined_data_cols = pd.concat([customer_data, products_data], axis="columns", join="inner")
  joined_data_cols.head()
  ```

  ![concat_columns.png](Images/concat_columns.png)

* The `concat` function creates a new DataFrame that includes data from all datasets that were joined. The amount of data returned will depend on the type of `join` performed when concatenating.

Indicate to students that additional information can be found in the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#set-logic-on-the-other-axes).

* The `join="inner"` argument will create an intersection of the data.

* The `join="outer"` argument will union the data.

Ask if there are any questions before moving on.

- - -

### 13. Student Do: Mastering Concatenation (15 min)

In this activity, students get hands one experiencing combining multiple DataFrames using the `concat` function. The goal of the activity is for students to take dues and membership data from two community organizations and combine the data into a single DataFrame.

**File:** [mastering_concatenation.ipynb](Activities/13-Stu_Concat_DataFrames/Unsolved/mastering_concatenation.ipynb)

**Instructions:** [README.md](Activities/13-Stu_Concat_DataFrames/README.md)

- - -

### 14. Instructor Do: Review Concat DataFrames (5 min)

The instructor reviews concatenation by conducting a Q & A session and a dry walkthrough of the solution for the previous student activity.

**File:** [mastering_concatenation.ipynb](Activities/13-Stu_Concat_DataFrames/Solved/mastering_concatenation.ipynb)

Start the review by conducting a Q & A with the following questions:

* If you wanted to consolidate two DataFrames with the same columns into one DataFrame, which `concat` axis would you use?

    **Answer:** By rows. Concatenating by rows will combine the two DataFrames so that all rows are in one DataFrame.

* Let's say you want to take an intersection of two DataFrames that you have combined. Would you use the inner join operation or outer join operation?

    **Answer:** Inner join. Inner join will return a DataFrame with only matching rows.

* Which join will produce more rows? An inner join our outer join?

    **Answer:** Outer join. Inner joins represent only a section of all of the data.

Open [mastering_concatenation.ipynb](Activities/13-Stu_Concat_DataFrames/Solved/mastering_concatenation.ipynb) to review the solution and go over the following points:

* The `concat` function can be used to combine or link more than one DataFrame.

* DataFrames can be concatenated either by `rows` or `columns`.

    * Concatenating by `row` will create a DataFrame that has the total number of rows.

    * Concatenating by `columns` produces a DataFrame that has the columns from all DataFrames concatenated.

  ![concat_axis.png](Images/concat_axis.png)

* DataFrames should be concatenated by `rows` when the columns of the DataFrame are the same and should remain the same. The idea is that the rows are appended.

  ![stu_concat_rows.png](Images/stu_concat_rows.png)

* DataFrames should be concatenated by `columns` when columns from one DataFrame need to be combined with columns from another. The idea is that the columns are appended.

  ![stu_concat_cols.png](Images/stu_concat_cols.png)

Ask if there are any questions before moving on.

- - -

### 15. Instructor Do: Standard Deviation and Risk (10 min)

This section focuses on standard deviation and how it can be used to determine the risk associated with an investment. You will demo how to calculate standard deviation using Pandas. Students will need the concepts covered in this section to calculate sharpe ratios in the next activity. Data for this activity was retrieved from [NASDAQ](http://nasdaq.com).

**Files:**

* [Standed Deviation and Risk Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_293)

* [std_dev_risk.ipynb](Activities/15-Ins_Std_Dev_Risk/Solved/std_dev_risk.ipynb)

Introduce **standard deviation and risk** to students by communicating that everything completed in class up until this point has been to prepare them for portfolio and risk analysis.

* With daily returns calculated, and data from multiple portfolios combined into one dataset, students are now able to complete a holistic analysis of stock data.

* The next step is to use **standard deviation and risk** to analyze portfolio performance, calculate risk, and identify risky investments.

Open the [slideshow](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_293) and explain the following:

* A key aspect of analyzing portfolio and stock data is determining risk. Pandas provides a Series of functions that can be used to calculate risk.

* One component of risk is calculating the mean performance or price of a stock. The second is calculating the standard deviatio`.

* **Mean** can be used to determine the average value of a portfolio or stock overtime. This can serve as a baseline for measuring risk and value: a portfolio/stock performing above average is more valuable; investing in a portfolio or buying a stock performing below average is risky business.

* A common technique for measuring how far away an asset is from the mean is calculating the standard deviation. **Standard deviation** identifies exactly how far away a value is from the average price. A low number indicates that the value is not far from the average; a high standard deviation means that the value is an outlier.

Live code how to use Pandas to calculate standard deviation in order evaluate risk:

* Standard deviation should be calculated using daily returns data. Calculating standard deviation against daily returns will help identify risk based on return value rather than price volatility.

  ![std_dev.png](Images/std_dev.png)

* The `std` Pandas function can be used to determine the risk associated with a portfolio or stock. Behind the scenes, the `std` function calculates the mean/average, and then it evaluates how far away from the average the input is. The function returns a new DataFrame.

  ```python
  # Daily Standard Deviations
  daily_returns.std()
  ```

  ```
  AAPL    0.018106
  MSFT    0.017839
  GOOG    0.017724
  FB      0.023949
  AMZN    0.022768
  dtype: float64
  ```

* Sorting the output from the `std` function in descending order (using `sort_values`) will display which portfolios/stocks have the most and least amounts of risk.

  ```python
  # Identify the stock with the most and least risk
  daily_std.sort_values(ascending=False)
  ```

  ![risk_sort.png](Images/risk_sort.png)

* It is often necessary to calculate standard deviation at the yearly level. Calculating annualized standard deviation can be done by multiplying the square root (`sqrt`) of the number of trading days in a year (`252`) with the standard deviation.

  ```python
  # Calculate the annualized standard deviation (252 trading days)
  annualized_std = daily_std * np.sqrt(252)
  annualized_std.head()
  ```

  ```
  AAPL    0.287428
  MSFT    0.283180
  GOOG    0.281354
  FB      0.380172
  AMZN    0.361434
  dtype: float64
  ```

* A key way to assess risk is to use the `plot.hist` function to create a chart of standard deviation trends. This will visually demonstrate the mean value, as well as the number and severity of any deviations for each element being plotted (i.e., each portfolio).

  ```python
  portfolio_a_std = np.random.normal(scale=0.5, size=10000)
  portfolio_b_std = np.random.normal(scale=1.0, size=10000)
  portfolio_c_std = np.random.normal(scale=1.5, size=10000)

  portfolio_std = pd.DataFrame({
      "0.5": portfolio_a_std,
      "1.0": portfolio_b_std,
      "1.5": portfolio_c_std
  })

  portfolio_std.plot.hist(stacked=True, bins=100)
  ```

  ![std_plot.png](Images/std_plot.png)

* Another way to visualize standard deviation is with a box plot. **Box plots** display the total spread of the data, and they can be created using the `plot.box` Pandas function.

* Box plots have what are known as whiskers. **Whiskers** represent the range, or spread, of the data. Data elements that extend beyond the whiskers are considered outliers.

  ```python
  # Plot box plot
  portfolio_std.plot.box()
  ```

  ![std_dev_box.png](Images/std_dev_box.png)

Emphasize that the takeaway from these charts is that the greater the spread, the greater the risk. The greater the risk, the greater the potential for earnings and lost.

Ask if there are any questions before moving on.

- - -

### 16. Instructor Do: Sharpe Ratios (5 min)

In this section, students will be introduced to sharpe ratios and why risk-reward ratios are important in finance. Data for this activity was retrieved from [NASDAQ](http://nasdaq.com).

**Files:**

* [Sharpe Ratios Slides](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_351)

* [sharpe_ratios.py](Activities/16-Ins_Sharpe_Ratios/Solved/sharpe_ratios.py)

Communicate to students that their skill in identifying risk and assessing investment performance has prepared them to learn how to adjust for risk in order to maximize reward.

Open the [slideshow](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_351) and begin the overview of sharpe ratios and how they are calculated. Cover the following points:

* **Sharpe ratios** are used to help compare rate of return for an investment with its risk. Sharpe ratios shed light on the potential of profits even with risk involved.

* Sharpe ratios measure the excess return for each deviation. This will identify, in the wake of risk, how much profit is left to be gained.

* Sharpe ratios are calculated by subtracting the **return of portfolio** from the investment's **risk-free rate**. The difference is than divided by the standard deviation.

    ![sharpe_ratio_formula.png](Images/sharpe_ratio_formula.png)

Open [sharpe_ratios.py](Activities/16-Ins_Sharpe_Ratios/Solved/sharpe_ratios.py) and live code how to calculate and plot sharpe ratios:

* Sharpe ratios are commonly used to indicate whether or not an investment is a good decision. While standard deviation illustrates how far an investment has deviated from its average, sharpe ratios uses standard deviation to illustrate the relationship between standard deviation and risk-reward.

* Sharpe ratios enable investors to judge whether or not an investment is a good decision. Sharpe ratios adjust for risk, making them a valuable indicator of asset performance.

  ```python
  # Calculate Sharpe Ratio
  sharpe_ratios = (all_portfolios_returns.mean() * 252) / (all_portfolios_returns.std() * np.sqrt(252))
  sharpe_ratios
  ```

  ![sharpe_ratios.png](Images/sharpe_ratios.png)

* The ratio of return-to-risk can be used to determine which stocks and/or portfolios have outperformed the others. The higher the sharpe ratio, the better the investment.

* The `plot` function can be used to visually compare sharpe ratios.

  ```python
  # Plot sharpe ratios
  sharpe_ratios.plot(kind="bar", title="Sharpe Ratios")
  ```

  ![sharpe_ratios_plot.png](Images/sharpe_ratios_plot.png)

Ask if there are any questions before moving on.
- - -

### 17. Student Do: Risky Business (20 min)

It's time to put it all together. In this activity, students will prep data and use standard deviation and sharpe ratios to analyze cryptocurrency portfolio performance. The goal is to calculate which portfolio has the highest risk. Students will also identify which individual cryptos have had the greatest return. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

Encourage students to work in pairs to complete the solution.

**File:** [risky_business.ipynb](Activities/17-Stu_Risky_Business/Unsolved/Core/risky_business.ipynb)

**Instructions:** [README.md](Activities/17-Stu_Risky_Business/README.md)

- - -

### 18. Instructor Do: Review Risky Business (10 min)

**File:** [risky_business.ipynb](Activities/17-Stu_Risky_Business/Solved/Core/risky_business.ipynb)

Open [risky_business.ipynb](Activities/17-Stu_Risky_Business/Solved/Core/risky_business.ipynb) to review the activity solution with students. Highlight the following:

* The `concat` function can be used to combine portfolio returns. This enables analysis (i.e., standard deviation) of an entire portfolio rather than an individual stock. It also allows data from investments/portfolio A to be compared with investments/portfolio B.

* Harold's portfolio returns are combined with student returns in order to later calculate standard deviation and sharpe ratio across the board.

  ```python
  # Concat returns DataFrames
  all_returns = pd.concat([harold_returns,my_returns], axis='columns', join='inner')
  all_returns.head()
  ```

  ![stu_concat_compare.png](Images/stu_concat_compare.png)

* Standard deviation is required to calculate sharpe ratios. Standard deviation calculates the average value and compares the distribution of values to that average.

* The `std` function can be used to compute standard deviation. The output from the function is a Series that indicates how far the value is from the mean, in the same units as the base data. The greater the value/deviation, the greater the risk and volatility.

  ```python
  # Calculate std dev
  all_portfolio_std = all_returns.std()
  all_portfolio_std.head()
  ```

  ```
  BTC     0.049189
  BTT     0.006185
  DOGE    0.062264
  ETH     0.050074
  LTC     0.048783
  dtype: float64
  ```

* Sharpe ratios are used to examine investment performance based on the risk-to-reward ratio.

    * The sharpe ratio calculates the risk associated with a return and then divides that by the standard deviation of a return.

    * The higher the sharpe ratio, the greater the reward associated with the risk. A high sharpe ratio indicates a smart investment.

* Calculating the sharpe ratio for Harold's and the students' portfolios reveals whose portfolio has the greatest reward associated with the risk.

  ```python
  # Calculate sharpe ratio
  sharpe_ratios = (all_returns.mean() * 252) / (all_portfolio_std * np.sqrt(252))
  sharpe_ratios.head()
  ```

  ```
  BTC    -0.269714
  BTT    -0.878716
  DOGE    0.105533
  ETH    -0.214963
  LTC    -0.222482
  dtype: float64
  ```

* Sharpe ratios can be visually represented with a bar chart. This allows users to easily see which investments have high and low sharpe ratios.

  ```python
  # Plot
  sharpe_ratios.plot.bar(title='Sharpe Ratios')
  ```

  ![sharpe_plot.png](Images/sharpe_plot.png)

Ask students the following questions:

* How many smart investments did Harold make compared to risky investments? How many did you make?

    **Answer:** Out of his 10 investments, Harold only made 4 good investments. Out of the students' 6 investments, 3 of them were smart investments.

* Which cryptos are the smartest investment?

    **Answer:** DOGE, TRON, and XML are the smartest crypto investments.

Ask if there are any questions before moving on.
- - -

### 19. Instructor Do: Decompress and End Class (5 min)

* [Congratulations Slide](https://docs.google.com/presentation/d/1pFBfNwFoHcvTsG1PGCvQLS9rpQdn645n9QrqTBjP7zw/edit#slide=id.g595c28c35f_0_392)

Another battle won, another level completed. Students have been excelling at a quantum speed, and it's important they understand this. End the class with the following positive remarks:

* Students have come so far. Earlier in the week they were just learning how to use Pandas. Now they're using Pandas to analyze investment risk and predict smart investments.

* These skills are applicable to the real world. Being able to programmatically combine and group data in order to perform financial analysis and calculate investment risk will go a long way professionally and personally.

Engage the students by asking how they plan to incorporate skills from today's lesson into their resumes and/or work lives. Two skills that should be highlighted are:

* Data Engineering and Analysis

    * The activities completed today involved reading, cleaning, combining, grouping, aggregating, and analyzing multiple datasets; this is actual data engineering and analysis.

    * Data engineers and data analysts complete these same tasks every day.

* Financial Reporting and Visualization

    * The final activity presents a real-world use case. With the proper narrative and flow, the final activity could be used as a financial report.

    * Students have calculated daily returns for investments and identified which investments are expected to produce the most reward and risk. They essentially have a report that presents findings on two portfolios and identifies the smarter investment.

### End Class

- - -
© 2019 Trilogy Education Services
