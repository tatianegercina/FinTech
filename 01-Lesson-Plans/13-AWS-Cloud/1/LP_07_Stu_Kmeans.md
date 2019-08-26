### 7. Student Do: Customer segments for e-commerce (20 min)

In this activity, students will identify the best number of clusters on a customers clustering scenario using the Elbow Curve, next students will use K-Means to cluster data and make conclusions about the obtained results.

**Instructions:**

* [README.md](Activities/04-Stu_K_Means_In_Action/README.md)

**Files:**

* [04_Stu_K_Means_In_Action.ipynb](Activities/04-Stu_K_Means_In_Action/Unsolved/04_Stu_K_Means_In_Action.ipynb)

* [shopping_data_cleaned.csv](Activities/04-Stu_K_Means_In_Action/Unsolved/data/shopping_data_cleaned.csv)

---

### 8. Instructor Do: Review Customer segments for e-commerce (10 min)

**Files:**

* [04_Stu_K_Means_In_Action.ipynb](Activities/04-Stu_K_Means_In_Action/Solved/04_Stu_K_Means_In_Action.ipynb)

* [shopping_data_cleaned.csv](Activities/04-Stu_K_Means_In_Action/Solved/data/shopping_data_cleaned.csv)

Walk through the solution and highlight the following:

* In this activity, the customers shopping data that were preprocessed before is used. Data is loaded on the `df_shopping` DataFrame.

    ```python
    file_path = Path("data/shopping_data_cleaned.csv")
    df_shopping = pd.read_csv(file_path)
    ```

* The Elbow Curve is used to find the best value for `k`, a `for-loop` is used to loop 10 times fitting the K-Means model and fetching the `inertia` to create the plot.

    ```python
    inertia = []
    k = list(range(1, 11))

    # Calculate the inertia for the range ok k values
    for i in k:
        km = KMeans(n_clusters=i, random_state=0)
        km.fit(df_shopping)
        inertia.append(km.inertia_)
    ```

* The Elbow Curve is created using `hvPlot`.

    ```python
    elbow_data = {"k": k, "inertia": inertia}
    df_elbow = pd.DataFrame(elbow_data)
    df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="Elbow Curve")
    ```

Explain students that, after observing the Elbow Curve, it can be concluded that the best two values for `k` can be `5` and `6` since at those points the elbow shape starts.

![Elbow Curve](Images/elbow-curve-customers.png)

* The `get_clusters()` function, is a mechanism to encapsulate the K-Means clustering algorithm to be reused. The value of `k` and the `data` where the clusters are going to be identified are passed as parameters.

    ```python
    def get_clusters(k, data):
        # Initialize the K-Means model
        model = KMeans(n_clusters=k, random_state=0)

        # Fit the model
        model.fit(data)

        # Predict clusters
        predictions = model.predict(data)

        # Create return DataFrame with predicted clusters
        data["class"] = model.labels_

        return data
    ```

* A visual analysis of using K-Means with `k=5` and `k=6` is done by creating a 2D-Scatter plot as well as a 3D-Scatter plot.

| Plot Type       | `k=5`                                       | `k=6`                                       |
| --------------- | ------------------------------------------- | ------------------------------------------- |
| 2D Scatter plot | ![2D Scatter k=5](Images/2d-scatter-k5.png) | ![2D Scatter k=6](Images/2d-scatter-k6.png) |
| 3D Scatter plot | ![3D Scatter k=5](Images/3d-scatter-k5.png) | ![3D Scatter k=5](Images/3d-scatter-k6.png) |

Comment to students, that plotting the clusters helps to have an idea about how the features interact and how the clusters are influenced by the features, despite only two or three dimensions can be plotted, doing a visual analysis contributes on decision making.

* After analyzing the plots, it can be concluded that using `k=6`, a more meaningful segmentation of customers can be done as follows:

  * _Cluster 1_: Medium income, low annual spend
  * _Cluster 2_: Low income, low annual spend
  * _Cluster 3_: High income, high annual spend
  * _Cluster 4_: Low income, high annual spend
  * _Cluster 5_: Medium income, low annual spend
  * _Cluster 6_: Very high income, high annual spend

* Having defined these clusters, we can formulate marketing strategies relevant to each cluster aimed to increase revenue.

Encourage one or two students to share theirs conclusions, ask any reminder question and move forward.
