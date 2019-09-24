### 6. Instructor Do: Decision Trees (10 min)

In this activity, students will be introduced to decision trees and how they can use them for classification problems.

**Files:**

* [decision-trees.ipynb](Activities/03-Ins_Decision-Trees/Solved/decision-trees.ipynb)

* [loans_data_encoded.csv](Activities/03-Ins_Decision-Trees/Resources/loans_data_encoded.csv)

Start by opening the lesson slides, move to the _Decision Trees_ section and highlight the following:

* Decision Trees encode a series of `True/False` questions.

* `True/False` questions can be represented with a series of if/else statements

* There are some key concepts, that it's important to know while working with decision trees:

  * **Root Node:** Represents the entire population or sample data, this node gets divided into two or more homogeneous sets.
  * **Parent Node:** A node that is divided into sub-nodes.
  * **Child Node:** Sub-nodes of a parent node.
  * **Decision Node:** A sub-node that is split into further sub-nodes.
  * **Leaf or Terminal Node:** Nodes that do not split.
  * **Branch or Sub-Tree:** A sub section of entire tree.
  * **Splitting:** Process of dividing a node into two or more sub-nodes.
  * **Pruning:** Process of removing sub-nodes of a decision node.
  * **Tree's Depth:** The number of decision nodes encountered before making a decision.

* Decision trees can become very complex and very deep, depending on how many questions have to be answered. Deep and complex trees tend to overfit to the data and do not generalize well.

Close the presentation, and comment to students that in this demo, you are going to use the loan applications encoded dataset presented before. The goal of this demo, is to predict fraudulent loan applications using a decision tree.

Open the unsolved version of the Jupyter notebook, live code the demo and highlight the following:

* In the initial imports cell, the `tree` module from `sklearn` is imported since it offers a decision tree implementation for classifications problems.

  ```python
  from sklearn import tree
  ```

* One interesting way to analyze a decision tree, is to visualize it. The following libraries are imported to create a visual representation of the decision tree.

  ```python
  import pydotplus
  from IPython.display import Image
  ```

* The [`pydotplus` package](https://anaconda.org/conda-forge/pydotplus) is not installed by default in Anaconda, so students should install it on their virtual environments by executing the following command on the terminal.

  ```bash
  conda install -c conda-forge pydotplus
  ```

* The `loans_data_encoded.csv` is loaded in a DataFrame called `df_loans`.

  ```python
  file_path = Path("../Resources/loans_data_encoded.csv")
  df_loans = pd.read_csv(file_path)
  ```

* Once the data is loaded into the `df_loans` DataFrame, the features and target sets are created. The features set `X` contains all the `df_loans` columns except the `bad` column, the `bad` column is the target variable `y`, where `1` means that the loan application was fraudulent, and `0` that it wasn't.

  ```python
  # Define features set
  X = df_loans.copy()
  X.drop("bad", axis=1, inplace=True)

  # Define target vector
  y = df_loans["bad"].values.reshape(-1, 1)
  ```

Comment to students, that in order to train and validate the decision tree model, the data is split in training and testing sets.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
```

Explain to students, that in order to improve algorithm's performance, the features data will be scaled using the 'StandardScaler`. There is no need to scale the target data, since it contains the labels that we want to predict using the decision tree.

```python
# Creating StandardScaler instance
scaler = StandardScaler()

# Fitting Standard Scaler with the training data
X_scaler = scaler.fit(X_train)

# Scaling data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* After scaling the features data, the decision tree model can be created and trained.

  ```python
  # Creating the decision tree classifier instance
  model = tree.DecisionTreeClassifier()
  ```

* The model is trained with the scaled traning data.

  ```python
  model = model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, some predictions are made using the scaled testing data.

  ```python
  predictions = model.predict(X_test_scaled)
  ```

In oder to evaluate the model, comment to students that a confusion matrix can, the `accuracy_score` and the `classification_report` from `sklearn.metrics` can be used.

* In this particular example, the confusion matrix is created using the `y_test` and the `results` vectors. The matrix shows how well the model predict fraudulent loan applications.

  ```python
  # Calculating the confusion matrix
  cm = confusion_matrix(y_test, predictions)
  cm_df = pd.DataFrame(
      cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
  )

  # Calculating the accuracy score
  acc_score = accuracy_score(y_test, predictions)
  ```

  ![Decision Tree evaluation results](Images/decision-trees-1.png)

* After observing the results, it can be seen that model's accuracy (`0.584`) is low, also precision and recall are not good enough to state that the model will be good predicting fraudulent loan applications.

* It can be concluded that this model may not be the best one for preventing fraudulent loan applications.

Finally, comment to students that an interesting way to analyze a decision tree is by visualizing it, so a visual representation of the final decision tree is created using `pydotplus` library.

![Decision tree visualization](Images/decision-trees-2.png)

Explain to students, that a very large and complex tree shape like this, probably indicates that the model is overfitted to this specific data and won't generalize well to other models.

* To ease the tree visualization, the image can be saved as `PDF` or `PNG`.

  ```python
  # Saving the tree as PDF
  file_path = Path("../Resources/loans_tree.pdf")
  graph.write_pdf(file_path)

  # Saving the tree as PNG
  file_path = Path("../Resources/loans_tree.png")
  graph.write_png(file_path)
  ```

Answer any questions before moving on.
