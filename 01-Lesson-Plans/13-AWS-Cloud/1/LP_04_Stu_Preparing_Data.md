### 4. Students Do: Preparing data for segmentation (20 mins)

In this activity, students will perform some data preparation tasks on a dataset that contains data from purchases on a e-commerce website made by 200 customers.

There are some data transformations that should be made on the dataset, so ask TAs to assist students and helping them understanding why the following changes are needed.

* **Annual Income:** In order to use K-Means, it is needed to have a similar scale on all the variables, so annual income should be regularized since it’s in a different scale than the other features; dividing by 1000 is the simplest solution.

* **Gender:** The K-Means algorithm only works with numerical data, so anytime you have categorical variables to be included on the clustering logic, it should transform them to any numerical value, in this case, some approach is transforming male to 1 and female to 0.

* **CustomerID:** Since this column is not relevant to the clustering algorithm, it should be dropped from the dataframe.
Students will use this dataset on further activities to find customers segments.


**Instructions:**

* [README.md](Activities/02-Stu_Practice/README.md)

**Files:**

* [starter-code.js](Activities/02-Stu_Practice/Unsolved/starter-code.js)
