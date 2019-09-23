### 10. Instructor Do: Random Forest (10 min)

In this activity, students will learn how to implement a random forest using `sklearn`.

**Files:**

* [random-forest.ipynb](Activities/05-Ins_Random_Forest/Solved/random-forest.ipynb)

* [loans_data_encoded.csv](Activities/05-Ins_Random_Forest/Resources/loans_data_encoded.csv)

Explain to students that in this demo, you are going to use the loan applications encoded dataset presented before. The goal of this demo, is to predict fraudulent loan applications using a random forest.

Use the unsolved Jupyter notebook to live code the solution and highlight the following:

* In order to use the random forest implementation from `sklearn`, the `RandomForestClassifier` class from the `ensemble` module should be imported.

  ```python
  from sklearn.ensemble import RandomForestClassifier
  ```

As it has been done before, the data is loaded in to a Pandas DataFrame and then scaled and split into training and testing set. Just briefly review this code and continue to live code the random forest implementation by highlighting the following:

* To create the target vector `y` before scaling the data, the `ravel` method is used instead of `reshape` as we did in the decision tree demo.

  ```python
  y = df_loans["bad"].ravel()
  ```

* When the random forest instance is created, there are two important parameters to set:

  ```python
  rf_model = RandomForestClassifier(n_estimators=500, random_state=78)
  ```

  * `n_estimators`: This is the number of random forest to be created by the algorithm, in general, a higher number makes the predictions stronger and more stable, however a very large number can result in higher training time.

  * `random_state`: This parameter defines the seed used by the random number generator, it's important to define a value for future model comparison.

Comment to students, that that according to a [research study](https://doi.org/10.1007/978-3-642-31537-4_13), it's possible to suggest that a range between `64` and `128` trees in a forest could be used for initial modeling.

* Once the random forest model is created, it's fitted with the training data.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, some predictions are made using the scaled testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* In oder to evaluate the model, a confusion matrix, the `accuracy_score` and the `classification_report` from `sklearn.metrics` are used.

* The confusion matrix is created using the `y_test` and the `results` vectors. The matrix shows how well the model predict fraudulent loan applications.

  ```python
  # Calculating the confusion matrix
  cm = confusion_matrix(y_test, predictions)
  cm_df = pd.DataFrame(
      cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
  )

  # Calculating the accuracy score
  acc_score = accuracy_score(y_test, predictions)
  ```

  ![Random forest evaluation results](Images/random-forest-1.png)

After observing the results, it can be concluded that this model may not be the best one for preventing fraudulent loan applications, comment to students that there are several strategies to improve this model such as:

* Reduce the number of features using PCA.

* Create new features based on new data from the problem domain.

* Increase the number of estimators.

Finally, explain to students that as it was commented in the random forest intro, a byproduct of the Random Forest algorithm is a ranking of feature importance (i.e. which features have the most impact on the decision).

* The `RandomForestClassifier` of `sklearn` provides an attribute called `feature_importances_`, where you can see which features were the most significant.

  ![Feature importance](Images/random-forest-2.png)

* In this demo, it can be seen that the `age` of the person and the `month` of the loan application are the more relevant features.

* If we need to drop some features, analyzing feature importance could help to decide which features can be removed.

Answer any questions before moving on.
