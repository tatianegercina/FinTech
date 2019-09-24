### 13. Students Do: Data Prep (15 min)

In this activity students will one-hot encode and normalize as needed a set of variables that describe imported automobiles.

### Files

[README.md](Activities/05-Stu_Data_Prep_/README.md)

---

### 14. Instructor Do: Review Playing With Neurons (5 min)

Open the solved notebook and guide students through each step.

* First, we label encode the categorical columns and turn them into a series of numerical values based on the categorical values they correspond to. Then, we use the one hot encoder function to split the series into columns of variables, each corresponding to a category of fuel type and body style.  

```python
# Label encode
label_encoder = LabelEncoder()
label_encoder.fit(df.fuel_type)
encoded_fuel = label_encoder.transform(df.fuel_type)

# One hot encode the categorical variable
encoded_fuel = encoded_fuel.reshape(len(encoded_fuel), 1)
enc = OneHotEncoder()
fuel_ohe = enc.fit_transform(encoded_fuel).toarray()
fuel_ohe = pd.DataFrame(fuel_ohe, columns = ['gas','diesel'])

# Label encode
label_encoder = LabelEncoder()
label_encoder.fit(df.body_style)
encoded_body = label_encoder.transform(df.body_style)

# One hot encode the categorical variable
encoded_body = encoded_body.reshape(len(encoded_body), 1)
enc = OneHotEncoder()
body_ohe = enc.fit_transform(encoded_body).toarray()
body_ohe = pd.DataFrame(body_ohe, columns = ['convertible','hatchback','sedan','wagon','hardtop'])
```

* Next, we can standardize all the continuous variables at once with the StandardScaler.

```python
scaler = StandardScaler().fit(data_to_scale)
scaled_data = scaler.transform(data_to_scale)
scaled_vars = pd.DataFrame(scaled_data, columns = df.iloc[:, 2:6].columns)
```

* Before this data can be a neural network's input, it needs to be put back together. 

```python
X = pd.concat([one_hot_encoded_vars,scaled_vars], axis = 1)
```

* The final input data should look like the below:

![prep.png](Images/prep.png)
