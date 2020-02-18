## FAQs

## Unit 11: Classification

<details>
<summary>What is the difference between linear regression and logistic regression?</summary>

Though both use regression techniques, linear and logistic regressions are both quite different.  If the values you are predicting are continuous meaning they can be any number, then linear regression is the correct model.  If your values are categorical or binary, then logistic regression is the correct model.
</details>

<details>
<summary>What is the difference between continuous and categorical data?</summary>
Continous data is quantitative data that can be any number with infinte possibilities.
Categorical data is data that can be classified in specific groups.

Examples of categorical data inclue:
- Male, Female
- Yes, No
- Positve, Negative
- Good, Bad, Neutral
- Snickers, Milky Way, Twix
- Soccer, Hockey, Baseball, Basketball, Lacrosse

</details>

<details>
<summary>
Why am I getting a value error for my continuous data?</summary>

Are you running a Logistic Regression model and keep getting an error like the one below?

![continuous_err](Resources/continuous_err.PNG)

This error means you are giving non-categorical data to your Logistic Regression model.  Logistic Regression models use categorical data, and cannot compute continuous data.

</details>


<details>
<summary>
 How do you preprocess data for classification?</summary>
Most categorical data is text based and must be converted to numerical so that computations can be ran.  For example ir your categories are male and female, you could convert them to 0 and 1.  scikit-learn offers functions that can handle this conversion simply.  Two options are `.LabelEncoder()` and `OneHotEncoder()`.

<blockquote>
<details>
<summary>Preprocessing Target Data</summary>

Using the .`Labelencoder()` method from scikit-learn we can convert categorical data to numberical.  We begin with a simple DataFrame showing 6 countries:

![country_df1](Resources/country_df1.PNG)

Then we import `LabelEncoder` from sklern.preprocessing, after which we instantiate the `.LabelEncoder()` object, run a `.fit()` then `.transform()`.  The results are stored in a new variable `encoded_y` and inserted into a new DataFrame.

```python
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoder.fit(df.Country)
encoded_y = encoder.transform(df.Country)
df['Encoded'] = encoded_y
```
Now you can see that the encoded values are numerical representations of the original countries:

![country_df2](Resources/country_df2.PNG)

</details>

<details>
<summary>Preprocessing Feature Data</summary>
There are situations when using `.LabelEncoder()` is not appropriate.  If you are encoding target values, (the values you wish to predict), then using the label encoder is great, however if you are encoding feature values, this method can cause accidental bias in your model prediction.  This is because the numerical representations of the data will be interpreted as values by the model.  A category of 5 will be given more weight than a category of 1.  This is where the `.get_dummies()` pandas function used in Unit 10 comes into play.  The function works by splitting the categorical column of data into multiple columns of separate data with a 1 or 0 representation.  In the below example we use the `.get_dummies()` to convert the same country data as before:

```python
encoded_data = pd.get_dummies(df.Country, columns='Country')
```
![country_df3](Resources/country_df3.PNG)
</details>
<details>
<summary>Scaling Feature Data</summary>
In our prevoius example, we converted feature data to binary to avoid introducing bias into the model.  For the same reason, we should scale data that has large numerical variance between features, so that all features are initiall weighted the same.  For example, let's suppose that our country dataframe also includes average number of children, average life expectancy, and average salary by country:

![country_df4](Resources/country_df4.PNG)

These values vary greatly.  If you were using these values in a model, the higher numbers would automatically be read in with more weight bias.  That is where scaling comes in!  Using the `StandardScaler()` from scikit-learn, we will scale the data.  First we instantiate the `.StandardScaler()` instance, then fit it to the data, then transform the data and show in a new DataFrame:

```python
data_scaler = StandardScaler()
data_scaler.fit(df)
data_scaled = data_scaler.transform(df)
```
The new DataFrame shows the scaled data in place of the former values.  Now all the values standardized:


![country_df5](Resources/country_df5.PNG)

</details>
</blockquote>
</details>

<details>
<summary>
 How does `train_test_split()` work?</summary>

The `train_test_split()` function makes splitting data for testing easy!  The function outputs 4 sets of data points - 2 sets of feature data, and 2 sets of target data.  This is why the variables that define the function are typically `X_train, X_test, y_train, y_test`.  The most important parameters of the function are the `X` and `y`.  During preprocessing we separate our data into the feature data, or `X`, and the target data, or `y`.

The `y` data are the values we wish to predict, and the `X` data are the values we use to influence our predictions.  If our data is stored in a DataFrame, we just break it out and store it in variables.  The values we wish to predict are stored as `y` and the features we are using to make our predictions are stored as `X`.  We then feed these into the `train_test_split()` function.

Other parameters include: `stratify`, `test_size`, `train_size`, `random_state`, and `shuffle`.

If the `y` values consists of binary data (for example, male/female), and 25% of those values are male, and 75% of those values are female, then setting the `stratify` parameter to `y` will ensure the test and train data have the same ratio of male to female as the entire data set.

The specific `test_size` and `train_size` can also be set to override the default sizes.  The default for these parameters will select sizes that complement the data set.  The defaults can be overridden using either `int` of `float` values.  If the value set is `int`, then this will indicate a specific sample size you wish to include in the test or train set.  If the value set is `float` then it will indicate a percentage of the total dataset you wish to include in the test or train set.

When using the `shuffle` parameter, the data is shuffled (randomized) prior to being divided into train and test sets.

When using this function the data is split randomly each time, however if the `random_state` parameter is set, the same random split will be selected each time.  To use this paramenter, any number can be used as the `random_state` as long as it is used each time you run the model.  Using this parameter will always ensure the same split is obtained even if `shuffle` is set to `True`.

An example of implementing a `train_test_split()` instance is as follows:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, shuffle = True)
```

</details>

<details>
<summary>
 What is the difference between supervised learning and unsupervised learning?</summary>

 Supervised learning models

</details>
<details>
<summary>
What is the difference between True/False Positives and True/False Negatives?</summary>
Keeping track of the differences between these four guys can be a mind bender.  It often makes more sense when thought of as a medical procedure - the test said you have the flu, but you actually did not would be a False Positive.  But when applying these terms to machine elarning, where the values we are predicting are usually more than just true or false, and are less applicable to our daily lives as medical testing, their meaning can become abstract.  Here is a quick referencd to keeping them straight.  In our example, the model is predicting whether a color will be blue, green or purple.
<blockquote>
<details>
<summary>True Positve</summary>
I thought you were green and I was right!

The model predicted this value as green and it is correct.
</details>
<details>
<summary>False Positive</summary>
I thought you were green and I was wrong!

The model predicted this value as green and it was incorrect.
</details>
<details>
<summary>True Negative</summary>
I thought you were not green and I was right!

The model predicted this value was not green it was correct.

</details>
<details>
<summary>False Negative</summary>
I thought you were not green and I was wrong!

The model predicted this value was not green and it was incorrect.
</details>
</details>

<details>
<summary>
How are precision and accuracy different?</summary>


Precision is a measure of how close elements are to each other.  Accuracy is a measure of how close items are to the target.
<img src='Resources/acc_prec.png' width = 650>
</details>

<details>
<summary>
How do you use a confusion matrix?</summary>

<blockquote>
<details>
<summary>Layout</summary>
The basic layout of a confusion matrix is the actual values are listed along the x axis, and predicted values are listed along on the y axis.

![confusion1](Resources/conf_matrix1.gif)
</details>
<details>
<summary>Precision</summary>
Precision is a measurement of how many positively predicted values were actually correct.  For example, if our model was predicting colors - blue, green and purple, precision would be the measurement of how many times time model predicted purple and the actual value was also purple.

![confusion3](Resources/conf_matrix3.gif)
</details>

<details>
<summary>Recall</summary>
Recall is a measurement of how many times a value was predict and was incorrect.  For example, if our model was predicting colors - blue, green and purple, recall would be the measurement of how many times green was predicted incorrectly.

![confusion2](Resources/conf_matrix2.gif)
</details>
</details>
<details>
<summary>
 What is the difference between logistic regression and support vector machines?</summary>

</details>

<details>
<summary>
What is the difference between decision trees and random forests?</summary>

</details>

<details>
<summary>
What is the point of using ensemble learning?</summary>

</details>

<details>
<summary>
how do I know if my data is imbalanced?</summary>

</details>

<details>
<summary>
How do I managed imabalanced data?</summary>

</details>
