### 2. Instructor Do: Logistic Regression (10 mins)

Having been introduced to classification, students will now receive a demonstration of how to use logistic regression to make linear predictions for categorical outcomes. This demo will contain two parts: a brief explanation of preprocessing and a more in-depth explanation of model fitting and execution.

**Files:**

[logistic_regression.pptx](Activities/01-Ins_Logistic_Regression/logistic_regression.pptx)

[Ins_Logistic_Regression.ipynb](Activities/01-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb)

Walk through the slideshow and highlight the following points:

* Communicate that Logistic Regression is a statistical method for predicting binary outcomes from data. With linear regression, our linear model may provide a numerical output such as age. With logistic regression, the numerical value for age could be translated to a probability between 0 and 1. This discrete output could then be labeled as "young" vs "old". The same approach can be used to predict the probability of credit worthiness based off of credit score, number of missed payments, number of public records, and credit age.

  ![logistic_1.png](Images/logistic_1.png)
  ![logistic_2.png](Images/logistic_2.png)
  ![logistic_3.png](Images/logistic_3.png)
  ![logistic_4.png](Images/logistic_4.png)

* Emphasize to students that running a logistic regression model involves 4 steps, which can be applied when running any machine learning model:

  1. Preprocess

  2. Train

  3. Validate

  4. Predict

* We can use logistic regression to predict which category or class a new data point should be classified as.

After presenting the slideshow, open the Jupyter notebook and complete a dry walk through of running logistic regression with  Scikit-Learn (sklearn). Quickly run through the next bullet points, emphasizing that classification algorithms require data to be clustered into classes/groups.

* Communicate to students that the only way to run a logistic regression model is to first prepare a dataset to be used for training the model. In order for a logistic regression model to learn on its own, it must be given data that is clustered in classes/groups.

  * For example, two classes can be created that represent credit risk: **low risk** (purple) and **high risk** (yellow). Logistic regression can then be used to classify new data points/applicants.

    ```python
    from sklearn.datasets import make_blobs

    X, y = make_blobs(centers=2, random_state=42)
    ```

    ![make-blobs.png](Images/make-blobs.png)

* Depending on time, further explain that the process of clustering data points into classes/groups is called **centering**.

  * Explain to students that **centering** is a a part of the pre-process step of advanced analytics that helps dictate the number of classes/groups to create. **Centering** improves the performance of logistic regression models by ensuring that all data points share the same starting mean value. Data points with the same starting mean value are clustered together.

  ![make_blobs_fx.png](Images/make_blobs_fx.png)

* The last step of preprocessing is splitting data into **training** and **testing** data sets. The **training** subset will be used to train the model and help it self learn. The testing data set will be used to evaluate and test the accuracy of the algorithm and its predictions.

  * Emphasize to students that the **training** and **testing** data sets can come from a single data set or two different ones. The **sklearn** `model_selection.train_test_split` module can be used to split a single data set into **training** and **testing** subsets. This will create four data sets:

    * X train

    * X test

    * Y train

    * Y test

    ```python
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    ```

Transition into the next part of the demo by explaining to students that once the preprocessing work has been completed, the logistic regression model can be ran. Demonstrate and explain how logistic regression models are trained and executed.

* **Logistic Regression** can be implemented using the sklearn `LogisticRegression` class. This module is a part of the **linear model** package, a package commonly chosen by developers to run linear regression. The object returned from the `LogisticRegression` class will be  a **classifier** object, which is used to train, validate, and make predictions.

  ![logistic_regression_class.png](Images/logistic_regression_class.png)

* Once a Logistic regression model has been created, it can be **trained**/**fitted**. The model can be **trained** by using the `train` function provided by the `LogisticRegression` object. As stated previously, **classification** is a form of **supervised learning**. In order for the algorithm to learn, it must be given data to learn from. This process is fitting/training.

    ```python
    # Train the data
    classifier.fit(X_train, y_train)
    ```

    ![train_model.png](Images/train_model.png)

The next step after training the model is **validating** it. A common approach is the Train/Test Split approach. Walk students through how this approach is used.

* In order to validate a model, it must be scored, which the **sklearn** `score` function can do. The **testing** data sets are passed to the `score` function, and the function evaluates results. Explain to students that the scoring process takes the predictions made using the training data and compares it to the predictions made using the test data. If the predictions are the same and the score is **1.0**, the model is considered accurate.

* It's important to note to students that two things need to be scored: the **training** AND **test** data.

  * When scoring the training data, the accuracy of the model is applied against the training data it was created with. The more data is trained, the higher the accuracy.

  * Scoring of test data consists of applying the model against the test data. The test data is considered new data the model has not seen. If score will reflect the accuracy of the predictions made by the model using the test data.

  * If the training score is more accurate than the testing score, the model is considered overtrained. **Overtraining** the model can result in **overfitting**, where the model learned rules for predictions that apply mostly just for the training data set. The goal is to have the scores as close to each other in accuracy as possible.

    ```python
    # Score the model
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")
    ```

    ![testing_model.png](Images/testing_model.png)

Once the model is proven to be accurate for both the training and test data, the last step is to actually make predictions using an entirely new data set. Explain to students how the **sklearn** package can be used to make **logistic regression** predictions.

* The **sklearn** `predict` function can be used to apply the model against a new data set. The model will predict which class the new data points will fall into (i.e. low credit risk or high credit risk).

    ```python
    # Generate a new data point (the red circle)
    import numpy as np
    new_data = np.array([[-2, 6]])
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.scatter(new_data[0, 0], new_data[0, 1], c="r", marker="o", s=100)

    # Predict the class (purple or yellow) of the new data point
    predictions = classifier.predict(new_data)
    print("Classes are either 0 (purple) or 1 (yellow)")
    print(f"The new point was classified as: {predictions}")
    ```

    ![predict_new_data.png](Images/predict_new_data.png)

If time remains, show students the results of the predictions made using the test data. Students did not see this because the `score` function executes predictions behind the scenes when calculating accuracy.

* When applying the model against the test data, the `score` function automatically calculates predictions behind the scenes. The **sklearn** `predict` function can be used see the actual predictions made from the data points in the test data set.

    ```python
    # Predict outcomes for test data set
    predictions = classifier.predict(X_test)
    pd.DataFrame({"Prediction": predictions, "Actual": y_test})
    ```

    ![predict_test.png](Images/predict_test.png)

Ask students if there are any questions before moving on. This was a heavy activity, so there will most likely be a number of questions. Try and answer one or two questions if timing permits. If not, ask students to save questions for review, and reiterate the following to students:

* When running a logistic regression model, or any model, follow these simple steps:

    1. Preprocess (i.e. centering)

    2. Train

    3. Validate

    4. Predict
