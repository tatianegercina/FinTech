# Unit 13: AWS-Cloud

### Helpful Links

* Click [here](https://d1.awsstatic.com/whitepapers/aws-overview.pdf) for a thorough whitepaper from Amazon Web Services describing what cloud computing is and what role their tools play.

* This guide from AWS is a handy reference for Lex bot deployments - [Deploying Amazon Lex Bots.](https://docs.aws.amazon.com/lex/latest/dg/examples.html)

---

### Additional Course Resources

* [Creating and Activating an AWS Account](1-Create-and-Activate-an-AWS-Account.md)

---

### FAQs

<details>
<summary>What is the difference between supervised learning and unsupervised learning?</summary><br>
<blockquote>
<details>
<summary>Supervised Learning</summary>

Supervised machine learning uses labeled data with input variables (feature data) and output variables (target data) and uses the feature data to predict the target data.  The data is divided into training and testing sets.  The training set is used to teach (supervise!) the model so it learns how the input data is connected to the output data and can make predictions.  The testing data set is used to validate how well the model performs on data it has not seen before, by running the model on the testing feature data, and comparing it's predictions to the testing target data.<br>
<br>
An example of supervised learning would be to predict this year's final grades in a class based on last year's student study habit data as feature data, with their corresponding final grades as target data.  The model could be trained with the previous year's data, and then used to make predictions on this year's final grades using the study habit data from the new class.

</details>
<details>
<summary>Unsupervised Learning</summary>

Unsupervised learning models are given only input variables and must work to make connections to the data without predicting a labeled target.  These types of models are often clustering models that uncover connections in the data and group all the features into classes accordingly.<br>
<br>
An example of unsupervised learning would be to use website purchase data to group customers into two classes based on their spending habits.  This clustering might reveal that class 1 more spends more with a coupon incentive, while class 2 spends more on targeted advertising on social media.

</details>
</blockquote>
</details>


<details>
<summary>What is KMeans?</summary>

<blockquote>
<details>
<summary>What it is:</summary>

Kmeans is one of the most popular unsupervised machine learning models.  This clustering algorithm uses a number (refered to as `k`) of clusters and then plots those initial clusters in random locations. The distance between each cluster and each data point is then taken, and each data point is assigned to the nearest cluster, after which the mean of each cluster is calculated to create centroids.  Centroid is simply the word for the mean of the cluster (the center!).  The data is reclustered based on the new centroid location rather than the initial random location. This is where the *means* in *k-means* comes from! The variance of the clusters is then calculated, and the process starts again with new randomly generated clusters.  The process is repeated for the number of times you specify, after which the scenario with the lease variance is chosen to represent the final clusters.

![k-means](Images/k-means.gif)


The following video from StatQuest on YouTube provides an excellent, easy to understand explanation of the process: [K-means Clustering.](https://www.youtube.com/watch?v=4b5d3muPQmA)
</details>

<details>
<summary>How do you determine the `k` number of clusters?</summary>
There are several ways to deterimine the best number of clusters for your model. For our class, we use the elbow method.  The elbow method takes into account a range of values for `k` and plots their inertia, inertia being how far the clusters expand from the centroid.  This number should be as low as possible, indicating tightly packed clusters.  When these values are plotted on a line chart, a bend should form where the optimal value of `k` is located.  This bend incates the point at which adding clusters does not greatly improve the inertia, thus the smallest amount of clusters with the best inertia.

In the below elbow chart, the bend occurs at 6, meaning this is the optimal value for `k` for this example:

![elbow chart](Images/elbow_chart.png)
</details>
</blockquote>
</details>

<details>
<summary>What is PCA?</summary>

</details>
<details>
<summary>What is the cloud?</summary>
<blockquote>
<details>
<summary>Types of cloud services:</summary>

</details>
</blockquote>
</details>


<details>
<summary>What is AWS and why should I care?</summary>

</details>

<details>
<summary>What is an IAM Role?</summary>c

</details>

<details>
<summary>What are S3 buckets?</summary>

</details>
<details>
<summary>What is Boto3?</summary>

</details>
<details>
<summary>What is Sagemaker?</summary>

<blockquote>
<details>
<summary>Sagemaker SDK Docs</summary>

</details>

<details>
<summary>Built-in Algorithms</summary>

</details>
</blockquote>
</details>

<details>
<summary>Why deploy a machine learning model in the cloud?</summary>

</details>

<details>
<summary>What is a conversational user interface?</summary>

</details>
