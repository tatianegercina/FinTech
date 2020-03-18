# PCA in Action

In this activity, you will use PCA to reduce the dimensions of the consumers shopping dataset from `4` to `2` features. After applying PCA, you will use the principal components data to fit a k-means model with `k=6` and make some conclusions.

## Instructions

1. Import the preprocessed data from the consumers shopping dataset into a DataFrame called `df_shopping`.

2. Standardize the data of all the DataFrame features.

3. Apply PCA to reduce dimensions from 4 to 2 and create a DataFrame with the principal components data.

4. Fetch the explained variance, analyze its value, and answer the following question: Are two principal components the best number of new dimensions?

5. If you conclude that two principal components is the appropriate number of new dimensions, proceed to step 6. Or explore what happens if you modify the number of principal components. Once you finish, write your conclusions.

6. Fit the k-means algorithm with `k=6` and the principal components data.

7. Plot the resulting clusters, use the appropriate scatter plot depending on the number of dimensions you have.

   ---

   © 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
