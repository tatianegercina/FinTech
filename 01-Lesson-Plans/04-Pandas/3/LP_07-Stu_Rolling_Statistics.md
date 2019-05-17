### 7. Students Do: Simple Moving Averages (20 mins)

**Instructions:**

* [README.md](Activities/07_Stu_Rolling_Statistics/README.md)

**Files:**

* [simple_moving_averages.ipynb](Activities/07_Stu_Rolling_Statistics/Unsolved/simple_moving_averages.ipynb)

### 8. Instructor Do: Simple Moving Averages (5 mins)

**Files:**

* [simple_moving_averages.ipynb](Activities/07_Stu_Rolling_Statistics/Solved/simple_moving_averages.ipynb)

Open the solution and explain the following:

* The `rolling` function and the `window` parameter set the time window for the calculated metric, in this case the average or `mean`. 

  ![rolling-mean-calculation](Images/rolling-mean-calculation.png)

* Notice the last `19` datetime indexes contain `NaN` values, this is because the `window` parameter has been set to `20` and therefore the last `19` indexes do not have enough data to support the `20` day time window. 

  ![not-enough-window-data](Images/not-enough-window-data.png)

* When overlaying the SMAs over the plot of the daily closing prices for NFLX, one can see the ways in which larger rolling time windows smooth data and show general trends as opposed to smaller rolling time windows that showcase more volatility.

  ![sma-overlay](Images/sma-overlay.png)

* When overlaying the STDs over the plot of the daily closing prices for NFLX, one can see the differences in volatility for different time scopes. 

  ![std-overlay](Images/std-overlay.png)

* Because Harold's company is looking to invest long-term in NFLX, the `SMA100` and `STD100` should hold more emphasis. Based on the chart overlays, although there is a recent price uptrend in late 2018, long-term volatility has been high for the entirety of 2018 to 2019. Therefore, it may best to hold off on investing in NFLX long-term for now.