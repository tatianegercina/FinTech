### Instructor Do: Moving Averages and Exponentially Weighted Moving Averages (0:15)

* Recapitulate for the class that we have learned about the components of time series data--trend, seasonality, and noise.

* Inform your students that we will now focus on some techniques to reduce noise in order to identify patterns such as trends and periodicity.

* Open the [notebook](tbd), whose first data frame contains the liquor sales data that we just saw.

  ![Images/ma01.png](Images/ma01.png)

  * As we have seen, there is quite a bit of fluctuation, as well as some noise.

* Explain that the moving average, also called the rolling average, is a method to filter out noise.

  * Each value is the **average** of a certain number of values that come before it.

* Demonstrate the example in the notebook:

  ```python
  df['liquor_sales'].rolling(window=12).mean().plot()
  ```

  * pandas provides a `rolling()` method, used in conjunction with `mean()` method here, to calculate the moving average of the data set.

  * The `window` argument specifies the number of previous values that are averaged in a rolling average. Here, it is 12.

  * Each value that is plotted is the average of the values of the 12 previous months.

  * The noise in the plot of the rolling average is considerably more attenuated. The upward trend of liquor sales over the years is much more clearly outlined here.

  ![Images/ma02.png](Images/ma02.png)

* Explain that one of the potential drawbacks of rolling averages is that the observations are lagged:

  ![Images/ma03.png](Images/ma03.png)

  * Because the window is 12, the first 11 rows are NaN values.

* Next, explain that the Exponentially Weighted Moving Average is a similar technique to smooth out data and filter noise.

  * It is also called the Exponential Moving Average.

* Explain the principal difference between moving averages and EWMAs.

  * In a moving average, all values inside a window have equal weight.

  * For example, in the liquor sales example, the window was 12, and in calculating the moving average of a given month, all 12 months weigh equally.

  * In an EWMA, on the other hand, recent values carry more weight than values from a more distant past.

  * This strategy may better capture trends than a simple moving average.

* Illustrate the example of EWMA in the notebook:

  ![Images/ma04.png](Images/ma04.png)

  * Here, the dataset used is of Microsoft Stock price data over a number of years.

  * This plotting of the original, unweighted data shows a fair amount of volatility.

* Explain that here, too, a pandas method exists to calculate the EWMA.

  ```python
  msft.ewm(halflife=15).mean().plot()
  ```

* Explain that the `halflife` argument dictates how quickly the weighting of past value decreases as you go further back in dates. The first plot has a half-life of 15 data points, and the second a half-life of 60.

  ![Images/ma05.png](Images/ma05.png)

  ![Images/ma06.png](Images/ma06.png)

  * The first plot smoothes the data considerably more than the raw data, but the second one even more so.
