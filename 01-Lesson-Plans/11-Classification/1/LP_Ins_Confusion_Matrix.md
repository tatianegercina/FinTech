### 9. Instructor Do: Confusion Matrix & Classification Report (10)

Students receive a live demonstration of how to create and use a confusion matrix and classification report to evaluate models for error.

**Files**

* [Slides]()

* [confusion_matrix.ipynb](Activities/03-Ins_Confusion_Matrices/Solved/confusion_matrix.ipynb)

Open the starter-file, and highlight the below discussion points while live coding how to use a **confusion matrix**.

* A **confusion matrix** is used to measure and gauge the success of a model. Confusion matrices reveal the number of true negatives and true positives (actuals) for each categorical class and compares it to the number of predicted values for each class. These values are then individually summed by column and row. The aggregate sums are then compared to gauge accuracy and precision. If the aggregates match, the model can be considered accurate and precise.

  ![confusion_matrix_table.png](Images/confusion_matrix_table.png)

* Confusion matrices are great because they describe the performance of the classification model. By looking at the confusion matrix, one can determine whether or not the model has been correctly trained to produce comprehensive accurate and precise predictions.

* For binary classifiers like the **logistic regression** classifier, a **confusion matrix** would measure the number of positive and negative predictions. These will then be compared in relation to the actuals.

* So now the question is, how does one get data loaded into a confusion matrix for model evaluation? Most models will come equipped with a confusion matrix module, like the **sklearn** `metrics.confusion_matrix` module. The **sklearn** `confusion_matrix` function accepts two arguments, one data set containing the predicted values and another containing the actual data points.

Transition to the live coding aspect of the demo, and demonstrate how to use and interpret the **sklearn** `confusion_matrix` function.

* The `confusion_matrix` function can be imported into the Python environment from the `metrics` package. Once imported, it can be executed using the actual and predicted data points. The output is a two dimensional array. Columns reflect binary classes (high credit risk or low credit risk), and the rows represent the number of samples/data points that actually belong to that class.

    ```python
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)
    ```

    ![confusion_matrix.png](Images/confusion_matrix.png)

Communicate to students that a **classification report** can also be used to evaluate a model. When evaluating a model, the **accuracy**, **precision**, and **recall** must all be evaluated to ensure the rate of false positive sand false negatives are minimal. The results from these tests can be stored within a **classification report**, which can be used to assess and evaluate number of predicted occurrences for each class.

* Classification reports calculate the precision, recall, and f1 score (accuracy in relation to precision and recall). Classification reports can be generated using the **sklearn** `metrics.classification_report` module. All that is required to execute the `classification_report` function is the actual data points and predicted data points.

  * The **classification report** will automatically calculate precision, recall, and accuracy.

    ```python
    from sklearn.metrics import classification_report
    target_names = ["Class Purple", "Class Yellow"]
    print(classification_report(y_test, predictions, target_names=target_names))
    ```

    ![classification_report.png](Images/classification_report.png)

Finish the activity by asking students if there are any questions, and then transition to the student activity.
