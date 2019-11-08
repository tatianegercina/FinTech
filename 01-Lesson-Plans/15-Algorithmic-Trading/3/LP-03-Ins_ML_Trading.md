### 3. Instructor Do: Random Forest Trading (15 min)

In this activity, students will learn how to use a set of trading signal features generated from raw BTC/USD data to train a random forest machine learning model that will autonomously make predictions and corresponding trades.

**File:** [random_forest_trading.ipynb](Activities/01-Ins_Random_Forest_Trading/Solved/random_forest_trading.ipynb)

Open the slideshow and quickly discuss the following:

* What is a Random Forest model?

  **Answer:** A Random Forest model is among one of the best supervised algorithms in terms of its ability to predict outcomes. The Random Forest model utilizes a combination of multiple decision tree models to "average away" or minimize the impact of any single decision tree with high variance, thereby creating a more reliable predicted result derived from the strongest features. For example, in regards to portfolio optimization, combining the concept of sharp ratios and portfolio diversification tends to create a portfolio of maximum expected return with minimal variance or risk due to the tendency for non-correlated stock to "cancel" out each other's variances.

* Why is it called a Random Forest?

  **Answer:** A Random Forest model is a combination of many decision tree models with each decision tree or "tree" randomly selecting a subset of the observations and features to train itself on. The result is a final prediction that is an average across this "forest" of random tress.

* How does a Random Forest model work?

  **Answer:** Specifically, a random forest is a collection of bagged decision tree models that split on a subset of features (rather than all the features in the model) at each split. In other words, each decision tree model gets a different view (different data, different variables) and what is left as the final prediction is an average result of all the decision tree models in which the mistakes of each individual tree is "averaged away" with only the strongest features remaining.

Then, open the solution file and discuss the following:

* As always, before proceeding to generating the multiple features or trading signals of the Random Forest model, the following will first have to be done: importing the relevant libraries, reading in the data as a Pandas DataFrame, and preparing/cleaning the data.

  ![data-prep-1](Images/data-prep-1.png)

  ![data-prep-2](Images/data-prep-2.png)

  ![data-prep-3](Images/data-prep-3.png)

  ![data-prep-4](Images/data-prep-4.png)

* The Random Forest model will utilize three trading signal features derived from three different technical indicators, namely an exponential moving average of closing prices, an exponential moving average of daily return volatility, and a Bollinger Band, which is a set of lines representing a (positive and negative) standard deviation away from a simple moving average (SMA) of the asset's closing price.

* In contrast to a simple moving average (SMA), an exponential moving average (EMA) represents a moving average with more weight given to the most recent of prices. Therefore, a short window EMA describes "faster" price action than its long window EMA or "slower" counterpart. The logic then dictates such that when the fast EMA is greater than the slow EMA, a long trade opportunity exists, as price action should rise in the short-term, while a short trade opportunity arises for the opposite scenario.

  ![ema](Images/ema.png)

  ![ema-plot](Images/ema-plot.png)

* Similarly, an exponential moving average of daily return volatility gives more weight to the most recent of daily returns. Therefore, when a short window EMA of daily return volatility is greater than a long window EMA of daily return volatility, the crossover suggests that a long opportunity exists where daily returns are expected to rise, while a short opportunity exists for the opposite scenario where daily returns are expected to fall.

  ![ema-std](Images/ema-std.png)

  ![ema-std-plot](Images/ema-std-plot.png)

* Lastly, a Bollinger Band describes a middle, upper, and lower band, in which the middle is a simple moving average (SMA) of closing prices, while the upper and lower bands describe the rolling standard deviation above and below the SMA, respectively. Therefore, when the asset closing price is less than the lower band, a long opportunity exists as the signal suggests that the price action will tend to move upwards and more in line with where the price *should* be (within the negative standard deviation). A short opportunity exists for the opposite scenario in which the asset closing price is greater than the upper band, suggesting that the price action will tend to move lower and within the positive standard deviation.

  ![bollinger-band.png](Images/bollinger-band.png)

  ![bollinger-band-plot.png](Images/bollinger-band-plot.png)

* After constructing the trading signals or the features of the Random Forest model, the next step is to define the x-variable list, shift the index of the Pandas DataFrame by 1, and construct the dependent variable. The shift ensures that the model will use the current day values to predict the *next* day's outcome--whether the next day will be a positive or negative return.

  ![set-x-var-list-and-shift](Images/set-x-var-list-and-shift.png)

  ![dependent-variable](Images/dependent-variable.png)

* Almost there! The final remaining steps before proceeding to train the Random Forest model is to now define the training and test windows and separate the X and Y training/testing datasets.

  ![training-testing-windows.png](Images/training-testing-windows.png)

  ![x-y-training-datasets](Images/x-y-training-datasets.png)

  ![x-y-testing-datasets](Images/x-y-testing-datasets.png)

* And now for the last piece to the puzzle! After importing the `sklearn` library and associated Random Forest classes, the model is fit with the x and y training data and then used to predict the y values derived from the x test dataset. The results are then shown in the following DataFrame.

  ![random-forest-model](Images/random-forest-model.png)

* The results are then plotted against the actual results (where or not the particular day was a positive or negative return) to show the turnover of the Random Forest model. In other words, the following plot shows how many times the model predicted that a particular day would be positive or negative based off of the features or trading signals.

  ![random-forest-model-plot-1](Images/random-forest-model-plot-1.png)

  ![random-forest-model-plot-2](Images/random-forest-model-plot-2.png)

* And finally, the cumulative return plot related to the strategy employed by the predictive Random Forest model is shown. Unfortunately, the strategy would have lost money from 09-15-2019 to 09-25-2019.

  ![Images/model-cumulative-returns-plot.png](Images/model-cumulative-returns-plot.png)
