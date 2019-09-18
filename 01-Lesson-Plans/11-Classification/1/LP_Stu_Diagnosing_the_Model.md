### 10. Students Do: Diagnosing the Model (10 min)

Students complete a bridge activity where they return to the model they created to predict diabetes and will use a **confusion matrix** and **classification report** to evaluate and diagnose the model. Emphasis needs to be placed on how to interpret confusion matrices and classification reports in order to diagnose issues in the model.

**Files**

* [README.md](Activities/04-Stu_Diagnosing_the_Model/README.md)

* [diagnosis.ipynb](Activities/04-Stu_Diagnosing_the_Model/Unsolved/diagnosis.ipynb)

### 11. Instructor Do: Diagnosing the Model Activity Review (10 min)

Students receive a dry walk through of the solution and are given the opportunity ask questions about creating and interpreting **confusion matrices** and **classification reports**.

**Files:** [diagnosis.ipynb](Activities/04-Stu_Diagnosing_the_Model/Solved/diagnosis.ipynb)

Engage the class with a brief Q&A session. Ask students if they have any questions about **confusion matrices** and **classification reports**. If students do not pose any questions, ask some of the below guided questions. Spend no more than 5 minutes on the Q&A session.

* What is a **confusion matrix**?

  * **Answer** A table used to describe the performance of the model. The **confusion matrix** will highlight differences in the number of samples predicted to belong to a specific class with the actual number of samples that do belong to that class.

* Would a user aggregate the columns or rows of a **confusion matrix**?

  * **Answer** Both. Values for columns and rows will be aggregated and then compared. Columns will reflect the sum of predicted categorical outcomes, and the rows will reflect the actual sum of outcomes.

* What is a **classification report**?

  * **Answer** A report that details the precision, recall, and accuracy of the predicted data points for each categorical class. A **classification report** can be used to determine the rate of false positives, false negatives, and the quality of the predictions.

Transition to the dry walk through by opening the solution file, and highlight the below discussion points. Go through this section quickly as students should be well versed in creating **confusion matrices** and **classification reports**.

* A **confusion matrix** is a table that describes the performance of a model by looking at the total number of outcomes for each class. Confusion matrices look at the total number of actual outcomes and juxtaposes them with predicted outcomes.

  * For example, with a confusion matrix, you can aggregate the number of actual positives and compare it to the number of predicted positives. The closer the values, the better the model. The same can be said with negative outcomes.

  * **Confusion matrices** can be a little difficult to understand at first. If students have questions/difficulty understanding, and or seem lost, use the following scenario to help reinforce how a confusion matrix is used:

    ```python
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)
    ```

    ![reading_confusion_matrix.png](Images/reading_confusion_matrix.png)

* Similarly, the **classification report** reveals the precision, recall, and accuracy of the predicted values for each class. These ratios are calculated using the actual and predicted data points.

    ```python
    from sklearn.metrics import classification_report
    target_names = ["No Diabetes", "Diabetes"]
    print(classification_report(y_test, predictions, target_names=target_names))
    ```

Next, transition into the interpretation part of the review activity. Ask students guided questions that will require them to interpret the results from the matrix and report.

* Ask students to interpret the **classification report**. What does it mean for the **diabetes** class to have a lower recall score compared to **no diabetes**?

  * **Answer** The **diabetes** predictions have a lower recall rate which means a higher rate of false negatives. There are individuals being predicted as not having diabetes that actually do. However, the data points predicting no diabetes have a higher recall score which means a lower rate of false negatives.

  * **Answer** The model is arguably precise but could benefit from additional training/fitting to improve predictions and reduce false negatives.

* Reassure students that even if the differences between **precision** and **recall** seem a little fuzzy right now, the difference will eventually make more sense as they interpret more classification reports.

Ask if there are any questions before moving forward.
