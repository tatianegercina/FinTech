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

Comment to students, that you will use simulated data about loans, there are a total of 500 records in the dataset, where each row represents a loan application along an arbitrary year. Every column represents the following data about each loan application.

* `amount`: The loan amount in USD.
* `term`: The loan term in months.
* `month`: The month of the year when the loan was requested.
* `age`: Age of the loan applicant.
* `education`: Educational level of the loan applicant.
* `gender`: Gender of the loan applicant.
* `bad`: Stands for a bad or good loan applicant (`1` - bad, `0` - good).

Continue the demo by loading the dataset on the `loans_df` DataFrame, and highlight the following:

* The dataset has three text features: `month`, `education` and `gender`.

    ![Original loans dataset](Images/categorical-data-1.png)

* In order to use this dataset to train a machine learning model, these three features need to be converted to numerical values.

* There are different methods to deal with text and categorical data, one of the simplest is _integer encoding_, where every different text value or label is represented as an integer.

* The `preprocessing` library of `sklearn`, contains some functions to encode text labels.

* The `LabelEncoder` function, encodes text labels with integer values between `0` and the total number of classes minus `1`.

* To start using the `LabelEncoder` method, first an instance should be created.

    ```python
    label_encoder = LabelEncoder()
    ```

* Once the `LabelEncoder` instance is created, it should be trained (fitted) with the text data you want to encode. The first example shows how the `LabelEncoder` can be fitted with one column of a DatFrame.

    ```python
    label_encoder.fit(loans_df["month"])
    ```

* After fitting the `LabelEncoder`, the classes identified can be retrieved from the `classes_` attribute.

    ![Label Encoder classes](Images/categorical-data-2.png)

* To encode the text labels as integer numbers, the `transform` method is used to create a new column in the DataFrame with the `month` column values encoded as numbers.

    ```python
    loans_df["month_le"] = label_encoder.transform(loans_df["month"])
    ```

Show the DataFrame's head, comment students that, despite the `LabelEncoder` do the job of transforming text labels to numerical values, there is a contextual issue in this particular case: the number assigned to some months doesn't match with the actual month number (e.g. `july` is encoded as `5`)

![Months' names encoded as numbers with Label Encoder](Images/categorical-data-3.png)

* Despite this encoding is technically correct, it can lead to misconceptions while doing further data analysis.

* The `LabelEncoder` is a great tool, but in some particular cases, a manual integer encoding could be made.

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

    ![Meaninful encoded months' names](Images/categorical-data-4.png)

* The `month` and `month_le` columns are dropped since they won't be used anymore.

    ```python
    loans_df.drop(["month", "month_le"], axis=1, inplace=True)
    ```

Comment to students, that sometimes there is problem with this type of encoding, since there are different numbers in the same column, the machine learning model can misunderstand the data to be in some kind of order, for example, since `0 < 1 < 2`; the model may derive a correlation like as the `month_num` increases the `amount`, `term` or `age` increase, but this's clearly not the correct scenario.

* Whether to use `LabelEncoder` or not, will depend on the machine learning performance metrics.

* One way to overcome this issue related to `LabelEncoder`, is to use a binaty encoding method.

* The `get_dummies` method from Pandas, offers a practical solution to encode categorial or text data as binary encoded data.

* The `get_dummies` transforms each categorical feature into new columns with a `1` (True) or `0` (False) encoding to represent if that categorical label was present or not in the original row.

* As a first example, the `gender` column is encoded.

  ![gender column binary encoded](Images/categorical-data-5.png)

* It's also possible to encode multiple columns using `get_dummies`.

  ```python
  loans_binary_encoded = pd.get_dummies(loans_df, columns=["education", "gender"])
  ```

* Once the categorical data is encoded, the resulting DataFrame is saved as a `CSV` file for further usage.

  ```python
  loans_binary_encoded = pd.get_dummies(loans_df, columns=["education", "gender"])
  ```

Tell students, that the final step we need to perform is scaling and normalization. Many machine learning algorithms will perform better with a normalized or scaled dataset.

* `sklearn` provides a variety of scaling and normalization options. The most common is `StandardScaler`.

* `StandardScales` standardizes the features by removing the mean and scaling to unit variance.

* `StandardScaler` can be used when you don't know anything about your data.

* To use `StandarScaler` the `model -> fit-> predict/transform` workflow is also used.

  ```python
  # Creating the scaler instance
  data_scaler = StandardScaler()

  # Fitting the scaler with the encoded data
  data_scaler.fit(loans_binary_encoded)

  loans_data_scaled = data_scaler.transform(loans_binary_encoded)
  ```

* The resulting data, is ready to be used on a machine learning model.

  ![Scaled data](Images/categorical-data-6.png)

Answer any questions before moving on.
