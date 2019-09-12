### 12. Student Do: Build Loan Approver (15 mins)

Students will participate in a bag of tricks activity where they apply the machine learning concepts and technical skills learned thus far to create a model for approving loans.

**Instructions:** [README.md](Activities/05-Stu_Loan_Approver/README.md)

**Files:** [starter-code.js](Activities/05-Stu_Loan_Approver/Unsolved/loan_approver.ipynb)

### 13. Instructor Do: Build Loan Approver Activity Review (10 mins)

The instructor leads a facilitated review discussion on the loan approver. The review will be a dry walk through with accompanying guided/review questions.

**Files:** [loan_approver.ipynb](Activities/05-Stu_Loan_Approver/Solved/loan_approver.ipynb)

In order to ensure pacing of the activity, do not ask all of the below questions. Use these questions as prompts to engage students and increase discussion.

Begin the review session with a few guided questions:

* Using the confusion matrix and classification report to evaluate the model, would you trust the predictions made by this model to decide when and when you should not loan out money? Should a bank trust it?

  * **Answer** The model in its current state is not optimized for accuracy. It should not be trusted to make predictions.

* What can we do to improve the accuracy of the model?

  * **Answer** Train the model with more data.

Open the solution and transition to a dry walk through of the activity. Remind students of the following:

* In order to build a supervised model and make predictions, data has to be provided that can be used to predict outcomes. This data set must contain **features** and a **target**.

  * Features are the fields that relate to credit worthiness (i.e. **assets**, **liabilities**, **income**, and **credit score**).

  * The target is the predicted outcome (i.e. approve or deny status.)

* Since features can vary in scale and range, features have been normalized (i.e. a candidate's income can be a value 100,000; however, their credit score's max value can only be 900). This ensures differences in scale do not sway predictions. Values have been normalized between 0 and 1.

* **Sklearn's** `LogisticRegression` module that can be used to create a logistic regression model. This model is needed in order to classify categorical outcomes.

  * The `LogisticRegression` module comes with functions to support preprocessing and model execution, such as `train_test_split`, `fit`, and `predict`.

* Fitting a model requires train and test data. The **sklearn** `train_test_split` function can be used to split a single data into these subsets. The model will then use the train and test data to make predictions and evaluate performance.

* Training/fitting a model with **sklearn** is as simple as running a single function: `fit`. The `fit` function has two main parameters: the features training data and the target training data.

* Using the model to make predictions is just as easy. The **sklearn** `predict` function accepts a single argument: the features to use to predict.

Continue the next part of the review by asking students questions and then explaining how the answer is implemented in the code:

* When measuring the performance and reliability of a model, machine learning engineers need to consider the precision of the model. What is precision?

  * **Answer** Precision is the ratio of correctly predicted positive outcomes out of all predicted positive outcomes.

* Recall is another performance metric that can be considered. What does recall measure? What does recall reveal about the model's predictions?

  * **Answer** Recall measures the number of correct positive predictions out of all predictions. The recall reveals that our model predicts more correct denies than approves.

* Based off of the precision and recall returned from the classification report, how has this model performed?

  * **Answer** The model would benefit from additional fitting/training. The model currently denies users more than approves, even when it should approve.

* What is the difference between the confusion matrix and the classification report?

  * **Answer** The confusion matrix identifies the number of categorical outcome predictions made by the model and juxtaposes it against the actual results. Confusion matrices are perfect for evaluating false positives and false negatives. The classification report uses accuracy, precision, and recall to measure the performance and success of the model.The focus is on the ratio of correctly and incorrectly predicted values against all predictions.

Ask for any remaining questions before moving on.
