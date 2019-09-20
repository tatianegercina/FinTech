## KNN Loan Approver

In this activity, you will build a K-Nearest Neighbors classifier that can be used to predict the loan status (approve or deny) given a set of input features.

### Instructions

1. Read the data into a Pandas DataFrame
2. Separate the Features (X) from the Target (y). In this case, the loan status is the target.
3. Separate the data into training and testing data.
4. Create a classifier using sklearn.
5. Loop through different k values and plot the results to find the optimal k value.
6. Train the model using the optimal k value.
7. Calculate the accuracy score using both the training and the testing data.
8. Make predictions using the testing data.
9. Generate the confusion matrix for the test data predictions.
10. Generate the classification report for the test data.