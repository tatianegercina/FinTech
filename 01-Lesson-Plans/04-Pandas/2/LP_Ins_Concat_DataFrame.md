### 12. Instructor Do: Concatenating DataFrames (5 mins)

**Files:**

* [concat_dataframe.ipynb](Activities/12-Concating_DataFrames/Solved/concat_dataframe.ipynb)

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
