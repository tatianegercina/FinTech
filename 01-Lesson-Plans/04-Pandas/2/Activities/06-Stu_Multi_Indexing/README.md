## Indexing Fever!

You've caught the multi-indexing fever! Add power to your financial analytic pipelines by introducing multi-indexing to ALL of your code. Since you're working with stock data, index your data based off of ticker and date.

## Instructions

Using the [starter-file](Unsolved/Core/indexing_fever.ipynb) provided, and the Nasdaq historical stock [data](Resources/nasdaq_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`.

2. Output a sample of the data.

3. Create multi-index using `DatetimeIndex`.

4. Select close price for `GOOG` for January 2019 using `YYYY-MM` format, i.e. '2019-01'.

5. Determine average close price for `TSLA` for date range 2019-02-01 to 2019-04-30.

### Challenge

Take this activity to the next level by calculating cummulative returns for MSFT and TSLA data for dates May 2016 to May 2019.

1. Use the `sort_index` function to sort by ticker. Hint: `sort_index(axis=0)`.

1. Slice data for MSFT and TSLA using `date_range` function.

2. Calculate daily returns for tickers and date range.

3. Calculate `cumprod`.

4. Plot data for both tickers on the same plot. Hint: the `unstack(level=)` can be used to plot index tickers as separate lines. The level of the index has to be passed to the function as an argument.

5. Resample three years of cumulative returns data to calculate the average cumulative return.

### Hint

When plotting multi-indexed data, the `unstack(level=)` should be used to plot index tickers as separate lines. The level of the index has to be passed to the function as an argument, in the form of positional notation.

  ```python
  three_year_cumprod.unstack(level=0).plot()
  ```
