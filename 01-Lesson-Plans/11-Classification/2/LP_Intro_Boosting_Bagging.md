### 14. Instructor Do: Boosting and Bagging (15 mins) (Critical)

Students are given a formal lecture on boosting, bagging, its benefits, and its application in advanced analytics. Guided questions are provided to promote student engagement and to re-enforce content.

Navigate to the **boosting** and **bagging** section of the slideshow. Highlight the following:

* Address the class and tell them that if they were to take all of the classification models they've used so far and compared them, they'd find that some algorithms performed better than others, as expected.

  * Indicate that even though some of the other algorithms performed worse, they were able to still execute independently and classify labels with decent accuracy.

  * Explain to students that they will come across algorithms that actually fail at learning in an adequate fashion. These algorithms/classifiers are considered **weak learners**.

  * Define **weak learners** as algorithms/classifiers that are unable to accurately learn from the data they are being provided. The classifiers can make predictions; however, their predictions are not representative of the relationship between inputs and target.

  * **Weak learners** are described as being only slightly better than random chance.

* Explain to students that **weak leaners** are still valuable in machine learing. Ask students if they have any guess as to what can be done to make a **weak learner** perform more accurately?

  * **Answer** Boost **weak learners** with other algorithms for an **ensemble learning** approach.

* Indicate to students that a decision tree can be classified as a **weak learner**. Ask students what they think would make a decision tree a weak learner:

  * **Answer** The decision tree having only one split (i.e. a stump)

Transition into explaining to students what boosting is and how it benefits machine learning algorithms.

* Boosting is both a process and an algorithm.

* Boosting is used to convert weak learners into strong learners

* Boosting reduces bias and variance in predictions
