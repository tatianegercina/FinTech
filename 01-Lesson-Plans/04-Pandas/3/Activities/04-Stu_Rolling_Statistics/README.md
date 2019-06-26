# Simple Moving Averages

Harold has been asked to plot the 20-day, 50-day, and 100-day simple moving averages and rolling standard deviations for Netflix stock (NFLX). Upper management is looking to potentially invest long term in NFLX, but they want to be sure that they'll be taking a position at the right time.

Use the Pandas library to help Harold plot the simple moving averages and rolling standard deviations in order to generate insights regarding whether or not the company should currently invest in NFLX long term.

## Instructions

Using the starter file, complete the following steps.

1. Import libraries and dependencies. 

1. Read in `nflx.csv` as a Pandas DataFrame, and set the Date column as a datetime index.

1. Use the `rolling` function and set the `window` parameter to designate the time windows. Then, use the `mean` function to calculate the following:

    * 20-day simple moving average

    * 50-day simple moving average

    * 100-day simple moving average

1. Overlay the plot for daily closing prices of NFLX with the SMAs. 

1. Use the `rolling` function and set the `window` parameter to designate the time windows. Then, use the `mean` function to calculate the following:

    * 20-day rolling standard deviation

    * 50-day rolling standard deviation
  
    * 100-day rolling standard deviation

1. Overlay the plot for daily closing prices with the STDs. 

## Hint

Go [here](https://www.investopedia.com/terms/s/sma.asp) to learn more about simple moving averages and how they work.

- - - 
© 2019 Trilogy Education Services
