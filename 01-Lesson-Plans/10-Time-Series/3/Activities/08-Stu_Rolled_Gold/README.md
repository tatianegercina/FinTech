# Rolled Gold

In this activity, you will compare a linear regression model with a train/test split to a model trained using rolling out-of-sample data.

## Instructions

The dataset lists the price of gold in the years 2001–2019. Use the closing price in U.S. dollars ("USD (PM)") to generate your train and test datasets.

### Train Test Spit Model

Use the data from 2001 through 2018 to predict the prices for 2019.

Calcualte the out-of-sample root mean square error (RMSE) for 2019.

### Rolling Out-of-Sample Model

Use Scikit-learn to make out-of-sample predictions of gold price on a rolling weekly basis. During each iteration, split a 13-week window into a training period of 12 weeks and a testing period of 1 week.

For example, for an iteration that begins on January 4, 2001, the next 12 weeks should comprise the training period. The week after the training period will be the testing period.

The lagged return values (X) should be regressed against the return values (Y).

Compile a DataFrame of actual returns and out-of-sample predicted returns.

Using the 2019 data from the Results DataFrame, compute the out-of-sample RMSE.

How does the RMSE for the two models compare?

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
