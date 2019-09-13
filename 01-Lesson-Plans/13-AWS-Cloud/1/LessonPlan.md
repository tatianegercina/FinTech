## 13.1 Lesson Plan: Unsupervised Learning and The Cloud

### Overview

Today's class will introduce students to unsupervised learning and cloud services. Students will gain hands-on experience with the K-Means algorithm, one of the most used unsupervised algorithms for clustering. Additionally, students will learn how to speed up ML algorithms by using principal component analysis (PCA), as well as to recognize and explain at least three main differences between supervised and unsupervised machine learning algorithms.

The concept of _The Cloud_ is presented to students, by highlighting the importance that these kind of computing services have for FinTech professionals, given that the cloud allows to scale machine learning models to be used by hundreds or thousands of users.

As a prelude for the rest of the unit, a demo of the homework is presented, as well as an introduction to Amazon Web Services (AWS) and AWS SageMaker.

### Class Objectives

By the end of the class, students will be able to:

* Recognize the differences between supervised and unsupervised machine learning.

* Apply the K-Means algorithm to identify clusters on a given dataset.

* Diagnose what are the data preprocessing tasks that a dataset would need to apply the K-Means algorithm.

* Demonstrate how the K-Means algorithm is useful for customer segmentation.

* Speed-up the ML algorithms using principal component analysis.

* Understand the basic concepts of the cloud and Amazon Web Services.

* Recognize the main features of AWS SageMaker.

### Instructor Notes

* Students have learned the generalities of ML and they already know how to apply supervised ML; this class offers an overview of unsupervised ML, students will have hands-on experience using K-Means on a business case scenario, to demonstrate how unsupervised ML could add value to business decision making.

* Understating unsupervised learning may be challenging, however everyone is a customer and are familiar with how companies use data to target customers or potential customers to offer products and services, try to use analogies about how companies like [Amazon, Netflix, Google](https://www.pointillist.com/blog/customer-behavior-data/), or [Target](https://www.forbes.com/sites/kashmirhill/2012/02/16/how-target-figured-out-a-teen-girl-was-pregnant-before-her-father-did/) are using customer segmentation to provide a customized offer, or [how Spotify is using segmentation](https://towardsdatascience.com/in-this-article-i-provide-a-detailed-analysis-of-spotify-as-a-company-music-industry-direction-eeb945d7257c) to improve their products and services.

* There are several theoretical aspects behind the K-Means and PCA algorithms, focus the class on the practical application of these algorithms for customer segmentation and share the additional references presented on the slides for those students interested on having a deeper understanding.

* The cloud is a core concept for FinTech professionals, however it might be seen complex and nebulous for some students; it's important to highlight how companies like Amazon Web Services have reduced the technological complexity behind the cloud, by offering user friendly interfaces that allow to deploy a machine learning model with few lines of code and some mouse clicks.

* On Day 1, a homework demo is presented, be sure to get familiar with homework's solutions before the class.

* Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. Also encourage students to work with partners.

* **Important!** Slack out the disclaimer for [AWS Free Tier](../Supplemental/AWS-Free-Tier.pdf) services at the end of Today´s class. Explain students, that while we are only using free tier services in class, they should review this documentation in order to avoid accidentally incurring charges.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.1 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 mins)

In this activity, students will be introduced to unsupervised learning and its most relevant applications. Also, an overview of the unit is presented including a homework demo.

**Files:**

* [Lesson 13.1 Slides]()

Welcome the class to Unit 13, open the lesson slides and move to the _What you will achieve on this unit_ section by highlighting the following:

* The cloud is a core tool for FinTech professionals, students will learn how to leverage their Python and machine learning skills, by using Amazon Web Services to deploy models and business applications that could be reached by hundreds or thousands of people.

* Along this unit, students will have hands-on experience with the following AWS services:

  * **Amazon SageMaker:** To deploy machine learning models.
  * **Amazon Lex:** To create conversational interfaces.
  * **Amazon S3:** To store files in the cloud.
  * **AWS Lambda:** To create serverless applications.

Open your AWS Management Console, open the _Cryptocurrencies Clustering_ homework's solution and briefly explain to students that a machine learning model could be deployed in the cloud using Jupyter notebooks, a tool they already know, and Amazon SageMaker.

Continue by opening the Amazon Lex Management console, open the _RoboAdvisor_ homework's solution, and test the bot with the sample utterance `I'm worried about my retirement` to conduct a sample dialog as follows.

![RoboAdvisor Demo](Images/robo-advisor-demo.gif)

Ends the homework demo, by commenting students that they will create two chatbots using Amazon Lex and AWS Lambda in this unit:

1. A cryptocurrencies converter.

2. An investment portfolio robo advisor.

Continue with the slides by highlighting the following:

* Cloud services are awesome tools for FinTech professionals, students already master several skills that will empower the cloud applications they will be able to create, however.

* This journey starts by learning about unsupervised learning.

Make sure that all students have created their AWS account, ask TAs to assist any student that could be pending on creating it.

Answer any questions before moving on.

---

### 2. Instructor Do: Introduction to Unsupervised Learning (10 mins)

After an introduction to machine learning and NLP, students are eager to learn more about this matter. In this activity, students will be introduced to unsupervised learning and its most relevant applications.

**Files:**

* [Lesson 13.1 Slides]()

Open the lesson slides and go to the _Introduction to Unsupervised Learning_ section.

Start the presentation by explaining to students that, in general terms, machine learning has two main areas of application, supervised and unsupervised learning.

Students are already familiar with supervised learning algorithms and its applications, highlight to students the main differences between these types of learning.

| Supervised Learning                      | Unsupervised Learning                    |
| ---------------------------------------- | ---------------------------------------- |
| Input data is labeled                    | Input data is unlabeled                  |
| Uses training datasets                   | Uses just input datasets                 |
| **Goal:** Predict a class or value | **Goal:** Determine patterns or grouping data |

Start a short facilitated discussion with students, take one or two answers from the class by asking the following question.

* If unsupervised learning deals with unlabeled data, what kind of questions or business problems do you think can we afford?

  **Sample Answer:** We can group customers on a retail chain by shopping habits, so we can send customized offers by e-mail or using a mobile app to increase sales.

  **Sample Answer:** Having thousands of transactions per day on credit card operations, it's hard to identify anomalous or fraudulent transactions, we can use unsupervised learning to find patters among transactions data to identify anomalies and potential fraudulent transactions.

  **Sample Answer:** We can use unsupervised learning to cluster stocks data, so we can create investment portfolios according to the resulting groups.

As an example, a customer clustering problem is followed; continue with the presentation on the slide entitled _How can we understand our customers?_, move forward by highlighting the following:

* Beyond the typical segmentation variables, such as age, gender, income or zip code, nowadays understanding customers is crucial on every sector.

* Supervised learning is very helpful predicting the future based on labeled historic data, however, there are some hidden patters on data that supervised learning is unable to find.

* Unsupervised learning enhances customers understanding, we can cluster data to find hidden or unknown patterns that can be used, for example, to develop a customized offer that responses to the needs identified on every group.

* The main applications of unsupervised learning on industry are:

  * **Clustering:** It allows to automatically split the dataset into groups according to similarity. It can be used for customer segmentation and targeting.

  * **Anomaly Detection:** Automatically discovers unusual data points in a dataset. It's useful in identifying fraudulent transactions, discovering faulty pieces of hardware, or identifying an outlier caused by a human error during data entry.

* Customer segmentation is one of the most popular applications of unsupervised learning. It is the division of potential customers in a given market into discrete groups.

* Thanks to unsupervised learning algorithms, we can group customers based similarities such as:

  * Customer needs (e.g. a particular product can satisfy some of them).
  * Responses to online marketing channels.
  * Buying habits (e.g. best day for buying, weekly spend)

Comment to students, that customer segmentation is driving revenue in leading companies such as Netflix and Amazon as it's presented on the slides.

  * 75% of Netflix viewer activity is driven by recommendation ([Source](http://blog.springtab.com/personalization-examples-netflix/)).
  * 35% of Amazon’s sales are generated through their recommendation engine ([Source](https://www.martechadvisor.com/articles/customer-experience-2/recommendation-engines-how-amazon-and-netflix-are-winning-the-personalization-battle/)).
  * Netflix’s recommendation system saves the company an estimated $1Billion per year through reduced churn ([Source](https://dl.acm.org/citation.cfm?id=2843948)).

End the presentation with a closing facilitated discussion, ask the following questions to students:

* How a bank could use customer segmentation to improve their products?

  **Sample Answer:** Instead of having a generic offer of credit cards, a bank could use customer segmentation to offer credit cards according to demographics such as: age, geography, gender, generation (e.g. Millennials and Baby Boomers), income level, marital status, etc.

* How an investment portfolio can be improved using customer segmentation?

  **Sample Answer:** Using customer segmentation a portfolio can be categorized by industry, location, revenue, account size, and number of employees to reveal where risk and opportunity live within the portfolio. These patterns can provide key measurable data for more predictive credit risk management.

Comment to students that, unsupervised learning and algorithms like K-Means, are the tools behind this kind of magic that is perceived by customers.

Answer any questions before moving on.

--

### 3. Instructor Do: Data Preparation for Unsupervised Learning (10 mins)

In this activity, students will learn about the data preparation considerations they should take into account before start working with unsupervised learning algorithms.

**Files:**

* [01_Ins_Data_Preparation.ipynb](Activities/01-Ins_Data_Prep/Solved/01_Ins_Data_Preparation.ipynb)

* [iris.csv](Activities/01-Ins_Data_Prep/Resources/iris.csv)

* [new_iris_data.csv](Activities/01-Ins_Data_Prep/Resources/new_iris_data.csv)

Before start playing with unsupervised learning algorithms, explain to students that data preparation for unsupervised learning doesn't differ to much from the process followed for supervised learning problems.

Comment to the class that, as they already done in past lessons, they should consider the following data preparation tasks:

1. **Data Selection:** Make a good choice of what data are going to be used. It's important to consider what data is available, what data is missing and what data can be removed.
2. **Data Preprocessing:** Organize the selected data by formatting, cleaning and sampling it.
3. **Data Transformation:** Transform the data to a format that eases its treatment and storage for future use (e.g. CSV file, spreadsheet, database).

Highlight to students, that the main difference on preparing data for unsupervised learning is that its algorithms don't have any target variable, they only have input features that will be used to find patterns on the data. So, they should take care on selecting features that could help to find those patterns or create groups.

Open the unsolved version of the Jupyter notebook, live code the demo and highlight the following:

* To get started with unsupervised learning, [the iris dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) will be used. So, the data preparation workflow will use this data.

* The data preparation workflow is quite similar as the one students have been following in the past, once the data is selected, the next step is to load the data into a pandas DataFrame.

  ![Lading the iris dataset](Images/reading-iris-data.png)

* In forthcoming activities, the `class` of the iris plants will be found using unsupervised learning, so the next step is to remove the `class` column since it is not necessary.

  ![Removing the class column](Images/removing-class-column.png)

Comment to students that, since all the variables on the dataset are numerical, there are no additional data preprocessing tasks to do. However, data transformations have to be done when there are categorical data or non-numeric features on the dataset. For example, transforming `male` and `female` categorical values to `0` and `1` respectively.

* Finally, the preprocessed DataFrame is saved on a new `CSV` file for further use.

  ```python
  file_path = Path("../Resources/new_iris_data.csv")
  new_iris_df.to_csv(file_path, index=False)
  ```

Ask the class if there are any further questions before moving on the next activity.

---

### 4. Students Do: Understanding customers (20 mins)

In this activity, students will perform some data preparation tasks on a dataset that contains data from purchases on a e-commerce website made by 200 customers. Students will use this dataset on further activities to find customers segments.

There are some data transformations that should be made on the dataset, so ask TAs to assist students if there are any questions about why the following changes are needed.

* **Annual Income:** This feature should be regularized since it’s in a different scale than the other features; dividing by `1000` is the simplest solution.

* **Gender:** The `Gender` should be transformed to a numerical value, in this case, transforming `Male` to `1` and `Female` to `0` is a feasible solution.

* **CustomerID:** Since this column is not relevant to the clustering algorithm, it should be dropped from the DataFrame.

**Instructions:**

* [README.md](Activities/02-Stu_Preparing_Data/README.md)

**Files:**

* [preparing_data.ipynb](Activities/02-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

* [shopping_data.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data.csv)

---

### 5. Instructor Do: Review Understanding customers (10 mins)

**Files:**

* [preparing_data.ipynb](Activities/02-Stu_Preparing_Data/Solved/preparing_data.ipynb)

* [shopping_data.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data.csv)

* [shopping_data_cleaned.csv](Activities/02-Stu_Preparing_Data/Resources/shopping_data_cleaned.csv)

Walk through the solution and highlight the following:

* Unsupervised learning algorithms only work with numerical data, so checking data types is an important task to ensure that numerical values were loaded to the DataFrame with the appropriate data type.

  ![Data types check](Images/datatypes-check.png)

* All columns have an appropriate data type, so no adjustments are needed.

* The `CustomerID` column can be dropped, it's not relevant for clustering since it doesn't denote any relevant characteristic of customers shopping habits.

  ```python
  df_shopping.drop(columns=["CustomerID"], inplace=True)
  ```

* Looking for `null` values and duplicate entries is part of any data preprocessing workflow; there are no `null` values nor duplicates on this DataFrame, so no additional adjustments are needed on this matter.

* The `Genre` column is categorical, so it should be transformed to numerical values. Transforming `Male` to `1` and `Female` to `0` is a common practice.

  ```python
  def changeGenre(genre):
    if genre == "Male":
        return 1
    else:
        return 0

  df_shopping["Genre"] = df_shopping["Genre"].apply(changeGenre)
  ```

* The `Annual Income` column is on a different scale than the other columns, so this column should be rescaled. Dividing by `1000` is the simplest approach.

  ```python
  df_shopping["Annual Income"] = df_shopping["Annual Income"] / 1000
  ```

* Finally, the cleaned DataFrame is saved as a `CSV` file for being used on forthcomming activities.

```python
  file_path = Path("../Resources/shopping_data_cleaned.csv")
  df_shopping.to_csv(file_path, index=False)
  ```

Be sure that there are no pending questions before moving forward.

---

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

---

### 7. Student Do: Customer segments for e-commerce (20 min)

In this activity, students will identify the best number of clusters on a customers clustering scenario using the Elbow Curve, next students will use K-Means to cluster data and make conclusions about the obtained results.

**Instructions:**

* [README.md](Activities/04-Stu_K_Means_In_Action/README.md)

**Files:**

* [k_means_in_action.ipynb](Activities/04-Stu_K_Means_In_Action/Unsolved/k_means_in_action.ipynb)

* [shopping_data_cleaned.csv](Activities/04-Stu_K_Means_In_Action/Resources/shopping_data_cleaned.csv)

---

### 8. Instructor Do: Review Customer segments for e-commerce (10 min)

**Files:**

* [k_means_in_action.ipynb](Activities/04-Stu_K_Means_In_Action/Solved/k_means_in_action.ipynb)

* [shopping_data_cleaned.csv](Activities/04-Stu_K_Means_In_Action/Resources/shopping_data_cleaned.csv)

Walk through the solution and highlight the following:

* In this activity, the customers shopping data that were preprocessed before is used. Data is loaded on the `df_shopping` DataFrame.

    ```python
    file_path = Path("../Resources/shopping_data_cleaned.csv")
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

--

### 9. BREAK (15 min)

---

### 10. Instructor Do: Speeding up ML algorithms with PCA (10 min)

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

---

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

---

### 13. Instructor Do: Welcome to the Cloud and Amazon Web Services (10 min)

In this activity, students will be introduced to the cloud and the generalities of Amazon Web Services.

**Files:**

* [Lesson 13.1 slides]()

Open the lesson slides, move to the _Welcome to The Cloud and Amazon Web Services_ section and introduce the concept of _The Cloud_ by asking students to share what they think the cloud is.

Collect two or three answers, and emphasize the following points:

* In essence, the cloud refers to the on-demand availability of computer system resources.

* The computing resources include: compute processing power, data storage, and other services.

* There is no need to have physical access to the hardware, it is managed through the internet (through public and/or private networks).

* Normally, you pay as you go for what you use (sometimes down to the second or byte) with little or no upfront costs.

* Services are usually charged like a utility service (think electricity bill).

* Cloud computing is usually cheaper due to the economics of scale (and no upfront cost of physical hardware, setup or provisioning).

* You get access to unlimited resources (in theory, maybe not practice).

* There are multiple services models, with trade-offs in responsibility and control. The most common are:
  * **Infrastructure as a service (IaaS):** Online services that provide APIs to access different infrastructure such as servers, virtual machines, storage, load balancers or network interfaces (e.g. [Azure Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/)).
  * **Platform as a service (PaaS):** Provides a platform that allow customers to develop, run, and manage applications without the complexity of building and maintaining their own physical infrastructure (e.g. [Amazon Web Services](https://aws.amazon.com/)).
  * **Software as a service (SaaS):** Refers to a software licensing and delivery model where software is licensed on a subscription basis and is centrally hosted (e.g. [Microsoft Office 365](https://www.office.com)).
  * **Function/Code as a service (FaaS):** Also known as _serverless computing_, it offers a remote procedure call that enables the deployment of individual functions in the cloud that run in response to events (e.g. [AWS Lambda](https://aws.amazon.com/lambda/)).

* _Clouds_ can be created in a private data center (_Private Cloud_), in a data center managed by a provider (_Public Cloud_) or in a combination of both (_Hybrid Cloud_)

* Cloud computing is considered secure enough to be used by many banks and government offices.

* Cloud services allow you to scale your resources up and down as required.

* There are multiple Cloud service providers, including: Amazon, Microsoft, Google, Oracle and IBM.

* Some of the disadvantages of the cloud are:

  * Having to trust a 3rd party provider with your data (encryption can sometimes address this).
  * You probably have to give up some privacy and confidentiality.
  * You depend on the Service Level Agreements of a provider for issues to be addressed.
  * Incidents such as hardware failure are inevitable but you have less oversight on their resolution.
  * Hardware might be shared with other tenants, "bad neighbors" can affect your resources.
  * Clouds can fail and have downtime, including due to planned maintenances out of your control.

Visit the [Amazon Web Services (AWS)](https://aws.amazon.com/) homepage and cover the following points:

* Launched in March 2006, Amazon Web Services ("AWS", a subsidiary of Amazon.com) popularized the concept of "Cloud Computing".

* AWS comprises more than 140 services, including technologies for compute, storage, networking, database, analytics, IoT, Machine Learning and more.

* AWS started with a service called _Elastic Compute Cloud_ (or "_EC2_").

* Although Amazon didn't invent the concept, it pioneered the Cloud's adoption.

* AWS is the leading cloud computing provider (in 2019).

* [Thousands of companies use AWS](https://aws.amazon.com/solutions/case-studies/all/), including: 2U, AirBnb, Adobe, CapitalOne, Comcast, Dropbox, Expedia, GE, Kellogg's, McDonalds's, Philips, Yelp, and many more.

Slack-out this following link to students if they want to learn more about the AWS offer: [AWS Cloud Products](https://aws.amazon.com/products/)

Answer any questions before moving on.

---

### 14. Instructor Do: Intro to Amazon SageMaker (5 min)

In this activity, students will learn how Amazon SageMaker works and what are its main features.

Open your web browser, visit the [AWS SageMaker homepage](https://aws.amazon.com/sagemaker/) and highlight the following points:

![Amazon SageMaker homepage](Images/amazon-sagemaker-home.png)

* Amazon SageMaker is a _platform service_ which consists of three main components that work together or independently:

  * **Build:** Notebook service to explore and prepare the data
  * **Train:** Model training environment and infrastructure
  * **Deploy:** Publish and host a model on an HTTP API endpoint or execute a batch prediction / inference.

* Additionally, Amazon SageMaker includes layers that work across all the components:

  * **Ground Truth:** Data labeling service.
  * **Tuning:** Automatic Model Tuning by searching hyper-parameter values for best model fit.
  * **Algorithms:** Built-in algorithms (K-NN, K-Means, PCA, Forecasting, and many more).
  * **Frameworks:** Deep learning framework containers (Scikit-learn, TensorFlow, MXNet, PyTorch, and others).
  * **Docker containers:** Bring your own model or algorithm container and publish to [AWS ECR](https://aws.amazon.com/ecr/).
  * **Marketplace:** Amazon SageMaker integrates with AWS Marketplace to find, buy and deploy third-party algorithms and models.

Review some of the advantages of using Amazon SageMaker:

* Provides tools that streamline a typical workflow for creating a machine learning model.
* Its infrastructure enables growth at scale with on-demand compute instances and dynamic storage.
* Pricing for building, training and hosting is billed by the second, no minimum fees and no upfront commitments.
* Advertises "One-click Training" and "One-click Deployment".
* Comes with built-in security, which includes access controls and monitoring.

Answer any questions before moving on.

---

### 15. Students Do: Explore SageMaker (5 min)

This activity is intended to give students a few minutes to explore SageMaker.

Ask students to login into their [AWS Console](https://console.aws.amazon.com) and highlight the following:

* The Amazon SageMaker service could be reached at the _Find Services_ search box by typing `sagemaker` on it.

    ![Looking for SageMaker](Images/looking-sagemaker.png)

* Amazon SageMaker might not be available on all AWS regions, but `us-west (Oregon)` is sure to have it.

Ask students to explore the main components on the left pane menu, they can explore beyond the class by clicking on _Start with an overview_.

![Amazon SageMaker Landing Page](Images/sagemaker-landing.png)

Have TA's ensure all students are able to login, and answer any questions before moving on.


### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
