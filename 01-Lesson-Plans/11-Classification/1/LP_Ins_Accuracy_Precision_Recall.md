### 8. Instructor Do: Accuracy, Precision, Recall (10 min)

The instructor provides a formal lecture explaining to students what accuracy, precision, and recall is in relation to logistic regression models, as well as how to measure each metric.

**Files**

* [Slides]()

Navigate to the 11.1 slides, and highlight the following:

* Explain to students that **accuracy**, **precision**, and **recall** are especially important for **classification** models, which a **binary decision problem**. **Binary decision problems** have two possible correct answers: **True Positive** and **True Negative**.

  * Inaccurate and imprecise models result in models returning false positives and false negatives.

* When running a classification model, or any statistical model, it is important that the model is evaluated for **accuracy**, **precision**, and **recall**.

* Accuracy is how often the model is correct: the ratio of correctly predicted observations to the total number of observations. As demonstrated previously, the **accuracy** of a model can be evaluated by scoring the model using training and testing data sets. Scoring will reveal how accurate the model. However, it does not communicate how precise it is.

  * Accuracy can be very susceptible to imbalanced classes. In the case of the homework assignment, the number of good loans greatly outweighs the number of at-risk loans. In this case, it can be really easy for the model to only care about the good loans because that has the biggest impact on accuracy. However, we also care about the at-risk loans, so we need a metric that can help us evaluate each class prediction.

  * **Calculation:** (TP + TN) / (TP + TN + FP + FN)

* **Precision** is the ratio of correctly predicted positive observations to the total predicted positive observations (i.e. of all the samples classified as having diabetes or a credit risk, how many actually have diabetes/are a credit risk).

  * Another example of **precision** is of all of the individuals that were classified by the model as being a credit risk, how many actually were a credit risk? The question at hand: did we classify comprehensively and correctly?

  * A similar example would be of all the loans predicted to be in good standing, how many actually are? Of the loans predicted to be at-risk, are they actually at-risk?

  * High precision relates to a low **false positive** rate.

  * **Calculation:** TP / (TP + FP)

* **Recall** is the ratio of correctly predicted positive observations to all predicted observations for that class (i.e. of all of the actual diabetes/credit risk samples, how many were correctly classified as having diabetes/being a credit risk). The question at hand: did we classify all samples correctly, leaving little room for **false negatives**.

  * A better way to understand **recall** is of all of the individuals that are a credit risk, how many were classified by the model as being a credit risk?

  * High recall relates to a more comprehensive output and a low **false negative** rate.

  * **Calculation:** TP / (TP + FN)

Encourage students to consult the following [documentation](https://blog.exsilio.com/all/accuracy-precision-recall-f1-score-interpretation-of-performance-measures/) if they need additional explanation of precision and recall and how they are calculated.

Use the remaining time to answer any questions about logistic regression models and evaluating predictions. Then, move forward with the next activity.
