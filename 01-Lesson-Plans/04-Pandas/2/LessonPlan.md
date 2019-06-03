## 4.2 Lesson Plan - Risk and Returns over Time

### Overview

In the last class, students got their hands dirty using Pandas to read, clean, and analyze financial data over time. Today's class will continue this trajectory and will introduce students to the basics of using Pandas to conduct time series analysis and calculate risks and returns over time.

Learning how to use Pandas to analyze time-series data will allow students to manage all of the financial data they will inevitably come across in FinTech. In this lesson, students will learn how to group data and apply multi-indexing on a DataFrame to improve the effectiveness of analyzing and visualizing stock exchange data.

This class lesson will afford students the opportunity to demonstrate competence in using Pandas to sort and group data, create and leverage multiple indexes, calculate sharpe ratios, and compute standard deviation and risk--all of which are critical when evaluating investment/portfolio performance and return on investment.

### Class Objectives

By the end of class, students will be able to:

* Demonstrate the ability to group data on a DataFrame to perform calculations over the grouped data.

* Demonstrate the ability to manipulate datetime data on its different formats (single variables, DataFrame columns, and series).

* Identify the calculations that can be done with datetime data.
Declare and use datetime indexes

* Calculate standard deviation, mean and median with Pandas.

* Interpret the meaning of standard deviation on risk use cases.

* Describe how stocks deviate from the mean to determine risk.

* Describe what sharpe ratios are.

* Calculate sharpe ratios using Pandas and DataFrames.

### Instructor Notes

* Today's class is a quantum leap for students since they will move beyond the basics of Pandas to start learning some advance concepts to be used on risk analysis use cases.

* Since this class introduces new financial concepts and how they can be coded and applied using Pandas, it is important to spend time preparing and running the code examples before class. As you prepare, be sure you are able to help students articulate what they are doing and why they are doing it, from a financial point of view. This is especially true for the standard deviation and sharpe ratio activities. Students will need clear explanation of these financial/statistical concepts.

* Using `MultiIndex` and `groupby()` on Pandas is not trivial. Students will learn these concepts on a practical way by analyzing crypto currencies and stock exchange data, so make sure to underscore and reiterate how Pandas is lessening the burden of analysis by providing financial functions. For example, instead of having to organize two years worth of daily returns data for each cryptocurrency in an Excel file just to calculate the average, the `groupby` function can automatically consolidate the data so that an average can be calculated. Similarly, instead of being burdened with having to create a `groupby` function themselves, students get to use the Pandas function for free.

* The grouping and multi-indexing modules are pretty abstract concepts and are sometimes difficult to understand without visual representation. When reviewing these modules, make sure to present the slides before completing the demo so that students can absorb the conceptual information with the visual representation.

Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. Also encourage students to work with partners.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome (5 mins)

Welcome the students to the second day of Pandas. Students will leverage data cleaning, indexing, and visualization skills from Day 1 in order to sort, group, multi-index, and concatenate multiple financial datasets for daily returns and investment risk analysis. By the end of the day, students will have used Pandas to compare two portfolios and identify which is the smarter investment.

**Files:**

* [welcome-slides]()

Kick the class off with a returns refresher activity. This activity will be two fold. The focus is on demonstrating to students how to extract historical ticker data from NASDAQ.com as a CSV so that they can understand that all of the data they need to perform ROI analysis is just a few clicks away. Using NASDAQ.com, students can leverage historical stock data to keep a running tab on daily returns for specific stocks. Students will watch and follow along as the instructor navigates the NASDAQ site.

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

* Load the saved file into Pandas, and output the data to the screen. Use the `index_col`, `parse_dates`, and `infer_datetime_format` attributes to create a DatetimeIndex (based off of `Trader DATE`) for date range manipulation. Emphasize to students that these attributes are used to ensure Pandas interprets the date index as a date object.

  ```python
  # Read in CSV data
  csv_path = Path('../Resources/fb_nasdaq.csv')
  fb_ticker_data = pd.read_csv(csv_path, index_col='Trade DATE', parse_dates=True, infer_datetime_format=True)
  fb_ticker_data.head()
  ```

* Instead of actually calculating daily returns, ask the students to orally summarize the required steps to calculate daily returns for three months of data. Write the steps on the board so they can be reinforced in the students' visual memory:

  > "Now that we have the historical stock data, what are the necessary steps for calculating daily returns?"

    1. Clean the data

    2. Execute pct_change

After the refresher is complete, ask students if they have any questions.

If time remains, proceed to finish reviewing the agenda for today's class. Communicate that today's activities will provide the foundation needed for students to begin grouping and aggregating data. Foreshadow what's to come by explaining that it is common to group and aggregate financial data by a number of different metrics, including dates, tickers, categories, etc. Example use cases include determining the average close price for a list of stock tickers and aggregating data (summing, adding, averaging) across time three month intervals.

- - -

### 2. Instructor Do: Sorting (5 mins)

In this activity, students will learn how to sort DataFrame values in ascending and descending order. Instructors will disseminate the necessary conceptual and technical information through a live demonstration.

**Files:**

* [sort_dataframe.ipynb](Activities/Ins_Sorting/Solved/sort_dataframe.ipynb)

Explain that it is very common to sort values in ascending or descending order. Pandas provides a function for this called `sort_values` that will sort a DataFrame by a column. We can use this to find the highest or lowest daily returns from our stock data.

Walk through the solution and highlight the following:

* A DataFrame can be created from lists or dictionaries. In this example, a DataFrame of painting prices is supplied as a Python Dictionary which we convert to a DataFrame.

  ![creating-dataframes.png](Images/creating-dataframes.png)

* The DataFrame can be sorted by any column using `sort_values`. In this example, the DataFrame is sorted in ascending order (the default) by the price.

  ![sort-ascending.png](Images/sort-ascending.png)

* The DataFrame can also be sorted in descending order using the `ascending=False` parameter.

  ![sort-descending.png](Images/sort-descending.png)

- - -

### 3. Students Do: Sorting (15 mins)

In this activity, students will extract data for a single ticker from NASDAQ.com and calculate daily returns for the year of 2019. The data will then be sorted in descending order to identify the top 5 performing days for returns.

**Files:**

* [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Unsolved/out_of_sorts.ipynb)

**Instructions:**

* [README.md](Activities/03-Stu_Sorting/README.md)

While students are completing the activity, instructors and TAs should be walking around to ensure students do not have any difficulty extracting data from the NASDAQ website.

If a student finishes the activity early, ask them if they'd be willing to participate in an activity in the review module. The activity will include the student live coding how to sort a DataFrame by more than one column. Spend up to 5 minutes with this student preparing for and reviewing the prompt. The prompt can be found below:

* Let's say there's a DataFrame named `df` that contains Olympic medal data (gold, silver, and bronze). The DataFrame has four columns: `country`, `no_of_medals`, `class_of_medal`, and `year_medal_won`. Sort the data alphabetically by country. Then, present the data so that the medal classes are sorted by number of medals awarded, in descending order (the medals awarded most should be at the top).

- - -

### 4. Instructor Do: Review Sorting (5 mins)

**Files:**

* [out_of_sorts.ipynb](Activities/03-Stu_Sorting/Solved/out_of_sorts.ipynb)

Review the sorting activity by having a student participate in a live coding exercise in front of the class. This exercise should only be completed if a student feels comfortable. The student should also have agreed in the last module to conduct the live coding exercise. If a student doesn't agree to complete the activity, or none of the students seemed exceptionally competent with the `sort_values` function/concepts, skip down to the dry walkthrough of the solution.

Ask the student who was vetted out in the previous exercise to live code an answer to the following prompt. If the student loses momentum or seems stuck while live coding, ask guided questions like "How does one sort by more than one column?" and "Can I use a list to tell Pandas to sort some columns by ascending and others descending?"

Continue the reflective exercise by asking the student who was vetted out in the previous exercise to live code an answer to the following prompt. If the student loses momentum or seems stuck while live coding, ask guided questions like "How does one sort by more than one column?" and "Can I use a list to tell Pandas to sort some columns by ascending and others descending?"

Scenario:

* Let's say there's a DataFrame named `df` that contains Olympic medal data (gold, silver, and bronze). The DataFrame has four columns: `country`, `no_of_medals`, `class_of_medal`, and `year_medal_won`. Sort the data alphabetically by country. Then, present the data so that the medal classes are sorted by number of medals awarded, in descending order (the medals awarded most should be at the top).

  ```python
  df.sort_values(['country','no_of_medals'], ascending=[True,False])
  ```

If the student live coding review activity could not be completed, open the solution and explain the following:

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

Ask for any remaining questions before moving on.

- - -

### 5. Instructor Do: Groupby (10 mins)

This module focuses on getting students started with grouping and aggregating data. Grouping data is particularly valuable when dealing with data for multiple stocks. Students will receive a brief overview of what grouping is, and then the instructor will perform a live demo of how to use the Pandas `groupby` function.

**Files:**

* [groupby.ipynb](Activities/05-Ins_Groupby/Solved/groupby.ipynb)

The `groupby` function is just as common as the `sort_values` function. Both of these functions are used to wrangle data into a state that is usable for analysis.

Navigate to the Unit 4.2 slides, and provide a brief overview of the `groupby` function.

* A common technique with data analysis is to summarize data by grouping similar values. An example of this might be to group sales data by country, or in our case, we may want to group the data by the stock ticker and count, sum, or average the results per stock.

* The `groupby` function operates by segmenting a dataset into groups. Once the groups are created, a function or operation can be executed against each group (i.e. addition). The results for each group are then combined together to create the final output.

* Data has to be grouped using `groupby` before the values in each group can be aggregated respectively. This ensures that data is aggregated at the group level rather than the column level.

Demonstrate how to use the `groupby` function. Live code the below examples.

* A DataFrame can be grouped by any Series that contains repeating values or categories. TO group data, use the `groupby` function. The `groupby` function accepts a Series name as an argument, and users can also specify a return column with `[]` brackets.

  ```python
  # Group by crypto data by cryptocurrency
  crypto_data_grp = crypto_data.groupby('cryptocurrency').count()
  crypto_data_grp
  ```

  ![group_count.png](Images/group_count.png)

* The `groupby` function requires that a function or aggregation be applied against the grouped data. When a function is not provided, a `DataFrameGroupBy` object is returned instead of data. `DataFrameGroupBy` objects have to be aggregated in order to be used.

  ```python
  # Group by crypto data by cryptocurrency
  crypto_data_grp = crypto_data.groupby('cryptocurrency')
  crypto_data_grp
  ```

  ```
  <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001CFF748A518>
  ```

* Aggregate functions (i.e. `count`, `sum`, `mean`) can be used to summarize data. This allows calculations to be executed against specific groups of data rather than an entire Series.

  ```python
  # Calculate average data_priceUsd for each crypto
  crypto_data_mean = crypto_data.groupby('cryptocurrency').mean()
  crypto_data_mean
  ```

  ![group_by_aggregate.png](Images/group_by_aggregate.png)

* DataFrames can also be grouped by more than one column. This groups values across each specified column and summarizes the data into one record. This approach can be used as a way to identify if there are any duplicates within the data. As evidenced by the below screenshot, each `cryptocurrency` and `data_priceUsd` combination only occurs once. The below screenshots communicate the differences between grouping by one or multiple columns.

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

* The `groupby` function can be used to plot multiple lines on a line chart. Plotting a grouped DataFrame will automatically create axes subplots.

  ```python
  # Plot data_priceUsd for each crypto across time
  grouped_cryptos = crypto_data.groupby('cryptocurrency')['data_priceUsd'].plot(legend=True)
  grouped_cryptos
  ```

  ![plotting_groupby.png](Images/plotting_groupby.png)

- - -

### 6. Students Do: Groupby (15 mins)

This activity will entail students working with historical cryptocurrency data. Students will load in cryptocurrency data, group data by each crypto, and then perform aggregations to analyze price trends. Students will then plot the results.

**Files:**

* [crypto_circus.ipynb](Activities/06-Stu_Groupby/Unsolved/crypto_circus.ipynb)

**Instructions:**

* [README.md](Activities/06-Stu_Groupby/README.md)

- - -

### 7. Instructor Do: Review Groupby (10 mins)

**Files:**

* [crypto_circus.ipynb](Activities/06-Stu_Groupby/Solved/crypto_circus.ipynb)

Walkthrough the solution and go over the following discussion points:

* The `groupby` function can be used to group a DataFrame by a column. This allows for data to be aggregated and summarized in groups rather than all at once. DataFrames can be grouped by a single column or more than one.

* Data that has been grouped, known as a `DataFrameGroupByObject`, can be plotted. Plotting a `DataFrameGroupByObject` will create a chart with multiple lines/bars. Each line/bar will represent a respective group. In order to ensure all groups are plotted on the same chart, the data/column with the data points must be specified (i.e. `data_priceUsd`). Otherwise, multiple charts will be created for each group.

  ```python
  # Determine average price across two years
  crypto_data_avg = crypto_data.groupby('cryptocurrency')['data_priceUsd'].mean()
  crypto_data_avg
  ```

  ![plot_group.png](Images/plot_group.png)

* Grouping data is valuable when aggregations need to be performed, especially across time periods. Using `groupby` with the `avg` function calculates the average price for each crypto across the two year time period.

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

* `Min` is another common aggregate function used with grouped data. `Min` can be used to determine the lowest price in the two year time period, per crypto.

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

End the review session with the following reflective questions:

* Does the concept of grouping to aggregate data make sense?

* How was working with more than one ticker in this activity?

* What are some examples of situations where data would need to be grouped and then aggregated?  example would be calculating average grade by students.

- - -

### 8. Instructor Do: Multi Indexing (10 mins)

**Files:**

* [Multi Indexing Slides]()

* [multi_indexing.ipynb](Activities/08-Ins_Multi_Indexing/Solved/multi_indexing.ipynb)

Now that students have learned that indexes can be created by using the `groupby` key, it's important they know how to directly multi-index DataFrames. Multi-indexing is a direct way to create multiple indexes in a DataFrame. Like the `groupby` function, multi-indexing allows data to be grouped and accessed or manipulated by group.

Navigate to the Unit 4.2 slides and provide an overview of multi-indexing.

* Multi-indexing is the process of indexing a dataset by more than one value. Multi-indexing is like using two bookmarks in a book. Each bookmark is an index, and depending on which index you go to, you'll get different content.

* Multi-indexing is sometimes referred to as Hierarchical Indexing as relationships can exist between indexes. For example, a state can be one index and a city could be another. Because a city belongs to a state, these indexes would be hierarchical.

* Multiple indexes are valuable as it enables dimensional data to be grouped and retrieved. This is particularly valuable when working with Financial data and dates. While dates are great to index, dates do not always provide all of the detail needed to manipulate and analyze data. For example, when looking at stock prices and purchases over time, it is important to group data by both date and ticker. In this operation, both date and ticker can be indexes, and by specifying date and ticker, you can slice out the price of a particular stock at a specific point in time. Essentially, multi-indexing improves data storage, lookup, and manipulation/assignment.

Live code how to create and use multiple indexes, as well as how to access data using more than one index.

* Multi-indexing is commonly done when working with `Date` data. `Date` data when used as an index is considered a `DatetimeIndex`. `DatetimeIndexes` have the ability to inherently create multi-indexing. A `DatetimeIndex` can be created by passing a `Date` field to the `index_col` attribute when using `read_csv`. `parse_dates` and `infer_datetime_format` should also be included.

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

* The `loc` function can be used to slice data from a DataFrame with multiple indexes. While not all indexes are required to be passed, the top level index needs to be specified (i.e. `year`). When all indexes are passed to the `loc` function, only one record will be returned. If fewer than all indexes are provided, more than one record of data will be output. Essentially, indexes have to be accessed and used hierarchically (i.e. `year` > `month` > `day`).

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

- - -

### 9. Students Do: Multi-Indexing (15 mins)

In this activity, students will use hierarchical indexes to gain access to historical stock data. The objective of the assignment is for the students to take their indexing skills to the next level by using DataFrames with multiple indices. Students will leverage NASDAQ data to perform data segmentation for a single ticker across multiple months in a year.

**Files:**

* [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Unsolved/Core/indexing_fever.ipynb)

**Instructions:**

* [README.md](Activities/09-Stu_Multi_Indexing/README.md)

- - -

### 10. Instructor Do: Review Multi-Indexing (10 mins)

**Files:**

* [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Solved/Core/indexing_fever.ipynb)

Walkthrough the solution and go over the following discussion points:

* The `read_csv` accepts arguments that make creating indexes easy. Passing a column name to the read_csv `index_col` parameter will create a DataFrame index based off of the values in that Series. When working with Dates as indexes, it is common to set the following two `read_csv` parameters to `True`: `parse_dates` and `infer_datetime_format`. These two date parameters for read_csv will eliminate the need to cast a date Series to a `datetime` object.

  ```python
  # Read csv data with dates
  csv_path = Path("../../Resources/nasdaq_data.csv")
  nasdaq_data = pd.read_csv(csv_path, parse_dates=True, index_col="Trade DATE", infer_datetime_format=True)
  ```

* Multi-indexing is used to create multiple look up points for data, as well as to create hierarchal relationships between data elements. Multi-indexing will enable users to index data with more than one data element (i.e. `year` and `month`). Multi-indexing is valuable as it enables data to be indexed with more than one column. Using multi-indexing, especially with date Series, ensures financial data can be stored and accessed by date.

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

* Changes in time can be calculated by using the `timedelta` Pandas function. The function accepts the number of days one wants to traverse as an argument and then identifies the specific date. For example, the `timedelta` function can be used to determine what the date was 60 days from today. `Year` and `month` attributes are also available for `timedelta` objects.

  ```python
  # Calculating GOOG stock price for 30 days ago
  time_delta = date.today() - timedelta(days=30)
  goog_thirty_days_ago = nasdaq_data_grp.loc[(time_delta.year,time_delta.month)]
  print(goog_thirty_days_ago)
  ```

* In order to use the `timedelta` function, the `timedelta` function needs to be imported. In order to get access to date functions that identify the current time and current day, the `date` object will also need to be imported from `datetime`. For example, `date.today()` can be used to determine today's date.

  ```python
  from datetime import datetime, date, timedelta
  ```

- - -

### 11. BREAK (15 mins)

- - -

### 12. Instructor Do: Concatenating DataFrames (5 mins)

**Files:**

* [concat_dataframe.ipynb](Activities/12-Concating_DataFrames/Solved/concat_dataframe.ipynb)

Indexing, grouping, and sorting datasets are all steps taken to prepare data for analysis. Another is combining, also known as concatenating, datasets. This is beneficial when more than one dataset needs to be combined. For example, multiple months of financial records or investment data from different markets can be consolidated into one dataset in order to streamline and centralize data analysis.

Navigate to the 4.2 slides, and provide a brief overview of concatenation:

* Concatenation is the process of appending data from one object with another.

* Concatenation creates a new object that represents data from all concatenated objects.

* There are multiple ways to concatenate objects, including by column and row.

* DataFrames can be joined together, or `concatenated`, using the Pandas `concat` function. This function enables users to join and combine more than one DataFrame. The function accepts the following arguments: a list of DataFrames to be joined, the `axis` to join on (by column or row), and the `join` operation (inner vs outer).

Live code the following examples:

* DataFrames can be joined by either `column` or `row`. The `axis` argument can be configured to specify which to use. If a new dataset needs to be created where multiple columns from different DataFrames need to be reflected, the DataFrames should be joined on `column`. This will create a new, composite DataFrame that incorporates the columns from all DataFrames. If rows from one DataFrame simply needs to be combined or added to another DataFrame, the DataFrames should be joined on `row`. Joining on the `row` axis would require all DataFrames being joined to have the same columns.

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

The `concat` function creates a new DataFrame that includes data from all of the datasets that were joined. The amount of data returned will depend on the type of `join` performed when concatenating. Indicate to students that additional information can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#set-logic-on-the-other-axes).

* The `join="inner"` argument will create an intersection of the data.

* The `join="outer"` argument will union the data.

- - -

### 13. Students Do: Concat DataFrames (15 mins)

**Instructions:**

* [README.md](Activities/13-Stu_Concat_DataFrames/README.md)

**Files:**

* [joining_forces.ipynb](Activities/13-Stu_Concat_DataFrames/Unsolved/joining_forces.ipynb)

- - -

### 14. Instructor Do: Review Concat DataFrames (5 mins)

**Files:**

* [joining_forces.ipynb](Activities/13-Stu_Concat_DataFrames/Solved/joining_forces.ipynb)

Conduct a formal review Q&A with the following questions:

* If I wanted to consolidate two DataFrames with the same columns into one DataFrame, which concat axis would I use?

    > "By rows. Concatenating by rows will combine the two DataFrames so that all rows are in one DataFrame."

* Let's say I wanted to take an intersection of two DataFrames that I have combined. Would I use the inner join operation or outer join operation?

    > "Inner join. Inner join will return a DataFrame with only matching rows."

* Which join will produce more rows? An inner join our outer join?

    > "Outer join. Inner joins represent only a section of all of the data."

Walkthrough the solution and go over the following discussion points:

* The `concat` function can be used to combine or link more than one DataFrame.

* DataFrames can be concatenated either by `rows` or `columns`. Concatenating by `row` will create a DataFrame that has the total number of rows. Concatenating by `columns` produces a DataFrame that has the columns from all DataFrames concatenated.

  ![concat_axis.png](Images/concat_axis.png)

* DataFrames should be concatenated by `rows` when the columns of the DataFrame are the same and should remain the same. The idea is that the rows are appended.

  ![stu_concat_rows.png](Images/stu_concat_rows.png)

* DataFrames should be concatenated by `columns` when columns from one DataFrame need to be combined with columns from another. The idea is that the columns are appended.

  ![stu_concat_cols.png](Images/stu_concat_cols.png)

- - -

### 15. Instructor Do: Standard Deviation and Risk (10 mins)

The Standard Deviation and Risk module focuses on students learning what `standard deviation` is and how it can be used to determine the risk associated with an investment. The instructor will demo how to calculate `standard deviation` using Pandas. Students will learn standard deviation so they can then calculate `sharpe ratios` in the next activity.

**Files:**

* [std_dev_risk.ipynb](Activities/15-Ins_Std_Dev_Risk/Solved/std_dev_risk.ipynb)

Everything completed in class up until this point has been to prepare students for portfolio analysis. With daily returns calculated, and data from multiple portfolios combined into one dataset, students are able to complete a holistic analysis of the data. For this section of the lesson, students will leverage data preparation skills to analyze portfolio performance, calculate risk, and identify risky investments.

Navigate to the 4.2 slides, and highlight the following:

* A key aspect of analyzing portfolio and stock data is determining risk. Pandas provides a series of functions that can be used to calculate risk. One component of risk is calculating the `mean` performance or price of a stock. The second is calculating the `standard deviation`.

* `Mean` can be used to determine the average value of a portfolio/stock overtime. This can serve as a baseline for measuring risk and value. A portfolio/stock doing better than average is more valuable. Investing in a portfolio or buying a stock doing below average is risky business.

* A common technique for measuring how far away an asset is from the `mean` is to calculate the `standard deviation`. `Standard deviation` identifies exactly how far away from the average price the value is. A low number indicates that the value is not far form the average. A high `standard deviation` means the value is an outlier.

Live code how to use Pandas to calculate `standard deviation` to evaluate risk:

* `Standard deviation` should be calculated using daily returns data. Calculating `standard deviation` against daily returns will help identify risk based off of return value rather than price volatility.

  ![std_dev.png](Images/std_dev.png)

* The `std` Pandas function can be used to determine the risk associated with a portfolio/stock. Behind the scenes, the `std` function calculates the mean/average, and then it evaluates how far away from the average the input is. The function returns a new DataFrame.

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

* It is common to need `standard deviation` at the yearly level. Calculating annualized standard deviation can be done by multiplying the the square root (`sqrt`) of the number of trading days in a year (`252`) with the standard deviation.

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

* A key way to assess risk is to use the `plot.hist` function to create a chart of standard deviation trends. This will visually demonstrate the mean value, as well as the number and severity of any deviations for each element being plotted (i.e. each portfolio).

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

* Another way to visualize `standard deviation` is with a `box plot`. `Box plots` display the total spread of the data, and they can be created using the `plot.box` Pandas function. Box plots have what are known as `whiskers`. `Whiskers` represent the range/spread of the data. Data elements that extend beyond the `whiskers` are considered outliers.

  ```python
  # Plot box plot
  portfolio_std.plot.box()
  ```

  ![std_dev_box.png](Images/std_dev_box.png)

* The take away from these charts, which should be emphasized to students, is that the greater the spread, the greater the risk. The greater the risk, the greater the potential for earnings and lost.

- - -

### 16. Instructor Do: Sharpe Ratios (5 mins)

In this module, students will be introduced to sharpe ratios and why risk-reward ratios are important in finance.

**Files:**

* [sharpe_ratios.py](Activities/16-Ins_Sharpe_Ratios/Solved/sharpe_ratios.py)

Now that students have been taught how to assess and identify risk and investment performance, they are now prepared to learn how to adjust trade patterns to adjust for risk-reward.

Open the 4.2 slides, and provide an overview of what `sharpe ratios` are and how they are calculated.

* Sharpe ratios are used to help compare rate of return for an investment with its risk. Sharpe ratios shed light on the potential of profits even with risk involved.

* Sharpe ratios measure the excess return for each deviation. This will identify, in the wake of risk, how much profit is left to be gained.

* Sharpe ratios are calculated by subtracting the `return of portfolio` from the investment's `risk-free rate`. The difference is than divided by the `standard deviation`.

  Sharpe Ratios = <img src="https://latex.codecogs.com/gif.latex?\frac{R_{p}-R_{f}}{\sigma_{p}}$" title="\frac{R_{p}-R_{f}}{\sigma_{p}}$" />

Open the solution, and live code how to calculate and plot sharpe ratios:

* Sharpe ratios are commonly used to indicate whether or not an investment is a good decision. While standard deviation illustrates how far an investment has deviated from its average, sharpe ratios uses standard deviation to illustrate the relationship between standard deviation and risk-reward. Sharpe ratios enables investors to judge whether or not an investment is a good decision. Sharpe ratios adjust for risk, making them a valuable indicator of asset performance.

  ```python
  # Calculate Sharpe Ratio
  sharpe_ratios = (all_portfolios_returns.mean() * 252) / (all_portfolios_returns.std() * np.sqrt(252))
  sharpe_ratios
  ```

  ![sharpe_ratios.png](Images/sharpe_ratios.png)

* The ratio of return-to-risk can be used to determine which stocks and/or portfolios have out-done the others. The higher the `sharpe ratio`, the better the investment. The `plot` function can be used to visually compare `sharpe ratios`.

  ```python
  # Plot sharpe ratios
  sharpe_ratios.plot(kind="bar", title="Sharpe Ratios")
  ```

  ![sharpe_ratios_plot.png](Images/sharpe_ratios_plot.png)

- - -

### 17. Students Do: Risky Business (20 mins)

It's time to wrap it all together. In this activity, students will prep data and use standard deviation and sharpe ratios to analyze cryptocurrency portfolio performance for Harold and themselves. The goal is to calculate who has the riskier portfolio: Harold or themselves. Students will also identify which individual cryptos have had the greatest return.

Encourage students to work in pairs for this assignment.

**Files:**

* [risky_business.ipynb](Activities/17-Stu_Risky_Business/Unsolved/Core/risky_business.ipynb)

**Instructions:**

* [README.md](Activities/17-Stu_Risky_Business/README.md)

- - -

### 18. Instructor Do: Review Risky Business (10 mins)

**Files:**

* [risky_business.ipynb](Activities/17-Stu_Risky_Business/Solved/Core/risky_business.ipynb)

Walk through the solution and highlight the following:

* The `concat` function can be used to combine portfolio returns. This enables analysis (i.e. standard deviation) to be performed on an entire portfolio rather than an individual stock. This allows data from investments/portfolio `A` to be compared with investments/portfolio `B`. Harold's portfolio returns are combined with student returns in order to later calculate `standard deviation` and `sharpe ratio` for across the board.

  ```python
  # Concat returns DataFrames
  all_returns = pd.concat([harold_returns,my_returns], axis='columns', join='inner')
  all_returns.head()
  ```

  ![stu_concat_compare.png](Images/stu_concat_compare.png)

* `Standard deviation` is required to calculate `sharpe ratios`. `Standard Deviation` calculates the average value and compares the distribution of values to that average. The `std` function can be used to compute standard deviation. The output from the function is a Series that indicates how far the value is from the mean, in the same units as the base data. The greater the value/deviation, the greater the risk and volatility.

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

* `Sharpe ratios` are used to examine investment performance based off of the risk to reward ratio. `Sharpe ratio` calculates the risk associated with a return and then divides that by the standard deviation of a return. The higher the `sharpe ratio`, the greater the reward associated with the risk. A high `sharpe ratio` indicates a smart investment. Calculating the `sharpe ratio` for Harold's and the students' portfolios reveals who's portfolio has the greatest reward associated with the risk.

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

* `Sharpe ratios` can be visually represented with a bar chart. This allows users to easily see which investments have high and low sharpe ratios.

  ```python
  # Plot
  sharpe_ratios.plot.bar(title='Sharpe Ratios')
  ```

  ![sharpe_plot.png](Images/sharpe_plot.png)

Ask the students the following questions:

* How many smart investments did Harold make compared to risky investments? How many did you make?

  ```
  Out of his 10 investments, Harold only made 4 good investments. Out of the students' 6 investments, 3 of them were smart investments.
  ```

* Which cryptos are the smartest investment?

  ```
  DOGE, TRON, and XML are the smartest crypto investments.
  ```

- - -

### 19. Decompress (5 mins)

Another battle won, another level completed. Students have been excelling at a quantum speed, and it's important they understand this. End the class with the following positive remarks:

* Acknowledge that students have come far. Earlier in the week they were just learning how to use Pandas. Now they're using Pandas to analyze investment risk and predict smart investments.

* Emphasize that these skills are extremely applicable to the real world. Being able to programmatically combine and group data in order to perform financial analysis and calculate investment risk will go along way professionally and personally.

Engage the students by asking how they plan to incorporate skills from today's lesson into their resumes and/or work lives. Two skills that should be highlighted are:

* Data Engineering and Analysis

  * Communicate that the activities students completed involving reading, cleaning, combining, grouping, aggregating, and analyzing multiple datasets is actual data engineering and analysis. Data Engineers and Data Analysts are completing these same tasks day to day.

* Financial Reporting and Visualization

  * State that with the proper narrative and flow, the final activity could be used as a financial report. Students have calculated daily returns for investments and identified which investments are expected to produce the most reward and risk. They essentially have a report that presents findings on two portfolios and identifies which is a smarter investment. Underscore that this is a real world use case.

### End Class
