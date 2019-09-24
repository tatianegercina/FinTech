# Clustering Customers for e-commerce

Once you have prepared the data, it's time to start looking for patterns that could lead you to define customers clusters. After talking with the CFO of the company about the next quarter goals, you figured out that one way to understand customers, from the available data, is to cluster them according their spending capacity, however you have to find how many groups you can define.

You decide to use your new unsupervised learning skills and put K-Means in action!

## Instructions

Accomplish the following tasks and use K-Means to cluster the customers data.

1. Load the data you already cleaned on a DataFrame and call it `df_shopping`.

2. Find the best number of clusters using the Elbow Curve.

3. Create a function called `get_clusters(k, data)` that finds the `k` clusters using K-Means on `data`. The function should return a DataFrame copy of `Data` that should include a new column containing the clusters found.

4. Use the `get_clusters()` function with the two best values for `k` according to your personal opinion; plot the resulting clusters as follows and postulate your conclusions:

    * Create a 2D-Scatter plot using `hvPlot` to analyze the clusters using `x="Annual Income"` and `y="Spending Score (1-100)"`.

    * Create a 3D-Scatter plot using Plotly Express to analyze the clusters using `x="Age"`, `y="Spending Score (1-100)"` and `z="Annual Income"`.
