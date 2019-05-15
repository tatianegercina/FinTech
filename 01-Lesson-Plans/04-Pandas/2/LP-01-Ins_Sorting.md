### 2. Instructor Do: Sorting (5 mins)

**Files:**

* [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Explain that it is very common to sort values in ascending or descending order. Pandas provides a function for this called `sort_values` that will sort a DataFrame by a column. We can use this to find the highest or lowest daily returns from our stock data.

Walk through the solution and highlight the following:

* A DataFrame can be created from lists or dictionaries. In this example, a DataFrame of painting prices is supplied as a Python Dictionary which we convert to a DataFrame.

  ![creating-dataframes.png](Images/creating-dataframes.png)

* The DataFrame can be sorted by any column using `sort_values`. In this example, the DataFrame is sorted in ascending order (the default) by the price.

  ![sort-ascending.png](Images/sort-ascending.png)

* The DataFrame can also be sorted in descending order using the `ascending=False` parameter.

  ![sort-descending.png](Images/sort-descending.png)
