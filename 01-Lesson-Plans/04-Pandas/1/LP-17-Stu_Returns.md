### 17. Students Do: Returns Over Date Ranges (20 mins)

In this activity, Harold's manager wants Harold to analyze the last 10 years of historical price data for AMD and plot the daily returns over the last 1, 3, 5, and 10 year time periods. In addition, Harold's manager wants to see the differences in average daily returns for each time period to perhaps understand whether a short or long term perspective should be used in prospecting AMD as a potential candidate.

Help Harold analyze the last 10 years of AMD stock data.  

**Instructions:**

* [README.md](Activities/17-Stu_Returns/README.md)

**Files:**

* [returns_over_date_ranges.ipynb](Activities/17-Stu_Returns/Unsolved/returns_over_date_ranges.ipynb)

### 18. Instructor Do: Returns Over Date Ranges (5 mins)

**Files:**

* [returns_over_date_ranges.ipynb](Activities/17-Stu_Returns/Solved/returns_over_date_ranges.ipynb)

Open the solution and explain the following:

* We need to set the `%matplotlib inline` feature to display plots in jupyter notebooks.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  from pathlib import Path
  %matplotlib inline
  ```

* After reading in the csv as a DataFrame and doing some quick summary statistical analysis, data should be trimmed to match the needs of the requirements. In this case, only the `close` column is needed to calculate daily returns.

  ![drop-columns](Images/drop-columns.png)

* Setting the date as the index allows us to slice the DataFrame by specified date ranges using the `loc` function, which allows for `[start:end]` notation.

  ![datetime-index](Images/datetime-index.png)

* Notice however the hard-coding that had to be done to create the slice notations for each time period. It would be much more convenient to be able to choose a date and use a function to go 365 days prior to that date to create 1 year, 3 year, 5 year, and 10 year time chunks; `datetime` objects will help us do this in the future.

  ```python
  # Slice DataFrame into 1 year time frame
  daily_return_1_year = daily_return.loc['2018-04-30':'2019-04-29']
  daily_return_1_year
  ```

* The data shows that trading AMD in the short-term is potentially more profitable as the average daily return of a `1 Year` time frame is the highest at `0.004538` or `4.53%`.

Ask for any remaining questions before moving on.
