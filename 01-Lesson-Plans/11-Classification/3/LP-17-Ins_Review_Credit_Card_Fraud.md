## 17. Instructor Review: Credit Card Fraud

**Files:**

[cc_fraud.ipynb](Activities/09-Stu_Do_Credit_Card_Fraud/Solved/cc_fraud.ipynb)

For this review, go around the class and ask students which methods they tried, both in terms of sampling strategies as well as different algorithms. Which ones worked the best?Which didn't work so well? Which results were surprising?

After surveying the class, open the solved notebook and walk through our solution. Stress that this is only one (most likely non-optimal) way of solving the problem.

* We found the SMOTEENN ssampling method to generate the best classification metrics when restricting the model to logistic regression. Note, however, that oversampling also produced high precision and recall scores for both classes, indicating that fraudulent and non-fraudulent transactions are relatvily easily separable using these features.

* We chose a balanced random forest implementation for the ensemble model. The performance seems comparable to the logistic regression after resampling. 

* The PR curve looks very similar, with the logistic regression results seemingly a little better at thresholds that produce higher recall - i.e., lower thresholds for predicting a the fraud class. 

Ask students if there are any questions about this activity before starting to finish up class.