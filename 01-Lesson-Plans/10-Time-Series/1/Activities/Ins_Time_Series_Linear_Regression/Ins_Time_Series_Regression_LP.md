### Instructor Do: Time Series Linear Regression (0:10)

* Inform the class that the idea of linear regression for time series is the same as in the previous example, but that the implementation requires a tweak or two.

* Open the [notebook](time_series_linear_regression.ipynb) and show the data frame:

  * This is a data frame of weather data in Austin, TX in 2010.

  * The data frame has been sliced to contain data from May through July of 2010.

  ![Images/ts_regression01.png](Images/ts_regression01.png)

* Show the Temperature column plotted against the date:

  ![Images/ts_regression02.png](Images/ts_regression02.png)

* Explain that the goal is to perform linear regression of temperature and the date.

* Explain the next two lines of code:

  ```python
  X = df['Temperature'].to_frame()
  X.shape
  ```

  * As seen before, scikit-learn's models require that the X variable be formatted in the correct shape.

  * Converting the column into a data frame gives it 2208 rows and 1 column of data.

* Explain that datetime objects have attributes, such as day of the year.

  ```python
  X['Day_of_Year'] = X.index.dayofyear
  ```

  * This creates a new column, called `Day_of_Year`.

  * `X.index` is in datetimeformat, and has attributes such as `dayofyear`, `weekofyear`, etc. that can be extracted from it.

  * More attributes can be found in the [documentation](https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DatetimeIndex.html)

* Explain that for time series, scitkit-learn requires converting the datetime type of the data (in this case, the data frame index) to floating point type.

  ```python
  X_binary_encoded = pd.get_dummies(X, columns=['Day_of_Year'])
  ```

  * The `pd.get_dummies()` method creates a column for each day of the year, and for each row assigns a binary value for that day.

  * This creates a useable array of the dates.

  ![Images/ts_regression03.png](Images/ts_regression03.png)

* Additionally, explain that we delete the extraneous column in the data frame created by `pd_get_dummies()`:

  ```python
  X_binary_encoded = X_binary_encoded.drop('Temperature', axis=1)
  ```

  * The argument `axis=1` specifies that it is the column that is dropped.

* Explain that the rest of the code is familiar from previous examples:

  ```python
  y = df['Temperature'].copy()
  model = LinearRegression()
  results = model.fit(X_binary_encoded, y)
  predictions = model.predict(X_binary_encoded)
  ```

  * The `Temperature` column is specified as the dependent variable array.

  * A model is created, and fits the independent and dependent variables.

  * An array of predictions is created using `model.predict()`.

* Explain that the metrics of the linear regression model are generated:

  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  import numpy as np
  r2 = r2_score(y, predictions)
  mse = mean_squared_error(y, predictions)
  rmse = np.sqrt(mse)
  ```

* Note that the R-squared value, at 0.23, is fairly low, and that we will cover the interpretation of these numbers in the next activity.

* Note also that the trend appears at least somewhat linear for the specified timeline, but that a longer timespan, say from January through December, will not be good for a linear regression model.

  * This underscores the important that linear regression, rather than a mechanical process, requires thinking about the variables.

* Take a moment to summarize the key points of this activity:

  * The idea is the same as before. We use scikit-learn to create a model of the independent variable (X) and the dependent variable (y).

  * Because datetime data cannot be directly imported into a scikit-learn model, we've had to create a binary encoding for each row, and drop an unnecessary column.

* Finally, if time allows, quickly demonstrate an approximate visualization of the linear regression best fit line.

  ![Images/ts_regression04.png](Images/ts_regression04.png)

  * Because of the difficulty of generating a visualization directly from a data frame of binary encodings (`X_binary_encoded`), the original data frame was grouped by day, and the mean for each day obtained.

  * A new linear regression model was created with this data, and a visualization created.

  * We will not go over the code, but students may wish to do so on their own time.
