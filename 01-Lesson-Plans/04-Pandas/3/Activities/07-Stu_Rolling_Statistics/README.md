# Simple Moving Averages

In this activity, Harold has been asked to plot the 20-day, 50-day, and 100-day Simple Moving Averages and Rolling Standard Deviations for Netflix stock (NFLX). Upper management is looking to potentially invest long-term in NFLX; however, they want to be sure that they'll be taking a position at the right time.

Use the Pandas library to help Harold plot the Simple Moving Averages and Rolling Standard Deviations to generate insights regarding whether or not his company should currently invest in NFLX long-term.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import libraries and dependencies

  * Read in the `nflx.csv` as a Pandas DataFrame and set the `date` column as a datetime index.

  * Use the `rolling` function and set the `window` parameter to designate the time windows. Then use the `mean` function to calculate the following:

  * 20-Day Simple Moving Average
  * 50-Day Simple Moving Average
  * 100-Day Simple Moving Average

  * Overlay the SMAs on top of the plot for daily closing prices of NFLX.

  * Use the `rolling` function and set the `window` parameter to designate the time windows and use the `mean` function to calculate the following:

  * 20-Day Rolling Standard Deviation
  * 50-Day Rolling Standard Deviation
  * 100-Day Rolling Standard Deviation

  * Overlay the STDs on top of the plot for daily closing prices of NFLX.

## Hints

* To learn more about simple moving averages and how they work, read more [here](https://www.investopedia.com/terms/s/sma.asp)  
