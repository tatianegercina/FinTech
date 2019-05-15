### 18. Students Do: Multi-Indexing (15 mins)

In this activity, students will use hierarchical indexes to gain access to historical stock data. The objective of the assignment is for the students to take their indexing skills to the next level by using DataFrames with multiple indices. Students will leverage NASDAQ data to perform data segmentation for a single ticker across multiple months in a year.

**Files:**

* [indexing_fever.ipynb](Activities/09-Stu_Multi_Indexing/Unsolved/Core/indexing_fever.ipynb)

**Instructions:**

* [README.md](Activities/09-Stu_Multi_Indexing/README.md)

### 19. Instructor Do: Review Multi-Indexing (5 mins)

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
