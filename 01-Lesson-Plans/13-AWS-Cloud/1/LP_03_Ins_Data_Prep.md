### 3. Instructor Do: Data Preparation for Unsupervised Learning (10 mins)

In this activity, students will learn about the data preparation considerations they should take into account before start working with unsupervised learning algorithms.

**Files:**

* [01_Ins_Data_Preparation.ipynb](Activities/01-Ins_Data_Prep/Solved/01_Ins_Data_Preparation.ipynb)

* [iris.csv](Activities/01-Ins_Data_Prep/Resources/iris.csv)

* [new_iris_data.csv](Activities/01-Ins_Data_Prep/Resources/new_iris_data.csv)

Before start playing with unsupervised learning algorithms, explain to students that data preparation for unsupervised learning doesn't differ to much from the process followed for supervised learning problems.

Comment to the class that, as they already done in past lessons, they should consider the following data preparation tasks:

1. **Data Selection:** Make a good choice of what data are going to be used. It's important to consider what data is available, what data is missing and what data can be removed.
2. **Data Preprocessing:** Organize the selected data by formatting, cleaning and sampling it.
3. **Data Transformation:** Transform the data to a format that eases its treatment and storage for future use (e.g. CSV file, spreadsheet, database).

Highlight to students, that the main difference on preparing data for unsupervised learning is that its algorithms don't have any target variable, they only have input features that will be used to find patterns on the data. So, they should take care on selecting features that could help to find those patterns or create groups.

Open the unsolved version of the Jupyter notebook, live code the demo and highlight the following:

* To get started with unsupervised learning, [the iris dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) will be used. So, the data preparation workflow will use this data.

* The data preparation workflow is quite similar as the one students have been following in the past, once the data is selected, the next step is to load the data into a pandas DataFrame.

  ![Lading the iris dataset](Images/reading-iris-data.png)

* In forthcoming activities, the `class` of the iris plants will be found using unsupervised learning, so the next step is to remove the `class` column since it is not necessary.

  ![Removing the class column](Images/removing-class-column.png)

Comment to students that, since all the variables on the dataset are numerical, there are no additional data preprocessing tasks to do. However, data transformations have to be done when there are categorical data or non-numeric features on the dataset. For example, transforming `male` and `female` categorical values to `0` and `1` respectively.

* Finally, the preprocessed DataFrame is saved on a new `CSV` file for further use.

  ```python
  file_path = Path("../Resources/new_iris_data.csv")
  new_iris_df.to_csv(file_path, index=False)
  ```

Ask the class if there are any further questions before moving on the next activity.
