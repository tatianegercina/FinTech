## 13.2 Lesson Plan—Deploying ML Models with SageMaker

### Overview

In today's class, students will continue working with Amazon Web Services (AWS) and will learn how to leverage some cloud computing services for machine learning using Amazon SageMaker Studio.

### Class Objectives

By the end of class, students will be able to:

* Describe the pros and cons of using cloud services to deploy machine-learning models.

* Orchestrate a cloud solution by combining different AWS services.

* Understand how Amazon SageMaker Studio can be used to deploy machine-learning models.

### Instructor Notes

* Slack out the [Deep Learning Installation Guide](../../14-Deep-Learning/Supplemental/deep_learning_installation_guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* This lesson introduces new content rapidly. Students may express frustration at learning new cloud technologies. Remind students that while the learning curve may be steep at first, AWS and cloud experience is highly sought-after and well worth the effort required to become comfortable with it.

* Note that in the past, AWS content has appeared differently for some instructional teams. It seems that AWS does A/B testing on their UI. If your AWS views _don’t_ match up with the views in the lesson plan, check that you've pulled the latest updates from GitHub or look in the Slack Instructional Team channel for announcements regarding this.

* Check prior to class that all students have an AWS account and are able to log in.

* Today's class should be a fun one. Students will put together many different technologies covered so far and learn how they can interact with cloud services.

* There are a few activities that require setup. Have the class follow along and ask questions as you go.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [13.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=30a703ee-9c5d-497a-9348-aaee016135c6) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome the class to day 2 of Unit 13, this should be a fun one since students will go deeper into using AWS to deploy ML models.

Open the lesson slides and review the class objectives. Continue to the "AWS Free Tier" section and highlight the following:

* Throughout this unit, we will use the free tier of AWS as well as the trial period for some of the services.

* The details of the services that we will use in class can be seen in the following table.

  | Amazon SageMaker (Free Trial)                                                    | Amazon Lex (12 Months Free)       | AWS Lambda (Always Free)                              | Amazon S3 (12 Months Free) |
  | -------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------- | -------------------------- |
  | `250` hours per month of `t2.medium` notebook usage for the first **two months** | `10,000` text requests per month  | `1,000,000` free requests per month                   | `5` GB of Standard Storage |
  | `50` hours per month of `m4.xlarge` for training for the first **two months**    | `5,000` speech requests per month | Up to `3.2` million seconds of compute time per month | `20,000` Get Requests      |
  | `125` hours per month of `m4.xlarge` for hosting for the first **two months**    |                                   |                                                       | `2,000` Put Requests       |

* As you can see, Amazon SageMaker offers a two-months free trial. This period starts the day you launch your first notebook or instance in this service, so if you have never used Amazon SageMaker before, your trial period started in the past class.

* Amazon Lex and Amazon S3 are free to use for one year as long as you don't overpass the limits of each service.

* In the case of AWS Lambda, it's always free if you pull less than `1,000,000` requests and you use les that  `3.2` million seconds ofr compute time per month. This limits are usually enough for testing purposes.

Slack out the following resources to be used as a future reference, and encourage students to keep updated of the Free Tier limits by visiting the AWS Free Tier documentation.

* [AWS Free Tier Supplemental](../Supplemental/AWS-Free-Tier.md)

* [AWS Free Tier Documentation](https://aws.amazon.com/free)

Answer any questions before moving on.

---

### 2. Everyone Do: Creating an Administrator User on IAM (15 min)

In this activity, students will learn how to create an `administrator` user using AWS Identity and Access Management (IAM) service. This will add some extra security when working on AWS. This is a collaborative activity where students should follow your steps throughout the process, so be sure to keep the pace of the activity and ask TAs to assist those students who may be stuck.

Explain to students that a common best practice is to avoid using the principal or root user to manage an AWS account. The root user is the one they used to create their AWS account and the same user they use in Day 1.

Highlight to students that usually a new user should be created for each person that requires administrative access to the services of managed by an AWS root account, especially in corporate environments.

Explain to students, that AWS provides a service called Identity and Access Management (IAM) service to create and manage users.

Open the [AWS Management Console](https://console.aws.amazon.com) using your root user, ask to students to do the same to follow you in the process of creating a new user in IAM.

Once all the students opened their AWS Management Console, explain to students that now you will create an `administrator` user that will have permissions to administer all the AWS services; this user may look redundant with the root user, however, if the access credentials of this new `administrator` user get compromised, you can block it or recreate the password to secure your services without compromising your root users.

Continue the demo and highlight the following:

* Start by looking for the IAM service on the Find Services search box, type `iam`, and click on IAM service.

  ![Create an administrator IAM user - Step 1](Images/iam-user-1.png)

* In the IAM start page, you may note that this service is marked as `Global` in the upper right corner, this means that IAM users can access AWS resources in any AWS Region. In the left pane menu, choose the "Users" option to continue.

  ![Create an administrator IAM user - Step 2](Images/iam-user-2.png)

* In the Users start page, click on the "Add user" button to continue.

  ![Create an administrator IAM user - Step 3](Images/iam-user-2_bis.png)

* On the _Add user_ page, fill out the details of the new `administrator` user and click on the "Next: Permissions" button to continue.

  * **User name:** `administrator`
  * **Access type:** Select the "Programmatic access" and "AWS Management Console access" boxes.
  * **Console password:** Choose "Custom password" and type a password you may remember.
  * **Require password reset:** Uncheck this box.

  ![Create an administrator IAM user - Step 3](Images/iam-user-3.png)

* On the "Set permissions" page, choose "Add user to group" and click on the "Create group" button.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4.png)

* In the "Create group" dialog box, type `Administrators` on the "Group name" textbox.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4_bis.png)

* Click on "Filter policies" and then choose "AWS managed - job function" to filter the policies table content.

  ![Create an administrator IAM user - Step 5](Images/iam-user-5.png)

* In the policy list, select the checkbox for AdministratorAccess. Then choose the _Create group_ button.

  ![Create an administrator IAM user - Step 6](Images/iam-user-6.png)

* After creating the group, select the checkbox for your new group. Choose Refresh if necessary to see the group on the list.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7.png)

* Click on the "Next: Tags" button to continue.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7_bis.png)

* On the "Add Tags" page, leave the defaults and click on the "Next: Review" button to continue.

  ![Create an administrator IAM user - Step 8](Images/iam-user-8.png)

* Review the list of group memberships to be added to the new user. When you are ready to proceed, click on the "Create user" button.

  ![Create an administrator IAM user - Step 9](Images/iam-user-9.png)

* Once the user is created, download the user's credentials by clicking on the "Download .csv" button. Keep these credentials safe.

  ![Create an administrator IAM user - Step 10](Images/iam-user-10.png)

Explain to students that now you should enable access to billing data for the new IAM administrator user, proceed as follows:

* On the navigation bar, click on your account name and then choose "My Account".

  ![Create an administrator IAM user - Step 11](Images/iam-user-11.png)

* In the next page, scroll down to the "IAM User and Role Access to Billing Information" section, and click on the _Edit_ option.

  ![Create an administrator IAM user - Step 12](Images/iam-user-12.png)

* Check the option "Activate IAM Access" and click on the "Update" button to finish.

  ![Create an administrator IAM user - Step 13](Images/iam-user-13.png)

Explain to students that now, they should sign out from their current session with their root user to start using their new `administrator` user.

![Create an administrator IAM user - Step 14](Images/iam-user-14.png)

Next, ask to students to open the `CSV` file with the new `administrator` user credentials they downloaded before and highlight the following:

* In the `CSV` file, you will find a custom login link that you need to use to access the AWS Management Console with your `administrator` user.

  ![Create an administrator IAM user - Step 15](Images/iam-user-15.png)

* Copy the custom login link and paste it on your browser to open the custom login page. Type `administrator` as the "IAM user name" and the password you choose before. Click on the "Sign in" button to continue.

  ![Create an administrator IAM user - Step 16](Images/iam-user-16.png)

* Now you are logged-in into the AWS Management Console with your brand new IAM user. You may note that the IAM user name appears in the upper right conner followed by your AWS account ID.

  ![Create an administrator IAM user - Step 17](Images/iam-user-17.png)

Explain to students that from now on, they should avoid using their "root user" and work with this new administrator user instead.

Answer any questions before moving on.

---

### 3. Instructor Do: Intro to the Amazon Simple Storage Service (Amazon S3) (15 min)

In this activity, students will learn how the Amazon S3 works and its importance for running ML models in Amazon SageMaker. Students will also learn how to create private and public Amazon S3 buckets.

**Files:**

* [public-happy-face.png](Activities/01-Ins_Intro_S3/Solved/public-happy-face.png)

* [private-wink-face.png](Activities/01-Ins_Intro_S3/Solved/private-wink-face.png)

Be sure that you are logged-in using your new `administrator` IAM user before starting this activity.

Explain to students that AWS offers a service to store files in the cloud that is called Amazon Simple Storage Service or Amazon S3.

Open the AWS Management Console, in the "Find Services" search box type `s3` and select `S3` from the services list.

![Launching Amazon S3 from the AWS Management Console](Images/amazon-s3-launch.png)

Explain to students that you will demo how they can use Amazon S3 and highlight the following.

* Amazon S3 stores the files in a container that is called "Bucket".

* You can have as many buckets as you want, but you must be cautious when defining the access permissions, since you can have public and private buckets.

* When you create a bucket, you can choose the AWS Region where you want to store your data. Depending on the region, different user data privacy legislation may apply.

* You may note that you already have a bucket, it was created by Amazon SageMaker Studio in Day 1 when you configured your Amazon SageMaker Studio instance.

  ![Current bucket in Amazon S3](Images/amazon-s3-getting-started.png)

* Note that this bucket can have public objects and it's on the `US East (Ohio)` AWS Region since that is the current region where the Amazon SageMaker Studio preview is available.

* You can have public or private buckets in Amazon S3. You will use private buckets to store the prediction results of the ML models that your will create in Amazon SageMaker Studio, and public buckets to store some files that we will use in the next. class.

* To create a new bucket, click on the "Crete bucket" button.

  ![Creating a new Amazon S3 bucket](Images/amazon-s3-create-new-bucket.png)

* In the "Create bucket" page, first you need to define a new for your bucket. Bucket's names are unique across all the Amazon S3 space, so AWS checks the uniqueness of the name you typed before creating it.

* We will start by creating a private bucket to store the prediction results for our ML models.

* As the "Bucket name" type the `sm-models` followed by the current timestamp, for example `sm-models-20200330-1244`. You should select the `US East (Ohio)` AWS Region since the Amazon S3 buckets and the Amazon SageMaker Studio instance should be in the same region.

  ![Setting the Amazon S3 bucket's name and region](Images/amazon-s3-name-region.png)

* To define a private bucket, you should check the "Block all public access" option. Click on the "Create bucket" button to continue.

  ![Setting private access to the Amazon S3 bucket](Images/amazon-s3-private-access.png)

* Now, on the Amazon S3 console, note that your new bucket has been created and it has `Not Public` access.

* Adding files to a bucket is easy. Click on the name of your new bucket, next click on the "Upload" button and add the file you want to store in the bucket. Continue by clicking on the "Upload" button and you are done.

  ![Uploading a file to the private Amazon S3 bucket](Images/amazon-s3-private-file-upload.gif)

Explain to students that if they click on the file name, they will see the file's properties.

![Private file properties in Amazon S3](Images/amazon-s3-private-file-properties.gif)

Continue the demo by highlighting the following:

* If you click on the "Object URL", you may note that you can't see the image we uploaded, this is because this object is private.

  ![Opening a private objet URL](Images/amazon-s3-private-file-url.gif)

* Now let's create a public bucket. You need to return to the Amazon S3 console, you may click on the "Amazon S3" link.

  ![Moving back to the Amazon S3 console](Images/amazon-s3-back-to-home.png)

* From the Amazon S3 Console, click on the "Create bucket" button.

* We will name the public bucket as `public-share` followed by the current timestamp, for example `public-share-20200330-1326`. For this bucket, we will choose the `Canada (Cental)` AWS Region.

  ![Setting the name and region for the public Amazon S3 bucket](Images/amazon-s3-public-bucket-name-region.png)

* In the "Bucket settings for Block Public Access" section, uncheck the "Block all public access" option and be sure that all the options bellow are unchecked.

  ![Setting public access to the Amazon S3 bucket](Images/amazon-s3-settting-public-access.png)

* Note that you will see a warning message stating that you are about to make the buckets and its object available to the public. Check the acknowledge notice and click on the "Create bucket" button to continue.

Explain to students that it's okay to have public bucket, but they have to be careful about the files the share as public since they will be available to any person in the Internet.

Continue the demo by uploading a file to the new public bucket, you have a happy face icon in the `Solved` folder of this activity that you can use.

![Uploading a file to the public Amazon S3 bucket](Images/amazon-s3-upload-public-file.gif)

Next, explain to students that the file you uploaded is not public yet, first you need to set the particular access for that file public for everyone.

Click on the file name, next, click on the "Permissions" tab. Under the "Public access" section, choose "Everyone" and check the "Read object" property; save the changes and go back to the "Overview" tab to open the object's URL to see a nice happy face.

![Setting access to everyone to a particular file](Images/amazon-s3-set-everyone-access.gif)

Explain to students that a public Amazon S3 bucket, may contain private or public files depending on the particular permissions you particularly set to the objects or the AWS IAM policies you define.

Answer any questions before moving on.

---

### 4. Students Do: Creating Amazon S3 Buckets (15 min)

**Instructions:**

* [README.md](Activities/02-Stu_Practice/README.md)

**Files:**

* [starter-code.js](Activities/02-Stu_Practice/Unsolved/starter-code.js)

---

### 5. Instuctor Do: Review Creating Amazon S3 Buckets (10 min)

**Files:**

* [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Walk through the solution and highlight the following:

* Something really important

---

### 6. Everyone Do: Intro to Amazon SageMaker Built-in Algorithms (30 min)

In this activity, students will learn how a machine-learning model is created, trained, deployed, and evaluated in Amazon SageMaker.

**Files:**

* [rainfall_forecast.ipynb](Activities/03-Ins_SageMaker_Deployment/Unsolved/rainfall_forecast.ipynb)

* [x_austin_final.csv](Activities/03-Ins_SageMaker_Deployment/Resources/x_austin_final.csv)

* [y_austin_final.csv](Activities/03-Ins_SageMaker_Deployment/Resources/y_austin_final.csv)

Explain to students that Amazon has actually created an extensive library of machine-learning models that are optimized for the cloud. This demo will show how to use one of those models.

Tell students that in this demo, you are going to deploy one of Amazon's linear regression models to predict the amount of rain that will fall in Austin, given the average temperature in degrees Fahrenheit.

Start the demo by opening the Jupyter lab UI at your Amazon SageMaker instance, and create a new folder called `Data`.

![Deploy SageMaker Model - step 1](Images/deploy-sagemaker-1.png)

Open the `Data` folder, and upload the following `CSV` files:

* `x_austin_final.csv`, this file contains historical weather conditions in Austin, Texas, over 1,319 days.

* `y_austin_final.cvs`, this file contains the precipitation sums in inches in Austin, Texas, over 1,319 days.

![Deploy SageMaker Model - step 2](Images/deploy-sagemaker-2.png)

Navigate to the main folder on Jupyter lab, and import the unsolved version of the Jupyter Notebook to your Amazon SageMaker notebook instance. Live code the demo by highlighting the following:

* In the `Initial imports` section, some well-known libraries are imported. `sklearn` library is used to split the dataset in training and testing sets and to evaluate the model.

  ```python
  import os
  import io
  import json
  import numpy as np
  import pandas as pd
  from path import Path
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import mean_squared_error, r2_score
  ```

* To use Amazon SageMaker, the following libraries are needed.

  ```python
  import sagemaker
  import sagemaker.amazon.common as smac
  from sagemaker.predictor import csv_serializer, json_deserializer
  from sagemaker import get_execution_role
  from sagemaker.amazon.amazon_estimator import get_image_uri
  import boto3
  ```

* Along with the `sagemaker` modules, the `boto3` library is imported; this is [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

* The data to train and test the model is loaded into two Pandas DataFrames. Next, the data is transformed into a vector as follows:

  * The `x_austin_final.csv` data is loaded into the `features` DataFrame. Next, the `TempAvgF` column, which denotes the average temperature in Austin in degrees Fahrenheit, is taken as an input variable (predictor) for the linear model.

    ```python
    # Read the weather features data
    file_path = Path("Data/x_austin_final.csv")
    features = pd.read_csv(file_path)

    # Transforming the "TempAvgF" column to a vector
    X = features["TempAvgF"].values.reshape(-1, 1)
    ```

    * The `y_austin_final.csv` data is initially loaded into the `y` DataFrame; this data represents the target variable in the linear model.

      ```python
      # Read the target data (precipitation sum inches)
      file_path = Path("Data/y_austin_final.csv")
      y = pd.read_csv(file_path, names=["PrecipitationSumInches"], header=None)

      # Transforminf y into a vector
      y = y.iloc[:, 0].values
      ```

* The data is split into training and testing datasets using the `train_test_split()` function from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  ```

Tell students that once the data is loaded, the next step is to create the linear regression model. The process starts with some initial configurations as follows:

* The training and testing data should be stored in an Amazon S3 bucket, so a variable to store the name of the bucket we created before is defined.

  ```python
  bucket = "sagemaker-bucket-name-here"
  ```

* To identify the data files stored in Amazon S3, a prefix is defined.

  ```python
  prefix = "austin-rainfall-regression"
  ```

* The current role of the IAM user running the notebook is stored in the `role` variable.

  ```python
  role = get_execution_role()
  ```

Now it's time to upload the data to Amazon S3. Explain to students that in order to train the machine-learning model using Amazon SageMaker, the training and testing data should pass through an Amazon S3 bucket formatted using the [protobuf recordIO format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html#td-serialization).

* The profobuf recordIO format, is a method to serialize structured data (similar to `JSON`), to allow different applications to communicate with each other or for storing data.

Explain to students that using the profobuf recordIO format allows you to take advantage of **Pipe mode** when training the algorithms that support it. In Pipe mode, your training job streams data directly from Amazon S3. Streaming can provide faster start times for training jobs and better throughput.

Continue with the following code to format the training data as a protobuf recordIO and upload it to the Amazon S3 bucket.

```python
# Encode the training data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_train).astype("float32")
labels = np.array(Y_train).astype("float32)
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded training data to Amazon S3
key = 'linear_train.data'
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "train", key)).upload_fileobj(buf)
s3_train_data = "s3://{}/{}/train/{}".format(bucket, prefix, key)
print("Training data uploaded to: {}".format(s3_train_data))
```

Tell students that if you provide test data, the algorithm logs include the test score for the final model. Live code the following to upload the testing data.

```python
# Encode the testing data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_test).astype("float32")
labels = np.array(Y_test).astype("float32")
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded testing data to Amazon S3
key = "linear_test.data"
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "test", key)).upload_fileobj(buf)
s3_test_data = "s3://{}/{}/test/{}".format(bucket, prefix, key)
print("Testing data uploaded to: {}".format(s3_test_data))
```

Once you have uploaded your data to Amazon S3, it is time to train the machine-learning model. Tell students that in this demo, you will use the Amazon SageMaker's [linear learner algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) to run a linear regression prediction model.

Create the instance of the linear learner algorithm and highlight the following:

* The instance of the `linear learner` is created using the `get_image_uri()` method from the `sagemaker` library.

  ```python
  container = get_image_uri(boto3.Session().region_name, "linear-learner")
  ```

* Before creating the estimator container, an Amazon SageMaker's session should be started.

  ```python
  sess = sagemaker.Session()
  ```

* The estimator container is an AWS EC2 instance that will store and run the model. The estimator container is created using a `ml.m4.xlarge` train instance type.

  ```python
  linear = sagemaker.estimator.Estimator(
    container,
    role,
    train_instance_count=1,
    train_instance_type="ml.m4.xlarge",
    output_path="s3://{}/{}/output".format(bucket, prefix),
    sagemaker_session=sess
    )
  ```

* The linear learner hyperparameters are defined next. Highlight that the `feature_dim` parameter should match with the number of predictors in `X`; in this case, since we only have one predictor, its value is `1`.

  ```python
  # Define linear learner hyperparameters
  linear.set_hyperparameters(
    feature_dim=1,
    mini_batch_size=100,
    predictor_type="regressor",
    epochs=10,
    num_models=32,
    loss="absolute_loss"
    )
  ```

* The model is trained using the `fit` method of the Amazon SageMaker estimator. Note: This step might take a few minutes.

  ```python
  linear.fit({'train': s3_train_data, 'test': s3_test_data})
  ```

Explain to students that this step might take a few minutes, and it will use resources from the AWS account. Normally, this time is not billed in the two-month trial period, however, clarify to students that policies of AWS free and trial offers constantly changes, so they should always check the pricing pages for any service that they want to use. Below, a sample output is shown. You will notice that the text is in red, but this does not denote an error.

![Deploy SageMaker Model - step 3](Images/deploy-sagemaker-3.gif)

Once the `linear-learner` model has been trained, tell students that it can be deployed to make predictions of the rainfall in Austin. Continue the demo and highlight the following:

* An instance of the linear-learner predictor is created. Note: This step might take a few minutes.

  ```python
  linear_predictor = linear.deploy(initial_instance_count=1, instance_type="ml.m4.xlarge")
  ```

* Some configurations are made to specify the type of data files that are going to be used and to define how the data is going to be serialized and deserialized.

  ```python
  linear_predictor.content_type = 'text/csv'
  linear_predictor.serializer = csv_serializer
  linear_predictor.deserializer = json_deserializer
  ```

* Some predictions are made using the testing data; results are stored on the `y_predictions` array.

  ```python
  result = linear_predictor.predict(X_test)
  y_predictions = np.array([r["score"] for r in result["predictions"]])
  ```

Explain to students that once you have the predictions, the model can be evaluated using the techniques they already know. First, a plot to contrast the predicted rainfall values versus the real values is created.

![Deploy SageMaker Model - step 4](Images/deploy-sagemaker-4.png)

* Additionally, the `RMSE` and `R2` scores are calculated.

  ![Deploy SageMaker Model - step 5](Images/deploy-sagemaker-5.png)

  Finally, after reviewing the model evaluation's results, explain to students that the endpoint needs to be deleted to avoid additional AWS resources usage and extra billing.

```python
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
```

Slack out the following page to students, where they can learn more about the different Amazon SageMaker built-in algorithms.

* [Use Amazon SageMaker Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

Answer any questions before moving on.

---

### 7. BREAK (15 min)

---

### 8. Student Do: Credit Risk Evaluation with Amazon SageMaker (20 min)

In this activity, students will train and deploy a binary classification model to predict the credit risk of a person using the [German Credit Risk dataset](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) and the SageMaker built-in `Linear Learner` algorithm.

This activity will require the use of an AWS SageMaker notebook instance. The unsolved notebook will guide students through the process and indicate what the missing code snippets are.

**Instructions:**

* [README.md](Activities/05-Stu_Credit_Risk_Classification/README.md)

**Files**:

* [credit-risk-classification.ipynb](Activities/05-Stu_Credit_Risk_Classification/Unsolved/credit-risk-classification.ipynb)

* [german_credit_data.csv](Activities/05-Stu_Credit_Risk_Classification/Resources/german_credit_data.csv)

---

### 9. Instructor Do: Review Credit Risk Evaluation with Amazon SageMaker (10 min)

* Open JupyterLab in your AWS SageMaker notebook instance.

* Upload the dataset: [german_credit_data.csv](Activities/05-Stu_Credit_Risk_Classification/Resources/german_credit_data.csv).

* Upload the solved notebook: [credit-risk-classification.ipynb](Activities/05-Stu_Credit_Risk_Classification/Solved/credit-risk-classification.ipynb).

* Walk through the solved notebook, cell by cell, highlighting the following points:
  * This activity is similar to the previous Housing Price Prediction; however, rather than `linear regression`, we are calculating a `logistic regression` to perform a `binary classification`.
  * The output of the model prediction is a binary label (0, 1): "good" or "bad" credit risk.
  * Despite using a curated dataset, we still need to perform some data preparation tasks: split, hot-encode, and scale the input features.
  * Similar to the housing price prediction, we use the AWS SageMaker built-in `linear-learner` algorithm but change the hyper-parameter `predictor_type` to `binary_classifier`.
  * Unlike with housing price prediction, the predictions are in the `predicted_label` field in the prediction result.
  * For our model evaluation, besides the accuracy score, we use a confusion matrix to get a quick sense of the model's true-positive or negative and false-positive or negative prediction combinations.

Answer any questions before moving on.

---

### 10. Everyone Do: Deleting AWS Resources (15 min)

In this activity, students will learn how to delete their Amazon SageMaker notebook instance so that no billing charges are incurred for it after class.

Open the Amazon SageMaker console, on the left pane menu, under the Notebook section, click on Notebook instances.

![Deleting Amazon SageMaker instance - 1](Images/deleting-sm-1.png)

Select the `sm-test` notebook instance on the left circular dot. Once selected, click on the right Actions menu and select Stop.

*![Deleting Amazon SageMaker instance - 2](Images/deleting-sm-2.png)*

Refresh the page and wait for the instance `Status` to change to `Stopped`. Note: This process will take a few minutes.

![Deleting Amazon SageMaker instance - 3](Images/deleting-sm-3.png)

Select the instance again on the left circular dot, click on Actions and select Delete then confirm the delete.

![Notebook Instance delete](Images/notebook-confirm-delete.png)

* At the end of today's lesson, the notebook instances list should be empty and state: "There are currently no resources." Otherwise, charges will be incurred for any remaining active instances.

Lastly, go to the Amazon S3 console and remove the buckets created for the activity as follows.

* Choose the checkbox next to the bucket name, next click on the Delete button.

![Deleting Amazon SageMaker instance - 4](Images/deleting-sm-4.png)

* On the Delete bucket window, type the name of the bucket to confirm that you want to delete it. Next, click on the Confirm button to finish.

![Deleting Amazon SageMaker instance - 5](Images/deleting-sm-5.png)

Answer any questions before moving on.

---

### 11. Instructor Do: Pros and Cons of Deploying Machine Learning Models with Amazon SageMaker (10 min)

Lead and facilitate a discussion around deploying models in Amazon SageMaker and why a RESTful ML API is useful.

Have students share their opinions with the class and bring up the following points:

**Pros:**

* Data storage capacity: By using an Amazon S3 bucket to store the data, we could have trained a model on multiple terabytes of data, or a lot more space than would fit in our personal computer.

* Hardware/GPU: By using different Amazon SageMaker instances to train our model, we can access compute power, including GPU capabilities, making powerful hardware available to us as required.

* Cost: Using AWS resources, we only pay for what we use. We will turn off everything before ending the class and not incur further charges.

* Availability: By deploying our model to another Amazon SageMaker instance, we have made the prediction functionality available 24/7 through a secure endpoint to an application or to be consumed by others without having to make our computer available.

* RESTful API: As learned in previous units, APIs provide a standard mechanism to access data. Our machine-learning API can be consumed through apps and other channels in a simple form while remaining secure and allowing other constraints (authentication, authorization, rate limiting, etc.).

**Cons:**

* Data privacy and security: By uploading data to a third party, you are trusting your data to them. Certain kinds of data are subject to compliance and regulatory constraints.

* Visibility: You will not have oversight on AWS internal handling of your data and infrastructure.

* Unavailability: Although there are service-level agreements in place, AWS (and any other cloud provider) can and has suffered outages at times, causing data unavailability.

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
