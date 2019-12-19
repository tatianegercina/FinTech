# Out of Sorts

You're trying to identify the top 5 performing days for Tesla investment returns, but you have over a hundred days' worth of data, and nothing is sorted. Sort the stock data in descending order to identify the top 5 performing days.

## Instructions

Using the [starter file](Unsolved/out_of_sorts.ipynb) and Google Finance historical stock data, complete the following steps:

1. Navigate to [Google Sheets](https://docs.google.com/spreadsheets/) and use the in-built Google Finance function to download ticker data. Load the CSV data into Pandas using the `read_csv` function.

2. Index data by `Date`.

3. Clean the data.

4. Output a sample of the data.

5. Calculate daily returns.

6. Sort the DataFrame by `Close` in descending order using `sort_values` to obtain top daily return records. 

7. Slice out 5 records.

8. Plot the data.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.