## 3.3 Lesson Plan: Risk and Returns Over Time

### Overview

In the last class, students got their hands dirty using Pandas to read, clean, and analyze financial data over time. Today's lesson continues this trajectory, as students learn how to use Pandas to conduct time series analysis to calculate risks and returns over time. This skill will allow students to manage all the financial data they encounter in FinTech. Students will also learn how to group data and apply multi-indexing to a DataFrame to improve the analysis and visualization of stock exchange data.

### Class Objectives

By the end of class, students will be able to:

* Group data in a DataFrame to perform calculations on the grouped data.

* Manipulate datetime data in different formats: single variables, DataFrame columns, and series.

* Identify the calculations that can be done with datetime data.

* Declare and use a DateTimeIndex.

* Calculate mean, median, and standard deviation using Pandas.

* Apply standard deviation to risk analysis use cases.

* Determine risk by identifying how stocks deviate from the mean.

* Describe Sharpe ratios and calculate them using Pandas DataFrames.

### Instructor Notes

* Prepare for the lesson by running the code examples and reviewing the lectures before class. Today's lesson will be a quantum leap for students, as they move beyond the basics of Pandas to more advanced concepts that can be applied to risk analysis use cases. You must clearly articulate what you are doing in each live demo and why, from a financial point of view. This is especially true for the standard deviation and Sharpe ratio activities.

* Throughout the lesson, be sure to underscore how Pandas lessens the burden of analysis by providing financial functions such as `MultiIndex` and `groupby()`. Students will learn the practical applications of these concepts by analyzing cryptocurrencies and stock exchange data. For example, tell students they can use the `groupby` function to automatically consolidate data to calculate an average, rather than organizing two years’ worth of daily returns data for each cryptocurrency in an Excel file. Similarly, instead of having to create a `groupby` function themselves, students get to use the Pandas function for free.

* The sections on grouping and multi-indexing contain abstract concepts that can be difficult to grasp without a visual representation. Therefore, be sure to show the slides before walking through the demos so students can absorb the information.

* Be mindful of the class pacing; it should feel urgent, not rushed. Check for understanding regularly, and circulate the classroom with the TAs during activities to offer your assistance. Stick to the Time Tracker as closely as possible. Encourage any struggling students to attend office hours.

* Encourage students to work in pairs or groups on the in-class activities, to help facilitate discussions as well as troubleshooting. Collaborative exercises such as student-led activity reviews and discussions have been built into this lesson.

* Have your TAs keep track of time with the Time Tracker.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [3.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=10e7097d-5905-4c40-b413-aaa600dbb8ee) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1dJd77Q_QXtLv60K0w7DqLNW_FToh0y9S_nD4ZiLLdic/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Intro to Sorting (10 min)

In this section, you will provide an overview of today's lesson and then introduce students to sorting.

**Files:**

* [sort_dataframe.ipynb](Activities/01-Ins_Sorting/Solved/sort_dataframe.ipynb)

Welcome students to the second day of Pandas. Open the lesson slides to explain the focus of today's class and highlight the following:

* You will leverage your data cleaning, indexing, and visualization skills from Day 1 to sort, group, multi-index, and concatenate multiple financial datasets for daily returns and investment risk analysis.

* By the end of the lesson, you will have used Pandas to compare two portfolios and identify which is the smarter investment.

Move to the `Sorting` section of the slideshow, and highlight the following:

* When you work with financial data, it is common to sort values in ascending or descending order. Data is not always organized in the best way for analysis. Sometimes, data needs to be cleaned and sorted.

* Pandas provides a function for this called `sort_values` that will sort a DataFrame by a column.

* Using `sort_values`, data can be sorted in ascending or descending order. This is especially important when dealing with dates. What makes more sense–sorting dates, or randomly listing them?

* This function can be used to find the highest or lowest daily returns from stock data.

Open the file `sort_dataframe.ipynb` and highlight the following:

* A DataFrame can be created from lists or dictionaries. In this example, a DataFrame of painting prices is supplied as a list of Python dictionaries, which we convert to a DataFrame.

  ![creating-dataframes.png](Images/creating-dataframes.png)

* The DataFrame can be sorted by any column using `sort_values`. In this example, the DataFrame is sorted in ascending order (the default) by price.

  ![sort-ascending.png](Images/sort-ascending.png)

* The DataFrame can also be sorted in descending order using the `ascending=False` parameter.

  ![sort-descending.png](Images/sort-descending.png)

* The DataFrame can also be sorted by the index.

  ![sort index](Images/sort_index.png)

* We can also set a new index and *then* sort.  In the following example, we set the `Price` column as the index and then sort based on descending price values.

  ![set-index-sort.png](Images/set-index-sort.png)

Close this activity by highlighting the following about sorting, and the skills that students will learn in today's class:

* Today's activities will provide the foundation you need to begin grouping and aggregating data.

* It's common to group and aggregate financial data by different metrics, including dates, tickers, and categories.

* Example use cases include determining the average close price for a list of stock tickers and aggregating data (summing, adding, averaging) over time (e.g., 3-month intervals).

Ask if there are any questions before moving on.

---

### 2. Student Do: Out of Sorts (10 min)

In this activity, students will analyze data for a single ticker to calculate daily returns for the year 2019. The data will then be sorted in descending order to identify the top five performing days for returns.

**Files:**

* [out_of_sorts.ipynb](Activities/02-Stu_Sorting/Unsolved/out_of_sorts.ipynb)

* [bb_stock_data.csv](Activities/02-Stu_Sorting/Resources/bb_stock_data.csv)

**Instructions:**

* [README.md](Activities/02-Stu_Sorting/README.md)

As students work on the activity, circulate the room with the TAs to offer assistance to students who need it.

If a student finishes the activity early, ask if they are willing to help present the solution by live coding how to sort a DataFrame by more than one column. This live-coding exercise will be completed in the activity review (the next part of the lesson).

---

### 3. Instructor Do: Review Out of Sorts (10 min)

Review the sorting activity by having a student participate in a live-coding exercise in front of the class. This exercise should be completed only if the student feels comfortable and previously agreed to participate.

Skip to the dry walkthrough of the activity solution if you do not have a student who can live code this activity.

**Files:**

* [out_of_sorts.ipynb](Activities/02-Stu_Sorting/Solved/out_of_sorts.ipynb)

* [bb_stock_data.csv](Activities/02-Stu_Sorting/Resources/bb_stock_data.csv)

**Student Live Codes the Solution:**

Ask the student to live code the solution. If the student loses momentum or seems stuck while live coding, ask guided questions such as:

* How does one sort by more than one column?

    **Answer:** List the columns to sort by in a comma separated list.

* Can you use a list to tell Pandas to sort some columns by ascending values, and others by descending values?

    **Answer:** Yes. The `ascending` parameter can be used to sort columns by ascending values. Default value is `True`. `False` will sort in descending order. The `ascending` parameter accepts a list of Boolean responses when data is sorted by more than one column.

**Dry Walkthrough of the Solution:**

Do this dry walkthrough in place of the live-coding exercise if you do not have a student volunteer.

Open the solution and explain the following:

* Once the data is loaded into the DataFrame and cleaned, the daily returns of the Blackberry stock in 2019 is calculated using the `pct_change` function.

  ![BB daily returns](Images/bb_daily_returns.png)

* The `sort_values` function has an attribute called `ascending` that can be configured as either `True` or `False`—setting ascending to `True` sorts data in ascending order. `False` sorts data in descending order.

* In this activity, we set `ascending=False` and sort the DataFrame by the `Close` column to get the records with the top daily returns first.

  ![stu_sort_descending.png](Images/stu_sort_descending.png)

* Next, we fetch the top five daily returns and create a new DataFrame.

  ![BB top five daily returns](Images/bb_top_five_daily_returns.png)

* Finally, we plot the data from the top five daily returns.

  ![Plotting BB top five daily returns](Images/bb_top_five_daily_returns_plot.png)

Ask if there are any questions before moving on.

---

### 4. Instructor Do: Grouping (10 min)

This section focuses on grouping and aggregating data. Grouping data is particularly valuable when dealing with data for multiple stocks. You will give an overview of grouping and then perform a live demo of how to use the `groupby` function in Pandas. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

**Files:**

* [groupby.ipynb](Activities/03-Ins_Groupby/Solved/groupby.ipynb)

* [crypto_data.csv](Activities/03-Ins_Groupby/Resources/crypto_data.csv)

Open the lesson slides, move to the "Grouping" section, and introduce the `groupby` function by explaining the following:

* A common technique in data analysis is to summarize data by grouping similar values.

  * One example is grouping sales data by country or category.

  * We also may want to group data by the stock ticker.

  * Once you group data, you can use an aggregated function (or aggregations) to operate on the grouped data.

  * Example aggregations that can be done on groups are adding, summing, determining min and max, etc.

  ![Visual data aggregation](Images/visual_data_grouping.png)

* Pandas offers the `groupby` function to group the data in a DataFrame.

  * The `groupby` function is just as standard as the `sort_values` function.

  * Both of these functions are used to wrangle data into a state that is usable for analysis.

  * The `groupby` function splits data into groups. Once groups are created, a function or operation can be executed against each group (e.g., addition).

  * Data must be grouped using `groupby` before the values in each group can be aggregated. This ensures data is aggregated at the group level, rather than at the column level.

  ![Visual data grouping](Images/visual_grouping.png)

Start the live demonstration of how to use the `groupby` function. Open the unsolved version of the Jupyter notebook and live code while explaining the following:

* To group data, use the `groupby` function against a non-unique column. The `groupby` function accepts a series name as an argument. Users can also specify a return column with brackets, `[]`.

  ![group_count.png](Images/group_count.png)

* The `groupby` function requires a function or aggregation.

  * Whenever a function is not chained to a `groupby` function, the output will be a `DataFrameGroupBy` object rather than an actual DataFrame.

  * `DataFrameGroupBy` objects must be aggregated before they can be used.

  ```python
  # Group by cryptocurrency
  crypto_data_grp = crypto_data.groupby("cryptocurrency")
  crypto_data_grp
  ```

  ```text
  <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001CFF748A518>
  ```

* Examples of aggregate functions that can be applied against `DataFrameGroupBy` objects include `count`, `sum`, and `mean`, just to name a few. These functions will proceed with a `groupby` function.

  ![group_by_aggregate.png](Images/group_by_aggregate.png)

* DataFrames can be grouped by more than one column. This will group values across each specified column and summarize the data into one record. This approach can be used as a way to identify if there are any duplicates within the data.

* In this demo, we group the data by the `cryptocurrency` and `data_price` columns to create a view where we can count how many times a price is repeated by cryptocurrency.

  ![multi_group_count.png](Images/multi_group_count.png)

* We may want to round the prices; we can do that using the `round` function of the DataFrame, then we can group the data again.

  ![multi_group_round_count.png](Images/multi_group_round_count.png)

* Once the data is grouped, each group can be plotted for comparison. This will plot multiple lines on a single plot. Each line is considered a subplot.

  ![plotting_groupby.png](Images/plotting_groupby.png)

Slack out to students the [Group By Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html) as a further reference and ask if there are any questions before moving on.

---

### 5. Student Do: Group Dynamics (15 min)

In this activity, students will work with historical cryptocurrency data. They will load in cryptocurrency data, group data by each crypto, perform aggregations to analyze price trends, and then plot the results. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

**Files:**

* [group_dynamics.ipynb](Activities/04-Stu_Groupby/Unsolved/group_dynamics.ipynb)

* [crypto_data.csv](Activities/04-Stu_Groupby/Resources/crypto_data.csv)

**Instructions:**

* [README.md](Activities/04-Stu_Groupby/README.md)

---

### 6. Instructor Do: Review Group Dynamics (10 min)

In this section, review the Group Dynamics activity by completing a dry walkthrough of the solution. End by asking a series of review questions to test students' understanding.

**Files:**

* [group_dynamics.ipynb](Activities/04-Stu_Groupby/Solved/group_dynamics.ipynb)

* [crypto_data.csv](Activities/04-Stu_Groupby/Resources/crypto_data.csv)

Open the solution file and complete a dry walkthrough of the student activity solution, covering the following points:

* The `groupby` function can be used to group a DataFrame by a column. This allows data to be aggregated and summarized in groups rather than all at once. A single column or multiple columns can group DataFrames.

* Data that has been grouped, known as a `DataFrameGroupByObject`, can be plotted.

  * Plotting a `DataFrameGroupByObject` will create a chart with multiple lines/bars. Each line/bar represents a group.

  * To ensure all groups are plotted on the same chart, the data (the column with the data points) must be specified (i.e., `data_price`). Otherwise, multiple charts will be created for each group.

  ![plot_group.png](Images/plot_group.png)

* Grouping data is valuable when aggregations need to be performed, especially across periods. Using `groupby` with the `avg` function calculates the average price for each crypto over the two years.

  ![group_average.png](Images/group_average.png)

* The `max` price for a cryptocurrency can also be calculated for a period using the `groupby` function. This will return the highest price for the period, per crypto.

  ```python
  # Determine max price across two years
  crypto_data_max = crypto_data.groupby("cryptocurrency")["data_price"].max()
  crypto_data_max
  ```

  ```text
  cryptocurrency
  bitcoin         19339.922660
  bitcoin-cash     3476.844119
  ethereum         1346.037491
  litecoin          352.713468
  ripple              2.999459
  Name: data_price, dtype: float64
  ```

* `Min` is another standard aggregate function used with grouped data. `Min` can be used to determine the lowest price in the two years, per crypto.

  ```python
  # Determine min price across two years
  crypto_data_min = crypto_data.groupby("cryptocurrency")["data_price"].min()
  crypto_data_min
  ```

  ```text
  cryptocurrency
  bitcoin         1714.964198
  bitcoin-cash      78.977344
  ethereum          84.374014
  litecoin          22.550468
  ripple             0.154144
  Name: data_price, dtype: float64
  ```

If time remains, end the review by calling on students to answer the following reflective questions:

* Does the concept of grouping to aggregate data make sense?

    **Sample Answer:** Yes. When aggregating data without groups, all of the data is aggregated. Grouping and then aggregating allows calculations to be executed against groups (e.g., January's stock data would be grouped and computed separately from February's).

* How did working with more than one ticker help you in this activity?

    **Sample Answer:** Working with more than one ticker accelerates processing. Instead of analyzing one ticker at a time, data for all stocks can be put into one file, analyzed as individual groups, and then combined to create a single `DataFrame` object.

* What are some examples of situations where data would need to be grouped and then aggregated?

  **Sample Answers:**

  * Calculating daily returns by quarter.

  * Calculating final grades for each student per class.

  * Calculating the number of horror movies released every decade between 1970 and 1990.

Answer any questions before moving on.

---

### 7. Instructor Do: Multi-Indexing (10 min)

Now that students have learned that indexes can be created by using the `groupby` key, they must know how to directly multi-index DataFrames.

Multi-indexing is a direct way to create multiple indexes in a DataFrame. Like the `groupby` function, multi-indexing allows data to be grouped and accessed or manipulated by a group.

**Files:**

* [multi_indexing.ipynb](Activities/05-Ins_Multi_Indexing/Solved/multi_indexing.ipynb)

* [metro_inc_stock_data.csv](Activities/05-Ins_Multi_Indexing/Resources/metro_inc_stock_data.csv)

Open the lesson slides, move to the "Multi-Indexing" section, and provide an overview:

* **Multi-indexing** is the process of indexing a dataset by more than one value. Multi-indexing is like using two bookmarks in a book. Each bookmark is an index, and depending on which index you go to, you'll get different content.

* Multi-indexing is sometimes referred to as hierarchical indexing, as relationships can exist between indexes. For example, a province can be one index and a city can be another. Because a city belongs to a province, these indexes would be hierarchical.

* Multiple indexes are valuable because they enable dimensional data to be grouped and retrieved.

  * This is particularly helpful when working with financial data and dates. While dates are great to index, dates do not always provide all of the detail needed to manipulate and analyze data.

  * For example, when looking at stock prices and purchases over time, it is important to group data by both date and ticker. In this operation, both date and ticker can be indexes, and by specifying date and ticker, you can slice out the price of a particular stock at a specific point in time.

* Essentially, multi-indexing improves data storage, lookup, and manipulation/assignment.

Now, open the unsolved Jupyter notebook and live code on how to create and use multiple indexes, as well as how to access data using more than one index. Cover the following points:

* When working with indexes, it's a common practice to clean data before setting indexes. For example, a Series being used as an index should not have any `NaN` values. These can be handled by first executing `dropna` against a DataFrame. The `set_index` function can then be used to set the index. (*NOTE:* The data set for this demo has already be cleaned.)

* Multi-indexing is commonly done when working with `Date` data.

* When used as an index, `Date` data is considered a `DatetimeIndex`. `DatetimeIndexes` have the inherent ability to create multi-indexes.

* A `DatetimeIndex` can be created by passing a `Date` field to the `index_col` attribute when using `read_csv`. `parse_dates` and `infer_datetime_format` should also be included.

  ```python
  # Read in data
  csv_path = Path("../Resources/metro_inc_stock_data.csv")
  ticker_data = pd.read_csv(csv_path, parse_dates=True, index_col="Date", infer_datetime_format=True)
  ```

* `DatetimeIndexes` can be split into year, month, and day segments. The `DatetimeIndex` object includes the attributes `index.year`, `index.month`, and `index.day` for this. Passing these to a `groupby` statement will create multiple indexes based on each attribute.

* The `first` function is used to display the first value for each group within a GroupBy object. In this case, every group down to the `year`, `month`, and `day` level is unique, and therefore grabs the first and only value of every group.

  ![multi_index_date.png](Images/multi_index_date.png)

* Multi-indexed data can be selected by using the `first` and `last` functions. `First` selects the first multi-index group, and `last` selects the last group.

  ![multi_index_first.png](Images/multi_index_first.png)

  ![multi-index-last](Images/multi-index-last.png)

* Because multi-indexing involves grouping data, aggregation can be applied against the data. A common example is the `mean` function for calculating the average. This is an alternative to using the `first` and `last` functions. Because aggregate functions are being used, outputs represent summarized/aggregated records.

  ![multi_index_agg.png](Images/multi_index_agg.png)

* The `loc` function can be used to slice data from a DataFrame with multiple indexes.

  * While not all indexes are required to be passed, the top-level index needs to be specified (e.g., `year`).

  * When all indexes are passed to the `loc` function, only one record will be returned. If fewer than all indexes are provided, more than one record of data will be output.

  * Essentially, indexes must be accessed and used hierarchically (e.g., `year` > `month` > `day`).

  ![multi_index_slice.png](Images/multi_index_slice.png)

Ask if there are any questions before moving on.

---

### 8. Student Do: Indexing Fever (15 min)

In this activity, students will use hierarchical indexes to gain access to historical stock data. The goal of this activity is for students to take their indexing skills to the next level by using DataFrames with multiple indexes.

**Files:**

* [indexing_fever.ipynb](Activities/06-Stu_Multi_Indexing/Unsolved/indexing_fever.ipynb)

* [bombardier_stock_data.csv](Activities/06-Stu_Multi_Indexing/Resources/bombardier_stock_data.csv)

**Instructions:**

* [README.md](Activities/06-Stu_Multi_Indexing/README.md)

---

### 9. Instructor Do: Review Indexing Fever (5 min)

In this section, you will perform a dry walkthrough of the solution for the Indexing Fever activity.

**Files:**

* [indexing_fever.ipynb](Activities/06-Stu_Multi_Indexing/Solved/indexing_fever.ipynb)

* [bombardier_stock_data.csv](Activities/06-Stu_Multi_Indexing/Resources/bombardier_stock_data.csv)

Open the solved version to review the solution, and cover the following points:

* `read_csv` accepts arguments that make creating indexes easy. Passing a column name to the `read_csv` `index_col` parameter will create a DataFrame index based on the values in that series.

* When working with dates as indexes, it's common to set the following two `read_csv` parameters to `True`: `parse_dates` and `infer_datetime_format`. These two date parameters eliminate the need to cast a date series to a `datetime` object.

  ```python
  # Read csv data
  csv_path = Path("../Resources/bombardier_stock_data.csv")

  bbd_df = pd.read_csv(
      csv_path, parse_dates=True, index_col="Date", infer_datetime_format=True
  )
  ```

* Multi-indexing is used to create multiple lookup points for data, as well as hierarchal relationships between data elements.

* Multi-indexing enables users to index data with more than one data element (e.g., `year` and `month`).

* Multi-indexing is valuable because it enables data to be indexed with more than one column. Using multi-indexing, especially with date series, ensures that financial data can be stored and accessed by date.

  ![Multi_Indexing_Relationship.png](Images/Multi_Indexing_Relationship.png)

* Grouping data creates indexes naturally. Grouping data by a `DatetimeIndex` creates two indexes: one for the year and one for the month. Each of these can be accessed by using the `year` and `month` attributes.

* Grouped data can be selected by using the `first` and `last` functions. These will return the first group of grouped items and the last group, respectively.

* When using a `DateTimeIndex`, data can be grouped by date. Components of date (i.e., year or month) can be accessed using `index.year` and `index.month`.

  ![Multi_Indexing_Groupby.png](Images/Multi_Indexing_Groupby.png)

* Once items have been grouped and indexed, data can be retrieved using those indexes and the `loc` function.

* In this activity, we select data from a `DateTimeIndex` by using the `loc` function and passing as parameters the year (`2019`) and the month (`5`) as index values.

  ![Multi_Indexing_Lookup.png](Images/Multi_Indexing_Lookup.png)

* For the challenge section, to calculate the mean close price for `BBD.B` for all of `2019`, we fetch all the data from `2019` using the `loc` function and use the `mean` to calculate the mean close price.

  ![multi-index-challenge](Images/multi-index-challenge.png)

Answer any questions before moving on.

---

### 10. BREAK (40 min)

---

### 11. Instructor Do: Concatenating DataFrames (10 min)

In this section, you will provide an overview of concatenation and then live code how to concatenate DataFrames. Data for this activity was retrieved from [Kaggle](http://kaggle.com).

**Files:**

* [concat_dataframe.ipynb](Activities/07-Ins_Concat_DataFrame/Unsolved/concat_dataframes.ipynb)

* [customer_info.csv](Activities/07-Ins_Concat_DataFrame/Resources/customer_info.csv)

* [rance_products.csv](Activities/07-Ins_Concat_DataFrame/Resources/france_products.csv)

* [netherlands_products.csv](Activities/07-Ins_Concat_DataFrame/Resources/netherlands_products.csv)

* [products.csv](Activities/07-Ins_Concat_DataFrame/Resources/products.csv)

* [uk_products.csv](Activities/07-Ins_Concat_DataFrame/Resources/uk_products.csv)

Open the lesson slides, move to the "Concatenation" section, and explain the following:

* Indexing, grouping, and sorting datasets are all part of data analysis preparation. Another step in this process is combining, or concatenating, datasets. This is beneficial when more than one dataset needs to be combined.

* For example, many months of financial records or investment data from different markets can be consolidated into one dataset to streamline and centralize data analysis.

Open the slideshow and provide a brief overview of concatenation:

* **Concatenation** is the process of appending data from one object with another.

* Concatenation creates a new object that represents data from all concatenated objects.

* DataFrames can be concatenated so that the records from two or more DataFrames are combined.

* Concatenation can be done by column, so that the columns from one DataFrame are placed adjacent to columns from another DataFrame.

* There are multiple ways to concatenate objects, including by column and row.

* DataFrames can be joined together, or concatenated, using the Pandas `concat` function.

* The `concat` function accepts the following arguments:

  * a list of DataFrames to be joined

  * the `axis` to join on (by column or row)

  * the `join` operation (inner vs. outer)

* The `join="inner"` argument will create an intersection of the data.

* The `join="outer"` argument will union the data.

Open the unsolved version of the Jupyter notebook, live code the demo, and highlight the following:

* A key consideration to keep in mind when concatenating DataFrames is that data is joined by index. Pandas `concat` function will by default join rows or columns by index. Before concatenating DataFrames, make sure the same column is used as the index for all DataFrames.

  ```python
  # Set data files' paths
  france_data_path = Path("../Resources/france_products.csv")
  uk_data_path = Path("../Resources/uk_products.csv")
  netherlands_data_path = Path("../Resources/netherlands_products.csv")
  customer_data_path = Path("../Resources/customer_info.csv")
  products_data_path = Path("../Resources/products.csv")

  # Read in data and index by CustomerID
  france_data = pd.read_csv(france_data_path, index_col="CustomerID")
  uk_data = pd.read_csv(uk_data_path, index_col="CustomerID")
  netherlands_data = pd.read_csv(netherlands_data_path, index_col="CustomerID")
  customer_data = pd.read_csv(customer_data_path, index_col="CustomerID")
  products_data = pd.read_csv(products_data_path, index_col="CustomerID")
  ```

* DataFrames can be joined by either `column` or `row`. The `axis` argument can be configured to specify which one to use.

* If rows from one DataFrame simply need to be combined or added to another DataFrame, the DataFrames should be joined on `row`. Joining on the `row` axis requires the DataFrames being joined to have the same columns.

  ![concat_rows.png](Images/concat_rows.png)

* If you need to create a dataset that reflects multiple columns from different DataFrames, the DataFrames should be joined on `column`. This will create a DataFrame that incorporates the columns from all DataFrames.

  ![concat_columns.png](Images/concat_columns.png)

* The `concat` function creates a new DataFrame that includes data from all datasets that were joined. The amount of data returned will depend on the type of `join` performed when concatenating.

Slack out to students the [Pandas documentation about merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) for further reading and more examples of DataFrames concatenation.

Answer any questions before moving on.

---

### 12. Student Do: Mastering Concatenation (15 min)

In this activity, students will get hands-on experience with combining multiple DataFrames using the `concat` function. The goal of the activity is for students to take dues and membership data from two community organizations and combine the data into a single DataFrame.

**Files:**

* [mastering_concatenation.ipynb](Activities/08-Stu_Concat_Dataframes/Unsolved/mastering_concatenation.ipynb)

* [fin_leaders_america.csv](Activities/08-Stu_Concat_Dataframes/Resources/fin_leaders_america.csv)

* [fin_leaders_members.csv](Activities/08-Stu_Concat_Dataframes/Resources/fin_leaders_members.csv)

* [invstrs_leadership_members.csv](Activities/08-Stu_Concat_Dataframes/Resources/invstrs_leadership_members.csv)

* [invstrs_leadership.csv](Activities/08-Stu_Concat_Dataframes/Resources/invstrs_leadership.csv)

**Instructions:**

* [README.md](Activities/08-Stu_Concat_Dataframes/README.md)

---

### 13. Instructor Do: Review Mastering Concatenation (5 min)

In this part of the lesson, review the Mastering Concatenation activity with students. You will start with a brief Q&A to test students' understanding, and then perform a dry walkthrough of the solution.

**Files:**

* [mastering_concatenation.ipynb](Activities/08-Stu_Concat_Dataframes/Solved/mastering_concatenation.ipynb)

* [fin_leaders_america.csv](Activities/08-Stu_Concat_Dataframes/Resources/fin_leaders_america.csv)

* [fin_leaders_members.csv](Activities/08-Stu_Concat_Dataframes/Resources/fin_leaders_members.csv)

* [invstrs_leadership_members.csv](Activities/08-Stu_Concat_Dataframes/Resources/invstrs_leadership_members.csv)

* [invstrs_leadership.csv](Activities/08-Stu_Concat_Dataframes/Resources/invstrs_leadership.csv)

Start the review by conducting a Q&A with the following questions:

* If you want to consolidate two DataFrames with the same columns into one DataFrame, which `concat` axis would you use?

  **Answer:** `row`. Concatenating by rows will combine the two DataFrames so that all rows are in one DataFrame.

* Let's say you want to take an intersection of two DataFrames that you have combined. Would you use the inner join operation or outer join operation?

  **Answer:** Inner join. An inner join will return a DataFrame with only matching rows.

* Which join will produce more rows: inner join or outer join?

  **Answer:** Outer join. Inner joins represent only a section of all of the data.

Open the solution and perform a dry walkthrough by covering the following points:

* The `concat` function can be used to combine or link more than one DataFrame.

* DataFrames should be concatenated by `rows` when the columns of the DataFrame are the same and should remain the same. The idea is that the rows are appended.

  ![stu_comined_dues](Images/stu_comined_dues.png)

* DataFrames should be concatenated by `columns` when columns from one DataFrame need to be combined with columns from another DataFrame. The idea is that the columns are appended.

  ![stu_concat_cols.png](Images/stu_concat_cols.png)

Answer any questions before moving on.

---

### 14. Instructor Do: Standard Deviation and Risk (10 min)

This section focuses on standard deviation and how it can be used to determine the risk associated with an investment. You will demo how to calculate the standard deviation using Pandas. Students will use the concepts covered in this section to calculate Sharpe ratios in the next activity.

**Files:**

* [std_dev_risk.ipynb](Activities/09-Ins_Std_Dev_Risk/Solved/std_dev_risk.ipynb)

* [tech_stocks_closing_value_2018.csv](Activities/09-Ins_Std_Dev_Risk/Resources/tech_stocks_closing_value_2018.csv)

Open the lesson slides and move to the "Standard Deviation and Risk" section.

Explain to students that everything completed in class up until this point has been to prepare them for portfolio and risk analysis. Highlight the following:

* An essential aspect of analyzing portfolio and stock data is determining **risk**.

* With daily returns calculated, and data from multiple portfolios combined into one dataset, you are now able to complete a holistic analysis of stock data.

* One component of risk is calculating the mean performance, or price, of a stock. The second is calculating the standard deviation.

* The **mean** can be used to determine the average value of a portfolio or stock over time. This can serve as a baseline for measuring risk and value: a portfolio/stock performing above average is more valuable; investing in a portfolio or buying a stock performing below average is risky business.

* A common technique for measuring how far away an asset is from the mean is calculating the standard deviation. **Standard deviation** identifies precisely how far away a value is from the average.

* The next step is to use **standard deviation** and **risk** to analyze portfolio performance, calculate risk, and identify risky investments.

  * A low standard deviation indicates that the value is not far from the average.

  * A high standard deviation means that the value is an outlier.

* Pandas provides a series of functions that can be used to calculate risk. The `std` function is used to calculate the standard deviation for a DataFrame.

* Standard deviation can be used to determine the risk associated with an investment. Standard deviation is also used to calculate how much returns have been distributed from the average.

* The higher the standard deviation, the greater the risk, and the potential for a higher payout.

End the presentation and open the unsolved Jupyter notebook. Live code how to use Pandas to calculate standard deviation to evaluate risk, highlighting the following:

* For this demo, we will use stock data from some popular technology companies.

  ![risk_data](Images/risk_data.png)

* Standard deviation should be computed using daily returns data, so we use the `pct_change` function to calculate daily returns for our stock data.

  ![risk_daily_returns](Images/risk_daily_returns.png)

* Calculating standard deviation against daily returns will help identify risk based on return value, rather than price volatility.

* The `std` Pandas function can be used to determine the risk associated with a portfolio or stock. Behind the scenes, the `std` function calculates the mean/average, and then it evaluates how far away from the average the input is. The function returns a new DataFrame.

  ![std_dev.png](Images/std_dev.png)

* Sorting the output from the `std` function in descending order (using `sort_values`) will display the portfolios/stocks that have the most and least amount of risk.

  ![risk_sort.png](Images/risk_sort.png)

* It's often necessary to calculate standard deviation at the yearly level. Calculating annualized standard deviation is done by multiplying the square root (`sqrt`) of the number of trading days in a year (`252`) with the standard deviation.

  ![anual_std](Images/anual_std.png)

* A key way to assess risk is to use the `plot.hist` function to create a chart of standard deviation trends. This will visually demonstrate the mean value, as well as the number and severity of any deviations for each element being plotted (i.e., each portfolio).

  ![std_plot.png](Images/std_plot.png)

* Another way to visualize standard deviation is with a box plot. **Box plots** display the total spread of the data, and they can be created using the `plot.box` Pandas function.

* Box plots have what are known as whiskers. **Whiskers** represent the range, or spread, of the data. Data elements that extend beyond the whiskers are considered outliers.

  ![std_dev_box.png](Images/std_dev_box.png)

Emphasize that the takeaway of these charts is that the greater the spread, the greater the risk. The greater the risk, the greater the potential for earnings and loss.

Answer any questions before moving on.

---

### 15. Instructor Do: Sharpe Ratios (10 min)

In this section, students will be introduced to Sharpe ratios and learn why risk-reward ratios are important in finance.

**Files:**

* [sharpe_ratios.ipynb](Activities/10-Ins_Sharpe_Ratios/Solved/sharpe_ratios.ipynb)

* [tech_stocks_2018_a.csv](Activities/10-Ins_Sharpe_Ratios/Resources/tech_stocks_2018_a.csv)

* [tech_stocks_2018_b.csv](Activities/10-Ins_Sharpe_Ratios/Resources/tech_stocks_2018_b.csv)

Explain to students that understanding how to identify risk and assess investment performance will help them adjust for risk to maximize reward.

Open the slideshow, move to the "Sharpe Ratios" section, and provide an overview of Sharpe ratios and how they are calculated. Cover the following points:

* **Sharpe ratios** are used to help compare the rate of return for an investment with its risk. Sharpe ratios shed light on the potential of profits, even with the risk involved.

* Sharpe ratios measure the excess return for each deviation. This will identify, in the wake of risk, how much profit is left to be gained.

* Sharpe ratios are calculated by subtracting the **return of portfolio** from the investment's **risk-free rate**. The difference is then divided by the standard deviation.

  ![sharpe_ratio_formula.png](Images/sharpe_ratio_formula.PNG)

* The risk-free rate is the return that one expects if investing in securities that effectively offer a guaranteed return. Usually the return on very short-term Australian or U.S. government bonds are used. Because such securities yield 0% (or less!) these days, rather than explicitly subtract zero from the numerator every time we calculate the Sharpe Ratio, we'll calculate Sharpe as the ratio of portfolio return relative to its risk (i.e., without the risk-free rate).

Open the unsolved Jupyter notebook and live code on how to calculate and plot Sharpe ratios. Explain the following as part of the demo:

* To calculate Sharpe ratios in this demo, we will use data from two files with stock data from diverse technology companies.

* After loading the data, we calculate daily returns and concatenate the resulting DataFrames using a `join` operation to compare prices on the same dates.

  ![sharpe_rations_concat](Images/sharpe_rations_concat.png)

* Sharpe ratios are commonly used to indicate whether or not an investment is the right decision. While standard deviation illustrates how far an investment has deviated from its average, Sharpe ratios use standard deviation to illustrate the relationship between standard deviation and risk-reward.

* Sharpe ratios enable investors to judge whether or not an investment is a good decision. Sharpe ratios adjust for risk, making them a valuable indicator of asset performance.

  ![sharpe_ratios.png](Images/sharpe_ratios.png)

* The return-to-risk ratio can be used to determine which stocks and/or portfolios have outperformed the others—the higher the Sharpe ratio, the better the investment.

* The `plot` function is used to compare Sharpe ratios visually.

  ![sharpe_ratios_plot.png](Images/sharpe_ratios_plot.png)

Answer any questions before moving on.

---

### 16. Student Do: Risky Business (15 min)

Now, it's time to put it all together! In this activity, students will prep data and use standard deviation and Sharpe ratios to analyze cryptocurrency portfolio performance. The goal is to calculate which portfolio has the highest risk. Students will also identify which individual cryptos have had the highest return. Data for this activity was retrieved from [Coinbase](http://coinbase.com).

Encourage students to work in pairs to complete this activity.

**Files:**

* [risky_business.ipynb](Activities/11-Stu_Risky_Business/Unsolved/risky_business.ipynb)

* [harold_portfolio.csv](Activities/11-Stu_Risky_Business/Resources/harold_portfolio.csv)

* [my_portfolio.csv](Activities/11-Stu_Risky_Business/Resources/my_portfolio.csv)

**Instructions:**

* [README.md](Activities/11-Stu_Risky_Business/README.md)

---

### 17. Instructor Do: Review Risky Business (5 min)

**Files:**

* [risky_business.ipynb](Activities/11-Stu_Risky_Business/Solved/risky_business.ipynb)

* [harold_portfolio.csv](Activities/11-Stu_Risky_Business/Resources/harold_portfolio.csv)

* [my_portfolio.csv](Activities/11-Stu_Risky_Business/Resources/my_portfolio.csv)

Open the solution, conduct a dry walkthrough review, and highlight the following:

* It's important to remember to clean data before beginning to analyze and compute calculations with it. Remember to use the `dropna` function to remove `NaN` values. If the `dropna` function is not used, `NaN` values may end up becoming indexes.

* The `concat` function can be used to combine portfolio returns. This enables analysis (i.e., standard deviation) of an entire portfolio rather than an individual stock. It also allows data from investments/portfolio A to be compared with investments/portfolio B.

* Harold's portfolio returns are combined with student returns in order to later calculate standard deviation and Sharpe ratios across the board.

  ```python
  # Concat returns DataFrames
  all_returns = pd.concat([harold_returns,my_returns], axis='columns', join='inner')
  all_returns.head()
  ```

  ![stu_concat_compare.png](Images/stu_concat_compare.png)

* Standard deviation is required to calculate Sharpe ratios. Standard deviation calculates the average value and compares the distribution of values to that average.

* The `std` function can be used to compute standard deviation. The output from the function is a series that indicates how far the value is from the mean, in the same units as the base data. The greater the value/deviation, the greater the risk and volatility.

  ```python
  # Calculate std dev
  all_portfolio_std = all_returns.std()
  all_portfolio_std.head()
  ```

  ```
  BTC     0.070488
  BTT     0.030731
  DOGE    0.050907
  ETH     0.091517
  LTC     0.084703
  dtype: float64
  ```

* Sharpe ratios are used to examine investment performance based on the risk-to-reward ratio.

  * The Sharpe ratio calculates the risk associated with a return and then divides that by the standard deviation of a return.

  * The higher the Sharpe ratio, the greater the reward associated with the risk. A high Sharpe ratio indicates a smart investment.

* Calculating the Sharpe ratio for Harold's and the students' portfolios reveals whose portfolio has the greatest reward associated with the risk.

  ```python
  # Calculate sharpe ratio
  sharpe_ratios = (all_returns.mean() * 252) / (all_portfolio_std * np.sqrt(252))
  sharpe_ratios.head()
  ```

  ```
  BTC      0.936891
  BTT    -32.935733
  DOGE     5.615811
  ETH     -5.638309
  LTC     -0.796855
  dtype: float64
  ```

* Sharpe ratios can be visually represented with a bar chart. This allows users to see which investments have high and low Sharpe ratios quickly.

  ![sharpe_plot.png](Images/sharpe_plot.png)

Ask students the following questions:

* How many smart investments did Harold make compared to risky investments? How many did you make?

    **Answer:** Out of his ten investments, Harold made six smart investments. Out of the students' six investments, three of them were smart investments.

* Which three cryptos were the smartest investments?

    **Answer:** ZIL, XRP and DOGE were the smartest crypto investments.

For the challenge section, the first step is to compute the annualized standard deviation for each portfolio.

![cryto_stu_annual_std](Images/cryto_stu_annual_std.png)

Next, the Sharpe ratios for each portfolio are calculated.

![crypto_stu_sharpe_ratios](Images/crypto_stu_sharpe_ratios.png)

To decide who has the smartest portfolio, the average Sharpe ratios are calculated and compared.

![crypto_stu_final](Images/crypto_stu_final.png)

Conclude the review by asking students the following question:

* Which portfolio was the smartest investment, based on risk to reward ratio?

  **Answer:** My portfolio was the smartest! Harold owes me five dollars.

Answer any questions before moving on.

---

### 18. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
