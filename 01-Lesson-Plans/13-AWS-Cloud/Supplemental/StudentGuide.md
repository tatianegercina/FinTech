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
Placeholder
https://www.youtube.com/watch?v=FgakZw6K1QQ
</details>
<details>
<summary>What is the cloud?</summary>

The cloud is an abstract term for accessing computing power online from a machine other than your own.  When you save files to the cloud, it really just means you're saving your files on a machine (server) located somewhere else, but that can be accessed anywhere via the internet.  These servers are located on server farms where thousands of computers are operating simultaneously to provide computing services via *"the cloud"*.

Storage such as Google Drive is a popular cloud computing product, but there are many others.  Amazon Web Services (AWS) currently provides over 175 services on the cloud.  Examples include; Sagemaker - which allows you to run juypter notebooks on the cloud, Lex - which allows you build conversational interfaces (chatbots) and run them in the cloud, and Relational Database Service (RDS), which allows you to connect to a database via the cloud.

For a full list of AWS services click [here.](https://aws.amazon.com/products/)

<blockquote>
<details>
<summary>Types of cloud services:</summary>

Cloud services can be divided into 4 general categories:

**Infrastructure as a service (IaaS):** Online services that provide APIs to access different infrastructures such as servers, virtual machines, storage, load balancers, or network interfaces (e.g., [Azure Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/)).

**Platform as a service (PaaS):** Provides a platform that allow customers to develop, run, and manage applications without the complexity of building and maintaining their own physical infrastructure (e.g., [Amazon Web Services](https://aws.amazon.com/)).

**Software as a service (SaaS):** Refers to a software licensing and delivery model where software is licensed on a subscription basis and is centrally hosted (e.g., [Microsoft Office 365](https://www.office.com/)).

**Function/code as a service (FaaS):** Also known as serverless computing, it offers a remote procedure call that enables the deployment of individual functions in the cloud that run in response to events (e.g., [AWS Lambda](https://aws.amazon.com/lambda/)).

</details>
</blockquote>
</details>


<details>
<summary>What is AWS?</summary>

AWS is a cloud computing platform provided by Amazon, offering over 175 different services via the cloud.  AWS is trusted by large companies and individual users alike to provide scalable, flexible computing power that is both cost effective and secure.  You might be surprised to know that many companies, including Netflix, use AWS for all their tech needs, including database and storage.

Because the infrastructure is already in place, companies can easily scale up as needed without a huge up-front investment, and because they offer flexible usage options there is a cost appropriate option for everyone.

</details>

<details>
<summary>What is an IAM Role?</summary>

AWS Identity and Access Management (IAM) allows you to securely control the acces of others to your AWS resources.   By creating an IAM User you are granting others secure access to your account without actually giving them your password.  After creating the user, a role can be assigned to the user that defines and resticts that access as you wish.  An IAM role defines *who* can do *what* to your AWS resources, and *when* they can do it. [This](https://aws.amazon.com/iam/faqs/) document from AWS contains some great frequently asked questions baout the IAM service.

</details>

<details>
<summary>What are S3 buckets?</summary>

Simple Storage Service, or S3 as its commonly known, is one of the most popular AWS services and was also one of first to be introduced, launching back in 2006.  S3 offers secure object storage in the cloud for anything from csv files to images and can be scaled as needed.  S3 can be used for anything from simple image hosting for your website, to connecting to data directly for database applications or analytics.

Much like using virtual file folders on your own machine to store and organize your files, an S3 bucket is simply where your objects are stored on S3.

</details>
<details>
<summary>What is Boto3?</summary>

Boto3 is considered a Software Development Kit (SDK) for AWS.  SDKs are similar to Application Programming Interfaces (APIs) in that they both allow the user to interact with a platform, however SDKs are built to interact with a specific platform, where APIs are typicall used to allow platforms to interact with each other.  Boto3 allows Python developers to with various AWS resources outside of the AWS console, by programming those resources with code.

A popular application of Boto3 is working with the contents of S3 buckets.  Boto3 is used to access those contents via Python code, and then you can manipulate the contents as you normally would - for example you might use Boto3 inside a Jupyter Notebook to load CSVs from an S3 bucket and then proceed to work with those CSVs with Pandas.

The [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is a great starting point for working with this SDK.  It describes the usage of the SDK and provides tutorials for implementing it with various AWS resources.

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
