### 10. Instructor Do: Introduction to Ensemble Learning (10 min)

In this activity, students will be introduced to ensemble learning, weak learners and random forest.

Navigate to the _Introduction to Ensemble Learning_ section of the Lesson 11.2 slides. Highlight the following:

* Address the class and tell them that if they were to take all of the classification models they've used so far and compared them, they'd find that some algorithms performed better than others, as expected.

  * Indicate that even though some of the other algorithms performed worse, they were able to still execute independently and classify labels with decent accuracy.

  * Explain to students that they will come across algorithms that actually fail at learning in an adequate fashion. These algorithms/classifiers are considered **weak learners**.

Communicate that **weak learners** are a consequence of limited data to learn from. This may mean too few features or the data provided doesn't allow for data points to be classified.

* Provide more context around **weak learners** by defining them as algorithms/classifiers that are unable to accurately learn from the data they are being provided. This is why their predictions are only a little better than random chance. The classifiers can make predictions; however, their predictions are not representative of the relationship between inputs and target.

* **Weak learners** are described as being only slightly better than random chance.

Explain to students that **weak learners** are still valuable in machine learning.

* **Weak learners** are valuable because they can be combined with other classifiers in order to make a more accurate and robust prediction engine. A single **weak learner** will make inaccurate and imprecise predictions. Combined **weak learners** can perform just as well as any other **strong learner**.

  * Classify this type of learning as an example of **ensemble learning**. **Ensemble models** help improve accuracy and robustness, as well as decrease variance.

* Underscore that **weak learners** have to be combined using a specific algorithm. Example algorithms include **GradientBoostedTree** , **XGBoost**, and **Random Forests**.

* Ask students if they have any guess as to what can be done to make a **weak learner** perform more accurately?

  * **Answer** Boost **weak learners** with other algorithms for an **ensemble learning** approach.

* Indicate to students that a decision tree could be classified as a **weak learner**. Ask students what they think would make a decision tree a weak learner:

  * **Answer** The decision tree having only one split (i.e. a stump)

Continue the presentation by introducing the random forest algorithm, and highlight the following:

* Instead of a having single, complex tree like the ones created by decision trees, a random forest algorithm will sample the data and build several smaller, simpler decisions trees.

* In a random forest, each tree is much simpler because it is built from a subset of the data.

* These simple trees are created by randomly sampling the data and creating a decision tree for only that small portion of data. This is known as a **weak classifier** because it is only trained on a small piece of the original data and by itself is only slightly better than a random guess. However, many _slightly better than average_ small decision trees can be combined to create a **strong classifier**, which has much better decision making power.

* Some of the benefits of the decision tree algorithm are:

  * It’s robust against overfitting because all of those weak classifiers are trained on different pieces of the data.

  * It can be used to rank the importance of input variables in a natural way.

  * It can handle thousands of input variables without variable deletion.

  * It´s robust to outliers and non-linear data. Random forest handles outliers by binning them. It's also indifferent to non-linear features.

  * It runs efficiently on large databases.

Answer any questions before moving on.
