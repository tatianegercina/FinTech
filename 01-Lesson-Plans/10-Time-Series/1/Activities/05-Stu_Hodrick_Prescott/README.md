# And I'll Be there—You've Got a FRED

## Introduction

* In this activity, you will use the Hodrick-Prescott filter to examine macro economic trends in the United States between 2004 and 2010.

* FRED, or Federal Reserve Economic Data, is a database of macroeconomic data in the United States.

## Instructions

## Fetching FRED data

* Use Pandas's web datareader to pull in data from FRED as a Pandas DataFrame. You do not need an API key.

* See the documentation for an example of retrieving data from FRED: [https://pandas-datareader.readthedocs.io/en/latest/remote_data.html](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html).

### Hodrick-Prescott Filter

* Use the DataReader to fetch the GDP data from FRED using the start and end dates.

* Plot the raw GDP data as a line plot.

* Use the `hpfilter` function to decompose the GDP column into the trend and noise components.

* Plot the GDP trend data as a line plot.

* Plot the GDP noise as a line plot.

* Repeat the processes for inflation (keyword `CPIAUCNS`) and job count (keyword `PAYEMS`).

* For at least one of these data sets, plot the exponentially-weighted moving averages. How do the results compare to results of the H-P filter?

### Notes

You will need to install the [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) for the activity.

```
pip install pandas-datareader
```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
