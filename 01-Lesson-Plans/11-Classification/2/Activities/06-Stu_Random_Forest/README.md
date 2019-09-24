# Students Do: Predicting Fraud with Random Forests

In this activity, you are going to explore how random forest algorithm can be used to identify fraudulent credit card transactions. You will use the `transactions_data_encoded.csv` file that you created before to train the model

## Instructions

### Loading and Preprocessing Loans Encoded Data

1. Load the `transactions_data_encoded.csv` in a pandas DataFrame called `df_transactions`.

2. Define the features set by copying the `df_transactions` DataFrame and dropping the `isFraud` column.

3. Create the target vector by assigning the values of the `isFraud` column from the `df_transactions` DataFrame.

4. Split the data into training and testing sets.

5. Use the `StandardScaler` to scale the features data, remember that only `X_train` and `X_testing` DataFrames should be scaled.

### Fitting the Random Forest Model

6. Once data is scaled, create a random forest instance and train it with the training data (`X_train_scaled` and `y_train`), define `n_estimators=200` and `random_state=78`.

### Making Predictions Using the Random Forest Model

7. Validate the trained model by predicting fraudulent transactions using the testing data (`X_test_scaled`).

### Model Evaluation

8. Evaluate model's results by using `sklearn` to calculate the confusion matrix, the accuracy score, and the classification report.

### Feature Importance

9. In this section, you are asked to fetch the features' importance from the random forest model and display the top 10 most important features.

### Analysis Questions

10. Analyze the model's evaluation results and answer the following questions.

* **Question 1:** Would you trust in this model to deploy a fraud detection solution in a bank?

* **Question 2:** What are your insights about the top 10 most importance features?
