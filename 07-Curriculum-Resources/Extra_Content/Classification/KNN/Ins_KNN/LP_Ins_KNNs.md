### 18. Instructor Do: K-Nearest Neighbor (10 mins) (Critical)

The instructor introduces students to another algorithm: K-Nearest Neighbor.

**Files:** [ins_knn.ipynb](Activities/08-Ins_KNN/Solved/ins_knn.ipynb)

Navigate to the K-Nearest Neighbor section of the slideshow, and highlight the following:

* Mention to students that many of the classification problems they've seen so far have been linear in nature. However, there will circumstances where outcomes are unaffected by the change in inputs.

* Logistic Regression and SVM are great algorithms for classifying linear data points. However, there are instances when non-linear classification is required. K-Nearest neighbors is a great algorithm for non-linear classification.

* Explain that **non-linearity** is a type of relationship where the outcome is not dependent on inputs; change in both outcome and inputs are independent of another and disproportionate.

* Communicate that **non-linear** data are more difficult to classify due to the lack of relationship between outcome and inputs. Most non-linear algorithms utilize a trial and error approach due to this difficulty.

* Summarize how non-linear analysis works. Explain that because of the randomness of values with non-linear analysis, non-linear regression employs a **sum of squares** methodology.

* Explain the **sum of squares** approach. Reinforce to students that the smaller the **sum of squares**, the better the non-linear model.

  1. Finding the difference between the mean and each data point

  2. The differences for each data point is squared

  3. Squared values are then aggregated

Open the solution file, and live code how to build and execute the **K-Nearest Neighbor (KNN)** algorithm:

* The **K-Nearest Neighbor** algorthim uses a non-linear approach to classification. The **KNN** algorithm predicts classification by locality. By identifying all of the neighbors for a data point, as well as their classification, the **KNN** algorithm is able to predict the class of new data points.

  * A good way to remember and understand this algorithm is with the saying "You are who your friends are".

* The **KNN** algorithm can be built using the **sklearn** `neighbors.KNeighborsClassifier` object. This has to be imported into the Python environment. Import the `KNeighborsClassifier` library.

    ```python
    from sklearn.neighbors import KNeighborsClassifier
    ```

* Like with linear regression, non-linear regression models also need test and training data. The `train_test_split` function can be used to generate these subsets. Create a data set to use and split it into test and train subsets.

    ```python
    X, y = sklearn.datasets.make_moons(noise=0.3, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], c=y)

    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)
    ```

As stated previously, the KNN algorithm focuses on identifying the number of nearest neighbors for classification. Walk students through how to identify the optimal value for `K`.

* `K` represents the number of neighbors required to classify a label for the data point. The best way to find the optimal `K` is through trial and error; execute the model multiple times and evaluate the performance as you increase and decrease `K`.

* The best way to find the optimal `K` value is to loop through a range of numbers, and set each number to `K`. Then, fit the model with the data and score it. The first `K` value with the highest accuracy score should be used as `K`. Storing each iterations score in an array is an easy way to keep track of model scores and their relationship to `K`.

    ```python
    from sklearn.neighbors import KNeighborsClassifier

    # Loop through different k values to see which has the highest accuracy
    # Note: We only use odd numbers because we don't want any ties
    train_scores = []
    test_scores = []
    for k in range(1, 20, 2):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        train_score = knn.score(X_train, y_train)
        test_score = knn.score(X_test, y_test)
        train_scores.append(train_score)
        test_scores.append(test_score)
        #print(f"predictions: {prediction}, actual= {y_test}")
        print(f"k: {k}, Train/Test Score: {train_score:.3f}/{test_score:.3f}")
    ```

  ![finding_k.png](Images/finding_k.png)

  * It's important to note that if the number of features is even, `K` should be odd, and vice versa.

Next, demonstrate to students how to use the KNN model to make predictions.

* **KNN** finds the label of the nearest neighbor(s), and then assigns that same label to the data point being evaluated. When more than one neighbor is specified, the label shared by the majority of the neighbors is used as the label for the data point. The key is finding the optimal number of values to use.

* Once the optimal `K` value has been identified, it can be used to configure the model. Then, predictions can be made using the `predict` function.

    ```python
  # Note that k: 7 provides the best accuracy where the classifier starts to stabilize
  knn = KNeighborsClassifier(n_neighbors=7)
  knn.fit(X_train, y_train)
  print('k=7 Test Acc: %.3f' % knn.score(X_test, y_test))

  # Make prediction
  prediction = knn.predict(X_test)
  df = pd.DataFrame({"Prediction": prediction,
                  "Actual": y_test})
  df
    ```

  ![knn_predict .png](Images/knn_predict.png)

* Communicate that the number of neighbors decides what the classification is. The lower the number of neighbors, the more accurate the prediction, and the lower the bias. The higher the number of neighbors, the less accurate and precise the prediction because of higher bias.

  * It's important to note that a `K` value of 1 can also have bias.

End the activity noting to students that when applied correctly with a non-linear circumstance, the **KNN** algorithm can out-perform both SVM and Logistic Regression.

Ask if there are any questions. Then continue to the next activity.
