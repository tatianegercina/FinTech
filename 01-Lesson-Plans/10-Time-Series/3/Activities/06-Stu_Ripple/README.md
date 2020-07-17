# Ripple Volatility

In this activity, you will create GARCH and linear regression models for the price of Ripple (XRP), a cryptocurrency. Then, you will validate the latter model with training and test sets.

## Instructions

1. Use Scikit-learn to create a linear regression model, with the closing price returns as the dependent variable, and one-day lagged returns as the independent variable.

2. Using the training ("in-sample") dataset, estimate a sklearn regression model with XRP returns as the dependent variable, and XRP lagged returns (lagged one day) as the independent variable. Plot the predicted values of the testing set.

3. Apply your fitted model to the test ("out-of-sample") dataset. Then, plot the predicted values of the testing set.

4. Compute the root mean square error (RMSE) of in-sample and out-of-sample results. How does the model perform out-of-sample (on data that it has never seen before)? Are the predictions as good as, better, or worse than those that were observed for the training dataset?

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
