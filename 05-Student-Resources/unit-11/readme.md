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
<summary>Preprocessing Target Data:</summary>

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
<summary>Preprocessing Feature Data:</summary>
There are situations when using `.LabelEncoder()` is not appropriate.  If you are encoding target values, (the values you wish to predict), then using the label encoder is great, however if you are encoding feature values, this method can cause accidental bias in your model prediction.  This is because the numerical representations of the data will be interpreted as values by the model.  A category of 5 will be given more weight than a category of 1.  This is where the `.get_dummies()` pandas function used in Unit 10 comes into play.  The function works by splitting the categorical column of data into multiple columns of separate data with a 1 or 0 representation.  In the below example we use the `.get_dummies()` to convert the same country data as before:

```python
encoded_data = pd.get_dummies(df.Country, columns='Country')
```
![country_df3](Resources/country_df3.PNG)
</details>
<details>
<summary>Scaling Feature Data:</summary>
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
 What do the parameters of `train_test_split()` mean?</summary>

</details>

<details>
<summary>
 What is the difference between supervised learning and unsupervised learning?</summary>

</details>

<details>
<summary>
 How do you understand the difference between precision, recall and accuracy?</summary>

</details>

<details>
<summary>
 How do you read a confusion matrix?</summary>

</details>

<details>
<summary>
 What is the difference between logistic regression and support vector machines?</summary>

</details>

<details>
<summary>
 What is `labelencoder()` and why do I have to use it?</summary>

</details>

<details>
<summary>
What is `standardscaler()` and why do I have to use it?</summary>

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
