## Indexing Fever!

You've caught the multi-indexing fever! Add power to your financial analytic pipelines by indexing your data by month and year with a DatetimeIndex.

## Instructions

Using the [starter-file](Unsolved/Core/indexing_fever.ipynb) provided, and the Nasdaq historical stock [data](Resources/nasdaq_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`.

2. In the `read_csv` function, set the index to equal `Trade DATE` Series. Enable read_csvs `parse_dates` and `infer_datetime_format` parameters.

3. Group data by DatetimeIndex year and month.

4. Select close price for `GOOG` for May 2019 by passing in values for `year` and `month` indices.

5. Identify `GOOG` closing price for 30 days ago using `time_delta` function. Hint: subtract `timedelta(days=30)` from `date.today()`.

### Challenge

Take this activity to the next level by calculating the mean close price for `GOOG` for all of `2019`.

### Hint

Additional information regarding `DatetimeIndex` capabilities can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html). Information regarding `timedeltas` can be found at the this [location](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html).
