### 5. Instructor Do: Groupby (10 mins)

**Files:**

* [groupby.ipynb](Activities/05-Ins_Groupby/Solved/groupby.ipynb)

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
