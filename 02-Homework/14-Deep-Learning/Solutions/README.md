# LSTM Stock Predictor

Due to the volatility of cryptocurrency speculation, investors will often try to incorporate sentiment from social media and news articles to help guide their trading strategies. One such indicator is the [Crypto Fear and Greed Index](https://alternative.me/crypto/fear-and-greed-index/) which attempts to use a variety of data sources to produce a daily FNG value for cryptocurrency. You have been asked to help build and evaluate deep learning models using both the FNG values and simple closing prices to determine if the FNG indicator provides a better signal for cryptocurrencies than the normal closing price data. 

In this assignment, you will use deep learning recurrant neural networks to model Bitcoin closing prices. One model will use the FNG indicators to predict the closing price while the second model will use a window of closing prices to predict the nth closing price. 

You will need to:

1. Prepare the data for training and testing
2. Build and train custom LSTM RNNs
3. Evaluate the performance of each model


1. Prepare the data for training and testing

Use the starter code as a guide to create a Jupyter notebook for each RNN. The starter code contains a function to help window the data for each dataset. 

For the Fear and Greed model, you will use a 10 day rolling window of the FNG values to try and predict the 11th day closing price. 

For the closing price model, you will use a 10 day rolling window of closing prices to try and predict the 11th day closing price.

Each model will need to use 70% of the data for training and 30% of the data for testing.

Apply a MinMaxScaler to the X and y values to scale the data for the model. 

Finally, reshape the X_train and X_test values to fit the model's requirement of (samples, time steps, features).


2. Build and train custom LSTM RNNs

In each Jupyter notebook, create the same custom LSTM RNN architecture. In one notebook, you will fit the data using the FNG values. In the second notebook, you will fi thte data using only closing prices. 

Use the same parameters and training steps for each model. This is necessary to accurately compare each model.

3. Evaluate the performance of each model

Finally, use the testing data to evaluate each model and compare the performance.

Which model has a lower loss?

Which model tracks the actual values?