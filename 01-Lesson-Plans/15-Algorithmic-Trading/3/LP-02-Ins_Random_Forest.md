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
