# Calculating Beta with Pandas DataFrames

In this activity, you will practice how to calculate the beta value between the daily returns of MSFT and the S&P 500 (overall market).

## Instructions

Perform the following:

1. Import the `pandas`, `pathlib`, and `seaborn` libraries, and set the `%matplotlib inline` property.

2. Create a two variables `msft_csv_path` and `sp500_csv_path` that represents the path to the [MSFT.csv](Resources/MSFT.csv) and [SP500.csv](Resources/SP500.csv) using the Pathlib library.

3. Read the CSVs into Pandas DataFrames, setting the `date` as datetime index for both.

4. Use the `concat` function to combine the DataFrames by column and perform an inner join. Also, make sure to sort the index of the Pandas DataFrame in ascending order (important for time series calculations!)

5. Drop the extraneous columns: `volume`, `open`, `high`, `low`.

6. Rename the columns for the respective stock (MSFT or SP500).

7. Calculate the daily returns of the combined DataFrame.

8. Use the `cov` function to calculate the covariance between the daily returns of MSFT and the daily returns of the S&P 500.

9. Use the `var` function to calculate the variance of the daily returns for MSFT.

10. Calculate the beta value for MSFT by dividing the previously calculated covariance value by the calculated variance.

11. Use the `rolling` function to calculate a 30 day rolling covariance of MSFT daily returns vs. S&P 500 daily returns. Plot the 30 day rolling covariance.

12. Use the `rolling` function to calculate a 30 day rolling variance of S&P 500 daily returns. Plot the 30 day rolling variance.

13. Calculate the 30 day rolling beta value for MSFT by dividing the previously calculated 30 day rolling covariance value by the calculated 30 day rolling variance. Plot the 30 day rolling beta.

14. Use the `lmplot` from the `seaborn` library to plot a scatterplot of MSFT to S&P500 daily returns and fit a regression line.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
