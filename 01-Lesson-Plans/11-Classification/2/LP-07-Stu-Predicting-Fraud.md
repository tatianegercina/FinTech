### 7. Students Do: Predicting Fraudulent Credit Card Transactions (10 min)

In this activity, students will create a decision tree model to predict fraudulent credit card transactions.

**Instructions:**

* [README.md](Activities/04-Stu_Predicting_Fraud/README.md)

**Files:**

* [preventing-fraud.ipynb](Activities/04-Stu_Predicting_Fraud/Unsolved/preventing-fraud.ipynb)

* [transactions_data_encoded.csv](Activities/04-Stu_Predicting_Fraud/Resources/transactions_data_encoded.csv)

---

### 8. Instructor Do: Review Predicting Fraudulent Credit Card Transactions (10 min)

**Files:**

* [preventing-fraud.ipynb](Activities/04-Stu_Predicting_Fraud/Solved/preventing-fraud.ipynb)

Open the solution, and live code the review by highlighting the following:

* As it was shown on the previous explanation, the `tree` module from `sklearn` should be imported to create a decision tree model instance.

  ```python
  from sklearn import tree
  ```

* In order to create the decision tree graph, the following libraries are imported.

  ```python
  import pydotplus
  from IPython.display import Image
  ```

* The data from the `transactions_data_encoded.csv` file, is loaded in a pandas DataFrame called `df_transactions`.

  ```python
  file_path = Path("../Resources/transactions_data_encoded.csv")
  df_transactions = pd.read_csv(file_path)
  ```

* After loading the data, the features and target sets are defined.

  ```python
  # Define features set
  X = df_transactions.copy()
  X.drop("isFraud", axis=1, inplace=True)

  # Define target vector
  y = df_transactions["isFraud"].values.reshape(-1, 1)
  ```

* The data is split into training and testing set, using the `train_test_split` method from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
  ```

* In order to improve algorithm's performance, the features data is scaled using the `StandardScaler`  method from `sklearn`.

  ```python
  # Create the StandardScaler instance
  scaler = StandardScaler()

  # Fit the Standard Scaler with the training data
  X_scaler = scaler.fit(X_train)

  # Scale the training data
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Recall to students, that the target data is not scaled since it contains the classes that you want to predict with the decision tree.

* Once the data is scaled, the decision tree model is created and fitted with the training data.

  ```python
  # Create the decision tree classifier instance
  model = tree.DecisionTreeClassifier()

  # Fit the model
  model = model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, some predictions are made using the testing data.

  ```python
  # Making predictions using the testing data
  predictions = model.predict(X_test_scaled)
  ```

* The model is evaluated using `sklearn` to calculate the confusion matrix, the accuracy score and to generate the classification report.

  ![Model's evaluation results](Images/preventing_fraud_review_1.png)

Comment to students, that despite model's accuracy is high, this model is not precisely predicting the fraudulent transactions as it can be seen after reviewing the precision and recall value. Remind students, that this is why getting the classification report is always important to evaluate a classification model.

Continue live coding the review, by creating the model graph using the `pydotplus` library and highlight the following.

```python
# Create DOT data
dot_data = tree.export_graphviz(
    model, out_file=None, feature_names=X.columns, class_names=["0", "1"], filled=True
)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

# Show graph
Image(graph.create_png())
```

![Transaction tree graph](Images/transactions_tree.png)

* The tree is to deep, however it can be observed that only one subtree grows.

* This phenomenon occurs when the target classes are imbalanced.

* Having imbalanced target classes is a common problem in classification machine learning algorithms, when there are a disproportionate ratio of observations in each class.

Comment to students, that they will learn how to deal with imbalanced classes in next class.

Answer any questions before moving on.
