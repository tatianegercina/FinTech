### 2. Instructor Do: Dealing with Text and Categorical Data in Machine Learning (10 mins)

In this activity, students will learn how categorical data should be preprocessed to be used in machine learning algorithms.

**Files:**

* [categorical-data.ipynb](Activities/01_Ins-Categorical-Data/Solved/categorical-data.ipynb)

Recall to students, that machine learning algorithms work with numerical data, however datasets also have text and categorical data such as gender, education level or marital status, that could represent a valuable input variable for a machine learning algorithms.

Explain to students, that in order to use text or categorical data in a machine learning algorithm, these kind of data values should be converted to a numerical representations.

Tell students that, we will use `pandas` and the `preprocessing` library of `sklearn` to encode text and categorical data as numbers.

Open the unsolved version of the Jupyter notebook and highlight the following:

* On the _initial imports_ cell, two functions from the `preprocessing` library of `sklearn` are imported.

  ```python
  from sklearn.preprocessing import LabelEncoder, StandardScaler
  ```

* [The `LabelEncoder` function](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) performs integer encoding of labels.

* [The `StandardScaler` function](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) will be used to standardize numerical features.
