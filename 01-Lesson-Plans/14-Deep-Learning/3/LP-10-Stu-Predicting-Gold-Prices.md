### 10. Students Do: Predicting Gold Closing Prices (30 min)

This activity is a mini-project where students will gain hands-on experience building an RNN LSTM model for time-series data predicting gold closing prices.

**Instructions:**

* [README.md](AActivities/06-Stu_Predict_Gold_Prices/README.md)

**Files:**

* [gold_price_predict.ipynb](Activities/06-Stu_Predict_Gold_Prices/Unsolved/gold_price_predict.ipynb)

---

### 11. Instructor Do: Review Predicting Gold Closing Prices (15 min)

**Files:**

* [gold_price_predict.ipynb](Activities/06-Stu_Predict_Gold_Prices/Solved/gold_price_predict.ipynb)

Open the unsolved version of the Jupyter notebook, live code the solution, and highlight the following:

* In real-world applications, you may need to interact with live data that you should retrieve from an API, that's why we used in this activity the Quandl API.

* As you already know, the safest way to store API keys is using environment variables, so we start by importing our Quandl API key.

  ```python
  # Import the API key for QUANDL
  import os

  quandl_key = os.getenv("QUANDL_API_KEY")
  ```

* In this activity, you were asked to create a model to predict gold prices, so using our API key, we fetch the historical prices of gold up to Yesterday using the Quandl end-point for this price and the `requests` library.

  ```python
  # Set Gold price URL
  request_url = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key="

  gold_prices_url = request_url + quandl_key

  # Fetch Gold prices from QUANDL
  import requests

  response_data = requests.get(gold_prices_url).json()
  ```

* To retrieve the prices of gold, first, we get the keys of the `response_data` dictionary, where we realized that there is only one key called `dataset` that encloses all the data from the API response.

  ![Exploring the gold prices response](Images/explore-gold-prices-response.png)

* After printing the content of the `dataset` key, we can identify that there are two keys with the data we need, these keys are `column_names` and `data`.

  ![Content of the dataset key](Images/dataset-key-content.png)

* As you can imagine, we can also go to the API documentation to understand the structure of the response and identify where is the data we need. However, when you review the [Quandl API documentation for time-series data](https://docs.quandl.com/docs/in-depth-usage), you can see that the name of the main key of the `json` output is `dataset_data`.

  ![Quandl API docs](Images/quandl-api-docs.png)

* This errata in the documentation could be due to a change in the API that is not updated in the documentation jet, that's why sometimes you will need to manually explore the response of an API to identify where the data you need is located.

* Once we identify where the data we need is, we create a DataFrame. It's essential to explicitly cast the `Date` column to `datetime` data type and set this column as the DataFrame index.

  ```python
  # Create a DataFrame with Gold prices
  gold_df = pd.DataFrame(
      response_data["dataset"]["data"],
      columns=response_data["dataset"]["column_names"],
  )

  #Transform the "Date" column to datetime
  gold_df['Date']= pd.to_datetime(gold_df['Date'])

  # Set the "Date" column as the DataFrame Index
  gold_df.set_index("Date", inplace=True)

  # Show the DataFrame head
  gold_df.head()
  ```

  ![Sample gold prices DataFrame](Images/sample-gold-prices-df.png)

* It's important to clean the data before start using it any machine learning model. In this case, we look for missing data by counting all the null values in the DataFrame.

  ![Missing gold prices in the DataFrame](Images/missing-gold-prices.png)

* As you can see, there are `16020` missing prices in the DataFrame, so we will fill these missing values with the gold price of the preceding day using the `fillna()` method of the DataFrame and setting `method=pad`.

  ```python
  # Filling missing values with the previous ones
  gold_df = gold_df.fillna(method ='pad')
  ```

* Once that we cleaned up our data, we will create the features and target set using the custom `window_data()` function we define.

* For this demo, we will use a window size of `30` days, and since we want to predict the gold prices in US Dollars, we will pass `1` as feature and target columns index.

  ```python
  # Define the window size
  window_size = 30

  # Set the index of the feature and target columns
  feature_column = 1
  target_column = 1

  # Create the features (X) and target (y) data using the window_data() function.
  X, y = window_data(gold_df, window_size, feature_column, target_column)
  ```

* Next, to avoid the dataset being randomized, we manually create the training and testing sets using array slicing and defining the 70% of the data for training and the remainder for testing.

  ```python
  # Manually splitting the data
  split = int(0.7 * len(X))

  X_train = X[: split - 1]
  X_test = X[split:]

  y_train = y[: split - 1]
  y_test = y[split:]
  ```

* Before training the RNN LSTM model, we use the `MinMaxScaler` from `sklearn` to scale the training and testing data between `0` and `1`. Note that we scaled the features and the target sets.

  ```python
  # Importing the MinMaxScaler from sklearn
  from sklearn.preprocessing import MinMaxScaler

  # Create a MinMaxScaler object
  scaler = MinMaxScaler()

  # Fit the MinMaxScaler object with the features data X
  scaler.fit(X)

  # Scale the features training and testing sets
  X_train = scaler.transform(X_train)
  X_test = scaler.transform(X_test)

  # Fit the MinMaxScaler object with the target data Y
  scaler.fit(y)

  # Scale the target training and testing sets
  y_train = scaler.transform(y_train)
  y_test = scaler.transform(y_test)
  ```

* As you already know, the LSTM API from Keras needs to receive the features data as a _vertical vector_, so that we reshape the `X` data in the form `reshape((X_train.shape[0], X_train.shape[1], 1))`. Both sets, training, and testing should be reshaped.

  ```python
  # Reshape the features data
  X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
  X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
  ```

* We finally get the data ready to be used by our model, so we will define a three layers RNN LSTM model using `30` units in each layer since this is the size of our time windows, and a dropout fraction of `20%`.

  ```python
  # Define the LSTM RNN model.
  model = Sequential()

  # Initial model setup
  number_units = 30
  dropout_fraction = 0.2

  # Layer 1
  model.add(LSTM(
      units=number_units,
      return_sequences=True,
      input_shape=(X_train.shape[1], 1))
      )
  model.add(Dropout(dropout_fraction))

  # Layer 2
  model.add(LSTM(units=number_units, return_sequences=True))
  model.add(Dropout(dropout_fraction))

  # Layer 3
  model.add(LSTM(units=number_units))
  model.add(Dropout(dropout_fraction))

  # Output layer
  model.add(Dense(1))
  ```

* We compile the model using the `adam` optimizer, and `mean_square_error` as loss function since the value we want to predict is continuous.

  ```python
  # Compile the model
  model.compile(optimizer="adam", loss="mean_squared_error")
  ```

* Now, we will train the model using the training data, `10` epochs, and a batch size of `90`. Remember, it's important to set `shuffle=False` to keep the sequential order of the time-series data.

  ```python
  # Train the model
  model.fit(X_train, y_train, epochs=10, shuffle=False, batch_size=90, verbose=1)
  ```

* Time to assess our model's performance! We will use the `evaluate()` method of the model and the testing data to evaluate the model's performance using the mean square error (MSE) metric we defined.

  ![Mean square error of the model](Images/rnn-lstm-gold-mse.png)

* It seems that the model is not to bad since the MSE is close to zero. Now, we will make predictions using the testing data for further analysis.

```python
# Make predictions using the testing data X_test
predicted = model.predict(X_test)
```

* Since we scaled the original values using the `MinMaxScaler`, we need to recover the original gold prices to better understand of the predictions.

* We will use the `inverse_transform()` method of the scaler to decode the scaled testing and predicted values to their original scale.

  ```python
  # Recover the original prices instead of the scaled version
  predicted_prices = scaler.inverse_transform(predicted)
  real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))
  ```

* Finally, we will create a DataFrame with the decoded values to create a line chart to contrast the predicted vs. the actual values.

  ```python
  # Create a DataFrame of Real and Predicted values
  stocks = pd.DataFrame({
      "Actual": real_prices.ravel(),
      "Predicted": predicted_prices.ravel()
  })
  ```

* Once we create the DataFrame, we can use the `plot()` method of the DataFrame to create the line chart.

  ![Line chart with Actual Vs. Predicted gold prices](Images/actual-vs-predicted-gold-prices.png)

* In this activity, you gained hands-on experience in creating RNN LSTM models to make predictions using time-series data.

* Some other tests can be done, such as varying the time window size, the number of layers in the model, or using different batch sizes for training.

* This fine-tuning of a model's parameters is part of the job that should be done to find the model that fits best to a particular business problem.

Answer any questions before moving on.

---
