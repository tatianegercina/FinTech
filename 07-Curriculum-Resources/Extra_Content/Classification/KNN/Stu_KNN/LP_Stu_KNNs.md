### 19. Student Do: KNN Loan Approver (15 mins)

For this bridge activity, students revisit the loan approver application they made using the SVM classification algorithm. Instead of using SVM, students leverage the KNN algorithm.

**Instructions:** [README.md](Activities/09-Stu_KNN_Loan_Approver/README.md)

**Files:** [knn_loan_approver.ipynb](Activities/09-Stu_KNN_Loan_Approver/Unsolved/knn_loan_approver.ipynb)

### 20. Instructor Do: KNN Loan Approver Activity Review (10 mins)

The students participate in a facilitated review discussion of the KNN loan approver.

**Files:** [knn_loan_approver.ipynb](Activities/09-Stu_KNN_Loan_Approver/Solved/knn_loan_approver.ipynb)

Conduct a facilitated discussion to review the KNN loan approver content. Begin the discussion with a few review questions. Ask students:

* We've touched base on two different types of classification algorithms: linear and non-linear. When would one want to use a non-linear classification algorithm?

  * **Answer** Non-linear classification algorithms are used when features and outcomes are random and/or independent of one another. With linear classification, outcomes are directly related to inputs, and any changes will result in a proportionate change.

* If there can be no relationship between input and outcome, how is KNN able to predict outcomes and categorical classes?

  * **Answer** The KNN algorithm leverages the idea of **similarity**: data points close in proximity are more likely to be of the same type. The KNN algorithm evaluates the outcome/classes of data points closest to the data point in consideration. The new data point will inherit the label/class of the points closest to it.

* The `KNeighborsClassifier` object has one main parameter: `n_neighbors`. What's the process to figure out the optimal value for `n_neighbors`?

  * **Answer** The optimal value for `K` can be determined by looping through a range of potential values and implementing the model with each one. Then, the model should be scored for accuracy. The `K` value with the highest **test** and **train** accuracy is the optimal value.

  ![knn_n_neighbors.png](Images/knn_n_neighbors.png)

Open up the solution, and highlight the folowing discussion point before ending the activity:

* When it comes to the test data, the KNN algorithm was able to correctly classify all of the denies that were actually denied.  However, the model was only able to correctly classify 58% of the denies.

  ![knn_performance.png](Images/knn_performance.png)

* Emphasize that the model is more precise when approving than denying.

* The model has better recall when finding data points that belong to class **deny** than **approve**.

* Let students know that the accuracy, precision, and recall metrics will be used to compare model performance (Logistic Regression, SVM, and KNN) in order to determine the model for loan eligibility (with respects to the data being used).

Ask for any remaining questions before moving on.
