### 4. Students Do: Review Logistic Regression (15 min)

In this activity, students will create a logistic regression model to predict the likelihood of a loan approval or denial.

* Students should be familiar with the logistic regression model and this dataset in particular, as they worked with both back in unit 11. However, we will add two new elements: first, they will need to output not just the predictions for the classes but the probabilities of the predictions; second, they will need to find the mean squared error (MSE) of the probabilities compared to the actual results. 

* Students should be encouraged to look up unfamiliar functions in the sklearn documentation. 

**Instructions:**

* [README.md](Activities/01-Stu_Logistic_Reg/README.md)

**Files:**

* [logistic_regression.ipynb](Activities/01-Stu_Logistic_Reg/Unsolved/logistic_regression.ipynb)

---


### 5. Instructor Review: Logistic Regression (15 min)

**Files:**

* [logistic_regression.ipynb](Activities/01-Stu_Logistic_Reg/Solved/logistic_regression.ipynb)

Open the solved file and go over any questions students may have about the code. 

* Up until we output probabilities for each prediction, the code is essentially identical to the activity in Unit 11 that asked students to predict loan status using logistic regression.

* For the purposes of classification, we defined accuracy and other metrics according to how well the predicted classes matched up to the actual test outcomes. This makes sense because the model is only asked to come up with an end result - the prediction. However, remind students that neural networks have intermediate layer(s) of predictions. Thus, the neurons that we compare to logistic regression models are not only outputting the final results but some intermediate output that is used by other neurons to get to the final prediction. This is why we need a different metric to measure the quality of the output. 

* Remind students that logistic regressions don't actually output binary classes - they generate probabilities for each class that are converted to a class based on which class is more likely. We can retrieve the underlying probabilities in sklearn with this code:

```python
lreg.predict_proba(X_test)
```

* The output of this function is a two-column array; the first column corresponds to the probability approve (1) class and the second corresponds to the deny (0) class. Students can check the probabilities against the binary prediction classes to verify this: notice that probabilities greater than 0.5 or 50% in the first column correspond with the "approve" class. 

* Next we want to calculate a mean squared error metric, which is a cost function (more on this later) that is used in neural networks to give feedback to neurons in order for the neural net to learn. For now, students should understand that the metric, like all cost functions, represents the difference between the model output and the true outcomes. Unlike a accuracy score, however, the MSE allows small changes in the model's parameters as it learns because it uses probabilites and not predicted classes.

* In order to calculate the MSE, we need to use the mean_square_error function. First, however, we must map the actual test outcomes to numerial values that correspond to 1 for approve and 0 for deny, then isolate the probability of approve (1) from the probability output. We can accomplish both in one line of code. 

```python
mean_squared_error(y_test.map({'approve':1, 'deny':0}), probs[:,0])
```

* The value of this MSE output is not very meaningful on its own. Students can imagine, however, that when a neural network learns, it compares the value of the MSE after changing model parameters in order to determine whether the model is getting better or worse. 

While the code is pretty simple, the concepts that this activity is attempting to illustrate are complex. Take time to answer student questions and go back to the slides if necessary before moving on to the next activity. 