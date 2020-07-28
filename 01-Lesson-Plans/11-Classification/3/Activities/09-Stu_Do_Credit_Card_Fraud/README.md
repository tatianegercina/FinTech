# Credit Card Fraud

In this activity, you will practice resampling techniques and use different models to classify credit card transactions as fraudulent or not fraudulent. 

## Instructions

* Implement one undersampling, one oversampling, and one combination sampling technique, using the algorithm of your choice. 

* Compare results of the sampling techniques using a logistic regression classifier, and choose the "best" resampling technique. 

* Compare the logistic regression using resampled data to the results of an ensemble method of your choice. 

## Hints:

* You may need to increase the number of maximum training iterations in the logistic regression model. This can be set using the `max_iter` parameter.

```
model = LogisticRegression(solver='lbfgs', random_state=1, max_iter=2000)
```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
