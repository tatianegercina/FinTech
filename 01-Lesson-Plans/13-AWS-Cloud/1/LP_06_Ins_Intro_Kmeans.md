### 6. Instructor Do: The K-Means Algorith (15 min)

In this activity, students will learn how the K-Means algorithm works, use your time wisely to cover the theoretical part as well as the coding part.

**Files:**

* [Lesson 13.1 slides]()

* [03_Ins_K-Means.ipynb](Activities/03-Ins_KMeans/Solved/03_Ins_K-Means.ipynb)

Open the lesson slides and move to _The K-Means Algorithm_ section, go through the slides an highlight the following.

* To understand how K-Mean works a fictional anecdote is used.

  > The anecdote begins by imagining you are on a room full of blue spheres, you want to learn more about them, so you start to observe around.
  >
  > You realized that every sphere represents a flower and that axes represent features of flowers. After observing the flowers, you discovered that there are some patterns when you combine the three features.
  >
  > At this point, K-Means comes to the rescue!

Finish the anecdote, by explaining to students, that K-Means is an unsupervised learning algorithm used to identify clusters and solve clustering issues.

Continue on the slides to formally introduce K-Means, highlight the following:

* K-Means algorithm groups the data into `k` clusters, where belonging to a cluster is based on some similarity or distance measure to a _centroid_.

* A _centroid_ represents a data point that is the arithmetic mean position of all the points on a cluster.

* At a glace, the K-Means algorithm works as follows:

  1. Randomly initialize the `k` starting centroids.
  2. Each data point is assigned to its nearest centroid.
  3. The centroids are recomputed as the mean of the data points assigned to the respective cluster.
  4. Repeat steps `1` through `3` until the stopping criteria is triggered.

* One of the key tasks using K-Means is to find the best number of `k`.

* The _Elbow Curve_ is the most common method used to figure out the best value of `k`.

* On the _Elbow Curve_, the `x` axis is the value of `K`, while the `y` axis is the value of some objective function.

* The _inertia_, that is the sum of squared distances of samples to their closest cluster center, is commonly used as objective function.

* Visually the best number for `k`, is the `k` value where the curve turns showing like an elbow on the curve.

* Analytically using the inertia, we choose as the best `k`, the `k` value where adding more clusters only marginally decreases the inertia.

Comment to students, that Today they will learn how to use `K-Means` and finding the best value for `k` using Python.

Close the presentation, open the starter unsolved Jupyter notebook and live code the demo by highlighting the following:

* This demo uses the data from the Iris dataset presented before.

* The K-Means algorithm is imported from the `sklearn` library.

  ```python
  from sklearn.cluster import KMeans
  ```

* After the data is loaded on a DataFrame, the first step is to create an instance of the K-Means algorithm and initialize it with the desired number of clusters (K). For this demo, we will use `k = 3` since we already know we have three classes of iris plants.

  ```python
  model = KMeans(n_clusters=3, random_state=5)
  ```

* Once the model instance is created, the next step is to fit the model with the unlabeled data. When the model is fitted, the K-Means algorithm will iteratively look for the best centroid for each of the `k` clusters.

  ```python
  model.fit(df_iris)
  ```

* After the model is fitted, the corresponding cluster for every iris plant on the dataset can be found using the `predict()` method.

  ![K-Means predictions](Images/kmeans-predictions-iris.png)

Explain to students that, as they can see, three classes were found labeled as `0`, `1`, and `2`. Make clear to the class that naming classes is part of the job done by a subject matter expert on each business case, the K-Means algorithm is just able to identified how many clusters are on the data and label them with numbers.

Continue the demo by adding a new column to the DataFrame with the predicted classes.

![Adding predicted classes](Images/addind-classes-column.png)

* Visualizing the clusters helps to graphically understand how they are arranged, despite we have four features on the DataFrame, we can take two or three of them to plot the clusters.

  | Two features                          | Three Features                        |
  | ------------------------------------- | ------------------------------------- |
  | ![2 Features](Images/plotting-2d.png) | ![3 Features](Images/plotting-3d.png) |

Continue the live coding demo by showing students how the best value for `k` can be found, highlight the following:

* Two list are created to store the values for the `inertia` and to define how many values of `k` we want to try. Ten values of `k` are normally a good number to start.

  ```python
  inertia = []
  k = list(range(1,11))
  ```

* A `for-loop` is defined to fit the K-Means model with the data from `df_iris` and a number of clusters ranging from 1 to 10, the `inertia` is fetched on each iteration to be compared on the Elbow Curve.

  ```python
  # Looking for the best k
  for i in k:
      km = KMeans(n_clusters = i, random_state = 0)
      km.fit(df_iris)
      inertia.append(km.inertia_)
  ```

* The Elbow Curve is plotted using `hvPlot`, so a DataFrame is created.

  ```python
  elbow_data = {
    "k": k,
    "inertia": inertia
  }
  df_elbow = pd.DataFrame(elbow_data)
  df_elbow.hvplot.line(x = "k", y="inertia", title="Elbow Curve", xticks=k)
  ```

* As can be seen on the Elbow Curve, visually the best value for `k` is `3`.

  ![Elbow Curve](Images/elbow-curve.png)

Answer any question that could arise from the class before continue.
