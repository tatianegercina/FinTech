# 10.3 Lesson Plan: Volatility and Beyond

### Overview

Today's class will round out time series modeling with GARCH. Students will also gain exposure to the theory and practice of model validation.

### Class Objectives

By the end of this class, students will be able to:

* Model and predict volatility with GARCH.

* Define overfitting and articulate the benefits of parsimony.

* Use Scikit-learn to train and test time series data.

* Make out-of-sample predictions in rolling windows.

* Evaluate the accuracy of out-of-sample predictions.

- - -

### Instructor Notes

* Through longer activities, students will consolidate their skills from the previous two days, creating financial models in multiple steps, from stationarizing data to identifying model orders to making predictions on future values and volatility. You and your TAs should be on the lookout for your weaker students during the longer activities. Make sure that such students do not flounder.

* Your students will also learn to validate models by training and testing data. Emphasize that this will be a valuable skill in later units as they dive more deeply into machine learning.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1xHeGCp3x1TFYbcTvRj2gzRrPX64cK_zaAdm49w2PNP8/edit#slide=id.g5f3ad86fc3_0_0).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

### 1. Instructor Do: Introduction (5 min)

In this section, you will give a broad overview of today's class.

Welcome students to the second day of the time series unit, and briefly summarize key concepts from day 2:

* Auto-correlation is an important feature of many time series datasets.

* Stationarity of a time series can determine the time series model.

* ARMA models use past values and past errors to predict future values. An ARMA model assumes stationarity.

* ARIMA is similar to ARMA, but does not assume stationarity.

Describe to students what they will be doing today:

* They will learn to model volatility in a time series.

* They will learn to validate models by training and testing them.

* They will learn to create a model that can continuously update itself.

### 2. Instructor Do: GARCH (15 min)

**File:**

* [garch.ipynb](Activities/01-Ins_GARCH/Solved/garch.ipynb)

Before introducing GARCH to the class, introduce the topic of volatility:

* Volatility can dictate the larger movements of the market. Higher volatility, for example, tends to accompany lower returns.

* In portfolio management, for example, diversifying the types of assets can help reduce risk in a volatile market, and the forecasting of volatility would help make adjustments to reduce risk.

* Another example is the pricing of derivatives. The price of derivatives, such as options, are influenced much more by volatility than the price of the underlying asset. Characterizing and forecasting volatility is therefore a key skill in derivative trading.

* Understanding volatility is also important to banks as loan failures can occur in a cluster. Assets must exceed liabilities, so regulators and banks alike create forecast models for asset volatility.

Explain that GARCH models volatility. Open the slideshow and summarize the key features of the ARMA model (Slide 5):

* An autoregressive component in which future values are predicted based on past values. In this model, values are a function of time.

* A moving average component in which future values are predicted based on past errors.

Explain that GARCH models are structured similarly, but to predict volatility (Slide 6):

* As with ARMA models, there are autoregressive and moving average components.

Formalize the term volatility (Slides 7-8):

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

* Volatility clusters are visible here in plot of S&P returns, notably between 2008 and 2010 or so.

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

* From the `arch` module, `arch_model` is imported.

* The arguments `mean="Zero", vol="GARCH"` specify the GARCH model.

* The arguments `p=1, q=1`, as in ARMA models, specify the auto-regressive and moving average orders. These can be identified by the same process of plotting the ACF and the PACF, and identifying AIC and BIC values.

  * To reiterate, `p` is the AR component of the model
  * and `q` is the MA component of the model
  * the concept is similar to ARMA, except here we're forecasting volatility.

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

  * This chart shows our estimate of volatility of the S&P 500 for the next three days.

  * The chart shows that volatility (i.e., risk) in the market is expected to rise.

  * Therefore, with GARCH, we've developed a cool way to forecast risk in the market.

### 3. Students Do: Euro-USD Volatility (15 min)

**Files:**

* [README.md](Activities/02-Stu_USD/README.md)

* [USD_per_Euro_Hourly_Mid Prices.csv](Activities/03-Stu_USD/Resources/USD_per_Euro_Hourly_Mid Prices.csv)

* [usd.ipynb](Activities/02-Stu_USD/Unsolved/usd.ipynb)

### 4. Instructor Do: Review Activity (10 min)

**Files:**

* [usd.ipynb](Activities/02-Stu_USD/Solved/usd.ipynb)

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

* The DataFrame is resampled. Since we start with hourly exchange rates, we'll convert them from hourly to daily using the above block of code.

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

* All NaNs are dropped, and the results are transposed with `T`. The transpose  switches the rows and columns to make it easier to plot.

* The volatility is plotted with the `pd.plot()` method:

  ![Images/usd04.png](Images/usd04.png)

* Based on the upward trend in the plot, the volatility of the EUR-USD exchange rate is predicted to increase over the next 5 days.

### 5. Instructor Do: Overfitting and Parsimony (10 min)

Open the slideshow and introduce the concept of overfitting:

* Overfitting occurs when a model is too specific to a particular data set.

* An overfitted model memorizes the random patterns of the training data too well. It memorizes the quirks of a dataset without identifying the underlying patterns.

* Consequently, such a model will perform poorly when it encounters new data with similar underlying patterns, but with different quirks.

* In other words, overfit models learn the noise found in the training data, rather than just the signal.

* Because models are optimized to limit the training error, they can become too focused on the unique patterns of the training data, and fail to extend to  previously unseen data.

Explain that overfitting typically involves an excessive number of variables in a model.

*  With more parameters, the model can memorize the rare patterns of the training data, resulting in a rigid model that does not generalize well.

Explain that a useful analogy might be to memorize the answers to a math test without learning the underlying principles.

* The learning that takes place is useful in one particular setting, but is less generalizable to other contexts.

Next, explain variance and bias, two important concepts in machine learning:

* Bias and variance are errors in predicting data from underfitting and overfitting, respectively.

* In an underfit model, the bias is high, meaning that the model is not sophisticated enough to capture the general pattern of the data. In other words, a model with a high bias is too simple.

* In an overfit model, the variance (defined in this setting as prediction error on new data) is high, meaning that the model is too complex, and will not be generalizable to other contexts.

* When choosing a model, it is important to keep in mind the balance between bias and variance.

Define the concept of parsimony:

* It is a statistical application of Occam's razor: when two models perform similarly, choose the simpler one.

* Do not make a model more complex than is needed to explain the data. Needlessly complex models may be computationally expensive and hard to interpret.

* Parsimony is especially pertinent with financial data, which tend to be noisy, and are thus easy to overfit.

Explain that we have already seen parsimony in action:

* AIC and BIC reward models for fitting data accurately, but punish them for having a large number of parameters.

### 6. Instructor Do: Train, Test, Split (10 min)

**File:**

* [train_test.ipynb](Activities/03-Ins_Train_Test/Solved/train_test.ipynb)

Inform your students that they will now learn to minimize the problems posed by overfitting.

Explain that a common strategy used in machine learning is to split a dataset into a train set and a test set.

* With the training set, the model learns the relevant patterns in the data. The model seeks to minimize error on the training data.

* Then the testing set is used evaluate the model's performance on unseen data.

* If the model underperforms with the testing set, the model can be retrained with better (or more) data, or the model itself can be tweaked.

Remind your students that we have worked with a number of models so far, including ARMA, ARIMA, GARCH, and linear regression:

* Models were trained on the entire dataset, then made predictions.

* We will now split a dataset into training and testing data and run linear regression on them.

Open the notebook and introduce the dataset:

  ```python
  df['Return'] = df.Close.pct_change() * 100
  df['Lagged_Return'] = df.Return.shift()
  df = df.dropna()
  ```

  ![Images/train01.png](Images/train01.png)

* It is the familiar S&P 500 stock dataset.

* The returns and lagged returns are computed, as we have done before.

* NaN values are deleted from the DataFrame.

* In regression, the lagged returns will be the **independent** variable and the returns will be the **dependent** variable, since we are attempting to answer to what extent past values affect future values. It's like asking the question: given today's return, what's the expected return going to be tomorrow?

Explain that the next step is to split the dataset into `train` and `test` sets:

  ```python
  train = df.loc['2008':'2012']
  test = df.loc['2013']
  ```

* The `loc[]` accessor is used to assign the data from years 2008 through 2012 to the testing set, and 2013 data to the testing set.

* In machine learning, data is typically randomly assigned to training and test sets. That is, any given data point might be assigned to the training set, or it might be assigned to the testing set. This is possible because each data point is independent of another.

* However, in a time series in which autocorrelation exists, that is not possible. Instead, data points prior to a cutoff point comprise the training set, and all points that come after comprise the testing set.

* Another common practice is to assign 80% of the data to the training set, and 20% to the testing set. Oftentimes, with time-series data, it's good to explicitly specify the date ranges.

Explain the code with which `train` and `test` sets are divided into dependent and independent variables.

  ```python
  X_train = train["Lagged_Return"].to_frame()
  X_test = test["Lagged_Return"].to_frame()
  y_train = train["Return"]
  y_test = test["Return"]
  ```

* The lagged return values from the train and test sets comprise the independent variables, or `X`.

* The return values comprise the dependent variable, or `y`.

* As noted previously, the Scikit-learn library requires that the x-variable be shaped in two dimensions. The `to_frame()` method accomplishes this.

Explain the following block of code:

  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)
  ```

* With Scikit-learn, a model is created, fitted to the training set.

* Then the model predicts y-values based on the testing set.

Explain the optional step to assemble actual and predicted values in a single DataFrame:

  ```python
  Results = y_test.to_frame()
  Results["Predicted Return"] = predictions
  ```

* `y_test.to_frame()` transforms actual test values into a DataFrame.

* The predicted y-values are added into the DataFrame as a column.

Show the plot of the predictions and the actual results in the test set:

  ![Images/train02.png](Images/train02.png)

Finally, walk through the error metrics:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  mse = mean_squared_error(
      Results["Return"],
      Results["Predicted Return"])
  rmse = np.sqrt(mse)
  ```

  ```python
  in_sample_results = y_train.to_frame()
  in_sample_results["In-sample Predictions"] = model.predict(X_train)
  in_sample_mse = mean_squared_error(
      in_sample_results["Return"],
      in_sample_results["In-sample Predictions"])
  in_sample_rmse = np.sqrt(in_sample_mse)
  ```

* The RMSE is a measure of model accuracy. The higher the RMSE, the lower the accuracy (since a higher RMSE means higher prediction error).

* In the first block, the RMSE of the **test** set is computed.

* In the second block, the RMSE of the **train** set is computed.

* The in-sample (_training_ sample) RMSE, at 1.65, is higher than the out-of-sample (_testing_ sample) at 0.70. Typically, out-of-sample errors are higher than in-sample errors.

### 7. Students Do: Ripple (30 min)

In this activity, students will create GARCH and linear regression models for the price of Ripple (XRP), a cryptocurrency. They will validate the latter model with training and test sets.

**Files:**

* [README.md](Activities/04-Stu_Ripple/README.md)

* [USD_per_Ripple_XRP_prices.csv](Activities/04-Stu_Ripple/Resources/USD_per_Ripple_XRP_prices.csv)

* [xrp.ipynb](04-Stu_Ripple/Unsolved/xrp.ipynb)

### 8. Instructor Do: Review Activity (10 min)

A detailed walk-through of the code is given below. However, in the interest of time, use your judgment to highlight the major points and gloss over parts students have seen repeatedly.

**File:**

* [xrp.ipynb](Activities/04-Stu_Ripple/Solved/xrp.ipynb)

Open the notebook and display the plot of Ripple's closing price:

  ![Images/xrp01.png](Images/xrp01.png)

* Early 2018 seems to have been the period of greatest price volatility.

* The time series will have to be made stationary.

Explain the steps taken to stationarize the time series:

  ```python
  df['Return'] = df.Close.pct_change() * 100
  df['Lagged_Return'] = df['Return'].shift()
  df = df.replace(-np.inf, np.nan).dropna()
  ```

* Two columns are created: one for daily return values and one for return values at a lag of one day.

* All infinity values are replaced with NaNs, and all NaNs are subsequently dropped. (Occasionally these _infs_ are created when calculating percentage returns).

In the next part, walk through the steps of creating and validating a linear regression model. Explain that the time series is split so that 2017 through 2018 is included in the training set, and data for 2019 is used for the test set:

  ```python
train = df['2017':'2018']
test = df['2019']
  ```

* The `train` dataframe is obtained by slicing the DataFrame's datetime index to include only years 2017 through 2018.
* The `test` dataframe is obtained by slicing the DataFrame's datetime index to include only 2019.

Explain that the train and test sets are now defined for independent and dependent variables:

  ```python
  X_train = train["Lagged_Return"].to_frame()
  y_train = train["Return"]
  X_test = test["Lagged_Return"].to_frame()
  y_test = test["Return"]
  ```

* `X_train` and `X_test` are transformed into DataFrames in order to reshape them to meet the requirements of Scikit-learn.

* `y_train` and `y_test` can remain as pandas series, however.

Briefly go over the boiler plate code to generate a linear regression model with Scikit-learn:

  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)
  ```

* The model is created and fitted to the training data.

* Predictions are generated using the test data.

Explain that the predicted values are plotted:

  ```python
  Results = y_test.to_frame()
  Results["Predicted Return"] = predictions
  Results.plot()
  ```

* `y_test`, the actual values in the test set, is compared with the predicted values in the test set.

Finally, go over the metrics of the in-sample and out-of-sample predictions:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  mse = mean_squared_error(
      Results["Return"],
      Results["Predicted Return"])
  out_of_sample_rmse = np.sqrt(mse)

  in_sample_results = y_train.to_frame()
  in_sample_results["In-sample Predictions"] = model.predict(X_train)
  in_sample_mse = mean_squared_error(
      in_sample_results["Return"],
      in_sample_results["In-sample Predictions"])
  in_sample_rmse = np.sqrt(in_sample_mse)
  ```

  * The RMSE is obtained by comparing predicted and actual data.

  * The out-of-sample RMSE is lower than the in-sample RMSE. RMSE is typically lower for training data, but is higher in this case.

  * This could be due to the fact that our out-of-sample period is small, so just by chance, the model happened to do better out-of-sample than in-sample.

- - -

### 9. Break (40 min)

- - -

### 10. Instructor Do: Rolling Out-of-Sample (15 min)

**File:**

* [sp500.ipynb](Activities/05-Ins_Rolling_Out_of_Sample/Solved/sp500.ipynb)

Point out that up to this point, we have created models as a one-shot affair. Explain that we will go over a procedure allows an analyst to update the financial model as new data continues to come in.

* In this activity, we will cover a more sophisticated iterative approach to the train-test-split technique in the previous activity.

* During each iteration, there will be a training window, a temporal segment of the entire dataset. That window will be followed by a testing period.

* In the first iteration of this activity, for example, the training window will be the first 26 weeks. The testing period will be the 27th week. In the second iteration, the training window will be weeks 2 through 27, and the testing period will be the 28th week.

* During each iteration, a regression model is created, fitted to the data, and generates predictions.

Open the notebook and inform students that the time series is the SP500 stock data, which they have seen before:

  ```python
  df['Return'] = df.Close.pct_change() * 100
  df['Lagged_Return'] = df.Return.shift()
  df = df.dropna()
  ```

* Once again, returns and lagged returns are computed. Linear regression will be performed on these values.

Briefly explain how the data is resampled into weekly values.

  ```python
  weeks = df.index.to_period("w").unique()
  ```

* The `to_period("w")` method here splits the index datetimes into weekly periods.

  ```python
  # Weekly Increments
  df.index.to_period("w")

  # Unique Weekly Increments
  weeks = df.index.to_period("w").unique()
  ```

Next, explain the pandas time series techniques used to calculate the training and testing data:

* The training period for this dataset will be 26 weeks total while the testing window will be one week. In other words, 26 weeks will be used to create a model that can predict the 27th week.

  ```python
  # Beginning of training window
  start_of_training_period = weeks[0].start_time.strftime(format="%Y-%m-%d")
  start_of_training_period

  # End of training window
  end_of_training_period = weeks[training_window + 0].end_time.strftime(format="%Y-%m-%d")
  end_of_training_period
  ```

* `weeks[0]` is the first week of the data frame. In this example, The start of the training period is `2007-12-31` and the end of the training period is `2008007-06`.

  ```python
  # The week of the first test window
  test_week = weeks[training_window + 0 + 1]
  test_week
  ```

* The test week is just the first week after the training window.

* We can also break that down into the start and end days of the test week.

  ```python
  # The first day of the test week
  start_of_test_week  = test_week.start_time.strftime(format="%Y-%m-%d")
  start_of_test_week

  # The last day of the test week
  end_of_test_week = test_week.end_time.strftime(format="%Y-%m-%d")
  end_of_test_week
  ```

* Finally, the training period and testing period can be sliced using the start and end values that were calculated above.

  ```python
  # Training data with just one window
  train = df[start_of_training_period:end_of_training_period]

  # Testing data with just one window
  test = df[start_of_test_week:end_of_test_week]
  ```

* The outcome of the above code is to split each weekly period into start and end dates in string format.

Explain that the goal is to roll through the period in 26-week windows, one week at a time:

  ```python
  training_window = 26
  timeframe = len(weeks) - training_window - 1
  ```

* The `timeframe` variable refers to the total timespan encompassed by the data frame, minus the training window of 26 weeks (minus 1 due to indexing).

* The last training window will therefore begin 26 weeks before the end of the total timespan. If there were to be a training window after this point, it would be less than the full 26 weeks, and the Python code would throw an out-of-bounds error.

Explain that empty data frames are created to hold predicted values and actual values:

  ```python
  all_predictions = pd.DataFrame(columns=["Out-of-Sample Predictions"])
  all_actuals = pd.DataFrame(columns=["Actual Returns"])
  ```

* During each rolling iteration, data will be appended to them.

* After the iterations are complete, the predicted values will be compared to actual values.

Walk through the for-loop:

  ```python
  for i in range(0, timeframe):

    start_of_training_period = weeks[i].start_time.strftime(format="%Y-%m-%d")
    end_of_training_period = weeks[training_window+i].end_time.strftime(format="%Y-%m-%d")
  ```

* The beginning and the end of each training are marked with `start_of_training_period` and `end_of_training_period`. The start is at the current week in the iteration, and the end comes 26 weeks later.

* During each iteration, the training period moves forward by one week.

  ```python
    test_week = weeks[training_window + i + 1]
    start_of_test_week  = test_week.start_time.strftime(format="%Y-%m-%d")
    end_of_test_week = test_week.end_time.strftime(format="%Y-%m-%d")

    train = df[start_of_training_period:end_of_training_period]
    test = df[start_of_test_week:end_of_test_week]
  ```

* The `test_week` is the week that comes after the training period.

* The 27 week period is split into `train` and `test` sets: 26 weeks of training data, and 1 week of test data.

  ```python
    X_train = train["Lagged_Return"].to_frame()
    y_train = train["Return"]
    X_test = test["Lagged_Return"].to_frame()
    y_test = test["Return"]

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    predictions = pd.DataFrame(
        predictions,
        index=X_test.index,
        columns=["Out-of-Sample Predictions"])

    actuals = pd.DataFrame(y_test, index=y_test.index)
    actuals.columns = ["Actual Returns"]

    all_predictions = all_predictions.append(predictions)
    all_actuals = all_actuals.append(actuals)
  ```

* The `X_train` and `X_test` series are converted into a data frame.

* A model is created for each training period, then fitted to the data.

* The test set is used to create predictions.

* Then the predicted and actual data are appended to `all_predictions` and `all_actuals` data frames during each iteration.

Reassure students that they will be able to use this notebook as a reference for future calculations.

### 11. Students Do: Rolled Gold (30 min)

In this activity, students will perform predictions with linear regression on a rolling out-of-sample basis, in order to predict the price of gold.

**Files:**

* [README.md](Activities/06-Stu_Rolled_Gold/README.md)

* [gold_price.csv](Activities/06-Stu_Rolled_Gold/Resources/gold_price.csv)

* [gold.ipynb](Activities/06-Stu_Rolled_Gold/Unsolved/gold.ipynb)

### 12. Instructor Do: Review Activity (10 min)

**File:**

* [gold.ipynb](Activities/06-Stu_Rolled_Gold/Solved/gold.ipynb)

Open the notebook and explain that, since regression will later be performed on returns and lagged returns in USD, those columns are created:

  ![Images/gold01.png](Images/gold01.png)

* NaNs are dropped as well.

Next, introduce the code involving the single training and test window. ("Train Test Split Predictions").

* The dataframe of daily gold price returns is split into `train` and `test` sets, with 2019 as the out-of-sample prediction period:

```python
train = df['2001':'2018']
test = df['2019']
```

*The rest of this section involves the linear regression and training/test window code that they used in the activity just prior.

*Point out that we'll save the out_of_sample_rmse developed from this approach, and later compare it the RMSE developed from the rolling-out-of-sample approach.

Next, introduce the preparatory steps for rolling out-of-sample predictions using Scikit-learn:

  ```python
  all_predictions = pd.DataFrame(columns=["Out-of-Sample Predictions"])
  all_actuals = pd.DataFrame(columns=["Actual Returns"])

  weeks = df.index.to_period("w").unique()

  training_window = 12
  timeframe = len(weeks) - training_window - 1
  ```

* Empty DataFrames named `all_predictions` and `all_actuals` are created to hold rolling predictions, as well as actual values.

* With `df.index.to_period("w").unique()`, the DataFrame index is split into weekly periods.

* The training window is defined as 12 weeks. (3 months)

* The `timeframe` defines the last week of the time series in which the training window will begin.

Walk through the iterations that take place inside the for-loop:

  ```python
  for i in range(0, timeframe):
    start_of_training_period = weeks[i].start_time.strftime(format="%Y-%m-%d")
    end_of_training_period = weeks[training_window+i].end_time.strftime(format="%Y-%m-%d")

    test_week = weeks[training_window+i+1]
    start_of_test_week  = test_week.start_time.strftime(format="%Y-%m-%d")
    end_of_test_week = test_week.end_time.strftime(format="%Y-%m-%d")

    train = df.loc[start_of_training_period:end_of_training_period]
    test = df.loc[start_of_test_week:end_of_test_week]

    X_train = train["Lagged_Return"].to_frame()
    y_train = train["Return"]
    X_test = test["Lagged_Return"].to_frame()
    y_test = test["Return"]

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    predictions = pd.DataFrame(predictions, index=X_test.index, columns=["Out-of-Sample Predictions"])

    actuals = pd.DataFrame(y_test, index=y_test.index)
    actuals.columns = ["Actual Returns"]

    all_predictions = all_predictions.append(predictions)
    all_actuals = all_actuals.append(actuals)
  ```

* In each iteration, the start and end of the training period are defined with `weeks[i]` and `weeks[training_window+i]`, respectively.

* The testing period is defined as `weeks[training_window+i+1]`. This is the week after (and only the week after) the training window ends.

* These time demarcations are used to declare the `train` and `test` sets.

* The train and test sets are divided into X and y values.

* Scikit-learn's linear regression model is instantiated and fitted to the training data.

* The test period X values are used to predict y values.

* The predicted and actual values of the test period are appended to the `all_predictions` and `all_actual` DataFrames created earlier.


Next, discuss the out-of-sample error metrics:

* What is going on is that the predicted out-of-sample values are compared to the actual values that occurred in that day. We'll compare how this out-of-sample approach predicted, relative to the single training and test window consructed previously.

* To make that comparison, first slice the rolling out-of-sample results to just include 2019.

```python
results_2019 = Results.loc['2019':]
```

* This makes a more "apples to apples" comparison between the two time approaches (since we'll be comparing over the same dates).

Train Test Split Model:
![rolling_gold_01.png](Images/rolling_gold_01.png)

Rolling Out-of-Sample Model:
![rolling_gold_02.png](Images/rolling_gold_02.png)

* Evaluating performance visually, the plot of the out-of-sample results for 2019 shows that gold returns and our model's predictions of gold returns seem to be trending together

* The visual results showing the predicted and actual returns from the single training and test window seem to also trend well together.

* So far, this is a good indication of our model's performance, but we'll have to check the RMSE to get a more solid idea about how well good the predictions from each approach are.

  ```python
  mse = mean_squared_error(
    results_2019["Actual Returns"],
    results_2019["Out-of-Sample Predictions"])
  rmse = np.sqrt(mse)

  ```

* Comparing the two RMSE's, the RMSE from the single training window is 0.73, whereas it is 0.75 from the rolling-out-of-sample model.

  * The rolling-out-of sample approach is an approach more akin to real life (you likely re-estimate your model when new data becomes available)

  * In addition to being more realistic, the rolling-out of sample approach is also more rigorous, as you are testing your model many more times across different time periods

  * Therefore, we expect a slightly higher out-of-sample RMSE, which is what we see.

  * The fact that the two are close to each other in value though does suggest that our model is reasonably stable.

### 13. Instructor Do: Reflect (10 min)

Take a few moments to recap and reflect before ending class:

* We learned that understanding volatility is important in financial forecasting, and we learned a useful model to predict volatility (GARCH).

* We learned about the risks of overfitting, and we learned to select model orders parsimoniously when required.

* We learned to validate a model by splitting a dataset into train and test sets.

* We learned to apply train/test split to a model that continuously updates itself on a rolling basis.

* We learned what time-series data is, and how to build models specifically tailored for the unique challenges inherent in such data.

* We learned how to identify stationary and non-stationary time series data, and which types of models are best for which type.

* Machine learning is really about fitting a model to the data and making predictions with it.

* Most machine learning libraries follow the Model -> Fit -> Predict pattern making it very easy to train and test different models.

* Data Preparation and model evaluation are often the most time consuming and most important part of machine learning.

### 14. End Class
