### 11. Students Do: Predicting Fraud with Random Forests (10 min)

In this activity, students will use a radom forest to create a model to prevent credit card fraudulent transactions.

**Instructions:**

* [README.md](activity/issue-1381/11-Stu-Random-Forest)

**Files:**

* [fraud-random-forest.ipynb](Activities/06_Stu-Random-Forest/Unsolved/fraud-random-forest.ipynb)

* [transactions_data_encoded.csv](Activities/06_Stu-Random-Forest/Resources/transactions_data_encoded.csv)

---

### 12. Instructor Do: Review Predicting Fraud with Random Forests (10 min)

**Files:**

* [fraud-random-forest.ipynb](Activities/06_Stu-Random-Forest/Solved/fraud-random-forest.ipynb)

* [transactions_data_encoded.csv](Activities/06_Stu-Random-Forest/Resources/transactions_data_encoded.csv)

Walk through the solution and highlight the following:

* The data used in this activity, is the same that students used with in the decision tree exercise, so data preprocessing is the same, except in the target set creation where the `ravel` method is used instead of `reshape`.

  ```python
  y = df_transactions["isFraud"].ravel()
  ```

* The random forest model instance is created defining `n_estimators = 100` and `random_state = 78`.

Recall students that defining the `random_state` parameter, is important to compare different models.

* The random forest model is trained with the training data. **Note:** This step will take few minutes due to the size of the DataFrame.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* Once the model is fitted, it's validated using the testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* The model is evaluated using the confusion matrix, the `accuracy_score` and the `classification_report` from `sklearn`.

  ![Random forest evaluation results](Images/stu-random-forest-1.png)

Comment to students, that it can be observed that model´s accuracy is quite good (`0.99`) and it's capable of predicting the 100% of non-fraudulent transactions, however after analyzing the confusion matrix, it can be seen that the model is not predicting the fraudulent transactions `isFraud = 1`, so precision, recall and F1 score were set to zero for this class.

Explain to students, that this is not an issue with the algorithm, it's an issue with the data since classes are unbalanced, and maybe, we should train the model with different features. Remind

* The features importance is retrieved from the random forest model using the `feature_importances_` attribute, finally the top 10 most important features are displayed.

  ![Top 10 important features](Images/stu-random-forest-2.png)

Finally, ask a couple of students about their insights in the _Analysis Questions_ sections, you can comment the following about each question.

* **Question 1:** Would you trust in this model to deploy a fraud detection solution in a bank?

  * **Sample Answer:** Model's accuracy seems to be good (`0.99`), after analyzing the confusion matrix, it can bee observed that the model is only predicting the fraudulent non-fraudulent transactions, so we can re-train the model using a different combination of features.

* **Question 2:** What are your insights about the top 10 most importance features?

  * **Sample Answer:** It seems that the merchant is not relevant for the model, so we can create a new random forest model by only taking these top 10 features. Also, for piloting this model in a business environment, we will only need to fetch new data about these 10 features.

Answer any questions before moving on.
