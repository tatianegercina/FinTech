# Students Do: Predicting Gold Closing Prices

In this activity, you will gain hands-on experience by building an RNN LSTM for predicting gold closing prices using time-series data.

## Instructions

### Initial Setup

To ensure models' reproducibility, set the random seed for `numpy` and `tensorflow` libraries.

### Data Preparation

In this section, you will retrieve the Gold historical prices from the London Bullion Market Association using the [Quandl API](https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing). Be sure to have your Quandl API key at hand.

#### Data Retrieval

* Import your Quandl API key from an environment variable named `quandl_key`.

* Open the ["Gold Price: London Fixing" at the Quandl website](https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing), and set the URL to retrieve the historical prices of gold in `json` format.

* Use the `requests` library to retrieve the historical prices of gold in `json` format.

* Explore the `json` response data and create a Pandas DataFrame containing the historical prices of gold in all the different currencies provided by the API, and set the data as the index of the DataFrame.

* Your DataFrame should look like the following sample:

  ![Sample gold prices DataFrame](Images/sample-gold-prices-df.png)

**Note:** Remember that while working with time-series data, it's important to transform dates data to `datetime` data type explicitly. Review the [Quandl API documentation for time-series data](https://docs.quandl.com/docs/time-series) if needed.

#### Data Cleaning

Before you continue, corroborate if there are any `null` or missing values in the DataFrame, if so, fill the missing values with the previous price in the series.

**Note:** You may want to review the [Working with missing data guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html) from the Pandas documentation.

#### Create the Features `X` and Target `y` Data

Use the `window_data()` function below to create the features set `X` and the target vector `y`. Define a window size of `30` days and use the column of the closing gold price (`USD (PM)`) for the feature and target column; this will allow your model to predict gold prices in USD.

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

#### Split Data Between Training and Testing Sets

To avoid the dataset being randomized, manually create the training and testing sets using array slicing. Use 70% of the data for training and the remainder for testing.

#### Scale Data with `MinMaxScaler`

Before training the RNN LSTM model, use the `MinMaxScaler` from `sklearn` to scale the training and testing data between `0` and `1`.

**Note:** You need to scale both features and target sets.

#### Reshape Features Data for the LSTM Model

The LSTM API from Keras needs to receive the features data as a _vertical vector_, so you must reshape the `X` data in the form `reshape((X_train.shape[0], X_train.shape[1], 1))`. Both sets, training, and testing should be reshaped.

### Build and Train the LSTM RNN

In this section, you will design a custom LSTM RNN in Keras and fit (train) it using the training data we defined.

You will need to:

1. Define the model architecture in Keras.

2. Compile the model.

3. Fit the model with the training data.

#### Create the LSTM RNN Model Structure

Design the structure of your RNN LSTM as follows:

* Number of units per layer: `30` (same as the window size)

* Dropout fraction: `0.2` (20% of neurons will be randomly dropped on each epoch)

* Add three `LSTM` layers to your model, remember to add a `Dropout` layer after each `LSTM` layer, and to set `return_sequences=True` in the first two layers only.

* Add a `Dense` output layer with one unit.

#### Compile the LSTM RNN Model

Compile the model using the `adam` optimizer, and `mean_square_error` as loss function since the value you want to predict is continuous.

#### Train the Model

Train (fit) the model with the training data using `10` epochs and a `batch_size=90`. Since you are working with time-series data, remember to set `shuffle=False` since it's necessary to keep the sequential order of the data.

### Model Performance

In this section, you will evaluate the model using the test data.

You will need to:

1. Evaluate the model using the `X_test` and `y_test` data.

2. Use the `X_test` data to make predictions.

3. Create a DataFrame of real (`y_test`) vs. predicted values.

4. Plot the real vs. predicted values as a line chart.

#### Evaluate the Model

Use the `evaluate()` method of the model using the testing data.

#### Make Predictions

* Use the `predict()` method of the model to make some closing gold price predictions using your brand new LSTM RNN model and your testing data. Save the predictions in a variable called `predicted`.

* Since you scaled the original values using the `MinMaxScaler`, you need to recover the original gold prices to better understand of the predictions. Use the `inverse_transform()` method of the scaler to decode the scaled testing and predicted values to their original scale.

#### Plotting Predicted Vs. Real Prices

* Create a Pandas DataFrame with two columns as follows to plot the predicted vs. the actual gold prices.

  * Column 1: Actual prices (testing data)

  * Column 2: Predicted prices

* Your DataFrame should look like the sample below:

  ![Sample actual vs. predicted gold prices](Images/sample-gold-prices-predictions-df.png)

* Use the `plot()` method from the DataFrame to create a line chart to contrast the actual vs. the predicted gold prices.

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
