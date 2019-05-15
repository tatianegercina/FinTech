### 4. Students Do: Correlated Stocks (20 mins)

**Instructions:**

* [README.md](Activities/09-Stu_Pandas_Visualization/README.md)

**Files:**

* [market_analysis.ipynb](Activities/09-Stu_Pandas_Visualization/Unsolved/market_analysis.ipynb)

### 5. Instructor Do: Correlated Stocks (5 mins)

**Files:**

* [market_analysis.ipynb](Activities/09-Stu_Pandas_Visualization/Solved/market_analysis.ipynb)

Open the solution and explain the following:

* Setting the `%matplotlib inline` feature is necessary to displaying the plots in the jupyter notebook file.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  from pathlib import Path
  %matplotlib inline
  ```

* The `value_counts()` function returns a Series object representing the frequency of unique values of a Series object or column of a DataFrame.

  ![value-counts-function](Images/value-counts-function.png)

* The `plot` function defaults to line charts; however, the `kind` parameter allows one to alter the type of chart produced.

  ```python
  # Plot a pie chart from the distribution of company sectors
  sector_count.plot(kind='pie')
  ```

* A pie chart is best suited for representing the distribution of a whole category. In this case, the distribution of company sectors in the S&P 500. The plot shows that `Consumer Discretionary` companies hold the greatest weight or proportion amongst the S&P 500 companies.

  ![pie_chart](Images/pie.png)

* To create certain plots, it may be easier to create a subset of the original DataFrame. In this example, the `Symbol` and `Market Cap` columns can be selected as a subset of the original data.

  ```
  market_cap = sp500_companies_csv.loc[:, ['Symbol', 'Market Cap']]
  ```

* Make sure to set the index on DataFrames that are intended for plotting to display the correct labels. For example, the x-axis labels on a line chart.

* Use the `nlargest()` function to return the top `n` number of rows based on a particular DataFrame column.

  ![nlargest-function](Images/nlargest-function.png)

* A bar chart is best suited for comparing the values of several variables of the same type. In this case, the market caps of the top 20 companies in the S&P 500. The plot shows the varying market cap values of the top 20 market cap companies of the S&P 500.

  ![bar_chart](Images/bar.png)

* A scatter plot is best suited for comparing the relationships between two variables. In this case, the relationship between price and earnings. The plot shows that there is generally a range between which most companies tend to cluster around price and earnings; however, as earnings increase there seems to be a slight positive trend in price as well.

  ![scatter_plot](Images/scatter.png)
Ask for any remaining questions before moving on.
