# And I'll Be there—You've Got a FRED

## Introduction

* In this activity, you will use the Hodrick-Prescott filter to examine macro economic trends in the United States between 2004 and 2010.

* FRED, or Federal Reserve Economic Data, is a database of macroeconomic data in the United States.

## Instructions

* Read the csv GDP data and set the `DATE` column as a datetime index.

* Plot the raw GDP data as a line plot.

* Use the `hpfilter` function to decompose the GDP column into the trend and noise components.

* Plot the GDP trend data as a line plot.

* Plot the GDP noise as a line plot.

* Repeat the processes for inflation (keyword `CPIAUCNS`) and job count (keyword `PAYEMS`).

* For at least one of these data sets, plot the exponentially-weighted moving averages. How do the results compare to results of the H-P filter?

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
