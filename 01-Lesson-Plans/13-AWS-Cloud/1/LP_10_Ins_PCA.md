### 2. Instructor Do: Speeding up ML algorithms with PCA (10 min)

In this activity, students will learn how to use Principal Component Analysis as a technique to speed-up machine learning algorithms by reducing the number of features.

**Files:**

* [05_Ins_PCA.ipynb](Activities/05-Ins_PCA/Solved/05_Ins_PCA.ipynb)

Explain to students that, Principal Component Analysis (PCA), is a statistical technique to speed up machine learning algorithms when the number of input features (or dimensions) is too high. Comment to students, that PCA reduces the number of dimensions by transforming a large set of variables into a smaller one that contains most of the information in the original large set.

Open the unsolved Jupyter notebook, live code the demo and highlight the following:

* There are two libraries that should be imported from `sklearn` to use PCA: `StandardScaler` and `PCA`.

  ```python
  from sklearn.preprocessing import StandardScaler
  from sklearn.decomposition import PCA
  ```

* The previously preprocessed version of the Iris dataset is used to explain how to apply PCA.

  ![The iris dataset without target class](Images/iris-dataset-no-targets.png)

* There are four features in the Iris dataset with values on different scales, the first step towards using PCA is to standardize the features' values. The `StandardScaler` library is used to do so.

  ![Using StandardScaler](Images/using-standardscaler.png)

* Once the features are standardized, PCA can be used to reduce the number of features in the dataset. First a PCA model should be created specifying the final number of features in the `n_components` parameter. In this demo, the features are reduced from `4` to `2`.

  ```python
  pca = PCA(n_components=2)
  ```

* After creating the PCA model, we apply dimensionality reduction on the scaled dataset.

  ```python
  iris_pca = pca.fit_transform(iris_scaled)
  ```

Tell students, that after dimensionality reduction, we get as a results a smaller set of dimensions called _principal components_, there isn’t a particular meaning assigned to each principal component, the new components are just the two main dimensions of variation that contains most of the information in the original dataset.

* The resulting principal components, are transformed into a DataFrame to be used next to fit the K-Means algorithm. You can see that principal component values has no direct relation with the values in the original dataset, they can be seen as a reduced representation of the original data.

  ![PCA Data](Images/pca-df.png)

Comment to students, that dimensionality reductions implies a lost of accuracy, however the trick is to sacrifice a little accuracy for simplicity. Smaller data sets are easier to explore and visualize, eases data analysis and speed-up machine learning algorithms without extraneous variables to process.

* In order to know how much information can be attributed to each principal component, the explained variances is used.

  ![Explained variance](Images/explained-variance.png)

Explain to students that in this demo, after using the attribute `explained_variance_ratio_`, they can see that the first principal component contains `72.77%` of the variance and the second principal component contains `23.03%` of the variance. Both components contain `95.80%` of the information.

* The Elbow Curve is generated using the principal components data, you can see that the resulting best value for `k` is `3`. Despite some accuracy is lost due to dimensionality reduction, the results are good enough.

  ![PCA Elbow Curve](Images/pca-elbow-curve.png)

* The K-Means algorithm is used to predict the clusters for the Iris data, but now, the principal components data is used with `k=3`.

  ```python
  # Initialize the K-Means model
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(df_iris_pca)

  # Predict clusters
  predictions = model.predict(df_iris_pca)
  ```

* Finally the clusters are plotted, now they are easier to analyze since we have only two features.

  ![Clusters plot](Images/pca-clusters-plot.png)

Answer any questions before moving on.
