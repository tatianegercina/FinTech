# Unit 11 - Risky Business

![Credit Risk](Images/credit-risk.jpg)

## Background

Auto loans, mortgages, student loans, debt consolidation... these are just a few examples of credit and loans that people are seeking online. Peer-to-peer lending services such as Lending Club or Prosper allow investors to loan other people money without the use of a Bank. However, investors always want to mitigate risk, so you have been asked by a client to help them use machine learning techniques to predict credit risk.

In this assignment, you will build and evaluate several machine learning models to predict credit risk using free data from Lending Club. Credit risk is an inherently imbalanced classification problem (the number of good loans is much larger than the number of at-risk loans), so you will need to employ different techniques for training and evaluating models with imbalanced classes. You will use the imbalanced-learn and scikit-learn libraries to build and evaluate models using the two following techniques:

1. [Resampling](#Resampling)
2. [Ensemble Learning](#Ensemble-Learning)

- - -

### Files

[Starter Notebook](Starter_Code/credit-risk.ipynb)

- - -

### Instructions

#### Resampling

You will use the [imbalanced-learn](https://imbalanced-learn.readthedocs.io) library to resample the Lending Club data and build and evaluate logistic regression classifiers using the resampled data.

You will:

1. Oversample the data using the `Naive Random Oversampler` and `SMOTE` algorithms.
2. Undersample the data using the `Cluster Centroids` algorithm.
3. Over- and Under-sample using a combination `SMOTEENN` algorithm.

For each of the above, you will need to:

1. Train a `logistic regression classifier` from `sklearn.linear_model` using the resampled data.
2. Calculate the `balanced accuracy score` from `sklearn.metrics`.
3. Calculate the `confusion matrix` from `sklearn.metrics`.
4. Print the `imbalanced classification report` from `imblearn.metrics`.

Use the above to answer the following:

> Which model had the best balanced accuracy score?
>
> Which model had the best recall score?
>
> Which model had the best geometric mean score?

#### Ensemble Learning

In this section, you will train and compare two different ensemble classifiers to predict loan risk and evaluate each model. You will use the `Balanced Random Forest Classifier` and the `Easy Ensemble AdaBoost Classifier`.

Be sure to complete the following steps for each model:

1. Train the model using the latest quarterly data from Lending Club.
2. Calculate the balanced accuracy score from `sklearn.metrics`.
3. Print the confusion matrix from `sklearn.metrics`.
4. Generate a classification report using the `imbalanced_classification_report` from imbalanced-learn.
5. For the Balanced Random Forest Classifier only, print the feature importance sorted in descending order (most important feature to least important) along with the feature score

Use the above to answer the following:

> Which model had the best balanced accuracy score?
>
> Which model had the best recall score?
>
> Which model had the best geometric mean score?
>
> What are the top 3 features?

- - -

### Resources

[2019 Q1 Loan Data](https://www.lendingclub.com/info/download-data.action)

- - -

### Hints and Considerations

Select the latest quarterly data from the Lending Club data. Keep the file in the zipped format and use the starter code to read the file.

Refer to the [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/) and [scikit-learn](https://scikit-learn.org/stable/) official documentation for help with training the models. Remember that these models all use the model->fit->predict API.

For the ensemble learners, use 100 estimators for both models.

- - -

### Submission

* Create Jupyter Notebooks for the homework and host the notebooks on Github.

* Include a Markdown that summarizes your homework and include this report in your Github repository.

* Submit the link to your Github project to Bootcampspot.
