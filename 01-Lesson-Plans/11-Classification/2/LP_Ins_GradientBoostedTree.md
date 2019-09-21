### 15. Instructor Do: Gradient Boosted Tree (10 mins) (Critical)

The instructor will provide a demonstration on how to use **boosting** in **sklearn** to improve the performance of a decision tree.

**File:** [gradient_boosted_tree.ipynb](Activities/15-Ins_Gradient_Boosted_Tree/Solved/gradient_boosted_tree.ipynb)

Open the unsolved file, and live code the following. Make sure to touch upon the below discussion points while coding.

* It's important to remember that **boosting** involves a set of meta-algorithms that are used to improve the performance of **weak learners**.

* There are a number of algorithms/libraries available. This activity and the next will focus on how to use the **sklearn** `GradientBoostingClassifier` algorithm.

* The `GradientBoostingClassifier` is a part of the `sklearn.ensemble` package. Like any other **sklearn** library, it has to be imported into the Python environment.

    ```python
    import pandas as pd
    from path import Path
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.ensemble import GradientBoostingClassifier
    ```

* Remind students that because we are working with categorical data, numeric values have to be converted to categories. The `sklearn.preprocessing` `StandardScaler` functions is used to do this.

* The `GradientBoostingClassifier` has four main arguments: `n_estimators`, `learning_rate`, `max_depth`, and `random_state`. Explain each of these parameters while configuring them.

  * The `n_estimators` paramater configures the number of **weak learners** being used with the **boosting** algorithm. The higher the value of `n_estimators`, the more trees that will be created to train the algorithm. The more trees, the better the performance.

  * `Learning_rate` controls overfitting. Smaller values should be used when setting `learning_rate`. `Learning_rate` will work with `n_estimators` to identify the number of **weak learners** to train.

    * The values should be between 0 and 1.

    * A common technique is to loop through a range of **learning rates**, creating and fitting the classifier with each value in the range. Once the classifier is created, it can be scored. The **learning rate** with the highest test accuracy should be used.

  * The `max_depth` argument identifies the size of each decision tree being used.

Explain that using the `GradientBoostingClassifier` is like using any other machine learning algorithm: it requires data, training, and scoring.

* Use the `sklearn.make_blobs` function to generate data for the algorithm.

* Split the data into train and test segments using `sklearn.train_test_split`.

* Create a classifier object using the `GradientBoostingClassifier` module.

    ```python
    classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    ```

* Train the model using the training data.

    ```python
    classifier.fit(X_train, y_train)
    ```

* Score the model using the `sklearn.score` function.

    ```python
    classifier.score(X_train)
    ```

* Now it's time to predict! Use the `sklearn.predict` function to make a prediction using the **ensemble learners** and the **test** data.

    ```python
    classifier.predict(X_test, y_test)
    ```

* Evaluate the model using the `sklearn.classification_report` and `sklearn.confusion_matrix` classes.
