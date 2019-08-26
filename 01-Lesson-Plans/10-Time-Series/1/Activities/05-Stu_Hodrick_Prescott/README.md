# And I'll Be there -- You've Got a FRED

## Introduction

* In this activity, you will use the Hodrick-Prescott filter to examine macro economic trends in the United States between 2004 and 2010.

* FRED, or Federal Reserve Economic Data, is a database of macroeconomic data in the United States.

## Instructions

* Use pandas's web datareader to pull in data from FRED as a pandas data frame. You do not need an API key.

* See the documentation for an example of retrieving data from FRED: [https://pandas-datareader.readthedocs.io/en/latest/remote_data.html](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html).

* Retrieve GDP data from FRED (keyword `GDP`) from 2004 to 2010, and separate the data into trend and non-trend components with the H-P filter. Plot the results.

* Repeat the processes for inflation (keyword `CPIAUCNS`) and job count (keyword `PAYEMS`).

* For at least one of these data sets, plot the moving and exponentially-weighted moving averages. How do the results compare to results of the H-P filter?
