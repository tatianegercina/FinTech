## 8. Instructor Review: Oversampling

**Files:**

[more_loans.ipynb](Activities/04-Stu_Do_More_Loans/Solved/more_loans.ipynb)

Since this activity is almost an exact replica of the oversampling demonstration, you can likely go through this review quickly. 

* First, we need to identify the variable that we are trying to predict, which is whether a person defaults on their credit card loan in the next month - this variable is default_next_month. We create the dependent and independent variables in the following code:

```python
x_cols = [i for i in df.columns if i != 'default_next_month']
X = df[x_cols]
y = df['default_next_month']
```

* Again, we split the data into train and test sets *before* doing oversampling. This is so that we maintain a purely observed test set.

* After running the oversampling and logistic regression functions, these are the evaluation metrics we receive:

Random Oversampling

![stovers_1](Images/stovers_1.PNG)

SMOTE Oversampling

![stovers_2](Images/stovers_2.PNG)

Ask students how they interpreted the evaluation metrics. What are some reasons why the evaluation metrics using both oversampling methods might both be relatively low?

* SMOTE is not guaranteed to outperform random oversampling in all applications. The threat of overfitting due to repeated samples with random oversampling is not as great when the imbalance in classes is not as extreme, as is the case in this data set. Moreover, the fact that SMOTE samples are mostly artificial can actually decrease model performance if the generated data does not have the same structure as the observed data does. 