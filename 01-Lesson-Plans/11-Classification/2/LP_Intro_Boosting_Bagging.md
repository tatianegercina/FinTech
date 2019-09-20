### 14. Instructor Do: Boosting and Bagging (15 mins) (Critical)

Students are given a formal lecture on **boosting**, **bagging**, its benefits, and its application in advanced analytics. Guided questions are provided to promote student engagement and to re-enforce content.

Navigate to the **boosting** and **bagging** section of the slideshow. Highlight the following:

* Address the class and tell them that if they were to take all of the classification models they've used so far and compared them, they'd find that some algorithms performed better than others, as expected.

  * Indicate that even though some of the other algorithms performed worse, they were able to still execute independently and classify labels with decent accuracy.

  * Explain to students that they will come across algorithms that actually fail at learning in an adequate fashion. These algorithms/classifiers are considered **weak learners**.

Communicate that **weak learners** are a consequence of limited data to learn from. This may mean too few features or the data provided doesn't allow for data points to be classified.

* Provide more context around **weak learners** by defining them as algorithms/classifiers that are unable to accurately learn from the data they are being provided. This is why their predictions are only a little better than random chance. The classifiers can make predictions; however, their predictions are not representative of the relationship between inputs and target.

* **Weak learners** are described as being only slightly better than random chance.

Explain to students that **weak learners** are still valuable in machine learning. This is where **boosting** and **bagging** comes in.

* **Weak learners** are valuable because they can be combined with other classifiers in order to make a more accurate and robust prediction engine. A single **weak learner** will make inaccurate and imprecise predictions. Combined **weak learners** can perform just as well as any other **strong learner**.

  * Classify this type of learning as an example of **ensemble learning**. **Ensemble models** help improve accuracy and robustness, as well as decrease variance.

* Underscore that **weak learners** have to be combined using a specific algorithm. Example algorithms include **GradientBoostedTree** and **GXBoost**.

* Ask students if they have any guess as to what can be done to make a **weak learner** perform more accurately?

  * **Answer** Boost **weak learners** with other algorithms for an **ensemble learning** approach.

* Indicate to students that a decision tree can be classified as a **weak learner**. Ask students what they think would make a decision tree a weak learner:

  * **Answer** The decision tree having only one split (i.e. a stump)

Transition into explaining to students what boosting is and how it benefits machine learning algorithms.

* **Boosting** is both a process and set of algorithms. Boosting is the process of combining a set of **weak learners** into a **strong longer**.

  * **Boosting** algorithms work by taking the predictions of each **weak learner** and aggregating them to produce a more accurate and precise prediction. The goal goal of a boosting algorithm is to combine **weak learners** into **ensemble learners**.

    * For this reason, **boosting algorithms** are considered **meta-algorithms**. Instead of working with and affecting data, **boosting algorithms** work with and affect other algorithms.

  * **Boosting** algorithms use weighted averages (the higher the average the more inaccurate the prediction) to determine what values are misclassified. The algorithm will iterate until there are no weighted predictions.

    * Other algorithms (i.e. **bagging**) create new base learners as older ones prove ineffective.

    ![boosting_flow.jpg](IMages/boosting_flow.jpg)

    * Photo retrieved from [here](https://www.educba.com/boosting-algorithm/). Needs to be recreated.

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

End the activity by letting students know that the next several activities will be dedicated to implementing/applying a GradientBoostedTree **boosting** algorithm to improve decision tree accuracy.

Ask students if they have any questions before moving on.
