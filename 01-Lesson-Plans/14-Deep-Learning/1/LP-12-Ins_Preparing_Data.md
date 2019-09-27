### 12. Instructor Do: Preparing Data for Neural Networks (15 min)

In this section we will go over some necessary transformations of data before it can be fed into a neural network. 

**Files**

[04-Ins/preparing_data.ipynb](Activities/04-Ins_Preparing_Data/Solved/preparing_data.ipynb)

Open the solved notebook and ask students to follow along as your demonstrate one-hot encoding and model scaling. 

* Like any machine learning model, neural nets require some preprocessing of data in order to be used effectively. Neural nets cannot deal with categorical variables in their raw forms, and explanatory variables that are represented in different units or have vastly different scales of magnitude can make models difficult to train. To solve the first problem, we apply one-hot encoding to categorical values in order to transform them into binary variables. To deal with the second, we apply standardization.

* One hot encoding involves taking a categorical variable, such as color with labels "red," "white," and "blue," and creating three new variables of the colors, with each instance of the data now showing a 1 if it corresponds to that color and 0 if it does not. 

* With scikit learn, one hot encoding actually involves two steps. First, we label encode the column (in this case, "target") and turn it into a series of numerical values based on the categorical values they correspond to. Then, we use the one hot encoder function to split the series into columns of variables, each corresponding to a category. 

```python
# Label encode
label_encoder = LabelEncoder()
label_encoder.fit(data.target)
encoded_target = label_encoder.transform(data.target)

# One hot encode the categorical variable
encoded_target = encoded_target.reshape(len(encoded_target), 1)
enc = OneHotEncoder()
target_ohe = enc.fit_transform(encoded_target).toarray()
target_ohe = pd.DataFrame(target_ohe, columns = ['setosa', 'versicolor', 'virginica'])
```

* The before and after representation of the data looks like this:

![onehot_1.png](Images/onehot_1.png)


![onehot_2.png](Images/onehot_2.png)


Ask a student to restate what we've accomplished with one hot encoding. 
**Answer**: We've transformed one categorical variable into many binary (numerical) variables, each corresponding to a category. 

* Now we want to standardize the other variables in the data. This involves de-meaning the variables - that is, make it so that each numerical variable has a mean of 0 - and a constance variance of 1. This makes it so that the variables all have approximately the same size, and reduces the likelihood that outliers or variables in different units will negatively affect model performance. 

* Scikit learn offers an easy way to standardize variables:

```python
scaler = StandardScaler().fit(data_to_scale)
scaled_data = scaler.transform(data_to_scale)
```

The before and after data looks like this:

![scaler_1.png](Images/scale_1.png)


![scaler_2.png](Images/scale_2.png)

Ask students if they have any questions before moving on to the final activity of the day. 