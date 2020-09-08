# Students Do: Predicting Loan Default with Random Forests

In this activity, you are going to explore how random forest algorithms can be used to identify loans that are likely to default. You will use the `sba_loans_encoded.csv` file that you created before to train the model.

## Instructions

### Loading and Preprocessing Loans Encoded Data

1. Load the `sba_loans_encoded.csv` in a pandas DataFrame called `df_loans`.

2. Define the features set by copying the `df_loans` DataFrame and dropping the `Default` column.

3. Create the target vector by assigning the values of the `Default` column from the `df_loans` DataFrame.

4. Split the data into training and testing sets.

5. Use the `StandardScaler` to scale the features data, remember that only `X_train` and `X_testing` DataFrames should be scaled.

### Fitting the Random Forest Model

6. Once data is scaled, create a random forest instance and train it with the training data (`X_train_scaled` and `y_train`), define `n_estimators=500` and `random_state=78`.

### Making Predictions Using the Random Forest Model

7. Validate the trained model by predicting loan defaults using the testing data (`X_test_scaled`).

### Model Evaluation

8. Evaluate model's results by using `sklearn` to calculate the confusion matrix, the accuracy score, and the classification report.

### Feature Importance

9. In this section, you are asked to fetch the features' importance from the random forest model and display the top 10 most important features.

### Analysis Questions

10. Analyze the model's evaluation results and answer the following questions:

* **Question 1:** Would you trust in this model to deploy a loan default solution in a bank?

* **Question 2:** What are your insights about the top 10 most importance features?



© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.