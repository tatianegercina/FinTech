# Students Do: Predicting Fraudulent Credit Card Transactions

According to the American Bankers Association, [_"every dollar of fraud now costs banks and credit unions roughly $2.92"_](https://www.aba.com/member-tools/industry-solutions/insights/state-card-fraud-2018), that's a reason why predicting fraud using machine learning techniques becomes a [broad area of research](https://scholar.google.com.mx/scholar?q=fraud+detection+machine+learning&btnG=&oq=fraud+detection+) and a great [business opportunity for FinTech startups](https://www.eu-startups.com/2019/06/paris-based-fintech-bleckwen-raises-e8-8-million-for-its-fraud-detection-software-to-prevent-financial-crime/).

In this activity, you are going to explore how tree based algorithms can be used to identify fraudulent credit card transactions. You will start using a decision tree model, that will be trained with the `transactions_data_encoded.csv` file that you created before.

## Instructions

### Loading and Preprocessing Loans Encoded Data

1. Load the `transactions_data_encoded.csv` in a pandas DataFrame called `df_transactions`.

2. Define the features set, by copying the `df_transactions` DataFrame and dropping the `isFraud` column.

3. Create the target vector by assigning the values of the `isFraud` column from the `df_transactions` DataFrame.

4. Split the data into training and testing sets.

5. Use the `StandardScaler` to scale the features data, remember that only `X_train` and `X_testing` DataFrames should be scaled.

### Fitting the Decision Tree Model

6. Once data is scaled, create a decision tree instance and train it with the training data (`X_train_scaled` and `y_train`).

### Making Predictions Using the Tree Model

7. Validate the trained model, by predicting fraudulent transactions using the testing data (`X_test_scaled`).

### Model Evaluation

8. Evaluate model's results, by using `sklearn` to calculate the confusion matrix, the accuracy score and generate the classification report.

### Visualizing the Decision Tree

9. Create a visual representation of the decision tree using `pydotplus`. Show the graph on the notebook, and also save it in `PDF` and `PNG` formats.

### Analysis Question

10. Finally, analyze the model's evaluation results and answer the following question.

    * Would you trust in this model to deploy a fraud detection solution in a bank?
