### Instructor Do: Hodrick-Prescott Filter (0:10)

* For this activity, you will need your IEX API key. If you do not have one, use the `IVV.csv` file, which contains the same data.

* Explain that this activity will be a demonstration of a mathematical transformation of time series data called the Hodrick-Prescott filter.

  * It is used to separate short-term fluctations, such as ones that occur daily, from longer-term trends.

  * It decomposes a time series into trend and non-trend components.

* Open the [notebook](tbd) and describe the dataset:

  * The data tracks the closing price during a two-year period of IVV, an exchange-traded fund (ETF) that tracks the S&P 500 index.

  ![Images/hp02.png](Images/hp02.png)

* Briefly explain the overall mathematical idea of the Hodrick-Prescott filter (Slide tbd):

  ![Images/hp01.png](Images/hp01.png)

  * It is a function that minimizes the sum of two values.

  * As seen previously, a time series can be decomposed into trend, seasonality, and noise.

  * If we temporarily disregard noise, then, time series data minus trend equals the seasonality.

  * The left side describes the cyclic element: time series (y) minus trend (tau).

  * The right side basically describes the volatility in trend.

  * The H-P filter essentially minimizes the aggregate values associated with trends and non-trends.

* Next, explain the Python  code used to run the Hodrick-Prescott filter:

  ```python
  import statsmodels.api as sm
  ts_noise, ts_trend = sm.tsa.filters.hpfilter(df['close'])
  ```

  * It is a module from the `statsmodels` library.

  * The `hpfilter()` function separates a column of closing prices into trend and noise (non-trend).

  * The code is much simpler than the mathematical description!

* Finally, show the plots of the trend and noise components after filtering:

  ![Images/hp03.png](Images/hp03.png)

  ![Images/hp04.png](Images/hp04.png)

  * The first plot shows the trend, which is considerably smoother than the raw time series data.

  * The second plot shows the noise (non-trend) that has been filtered out.
