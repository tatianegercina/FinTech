# PCA in Action

In this activity, you will use PCA to reduce the dimensions of the consumers shopping dataset from `4` to `2` features. After applying PCA, you will use the principal components data to fit a k-means means model with `k=6` and make some conclusions.

## Instructions

1. Load the `shopping_data_cleaned.csv` data file that you created before in Amazon SageMaker Studio into a folder called `Data`.

2. In the root folder of Amazon SageMaker Studio, load the starter Jupyter notebook `Stu_PCA.ipynb`.

3. Open the started Jupyter notebook in Amazon SageMaker Studio and select the `Python 3 (Data Science)` kernel.

4. Import the preprocessed data from the consumers shopping dataset into a DataFrame called `df_shopping`.

5. Standardize the data of all the DataFrame features using the `StandardScaler` from `sklearn`.

6. Apply PCA to reduce dimensions from `4` to `2` features and create a DataFrame with the principal components data. Remember to set `random_state=0` for model reproducibility.

7. Fetch the explained variance, analyze its value and answer the following question: How much information from the original dataset is explained by the principal components?

8. Fit the k-means algorithm with `k=6` and the principal components' data.

9. Plot the resulting clusters using the two principal components.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
