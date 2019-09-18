### 16. Students Do: SVM Loan Approver (15 mins)

Students are asked to update their loan approver with an SVM model and rerun the evaluation metrics. Students will then compare the performance of the SVM model with the Logistic Regression model.

**Instructions:** [README.md](Activities/07_Stu_SVM_Loan_Approver/README.md)

**Files:** [svm_loan_approver.ipynb](Activities/07_Stu_SVM_Loan_Approver/Unsolved/svm_loan_approver.ipynb)

### 17. Instructor Do: SVM Loan Approver Activity Review (10 mins)

The instructor leads a dry walk through of the previous activity.

**Files:**

* [ssvm_loan_approver.ipynb](Activities/07-Stu_SVM_Loan_Approver/Solved/svm_loan_approver.ipynb)

Open the solution and explain the following:

* The SVM algorithm is an alternative to the Logistic Regression model when it comes to running classification engines. The SVM algorithm is often times more more accurate than other models.

* The SVM package is a part of the `sklearn.svm` module. The `svc` constructor is used to create and configure the model.

* SVM models can be either 2D (linear) or multi-dimensional (poly). The dimension of the model is defined by the `kernel` argument.

    ```python
    # Instantiate a linear SVM model
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear')
    classifier
    ```

    ```
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
    kernel='linear', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)
    ```

* Once the model is created, it has to be fit with data.

    ```python
    # Fit the data
    classifier.fit(X_train, y_train)
    ```

* The model can then be scored for accuracy.

    ```python
    # Score the accuracy
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")
    ```

* An accurate model can make precise predictions. The **sklearn** `predict` function is used make predictions off of the new data.

    ```python
    # Make predictions using the test data
    predictions = classifier.predict(X_test)
    results = pd.DataFrame({"Prediction": predictions, "Actual": y_test}).reset_index(drop=True)
    results.head()
    ```

    ![prediction_results.png](Images/prediction_results.png)

* The last step is to evaluate the model. Just like with the Logistic Regression model, the `confusion_matrix` and `classification_report` libraries can be used to assess metrics and performance.

    ```python
    # Evaluate performance
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)

    from sklearn.metrics import classification_report
    print(classification_report(y_test, predictions))
    ```

  ![evaluate_svm.png](Images/evaluate_svm.png)

* Ask students which model performed better in terms of accuracy, precision, and recall.

  * **Answer** The SVM model performed better in terms of accuracy, precision, and recall.

If time remains, ask students the following guided/review questions.

* Ask students to define what support vector machines are.

  * **Answer** Data points that exist closest to the hyperplane. These points are used to help identify the position and orientation of the hyperplane, and they care called **support vectors**.

* A parameter named `kernel` is used when creating an SVM model. What does this parameter do?

  * **Answer** Identifies the orientation of the **hyperplane**, as either linear or multi-dimensional.

* What's the difference between the `decision_function` function and the `predict` function?

  * **Answer** The `decision_function` function has the classifier calculate the classification score for each data point. These values are used to classify the data points to either class. The output from `decision_function` should not be confused with the output from `predict`. `Predict` provides a classification/label. `Decision_function` returns a scalar value.

* What is `decision_function` used for?

  * **Answer** The `decision_function` function is used to identify the bounds of the **hyperplane**.

* If data points are overlapping, can their classification be trusted?

  * **Answer** No. Data points that are overlapping have a 50% chance of being classified incorrectly. The goal is to maximize the margin.

Ask if there are any questions before moving forward.
