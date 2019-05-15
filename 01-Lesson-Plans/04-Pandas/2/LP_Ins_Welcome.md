### 1. Instructor Do: Welcome (5 mins)

Welcome the students to the second day of Pandas. The focus for this class will be learning how to sort, group, multi-index, and concatenate DataFrames. Students will also learn how to use Pandas functions to calculate standard deviation and risk and sharpe ratios.

**Files:**

* [welcome-slides]()

Kick the class off with a returns refresher activity. This activity will be two fold. The focus is on teaching students how to extract historical ticker data from NASDAQ.com as a CSV, as well as calculate daily returns.

* Navigate to the [NASDAQ](https://nasdaq.com) website. Use the search bar to enter in the name or ticker of a stock. This example uses Facebook.

  ![nasdaq_search.png](Images/nasdaq_search.png)

* Use the left-hand navigation pane to select `Historical Quote`. This link will open a web UI that can be used to select the time range of data that is desired.

  ![launch_historical.png](Images/launch_historical.png)

* NASDAQ provides a simplified view into ticker prices with the `NASDAQ Official Close Price` page. This page provides access to ticker close prices. NASDAQ also provides flexibility in extracting additional data elements as well (i.e. open, high, etc.). Choose the `NASDAQ Official Close Price` page for this assignment.

  ![nasdaq_layout.png](Images/nasdaq_layout.png)

* Select `3 months` as the desired timeframe.

  ![select_timeframe.png](Images/select_timeframe.png)

* Scroll down to the `Download All Available Data` link, and right click. Click `Save Link As`. Choose a folder and name the file `fb_nasdaq.csv`. Click save.

  ![fb_nasdaq.png](Images/fb_nasdaq.png)

* Load the saved file into Pandas. Use the `index_col`, `parse_dates`, and `infer_datetime_format` attributes to create a DatetimeIndex (based off of `Trader DATE`) for date range manipulation. Emphasize to students that these attributes are used to ensure Pandas interprets the date index as a date object.

  ```python
  # Read in CSV data
  csv_path = Path('../Resources/fb_nasdaq.csv')
  fb_ticker_data = pd.read_csv(csv_path, index_col='Trade DATE', parse_dates=True, infer_datetime_format=True)
  fb_ticker_data.head()
  ```

* Drop `Symbol` Series.

  ```python
  # Drop Trade DATE and symbol column
  fb_ticker_data = fb_ticker_data.drop(columns='Symbol')
  fb_ticker_data.head()
  ```

* Slice data and calculate daily returns for Feb 2019.

  ```python
  # Calculate daily returns
  fb_slice = fb_ticker_data.loc['2019-03-01':'2019-02-01']
  fb_quarter_returns = fb_slice.pct_change()
  fb_quarter_returns
  ```

After the refresher is complete, ask students if they have any questions.

Proceed to finish reviewing the agenda for today's class. Communicate that today's activities will provide the foundation needed for students to begin grouping and aggregating data. Foreshadow what's to come by explaining that it is common to group and aggregate financial data by a number of different metrics, including dates, tickers, categories, etc. Example use cases include determining the average close price for a list of stock tickers and aggregating data (summing, adding, averaging) across time three month intervals.
