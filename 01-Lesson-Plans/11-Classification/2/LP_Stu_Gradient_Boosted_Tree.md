### 16. Students Do: Turbo Boost (10 min)

Students will complete a MSMD activity where they use the **sklearn** `GradientBoostedClassifier` **boosting** algorithm to detect fraudulent transactions using **ensemble learning**.

**Instructions:** [README.md](Activities/16-Stu_Gradient_Boosted_Tree/README.md)

**Files:** [boost_of_power.ipynb](Activities/16-Stu_Gradient_Boosted_Tree/Unsolved/boost_of_power.ipynb)

- - -

### 17. Instructor Do: Turbo Boost Activity Review (10 min)

**Files:** [boost_of_power.ipynb](Activities/16-Stu_Gradient_Boosted_Tree/Solved/boost_of_power.ipynb)

Open the solution and explain the following:

* The `GradientBoostedClassifier` model was able to produce incredibly high accuracy scores, higher than some of the algorithms we've seen. What about the `GradientBoostedClassifier` makes it better performant than some other algorithms?

  * **Answer** `GradientBoostClassifier` is an **ensemble learning** algorithm. It pools **weak learners** together and executes them in parallel in order to refit the model as needed. Because it leverages multiple algorithms and runs them in parallel, `GradientBoostClassifier`is a more robust algorithm than average.

    ![gradient_boosting_classifier.png](Images/gradient_boosting_classifier.png)

* Even though the accuracy score was high, the classification report shows the precision and recall for detecting one class was significantly greater than the classification for the other class.

  * Explain that this is because the classes are imbalanced, meaning that the algorithm was able to make predictions for one class better than it was for another, and as a result, the algorithm developed bias.

  * Let students know that they will learn what imbalanced classes are and how to deal with them in the next class.

    ![imbalanced_results.png](Images/imbalanced_results.png)

* What are the three main parameters for the `GradientBoostClassifier` model?

  * **Answer** **n_estimators**, **learning_rate**, and **max_depth**.

    * `n_estimators` determines the number of trees/weak learners to use.

    * `learning_rate` identifies how aggressive the algorithm will learn.

    * `max_depth` dictates the size of each tree.

* Remind students that **boosting** algorithms are supervised learning algorithms and they are built and trained just like any other algorithm. They can perform better than other algorithms because they make iterative predictions using more than one classifier.

Use the rest of the time for students to ask questions. If there are no questions, ask students how they're feeling about decision trees and **boosting** algorithms.

Move onto the next activity.
