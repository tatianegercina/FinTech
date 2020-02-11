### 9. Instructor Do: RNN LSTM and Time Series (20 min)

In this activity, students will learn how to built RNN LSTM models for time series forecasting using Keras.

**Files:**

* [lstm_predictor.ipynb](Activities/05-Ins_LSTM_Time_Series/Solved/lstm_predictor.ipynb)

* [stock_data.csv](Activities/05-Ins_LSTM_Time_Series/Resources/stock_data.csv)

Explain to students that RNN LSTM models can also be used to forecast time-series data, such as stock prices, sales, temperature, or even the heights of ocean tides or sound waves!

Open the unsolved version of the Jupyter notebook; live code the solution and highlight the following:

* At a glance, forecasting time series data using RNN LSTM models could be seen as a three steps process:

  * **Step 1:** Data preparation.

  * **Step 2:** Model building and training.

  * **Step 3:** Model evaluation and predicting new values.

* This activity will use a history of closing prices to predict the next closing price.

* The first step to solving this problem is to prepare the data for the model. This process typically requires the following steps:

  1. Load and clean the data (clean if needed).
  2. Window the data.
  3. Split the data into training and testing datasets.
  4. Scale and Normalize the data with `StandardScaler` or `MinMaxScaler`.
  5. Reshape the inputs for the model.

 When prototyping models, it's a common practice to set the random seed to ensure reproducibility; the random seed is set for `numpy` and `tensorflow` as follows.

  ```python
  from numpy.random import seed
  seed(1)

  from tensorflow import random
  random.set_seed(2)
  ```

* The data is loaded into a Pandas DataFrame. Note that the index is set to the column containing the date of the time series, and the `infer_datetime_format` and `parse_dates` parameters are set to `True`.

  ![Data Prep 1](Images/data-prep-1.png)

Explain to students that the first step towards preparing the data is to create the input features vectors `X` and the target vector `y`.

Explain to students that we will use the `window_data()` function to create these vectors and highlight the following.

```python
def window_data(df, window, feature_col_number, target_col_number):
    """
    This function accepts the column number for the features (X) and the target (y).
    It chunks the data up with a rolling window of Xt - window to predict Xt.
    It returns two numpy arrays of X and y.
    """
    X = []
    y = []
    for i in range(len(df) - window - 1):
        features = df.iloc[i : (i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)
```

* This function chunks the data up with a rolling window of _X<sub>t</sub> - window_ to predict _X<sub>t</sub>_.

* The function returns two `numpy` arrays:

  * `X`: The input features vectors.

  * `y`: The target vector.

* The function has the following parameters:

  * `df`: The original DataFrame with the time series data.

  * `window`: The window size in days of previous closing prices that will be used for the prediction.

  * `feature_col_number`: The column number from the original DataFrame where the features are located.

  * `target_col_number`: The column number from the original DataFrame where the target is located.

Explain to students, that we will predict closing prices using a `5` days windows of previous _T-Bonds_ closing prices, so that, we will create the `X` and `y` vectors by calling the `window_data` function and defining a window size of `5` and setting the features and target column numbers to `2` (this is the column with the _T-Bonds_ closing prices).

![Data Prep 2](Images/data-prep-2.png)

* To create the training and testing dataset, the data is manually split using array slicing to avoid randomizing data when creating the samples. This is because the sequencing of data in time is essential when training the model, so random sampling and shuffling should be avoided.

```python
# Use 70% of the data for training and the remainder for testing
split = int(0.7 * len(X))
X_train = X[: split - 1]
X_test = X[split:]
y_train = y[: split - 1]
y_test = y[split:]
```

Once the training and test datasets are created, explain to students that we need to scale the data before training the LSTM model. We will use the `MinMaxScaler` from `sklearn` to scale all values between `0` and `1`. Note that because this is a regression problem (we are predicting a closing price), we scale both the features **AND** the target data. If the output target were categorical, the `y` data would not need to be scaled.

```python
# Use the MinMaxScaler to scale data between 0 and 1.
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
scaler.fit(y)
y_train = scaler.transform(y_train)
y_test = scaler.transform(y_test)
```

Explain to students that the LSTM API from Keras needs to receive the features data as a _vertical vector_  so that we need to reshape the `X` data in the form `reshape((X_train.shape[0], X_train.shape[1], 1))`. Both sets, training, and testing are reshaped.

```python
# Reshape the features for the model
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
```

Once we prepare the data, explain to students that we are now going to build and train an LSTM RNN model using TensorFlow and Keras.

* The LSTM RNN model in Keras uses the `Sequential` model and the `LSTM` layer as we did before. However, there is a new type of layer called `Dropout`.

* The `Dropout` layer refers to a regularization technique for reducing overfitting in neural networks. It only drops a certain percentage of the connections to avoid overfitting.

Open the lesson slides, and move to the _Introduction to Dropout_ section to give a brief explanation about this concept to the class.

* For simplicity, the concept of dropout will be explained using a simple neural network design with just one layer.

* Dropout consists of removing units from the hidden layers. It achieves this by randomly selecting a fraction of the hidden nodes and sets their output to zero, regardless of the input. Dropout effectively removes those connections from contributing to the decision logic.

* The dropout layer will randomly select a different subset of units for each training input.

* In Keras, a dropout is implemented by adding a layer after each `LSTM` layer and defining the fraction of nodes to drop as the layer parameter.

Switch back to the Jupyter notebook and continue the solution:

```python
# Define the LSTM RNN model.
model = Sequential()

number_units = 5
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

* To create an LSTM RNN model, we will add `LSTM` layers.

* The `return_sequences` parameter needs to set to `True` every time we add a new `LSTM` layer, excluding the final layer. This is just how Keras knows to connect each layer.

* The `input_shape` is the number of time steps and the number of indicators. In this example, the number of time steps is equal to the window specified earlier (5), while the number of indicators is related to how many input features are used to predict the final price. In this case, only the past five closing prices are used to predict the next closing price, so the input shape is `(5, 1)`. Another way to remember this is `input_shape=(window_size, number_of_features)`.

* After each `LSTM` layer, we add a `Dropout` layer to prevent overfitting.

* The parameter passed to the `Dropout` layer is the fraction of nodes that will be drop on each epoch.

* For this demo, we will use a dropout value of `0.2`. It means that on each epoch, we will randomly drop `20%` of the units.

* The number of units in each `LSTM` layers, is equal to the size of the time window, in this demo, we are taking five previous `T-Bonds` closing prices to predict the next closing price.

Explain to students that the optimizer and loss parameters need to be specified to compile the model. For a regression problem, a good starting choice for these parameters is to use `adam` for the optimizer and `mean_squre_error` for the loss function. Further information about these can be found on [the Keras API for TensorFlow website(https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)].

```python
# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")
```

* Once the model is defined, we train (fit) the model using 10 epochs.

  ```python
  # Train the model
  model.fit(X_train, y_train, epochs=10, shuffle=False, batch_size=1, verbose=1)
  ```

* Since we are working with time-series data, it's important to set `shuffle=False` since it's necessary to keep the sequential order of the data.

* We can experiment with the `batch_size` parameter; however, the smaller batch size is recommended; in this demo, we will use a `batch_size=1`.

Explain to students that after training the model, it's time to evaluate our model to assess its performance.

* We will use the `evaluate()` method using the testing data.

  ```python
  # Evaluate the model
  model.evaluate(X_test, y_test)
  ```

* To better understand the model evaluation results, we will make some predictions and plot the predicted vs. the real prices.

  ```python
  # Make some predictions
  predicted = model.predict(X_test)
  ```

* Since we scaled the original values using the `MinMaxScaler`, we need to recover the original prices to better understand of the predictions.

* We will use the `inverse_transform()` method of the scaler to decode the scaled values to their original scale.

  ```python
  # Recover the original prices instead of the scaled version
  predicted_prices = scaler.inverse_transform(predicted)
  real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))
  ```

* To plot the predicted vs. the real values, we will create a DataFrame.

  ![model-eval-1](Images/model-eval-1.png)

* Finally, we plot the predicted vs. real prices using the `plot()` method of the DataFrame.

  ![model-eval-2](Images/model-eval-2.png)

After creating the plot, ask students the following question and conduct a brief discussion about the results:

* Will you trust in this model to predict prices?

  * **Sample Answer:** It's difficult to trust in this model as is because the error between the real and predicted values looks big.

Explain that if you wanted to use this model despite the initial error size, it might be useful to re-run the notebook using different iterations of training and testing data. Be sure to re-run the experiment without the random seed to gain additional randomness in the experiment.

Finally, explain to students that this model could be enhanced as follows:

* We can test different window sizes, for example, from `5` to `10`.

* We can test different dropout parameters, for example, between `0.2` and `0.5`.

* We may want to add or remove additional LSTM layers.

* When training the model, we can test different batch sizes and adjust the training epochs.

Answer any questions before moving on.

---
