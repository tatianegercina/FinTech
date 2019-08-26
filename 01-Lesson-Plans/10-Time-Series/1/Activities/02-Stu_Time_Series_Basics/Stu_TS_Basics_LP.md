### Students Do: Time Series Basics (10 mins)

* **Files:**

  * [starter notebook](tbd)

* In this activity, students will work with an Amazon stock price time series.

### Instructor Do: Review Activity (5 mins)

* Quickly walk through the basic steps of working with a time series in pandas. Try not to dwell on any point for too long, as students will work with these methods repeatedly throughout the week.

  ```python
  df2 = pd.read_csv('amazon.csv', parse_dates=True, index_col='Date')
  ```

  * The `parse_dates` and `index_col` arguments are used to format the time series index as datetime.

  ```python
  sep_2018 = df2.loc['2018-09']
  ```

  * The `loc[]` accessor is used to select only data from September, 2018.

  ```python
  df3 = df2.loc['2018-09':'2018-10']
  ```

  * The `loc[]` accessor is used to select rows from a date range.

  ```python
  df4 = df2.loc['2018 sep': '2018 oct']
  ```

  * The same date range can be obtained in a number of ways. The `loc[]` accessor is fairly flexible.

  ```python
  weekly = df2['Close'].resample('W').mean()
  ```

  * The weekly averages of closing stock prices is obtained with `resample('W)`.

* Finally, explain the bonus code:

  ```python
  df3 = df2.loc[:, df.columns.str.contains('Close')]
  ```

  * The data frame was selected only for columns containing the word 'Close' by using the `str.contains()` method and the `loc[]` accessor.

  * `df.columns.str.contains('Close')` returns an array of False and True for whether that column contains the specified keyword.
