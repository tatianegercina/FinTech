### 8. Instructor Do: Multi Indexing (10 mins)

**Files:**

* [Multi Indexing Slides]()

* [multi-index.ipynb](Activities/05-Ins_MultiIndex/Solved/multi_index.ipynb)

Navigate to the Unit 4.2 slides and provide an overview of multi-indexing.

* Multi-indexing occurs when there is more than one column/value is used as an index in a DataFrame. Multi-indexing is sometimes referred to as Hierarchical Indexing. There are a number of ways in which a DataFrame can have multiple indexes.

* Multiple indexes are valuable as it enables dimensional data to be grouped and retrieved. This is particularly valuable when working with Financial data and dates. While dates are great to index, dates do not always provide all of the detail needed to manipulate and analyze data. For example, when looking at stock prices and purchases over time, it is important to group data by both date and ticker. In this operation, both date and ticker can be indexes, and by specifying date and ticker, you can slice out the price of a particular stock at a specific point in time. Essentially, multi-indexing improves data storage, lookup, and manipulation/assignment.

Live code how to create and use multiple indexes, as well as how to access data using more than one index.

* Multi-indexing is commonly done when working with `Date` data. `Date` data is a unique type of index. It is considered a `DatetimeIndex`. `DatetimeIndexes` have the ability to inherently create multiple indexes. A `DatetimeIndex` can be created by passing a `Date` field to the `index_col` attribute when using `read_csv`. `parse_dates` and `infer_datetime_format` should also be included.

    ```python
    # Read in data
    csv_path = Path("../Resources/stock_data_by_ticker.csv")
    ticker_data = pd.read_csv(csv_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
    ticker_data.head()
    ```

* `DatetimeIndexes` have the ability to be broken up into multiple indices based off of year and month. The `DatetimeIndex` object includes the attributes `index.year`, `index.month`, and `index.day`. Passing these to a `groupby` statement would create multiple indexes based off of each attribute.

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

* Because multi-indexing involves grouping data, an aggregation also needs to be applied against the data. A common example is the `mean` function for calculating average.

  ```python
  # Group by year and month and calculate average
  ticker_data_grp_2 = ticker_data.groupby([ticker_data.index.year, ticker_data.index.month]).mean()
  ticker_data_grp_2.head()
  ```

  ![multi_index_agg.png](Images/multi_index_agg.png)

* The `loc` function can be used to slice data from a DataFrame with multiple indexes. While not all indexes are required to be passed, the top level index needs to be specified (i.e. `year`). If a specific index value is not available, the `:` symbol can be used to slice all records. Essentially, indexes have to be accessed and used hierarchically (i.e. `year` > `month` > `day`).

    ```python
    # Slice data for 4/12/2019 from first group
    ticker_data_slice = ticker_data_grp.loc[2019,4,12]
    ticker_data_slice.head()
    ```

  ![multi_index_slice.png](Images/multi_index_slice.png)
