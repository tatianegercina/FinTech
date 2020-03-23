# Students Do: Understanding Customers

One of the top online stores in Europe just hired you, they want to increase their revenue by offering custom offers to customers. Before you start looking for any machine learning algorithm, you ask the company for historical data about customer purchases. After checking the dataset, you realized that there is some data preprocessing work to be done.

## Instructions

You are given a dataset that contains historical data from purchases at an online store made by 200 customers. In this activity, you will put in action your data-preprocessing superpowers. Also, you'll add some new skills needed to start finding customers clusters.

Use the starter Jupyter Notebook and perform the following tasks:

* Load the data into Pandas DataFrame, name it as `df_shopping`, and fetch the top 10 rows.

* List the DataFrame's data types to ensure that they're aligned to the type of data stored in each column. Are there any columns whose data type needs to be changed? If so, make the corresponding adjustments.

* Another best practice is to drop any column that would be unnecessary. Are there any unnecessary columns that needs to be dropped? If so, make the corresponding adjustments.

* Remove all rows with `null` values, if any.

* Remove duplicate entries if any.

To use unsupervised learning algorithms, all the features should be numeric and on similar scales. Perform the following data transformations:

* The `Gender` column contains categorical data; anytime you have categorical variables, you should transform them to a numerical value. In this case, transforming `Male` to `1` and `Female` to `0` is a feasible solution.

* The `Annual Income` column is on a different scale than the other columns. It is necessary to have a similar scale on all the variables to use unsupervised learning algorithms, so `Annual Income` should be rescaled. In this case, dividing by `1000` is the simplest approach.

Once you are done with data preprocessing, save the cleaned DataFrame in a new `CSV` file as `shopping_data_cleaned.csv`.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
