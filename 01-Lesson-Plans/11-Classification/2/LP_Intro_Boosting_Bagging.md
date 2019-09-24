### 14. Instructor Do: Boosting and Bagging (15 mins) (Critical)

Students are given a formal lecture on **boosting**, **bagging**, its benefits, and its application in advanced analytics. Guided questions are provided to promote student engagement and to re-enforce content.

Navigate to the **boosting** and **bagging** section of the slideshow. Highlight the following:

* **Boosting** is both a process and set of algorithms. Boosting is the process of combining a set of **weak learners** into a **strong longer**.

  * **Boosting** algorithms work by taking the predictions of each **weak learner** and aggregating them to produce a more accurate and precise prediction. The goal goal of a boosting algorithm is to combine **weak learners** into **ensemble learners**.

    * For this reason, **boosting algorithms** are considered **meta-algorithms**. Instead of working with and affecting data, **boosting algorithms** work with and affect other algorithms.

  * **Boosting** algorithms use weighted averages (the higher the average the more inaccurate the prediction) to determine what values are misclassified. The algorithm will iterate until there are no weighted predictions.

    * Other algorithms (i.e. **bagging**) create new base learners as older ones prove ineffective.

    ![boosting_flow.jpg](Images/boosting_flow.jpg)

    * Photo retrieved from [here](https://www.educba.com/boosting-algorithm/). Needs to be recreated.

  * **Boosting** algorithms are so powerful and performant that they've been stealing the spotlight at Kaggle machine learning algorithms competitions. **Boosting** algorithms like XGBoost have consistently outperformed other algorithms in competitions, on multiple occasions. XGBoost's success has put **boosting** algorithms in the spotlight.

Highlight to students that **boosting** is not the only way to make a **weak learner** more robust and accurate. Another approach is called **bagging**.

* **Bagging** is another method used to improve the accuracy and robustness of a model.

* Where **boosting** takes multiple algorithms and coordinates them as an ensemble and runs the algorithms in tandem to identify the best prediction, **bagging** focuses on re-sampling data and running with different models on the fly in order to formulate the most accurate and precise prediction.

* Each classifier used in the **bagging** process runs independently of hte others. Once all classifiers are finished predicting, the **bagging** algorithm will aggregate results.

  * Results for a **bagging** algorithm are then aggregated via a voting process. Each classifier will vote for a label, and then the **bagging** algorithm will aggregate votes and classify the label with the most votes as the prediction.

* One of the key differences between **boosting** and **bagging** is that **boosting** algorithms will weigh predictions based off of accuracy, and as long as data points are weighted as inaccurate, **boosting** algorithms will continue to run. Instead of weighing predictions, **bagging** algorithms resample and replace data in order to improve model fitting and accuracy.

  * Summarize the comparison again to help reinforce the differences:

    * Bagging iteratively weighs inaccurate predictions and continue to execute.

    * Boosting iteratively resamples and replaces data in order to train the best model.

    ![bagging_flow.png](Images/bagging_flow.png)

    * Photo retrieved from [here](https://hackernoon.com/how-to-develop-a-robust-algorithm-c38e08f32201). Will need to be recreated.

If time remains, engage students with the below questions. If there are no conversations, go round-robin.

* Ask if there's a volunteer who would like to summarize the difference between boosting and bagging algorithms.

  * **Answer** Bagging iteratively weighs inaccurate predictions and continue to execute. Boosting iteratively resamples and replaces data in order to train the best model.

* Ask if another volunteer would like to explain what **boosting** and **bagging** algorithms are used for.

  * **Answer** **Boosting** and **bagging** algorithms are used to improve the accuracy and robustness of **weak learners**. Each class of algorithm converts **weak learners** into **strong learners** through **ensemble learning**.

* Ask a final question: what's the difference between **weak learners** and **strong learners**? Address the entire class and let anyone answer.

  * **Answer** **Strong learners** can make predictions with accuracy and precision. **Weak learners** make predictions that are only slightly better than random chance.

Ask students if they have any questions before moving on.
