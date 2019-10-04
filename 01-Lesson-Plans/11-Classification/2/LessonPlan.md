## 11.2 Lesson Plan: Trees and Ensemble Learning

---

### Overview

By the end of Today's class, students will recognize the benefits of using tree-based algorithms for classifications problems, also students will gain hands on experience with random forests and ensemble methods such as bagging and boosting.

Today´s lesson also introduce students on dealing with categorical data in machine learning, students will be able to identify when is worth to use categorical data as a feature in a model.

### Class Objectives

By the end of the unit, students will be able to:

* Identify when categorical variables are useful for a machine learning algorithm.

* Perform feature engineering on categorical features and convert labels to numerical class representations.

* Recognize the type of business cases where decision trees and random forests are a suitable solution for classifications problems.

* Demonstrate how random forest performs better than decision trees by avoiding overfitting.

* Identify the pros and cons of tree-based algorithms.

* Understand the implications of overfitting and how boosting and bagging can help to deal with it.

* Apply Gradient Tree Boosting models in classification problems.

---

### Instructor Notes

* Today's class is focused on teaching students how tree-based algorithms can be used for classification problems. Students start with an introduction to decision trees and are then introduced to Ensemble Learning algorithms such as Random Forests and Gradient Boosted Trees.

* tree-based algorithms have a wide range of applications, but today's class will use them for risk analysis scenarios.

* Some of the demos in Today's class will use a lot of memory to train the models which may throw warning messages in Jupyter. Reassure students that these warnings are typically not critical and can largely be ignored.

* Overfitting is a common problem in machine learning that will be discussed today, so take your time to understand its implications and how the techniques covered in this class can help to avoid it.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 11.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Day 2 introduces students to tree-based algorithms and Ensemble Learners such as Random Forests and Gradient Boosted Trees. Students will get experience applying this new family of machine learning algorithms to a variety of classification problems. This will also tie in with day 3 as a potential solution to imbalanced classes which will be seen later in the lesson.

Open the lesson slides and welcome students to day 2 by highlighting the following:

* Today a new family of machine learning algorithms is going to be introduced: _tree-based algorithms_.

* tree-based algorithms are supervised learning methods that are mostly used for classifications and regression problems.

* This class will cover the following algorithms and methods:

  * Decision trees
  * Random forest
  * Weak learners
  * Ensemble methods

Ask for any additional questions before moving on.

---

### 2. Instructor Do: Dealing with Text and Categorical Data in Machine Learning (10 min)

In this activity, students will learn how categorical data should be preprocessed to be used in machine learning algorithms.

**Files:**

* [categorical-data.ipynb](Activities/01-Ins-Categorical-Data/Solved/categorical-data.ipynb)

Set up this activity by explaining that before we dig into the tree-based algorithms, we need to briefly discuss the problem of categorical input features and the need for pre-processing and scaling input features.

Explain to students that while many datasets contain categorical features such as gender labels or risk categories, machine learning algorithms only work with numerical data.

Explain to students that in order to use text or categorical data in a machine learning algorithms, these kind of data values should be converted to numerical representations.

Additionally, many machine learning algorithms and models are sensitive to input features with wide ranges of numbers. A best practice for preparing the numerical input data is normalize all of the data to the same scale. This prevents any single feature from dominating the others.

Tell students that we will use `pandas` and the `preprocessing` library of `sklearn` to encode text and categorical data as numbers and to normalize all numerical inputs to the same scale. These preprocessing steps are critical for many machine learning algorithms.

Open the Jupyter notebook and highlight the following:

* On the _initial imports_ cell, two functions from the `preprocessing` library of `sklearn` are imported.

  ```python
  from sklearn.preprocessing import LabelEncoder, StandardScaler
  ```

* [The `LabelEncoder` function](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) performs integer encoding of labels.

* [The `StandardScaler` function](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) will be used to standardize numerical features.

Explain to students that they will use simulated data about loans. There is a total of 500 records in the dataset where each row represents a loan application along an arbitrary year. Every column represents the following data about each loan application.

* `amount`: The loan amount in USD.
* `term`: The loan term in months.
* `month`: The month of the year when the loan was requested.
* `age`: Age of the loan applicant.
* `education`: Educational level of the loan applicant.
* `gender`: Gender of the loan applicant.
* `bad`: Stands for a bad or good loan applicant (`1` - bad, `0` - good).

Continue the demo by loading the dataset on the `loans_df` DataFrame and highlight the following:

* The dataset has three text features: `month`, `education`, and `gender`.

    ![Original loans dataset](Images/categorical-data-1.png)

* In order to use this dataset to train a machine learning model, these three features need to be converted to numerical values.

* There are different methods to deal with text and categorical data, one of the simplest is _integer encoding_, where every different text value or label is represented as an integer.

* The `preprocessing` library of `sklearn`, contains some functions to encode text labels.

* The `LabelEncoder` function, encodes text labels with integer values between `0` and the total number of classes minus `1`.

* To start using the `LabelEncoder` method, first an instance should be created.

    ```python
    label_encoder = LabelEncoder()
    ```

* Once the `LabelEncoder` instance is created, it should be trained (fit) with the text data you want to encode. The fit step is learning how many classes to use for the encoding. The first example shows how the `LabelEncoder` can be fitted with one column of a DatFrame.

    ```python
    label_encoder.fit(loans_df["month"])
    ```

* After fitting the `LabelEncoder`, the classes identified can be retrieved from the `classes_` attribute.

    ![Label Encoder classes](Images/categorical-data-2.png)

* To encode the text labels as integer numbers, the `transform` method is used to create a new column in the DataFrame with the `month` column values encoded as numbers.

    ```python
    loans_df["month_le"] = label_encoder.transform(loans_df["month"])
    ```

Show the DataFrame's head and show that there is actually a problem with using `LabelEncoder` for all of the cateogrical data in this dataframe. Explain that there is a contextual issue in this particular case: the number assigned to some months doesn't match with the actual month number (e.g. `july` is encoded as `5`)

![Months' names encoded as numbers with Label Encoder](Images/categorical-data-3.png)

* Despite this encoding being technically correct, it can lead to misconceptions while doing further data analysis.

* The `LabelEncoder` is a great tool, but in some particular cases, a manual integer encoding could be used.

Explain to students that, in this particular case, a dictionary with the months' number is created to encode the months' names with their corresponding month number.

```python
months_num = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# Months' names encoded using the dictionary values
loans_df["month_num"] = loans_df["month"].apply(lambda x: months_num[x])
```

* The resulting DataFrame, contains the encoded months' names with a more meaningful numeric value for this context.

    ![Meaningful encoded months' names](Images/categorical-data-4.png)

* The `month` and `month_le` columns are dropped since they won't be used anymore.

    ```python
    loans_df.drop(["month", "month_le"], axis=1, inplace=True)
    ```

Explain to students that there is actually another consideration with this type of encoding. Certain machine learning models may actual place numerical significance on integer encodings. For example, the 12th month has a larger numerical encoding that may bias certain models. In cases like this, a binary encoding method can be used.

Remind students that they have already seen binary encoded data with the Pandas `get_dummies` function.

* The `get_dummies` transforms each categorical feature into new columns with a `1` (True) or `0` (False) encoding to represent if that categorical label was present or not in the original row.

* As a first example, the `gender` column is encoded.

  ![gender column binary encoded](Images/categorical-data-5.png)

* It's also possible to encode multiple columns using `get_dummies`.

  ```python
  loans_binary_encoded = pd.get_dummies(loans_df, columns=["education", "gender"])
  ```

* Once the categorical data is encoded, the resulting DataFrame is saved as a `CSV` file for further usage.

  ```python
  file_path = Path("../Resources/loans_data_encoded.csv")
  loans_binary_encoded.to_csv(file_path, index=False)
  ```

Tell students, that the final step we need to perform is scaling and normalization. Many machine learning algorithms will perform better with a normalized (scaled) dataset.

Explain to students, that some models are sensitive to very large numerical values and may not be able to converge due to those features. It's always a good idea to have features all on the same scale so they have equal importance to the model.

* `sklearn` provides a variety of scaling and normalization options. The two most common are `MinMaxScaler` and `StandardScaler`.

* `MinMaxScaler` will scale the data between 0 and 1.

* `StandardScaler` standardizes the features by removing the mean and scaling to unit variance.

* `StandardScaler` can be used when you don't know anything about your data.

* To use `StandardScaler` the `model -> fit-> predict/transform` workflow is also used.

  ```python
  # Creating the scaler instance
  data_scaler = StandardScaler()

  # Fitting the scaler with the encoded data
  data_scaler.fit(loans_binary_encoded)

  loans_data_scaled = data_scaler.transform(loans_binary_encoded)
  ```

* The resulting data is ready to be used for a machine learning model.

  ![Scaled data](Images/categorical-data-6.png)

Answer any questions before moving on.

---

### 3. Student Do: Encoding Categorical Data for Machine Learning (10 min)

In this activity, students are tasked to encode some categorical and text features of a dataset that contains `2097` loans applications. In forthcoming activities, they will use this dataset to predict defaulted loan applications.

**Instructions:**

* [README.md](Activities/02-Stu_Categorical_Data/README.md)

**Files:**

* [encoding-categorical-data.ipynb](Activities/02-Stu_Categorical_Data/Unsolved/encoding-categorical-data.ipynb)

* [sba_loans.csv](Activities/02-Stu_Categorical_Data/Resources/sba_loans.csv)

---

### 4. Instructor Do: Review Encoding Categorical Data for Machine Learning (10 min)

**Files:**

* [encoding-categorical-data.ipynb](Activities/02-Stu_Categorical_Data/Solved/encoding-categorical-data.ipynb)

Walk through the solution and highlight the following:

* To encode the `Month` column, a dictionary that maps months' names with their numerical values is created using the `month_name` method from the `calendar` module.

  ![Months dic](Images/months-dic.png)

* The `Month` column is encoded using a `lambda` function that looks for the dictionary's values using the month number as key.

  ```python
  loans_df["Month"] = loans_df["Month"].apply(lambda x: name_to_num[x])
  ```

* The `LabelEncoder´ from `sklearn` is used to encode the `RealEstate`, `RevLineCr` and `UrbanRural` columns, following the Model -> Fit -> Predict/Transform API workflow.

  ```python
  # Create the LabelEncoder instance
  le = LabelEncoder()

  # Fitting and encoding the columns with the LabelEncoder

  # RealEstate column
  le.fit(loans_df["RealEstate"])
  loans_df["RealEstate"] = le.transform(loans_df["RealEstate"])

  # Encoding RevLineCr column
  le.fit(loans_df["RevLineCr"])
  loans_df["RevLineCr"] = le.transform(loans_df["RevLineCr"])

  # Encoding UrbanRural column
  le.fit(loans_df["UrbanRural"])
  loans_df["UrbanRural"] = le.transform(loans_df["UrbanRural"])
  ```

* The the `Bank`, `State` and `City` columns, are binary encoded using the Pandas `get_dummies()` function. This will increase the number of columns in the DataFrame up to `684` columns.

  ![Binary Encoding sample](Images/encoding-categorical-1.png)

* Finally, the preprocessed DataFrame is saved as a `CSV` file named `sba_loans_encoded.csv` for forthcoming usage.

Answer any questions before moving on.

---

### 5. Instructor Do: Walking into the Algorithms Forest (5 min)

In this lesson, students will be introduced to tree-based algorithms and the `sklearn` modules that implements this algorithmic family.

Open the lesson slides, go to the _Walking into the Algorithms Forest_ section, and highlight the following:

* Tree-based algorithms are part of the supervised machine learning methods.

* These kind of algorithms can be used to solve classification or regression problems.

* These algorithms are quite often used in finance for assessing risk, preventing fraud, or fighting money laundering.

* In contrast to linear models, tree-based algorithms can map non-linear relationships in data.

Explain to students that in linear models, the relationship among input variables can be represented as a straight line, while non-linear models have a different shape.

* Predicting the price of a house based on its size is an example of a linear problem. This is because, as a general rule, the size of the house is directly proportional to the price of the house.

* Predicting if a credit application is going to be fraudulent or not may be an example of a non-linear problem due to the complex relationship between the input features and the output prediction.

Explain that a linear model fit to non-linear data would only be a good approximation of points near the line and a bad approximation for points that vary from the line.

Explain to students that the most used tree-based algorithms are: decision trees, random forests, and gradient boosting trees.

* `sklearn` has two modules that implement tree-based algorithms that we will be covering Today.

  * [`sklearn.tree`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree) implements decision trees.

  * [`sklearn.ensemble`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble) offers implementations for random forest, gradient boosting, boosting and bagging algorithms.

Answer any questions before moving on.

---

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

Close the presentation explain to students that in this demo, you are going to use the loan applications encoded dataset presented before. The goal of this demo is to predict fraudulent loan applications using a decision tree.

Open the unsolved version of the Jupyter notebook to live code the demo and highlight the following:

* In the initial imports cell, the `tree` module from `sklearn` is imported since it offers a decision tree implementation for classifications problems.

  ```python
  from sklearn import tree
  ```

* One interesting way to analyze a decision tree is to visualize it. The following libraries are imported to create a visual representation of the decision tree.

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

Explain to students that in order to train and validate the decision tree model, the data is split in training and testing sets.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
```

Explain to students that in order to improve an algorithm's performance, the features data will be scaled using the 'StandardScaler`. There is no need to scale the target data since it contains the labels that we want to predict using the decision tree.

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

Explain that we can use the confusion matrix, the `accuracy_score`, and the `classification_report` from `sklearn.metrics` to evaluate the model.

* In this particular example, the confusion matrix is created using the `y_test` and the `results` vectors. The matrix shows how well the model predicts fraudulent loan applications.

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

* After observing the results, it can be seen that model's accuracy (`0.584`) is low. Also, precision and recall are not good enough to state that the model will be good predicting fraudulent loan applications.

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

---

### 7. Students Do: Predicting Fraudulent Loans Applications (10 min)

In this activity, students will create a decision tree model to predict fraudulent loan applications.

**Instructions:**

* [README.md](Activities/04-Stu_Predicting_Fraud/README.md)

**Files:**

* [preventing-fraud.ipynb](Activities/04-Stu_Predicting_Fraud/Unsolved/preventing-fraud.ipynb)

* [sba_loans_encoded.csv](Activities/04-Stu_Predicting_Fraud/Resources/sba_loans_encoded.csv)

---

### 8. Instructor Do: Review Predicting Fraudulent Loans Applications (10 min)

**Files:**

* [preventing-fraud.ipynb](Activities/04-Stu_Predicting_Fraud/Solved/preventing-fraud.ipynb)

Open the solution, and live code the review by highlighting the following:

* The `tree` module from `sklearn` should be imported to create a decision tree model instance.

  ```python
  from sklearn import tree
  ```

* In order to create the decision tree graph, the following libraries are imported.

  ```python
  import pydotplus
  from IPython.display import Image
  ```

* The data from the `sba_loans_encoded.csv` file is loaded in a pandas DataFrame called `df_loans`.

  ```python
  file_path = Path("../Resources/sba_loans_encoded.csv")
  df_loans = pd.read_csv(file_path)
  ```

* After loading the data, the features and target sets are defined.

  ```python
  # Define features set
  X = df_loans.copy()
  X.drop("Default", axis=1, inplace=True)

  # Define target vector
  y = df_loans["Default"].values.reshape(-1, 1)
  ```

* The data is split into training and testing set using the `train_test_split` method from `sklearn`.

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

Recall to students that the target data is not scaled since it contains the classes that you want to predict with the decision tree.

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

* The confusion matrix, accuracy score, and classification report is used ot evaluate the model.

  ![Model's evaluation results](Images/preventing_fraud_review_1.png)

Explain to students that despite model's high accuracy, this model is not predicting all the fraudulent loan applications as can be seen from the precision and recall values. This is why it is important to include the classification report when evaluating a classification model.

Continue live coding the review by creating the model graph using the `pydotplus` library and highlight the following.

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

* The tree is to deep. However, it can be observed that only one subtree grows.

* This phenomenon occurs when the target classes are imbalanced.

* Having imbalanced target classes is a common problem in classification machine learning algorithms when there are a disproportionate ratio of observations in each class.

Explain to students that they will learn how to deal with imbalanced classes in next class, and that there are other tree algorithms such as ensemble learners that can be better at modeling imbalanced classes.

Answer any questions before moving on.

---

### 9. Instructor Do: Introduction to Ensemble Learning (10 min)

In this activity, students will be introduced to ensemble learning, weak learners, and random forests.

Navigate to the _Introduction to Ensemble Learning_ section of the slides. Highlight the following:

* Address the class and tell them that if they were to take all of the classification models they've used so far and compared them, they'd find that some algorithms performed better than others, as expected.

  * Indicate that even though some of the other algorithms performed worse, they were able to still execute independently and classify labels with decent accuracy.

  * Explain to students that they will come across algorithms that actually fail at learning in an adequate fashion. These algorithms/classifiers are considered **weak learners**.

Communicate that **weak learners** are a consequence of limited data to learn from. This may mean too few features or the data provided doesn't allow for data points to be classified.

* Provide more context around **weak learners** by defining them as algorithms/classifiers that are unable to accurately learn from the data they are being provided. This is why their predictions are only a little better than random chance. The classifiers can make predictions; however, their predictions are not representative of the relationship between inputs and target.

* **Weak learners** are described as being only slightly better than random chance.

Explain to students that **weak learners** are still valuable in machine learning.

* **Weak learners** are valuable because there are models that can combine many weak learners to create a more accurate and robust prediction engine. A single **weak learner** will make inaccurate and imprecise predictions. Combined **weak learners** can perform just as well as any other **strong learner**.

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

* Some of the benefits of the random forest algorithm are:

  * It’s robust against overfitting because all of those weak classifiers are trained on different pieces of the data.

  * It can be used to rank the importance of input variables in a natural way.

  * It can handle thousands of input variables without variable deletion.

  * It´s robust to outliers and non-linear data. Random forest handles outliers by binning them. It's also indifferent to non-linear features.

  * It runs efficiently on large databases.

Answer any questions before moving on.

---

### 10. Instructor Do: Random Forest (10 min)

In this activity, students will learn how to implement a random forest using `sklearn`.

**Files:**

* [random-forest.ipynb](Activities/05-Ins_Random_Forest/Solved/random-forest.ipynb)

* [loans_data_encoded.csv](Activities/05-Ins_Random_Forest/Resources/loans_data_encoded.csv)

Explain to students that in this demo, you are going to use the loan applications encoded dataset presented before. The goal of this demo is to predict fraudulent loan applications using a random forest.

Use the unsolved Jupyter notebook to live code the solution and highlight the following:

* In order to use the random forest implementation from `sklearn`, the `RandomForestClassifier` class from the `ensemble` module should be imported.

  ```python
  from sklearn.ensemble import RandomForestClassifier
  ```

The data is loaded in to a Pandas DataFrame and then scaled and split into training and testing set. Just briefly review this code and continue to live code the random forest implementation by highlighting the following:

* To create the target vector `y` before scaling the data, the `ravel` method is used instead of `reshape` as we did in the decision tree demo.

  ```python
  y = df_loans["bad"].ravel()
  ```

* When the random forest instance is created, there are two important parameters to set:

  ```python
  rf_model = RandomForestClassifier(n_estimators=500, random_state=78)
  ```

  * `n_estimators`: This is the number of random forest to be created by the algorithm, in general, a higher number makes the predictions stronger and more stable, however a very large number can result in higher training time. A good approach is to start low and increase the number if the model performance is not adequate.

    * A [research study](https://doi.org/10.1007/978-3-642-31537-4_13) suggests that a range between `64` and `128` trees in a forest could be used for initial modeling.

  * `random_state`: This parameter defines the seed used by the random number generator. It's important to define a random state when comparing multiple models.

* Once the random forest model is created, it's fitted with the training data.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, some predictions are made using the scaled testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* In oder to evaluate the model, a confusion matrix, the `accuracy_score` and the `classification_report` from `sklearn.metrics` are used.

* The confusion matrix is created using the `y_test` and the `results` vectors. The matrix shows how well the model predict fraudulent loan applications.

  ```python
  # Calculating the confusion matrix
  cm = confusion_matrix(y_test, predictions)
  cm_df = pd.DataFrame(
      cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
  )

  # Calculating the accuracy score
  acc_score = accuracy_score(y_test, predictions)
  ```

  ![Random forest evaluation results](Images/random-forest-1.png)

After observing the results, it can be concluded that this model may not be the best one for preventing fraudulent loan applications. Explain to students that there are several strategies that may improve this model such as:

* Reduce the number of features using PCA.

* Create new features based on new data from the problem domain.

* Increase the number of estimators.

Finally, explain to students that a byproduct of the Random Forest algorithm is a ranking of feature importance (i.e. which features have the most impact on the decision).

* The `RandomForestClassifier` of `sklearn` provides an attribute called `feature_importances_`, where you can see which features were the most significant.

  ![Feature importance](Images/random-forest-2.png)

* In this demo, it can be seen that the `age` of the person and the `month` of the loan application are the more relevant features.

* If we need to drop some features, analyzing feature importance could help to decide which features can be removed.

Answer any questions before moving on.

---

### 11. Students Do: Predicting Fraud with Random Forests (10 min)

In this activity, students are going to explore how the random forest algorithm can be used to identify fraudulent loan applications. Students will use the `sba_loans_encoded.csv` file that they created before to train the model

**Instructions:**

* [README.md](Activities/06-Stu_Random_Forest/README.md)

**Files:**

* [fraud-random-forest.ipynb](Activities/06-Stu_Random_Forest/Unsolved/fraud-random-forest.ipynb)

* [sba_loans_encoded.csv](Activities/06-Stu_Random_Forest/Resources/sba_loans_encoded.csv)

---

### 12. Instructor Do: Review Predicting Fraud with Random Forests (10 min)

**Files:**

* [fraud-random-forest.ipynb](Activities/06-Stu_Random_Forest/Solved/fraud-random-forest.ipynb)

* [sba_loans_encoded.csv](Activities/06-Stu_Random_Forest/Resources/sba_loans_encoded.csv)

Walk through the solution and highlight the following:

* The data used in this activity is the same that students used in the decision tree exercise, so data preprocessing is the same.

* The random forest model instance is created defining `n_estimators = 500` and `random_state = 78`.

Explain to students that defining the `random_state` parameter is important to compare different models.

* The random forest model is trained with the training data.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* Once the model is fitted, it's validated using the testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* The model is evaluated using the confusion matrix, the `accuracy_score` and the `classification_report` from `sklearn`.

  ![Random forest evaluation results](Images/stu-random-forest-1.png)

Explain to students that it can be observed that model´s accuracy is better than the one obtained using decision trees (`0.89`), in combination to the confusion matrix results and the precision and recall values, we could conclude that using random forest is better to predict fraudulent loan applications.

* The features importance is retrieved from the random forest model using the `feature_importances_` attribute, finally the top 10 most important features are displayed.

  ![Top 10 important features](Images/stu-random-forest-2.png)

Finally, ask a couple of students about their insights in the _Analysis Questions_ sections, you can comment the following about each question.

* **Question 1:** Would you trust in this model to deploy a fraud detection solution in a bank?

  * **Sample Answer:** Model's accuracy is better than using decision trees, so if we want to deploy a fraud detection solution for loans in a Bank, we would trust in random forest more than in decision trees.

* **Question 2:** What are your insights about the top 10 most importance features?

  * **Sample Answer:** It seems that the Bank is not relevant for the model, so we can create a new random forest model by only taking these top 10 features. Also, for piloting this model in a business environment, we will only need to fetch new data about these 10 features.

Answer any questions before moving on.

---

### 13. BREAK (15 min)

---

### 14. Instructor Do: Boosting and Bagging (15 min)

Students are given a formal lecture on **boosting**, **bagging**, its benefits, and its application in advanced analytics. Guided questions are provided to promote student engagement and to re-enforce content.

Navigate to the **boosting** and **bagging** section of the slideshow. Highlight the following:

* **Boosting** is both a process and set of algorithms. Boosting is the process of combining a set of **weak learners** into a **strong longer**.

  * **Boosting** algorithms work by taking the predictions of each **weak learner** and aggregating them to produce a more accurate and precise prediction. The goal goal of a boosting algorithm is to combine **weak learners** into **ensemble learners**.

    * For this reason, **boosting algorithms** are considered **meta-algorithms**. Instead of working with and affecting data, **boosting algorithms** work with and affect other algorithms.

  * **Boosting** algorithms use weighted averages (the higher the average the more inaccurate the prediction) to determine what values are misclassified. The algorithm will iterate until there are no weighted predictions.

    * Other algorithms (i.e. **bagging**) create new base learners as older ones prove ineffective.

    ![boosting_flow.jpg](Images/boosting_flow.jpg)

  * **Boosting** algorithms are so powerful and performant that they've been stealing the spotlight at Kaggle machine learning algorithms competitions. **Boosting** algorithms like XGBoost have consistently outperformed other algorithms in competitions, on multiple occasions. XGBoost's success has put **boosting** algorithms in the spotlight.

Highlight to students that **boosting** is not the only way to make a **weak learner** more robust and accurate. Another approach is called **bagging**.

* **Bagging** is another method used to improve the accuracy and robustness of a model.

* Where **boosting** takes multiple algorithms and coordinates them as an ensemble and runs the algorithms in tandem to identify the best prediction, **bagging** focuses on re-sampling data and running with different models on the fly in order to formulate the most accurate and precise prediction.

* Each classifier used in the **bagging** process runs independently of hte others. Once all classifiers are finished predicting, the **bagging** algorithm will aggregate results.

  * Results for a **bagging** algorithm are then aggregated via a voting process. Each classifier will vote for a label, and then the **bagging** algorithm will aggregate votes and classify the label with the most votes as the prediction.

* One of the key differences between **boosting** and **bagging** is that **boosting** algorithms will weigh predictions based off of accuracy, and as long as data points are weighted as inaccurate, **boosting** algorithms will continue to run. Instead of weighing predictions, **bagging** algorithms resample and replace data in order to improve model fitting and accuracy.

  * Summarize the comparison again to help reinforce the differences:

    * Bagging iteratively weighs inaccurate predictions and continue to execute.

    * Boosting iteratively resamples and replaces data in order to train the best model.

    ![bagging_flow.png](Images/bagging_flow.png)

If time remains, engage students with the below questions. If there are no conversations, go round-robin.

* Ask if there's a volunteer who would like to summarize the difference between boosting and bagging algorithms.

  * **Answer** Bagging iteratively weighs inaccurate predictions and continue to execute. Boosting iteratively resamples and replaces data in order to train the best model.

* Ask if another volunteer would like to explain what **boosting** and **bagging** algorithms are used for.

  * **Answer** **Boosting** and **bagging** algorithms are used to improve the accuracy and robustness of **weak learners**. Each class of algorithm converts **weak learners** into **strong learners** through **ensemble learning**.

Ask students if they have any questions before moving on.

---

### 15. Instructor Do: Gradient Boosted Tree (10 min)

The instructor will provide a demonstration on how to use **boosting** in **sklearn** to improve the performance of a decision tree.

**File:** [gradient_boosted_tree.ipynb](Activities/07-Ins_Gradient_Boosted_Tree/Solved/gradient_boosted_tree.ipynb)

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

  * The `n_estimators` parameter configures the number of **weak learners** being used with the **boosting** algorithm. The higher the value of `n_estimators`, the more trees that will be created to train the algorithm. The more trees, the better the performance.

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
        classifier = GradientBoostingClassifier(
          n_estimators=20,
          learning_rate=learning_rate,
          max_features=5,
          max_depth=3,
          random_state=0
          )

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

---

### 16. Students Do: Turbo Boost (10 min)

Students will complete a MSMD activity where they use the **sklearn** `GradientBoostedClassifier` **boosting** algorithm to detect fraudulent loan applications using **ensemble learning**.

**Instructions:**

* [README.md](Activities/08-Stu_Gradient_Boosted_Tree/README.md)

**Files:**

* [boost_of_power.ipynb](Activities/08-Stu_Gradient_Boosted_Tree/Unsolved/boost_of_power.ipynb)

---

### 17. Instructor Do: Turbo Boost Activity Review (10 min)

**Files:**

* [boost_of_power.ipynb](Activities/08-Stu_Gradient_Boosted_Tree/Solved/boost_of_power.ipynb)

Open the solution and explain the following:

* The `GradientBoostedClassifier` model was able to produce incredibly high accuracy scores, higher than some of the algorithms we've seen. What about the `GradientBoostedClassifier` makes it better performance than some other algorithms?

  * **Answer** `GradientBoostClassifier` is an **ensemble learning** algorithm. It pools **weak learners** together and executes them in parallel in order to refit the model as needed. Because it leverages multiple algorithms and runs them in parallel, `GradientBoostClassifier`is a more robust algorithm than average.

    ![gradient_boosting_classifier.png](Images/gradient_boosting_classifier.png)

* Even though the accuracy score was high, the classification report shows the precision and recall for detecting one class was greater than the classification for the other class.

  * Explain that this is because the classes are imbalanced, meaning that the algorithm was able to make predictions for one class better than it was for another, and as a result, the algorithm developed bias.

  * Let students know that they will learn what imbalanced classes are and how to deal with them in the next class.

* What are the three main parameters for the `GradientBoostClassifier` model?

  * **Answer** **n_estimators**, **learning_rate**, and **max_depth**.

    * `n_estimators` determines the number of trees/weak learners to use.

    * `learning_rate` identifies how aggressive the algorithm will learn.

    * `max_depth` dictates the size of each tree.

* Remind students that **boosting** algorithms are supervised learning algorithms and they are built and trained just like any other algorithm. They can perform better than other algorithms because they make iterative predictions using more than one classifier.

Use the rest of the time for students to ask questions. If there are no questions, ask students how they're feeling about decision trees and **boosting** algorithms.

Move onto the next activity.

---

### 18. Instructor Do: The Trees Versus the World (10 min)

In this activity, instructor will conduct a facilitated discussion in the class where students will be able to compare the strengths and weaknesses of decision trees, random forests, and classical classifiers (Logistic Regression, SVM, KNN).

Open the lesson slides, go to _The Trees Vs. The World_ section and start the discussion by asking the class the following question:

* Why do you think is worth to learn about classification algorithms?

Ask a couple of students to answer the question, provide your feedback by continuing with the first slide of the section and mentioning that classification algorithms are a matter worth of study since classification is a multidisciplinary challenge.

* **Finance and Banking:** Fraud detection, money laundry, credit risk assessment.

* **Retail and Marketing:** customized products offers, products recommendation, direct marketing optimization.

* **Politics:** Vote intention, party affinity.

* **Health:** Trials tests, ills diagnosis.

* **Security:** Intruders detection, predictive maintenance.

* **Education:** Programs affinity, customized curricula, desertion prevention.

Follow the discussion by asking students the next question:

* Are tree-based algorithms the strongest for classification?

Ask for one volunteer to answer the question, after listening to student's answer, comment to students some the the strengths of tree-based algorithms:

* Are easy to represent, making a complex model much easier to interpret.

* Can be used for any type of data: Numerical (e.g. loan’s amount) or categorical (e.g. bank’s name that issues a
loan).
* Require little data preparation.

* Can handle data that are not normally distributed.

* Can avoid overfitting.

Continue the presentation by showing to students, some of the cases when classical classifiers perform better than tree-based algorithms:

* Generally speaking, classical classifiers may be faster.

* Logistic regression may outperform Decision trees or random forests  having a large number of features with with low noise.

* SVM also support linear and non-linear models.

* SVM handles outliers better.

* KNN naturally supports incremental learning (data streams).

Close the discussion by asking this final question:

* Which algorithm should I use for classification?

Ask for one or two students to voluntary answer the question, and conclude by highlighting the following:

* There is no a definitive answer to this question, the best answers is _it depends_.

* The best algorithm for a classification problem will be determined by different factors such as:

  * Type of data (categorical, numerical, a combination of both).

  * Target classes distribution (balanced or imbalanced).

  * Number of features (input variables).

  * Data normality.

  * Data linearity.

  * Dataset size (number of records or samples)

Congratulate students on learning about a new family of machine learning algorithms, answer any questions before ending the class.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
