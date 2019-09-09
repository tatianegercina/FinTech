### 3. Students Do: Predicting Diabetes (15 mins)

In this activity, students will use the **sklearn** library to execute **logistic regression** models in order to predict whether or not an individual has diabetes. Students will leverage the material covered in the corresponding instructor demo activity to complete this MSMD activity.

**Instructions:**

* [README.md](Activities/02-Stu_Diabetes/README.md)

**Files:**

* [diabetes_lr.ipynb](Activities/02-Stu_Diabetes/Unsolved/diabetes_lr.ipynb)

### 4. Instructor Do: Predicting Diabetes Activity Review (10 mins)

**Files:**

* [diabetes_lr.ipynb](Activities/02-Stu_Diabetes/Solved/diabetes_lr.ipynb)

Open the solution and complete a dry walk through of the solution . Answer any questions that students have.

* Reiterate to students that in order to run a logistic regression model, a training and testing data set are required. A single data set can be split into these two subsets using the **sklearn** `train_test_split` function. Explain that these two data sets will be used to validate the accuracy of the model.

    ```python
    # Use the train_test_split function to create training and testing data sets
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    ```

* In order to run a logistic regression model, a logistic regression model object is needed. The **sklearn** `LogisticRegression` module is a common module used.

    ```python
    # Use the LogisticRegression module from the sklearn package to create a model
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state=1)
    classifier
    ```

    ![create_lr_model.png](Images/create_lr_model.png)

* Once a model is created, it has to be trained. After training, the model can be scored, and it can then be used to make predictions for new data points.

    ```python
    # Fit the model
    classifier.fit(X_train, y_train)

    # Score the model
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")

    # Make predictions
    predictions = classifier.predict(X_test)
    results = pd.DataFrame({"Prediction": predictions, "Actual": y_test}).reset_index(drop=True)
    results
    ```

    ![running_lr.png](Images/running_lr.png)

If time remains, facilitate a discussion around model evaluation using the following questions. Be mindful of pacing. Also encourage students to ask any of their own questions.

* How well did your model perform?

* How do you know? Did you count the results?

* If you were asked to diagnose a patient, how confident would you be in your model's prediction?

Explain to students that in addition to the accuracy score, there are other metrics that we can use for model evaluation such as precision and recall.

Ask if there are any questions before moving forward.
