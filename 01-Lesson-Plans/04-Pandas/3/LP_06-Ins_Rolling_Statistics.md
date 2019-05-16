### 6. Instructor Do: Rolling Statistics (10 mins)

**Files:**

* [rolling_statistics.ipynb](Activities/06-Ins_Rolling_Statistics/Solved/rolling_statistics.ipynb)

Walk through the solution and explain the following:

* What is a rolling statistic?

  > A rolling statistic is a metric calculated over the range of a shifting (or rolling) window. For example, a 7-day rolling mean of 14 days worth of closing prices for a stock would calculate the mean of the closing prices for days `1-7`, then days `2-8`, then days `3-9`, and so on...

* Why use a rolling statistic?

  > A rolling statistics helps to show the progression or change of a particular metric over time. For example, calculating the average closing price of 1 year's worth of stock data will output a single metric, the average closing price for the year. On the contrary, a rolling 7-day mean will give you the change in weekly average closing prices over the course of the year.

* Rolling statistics tend to smooth out the trend of the initial dataset, allowing for more general or holistic analysis of a dataset rather than focusing on every twist and turn of the data. Overlaying a rolling statistic trend on top of the original data trend makes this feature easier to spot.

  ![rolling-statistic-overaly](Images/rolling-statistic-overlay.png)

* Rolling statistics factor in the progression of time. Therefore, a rolling 7-day window makes sense when looking at a short-term weekly investment scope; however, if investing for the long-term a rolling-180 day window might make more sense.

* Sometimes comparing different scopes of time can reveal insights that would not have been found otherwise. For example, comparing the 30-day rolling standard deviation to the 180-day rolling standard deviation of TSLA stock shows that although on a monthly scale there was a spike in volatility in late 2018, overall on a 6-month scale the highest spike in volatility was in late 2016, where the stock skyrocketed (remember standard deviation/volatility is how far data points deviate from the mean, this does not always necessarily have to be negative).

  ![daily-close-tsla](Imagas/daily-close-tsla.png)

  ![rolling-std-dev-30](Images/rolling-std-dev-30.png)

  ![rolling-std-dev-180](Images/rolling-std-dev-180.png)

