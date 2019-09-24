# Students Do: Understanding customers

One of the top online stores in Europe just hired you, they want to increase their revenue by offering custom offers to customers. Before start looking for any machine learning algorithm, you ask the company for historic data about customers purchases. After checking the dataset, you realized that there are some data preprocessing work to be done.

## Instructions

You are given a dataset that contains historical data from purchases of a online store made by 200 customers, in this activity you will put in action your data preprocessing superpowers, also you'll add some new skills needed to start finding customers clusters.

Use the stater Jupyter notebook and perform the following tasks:

* Load the data on a Pandas DataFrame, name it as `df_shopping` and fetch the top 10 rows.

* List DataFrame's data types to ensure they're aligned to the type of data stored on each column. Is there any column whose data type need to be changed? If so, make the corresponding adjustments.

* Another best practice is to drop any column that would be unnecessary, is there any unnecessary column that is needed to be dropped? If so, make the corresponding adjustments.

* Remove all rows with `null` values if any.

* Remove duplicate entries if any.

In order to use unsupervised learning algorithms, all the features should be numeric, and also, on similar scales. Perform the following data transformations.

* The `Genre` column contains categorical data, anytime you have categorical variables, you should transform them to a numerical value, in this case, transforming `Male` to `1` and `Female` to `0` is a feasible solution.

* The `Annual Income` column is on a different scale than the other columns, it is needed to have a similar scale on all the variables in order to use unsupervised learning algorithms, so `Annual Income` should be rescaled. In this case, dividing by `1000` is the simplest approach.

Once you are done with data preprocessing, save the cleaned DataFrame on a new `CSV` file as `shopping_data_cleaned.csv`.
