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
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import GradientBoostingClassifier
    ```

* Remind students that data has already been normalized/standardized with categories encoded. The `sklearn.preprocessing` `StandardScaler` functions was used to do this.

* The `GradientBoostingClassifier` has four main arguments: `n_estimators`, `learning_rate`, `max_depth`, and `random_state`. Explain each of these parameters while configuring them.

  * The `n_estimators` paramater configures the number of **weak learners** being used with the **boosting** algorithm. The higher the value of `n_estimators`, the more trees that will be created to train the algorithm. The more trees, the better the performance.

  * `Learning_rate` controls overfitting. Smaller values should be used when setting `learning_rate`. `Learning_rate` will work with `n_estimators` to identify the number of **weak learners** to train.

    * The values should be between 0 and 1.

    * A common technique is to loop through a range of **learning rates**, creating and fitting the classifier with each value in the range. Once the classifier is created, it can be scored. The **learning rate** with the highest test accuracy should be used.

  * The `max_depth` argument identifies the size/depth of each decision tree being used. `Max_depth` will dictate the number of levels between leaf nodes and the root.

Explain that using the `GradientBoostingClassifier` is like using any other machine learning algorithm: it requires training data, fitting, and scoring.

* The `GradientBoostingClassifier` will require values for arguments `n_estimators`, `learning_Rate`, and `max_depth`. The defaults will be used for `n_estimators` and `max_depth`.

* In order to determine the optimal `learning_rate`, a loop is used to iterate over each possible `learning_rate`, and then the model is built and scored using that value. The **learning rate** with the highest test accuracy should be chosen.

    ```python
    # Create a classifier object
    learning_rates = [0.05, 0.1, 0.25, 0.5, 0.75, 1]
    for learning_rate in learning_rates:
        classifier = GradientBoostingClassifier(n_estimators=20,
                                                learning_rate=learning_rate,
                                                max_features=5,
                                                max_depth=3,
                                                random_state=0)

        # Fit the model
        classifier.fit(X_train_scaled, y_train.ravel())
        print("Learning rate: ", learning_rate)

        # Score the model
        print("Accuracy score (training): {0:.3f}".format(classifier.score(X_train_scaled, y_train.ravel())))
        print("Accuracy score (validation): {0:.3f}".format(classifier.score(X_test_scaled, y_test.ravel())))
        print()
    ```

    ![iterate_learning_rate.png](Images/iterate_learning_rate.png)

* The **learning rate** of `0.75` resulted in the highest test accuracy. Create a new classifier using this learning rate. Then, fit the model, score it, and then make predictions using the test data.

    ```python
    # Choose a learning rate and create classifier
    classifier = GradientBoostingClassifier(n_estimators=20,
                                            learning_rate=0.75,
                                            max_features=5,
                                            max_depth=3,
                                            random_state=0)

    # Fit the model
    classifier.fit(X_train_scaled, y_train.ravel())

    # Make Prediction
    predictions = classifier.predict(X_test_scaled)
    pd.DataFrame({"Prediction": predictions, "Actual": y_test.ravel()}).head(20)
    ```

    ![gb_model.png](Images/gb_model.png)

* Determine the accuracy rate using the `accuracy_score` function.

    ```python
    # Calculating the accuracy score
    acc_score = accuracy_score(y_test, predictions)
    print(f"Accuracy Score : {acc_score}")
    ```

  ```
  Accuracy Score : 0.568
  ```

* Evaluate the performance of the model by generating a **confusion matrix** and **classification report**.

    ```python
    # Generate the confusion matrix
    cm = confusion_matrix(y_test, predictions)
    cm_df = pd.DataFrame(
        cm, index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"]
    )

    # Displaying results
    display(cm_df)

    # Generate classification report
    print("Classification Report")
    print(classification_report(y_test, predictions))
    ```

    ![gb_evaluation.png](Images/gb_evaluation.png)

* If time remains, show students how to visualize the boosted tree. Use the `tree.export_graphviz` function and `pydotplus.graph_from_dot_data`.

    ```python
    # Graph tree
    dot_data = tree.export_graphviz(
        classifier.estimators_[9, 0],
        out_file=None, filled=True,
        rounded=True,
        special_characters=True,
        proportion=True,
    )

    graph = pydotplus.graph_from_dot_data(dot_data)
    Image(graph.create_png())
    ```

    ![gb_tree.png](Images/gb_tree.png)

Ask if there any questions before moving on.
