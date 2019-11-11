### 1. Instructor Do: Random Forest Trading (15 min)

In this activity, students will learn how to generate a set of trading signal derived from raw BTC/USD data that will be used as features to train a Random Forest machine learning model that will autonomously make predictions and corresponding trades.

**File:** [trading_signal_features.ipynb](Activities/01-Ins_Trading_Signal_Features/Solved/trading_signal_features.ipynb)

First, quickly introduce the following:

* Now that students have learned to generate trading signals, backtest their trading strategies, and evaluate their results, it is now time to incorporate machine learning into the mix! Students will now have the opportunity to use a machine learning model (Random Forest) to correctly predict next day positive or negative returns based off of multiple trading signals.

* The Random Forest model will require multiple features, or in this case, multiple trading signals to train itself on. Therefore, students will learn to generate multiple trading signals using various technical indicators such as an exponential moving average of closing prices, exponential moving average of daily return volatility, and Bollinger Bands, which is are a set of lines representing a (positive and negative) standard deviation away from a simple moving average (SMA) of the asset's closing price.

Then, open the solution file and discuss the following:

* As always, before proceeding to generating the multiple features or trading signals of the Random Forest model, the following will first have to be done: importing the relevant libraries, reading in the data as a Pandas DataFrame, and preparing/cleaning the data.

  ```python
  # Import libraries and dependencies
  import pandas as pd
  import numpy as np
  from pathlib import Path
  %matplotlib inline
  ```

  ```python
  # Set path to CSV and read in CSV, then set index as `Timestamp`
  csv_path = Path('../Resources/kraken_btc_1hr.csv')
  btc_df=pd.read_csv(csv_path)
  btc_df
  ```

  ```python
  btc_df.set_index(pd.to_datetime(btc_df['Timestamp'], infer_datetime_format=True), inplace=True)
  btc_df.drop(columns=['Timestamp'], inplace=True)
  btc_df
  ```

* Then, in order to calculate the exponential moving average of daily return volatility (2nd trading signal), we will of course need prepare the DataFrame by calculating the daily returns of BTC/USD closing prices. Using the `dropna` function to drop any rows with NA values is a generally good practice.

  ```python
  # Drop NAs and calculate daily percent return
  btc_df['daily_return'] = btc_df['Close'].dropna().pct_change()
  btc_df
  ```

* Now that the data is prepared, it is now time to move onto generating the multiple trading signals! Students should draw from their experiences from the previous unit 15 lessons where they generated a dual moving average crossover trading signal, as the process is similar.

* In contrast to a simple moving average (SMA), an exponential moving average (EMA) represents a moving average with more weight or focus given to the most recent of prices. Therefore, a short window EMA describes "faster" price action than its long window EMA or "slower" counterpart. The logic then dictates such that when the fast EMA is greater than the slow EMA, a long trade opportunity exists, as price action should rise in the short-term, while a short trade opportunity arises for the opposite scenario in which the slow EMA is greater than the fast EMA.

  * Students should be aware that these trading signals will incorporate a long, short, or hold strategy (rather than just long or hold, or short or hold), which is why the `crossover_signal` is calculated as the result of adding both the `crossover_long` and `crossover_short` signals together.

    ```python
    btc_df['crossover_signal'] = btc_df['crossover_long'] + btc_df['crossover_short']
    ```

    ![ema](Images/ema.png)

    ![ema-plot](Images/ema-plot.png)

* Similarly, an exponential moving average of daily return volatility gives more weight to the most recent of daily returns. Therefore, when a short window EMA or fast EMA of daily return volatility is greater than a long window or slow EMA of daily return volatility, the crossover suggests that a short opportunity exists where daily return volatility is expected to rise. This is because during times of rising price volatility, there often exists a negative price bias (selling) and vice versa for when daily return volatility is expected to fall (buying).

  ![ema-std](Images/ema-std.png)

  ![ema-std-plot](Images/ema-std-plot.png)

* Lastly, a Bollinger Band describes a middle, upper, and lower band, in which the middle is a simple moving average (SMA) of closing prices, while the upper and lower bands describe the rolling standard deviation above and below the SMA, respectively. Therefore, when the asset closing price is less than the lower band, a long opportunity exists as the signal suggests that the price action will tend to move upwards and more in line with where the price *should* be (within the negative standard deviation). A short opportunity exists for the opposite scenario in which the asset closing price is greater than the upper band, suggesting that the price action will tend to move lower and within the positive standard deviation.

  ![bollinger-band.png](Images/bollinger-band.png)

  ![bollinger-band-plot.png](Images/bollinger-band-plot.png)

At the end of the discussion, ask students whether or not they understand what the trading signals are suggesting. This is important as these trading signals will end up training the Random Forest model, therefore it is crucial for them to understanding the basis upon which the model will be trained.

---

### 2. Instructor Do: Random Forest Trading (15 min)

In this activity, students will learn how to use the set of trading signal features they generated in the previous activity to now train a Random Forest machine learning model.

**File:** [random_forest_training.ipynb](Activities/02-Ins_Random_Forest_Training/Solved/random_forest_training.ipynb)

Before proceeding with the coding activity, open the slides and briefly re-cap the the use of machine learning models in regards to trading:

* How will we incorporate a machine learning model in terms of trading?

  **Answer:** Machine learning models need to be trained before they can make predictions. Therefore, using the trading signals generated from the previous activity, the Random Forest model will train itself using the trading signals as independent variables that determine a dependent variable (a positive or negative return for the next day). The model can then be saved as a pre-trained model for later use and loaded again for easy deployment.

* What is a Random Forest model?

  **Answer:** A Random Forest model is among one of the best supervised algorithms in terms of its ability to predict outcomes. The Random Forest model utilizes a combination of multiple decision tree models to "average away" or minimize the impact of any single decision tree with high variance, thereby creating a more reliable predicted result derived from the strongest features. For example, in regards to portfolio optimization, combining the concept of sharp ratios and portfolio diversification tends to create a portfolio of maximum expected return with minimal variance or risk due to the tendency for non-correlated stock to "cancel" out each other's variances.

* Why is it called a Random Forest?

  **Answer:** A Random Forest model is a combination of many decision tree models with each decision tree or "tree" randomly selecting a subset of the observations and features to train itself on. The result is a final prediction that is an average across this "forest" of random tress.

Then, open the solution file and discuss the following:

* The trading signal data from the previous activity has been saved for students' convenience. Therefore, the only pre-requisite needed before training the Random Forest model is to read the CSV, set the index to the `Timestamp` column, and drop the extraneous column.

  ```python
  # Set path to CSV and read in CSV
  csv_path = Path('../Resources/trading_signals.csv')
  trading_signals_df=pd.read_csv(csv_path)
  trading_signals_df.head()
  ```

  ```python
  trading_signals_df.set_index(pd.to_datetime(trading_signals_df['Timestamp'], infer_datetime_format=True), inplace=True)
  trading_signals_df.drop(columns=['Timestamp'], inplace=True)
  trading_signals_df
  ```

* Now that the data is prepared, the next step is to define the x-variable list, shift the index of the Pandas DataFrame by 1, and construct the dependent variable. The shift ensures that the model will use the current day values to predict the *next* day's outcome--whether the next day will be a positive or negative return.

  ![set-x-var-list-and-shift](Images/set-x-var-list-and-shift.png)

  ![dependent-variable](Images/dependent-variable.png)

* It is also important to check for any positive or negative infinity values, as such values will cause problems when subsequently training the model as suggested by the error below.

  ```python
  # Drop NAs and replace positive/negative infinity values
  trading_signals_df.dropna(subset=x_var_list, inplace=True)
  trading_signals_df.dropna(subset=['daily_return'], inplace=True)
  trading_signals_df = trading_signals_df.replace([np.inf, -np.inf], np.nan)
  trading_signals_df.head()
  ```

  ![infinity-error.png](Images/infinity-error.png)

* Almost there! The final remaining steps before proceeding to train the Random Forest model is to now define the training and test windows and separate the X and Y training/testing datasets.

  ![training-testing-windows.png](Images/training-testing-windows.png)

  ![x-y-training-datasets](Images/x-y-training-datasets.png)

  ![x-y-testing-datasets](Images/x-y-testing-datasets.png)

* And now for the last piece to the puzzle! After importing the `sklearn` library and associated Random Forest classes, the model is fit with the x and y training data and then used to predict the y values derived from the x test dataset. The results are then shown in the following DataFrame.

  ![random-forest-model](Images/random-forest-model.png)

* Finally, the `joblib` library allows a user to save a pre-trained model to a file for convenient future deployment. Doing so can be very valuable as fitting a model can be resource intensive when dealing with large amounts of data, therefore persisting a model saves both time and effort (re-running code).

  ```python
  from joblib import dump, load
  dump(model, 'random_forest_model.joblib')
  ```

---

### 3. Instructor Do: Random Forest Trading (15 min)

In this activity, students will re-deploy a pre-trained Random Forest model to make predictions (positive or negative daily return) given the x test dataset of BTC/USD closing prices. Then, students will compare the actual results vs. the predicted results and backtest the Random Forest model given a capital allocation of $100,000.

**File:** [random_forest_trading.ipynb](Activities/03-Ins_Random_Forest_Trading/Solved/random_forest_trading.ipynb)

Briefly discuss the following before proceeding to the coding solution:

* Now that the pre-trained Random Forest model has been saved, re-deploying the model to make predictions becomes very straightforward--all that needs to be done is to feed in the x test data (trading signal data) and compare against the y test data (actual daily return results).

* Deploying an already trained model saves time and effort, offloading the need for developers to have to prepare the data, split the data (train and test datasets), and fit the model before finally being able to use the model to make predictions.

Open the solution file and discuss the following:

* For convenience, the x test and y test (actual results) datasets have been provided as CSVs. The remaining pre-requisites before loading and making predictions from the pre-trained model are to once again set the indexes to the DataFrames as `Timestamp` (a datetime object) and drop the extraneous columns.

  ![x-test-csv](Images/x-test-csv.png)

  ![y-test-csv](Images/y-test-csv.png)

* One, two, three, predict! By using a pre-trained Random forest model that has already been saved, the process of deploying the pre-trained model and making predictions becomes a mere two lines of code. Aligning the actual results vs. the predicted results within a DataFrame then makes for a more aesthetically pleasing comparison.

  ![pre-trained-model-predict.png](Images/pre-trained-model-predict.png)

  ![actual-results-vs-predicted-results](Images/actual-results-vs-predicted-results.png)

* The comparative results can then be plotted to show the turnover of the Random Forest model. In other words, the following plot shows how many times the model predicted that a particular day would be positive or negative based off of the features or trading signals.

  ![random-forest-model-plot-1](Images/random-forest-model-plot-1.png)

* Viewing the totality of the actual vs. predicted results can be hard to decipher, therefore viewing a small portion such as the last 10 records provides better understanding of how the model performs.

  ![random-forest-model-plot-2](Images/random-forest-model-plot-2.png)

* Calculating the cumulative returns of the model by multiplying the daily returns (actual results) against the predicted values shows that the model would have unfortunately lost money from 09-15-2019 to 09-25-2019 trading on BTC/USD hourly prices. This is to be expected, however, as the process for training and using a trading model can be straightforward, but the ability to create a sophisticated trading model that outperforms markets is not--otherwise, there would be no more finance jobs as machines would run the markets!

  ![Images/model-cumulative-returns-plot.png](Images/model-cumulative-returns-plot.png)

* Finally, backtesting the performance of the trading model by multiplying its cumulative returns against an initial capital allocation of $100,000 merely serves to visualize its performance in terms of capital.

  ![model-cumulative-returns-plot-backtest](Images/model-cumulative-returns-plot-backtest.png)

---

### 4. Instructor Do: Recap (15 min)

In this activity, instructors will briefly re-cap the process of training and using a Random Forest trading model, discuss the ways in which the model can potentially be improved, and consider deploying the model through alternative means such as AWS' Sagemaker--a machine learning cloud service that enables users to build, train, and deploy machine learning models quickly and conveniently.

Open the slideshow and quickly re-cap the following. Engage students by having them answer the questions wherever possible:

* What did we learn today?

  **Answer:** We learned how to implement a machine learning model (Random Forest) to make predictions of next-day daily returns, given a set of trading signals derived from raw asset closing prices.

* What was the process for implementing a machine learning trading model?

  **Answer** The process for implementing a machine learning model, regardless of domain, generally includes the following: preparing the data, splitting the data into train and test datasets, fitting the x and y train data to the model, making predictions from the x test data, and comparing the predicted results to the y test data (actual results) to evaluate the performance of the overall model.

* What was the main takeaway from today's lesson?

  **Answer:** That the process for implementing a machine learning trading model can be fairly straightforward, but the ability to construct a sophisticated enough trading model that can outperform the markets will require more effort via further understanding of the markets and fine-tuning of the model (more features and therefore information).

Then, ask students if they have any further questions before moving onto the following talking points regarding model improvement:

* Admittedly, the Random Forest trading model still has room for improvement before it can be considered a robust system for automated machine learning based trading. This is because while the activities aim to simplify the process for implementation to provide beginner insight, the trade-off in complexity affects the overall performance of the model. In particular, several factors could have benefited the training and therefore overall performance of the Random Forest trading model, such as using more observations or data, more features or variables, and continuous rather than binary calculations for trading signals.

* The number of observations and features supplied to the model for training can be increased to provide more information, and therefore a better understanding for the model to make more accurate predictions. In this case, there were only 462 observations and 3 features upon which the model was trained.

  ![x-test-shape](Images/x-test-shape.png)

* In addition, for simplicity, the trading signals were output as binary calculations--either 0 or 1, do not engage in the trade or engage in the trade. However, if a scaled continuous value were used instead of a binary value, the *extent* upon which a trading signal is defined or how *far* the values differ from the crossover point, could be used therefore providing more information to train the model.

  ![continuous-vs-binary](Images/continuous-vs-binary.png)

* Lastly, a lot of effort and time is spent on collecting and preparing training data. Therefore, as an alternative solution, Amazon SageMaker, a machine learning cloud service that enables users to build, train, and deploy machine learning models quickly and conveniently, could be used to minimize the work effort spent on preparing data and instead focus on optimizing the accuracy or performance of the model. Amazon SageMaker also provides several methods for accessing its functionality such as via the AWS web GUI, specific API endpoints, or the SageMaker Python SDK.

  ![aws-sagemaker](Images/aws-sagemaker.png)

Finally, end the lesson with some encouragement for students:

* Today marks the end of everything we have learned so far in the course! At this point in time, students have learned to not only use Python and its various libraries, but also learn how to implement machine learning based strategies to derive predictive insight. Students should feel very proud, as they have reached a technical milestone that many have yet to accomplish, and that they are on their way to becoming data scientists!

* Looking toward the horizon, students will soon delve deep into the world of Blockchain technology, or the next generation digital economy. With their now refined data analytic skills matched with machine learning capabilities, students will become absolute rock stars in the FinTech space once they add Blockchain to their technical repertoire!

---

### 5. Student Do: Work on Project (120 mins)

Students will use the remaining class time to work on their projects.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
