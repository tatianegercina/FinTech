# Indexing Fever

You've caught the multi-indexing fever! Add power to your financial analytic pipelines by indexing your data by month and year with a DatetimeIndex.

## Instructions

Using the [starter file](Unsolved/Core/indexing_fever.ipynb), complete the following steps:

1. Extract three months of historical data from [Google Sheets](https://docs.google.com/spreadsheets/) via the in-built Google Finance function, and load the CSV data into Pandas using `read_csv`.

2. In the `read_csv` function, set the index to equal `Date` series. Enable read_csv's `parse_dates` and `infer_datetime_format` parameters.

3. Group data by DatetimeIndex year and month.

4. Select close price for `GOOG` for May 2019 by passing in values for `year` and `month` indices.

### Challenge

Take this activity to the next level by calculating the mean close price for `GOOG` for all of `2019`.

### Hints

* Additional information about `DatetimeIndex` capabilities can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html).

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
