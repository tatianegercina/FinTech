# 10.2 Lesson Plan: ARMA Virumque

### Overview

Today's class is the heart of this unit. Students will be introduced to core concepts such as stationarity and autocorrelation. They will also learn to use time series models such as ARMA and ARIMA to create forecasts. They will also begin thinking about parsimony as they learn to estimate the order of a model.

### Class Objectives

By the end of this class, students will be able to:

* Quantify the accuracy of a linear regression model.

* Perform auto-correlation on time series data.

* Determine stationarity of a time series.

* Create an ARMA model to forecast financial data.

* Create an ARIMA model to forecast financial data.

* Use ACF and PACF plots to estimate the order of ARMA and ARIMA models.

* Explain the significance of Akaike Information Criterion and Bayesian Information Criterion in assessing statistical models.

- - -

### Instructor Notes

* Today's class is the most challenging in this unit. Starting with the concept of auto-correlation, students will build on previous skills and ideas as they progress through the day. Some of these ideas are counterintuitive. However, they will gain repeated exposure to them from one activity to the next. A major goal for today's class, then, is for students to gain confidence through the process of working through fairly challenging material through multiple exposures.

* Be mindful that because the each activity is a pre-requisite for the next, today's class may call for greater patience from both instructor and students. Do not rush through activities, and take the time to explain the core concepts and techniques in detail if necessary.

* Due to the sheer volume of material covered, the discussion of ACF and PACF plots, as well as AIC and BIC, in determining a model's order has been deferred until ARIMA. However, feel free to discuss it more fully during ARMA at your discretion.

* While it is likely that some students may not fully grasp all of today's material by the end of class, the payoff will be in day 3, when your students will have a chance to create predictive models from start to end.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

In this section, you will give a broad overview of today's class.

Welcome students to the second day of the time series unit, and briefly summarize key concepts from day 1:

* A time series can be decomposed into components such as trend, noise, and seasonality.

* Tools such as the Hodrick-Prescott filter, and EWMA can be used to identify trends in a time series.

* Linear regression can be a powerful tool used to describe and predict data.

Describe to students what they will be learning today:

* They will learn to quantify the accuracy of a linear regression model.

* They will learn to use processes to make a time series easier to model.

* They will learn to use powerful time series models, ARMA and ARIMA, to forecast financial data.

* They will encounter the concept of parsimony in models, an important idea in machine learning.

### 2. Instructor Do: Error, Accuracy, and Metrics (10 min)

In this activity, we will discuss quantifying a linear regression model: how accurately it describes the data.

**File:**

* [time_series_simple_regression.ipynb](Activities/01-Ins_Error_Accuracy_Metrics/Solved/time_series_simple_regression.ipynb)


Open the slideshow and recapitulate the linear regression plot below, which we have seen previously:

  ![Images/error01.png](Images/error01.png)

* The blue dots are a scatter plot of data points (years of experience vs salary).

* The red line is the best fit line. It represents the linear regression model.

* The distance between each data point and the best fit line is referred to as the error.

Explain that the linear regression model is mathematically constructed to **minimize** the the sum of all the errors after they have been squared (Slide 4).

  ![Images/error01.jpg](Images/error02.jpg)

Explain that one way to assess the accuracy of a linear regression model is to look at the errors:

* The **mean squared error**, or **MSE**, as the name states, is the average of the square of the errors of the dataset. It is the variance of the errors in the dataset.

* The **root mean square error**, or **RMSE**, is simply the square root of the MSE. It is therefore the standard deviation of the errors in the dataset.

* Lower MSE and RMSE scores, of course, indicate a more accurate model.

Explain that R2, or r-square, is a way to assess the relationship between two variables.

* The correlation coefficient is a numerical description of the extent to which the two variables move  together. It ranges from -1 to 1.

* **R2**, or **r-square value**, is simply the square of the correlation coefficient. It describes the extent to which a change in one variable is associated with the change in the other variable. It ranges from 0 to 1.

Having explained the general concepts, go over the code implementations of these metrics. Open the notebook and walk through the code:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  import numpy as np

  score = model.score(X_binary_encoded, y)
  r2 = r2_score(y, predictions)
  mse = mean_squared_error(y, predictions)
  rmse = np.sqrt(mse)
  np.std(y)
  ```

* After importing the pertinent `sklearn` modules, the R2, MSE, and RMSE are calculated.

* The RMSE is simply the square root of the mean squared error. A lower RMSE score (near 0) is ideal and means the model is fit well to the data.

Explain that you can also compare the RMSE to the standard deviation to get a better feel for the model fit.

* Ideally, the RMSE will not exceed the standard deviation of the temperature data.

* The standard deviation of the temperature, calculated by `np.std()`, is 3.84.

* The RMSE, or the standard deviation of the error, is 6.38.

* The RMSE exceeds the standard deviation, indicating that the model may not be very helpful. In other words, on average there are wider swings in the error than the measured temperatures.

### 3. Students Do: Regression Metrics (10 min)

**Files:**

* [README.md](Activities/02-Stu_Error_Accuracy_Metrics/README.md)

* [starter.ipynb](Activities/02-Stu_Error_Accuracy_Metrics/Unsolved/metrics.ipynb)

* [oil_futures.csv](Activities/02-Stu_Error_Accuracy_Metrics/Resources/oil_futures.csv)

### 4. Instructor Do: Review Activity (5 min)

**Files:**

* [metrics.ipynb](Activities/02-Stu_Error_Accuracy_Metrics/Solved/metrics.ipynb)

Open the solution notebook and explain the following:

  ```python
  df['Return'] = returns.copy()
  df['Lagged_Return'] = returns.shift()
  ```

  * Lagged Returns are used to associate a date with its returns. The goal of this assignment is to use the week of year data to predict the returns.


  ```python
  X['Week_of_year'] = X.index.weekofyear
  X_binary_encoded = pd.get_dummies(X, columns=['Week_of_year'])
  ```

  * The features are created by using the `weekofyear` attribute of the index. Because the index is a DateTimeIndex, the index can be transformed into other time periods such as weekly.

  ```
  y = df['Return']
  ```

  * The prediction target will be the returns.

  ```python
  model = LinearRegression()
  model.fit(X_binary_encoded, y)
  ```

  * A `LinearRegression` model is fit to the data. This model will attempt to use the week of year inputs to predict the returns.

Highlight the salient features of the error metrics:

* R2: An r-square value of 0.2 An interpretation of R2 is not always straight forward, can be misleading in isolation. With that caveat, 0.2 can be a robust value in financial contexts.

* The MSE is 2.986 and the RMSE (the square root of MSE) is 1.72. The RMSE is lower than the standard deviation of returns (1.93), indicating the standard deviation of errors is smaller than that of the raw data.

Ask for any remaining questions before moving on.

### 5. Instructor Do: Auto Correlation (15 min)

**File:**

  * [autocorrelation.ipynb](Activities/03-Ins_Auto_Correlation/Solved/autocorrelation.ipynb)

Open the notebook and briefly describe the data set:

  ![Images/ac01.png](Images/ac01.png)

  * The data set is the familiar weather data.

  * The temperature readings are hourly.

  * Each hourly reading is fairly close to that of the previous hour.

Introduce the concept of auto correlation:

  * Up to this point, when dealing with linear regression, we have tried to identify the relationship between two unrelated variables, such as date vs. weather, or years of experience vs. salary.

  * Auto correlation, on the other hand, determines to what extent, for example, today's values correlate with yesterday's values.

To illustrate auto correlation, explain to students that the `Lag_Temperature` column is the result of shifting the `Temperature` column down by one:

  ![Images/ac02.png](Images/ac02.png)

  * The temperature value from the first row is found in the `Lag_Temperature` column in the second row, for example.

  * The temperature data has been shifted down by one time period--in this case an hour.

  * The temperature from one hour to the next changes in relatively small increments.

  * Auto correlation, again, is a measure of how closely current values correlate with past values.

Show the plot of the temperature data versus a lagged copy of itself:

  ![Images/ac06.png](Images/ac06.png)

  * In this case, there appears to be an extremely close relationship.

  * In other words, a temperature reading is close in value to the reading from an hour earlier.

Now show the plotting of temperature over a 48-hour period, with the following observations:

  ![Images/ac03.png](Images/ac03.png)

  * The temperature, predictably, shows a cyclical pattern.

  * Despite significant swings seen in a day, the temperature change between one hour to the next is fairly small.

  * For a given temperature reading, say 6 am on January 1st, the most similar temperature reading is seen again 24 hours later.

You may wish to draw on the following scenario to further illustrate autocorrelation:

  * A pair of dice is thrown every minute. Their combined value and the time are recorded.

  * Since it is a random activity, there will not be a strong relationship between the current value of the dice and the preceding one. Here, the auto correlation will not be significant.

Next, explain the code used to calculate the auto correlation:

  ```python
  df.Temperature.autocorr(lag=1)
  ```

  * The `autocorr()` method here returns the autocorrelation of the `Temperature` column against a lagged copy of itself.

  * Here, the lag is 1, meaning that the series of temperature readings is correlated against a series of temperature readings taken one hour previously.

  * The correlation coefficient is 0.99, a very high number.

Explain that auto correlation can be computed at a different lag

  ```python
  df.Temperature.autocorr(lag=24)
  ```

  * Here, each temperature reading is autocorrelated with a temperature reading 24 hours later.

  * As expected, the auto correlation is very high at a lag of 24 as well.

Once again, if necessary, remind your students that auto correlation is simply the correlation of current data with past data.

Explain that the `plot_acf()` function visualizes what we have discussed so far:

  ```python
  sm.graphics.tsaplots.plot_acf(df.Temperature, lags=48)
  ```

  ![Images/ac04.png](Images/ac04.png)

  * The plot nicely illustrates the periodicity of daily temperature patterns.

  * This plot, in other words, shows autocorrelation at lags up to 48, which was specified in the argument `lags=48`.

  * As pointed out previously, there is high auto correlation at a lag of 1, slightly lower at lag 2, and so on. Then a high auto correlation is found at a lag of 24, and multiples of 24, such as 48.

Next, explain that the band in light blue is the confidence interval.

  * By default, the CI is set to 95%.

  * In other words, if the data set were noisy, and there's no meaningful auto correlation, there is 5% chance that the auto correlation at a particular lag would be found outside the CI band by random chance.

  * In this case, the auto correlation at all specified lags are outside the CI band, indicating a high likelihood that the auto correlation at each interval is **not** a random fluke.

  * As lag time increases, the CI band widens. This makes intuitive sense: as lag is increased, more potential for noise is introduced, and the statistical burden of proof is higher.

Next, introduce partial auto correlation functions:

  * The idea of PACF is different from auto correlation function.

  * Whereas an auto correlation function measures auto correlation at all specified lags, PACF essentially reduces components of auto correlation that are explained by previous lags. The effect is that it gives heavier weight to lags that have components that are not explained by earlier lags.

Explain that a PACF plot will illustrate the idea in concrete terms:

  ```python
  sm.graphics.tsaplots.plot_pacf(df.Temperature, lags=48, zero=False)
  ```

  ![Images/ac05.png](Images/ac05.png)

  * The `plot_pacf()` function creates a PACF plot with the same temperature data.

  * In the PACF plot, there are significant lags at 1, 2, and 24 hours.

  * The PACF estimates that lags at 1, 2, and 24 hours account for the other lags.

  * In other words, PACF answers the question, if there's already one lag that has been identified as being significant, will the data be better explained by flagging a second lag as significant?

  * In the ACF, there was high auto correlation at lags of 24 and 48 hours. This makes sense, as the temperature at the same time across three days would be expected to be very similar.

  * In the PACF, however, we do not see a high partial auto correlation at a lag fo 48 hours, since that can be explained by the lag at 24 hours.

Finally, summarize the key points of the activity:

  * Autocorrelation is a measure of high closely current values are correlated with past values.

  * In the activities to come, ACF and PACF will help us select the correct **order** of models for forecasting.

  * Doing so requires an understanding of how current values are affected by past values.

### 6. Students Do: Euro ETFs (10 min)

In this activity, students will examine a time series of bid-ask spreads of an ETF for autocorrelation.

**Files:**

* [README.md](Activities/04-Stu_ETF/README.md)

* [high_frequency_euro_ETF_bid_ask_spreads.csv](Activities/04-Stu_ETF/Resources/high_frequency_euro_ETF_bid_ask_spreads.csv)

* [autocorrelation.ipynb](Activities/04-Stu_ETF/Unsolved/autocorrelation.ipynb)

### 7. Instructor Do: Review Activity (5 min)

**File:**

* [autocorrelation.ipynb](Activities/04-Stu_ETF/Solved/autocorrelation.ipynb)

Walk through the solution code:

  ```python
  df=df.resample('10S').mean().dropna()
  df.bid_ask_spread.autocorr(1)
  ```

  * The bid-ask spread data is sampled at a 10-second interval, and NaN values are dropped.

  * The autocorrelation at a lag of 1 is 0.136.

Review the ACF and PACF plots:

  ```python
  from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
  plot_acf(df['bid_ask_spread'], lags=30, zero=False)
  plot_pacf(df['bid_ask_spread'], lags=30, zero=False)
  ```

  ![Images/etf01.png](Images/etf01.png)

  ![Images/etf02.png](Images/etf02.png)

  * The ACF and PACF plots here have a similar appearance, although that is not always the case.

  * The ACF and PACF both appear to be significant at a lag of 1.

### 8. Instructor Do: Stationarity and Non-Stationarity (10 min)

In this activity, you will define stationarity, a key concept in time series modeling.

Open slide 6 and introduce the term `stationarity`:

  * In a stationary process, statistical properties such as the mean and variance do not vary across time.

  * In other words, the mean and variance in one section in the time series should not differ significantly from the mean and variance in another.

  * A time series that exhibits a trend is therefore non-stationary.

Demonstrate a non-stationary time series:

  ![Images/stat01.png](Images/stat01.png)

  * It displays the stock price of a company over time.

  * It shows an upward trend and is therefore non-stationary.

Demonstrate a stationary time series:

  ![Images/stat02.png](Images/stat02.png)

  * The mean is constant over time.

Explain that stationary is important for the following reasons:

  * Many time series models assume stationarity, though some do not.

  * Knowing whether a process is stationary or non-stationary will help us determine which model to use. For example, ARMA models assume stationarity. ARIMA models, on the other hand, assume non-stationarity. We will encounter both of these models today.

Explain the importance of stationarity in time series modeling:

  * Stationary processes are easier to model.

  * A non-stationary process, on the other hand, is more difficult to model because its statistical properties vary across time.

Explain that a non-stationary time series can sometimes be made stationary with appropriate transformations.

  * The pair of non-stationary processes seen earlier, in fact, are from the same time series.

  * The stock price plot exhibited an upward trend.

  * Since stock prices tend to auto-correlate, plotting the difference of the price from one time point to the next yielded a stationary series.

  * Making a time series stationary stabilizes variables across time.

Open the notebook and show the code to convert from a non-stationary dataset to a stationary dataset.

  ```python
  from statsmodels.tsa.stattools import adfuller
  adfuller(data.Yield)
  ```

  * The Augmented Dickey-Fuller tests for stationarity. It's a quick statistical test to tell you if a series is stationary or not.

  * The p-value is the second value in the output. A p-value less than 0.05 means that the series is stationary.

  ```python
  df['Returns'] = df.Close.pct_change()
  ```

  * pct_change() is another was to make a series stationary. The difference between diff() is that pct_change() essentially normalizes the data (_i.e., with the denominator doing the scaling_).


  ```python
  df['Diff'] = df.Close.diff()
  ```

  * Diff() subtracts out this upward trend, and can often be an easy way to make a series stationary.


### 9. Students Do: Stationarity (15 min)

In this activity, students will perform techniques to stationarize a non-stationary time series.

**Files:**

  * [README.md](Activities/05-Stu_Stationarity/README.md)

  * [amazon.csv](Activities/05-Stu_Stationarity/Resources/amazon.csv)

  * [stationarity.ipynb](Activities/05-Stu_Stationarity/Unsolved/stationarity.ipynb)

### 10. Instructor Do: Review Activity (5 min)

**Files:**

  * [stationarity.ipynb](Activities/05-Stu_Stationarity/Solved/stationarity.ipynb)

Show the initial plot of Amazon's closing prices, and explain that this time series is non-stationary.

  ![Images/stationarity01.png](Images/stationarity01.png)

  * It shows an obvious upward trend which indicates non-stationary data, but we can also use the Augmented Dickey-Fuller test to verify. In this case, a p-value of 0.449 indicates non-stationary data.

Walk through the first part of the code, in which the diffs are plotted:

  ```python
  df['Diff'] = df.Close.diff()
  df = df.dropna()
  df.Diff.plot()
  ```

  * The `diff()` method calculates the differences in stock prices from one day to the next.

  * NaN values are dropped, and the column is plotted.

  ![Images/stationarity02.png](Images/stationarity02.png)

  * The series is not quite perfectly stationary. The right side of the plot (between May and November in 2011) shows higher variance.

Walk through the next transformation:

  ```python
  df['Returns'] = df.Close.pct_change()
  df = df.dropna()
  df.Returns.plot()
  ```

  ![Images/stationarity03.png](Images/stationarity03.png)

  * The stock price returns are calculated with the `pct_change()` method.

  * After the transformation, the series does appear more stationary than the previous example.

Walk through the final transformation:

  ```python
  df2 = df[df['Diff'] != 0]
  df2 = df2.replace(np.inf, np.nan).replace(-np.inf, np.nan)
  df2 = df2.dropna()

  df2['Log'] = np.log(df2['Diff'])
  df2 = df2.dropna()
  df2['Log'].plot()
  ```

  * All zero values are filtered out from the `Diff` column.

  * All infinity values are converted to NaNs, then dropped.

  * The logarithm of the `Diff` column is taken, and NaNs are dropped again.

  ![Images/stationarity04.png](Images/stationarity04.png)

  * The resulting series appears to be stationary.

Summarize the key points and procedures of this activity:

  * A time series can be made stationary by a variety of techniques.

  * Which technique to use can often be determined by examining the non-stationary plot.

  * NaN and infinity values must be dropped along the way.

### 11. Instructor Do: Auto-Regressive Moving Average Model (15 min)

Before diving into ARMA, quickly summarize auto-correlation for the class:

  * Auto-correlation is simply seeing to how well a time series correlates with a lagged copy of itself at a specified lag interval.

  * For example, if we have a week's worth of data, the value from each day would be matched up with the value from the previous day, and the two series would be mathematically correlated.

  * The main idea, again, is to determine how well past values correlate with future values at a specified lag, whether 1 or another lag period. Financial data, such as stock prices, often auto-correlate best at a lag of 1, but that is not always the case.

  * Plotting partial auto-correlation helps identify the **number** of lags that are significant in explaining the data.

Open slide 11 and introduce the concept of auto-regressive (AR) modeling:

  * In an AR model, past values are used to predict future values.

  * An AR model therefore assumes some degree of auto-correlation.

	  * An AR model may have one significant lag, or it may have multiple.

Explain the relationship between an AR model and a linear regression model:

  * An AR model **is** a linear regression model.

  * In an example of a linear regression model, the number of rooms in houses may be used to predict house prices.

  * In an example of an AR model, the past prices of a stock may be used to predict future prices.

Explain the elements of the autoregression model (Slide 13):

  ![Images/arma01.gif](Images/arma01.gif)

  * If we're dealing with stock prices, the term on the left, `y` at time `t`, is the current price. In other words, it is the value of the stock price at time `t`.

  * The first term on the right, the letter mu, is simply the mean of the time series.

  * In the next term on the right, the `alpha` is a coefficient that is multiplied by the second term. The second term is the past stock price at `t-1`.

  * The `epsilon` at time `t`, the final term in the equation, is the error, or noise, at time `t`.

  * This particular equation assumes a first order. That is, it assumes that there is only one significant lag.

  * It also assumes a lag of 1, seen from the term `t-1`.

Explain that in a second order AR model, where two significant lags are assumed, an `alpha 2` multiplied by `y` at `t-2` would be added to the above equation.

  ![Images/arma02.gif](Images/arma02.gif)

  * In this case, the second lag is assumed to be 2. If it were at 5 periods, the lag would be `t-5`.

  * Again, this second order model assumes that the present value is determined by past values at two different lag points.

* Now that we've gone over the equation, ask your students to focus on the larger picture:

  * An AR model predicts future values based on past values at a specified lag, and the number of significant lags.

Next, explain the features of an MA model:

  ![Images/arma03.gif](Images/arma03.gif)

  * Here, the `m` is the mean of the time series.

  * `epsilon` at `t-1` is the noise, or error, at time `t-1`, or in other words, at a specified lag before the current value.

  * `epsilon` at `t` is the noise, or error, at time `t`.

Contrast the MA model with the AR model:

  * In an AR model, past values (plus error) are used to predict future values.

  * In an MA model, past errors (plus current error) are used to predict future values. In other words, it is a form of error correction.

* Emphasize that a MA model is **not** the same thing as a moving/rolling average that we discussed previously.

  * In a moving average, each value is the average of a number of previous values. It does not take into account the error at each time point.

  * In an MA model, both past and current errors are used to estimate the current value.

Explain that an ARMA model simply combines the features of the AR and MA models.

Ask your students to identify the features of the ARMA model:

  ![Images/arma04.gif](Images/arma04.gif)

  * On the left side of the equation, `y` at time `t`, is the current value.

  * The first term on the right side, `mu`, is added to `alpha 1` `y` at time `t-1`, is from the AR model. It is a past (lagged) value times a coefficient.

  * The next term, `m``epsilon` at time `t-1`, is the mean of the time series multiplied by the error (epsilon) at time `t-1`.

  * The final term, `epsilon` at time `t`, is the error of the current value.

Reiterate that, despite the possibly intimidating mathematical formula, the idea behind the ARMA model is simple:

  * Past values and past errors are used to predict future values.

- - -
### 12. BREAK (15 min)
- - -

### 13. Instructor Do: ARMA in Practice (10 min)

**File:**

  * [ARMA.ipynb](Activities/06-Ins_ARMA/Solved/ARMA.ipynb)

Now that we have a theoretical understanding of the ARMA model, explain that we will go over using it in Python.

Open the notebook.

  * This is a dataset of NASDAQ stock prices from 2012 to 2019.

Display the plot and ask the class whether the time series is stationary:

  ![Images/arma_model01.png](Images/arma_model01.png)

  * It is non-stationary. The mean is not stable through the series, nor the variance.

Explain that an ARMA model requires a stationary time series.

  * Later today, we'll cover a model for non-stationary series.

Ask the class how one might transform this time series to be stationary:

  * Some strategies that we have discussed include taking the difference between each row and the previous one. This is applicable when the auto-correlation is high at lag 1.

  * Another related idea is to calculate the return.

  * An exponential time series can be made stationary by taking the logarithm.

Explain that here, we're stationarizing the time series by calculating the return.

  ```python
  df['Return'] = df['Close'].pct_change()
  returns = df['Return'].dropna()
  ```

  * The pandas function `pct_change()` calculates the returns, and NaN values are subsequently dropped.

Show the transformed series, and ask the class whether it is stationary.

  ```python
  returns.plot()
  ```

  ![Images/arma_model02.png](Images/arma_model02.png)

  * The mean of the series is relatively stable over time, and the series appears to be stationary.

Having stationarized the data, explain that creating an ARMA model itself is simple:

  ```python
  from statsmodels.tsa.arima_model import ARMA
  model = ARMA(returns, order=(1,1))
  results = model.fit()
  ```

  * After importing the module, a model is defined with the `ARMA()` method, then fit to the data.

Explain the arguments of the `ARMA()` method:

  * `returns`, as seen before, is the transformed Amazon stock closing prices.

  * `order=(1,1)` means that this is an ARMA model with a first-order AR component (AR1), and a first-order MA component (MA1).

  * In other words, an ARMA model means that the data is best explained by both an AR component (past values), and an MA component (past errors).

  * The order refers to the number of lags that are significant for the AR component, and for the MA component.

  * Since the order is (1,1), this particular model assumes that there is one significant lag for both AR and MA components.

Explain that here, the ARMA order was chosen somewhat arbitrarily, but that selecting it is an important part of using this model.

  * We will cover selecting the order in the next activity.

Explain that the model's `forecast()` method can be used to make predictions:

  ```python
  pd.DataFrame(results.forecast(steps=10)[0]).plot(title="Stock Returns Forecast")
  ```

  ![Images/arma_model04.png](Images/arma_model04.png)

  * The `steps=10` argument specifies two weeks (ten trading days) as the interval of prediction.

  * The predicted values (in this case, stock returns) are formatted as a dataframe and plotted.

Finally, highlight a few important features of the model's summary:

  ```python
  results.summary()
  ```

  * The p-value of the first lag is low at 0.012.

  * The AIC and BIC values should also be noted, lower values reflecting better accuracy. We will cover these values in greater detail later today.

### 14. Students Do: Yields (10 min)

In this activity, students will create an ARMA model on yield data.

**Files:**

  * [README.md](Activities/07-Stu_ARMA/README.md)

  * [yield.csv](Activities/07-Stu_ARMA/Resources/yield.csv)

### 15. Instructor Do: Review Activity (5 min)

**File:**

  * [yields.ipynb](Activities/07-Stu_ARMA/Solved/yields.ipynb)

Open the notebook and show the plot of the data:

  ![Images/yields01.png](Images/yields01.png)

  ```python
  from statsmodels.tsa.stattools import adfuller
  adfuller(data.Yield)
  ```

  * Because the trends are not obvious, the adfuller test can be used to determine stationarity.

  * In this example, the p-value is 0.011 (less than 0.05), suggesting stationarity.

 * In addition to the Dickey-Fuller test, since the data appears visually to not have a consistent upward or downward trend, this also suggests stationarity. Because of that, we will try modeling the series without further transformations.

Next, display the ACF plot and comment on the pattern:

  ![Images/yields02.png](Images/yields02.png)

  * There appears to be high autocorrelation that gradually declines.

  * The autocorrelation points all exceed the 95% confidence interval band.

Display the PACF plot:

  ![Images/yields03.png](Images/yields03.png)

  * This plot suggests two significant lags, possibly more.

  * The number of significant lags will affect the order of the ARMA model.

  * In this case, we may want to specify two as the number of lags, because the PACF is showing that the first two lags are significant.

Explain the code used to create the model:

  ```python
  from statsmodels.tsa.arima_model import ARMA
  model = ARMA(data.values, order=(2, 2))
  result = model.fit()
  result.summary()
  ```

  * Other than the order numbers, the code is boiler plate.

  * In `order=(2, 2)`, the first number denotes the AR order, and the second number denotes the MA order.

Discuss the summary of the results:

  * The p-values are all less than 0.05, suggesting a good fit.

Explain that the model can be used to make predictions:

  ```python
  pd.DataFrame(result.forecast(steps=5)[0]).plot(title="Yield Forecast")
  ```

  ![Images/yields5.png](Images/yields05.png)

  * The `forecast()` method is used here to predict yield values for the next 5 days.

### 16. Instructor Do: ARIMA (15 mins)

In this activity, in addition to describing the ARIMA model, you will elucidate the use of ACF and PACF plots, as well as AIC and BIC, in identifying the order of an ARIMA model.

**File:**

  * [ARIMA.ipynb](Activities/08-Ins_ARIMA/Solved/ARIMA.ipynb)

Open the notebook and describe the dataset:

  ![Images/ARIMA01.png](Images/ARIMA01.png)

  * It is a time series of the number of airline passengers from 1949 through 1960.

  * There is a pronounced upward trend. The time series is therefore non-stationary.

Ask the class whether **ARMA** would be a suitable model for this dataset:

  * **Answer:** No, it would not. There is a pronounced upward trend, and ARMA models assume stationarity.

Explain that, unlike an ARMA model, an **ARIMA** model stationarizes a non-stationary time series.

  * Specifically, it stationarizes a time series by differencing it. In pandas, we have differenced with the `diff()` method.

  * The stationarizing step is the key difference between ARMA and ARIMA. It is possible to stationarize a time series manually, as we have done before. But ARIMA automates the process.

Describe the ACF and PACF plots:

  ![Images/ARIMA02.png](Images/ARIMA02.png)

  * In the ACF plot, significant autocorrelation exists, with a blip at the 12th lag. This makes sense, as this is a monthly time series, and the lag at 12 accounts for seasonal traffic patterns in the data.

  ![Images/ARIMA03.png](Images/ARIMA03.png)

  * In the PACF plot, there appear to be at least two significant lags, at 1 and 2. The 12th lag also seems significant.

Explain the significance of ACF and PACF plots in estimating the order of the ARIMA model:

  * Up to this point, students were given AR and MA orders, but the ACF and PACF plots can be useful tools in identifying the order of ARMA and ARIMA models.

  * A general rule of thumb is to use the PACF to estimate the AR order. In this example, there appear to be between 2 and 8 lags that exceed the confidence interval. It is reasonable to settle on 2 as the AR order, as the first two lags significantly stand out from the rest.

  * Similarly, the ACF can be used to estimate the MA order. In this example, the first two lags also appear to be significant in the ACF.

  * We might like to capture the 12th lag to, but that will require a model that's a little more advanced ("Seasonal" ARIMA) than what we'll cover in this activity.

Walk through the code used to create an ARIMA model:

  ```python
  from statsmodels.tsa.arima_model import ARIMA
  model = ARIMA(df['NumberPassengers'], order=(2, 1, 2))
  results = model.fit()
  results.summary()
  ```

  * The code is nearly identical to that of an ARMA model.

  * In the `ARIMA()` function, the `order` argument is 2, 1, 2. The order refers to AR, diff, and MA components.

  * As discussed above, the AR and MA orders are 2 and 2.

  * The number in the middle refers to the order of differencing. In other words, it refers to the number of times a time series has been differenced. In this example, if `df['Passengers']` were differenced once, then differenced again to achieve stationarity, this number would be 2.

  * An ARIMA model in which the differencing order is zero is therefore an ARMA model. For example, an ARIMA model with an order of (1, 0, 1) is an ARMA model of an order of (1, 1).

Open slide 20 and explain the interpretation of AIC and BIC:

  * AIC stands for Akaike Information Criterion. BIC stands for Bayesian Information Criterion.

  * Both of these metrics estimate the quality of a model.

  * They weigh goodness of fit against the number of parameters. In other words, AIC and BIC favor the simplest model that best fit the data.

  * This means that they penalize models with a large number of parameters. A model with a large number of parameters may describe that particular dataset well, but may lose its predictive power when used on new data.

  * In this example, we have two models with orders of (2,1,2) and (2,1,4). Because each additional lag adds a variable to the model, AIC and BIC penalize the model with a higher order.

  * Lower AIC and BIC values are generally better.

Discuss the AIC and BIC found in the model summaries:

  ![Images/ARIMA04.png](Images/ARIMA04.png)

  * In the model with the (2, 1, 2) order, the AIC and BIC are 1344.04 and 1261.82.

  ![Images/ARIMA05.png](Images/ARIMA05.png)

  * In the (2, 1, 4) model, the AIC is slightly lower, and BIC slightly higher.

  * Because the first model achieves similar results at a lower order, it is reasonable to favor this model order over the second.

Take a moment to summarize the order of an ARIMA model:

  * The ACF and PACF plots can be used in conjunction with AIC and BIC scores to identify the model order.

  * AIC and BIC favor models with the best fit, and penalize higher order models for their complexity.

  * Lower AIC and BIC scores are usually better.

  * These quantities can also be used to estimate the order of an ARMA model. An ARMA model, however, does not have a differencing order, because it assumes that the time series is stationary and therefore doesn't need to be differenced.

Send the following link to students for more information on the order of an ARIMA model:

  * [https://people.duke.edu/~rnau/arimrule.htm](https://people.duke.edu/~rnau/arimrule.htm).

### 17. Students Do: An ARIMA and a Leg (15 min)

**Files:**

  * [README.md](Activities/09-Stu_ARIMA_Leg/README.md)

  * [oil_futures_front.csv](Activities/09-Stu_ARIMA_Leg/Resources/oil_futures_front.csv)

  * [stu_ARIMA.ipynb](Activities/09-Stu_ARIMA_Leg/Unsolved/stu_ARIMA.ipynb)

### 18. Instructor Do: Review Activity (5 min)

**File:**

* [stu_ARIMA.ipynb](Activities/09-Stu_ARIMA_Leg/Solved/stu_ARIMA.ipynb)

Open the notebook and explain the rationale for using ARIMA:

  ![Images/stu_ARIMA02.png](Images/stu_ARIMA02.png)

  ![Images/stu_ARIMA01.png](Images/stu_ARIMA01.png)

  * Since it is non-stationary, and using the difference daily prices of the series converts it to stationary, we can use **ARIMA** on the price series directly.

Describe the lag patterns seen in ACF and PACF plots:

  ![Images/stu_ARIMA03.png](Images/stu_ARIMA03.png)

  ![Images/stu_ARIMA04.png](Images/stu_ARIMA04.png)

  * The ACF appears to have a number of significant lags that slowly decline in importance.

  * The PACF appears to have one significant lag at 1. This means that most of the information is coming from the first lag. (However, there is a second lag at 10, which may be significant).

  * We might therefore tentatively estimate the order of the ARIMA model as (1, 1, 1), then see if a greater number of lags improves the model fit (i.e., the BIC, AIC) or changes the forecast.

Answer any remaining questions before moving on.

### 19. Instructor Do: Reflect (5 min)

Take a few moments to recap and reflect before ending class:


* We learned that certain models are robust against non-stationary data (ARIMA) while others need input data to be converted to stationary first (ARMA).

* We learned how to forecast stock prices and oil futures prices using statistical models (ARMA and ARIMA).

* We learned how to use time-series models to predict trends in things other than asset markets, for example, flight activity.

* These time-series models that you learned are used in practice everywhere, from forecasting next year's revenue to quantitative trading. As a result, you've learned a versatile tool for predicting future events.

### 20. End Class
