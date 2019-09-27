# Euro ETF

## Instructions

At a given moment in the ETF market, there is a price at which sellers are willing to sell and a price at which buyers are willing to buy. The closest discrepancy between the selling and buying prices is referred to as the bid-ask spread.

In this activity, you will analyze the autocorrelation of a ETF bid-ask spread. 

Open the dataset and parse the `timestamp` column as datetime, and set it as the index.

Resample the dataframe at 10-second intervals and obtain the mean. Drop all NaNs.

Obtain the autocorrelation value at a lag of 1. If you like, repeat the process for another lag, e.g., 2.

Plot the ACF and PACF. 

How many significant lags do you see in these plots outside the default confidence interval of 95%?



© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.