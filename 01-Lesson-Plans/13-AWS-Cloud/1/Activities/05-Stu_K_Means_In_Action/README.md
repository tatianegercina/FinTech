# Clustering Customers for E-Commerce

Once you have prepared the data, it's time to start looking for patterns that could lead you to define customer clusters. After talking with the CFO of the company about the next-quarter goals, you figured out that one way to understand customers, from the available data, is to cluster them according their spending capacity. However, you have to find how many groups you can define.

You decide to use your new unsupervised learning skills and put k-means in action!

## Instructions

Accomplish the following tasks and use k-means to cluster the customer data.

1. Load the `shopping_data_cleaned.csv` data file that you created before in Amazon SageMaker Studio into a folder called `Data`.

2. In the root folder of Amazon SageMaker Studio, load the starter Jupyter notebook `k_means_in_action.ipynb`.

3. Open the started Jupyter notebook in Amazon SageMaker Studio and select the `Python 3 (Data Science)` kernel.

4. Load the data on a DataFrame and call it `df_shopping`.

5. Find the best number of clusters using the elbow curve.

6. Create a function called `get_clusters(k, data)` that finds the `k` clusters using k-means on `data`. The function should return a DataFrame copy of `Data` that should include a new column containing the clusters found.

7. Use the `get_clusters()` function with the two best values for `k` according to your personal opinion; plot the resulting clusters using `x="Annual Income"` and `y="Spending Score (1-100)"`.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
