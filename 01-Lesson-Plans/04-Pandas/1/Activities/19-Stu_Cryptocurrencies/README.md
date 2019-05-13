## A Blast from the Past!

Two years ago, you made multiple investments in the cryptocurrency market. You purchased Bitcoin, Ethereum, Bitcoin-cash, Ripple, Litecoin, and a number of other alt coins. Between the volatility of the market and time constraints in your professional and personal life, you were unable to establish and maintain a dedicated presence in the cryptocurrency market.

Last night, the market lit up with crypto activity. Bitcoin, Ethereum, Bitcoin-cash, Ripple, and Litecoin dramatically increased in price! The crypto hype is back!

You've been out of the crypto game for a while, so perform a historical price analysis using Pandas to get a better understanding of crypto price fluctuations, volitility, and rate of return for your holdings for the past two years. Hypes like these come and go all the time; make sure the returns are worth it.

## Instructions

Using the [starter-file](Unsolved/blast_from_the_past.ipynb) provided, and Harold's financial [data](Resources/crypto_data.csv), complete the following steps:

1. Load CSV data into Pandas using `read_csv`.

2. Output a sample of the data.

3. Drop `data_time` and `timestamp` fields.

4. Calculate the number of records in the DataFrame.

5. Calculate average percent of nulls.

6. Calculate number of nulls.

7. Drop nulls.

8. Validate all missing values have been cleaned.

9. Enforce Date data types using the `Pandas.to_datetime().dt.date` function.

10. Create an index using `data_date`.

11. Drop `data_date` Series.

12. Plot DataFrame.

13. Segment crypto data into 5 DataFrames, with there being a DataFrame for each cryptocurrency.

14. Drop the `currency` Series from segmented DataFrames.

15. Calculate daily returns for each crypto subset.

16. Plot daily returns for each crypto in the same plot. See the below hint for more information regarding how to add more than one DataFrame to a plot.

### Challenge

Instead of plotting data for the entire DataFrame, segment the data by adding in yearly indexing.

1. Create a one year date range for 05/10/2017-05/10/2018 using indexing.

2. Create a two year date range for 05/10/2017-05/10/2019 using indexing.

3. Plot one year of returns for all cryptos on one chart.

4. Plot two years of returns for all cryptos on one chart.

### Hint

Multiple DataFrames can be plotted together on the same chart. In order to do this, the `ax` parameter associated with `plot` function will need to be used. By plotting the first DataFrame, and then passing that DataFrame in as `ax` for each subsequent plot, one plot is created with data from multiple DataFrames.

  ```python
  df1 = bitcoin_daily_returns_1_year.plot()
  df2.plot(ax=df1)
  df3.plot(ax=df1)
  df4.plot(ax=df1)
  df5.plot(ax=df1)
  ```

The `legend([])` function can be used to specify the legend labels for your plot object. `Legend` must be executed against a plot object. The label names listed in the brackets should follow the order in which the DataFrames were added to the plot.

  ```python
  df1.legend(['df1','df2','df3','df4','df5'])
  ```
