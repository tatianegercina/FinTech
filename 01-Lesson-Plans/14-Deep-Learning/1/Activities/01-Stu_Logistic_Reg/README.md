## Review Logistic Regression

In this activity, you will create a logistic regression model to predict the likelihood of a loan approval or denial.

### Instructions

1. Use the sklearn logistic regression implementation to predict the loan status of a test sample of the loans data. 
2. Output the probability that each loan will be appproved. 
3. Calculate the mean squared error for the **probabilities** the model outputs compared to the actual values (assuming approve is 1 and deny is 0).

### Hints

* The LogisticRegression module has a predict_proba function that outputs probabilities of predicted classes.
* The metrics module in scikit learn can help you calculate the mean squared error statistic. 
