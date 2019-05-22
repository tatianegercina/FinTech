### 6. Students Do: Groupby (15 mins)

This activity will entail students working with historical cryptocurrency data. Students will load in cryptocurrency data, group data by each crypto, and then perform aggregations to analyze price trends. Students will then plot the results.

**Files:**

* [crypto_circus.ipynb](Activities/06-Stu_Groupby/Unsolved/crypto_circus.ipynb)

**Instructions:**

* [README.md](Activities/06-Stu_Groupby/README.md)

### 7. Instructor Do: Review Groupby (5 mins)

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
