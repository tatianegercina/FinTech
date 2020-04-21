## 13.1 Lesson Plan—Unsupervised Learning and The Cloud

### Overview

Today's class will introduce students to unsupervised learning and cloud services. Students will gain hands-on experience with the k-means algorithm, one of the most used unsupervised learning algorithms for clustering. They will also learn how to speed up machine learning (ML) algorithms by using principal component analysis (PCA), and recognize and explain at least three main differences between supervised and unsupervised ML algorithms.

The concept of **the cloud** is presented to students by highlighting the importance that these kinds of computing services have for FinTech professionals, given that the cloud allows scaling ML models to be used by hundreds or thousands of users.

Students will be introduced to Amazon Web Services (AWS) cloud platform and resources in this unit, and will learn to deploy ML models in the cloud and create conversational interfaces, such as robo advisors.

As a prelude for the rest of the unit, a demo of the homework is presented.

### Class Objectives

By the end of today's class, students will be able to:

* Recognize the differences between supervised and unsupervised machine learning.

* Apply the k-means algorithm to identify clusters on a given dataset.

* Diagnose what the data preprocessing tasks are that a dataset would need to apply the k-means algorithm.

* Demonstrate how the k-means algorithm is useful for customer segmentation.

* Speed up the machine-learning algorithms using principal component analysis.

* Understand the basic concepts of the cloud and Amazon Web Services.

* Describe the benefits of the cloud for FinTech professionals.

* Recognize the main features of Amazon SageMaker.

* Demonstrate how to run Jupyter notebooks in Amazon SageMaker Studio.

### Instructor Notes

* Students have learned the generalities of machine learning; they already know how to use supervised machine learning algorithms. Today's class offers an overview of unsupervised machine learning, where students will have hands-on experience using k-means on a business case scenario.

* Students will demonstrate how unsupervised machine learning could add value to business decision-making.

* While understanding unsupervised learning may be challenging, everyone is a customer and familiar with how companies use data to target customers or potential customers to offer products and services. Try to use analogies about how companies like [Amazon, Netflix, Google](https://www.pointillist.com/blog/customer-behavior-data/), or [Target](https://www.forbes.com/sites/kashmirhill/2012/02/16/how-target-figured-out-a-teen-girl-was-pregnant-before-her-father-did/) are using customer segmentation to provide customized offers, or [how Spotify is using segmentation](https://towardsdatascience.com/in-this-article-i-provide-a-detailed-analysis-of-spotify-as-a-company-music-industry-direction-eeb945d7257c) to improve its products and services.

* There are several theoretical aspects behind the k-means and PCA algorithms. Focus the class on the practical application of these algorithms for customer segmentation and share the additional references presented on the slides for those students interested in having a more in-depth understanding.

* The cloud is a core concept for FinTech professionals, but might be seen as complex and nebulous for some students. It's important to highlight how companies like Amazon Web Services have reduced the technological complexity behind the cloud by offering user-friendly interfaces that allow the deployment of a machine learning model with few lines of code and some mouse clicks.

* Because the homework demo is being presented today (Day 1), get familiar with the homework's solutions before class.

* Be sure to set the pace for the class. Encourage students to work with partners, and remind them to attend office hours if they feel lost or stuck.

* **Important!** Slack out the disclaimer for [AWS Free Tier](../Supplemental/AWS-Free-Tier.md) services at the end of today's class. Explain to students that while we are only using free tier services in the class, they should review this documentation to avoid accidentally incurring charges.

* Before class, make sure that all students have created their AWS account, and ask TAs to help troubleshoot any issues. If any students are unable to access a free tier account, ask that they pair up with a peer for this week.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [13.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=496c4888-8f12-4852-b593-aaed011cc667) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 min)

In this activity, students will learn about the cloud, its pros and cons, and why it is essential for FinTech professionals. Students will also be introduced to AWS and the particular services that will be used in this unit. The activity will be concluded with a short demo of the conversational interfaces that will be utilized in class.

Start by welcoming the class to Unit 13, and explain that it will be fun, as they'll be learning how to deploy ML models in the cloud using AWS. They will also create conversational interfaces to implement bots that will be able to understand and respond using natural language.

Open the lesson slides, navigate to the "Welcome to the Cloud and Amazon Web Services" section, and ask students the following question:

* What do you think the cloud is?

Take two or three answers from the class, and then hit on the following points:

* In essence, the cloud refers to the on-demand availability of computer systems resources.

* The computing resources may include data storage, computing power, and collaboration platforms.

* There is no need to have physical access to the hardware; it is managed through the internet using public or private networks.

* Normally, you pay as you go for what services you use (sometimes down to the second or byte) with little or no upfront costs.

* Cloud computing is usually cheaper due to the economics of scale (and no upfront cost of physical hardware, setup, or provisioning).

Explain to students that the cloud is a core tool for FinTech professionals; they will learn how to leverage their Python and ML skills using AWS to deploy models and business applications that could be reached by hundreds or thousands of people.

Continue with the slides and highlight the following points about the models of cloud services:

* There are multiple cloud services models, with trade-offs in responsibility and control. The most common are:

  * **Infrastructure as a service (IaaS):** Online services that provide APIs to access different infrastructures such as servers, virtual machines, storage, load balancers, or network interfaces (e.g., [Azure Virtual Machines](https://azure.microsoft.com/services/virtual-machines/)).

  * **Platform as a service (PaaS):** Provides a platform that allows customers to develop, run, and manage applications without the complexity of building and maintaining their physical infrastructure (e.g., [Amazon Web Services](https://aws.amazon.com/)).

  * **Software as a service (SaaS):** Refers to a software licensing and delivery model where software is licensed on a subscription basis and is centrally hosted (e.g., [Microsoft Office 365](https://www.office.com)).

  * **Function/code as a service (FaaS):** Also known as serverless computing, it offers a remote procedure call that enables the deployment of individual functions in the cloud that run in response to events (e.g., [AWS Lambda](https://aws.amazon.com/lambda/)).

* Clouds can be created in a private data center (private cloud), in a data center managed by a provider (public cloud) or as a combination of both (hybrid cloud).

* Cloud computing is considered secure enough to be used by many banks and government offices worldwide.

* Cloud services allow you to scale your resources up, or down, as required.

* There are multiple cloud service providers, including Amazon, Microsoft, Google, Oracle, and IBM.

Tell students that in spite of our trust in the cloud and its prevalence in our daily lives, it has some disadvantages that we should consider.

Continue with the slides and highlight the following disadvantages of the cloud:

* You have to trust a third-party provider with your data (encryption can address this).

* You probably have to give up some privacy and confidentiality.

* You depend on the service level agreements of a provider for issues to be addressed.

* Incidents such as hardware failure are inevitable, but you have less oversight on their resolution.

* Hardware might be shared with other tenants; "bad neighbours" can affect your resources.

* Clouds can fail and have downtime, including those due to planned maintenances out of your control.

Now, open your browser, navigate to the [Amazon Web Services](https://aws.amazon.com/) homepage and cover the following points:

* Launched in March 2006, AWS popularized the concept of cloud computing and pioneered the cloud's adoption.

* AWS comprises more than 140 services, including technologies for computing, storage, networking, database, analytics, IoT, machine learning, and more.

* AWS first launched in the Canada region in 2016, named `ca-central-1`.

* This allowed customers in Canada to offer cloud services compliant with Canadian cloud services regulations.

* Thousands of companies use AWS worldwide, [in Canada we have some relevant success stories with companies like](https://aws.amazon.com/canada/customer-success-stories/) The National Bank of Canada, the Toronto Star, The Globe and Mail, the Government of Ontario, and many more.

Slack out the following link to students if they want to learn more about AWS: [AWS Cloud Products](https://aws.amazon.com/products/)

Explain to students that in this unit, they will have hands-on experience with the following AWS services:

* **Amazon SageMaker:** To deploy ML models.
* **Amazon Lex:** To create conversational interfaces.
* **Amazon S3:** To store files in the cloud.
* **AWS Lambda:** To develop serverless applications.

Conclude this introduction by telling students that in this unit, they will create two chatbots using Amazon Lex and AWS Lambda.

1. A cryptocurrency converter.

    ![Crypto converveter](Images/crypto-converter-demo.gif)

2. An investment portfolio robo advisor.

   ![RoboAdvisor Demo](Images/robo-advisor-demo.gif)

Answer any questions before moving on.

---

### 2. Everyone Do: Running Jupyter Notebooks in the Cloud with Amazon SageMaker (30 min)

In this activity, students will learn about Amazon SageMaker and how to run Jupyter notebooks in the cloud with Amazon SageMaker Studio. After giving a short presentation on Amazon SageMaker using the lesson slides, you will guide students through how to get started on the cloud service with a collaborative demo.

**Files:**

* [monte_carlo.ipynb](Activities/01-Evr_Intro_SageMaker_Studio/monte_carlo.ipynb)

* [tickers_data.csv](Activities/01-Evr_Intro_SageMaker_Studio/Resources/tickers_data.csv)

Go to the "Running Jupyter Notebooks in the Cloud with Amazon SageMaker" section in the slideshow, and highlight the following:

* Amazon SageMaker is a platform service that allows software developers and data scientists to build, train, and deploy ML models in the cloud.

* Amazon SageMaker is composed of different tools aimed to ease the entire machine learning workflow, from managing datasets to building, training, and deploying a model.

* In this class, we will focus on gaining hands-on experience with Amazon SageMaker Studio. It's a web-based integrated development environment (IDE) that allows you to access all the services and tools needed to build, train, debug, deploy, and monitor your machine learning models.

* Amazon SageMaker provides some built-in ML algorithms, but also supports leading ML frameworks such as TensorFlow, PyTorch, Apache MXNet, Keras, and Scikit-learn.

* Some of the advantages of using Amazon SageMaker are the following:

  * Provides tools that streamline a typical workflow for creating an ML model.

  * Its infrastructure enables growth at scale, with on-demand compute instances and dynamic storage.

  * Building, training, and hosting is billed by the second, with no minimum fees and no upfront commitments.

  * Productivity may be boosted with One-Click Training and One-Click Deployment.

  * Provides built-in security, including access controls and monitoring.

Explain to students that learning how to train and deploy models with Amazon SageMaker is an in-demand skill that is worth learning.

Continuing with the slides, show students some companies that currently use Amazon SageMaker, highlighting the following:

* [**The Globe and Mail**](https://www.cantechletter.com/newswire/the-globe-and-mail-selects-aws-as-its-preferred-cloud-provider/) is using Amazon SageMaker to build models to retain existing customers and acquire new ones.

* [**Novartis**](https://aws.amazon.com/blogs/industries/aws-and-novartis-re-inventing-pharma-manufacturing/?cs=4) is currently using Amazon SageMaker to build a computer vision-based model that will determine production line clearance.

* Using Amazon SageMaker, engineers at [**Coinbase**](https://aws.amazon.com/machine-learning/customers/innovators/coinbase/?cs=3) developed a machine learning-driven system that recognizes mismatches and anomalies in sources of user identification, allowing them to take action against potential sources of fraud quickly.

Now, you will continue to demo how to get started with Amazon SageMaker Studio. Ask students to log-in to the [AWS Management Console](https://console.aws.amazon.com/) using their root user and to follow your steps throughout the process.

From the AWS Management Console, type `sagemaker` in the "Find Services" search box and choose `Amazon SageMaker` from the list.

![Launching Amazon SageMaker](Images/launching-sagemaker.png)

Explain to students that AWS currently offers Amazon SageMaker Studio as a generally available preview version from the US East (Ohio) AWS region. Since it's a preview version, some aspects of the user interface (UI) may vary over the time it's released as a final version.

Despite they are going to use a preview version, explain to students that it's is fully functional and can be used free of charge during its preview period.

On the Amazon SageMaker homepage, click on the "Amazon SageMaker Studio" button in the left menu to continue.

![Opening Amazon SageMaker Studio](Images/open-sagemaker-studio.png)

If you are not in the `US East (Ohio)` AWS region, you will see a warning message asking to switch to that region. Open the AWS regions list, select the `US East (Ohio)` AWS region, and click again on the "Amazon SageMaker Studio" option in the left menu.

![Switching to the US East (Ohio) AWS Region](Images/switching-to-ohio.gif)

Once you land on the Amazon SageMaker Studio homepage, explain to students that one of the main advantages of using this tool is that it deals with all the technical complexity of creating Amazon SageMaker instances. Creating instances is a process that implies to deploy some [Amazon EC2 instances (similar to virtual machines)](https://aws.amazon.com/ec2/) and several privacy settings; following a manual process may take a few hours.

Continue setting the initial configuration for Amazon SageMaker Studio; under the "Get Started" section, choose the "Quick Start" option and leave the default user name.

![Choosing the default user name for Amazon SageMaker Studio](Images/sagemaker-studio-user.png)

Next, in the "Execution role" option, click on the list box and choose "Create a new role"; a pop-up window named "Create an IAM role" will appear. Select "Any S3 bucket" under the "S3 buckets you specify" option, and click on the "Create role" button to continue.

![Create an execution role](Images/sagemaker-studio-execution-role.gif)

Continue the demo by clicking on the "Submit" button.

![Create an Amazon SageMaker Studio instance](Images/sagemaker-create-instance.png)

Next, the new instance of Amazon SageMaker Studio and the new user will be configured; you will be led to a new page where you may have to wait about five minutes.

![Amazon SageMaker Studio instance creation](Images/sagemaker-studio-instance-in-progress.png)

Once the Amazon SageMaker Studio instance is ready, you will see the following notification message. You may have to wait an additional minute or two until the Studio user is ready—after that, you will see the "Open Studio" link enabled.

![Amazon SageMaker Studio is ready](Images/sagemaker-studio-instance-ready.png)

Continue the demo by clicking on the "Open Studio" link. A new window (or tab) will be opened and you will see the following loading page until the UI of Amazon SageMaker Studio appears. **Note:** This process may take up to five minutes the first time.

![Loading Amazon SageMaker Studio](Images/sagemaker-studio-loading.png)

After the loading process ends, you will see the UI of Amazon SageMaker Studio. You may note that it is practically the same UI as Jupyter lab, but with a different colour scheme.

![The Amazon SageMaker Studio UI](Images/sagemaker-studio-ui.png)

Explain to students that Amazon SageMaker Studio can be used in the same way they were working locally with Jupyter lab; the main difference is that Studio is a cloud application that allows access to all the computing power of AWS.

Continue the demo by clicking the "Launcher" tab. Explain to students that Amazon SageMaker has different built-in images to create notebooks; these images are similar to a Python virtual environment. Make sure that the "Data Science" image is selected, and then click on the "Python 3" notebook option. A fresh Jupyter notebook will appear. Test it by printing a `Hello!!` message.

![Creating a notebook in Amazon SageMaker Studio](Images/sagemaker-studio-create-notebook.gif)

Ensure all students have reached this point, and that everyone was able to run this simple testing line of code. Ask TAs to assist any students that may be stuck.

Once everyone in the class has Amazon SageMaker Studio running, explain to students that like any Jupyter lab interface, they can run their notebooks and custom code in Amazon SageMaker Studio.

Now, tell students that you will show them how to import a local Jupyter notebook into Amazon SageMaker Studio.

Have your TAs slack out the `monte_carlo.ipynb` Jupyter notebook and the `tickers_data.csv` data file.

Continue the demo by importing the data file into Amazon SageMaker Studio. Click on the "New Folder" icon and create a new folder named `Data`; after creating the folder, import the `tickers_data.csv` file from your local drive.

![Loading a CSV file into Amazon SageMaker Studio](Images/sagemaker_studio_csv.gif)

Next, move to the root folder and import the `monte_carlo.ipynb` Jupyter notebook into Amazon SageMaker Studio.

![Loading a Jupyter notebook into Amazon SageMaker Studio](Images/sagemaker-studio-ipynb.gif)

Continue the demo by opening the Jupyter notebook and selecting the "Python 3 (Data Science)" kernel. Run all the cells of the notebook and explain that this notebook code runs a Monte Carlo simulation using the tickers data you imported and pure Python code; we are not using the built-in algorithms of Amazon SageMaker yet.

![Running an imported Jupyter notebook in Amazon SageMaker Studio](Images/sagemaker-studio-running-notebook.gif)

Ensure that all the students were able to run this notebook, and answer any questions before moving on.

---

### 3. Instructor Do: Introduction to Unsupervised Learning (10 min)

In this activity, students will be introduced to unsupervised learning and its most relevant applications.

Explain to students that you will now introduce a new family of machine learning algorithms that are used to deal with unlabeled data.

Open the lesson slides and go to the introduction of the "Unsupervised Learning" section.

Start the presentation by explaining to students that, in general terms, machine learning has two main areas of application: supervised and unsupervised learning.

Students will already be familiar with supervised learning algorithms and their applications from previous units. Highlight the main differences between these modes of learning.

| Supervised Learning                | Unsupervised Learning                      |
| ---------------------------------- | ------------------------------------------ |
| Input data is labelled             | Input data is unlabelled                    |
| Uses training datasets             | Uses just input datasets                   |
| **Goal:** Predict a class or value | **Goal:** Determine patterns or group data |

Start a short facilitated discussion with students. Ask the following question, taking a couple of answers from the class:

* If unsupervised learning deals with unlabelled data, what types of questions or business problems do you think we can solve?

  **Sample answer:** We can group customers on a retail chain by shopping habits, so we can send customized offers by email or mobile app to increase sales.

  **Sample answer:** We can use unsupervised learning to find patterns among transaction data to identify anomalies and potentially fraudulent transactions (such as on credit card operations with a large number of daily transactions, making it challenging to identify abnormal activity). 

  **Sample answer:** We can use unsupervised learning to cluster stock data so we can create investment portfolios according to the resulting groups.

Move to the slide titled "How can we understand our customers?" and highlight the following:

* One of the most important uses of unsupervised learning, not only in FinTech, but also in sectors such as marketing, entertainment, or retail, is customer segmentation.

* Beyond the typical segmentation variables, such as age, gender, income, or postal code, understanding customers is crucial in every sector.

* Supervised learning is very helpful at predicting the future based on labelled historical data; however, there are often situations where supervised learning is not feasible, due to lack of information or lack of training labels.

* Unsupervised learning allows us to cluster data to find hidden or unknown patterns that can be used to understand customers better. For example, developing a customized offer that responds to the needs identified in every group.

* The main applications of unsupervised learning are:

  * **Clustering:** It allows us to automatically split the dataset into groups according to similarity. It can be used for customer segmentation and targeting.

  * **Anomaly detection:** Automatically discovers unusual data points in a dataset. It is useful in identifying fraudulent transactions, locating broken pieces of hardware, or identifying an outlier caused by a human error during data entry.

* Customer segmentation is one of the most popular applications of unsupervised learning. It is the division of potential customers in a given market into discrete groups.

* Thanks to unsupervised learning algorithms, we can group customers based upon similarities such as:

  * Customer needs (e.g., a particular product can satisfy some of them)
  * Responses to online marketing channels
  * Buying habits (e.g., the best day for buying, weekly spend)

Explain to students that customer segmentation is driving revenue in leading companies such as Netflix and Amazon.

* 75% of Netflix viewer activity is driven by recommendation ([source](http://blog.springtab.com/personalization-examples-netflix/)).

* 35% of Amazon’s sales are generated through their recommendation engine ([source](https://www.martechadvisor.com/articles/customer-experience-2/recommendation-engines-how-amazon-and-netflix-are-winning-the-personalization-battle/)).

* Netflix’s recommendation system saves the company an estimated $1 billion per year through reduced churn ([source](https://dl.acm.org/citation.cfm?id=2843948)).

End the presentation with a closing facilitated discussion. Ask the following questions to students:

* How could a bank use customer segmentation to improve its products?

  **Sample answer:** Instead of having a generic offer for a credit card, a bank could use customer segmentation to offer credit cards according to demographics such as age, geography, gender, generation (e.g., millennials and baby boomers), income level, marital status, etc.

* How could an investment portfolio be improved using customer segmentation?

  **Sample answer:** Using customer segmentation, a portfolio can be categorized by industry, location, revenue, account size, and the number of employees, to reveal where risk and opportunity live within the portfolio. These patterns can provide critical measurable data for more predictive credit risk management.

Explain to students that in today's class, they will learn how to use Scikit-learn to implement clustering and customer segmentation.

Answer any questions before moving on.

---

### 4. Instructor Do: Data Preparation for Unsupervised Learning (10 min)

In this activity, students will learn about the data preparation considerations they should take into account before they start working with unsupervised learning algorithms.

**Files:**

* [Ins_Data_Preparation.ipynb](Activities/02-Ins_Data_Prep/Solved/Ins_Data_Preparation.ipynb)

* [credit_risk.csv](Activities/02-Ins_Data_Prep/Resources/credit_risk.csv)

Explain to students that data preparation for unsupervised learning does not differ much from the process for supervised learning problems.

Tell students that the main difference in preparing data for unsupervised learning is that its algorithms don't have target variables—only input features, which are used to find patterns in the data. So they should take care in selecting features that help find those patterns, or create groups.

Tell students that the current and following activities will be run in Amazon SageMaker Studio so they may gain hands-on experience with this cloud application.

Import the `credit_risk.csv` data file into the `Data` folder in Amazon SageMaker Studio.

![Importing the credit risk data into Amazon SageMaker Studio](Images/sagemaker-studio-risk-data.gif)

Import the unsolved version of the Jupyter Notebook to Amazon SageMaker Studio, then open the notebook and select the `Python 3 (Data Science)` kernel.

![Importing the unsolved version of the Jupyter notebook](Images/sagemaker-studio-risk-ipynb.gif)

Live code the demo and highlight the following:

* To get started with unsupervised learning, we will use a credit risk dataset, where the risk level for each person is labelled as `low`, `medium`, or `high`.

* The columns in the dataset are as follows:

  * `age`: The age of the person.

  * `deb_ratio`: Monthly debt payments, alimony, and living costs divided by monthly gross income.

  * `monthly_income`: Monthly gross income.

  * `dependents`: The number of dependents of each person.

  * `gender`: The gender of the person.

  * `risk`: The risk level for each person.

* The first step is to load the data into a Pandas DataFrame. Note that we are not using the `path` module to define the route to the CSV file, since this module is not installed by default in Amazon SageMaker.

  ![Lading the credit risk dataset](Images/load-credit-risk-data.png)

* In forthcoming activities, the risk level of each person will be computed using unsupervised learning, so the next step is to remove the `risk` column, since it is not needed.

  ![Removing the risk column](Images/drop-risk-column.png)

Explain to students that all the variables in the dataset should be numerical to fit the unsupervised learning algorithms, so we need to transform any categorical data or non-numeric features. In this demo, we must change the `male` and `female` categorical values into numeric representations.

Explain to students that we may use the `LabelEncoder` from scikit-learn; however, we will perform a manual encoding this time using the `encodeGender()` function.

```python
def encodeGender(gender):
    """
    This function transforms the gender expressed in text into a numerical representation.
    """
    if gender.lower() == "male":
        return 1
    else:
        return 0
```

After defining the `encodeGender()` function, we encode the `gender` column using the `apply()` method from Pandas.

```python
clean_df["gender"] = clean_df["gender"].apply(encodeGender)
clean_df.head()
```

![Credit risk DataFrame with the encoded gender column](Images/encoded-gender.png)

Explain to students that it's recommended to have all the numerical features in the same scale, so in this demo, the `StandardScaler` from scikit-learn is used to scale the data.

```python
# Create the scaler instance
data_scaler = StandardScaler()

# Fit the scaler with the DataFrame's values
data_scaler.fit(clean_df.values)

# Scale the data
scaled_data = data_scaler.transform(clean_df.values)
```

After scaling the data, explain to students that the data is transformed into a DataFrame to be saved as a CSV file for further use.

![Creating a DataFrame with the scaled data and saving it as a CSV file](Images/saving-scaled-credit-risk-data.png)

Ask the class if there are any further questions before moving to the next activity.

---

### 5. Student Do: Understanding Customers (15 min)

In this activity, students will perform data preparation tasks on a dataset containing data from purchases on an ecommerce website made by 200 customers. Students will use this dataset on further activities to find customer segments.

Some data transformations should be made to the dataset, so ask TAs to assist students if there are any questions about why the following changes are needed.

* **Annual Income:** This feature should be regularized since it is on a different scale than the other features; dividing by `1000` is the simplest solution.

* **Gender:** The `Gender` should be transformed to a numerical value; in this case, transforming `Male` to `1` and `Female` to `0` is a feasible solution.

* **CustomerID:** Since this column is not relevant to the clustering algorithm, it should be dropped from the DataFrame.

**Instructions:**

* [README.md](Activities/03-Stu_Preparing_Data/README.md)

**Files:**

* [preparing_data.ipynb](Activities/03-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

* [shopping_data.csv](Activities/03-Stu_Preparing_Data/Resources/shopping_data.csv)

---

### 6. Instructor Do: Review Understanding Customers (10 min)

**Files:**

* [preparing_data.ipynb](Activities/03-Stu_Preparing_Data/Solved/preparing_data.ipynb)

* [shopping_data.csv](Activities/03-Stu_Preparing_Data/Resources/shopping_data.csv)

* [shopping_data_cleaned.csv](Activities/03-Stu_Preparing_Data/Resources/shopping_data_cleaned.csv)

Load the provided `shopping_data.csv` data file in Amazon SageMaker Studio into a folder called `Data`.

![Loading the shopping data into Amazon SageMaker Studio](Images/sagemaker-studio-shopping-data.gif)

In the root folder of Amazon SageMaker Studio, load the unsolved version of the Jupyter notebook `preparing_data.ipynb`. Open the Jupyter notebook and select the `Python 3 (Data Science)` kernel.

![Importing the unsolved version of the Jupyter notebook](Images/sagemaker-studio-shopping-ipynb.gif)

Live code the solution and highlight the following:

* Unsupervised learning algorithms only work with numerical data, so checking data types is an important task to ensure that numerical values were loaded to the DataFrame with the appropriate data type.

  ![Data types check](Images/datatypes-check.png)

* All columns, but `Gender`, have a numeric data type. So we will only need to encode the `Gender` column.

* The `CustomerID` column can be dropped; it is not relevant for clustering since it does not denote any important characteristics of customer shopping habits.

  ```python
  df_shopping.drop(columns=["CustomerID"], inplace=True)
  ```

* Looking for `null` values and duplicate entries is part of any data preprocessing workflow; there are no `null` values nor duplicates on this DataFrame, so no additional adjustments are needed.

* The `Gender` column is categorical, so it should be transformed into numerical values. Turning `Male` to `1` and `Female` to `0` is a common practice.

  ```python
  def encodeGender(gender):
      if gender.lower() == "Male":
          return 1
      else:
          return 0

  df_shopping["Gender"] = df_shopping["Gender"].apply(encodeGender)
  ```

* The `Annual Income` column is on a different scale than the other columns, so this column should be rescaled. Dividing by `1000` is the most straightforward approach.

  ```python
  df_shopping["Annual Income"] = df_shopping["Annual Income"] / 1000
  ```

* Finally, the cleaned DataFrame is saved as a `CSV` file for being used in future activities.

  ```python
  file_path = "Data/shopping_data_cleaned.csv"
  df_shopping.to_csv(file_path, index=False)
  ```

Be sure that there are no questions before moving forward.

---

### 7. BREAK (15 min)

---

### 8. Instructor Do: The K-Means Algorithm (15 min)

In this activity, students will learn how the k-means algorithm works. Use your time wisely to cover the theoretical portion, as well as the coding portion.

**Files:**

* [Ins_K-Means.ipynb](Activities/04-Ins_KMeans/Solved/Ins_K-Means.ipynb)

* [new_credit_risk.csv](Activities/04-Ins_KMeans/Resources/new_credit_risk.csv)

Open the lesson slides and move to the K-Means Algorithm section; go through the slides and highlight the following.

* To understand how k-means works, a fictional anecdote is used.

  > Imagine that you are in a room full of spheres (data points), and you want to learn more about them, so you start to observe.
  >
  > You realize that every sphere represents a flower, and that axes represent features of flowers. After observing the flowers, you discover that there are some patterns when you combine the three features.
  >
  > We can see that spheres (data points) with similar features seem to be closer together than data points with dissimilar features. We can use this spatial information to group similar data points together.

Explain to students that k-means is an unsupervised learning algorithm used to identify clusters and solve clustering issues.

Continue on the slides to formally introduce k-means, and highlight the following:

* The k-means algorithm groups the data into `k` clusters, where each piece of data is assigned to a cluster based on some similarity or distance measure to a **centroid**.

* A centroid represents a data point that is the arithmetic mean position of all the points on a cluster.

* At a glance, the k-means algorithm works as follows:

  1. Randomly initialize the `k` starting centroids.
  2. Each data point is assigned to its nearest centroid.
  3. The centroids are recomputed as the mean of the data points assigned to the respective cluster.
  4. Repeat steps `1` through `3` until the stopping criteria is triggered.

* One of the key tasks using k-means is to find the best number for `k`. In other words, `k` determines how many clusters or groups best represent the data.

* The **elbow curve** is the most common method used to figure out the best value of `k`.

* On the elbow curve, the `x` axis is the value of `k`, while the `y` axis is the value of some objective function.

* The **inertia** that is the sum of squared distances of samples to their closest cluster center is commonly used as an objective function.

* Visually, the best number for `k` is the `k` value, where the curve turns like an elbow.

* Analytically, using the inertia, we choose as the best `k` the `k` value where adding more clusters only marginally decreases the inertia.

Reassure students that while this may sound complex, k-means is quite simple to implement using Python.

Close the presentation, switch to Amazon SageMaker Studio, and upload the unsolved version of the Jupyter notebook.

![Uploading the unsolved version of the Jupyter notebook](Images/sagemaker-studio-risk-kmeans.gif)

Open the unsolved Jupyter Notebook, select the `Python 3 (Data Science)` kernel and live code the demo by highlighting the following:

![Opening the started notebook and select the Python 3 Data Science kernel](Images/sagemaker-studio-risk-kmeans-kernel.gif)

* This demo uses the data from the risk level dataset presented before.

* The k-means algorithm is imported from the `sklearn` library.

  ```python
  from sklearn.cluster import KMeans
  ```

* After the data is loaded in a DataFrame, the first step is to create an instance of the k-means algorithm and initialize it with the desired number of clusters (K). For this demo, we will use `k = 3`, since we already know we have three classes of risk levels.

  ```python
  model = KMeans(n_clusters=3, random_state=5)
  ```

* Once the model instance is created, the next step is to fit the model with the unlabeled data. When the model is being trained (fit to the data), the k-means algorithm will iteratively look for the best centroid for each of the `k` clusters.

  ```python
  model.fit(df_risk)
  ```

* After the model is fit, the corresponding cluster for every risk level in the dataset can be found using the `predict()` method.

  ![K-Means predictions](Images/kmeans-predictions-risk.png)

Explain to students that, as they can see, three classes were found, labelled as `0`, `1`, and `2`. Make it clear to students that naming the classes is part of the job done by a subject matter expert; the k-means algorithm is just able to identify how many clusters are in the data and label them with numbers.

Continue the demo by adding a new column to the DataFrame with the predicted risk levels, and explain to students that the predicted classes are in the `labels_` attribute of the model.

![Adding predicted classes](Images/adding-classes-column.png)

* Visualizing the clusters helps to understand how they are arranged graphically. In this case, we have too many features to represent visually, but we can take two of them to plot the clusters.

  ![Visualizing the clusters by plotting two Features](Images/plotting-2d.png)

Continue the live coding demo by showing students how the best value for `k` can be found; highlight the following:

* Two lists are created to store the values for the `inertia` and to define how many values of `k` we want to try. Ten values of `k` is usually a good number to start.

  ```python
  inertia = []
  k = list(range(1, 11))
  ```

* A `for-loop` is defined to fit the k-means model with the data from `df_risk` and a number of clusters ranging from 1 to 10. The `inertia` is fetched in each iteration to be compared to the elbow curve.

  ```python
  # Looking for the best k
  for i in k:
      km = KMeans(n_clusters=i, random_state=0)
      km.fit(df_risk)
      inertia.append(km.inertia_)
  ```

* The elbow curve is plotted using the `plot()` method of Pandas, so a DataFrame is created.

  ```python
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)
  df_elbow.plot.line(x="k", y="inertia", title="Elbow Curve", xticks=k)
  ```

* As can be seen on the elbow curve, visually, the best value for `k` is `3`.

  ![Elbow Curve](Images/elbow-curve.png)

Answer any questions before moving on.

---

### 9. Student Do: Customer Segments for E-Commerce (20 min)

In this activity, students will identify the best number of clusters on a customer clustering scenario using the elbow curve. Next, students will use k-means to cluster data and make conclusions about the obtained results.

**Instructions:**

* [README.md](Activities/05-Stu_K_Means_In_Action/README.md)

**Files:**

* [k_means_in_action.ipynb](Activities/05-Stu_K_Means_In_Action/Unsolved/k_means_in_action.ipynb)

* [shopping_data_cleaned.csv](Activities/05-Stu_K_Means_In_Action/Resources/shopping_data_cleaned.csv)

---

### 10. Instructor Do: Review Customer Segments for E-Commerce (10 min)

**Files:**

* [k_means_in_action.ipynb](Activities/05-Stu_K_Means_In_Action/Solved/k_means_in_action.ipynb)

* [shopping_data_cleaned.csv](Activities/05-Stu_K_Means_In_Action/Resources/shopping_data_cleaned.csv)

In the root folder of Amazon SageMaker Studio, load the unsolved version of the Jupyter notebook `k_means_in_action.ipynb`. Open the Jupyter notebook and select the `Python 3 (Data Science)` kernel.

![Importing the unsolved version of the Jupyter notebook](Images/sagemaker-studio-customers-ipynb.gif)

Live code the solution and highlight the following:

* This activity uses the customer shopping data that was preprocessed earlier.

  ```python
  file_path = "Data/shopping_data_cleaned.csv"
  df_shopping = pd.read_csv(file_path)
   ```

* The elbow curve is used to find the best value for `k`. A `for-loop` is used to loop ten times, fitting the k-means model and fetching the `inertia` to create the plot.

  ```python
  inertia = []
  k = list(range(1, 11))

  # Calculate the inertia for the range ok k values
  for i in k:
      km = KMeans(n_clusters=i, random_state=0)
      km.fit(df_shopping)
      inertia.append(km.inertia_)
  ```

* The elbow curve is created using the `plot()` method from Pandas.

  ```python
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)
  df_elbow.plot.line(x="k", y="inertia", xticks=k, title="Elbow Curve")
  ```

Explain to students that, after observing the elbow curve, they may conclude that the best two values for `k` are `5` and `6`, since at those points, the elbow shape starts.

![elbow curve](Images/elbow-curve-customers.png)

* The `get_clusters()` function is a mechanism to encapsulate the k-means clustering algorithm to be reused. The value of `k` and the `data` where the clusters are going to be identified are passed as parameters.

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

* A visual analysis of using k-means with `k=5` and `k=6` is done by creating a 2-D scatter plot, as well as a 3-D, scatter plot.

  Scatter plot with `k=5`.
  ![2D Scatter k=5](Images/2d-scatter-k5.png)

  Scatter plot with `k=6`.
  ![2D Scatter k=6](Images/2d-scatter-k6.png)

* After visually analyzing the clusters, the best value for `k` seems to be `6`. A value of `k=6`, allows to define more meaningful segmentation of customers as follows:

  * _Cluster 1_: Medium income, low annual spend
  * _Cluster 2_: Low income, low annual spend
  * _Cluster 3_: High income, high annual spend
  * _Cluster 4_: Low income, high annual spend
  * _Cluster 5_: Medium income, low annual spend
  * _Cluster 6_: Very high income, high annual spend

* Having defined these clusters, we can formulate marketing strategies relevant to each cluster aimed to increase revenue.

Encourage one or two students to share their conclusions and answer any questions before moving on.

---

### 11. Instructor Do: Speeding Up Machine Learning Algorithms with PCA (10 min)

In this activity, students will learn how to use Principal Component Analysis (PCA) as a technique to speed up ML algorithms by reducing the number of input features.

**Files:**

* [Ins_PCA.ipynb](Activities/06-Ins_PCA/Solved/Ins_PCA.ipynb)

Open the lesson slides and move to the "Speeding Up ML Algorithms with PCA" section and highlight the following:

* There are some machine learning problems where the number of input features (or dimensions) is too high, for example, in the order of tens or thousands of features.

* Working with too many variables may be complex and could lead to slow down ML algorithms computing.

* PCA is a statistical technique that reduces the number of input features (or dimensions) of a dataset by creating a smaller number of dimensions that represent the underlying structure of the data.

* The dimensions created by PCA are called principal components.

* A principal components represent data points where there is a significant variance, and the data is most spread out.

Explain to students that we are not going to deal with the mathematical complexity of PCA, the most crucial fact that they have to remember is that PCA is used to reduce the number of input features. As a result, ML algorithms computing may speed-up.

Close the presentation, switch to Amazon SageMaker Studio and upload the unsolved version of the Jupyter notebook. Next, open the notebook, select the `Python 3 (Data Science)` kernel and live code the demo by highlighting the following:

![Loading the unsolved Jupyter notebook](Images/sagemaker-studio-ins-pca.gif)

* Scikit-learn offers a class to compute PCA, you just need to import `PCA` from the `sklearn.decomposition` module.

  ```python
  from sklearn.decomposition import PCA
  ```

* For this demo, we will use the `new_credit_risk.csv` data file that we created before.

  ![Loading the credit risk data](Images/sagemaker-studio-pca-data.png)

* Before start using the PCA algorithm, it's essential to scale the data. We don't need to scale the data for this demo since we already scaled before, but keep in mind that this is crucial for the PCA algorithm to work.

* To start using this algorithm, a `PCA` model should be created specifying the final number of features in the `n_components` parameter. In this demo, the features will be reduced from `5` to `2` and the `random_state` parameter is set to `0` to allow model reproducibility.

  ```python
  pca = PCA(n_components=2, random_state=0)
  ```

* After creating the PCA model, we apply dimensionality reduction on the scaled dataset.

  ```python
  risk_pca = pca.fit_transform(df_risk)
  ```

Explain to students that after dimensionality reduction, we get as a result a smaller set of dimensions, these dimensions are the **principal components**. There isn’t a particular meaning assigned to each principal component; the new components are just the two main dimensions of variation that contains most of the information in the original dataset.

* The resulting principal components, are transformed into a DataFrame to be used next to fit the k-means algorithm. You can see that principal component values have no direct relationship with the values in the original dataset. They can be seen as a reduced representation of the original data.

  ![PCA Data](Images/pca-df.png)

Explain to students that dimensionality reductions imply a loss of accuracy; however, the trick is to sacrifice a little accuracy for simplicity. Smaller datasets are more comfortable to explore and visualize. They ease data analysis and speed up machine-learning algorithms without extraneous variables to process.

* To know how much information can be attributed to each principal component, the explained variance ratio is used.

  ![Explained variance](Images/explained-variance.png)

Explain to students that in this demo, after using the attribute `explained_variance_ratio_`, they can see that the first principal component contains `23.73%` of the variance, and the second principal component contains `20.45%` of the variance. Both components together contain `44.18%` of the information.

* The elbow curve is generated using the principal components data. You can see that the resulting best value for `k` is `3`. Despite some accuracy loss due to dimensionality reduction, the results are still good enough.

  ![PCA Elbow Curve](Images/pca-elbow-curve.png)

* The k-means algorithm is used to predict the clusters for the credit risk data. But now, the principal components data is used with `k=3`.

  ```python
  # Initialize the K-Means model
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(df_risk_pca)

  # Predict clusters
  predictions = model.predict(df_risk_pca)
  ```

* Finally, the clusters are plotted. Now they are easier to analyze since we have only two features.

  ![Clusters plot](Images/pca-clusters-plot.png)

Answer any questions before moving on.

---

### 12. Student Do: PCA in Action (15 min)

In this activity, students will use PCA to reduce the dimensions of the consumers' shopping dataset.

**Instructions:**

* [README.md](Activities/07-Stu_PCA/README.md)

**Files:**

* [06_Stu_PCA.ipynb](Activities/07-Stu_PCA/Unsolved/Stu_PCA.ipynb)

* [shopping_data_cleaned.csv](Activities/07-Stu_PCA/Resources/shopping_data_cleaned.csv)

---

### 13. Instructor Do: Review PCA in Action (10 min)

**Files:**

* [06_Stu_PCA.ipynb](Activities/07-Stu_PCA/Solved/Stu_PCA.ipynb)

* [shopping_data_cleaned.csv](Activities/07-Stu_PCA/Resources/shopping_data_cleaned.csv)

In the root folder of Amazon SageMaker Studio, load the unsolved version of the Jupyter notebook `Stu_PCA.ipynb`. Open the Jupyter notebook and select the `Python 3 (Data Science)` kernel.

![Importing the unsolved version of the Jupyter notebook](Images/sagemaker-studio-pca-stu.gif)

Live code the solution and highlight the following:

* Before using PCA, the features' values on the `df_shopping` DataFrame are standardized using the `StandardScaler` library from `sklearn`.

  ```python
  # Create the scaler instance
  data_scaler = StandardScaler()

  # Fit the scaler with the DataFrame's values
  data_scaler.fit(df_shopping.values)

  # Scale the data
  shopping_scaled = data_scaler.transform(df_shopping.values)
  ```

* PCA is used to reduce the number of features from `4` to `2`.

  ```python
  # Initialize PCA model
  pca = PCA(n_components=2, random_state=0)

  # Get two principal components for the data.
  shopping_pca = pca.fit_transform(shopping_scaled)
  ```

Explain to students that according to the explained variance, the first principal component contains `44.3%` of the variance and the second principal component contains `33.3%` of the variance. We have `77.6%` of the information in the original dataset so that we may have a valid representation of the original data from the principal components.

![Explained variance with two PCs](Images/explained-variance-2pcs.png)

* The k-means algorithm is fit with the principal components data to predict the clusters. A value of `k=6` is used, as this was the best value in the previous exercise using the elbow curve.

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

* Finally, a scatter plot is created to visualize the clusters using the PCA data. It can be seen that the six clusters are easy to visualize and understand.

  ![Clusters plot](Images/pca-data-plot.png)

Explain to students that the power of PCA to speed up machine-learning algorithms is more noticeable when you are dealing with a dataset that has tens or hundreds of features. For datasets up to ten features, PCA adds value to simplify data analysis and visualization.

Answer any questions before ending the class.

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
