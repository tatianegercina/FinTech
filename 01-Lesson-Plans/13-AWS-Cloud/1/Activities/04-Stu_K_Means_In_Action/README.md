# Clustering Customers for E-Commerce

Once you have prepared the data, it's time to start looking for patterns that could lead you to define customer clusters. After talking with the CFO of the company about the next-quarter goals, you figured out that one way to understand customers, from the available data, is to cluster them according to their spending capacity. However, you have to find how many groups you can define.

You decide to use your new unsupervised learning skills and put k-means in action!

## Instructions

Accomplish the following tasks and use k-means to cluster the customer data.

1. Load the data you already cleaned into a DataFrame and call it `df_shopping`.

2. Find the best number of clusters using the elbow curve.

3. Create a function called `get_clusters(k, data)` that finds the `k` clusters using k-means on `data`. The function should return a DataFrame copy of `Data` that should include a new column containing the clusters found.

4. Use the `get_clusters()` function with the two best values for `k` according to your personal opinion; plot the resulting clusters as follows and postulate your conclusions:

    * Create a 2-D scatter plot using `hvPlot` to analyze the clusters using `x="Annual Income"` and `y="Spending Score (1-100)"`.

    * Create a 3-D scatter plot using Plotly Express to analyze the clusters using `x="Age"`, `y="Spending Score (1-100)"`, and `z="Annual Income"`.

      ---

      © 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
