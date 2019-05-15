### 18. Students Do: Multi-Indexing (15 mins)

In this activity, students will use hierarchical indexes to gain access to historical stock data. The objective of the assignment is for the students to take their indexing skills to the next level by using DataFrames with multiple indices. Students will leverage NASDAQ data to perform data segmentation for multiple tickers across various date ranges.

**Files:**

* [indexing_fever.ipynb](Activities/06-Stu_Multi_Indexing/Unsolved/Core/indexing_fever.ipynb)

**Instructions:**

* [README.md](Activities/06-Stu_Multi_Indexing/README.md)

### 19. Instructor Do: Review Multi-Indexing (5 mins)

**Files:**

* [indexing_fever.ipynb](Activities/06-Stu_Multi_Indexing/Solved/Core/indexing_fever.ipynb)

Walkthrough the solution and go over the following discussion points:

* Multi-indexing is used to create multiple look up points for data, as well as to create hierarchal relationships between data elements. Multi-indexing will enable users to index data with more than one data element (i.e. `ticker` and `date`).

* Multi-indexing is valuable as it enables data to be indexed with more than one column. Using multi-indexing, especially with date Series, ensures financial data can be stored and accessed by date.

* The values associated with the index can then be grouped under the index. Hierarchical relationship between indexes is indicated by the `level` attribute of the index. The number of `levels` is based on the number of indexes.

    ![Ins_MultiIndexing_Review_Overview](Images/Ins_MultiIndexing_Review_Overview.png)

* Indices can be created for a DataFrame using the `set_index` function. The `set_index` function accepts a list of Series names to index by.

    ```python
    nasdaq_data = nasdaq_data.set_index(['ticker','date'])
    nasdaq_data.head()
    ```

    ![Ins_MultiIndexing_Set_Index.png](Images/Ins_MultiIndexing_Set_Index.png)

* An advantage of indexing with a date is that Pandas provides a DatetimeIndex object that allows date indexes to be used more effectively than when a string. The `DatetimeIndex` function can be used with `set_index` to create a `DatetimeIndex` object. The `DatetimeIndex` will cast a Series to a Datetime object so that it can be used with date functions. Once the `DatetimeIndex` has been created, dates can be accessed using various formats (i.e. `YYYYMMDD`, `YYYYMM`, `Month Day, Year`, etc.).

    ```python
    # Set multi-index
    nasdaq_data = nasdaq_data.set_index(['ticker',pd.DatetimeIndex(nasdaq_data['date'])])
    nasdaq_data.head()
    ```

    ![Ins_MultiIndexing_Datetime_Index.png](Images/Ins_MultiIndexing_Datetime_Index.png)

* When using multi-indexing, values for both indexes can be passed to the `loc` function. This will output only the data associated with those indices.

    ```python
    # Slice data using YYYY-MM-DD date format
    google_jan_1st_YYYYMMDD = nasdaq_data.loc[('AMZN','2019-01-09')]
    google_jan_1st_YYYYMMDD.head()
    ```

    ![Ins_MultiIndexing_Loc.png](Images/Ins_MultiIndexing_Loc.png)

* `DatetimeIndex` also allows dates to be sliced as months with the YYYYMM (i.e. 201901) format. This slices the data the month level, allowing for data to be returned without having to specify a month start, month end date. Without the `DatetimeIndex`, data would have to be sliced using a range [i.e. slice(`2019-01-01`,`2019-01-31`].

    ```python
    # Slicing month of January 2019 data using date range in `YYYY-MM` format
    google_jan_2019 = nasdaq_data.loc[('GOOG','2019-01')]
    google_avg_close = google_jan_2019['close'].mean()
    print(google_avg_close)
    ```

    ![Ins_MultiIndexing_Loc_YYYYMM.png](Images/Ins_MultiIndexing_Loc_YYYYMM.png)

* `DatetimeIndex` can also be used with the Pandas `date_range` function. The `date_range` function accepts a `start` value, number of `periods` wanted, and the `freq` of the data needed (i.e. daily, monthly, yearly).

    ```python
  # Slicing month of February 2019 data using date range in `YYYY-MM` format
  tsla_jan_2019 = nasdaq_data.loc[('TSLA',pd.date_range(start='2019-02-01',periods=14, freq='D')), :]
  tsla_avg_close = tsla_jan_2019['close'].mean()
  print(tsla_avg_close)
    ```

    ![Ins_MultiIndexing_Loc_Date_Range.png](Images/Ins_MultiIndexing_Loc_Date_Range.png)
