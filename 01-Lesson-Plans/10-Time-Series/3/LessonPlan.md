# 10.3 Lesson Plan: Volatility and Beyond

### Overview

Today's class will round out time series modeling with GARCH. Students will also gain exposure to the theory and practice of model validation.

### Class Objectives

By the end of this class, students will be able to:

* Create a time series linear regression model using Scikit-learn.

* Analyze and predict seasonal effects using regression.

* Quantify the accuracy of a linear regression model.

* Define overfitting and articulate the benefits of parsimony.

* Use Scikit-learn to train and test time series data.

* Make out-of-sample predictions in rolling windows.

* Evaluate the accuracy of out-of-sample predictions.

- - -

### Instructor Notes

* Slack out the [imblearn Installation Guide](../../11-Classification/Supplemental/Machine_Learning_Env_Setup_Guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* Through longer activities, students will consolidate their skills from the previous two days, creating financial models in multiple steps, from stationarizing data to identifying model orders to making predictions on future values and volatility. You and your TAs should be on the lookout for your weaker students during the longer activities. Make sure that such students do not flounder.

* Your students will also learn to validate models by training and testing data. Emphasize that this will be a valuable skill in later units as they dive more deeply into machine learning.

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [10.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=57855d94-d1e5-4334-a4bd-aadb010f656c) Note that this video may not reflect the most recent lesson plan.


### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1dpPDlLWNX3j-riUXrBoXQEOUn1l025swCYmP1aGKc1M/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

In this section, you will give a broad overview of today's class.

Welcome students to the last day of the time series unit, and briefly summarize key concepts from the previous days:

* Auto-correlation is an important feature of many time series datasets.

* Stationarity of a time series can determine the time series model.

* ARMA models use past values and past errors to predict future values. An ARMA model assumes stationarity.

* ARIMA is similar to ARMA, but does not assume stationarity.

Describe to students what they will be doing today:

* They will learn to quantify the accuracy of a linear regression model.

* They will learn to use processes to make a time series easier to model.

* They will encounter the concept of parsimony in models, an important idea in machine learning.

* They will learn to validate models by training and testing them.

* They will learn to create a model that can continuously update itself.

- - -

### 2. Instructor Do: Introduction to Linear Regression (15 min)

**File:**

* [linear_regression.ipynb](Activities/01-Ins_Linear_Regression/Solved/linear_regression.ipynb)

In this activity, you will explain linear regression to the class and demonstrate using Scikit-learn to create a linear regression model.

Use the slides to explain the linear equation:

  ```
  y = mx + b
  ```

  * This equation describes, or models, the relationship between variables x and y.

  * As x increases, y increases.

  * How fast y increases in relation to x is called the slope.

  * Slope is represented by the letter `m` in the equation.

  * The value of `y` when `x` is 0 is called the y-intercept. It is represented by the letter `b`.

Ask whether, on visual inspection, a trend exists:

  ![Images/linear_regression01.png](Images/linear_regression01.png)

  * `y` increases as `x` increases.

Explain that a line that best fits the trend can be drawn:

  ![Images/linear_regression02.png](Images/linear_regression02.png)

  * This line is called the best fit line, and computing it is called linear regression.

  * The equation is simple but tedious, and is best solved by a computer.

Explain that, in other words, linear regression identifies the line that best predicts `y` based on the value of `x`.

Explain the concept of residuals.

  * Even a best fit line that captures the data well is seldom, if ever, perfect.

  * A residual is the difference between the **predicted** value of `y` and its **actual** value.

  * Linear regression seeks to minimize the **square** value of residuals.

Summarize the key points of linear regression:

  * It models data with a linear trend. It is not useful when the data does not follow a linear trend, e.g., exponential trends.

  * Based on the X values, it predicts Y values.

  * It does not do a good job of describing non-linear patterns. We will cover techniques to model non-linear data later in the course.

Now that students understand linear regression conceptually, walk through the steps of performing linear regression in Python. Here are some introductory remarks:

  * The CSV contains data on years of job experience and salary.

  ![Images/linear_regression03.png](Images/linear_regression03.png)

  * We will use Scikit-learn, a machine learning library, to create a linear regression model.

Engage the class by asking, in a linear regression model, which column will be the dependent variable, and which the independent variable.

  * `YearsExperience` will be the independent variable, or `x`.

  * `Salary` will be the independent variable, or `y`.

Explain that in order to use Scikit-learn (sklearn) for regression, the independent variable (x) will need to be reformatted:

  ```python
  X = df.YearsExperience.values.reshape(-1, 1)
  ```

  * Scikit-learn cannot take in a pandas Series directly.

  * `reshape(-1, 1)` reshapes, or formats, the data.

  * `X.shape` returns `(30,1)`, meaning that `X` has 30 rows and 1 column of data.

  * The dependent variable can remain a pandas series, as seen by `y = df.Salary`.

Walk through the boiler plate code:

  ```python
  model = LinearRegression()
  model.fit(X,y)
  ```

  * A linear regression model is created (instantiated) using Scikit-learn, and the data are fit into the model.

Explain how to obtain the parameters of the model, its slope and y-intercept:

  ```python
  print(model.coef_)
  print(model.intercept_)
  ```

  * Again, Scikit-learn creates a linear equation model based on the data (y = mx + b).

  * `model.coef_` is the slope of the equation.

  * `model.intercept_` is the y-intercept.

Explain that the power of a linear regression model comes from its ability to describe and to predict.

  ```python
  predicted_y_values = model.predict(X)
  ```

  * This line creates an array of predicted y values based on x values.

  * In other words, if given an x-value (years of experience) that is not in the data set, the model will predict the corresponding y-value (salary).

Use the slideshow and recapitulate the linear regression plot below, which we have seen previously:

  ![Images/error01.png](Images/error01.png)

* The blue dots are a scatter plot of data points (years of experience vs salary).

* The red line is the best fit line. It represents the linear regression model.

* The distance between each data point and the best fit line is referred to as the error.

Explain that the linear regression model is mathematically constructed to **minimize** the sum of all the errors after they have been squared.

  ![Images/error01.jpg](Images/error02.jpg)

Explain that one way to assess the accuracy of a linear regression model is to look at the errors:

* The **mean squared error**, or **MSE**, as the name states, is the average of the square of the errors of the dataset. It is the variance of the errors in the dataset.

* The **root mean square error**, or **RMSE**, is simply the square root of the MSE. It is therefore the standard deviation of the errors in the dataset.

* Lower MSE and RMSE scores, of course, indicate a more accurate model.

Explain that R2, or r-square, is a way to assess the relationship between two variables.

* The correlation coefficient is a numerical description of the extent to which the two variables move together. It ranges from -1 to 1.

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

* The RMSE exceeds the standard deviation, indicating that the model may not be very helpful. In other words, on average, there are wider swings in the error than the measured temperatures.

- - -

### 3. Students Do: House Regression (15 min)

In this activity, students will perform linear regression on the number of rooms in houses versus their prices.

**Files:**

* [README.md](Activities/02-Stu_House_Regression/README.md)

* [USA_Housing.csv](Activities/02-Stu_House_Regression/Resources/USA_Housing.csv)

- - -

### 4. Instructor Do: Review House Regression (10 min)

**Files:**

* [housing.ipynb](Activities/02-Stu_House_Regression/Solved/housing.ipynb)

Open the solution, and complete a dry walkthrough of the code:

* Linear regression models can be implemented using the Scikit-learn package. A LinearRegression module is included and can be imported into the Python environment.

  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  ```

  ![scikit-learn.png](Images/scikit-learn.png)

* In order to create a linear regression model, **x** and **y** values must be identified. In this case, **x** will be the number of rooms in the house, and it will be reshaped. This will ensure the model is fitted to the data.

  ```python
  X = df.index.values.reshape(-1,1)
  y = df['Price']

  model.fit(X,y)
  predicted_y_values = model.predict(X)
  ```

  ![model_predict.png](Images/model_predict.png)

* The `model.predict()` function can be used to implement predictive analysis. The function will return an array of predicted y-values. This data can then be plotted using a **scatter** plot to highlight the correlation.

  ```python
  # Plot the results. The best fit line is red.
  plt.scatter(X, y)
  plt.plot(X, predicted_y_values, color='red')
  ```

  ![scatter_plot.png](Images/scatter_plot.png)

* The `model` object can be used to then extract the model coefficient (slope), y intercept, and model score. This can be done using the `coef_`, `intercept_`, and `score` attributes/functions.

  ![model_attributes.png](Images/model_attributes.png)

If time remains, ask students some of the following review questions:

* What is the purpose behind a linear regression model?

  * **Answer** Linear regression is used to perform predictive analysis.

* What type of relationship does linear regression explore?

  * **Answer** The relationship between dependent and independent variables.

* What makes a **scatter** plot a good plot to use for visualizing linear regressions?

  * **Answer** Both linear regression models and scatter plots emphasize the relationships and impact of two or more variables.

Ask if students have any questions before moving forward.

- - -

### 5. Instructor Do: Time Series Linear Regression (15 min)

**Files:**

* [time_series_simple_regression.ipynb](Activities/03-Ins_Time_Series_Linear_Regression/Solved/time_series_simple_regression.ipynb)

Inform the class that the idea of linear regression for time series is the same as in the previous example, but that the implementation requires a few tweaks.

Open the notebook and show the data frame:

* This is a data frame of weather data in Austin, TX in 2010.

* The data frame has been sliced to contain data from May through July of 2010.

  ![Images/ts_regression01.png](Images/ts_regression01.png)

Show the Temperature column plotted against the date:

  ![Images/ts_regression02.png](Images/ts_regression02.png)

Explain that the goal is to perform a linear regression of temperature and the date.

Explain the next three lines of code. As seen before, Scikit-learn's models require that the `X` variable be formatted in the correct shape.

![X variable formatted](Images/10_5_img1.png)

* Converting the column into a data frame gives it `2208` rows and `1` column of data.

Explain that datetime objects have attributes, such as the week of the year.

  ```python
  X['Week_of_Year'] = X.index.weekofyear
  ```

* This creates a new column, called `Week_of_Year`.

* `X.index` is in `datetime` format, and has attributes such as `dayofyear`, `weekofyear`, etc. that can be extracted from it.

* More attributes can be found in the [documentation](https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DatetimeIndex.html)

Explain creating dummy variables. The `pd.get_dummies()` method creates a column for each week of the year, and for each row assigns a numerical value for that week.

  ```python
  X_binary_encoded = pd.get_dummies(X, columns=['Week_of_Year'])
  ```

* Dummy variables are necessary because weeks are not continuous; they are categorical.

* As an example, week 17 of the year is assigned 1 for week 17, but 0 for all other weeks.

  ![Images/ts_regression03.png](Images/ts_regression03.png)

Use the slides to show the regression equation that results from the process:

  ![Images/regression_equation01.gif](Images/regression_equation01.gif)

* Each week is given its own weight in the overall equation.

* Because each week is a separate variable in the equation, this is called multiple regression.

Additionally, explain that we delete the extraneous column in the data frame created by `pd_get_dummies()`. The argument `axis=1` specifies that it is the column that is dropped. (For rows, it would be `axis=0`.)

  ```python
  X_binary_encoded = X_binary_encoded.drop('Temperature', axis=1)
  ```

Explain that the rest of the code is familiar from previous examples:

  ```python
  y = df['Temperature'].copy()
  model = LinearRegression()
  results = model.fit(X_binary_encoded, y)
  predictions = model.predict(X_binary_encoded)
  ```

  * The `Temperature` column is specified as the dependent variable array `y`. The `copy()` method is used to create a copy of a Pandas object, to ensure that no unwanted changes are made to the original data.

  * A model is created and fits the independent and dependent variables.

  * An array of predictions is created using `model.predict()`.

Explain that the metrics of the linear regression model are generated:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  import numpy as np
  r2 = r2_score(y, predictions)
  mse = mean_squared_error(y, predictions)
  rmse = np.sqrt(mse)
  ```

Note that the r-square value, at `0.23`, is fairly low and that we will cover the interpretation of these numbers in an upcoming activity.

Note also that the trend appears at least somewhat linear for the specified timeline, but that a longer timespan, say from January through December, will not be good for a linear regression model.

  * This underscores the importance that linear regression, rather than a mechanical process, requires thinking about the variables.

  * It also highlights the importance of plotting the data before reaching a conclusion!

Take a moment to summarize the key points of this activity:

  * The idea is the same as before. We use Scikit-learn to create a model of the independent variable (X) and the dependent variable (y).

  * Because datetime data cannot be directly imported into a Scikit-learn model, we've had to create a binary encoding for each row, and drop an unnecessary column.

Answer any questions before moving on.

- - -

### 6. Students Do: Oil Futures (15 min)

In this activity, students will identify seasonal effects in oil futures prices with linear regression.

**Files:**

* [README.md](Activities/04-Stu_Time_Series_Linear_Regression/README.md)

* [oil_futures_starter.ipynb](Activities/04-Stu_Time_Series_Linear_Regression/Unsolved/oil_futures.ipynb)

- - -

### 7. Instructor Do: Review Oil Futures (5 min)

**Files:**

* [oil_futures.ipynb](Activities/04-Stu_Time_Series_Linear_Regression/Solved/oil_futures.ipynb)

Explain that, rather than the settle prices, we're working with returns, the daily change of the settle price in percentage terms. The returns are multiplied by 100 to make the numbers easier to work with.

  ```python
  returns = df.Settle.pct_change() *100
  ```

  ![seattle_returns.png](Images/seattle_returns.png)

Explain that we need a column of returns, and lagged returns, which will be regressed:

  ```python
  df['Return'] = returns.copy()
  df['Lagged_Return'] = returns.shift()
  df = df.dropna()
  ```

  * Here, unlike previous examples with two separate variables, `Return` values are regressed against `Lagged_Return` values. This is called autoregression and will be further discussed on day 2.

  * A column of lagged returns is created by shifting each value downward by 1 row.

  * NaN values must be dropped.

Go over the steps of preparing the data to use in Scikit-learn:

  ```python
  X = df['Lagged_Return'].to_frame()
  X['Week_of_year'] = X.index.weekofyear
  ```

  * Creating the `X` data frame with `to_frame()` shapes the data in requisite shape, and it returns a usable datetime index.

  * The `weekofyear` attribute is used to create a column for the week of the year.

Next, explain that dummy variables are created for each week of the year. Communicate that the function creates dummy variables for each week. That is, it assigns a value of 0 or 1 for each week. For a date that falls on week 7, for example, it will assign 1 for week 7 and 0 to all other weeks.

  ```python
  X_binary_encoded = pd.get_dummies(X, columns=['Week_of_year'])
  ```

  ![get_dummies.png](Images/get_dummies.png)

* Quickly go through the rest of the code, which is boilerplate and includes creating a regression model that is created on lagged returns and returns, making predictions, and then generating r-square value.

  ```python
  y = df['Return']
  model = LinearRegression()
  res = model.fit(X_binary_encoded, y)
  predictions = model.predict(X_binary_encoded)
  r2 = r2_score(y, predictions)
  ```

  ![model_2.png](Images/model_2.png)

- - -

### 8. Break (40 min)

- - -

### 9. Instructor Do: Overfitting and Parsimony (10 min)

Open the slideshow and introduce the concept of overfitting:

* Overfitting occurs when a model is too specific to a particular data set.

* An overfitted model memorizes the random patterns of the training data too well. It memorizes the quirks of a dataset without identifying the underlying patterns.

* Consequently, such a model will perform poorly when it encounters new data with similar underlying patterns, but with different quirks.

* In other words, overfit models learn the noise found in the training data, rather than just the signal.

* Because models are optimized to limit the training error, they can become too focused on the unique patterns of the training data, and fail to extend to previously unseen data.

Explain that overfitting typically involves an excessive number of variables in a model.

*  With more parameters, the model can memorize the rare patterns of the training data, resulting in a rigid model that does not generalize well.

Explain that a useful analogy might be to memorize the answers to a math test without learning the underlying principles.

* The learning that takes place is useful in one particular setting but is less generalizable to other contexts.

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

- - -

### 10. Instructor Do: Train, Test, Split (10 min)

**File:**

* [train_test.ipynb](Activities/05-Ins_Train_Test/Solved/train_test.ipynb)

Inform your students that they will now learn to minimize the problems posed by overfitting.

Explain that a common strategy used in machine learning is to split a dataset into a train set and a test set.

* With the training set, the model learns the relevant patterns in the data. The model seeks to minimize errors in the training data.

* Then the testing set is used to evaluate the model's performance on unseen data.

* If the model underperforms with the testing set, the model can be retrained with better (or more) data, or the model itself can be tweaked.

Remind your students that we have worked with a number of models so far, including ARMA, ARIMA, GARCH, and linear regression:

* Models were trained on the entire dataset, then made predictions.

* We will now split a dataset into training and testing data and run a linear regression on them.

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

* In regression, the lagged returns will be the **independent** variable, and the returns will be the **dependent** variable since we are attempting to answer to what extent, past values affect future values. It is like asking the question: given today's return, what's the expected return going to be tomorrow?

Explain that the next step is to split the dataset into `train` and `test` sets:

  ```python
  train = df.loc['2008':'2012']
  test = df.loc['2013']
  ```

* The `loc[]` accessor is used to assign the data from years 2008 through 2012 to the testing set, and 2013 data to the testing set.

* In machine learning, data is typically randomly assigned to training and test sets. That is, any given data point might be assigned to the training set, or it might be assigned to the testing set. This is possible because each data point is independent of another.

* However, in a time series in which autocorrelation exists, that is not possible. Instead, data points prior to a cutoff point comprise the training set, and all points that come after comprise the testing set.

* Another common practice is to assign 80% of the data to the training set, and 20% to the testing set. Oftentimes, with time-series data, it is good to specify the date ranges explicitly.

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

- - -

### 11. Students Do: Ripple (15 min)

In this activity, students will create GARCH and linear regression models for the price of Ripple (XRP), a cryptocurrency. They will validate the latter model with training and test sets.

**Files:**

* [README.md](Activities/06-Stu_Ripple/README.md)

* [USD_per_Ripple_XRP_prices.csv](Activities/06-Stu_Ripple/Resources/USD_per_Ripple_XRP_prices.csv)

* [xrp.ipynb](Activities/06-Stu_Ripple/Unsolved/xrp.ipynb)

- - -

### 12. Instructor Do: Review Activity (10 min)

A detailed walk-through of the code is given below. However, in the interest of time, use your judgment to highlight the major points and gloss over parts students have seen repeatedly.

**File:**

* [xrp.ipynb](Activities/06-Stu_Ripple/Solved/xrp.ipynb)

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

Go over the metrics of the in-sample and out-of-sample predictions:

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

  * The out-of-sample RMSE is lower than the in-sample RMSE. RMSE is typically lower for training data but is higher in this case.

  * This could be due to the fact that our out-of-sample period is small, so just by chance, the model happened to do better out-of-sample than in-sample.

Ask for any remaining questions before moving on.

- - -

### 13. Instructor Do: Rolling Out-of-Sample (15 min)

**File:**

* [sp500.ipynb](Activities/07-Ins_Rolling_Out_of_Sample/Solved/sp500.ipynb)

Point out that up to this point, we have created models as a one-shot affair. Explain that we will go over a procedure that allows an analyst to update the financial model as new data continues to come in.

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

* `weeks[0]` is the first week of the data frame. In this example, the start of the training period is `2007-12-31` and the end of the training period is `2008007-06`.

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

* The `timeframe` variable refers to the total time span encompassed by the data frame, minus the training window of 26 weeks (minus 1 due to indexing).

* The last training window will, therefore, begin 26 weeks before the end of the total time span. If there were to be a training window after this point, it would be less than the full 26 weeks, and the Python code would throw an out-of-bounds error.

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

* The `X_train` and `X_test` series are converted into a DataFrame.

* A model is created for each training period, then fitted to the data.

* The test set is used to create predictions.

* Then the predicted and actual data are appended to `all_predictions` and `all_actuals` data frames during each iteration.

Reassure students that they will be able to use this notebook as a reference for future calculations.

- - -

### 14. Students Do: Rolled Gold (15 min)

In this activity, students will perform predictions with linear regression on a rolling out-of-sample basis, in order to predict the price of gold.

**Files:**

* [README.md](Activities/08-Stu_Rolled_Gold/README.md)

* [gold_price.csv](Activities/08-Stu_Rolled_Gold/Resources/gold_price.csv)

* [gold.ipynb](Activities/08-Stu_Rolled_Gold/Unsolved/gold.ipynb)

- - -

### 15. Instructor Do: Review Rolled Gold (10 min)

**File:**

* [gold.ipynb](Activities/08-Stu_Rolled_Gold/Solved/gold.ipynb)

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

* What is going on is that the predicted out-of-sample values are compared to the actual values that occurred in that day. We will compare how this out-of-sample approach predicted, relative to the single training and test window constructed previously.

* To make that comparison, first slice the rolling out-of-sample results to just include 2019.

```python
results_2019 = Results.loc['2019':]
```

* This makes a more "apples to apples" comparison between the two time approaches (since we will be comparing over the same dates).

Train Test Split Model:
![rolling_gold_01.png](Images/rolling_gold_01.png)

Rolling Out-of-Sample Model:
![rolling_gold_02.png](Images/rolling_gold_02.png)

* Evaluating performance visually, the plot of the out-of-sample results for 2019 shows that gold returns and our model's predictions of gold returns seem to be trending together

* The visual results showing the predicted and actual returns from the single training and test window seem also to trend well together.

* So far, this is a good indication of our model's performance, but we'll have to check the RMSE to get a more solid idea about how well good the predictions from each approach are.

  ```python
  mse = mean_squared_error(
    results_2019["Actual Returns"],
    results_2019["Out-of-Sample Predictions"])
  rmse = np.sqrt(mse)

  ```

* Comparing the two RMSE's, the RMSE from the single training window is 0.73, whereas it is 0.75 from the rolling-out-of-sample model.

  * The rolling-out-of sample approach is an approach more akin to real-life (you likely re-estimate your model when new data becomes available)

  * In addition to being more realistic, the rolling-out of sample approach is also more rigorous, as you are testing your model many more times across different time periods

  * Therefore, we expect a slightly higher out-of-sample RMSE, which is what we see.

  * The fact that the two are close to each other in value, though, does suggest that our model is reasonably stable.

Congratulate the class for making it through their first week of Machine Learning! This is a very valuable skill that is currently changing the face of finance.

- - -

### 16. Instructor Do: Career Services Lesson (35 min)

**Note:** If you are teaching this lesson on a weeknight, save this section for the next Saturday class.

Explain to students that now that they have completed their first projects and are starting to learn new things such as machine learning, it is time to think about updating resumes to showcase these valuable skills!

Use the following lesson plan to discuss the Career Services content for this week.

**Files:**

* [Career Services Lesson Plan](Career_Services_LessonPlan.md)

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
