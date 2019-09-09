### 2. Instructor Do: Logistic Regression (10 mins)

**Files:**

[logistic_regression.pptx](Activities/01-Ins_Logistic_Regression/logistic_regression.pptx)

[Ins_Logistic_Regression.ipynb](Activities/01-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb)

Walk through the slideshow and highlight the following points:

* Logistic Regression is a statistical method for predicting binary outcomes from data. With linear regression, our linear model may provide a numerical output such as age. With logistic regression, the numerical value for age could be translated to a probability between 0 and 1. This discrete output could then be labeled as "young" vs "old".

* Logistic regression is calculated by applying an activation function as the final step to our linear model. This transforms a numerical range to a bounded probability between 0 and 1.

  ![logistic-regression-activation-function.png](Images/logistic-regression-activation-function.png)

* We can use logistic regression to predict which category or class a new data point should have.

  ![logistic_1.png](Images/logistic_1.png)
  ![logistic_2.png](Images/logistic_2.png)
  ![logistic_3.png](Images/logistic_3.png)
  ![logistic_4.png](Images/logistic_4.png)

After presenting the slideshow, open the Jupyter notebook and walk through the Scikit-Learn implementation for logistic regression.

* The `make_blobs` function is used to generate two different groups (classes) of data. We can then apply logistic regression to determine if new data points belong to the purple group or the yellow group.

  ![make-blobs.png](Images/make-blobs.png)

* We create our model using the `LogisticRegression` class from Sklearn.

  ![logistic-regression-model.png](Images/logistic-regression-model.png)

* Then we fit (train) the model using our training data.

  ![train-logistic-model.png](Images/train-logistic-model.png)

* And validate it using the test data.

  ![test-logistic-model.png](Images/test-logistic-model.png)

* And finally, we can make predictions.

  ![new-data.png](Images/new-data.png)

  ![predicted-class.png](Images/predicted-class.png)
