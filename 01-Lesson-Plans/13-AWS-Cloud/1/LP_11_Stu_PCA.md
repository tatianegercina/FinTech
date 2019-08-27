### 11. Students Do: PCA in Action (20 min)

In this activity, students will use PCA to reduce the dimensions of the consumers shopping dataset.

**Instructions:**

* [README.md](Activities/06-Stu_PCA/README.md)

**Files:**

* [06_Stu_PCA.ipynb](Activities/06-Stu_PCA/Unsolved/06_Stu_PCA.ipynb)

---

### 12. Instructor Do: Review PCA in Action (10 min)

**Files:**

* [06_Stu_PCA.ipynb](Activities/06-Stu_PCA/Solved/06_Stu_PCA.ipynb)

Walk through the solution and highlight the following:

* After using PCA, the features' values on the `df_shopping` DataFrame are standardized using the `StandardScaler` library from `sklearn`.

  ```python
  shopping_scaled = StandardScaler().fit_transform(df_shopping)
  ```

* PCA is initially used, by reducing the number of features from `4` to `2`.

  ```python
  # Initialize PCA model
  pca = PCA(n_components=2)

  # Get two principal components for the iris data.
  shopping_pca = pca.fit_transform(shopping_scaled)
  ```

Comment to students that, after fetching the explained variance, the first principal component contains `33.7%` of the variance and the second principal component contains `26.2%` of the variance; since we have `59.9%` of the information in the original dataset, it's worth to explore increasing the number of principal components up to three to verify if this ratio improves.

![Explained variance with two PCs](Images/explained-variance-2pcs.png)

* After PCA is applied defining three principal components, the explained variance value improves. The `83.1%` of the information in the original dataset is preserved, so we can conclude that using three principal components is a better approach to reduce the dimensions in this case.

  ![Explained variance with three PCs](Images/explained-variance-3pcs.png)

* The K-Means algorithm is fitted with the principal components data to predict the clusters. A value of `k=6` is used, since this was the best value in the previous exercise using the Elbow Curve.

  ```python
  # Initialize the K-Means model
  model = KMeans(n_clusters=6, random_state=0)

  # Fit the model
  model.fit(df_shopping_pca)

  # Predict clusters
  predictions = model.predict(df_shopping_pca)

  # Add the predicted class columns
  df_shopping_pca["class"] = model.labels_
  ```

* Since we decided that three principal components were the best approach, a 3D-Scatter plot is created with Plotly Express to visually represent the clusters.

  ![Clusters plot](Images/pca-data-plot.png)

Explain students that, the power of PCA to speed-up machine learning algorithms, is more noticeable when you are dealing with a dataset that has tens or hundreds of features, for datasets up to ten features, PCA adds value to simplify data analysis and visualization.

Answer any questions before moving on.
