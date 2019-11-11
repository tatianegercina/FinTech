### 3. Instructor Do: Random Forest Trading (15 min)

In this activity, students will re-deploy a pre-trained Random Forest model to make predictions (positive or negative daily return) given the x test dataset of BTC/USD closing prices. Then, students will compare the actual results vs. the predicted results and backtest the Random Forest model given a capital allocation of $100,000.

**File:** [random_forest_trading.ipynb](Activities/01-Ins_Random_Forest_Trading/Solved/random_forest_trading.ipynb)

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

* And now for the last piece to the puzzle! After importing the `sklearn` library and associated Random Forest classes, the model is fit with the x and y training data and then used to predict the y values derived from the x test dataset. The results are then shown in the following DataFrame.

  ![random-forest-model](Images/random-forest-model.png)

* The results are then plotted against the actual results (where or not the particular day was a positive or negative return) to show the turnover of the Random Forest model. In other words, the following plot shows how many times the model predicted that a particular day would be positive or negative based off of the features or trading signals.

  ![random-forest-model-plot-1](Images/random-forest-model-plot-1.png)

  ![random-forest-model-plot-2](Images/random-forest-model-plot-2.png)

* And finally, the cumulative return plot related to the strategy employed by the predictive Random Forest model is shown. Unfortunately, the strategy would have lost money from 09-15-2019 to 09-25-2019.

  ![Images/model-cumulative-returns-plot.png](Images/model-cumulative-returns-plot.png)
