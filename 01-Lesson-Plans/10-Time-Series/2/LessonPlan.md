# 10.2 Lesson Plan: Time Series Models

### Overview

Today's class is the heart of this unit. Students will be introduced to core techniques to model or convert stationary data. They will also learn to use time series models such as ARMA, ARIMA, and GARCH to create forecasts.

### Class Objectives

By the end of this class, students will be able to:

* Determine stationarity of a time series.

* Create an ARMA model to forecast financial data.

* Create an ARIMA model to forecast financial data.

* Use ACF and PACF plots to estimate the order of ARMA and ARIMA models.

* Model and predict volatility with GARCH.

- - -

### Instructor Notes

* Slack out the [imblearn Installation Guide](../../11-Classification/Supplemental/Machine_Learning_Env_Setup_Guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* Today's class is the most challenging in this unit. Starting with the concept of stationarity, students will build on previous skills and ideas as they progress through the day. Some of these ideas are counterintuitive. However, they will gain repeated exposure to them from one activity to the next. A major goal for today's class, then, is for students to gain confidence through the process of working through fairly challenging material through multiple exposures.

* Be mindful that because each activity is a pre-requisite for the next, today's class may call for greater patience from both instructor and students. Do not rush through activities, and take the time to explain the core concepts and techniques in detail if necessary.

* While it is likely that some students may not fully grasp all of today's material by the end of class, the payoff will be in day 3, when your students will have a chance to create predictive models from start to end.


### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [10.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=55d24bd9-17d9-48f3-ad41-aad9011c28d4) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [10.2 Lesson Slides](https://docs.google.com/presentation/d/1LbFGZ_uiZZ5DgMdTJvNEoGOEM8uxkpT2u45jfzUSUQc/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

In this section, you will give a broad overview of today's class.

Welcome students to the second day of the time series unit, and briefly summarize key concepts from day 1:

* A time series can be decomposed into components such as trend, noise, and seasonality.

* Tools such as the Hodrick-Prescott filter, and EWMA can be used to identify trends in a time series.

Describe to students what they will be learning today:

* They will learn how to detect and convert non-stationary data to stationary.

* They will learn to model volatility in a time series.

* They will learn to use powerful time series models, ARMA,  ARIMA, and GARCH, to forecast financial data.

- - -

### 2. Instructor Do: Stationarity and Non-Stationarity (10 min)

**Corresponding Activity:** [01-Ins_Stationarity](Activities/01-Ins_Stationarity)

In this activity, you will define stationarity, a key concept in time series modeling.

**Files:**

* [stationarity.ipynb](Activities/01-Ins_Stationarity/Solved/stationarity.ipynb)

Use the slides to introduce the term `stationarity`:

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

  * The Augmented Dickey-Fuller tests for stationarity. It is a quick statistical test to tell you if a series is stationary or not.

  * The p-value is the second value in the output. A p-value less than 0.05 means that the series is stationary.

  ```python
  df['Returns'] = df.Close.pct_change()
  ```

  * pct_change() is another way to make a series stationary. The difference between diff() is that pct_change() essentially normalizes the data (_i.e., with the denominator doing the scaling_).


  ```python
  df['Diff'] = df.Close.diff()
  ```

  * Diff() subtracts out this upward trend, and can often be an easy way to make a series stationary.

- - -

### 3. Students Do: Stationarity (15 min)

**Corresponding Activity:** [02-Stu_Stationarity](Activities/02-Stu_Stationarity)

In this activity, students will perform techniques to make stationary a non-stationary time series.

**Files:**

  * [README.md](Activities/02-Stu_Stationarity/README.md)

  * [amazon.csv](Activities/02-Stu_Stationarity/Resources/amazon.csv)

  * [stationarity.ipynb](Activities/02-Stu_Stationarity/Unsolved/stationarity.ipynb)

- - -

### 4. Instructor Do: Review Stationarity (5 min)

**Files:**

  * [stationarity.ipynb](Activities/02-Stu_Stationarity/Solved/stationarity.ipynb)

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

  * The series is not quite perfectly stationary. The right side of the plot (between May and November in 2011) shows a higher variance.

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

- - -

### 5. Instructor Do: Auto-Regressive Moving Average Model (15 min)

Before diving into ARMA, quickly summarize auto-correlation for the class:

  * Autocorrelation is simply seeing to how well a time series correlates with a lagged copy of itself at a specified lag interval.

  * For example, if we have a week's worth of data, the value from each day would be matched up with the value from the previous day, and the two series would be mathematically correlated.

  * The main idea, again, is to determine how well past values correlate with future values at a specified lag, whether 1 or another lag period. Financial data, such as stock prices, often auto-correlate best at a lag of 1, but that is not always the case.

  * Plotting partial auto-correlation helps identify the **number** of lags that are significant in explaining the data.

Use the slides to introduce the concept of auto-regressive (AR) modeling:

  * In an AR model, past values are used to predict future values.

  * An AR model, therefore, assumes some degree of auto-correlation.

    * An AR model may have one significant lag, or it may have multiple.

Explain the relationship between an AR model and a linear regression model:

  * An AR model **is** a linear regression model.

  * In an example of a linear regression model, the number of rooms in houses may be used to predict house prices.

  * In an example of an AR model, the past prices of a stock may be used to predict future prices.

Explain the elements of the autoregression model:

  ![Images/arma01.gif](Images/arma01.gif)

  * If we are dealing with stock prices, the term on the left, `y` at time `t`, is the current price. In other words, it is the value of the stock price at time `t`.

  * The first term on the right, the letter mu, is simply the mean of the time series.

  * In the next term on the right, the `alpha` is a coefficient that is multiplied by the second term. The second term is the past stock price at `t-1`.

  * The `epsilon` at time `t`, the final term in the equation, is the error, or noise, at time `t`.

  * This particular equation assumes a first order. That is, it assumes that there is only one significant lag.

  * It also assumes a lag of 1, seen from the term `t-1`.

Explain that in a second order AR model, where two significant lags are assumed, an `alpha 2` multiplied by `y` at `t-2` would be added to the above equation.

  ![Images/arma02.gif](Images/arma02.gif)

  * In this case, the second lag is assumed to be 2. If it were at 5 periods, the lag would be `t-5`.

  * Again, this second order model assumes that the present value is determined by past values at two different lag points.

* Now that we have gone over the equation, ask your students to focus on the larger picture:

  * An AR model predicts future values based on past values at a specified lag, and the number of significant lags.

Next, explain the features of an MA model:

  ![Images/arma03.gif](Images/arma03.gif)

  * Here, `epsilon` at `t-1` is the noise, or error, at time `t-1`, or in other words, at a specified lag before the current value.

  * The `m` is the impact, or coefficient, from that previous error of the time series.

  * `epsilon` at `t` is the noise, or error, at time `t`.

Contrast the MA model with the AR model:

  * In an AR model, past values (plus error) are used to predict future values.

  * In an MA model, past errors (plus current error) are used to predict future values. In other words, it is a form of error correction.

* Emphasize that an MA model is **not** the same thing as a moving/rolling average that we discussed previously.

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

### 6. Instructor Do: ARMA in Practice (10 min)

**Corresponding Activity:** [03-Ins_ARMA](Activities/03-Ins_ARMA)

**File:**

  * [ARMA.ipynb](Activities/03-Ins_ARMA/Solved/ARMA.ipynb)

Now that we have a theoretical understanding of the ARMA model explain that we will go over using it in Python.

Open the notebook.

  * This is a dataset of NASDAQ stock prices from 2012 to 2019.

Display the plot and ask the class whether the time series is stationary:

  ![Images/arma_model01.png](Images/arma_model01.png)

  * It is non-stationary. The mean is not stable through the series, nor the variance.

Explain that an ARMA model requires a stationary time series.

  * Later today, we will cover a model for non-stationary series.

Ask the class how one might transform this time series to be stationary:

  * Some strategies that we have discussed include taking the difference between each row and the previous one. This is applicable when the auto-correlation is high at lag 1.

  * Another related idea is to calculate the return.

  * An exponential time series can be made stationary by taking the logarithm.

Explain that here, we are stationarizing the time series by calculating the return.

  ```python
  df['Return'] = df['Close'].pct_change()
  returns = df['Return'].dropna()
  ```

  * The Pandas function `pct_change()` calculates the returns, and NaN values are subsequently dropped.

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

  * The predicted values (in this case, stock returns) are formatted as a DataFrame and plotted.

Finally, highlight a few important features of the model's summary:

  ```python
  results.summary()
  ```

  * The p-value of the first lag is low at 0.012.

  * The AIC and BIC values should also be noted, lower values reflecting better accuracy. We will cover these values in greater detail later today.

- - -

### 7. Students Do: Yields (15 min)

**Corresponding Activity:** [04-Stu_Yields](Activities/04-Stu_Yields)

In this activity, students will create an ARMA model on yield data.

**Files:**

  * [README.md](Activities/04-Stu_Yields/README.md)

  * [yield.csv](Activities/04-Stu_Yields/Resources/yield.csv)

- - -

### 8. Instructor Do: Review Activity (10 min)

**Files:**

  * [yields.ipynb](Activities/04-Stu_Yields/Solved/yields.ipynb)

Open the notebook and show the plot of the data:

  ![Images/yields01.png](Images/yields01.png)

  ```python
  from statsmodels.tsa.stattools import adfuller
  adfuller(data.Yield)
  ```

  * Because the trends are not obvious, the adfuller test can be used to determine stationarity.

  * In this example, the p-value is 0.011 (less than 0.05), suggesting stationarity.

 * In addition to the Dickey-Fuller test, since the data appears visually not to have a consistent upward or downward trend, this also suggests stationarity. Because of that, we will try modeling the series without further transformations.

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

  * Other than the order numbers, the code is boilerplate.

  * In `order=(2, 2)`, the first number denotes the AR order, and the second number denotes the MA order.

Discuss the summary of the results:

  * The p-values are all less than 0.05, suggesting a good fit.

Explain that the model can be used to make predictions:

  ```python
  pd.DataFrame(result.forecast(steps=5)[0]).plot(title="Yield Forecast")
  ```

  ![Images/yields5.png](Images/yields05.png)

  * The `forecast()` method is used here to predict yield values for the next 5 days.

- - -

### 9. BREAK (15 min)

- - -

### 10. Instructor Do: ARIMA (15 mins)

**Corresponding Activity:** [05-Ins_ARIMA](Activities/05-Ins_ARIMA)

In this activity, in addition to describing the ARIMA model, you will elucidate the use of ACF and PACF plots, as well as AIC and BIC, in identifying the order of an ARIMA model.

**File:**

  * [ARIMA.ipynb](Activities/05-Ins_ARIMA/Solved/ARIMA.ipynb)

Open the notebook and describe the dataset:

  ![Images/ARIMA01.png](Images/ARIMA01.png)

  * It is a time series of the number of airline passengers from 1949 through 1960.

  * There is a pronounced upward trend. The time series is, therefore, non-stationary.

Ask the class whether **ARMA** would be a suitable model for this dataset:

  * **Answer:** No, it would not. There is a pronounced upward trend, and ARMA models assume stationarity.

Explain that, unlike an ARMA model, an **ARIMA** model stationarizes a non-stationary time series.

  * Specifically, it stationarizes a time series by differencing it. In Pandas, we have differentiated with the `diff()` method.

  * The stationarizing step is the key difference between ARMA and ARIMA. It is possible to stationarize a time series manually, as we have done before. However, ARIMA automates the process.

Describe the ACF and PACF plots:

  ![Images/ARIMA02.png](Images/ARIMA02.png)

  * In the ACF plot, significant autocorrelation exists, with a blip at the 12th lag. This makes sense, as this is a monthly time series, and the lag at 12 accounts for seasonal traffic patterns in the data.

  ![Images/ARIMA03.png](Images/ARIMA03.png)

  * In the PACF plot, there appear to be at least two significant lags, at 1 and 2. The 12th lag also seems significant.

Explain the significance of ACF and PACF plots in estimating the order of the ARIMA model:

  * Up to this point, students were given AR and MA orders, but the ACF and PACF plots can be useful tools in identifying the order of ARMA and ARIMA models.

  * A general rule of thumb is to use the PACF to estimate the AR order. In this example, there appear to be between 2 and 8 lags that exceed the confidence interval. It is reasonable to settle on 2 as the AR order, as the first two lags significantly stand out from the rest.

  * Similarly, the ACF can be used to estimate the MA order. In this example, the first two lags also appear to be significant in the ACF.

  * We might like to capture the 12th lag too, but that will require a model that's a little more advanced ("Seasonal" ARIMA) than what we will cover in this activity.

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

  * An ARIMA model in which the differencing order is zero is, therefore, an ARMA model. For example, an ARIMA model with an order of (1, 0, 1) is an ARMA model of an order of (1, 1).

Use the slides to explain the interpretation of AIC and BIC:

  * AIC stands for Akaike Information Criterion. BIC stands for Bayesian Information Criterion.

  * Both of these metrics estimate the quality of a model.

  * They weigh goodness of fit against the number of parameters. In other words, AIC and BIC favor the simplest model that best fits the data.

  * This means that they penalize models with a large number of parameters. A model with a large number of parameters may describe that particular dataset well but may lose its predictive power when used on new data.

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

  * AIC and BIC favor models with the best fit and penalize higher order models for their complexity.

  * Lower AIC and BIC scores are usually better.

  * These quantities can also be used to estimate the order of an ARMA model. An ARMA model, however, does not have a differencing order because it assumes that the time series is stationary and therefore does not need to be differenced.

Send the following link to students for more information on the order of an ARIMA model:

  * [https://people.duke.edu/~rnau/arimrule.htm](https://people.duke.edu/~rnau/arimrule.htm).

- - -

### 11. Students Do: An ARIMA and a Leg (15 min)

**Corresponding Activity:** [06-Stu_ARIMA_Leg](Activities/06-Stu_ARIMA_Leg)

**Files:**

  * [README.md](Activities/06-Stu_ARIMA_Leg/README.md)

  * [oil_futures_front.csv](Activities/06-Stu_ARIMA_Leg/Resources/oil_futures_front.csv)

  * [stu_ARIMA.ipynb](Activities/06-Stu_ARIMA_Leg/Unsolved/oil_futures_ARIMA.ipynb)

- - -

### 12. Instructor Do: Review Activity (10 min)

**File:**

* [stu_ARIMA.ipynb](Activities/06-Stu_ARIMA_Leg/Solved/oil_futures_ARIMA.ipynb)

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

- - -

### 13. Instructor Do: GARCH (15 min)

**Corresponding Activity:** [07-Ins_GARCH](Activities/07-Ins_GARCH)

**File:**

* [garch.ipynb](Activities/07-Ins_GARCH/Solved/garch.ipynb)

Before introducing GARCH to the class, introduce the topic of volatility:

* Volatility can dictate the larger movements of the market. Higher volatility, for example, tends to accompany lower returns.

* In portfolio management, for example, diversifying the types of assets can help reduce risk in a volatile market, and the forecasting of volatility would help make adjustments to reduce risk.

* Another example is the pricing of derivatives. The price of derivatives, such as options, are influenced much more by volatility than the price of the underlying asset. Characterizing and forecasting volatility is, therefore, a key skill in derivative trading.

* Understanding volatility is also important to banks as loan failures can occur in a cluster. Assets must exceed liabilities, so regulators and banks alike create forecast models for asset volatility.

Explain that GARCH models volatility. Open the slideshow and summarize the key features of the ARMA model:

* An autoregressive component in which future values are predicted based on past values. In this model, values are a function of time.

* A moving average component in which future values are predicted based on past errors.

Explain that GARCH models are structured similarly, but to predict volatility:

* As with ARMA models, there are autoregressive and moving average components.

Formalize the term volatility:

* In this context, volatility is the change in variance across a time series.

* Volatility, then, is a function of time.

* GARCH stands for Generalized Autoregressive Conditional Heteroskedasticity, where heteroskedasticity simply means uneven variance.


Use the `Volatile Periods in the US Stock Market` slides to illustrate how volatility clusters and to motivate GARCH models:

This slide shows an example of volatility clusters:

* Volatility and returns tend to cluster.

* GARCH is a model designed to take specific advantage of that.

* Tracing the S&P 500 over time gives us some examples of highly volatile periods:

  ![Images/garch01.png](Images/garch01.png)

* The first highlighted box captures the period after the September 11th attacks and the decline of the dotcom bubble, while the second highlights the recession that began in 2008, including the collapse of Lehmann Brothers.

* Scenarios such as political upheavals, natural disasters, and disruptions to oil supply can also cause volatility to cluster.

Explain that the cause of financial market volatility is largely psychological:

* When a big, unexpected event occurs, there is much uncertainty about the future.

* It takes time for people to figure out the financial impact, and until then, there are disagreements about the impact.

* It is these disagreements that lead to the volatility.

Open the notebook and walk through a code example of using GARCH to predict volatility. First, explain that like an ARMA model, a GARCH model assumes stationarity:

  ![Images/garch02.png](Images/garch02.png)

* The closing price has been stationarized by transforming it into returns.

* Volatility clusters are visible here in the plot of S&P returns, notably between 2008 and 2010 or so.

Explain the data preparation steps:

  ```python
  returns = sp500.loc['2008':'2009'].Close.pct_change() * 100
  returns = returns.dropna()
  ```

* The closing prices are stationarized as returns and multiplied by 100 for ease of view.

* Numbers that are NaNs are dropped.

Explain that the steps of creating a GARCH model are very similar to that of an ARMA model:

  ```python
  from arch import arch_model
  model = arch_model(returns, mean="Zero", vol="GARCH", p=1, q=1)
  res = model.fit(disp="off")
  res.summary()
  ```
* Open the terminal, and execute the following command to install the arch module: `pip install arch`

* From the `arch` module, `arch_model` is imported.

* The arguments `mean="Zero", vol="GARCH"` specify the GARCH model.

* The arguments `p=1, q=1`, as in ARMA models, specify the auto-regressive and moving average orders. These can be identified by the same process of plotting the ACF and the PACF and identifying AIC and BIC values.

  * To reiterate, `p` is the AR component of the model
  * and `q` is the MA component of the model
  * the concept is similar to ARMA, except here we are forecasting volatility.

* The model is created, fits the data, and the summary is printed.

  ![Images/garch03.png](Images/garch03.png)

* The results are plotted. Here, `annualize='D'` argument reflects a scaling by 252 trading days that are in a year.

Explain that the model can also be used to plot a forecast of _volatility_:

  ```python
  forecast_horizon = 3
  forecasts = res.forecast(start='2009-12-31', horizon=forecast_horizon)

  intermediate = np.sqrt(forecasts.variance.dropna()*252)
  final = intermediate.dropna().T
  final.plot()
  ```

* The forecast will be generated for 3 trading days.

* The `forecast()` method generates forecast values.

* Intermediate steps are taken to format the data properly for plotting. The standard deviation is taken of the forecast values by taking the square root of the variance, then transposed (with `T`), then plotted.

Show the plot of the volatility forecast:

  ![Images/garch04.png](Images/garch04.png)

  * This chart shows our estimate of the volatility of the S&P 500 for the next three days.

  * The chart shows that volatility (i.e., risk) in the market is expected to rise.

  * Therefore, with GARCH, we have developed a cool way to forecast risk in the market.

- - -

### 14. Students Do: Euro-USD Volatility (10 min)

**Corresponding Activity:** [08-Stu_USD](Activities/08-Stu_USD)

**Files:**

* [README.md](Activities/08-Stu_USD/README.md)

* [USD_per_Euro_Hourly_Mid_Prices.csv](Activities/08-Stu_USD/Resources/USD_per_Euro_Hourly_Mid_Prices.csv)

* [usd.ipynb](Activities/08-Stu_USD/Unsolved/usd.ipynb)

- - -

### 15. Instructor Do: Review Activity (10 min)

**Files:**

* [usd.ipynb](Activities/08-Stu_USD/Solved/usd.ipynb)

Open the notebook and display the plot of the exchange rate:

  ![Images/usd01.png](Images/usd01.png)

* Volatility appears to be more pronounced in the years 2015-2017.

* The series is non-stationary. It will need to be stationarized to use GARCH.

```python
df['Return'] = df.Rate.pct_change() * 100 * 24
df = df.resample('D').mean()
df = df.dropna()
df.head()
```

* The pct_change() in the above code makes the data stationary.

* The DataFrame is resampled. Since we start with hourly exchange rates, we will convert them from hourly to daily using the above block of code.

* Specifically, this block starts by calculating the percentage hourly return.

  * These hourly returns are scaled up to daily, by multiplying by 24 (currency markets trade 24 hours per day).

  * The resample('D') function then calculates the daily average percentage return.

* The plot of the resulting stationarized series also confirms the clustering of volatility seen in 2015, 2016, and 2017:

  ![Images/usd02.png](Images/usd02.png)

Explain the code for creating the GARCH model in Python:

  ```python
  model = arch.arch_model(returns, mean="Zero",  vol="GARCH", p=2, q=2)
  res = model.fit(disp="off")
  res.summary()
  ```

* The AR and MA orders, specified as `p` and `q`, were given in this activity.

* However, students can use ACF and PACF plots, as well as AIC and BIC, to identify the GARCH model order, just as they have done in ARMA AND ARIMA.

Next, walk through the code for plotting the volatility forecast:

  ```python
  forecast_horizon = 5
  forecasts = res.forecast(start='2019-12-08', horizon=forecast_horizon)
  ```

* The last date of the dataset (which can be identified by `df.tail()`) is 2019-12-08. It is defined as the starting date of the forecast.

* The `forecast_horizon` is defined as 5, meaning the forecast for the next 5 days will be generated.

* A forecast is generated with the `forecast()` method.

Finally, walk through the steps of plotting the volatility forecast:

  ```python
  intermediate = np.sqrt(forecasts.variance * 252)
  final = intermediate.dropna().T
  final.plot()
  ```

* With `np.sqrt(forecasts.variance * 252)`, the standard deviation of forecasts is scaled by 252 to account for the number of trading days in a year (standard deviation is the square root of variance).

* All NaNs are dropped, and the results are transposed with `T`. The transpose switches the rows and columns to make it easier to plot.

* The volatility is plotted with the `pd.plot()` method:

  ![Images/usd04.png](Images/usd04.png)

* Based on the upward trend in the plot, the volatility of the EUR-USD exchange rate is predicted to increase over the next 5 days.

- - -

### 16. Instructor Do: Reflect (5 min)

Take a few moments to recap and reflect before ending class:

* We learned that certain models are robust against non-stationary data (ARIMA) while others need input data to be converted to stationary first (ARMA).

* We learned how to forecast stock prices and oil futures prices using statistical models (ARMA and ARIMA).

* We learned that understanding volatility is important in financial forecasting, and we learned a useful model to predict volatility (GARCH).

* These time-series models that you learned are used in practice everywhere, from forecasting next year's revenue to quantitative trading. As a result, you have learned a versatile tool for predicting future events.

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
