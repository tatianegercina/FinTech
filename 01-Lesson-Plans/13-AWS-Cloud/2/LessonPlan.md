## 13.2 Lesson Plan—Deploying ML Models with SageMaker

### Overview

In today's class, students will be introduced to some Amazon Web Services (AWS) tools and will learn how to leverage some cloud computing services for machine learning using Amazon SageMaker.

### Class Objectives

By the end of class, students will be able to:

* Describe the pros and cons of using cloud services to deploy machine-learning models.

* Orchestrate a cloud solution by combining different AWS services.

* Understand how Amazon SageMaker works and how it can be used to deploy machine-learning models.

### Instructor Notes

* This lesson introduces new content rapidly. Students may express frustration at learning new cloud technologies. Remind students that while the learning curve may be steep at first, AWS and cloud experience is highly sought-after and well worth the effort required to become comfortable with it.

* **Important!** Slack out the disclaimer for [AWS Free Tier](../Supplemental/AWS-Free-Tier.md) services prior to class. Take some time at the beginning of class to explain that while we are only using free tier services in class; students should review this documentation in order to avoid accidentally incurring charges.

* Note that in the past, AWS content has appeared differently for some instructional teams. It seems that AWS does A/B testing on their UI. If your AWS views _don’t_ match up with the views in the lesson plan, check that you've pulled the latest updates from GitHub or look in the Slack Instructional Team channel for announcements regarding this.

* Check prior to class that all students have an AWS account and are able to log in.

* Today's class should be a fun one. Students will put together many different technologies covered so far and learn how they can interact with cloud services.

* There are a few activities that require setup. Have the class follow along and ask questions as you go.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome class to day 2 of Unit 13, this should be a fun one since students will go deeper into using AWS to deploy machine -earning models.

Explain to students that throughout this unit, we will use the free tier of AWS as well as the trial period for some of the services. Slack out the following resources to be used as reference to understand how the free offer of AWS works.

* [AWS Free Tier Supplemental](../Supplemental/AWS-Free-Tier.md)

* [AWS Free Tier Documentation](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23ai-ml)

Open the [AWS Free Tier Supplemental](../Supplemental/AWS-Free-Tier.md) and briefly explain to students the limits we will have for the services they will learn in this unit.

| Amazon SageMaker (Free Trial)                                                    | Amazon Lex (12 Months Free)       | AWS Lambda (Always Free)                              | Amazon S3 (12 Months Free) |
| -------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------- | -------------------------- |
| `250` hours per month of `t2.medium` notebook usage for the first **two months** | `10,000` text requests per month  | `1,000,000` free requests per month                   | `5` GB of Standard Storage |
| `50` hours per month of `m4.xlarge` for training for the first **two months**    | `5,000` speech requests per month | Up to `3.2` million seconds of compute time per month | `20,000` Get Requests      |
| `125` hours per month of `m4.xlarge` for hosting for the first **two months**    |                                   |                                                       | `2,000` Put Requests       |

Answer any questions before moving on.

### 2. Instructor Do: Creating an Administrator User on IAM (10 min)

In this activity, students will learn how to create an `administrator` user using AWS Identity and Access Management (IAM) service. This will add some extra security when working on AWS.

Explain to students that a common best practice is to avoid using the principal or root user to manage an AWS account. This principal user is the one they used to create the AWS account. A new user for each person that requires administrator access should be created using the AWS Identity and Access Management (IAM) service.

Open the [AWS Management Console](https://console.aws.amazon.com) using your root user, and show students how to create a new user on IAM as follows:

* Look for the IAM service on the Find Services search box, type `iam`, and click on IAM service.

  ![Create an administrator IAM user - Step 1](Images/iam-user-1.png)

* In the left pane menu, choose the _Users_ option and click on the _Add user_ button.

  ![Create an administrator IAM user - Step 2](Images/iam-user-2.png)

* On the _Add user_ page, fill out the details of the new `administrator` user and click on the _Next: Permissions_ button to continue.

  * **User name:** `administrator`
  * **Access type:** Select the _Programmatic access_ and _AWS Management Console access_ boxes.
  * **Console password:** Choose _Custom password_ and type your own password.
  * **Require password reset:** Unselect this box.

  ![Create an administrator IAM user - Step 3](Images/iam-user-3.png)

* On the _Set permissions_ page, choose _Add user to group_ and click on the _Create group_ button.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4.png)

* In the Create group dialog box, type `Administrators` on the _Group name_ textbox.

* Choose _Filter policies_, and then choose _AWS managed - job function_ to filter the table contents.

  ![Create an administrator IAM user - Step 5](Images/iam-user-5.png)

* In the policy list, select the check box for AdministratorAccess. Then choose the _Create group_ button.

  ![Create an administrator IAM user - Step 6](Images/iam-user-6.png)

* After creating the group, select the check box for your new group. Choose Refresh if necessary to see the group in the list.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7.png)

* Click on the _Next: Tags_ button to continue.

* On the _Next: Tags_ page, leave the defaults and click on the _Next: Review_ button to continue.

  ![Create an administrator IAM user - Step 8](Images/iam-user-8.png)

* Review the list of group memberships to be added to the new user. When you are ready to proceed, click on the _Create user_ button.

  ![Create an administrator IAM user - Step 9](Images/iam-user-9.png)

* Once the user is created, download the user's credentials by clicking on the _Download .csv_ button. Keep those credentials safe.

  ![Create an administrator IAM user - Step 10](Images/iam-user-10.png)

Enable access to billing data for the IAM admin user as follows:

* On the navigation bar, choose your account name, and then choose My Account.

  ![Create an administrator IAM user - Step 11](Images/iam-user-11.png)

* Scroll down to the _IAM User and Role Access to Billing Information_ section, and click on the _Edit_ option.

  ![Create an administrator IAM user - Step 12](Images/iam-user-12.png)

* Select the check box to _Activate IAM Access_ and choose _Update_.

  ![Create an administrator IAM user - Step 13](Images/iam-user-13.png)

Sign out from your session, open the `CSV` file with the new `administrator` user credentials and login into the AWS Management Console using the user's URL and password. Tell students that from now on, they should avoid using their _root user_ and work with this new admin user instead.

Answer any questions before moving on.

---

### 3. Student Do: Creating an Administrator User on IAM (10 min)

In this activity, students will create an administrator user to manage their AWS account.

**Instructions:**

* [README.md](Activities/01-Stu_IAM_User/README.md)

---

### 4. Instructor Do: Review Creating an Administrator User on IAM (10 min)

This review activity is intended to verify that all students have successfully created their admin user using IAM.

Make sure all students have their AWS account working properly. Ask TAs to assist students who could have any issue before moving forward. Forthcoming activities will use the `administrator` IAM user by default.

Answer any questions before moving on.

---

### 5. Student Do: Creating an Amazon SageMaker Notebook Instance (20 min)

In this activity, students will learn how to create an instance of Amazon SageMaker and how to use Jupyter notebooks on the AWS cloud.

**Files:**

* [monte_carlo.ipynb](Activities/02-Evr_SageMaker/Solved/monte_carlo.ipynb)

Tell students that you will demo how to create an Amazon SageMaker notebook Instance, and ask them to follow your steps as you move along the demo. Ask TAs to assist students if they get stuck along the process.

Login into your AWS Management Console using your admin user. Tell students that the first component that Amazon SageMaker requires is an [Amazon S3](https://aws.amazon.com/s3) bucket to store data to feed machine-learning models or to store prediction results.

To create an Amazon S3 bucket, follow the next steps:

* On the Find Services search box, type `s3` and select the S3 service from the list.

  ![Creating an Amazon SageMaker instance - step 1](Images/sagemaker-1.png)

* On the Amazon S3 console, click on the Create bucket button.

  ![Creating an Amazon SageMaker instance - step 2](Images/sagemaker-2.png)

* Fill the following details on the Create button window.

  * **Section: Name and region**
    * Bucket name: `sagemaker-<CURRENT-DATE+TIME>` (for example: `sagemaker-20190903-1026`)
    * Region: `US West (Oregon)` (S3 and SageMaker instance regions should be the same)
    * Click: Next
    ![Creating an Amazon SageMaker instance - step 3](Images/sagemaker-3.png)
  * **Section: Configure options**
    * Click: Next (leave defaults)
    ![Creating an Amazon SageMaker instance - step 4](Images/sagemaker-4.png)
  * **Section: Set permissions**
    * Click: Next (leave defaults)
    ![Creating an Amazon SageMaker instance - step 5](Images/sagemaker-5.png)
  * **Section: Review**
    * Click: Create bucket
    ![Creating an Amazon SageMaker instance - step 6](Images/sagemaker-6.png)

* Note down (copy/paste/save) the name of bucket for use in the following section.

Explain to students that the next step is to create a Jupyter Notebook instance on Amazon SageMaker. Follow the next steps.

* Navigate to the AWS Management Console homepage. On the Find Services search box, type `sagemaker` and select Amazon SageMaker from the list.

  ![Creating an Amazon SageMaker instance - step 7](Images/sagemaker-7.png)

* On the Amazon SageMaker console, be sure that `Oregon` is the selected region, on the left pane menu, under Notebook section choose Notebook instances.

  ![Creating an Amazon SageMaker instance - step 8](Images/sagemaker-8.png)

* On the Notebook instances page, click on the Create notebook instance button.

  ![Creating an Amazon SageMaker instance - step 9](Images/sagemaker-9.png)

* Fill in the following values on the Create notebook instance page:

  * **Section: Notebook instance settings**
    * Notebook instance name: `sm-test`
    * Notebook instance type: `ml.m4.xlarge`
    * Elastic Inference: `none`
    ![Creating an Amazon SageMaker instance - step 10](Images/sagemaker-10.png)
  * **Section: Permissions and encryption**
    * IAM role: On the dropdown list select the `Create a new role` option.
    ![Creating an Amazon SageMaker instance - step 11](Images/sagemaker-11.png)
    * Under the S3 buckets you specify - optional section, choose Specific S3 buckets and type the name of the Amazon S3 bucket you created in the past section (e.g., `sagemaker-20190903-1026`), click on Create role to continue.
    ![Creating an Amazon SageMaker instance - step 12](Images/sagemaker-12.png)
    * Root access: Be sure that the `Enable - Give users root access to the notebook` option is selected. Tell students, that this option is less safe but allows more control over the instance.
    ![Creating an Amazon SageMaker instance - step 13](Images/sagemaker-13.png)

* Scroll down, and click on the Create notebook instance button to continue. Comment to students that the creations process takes few minutes to finish.

  ![Creating an Amazon SageMaker instance - step 14](Images/sagemaker-14.png)

While the notebook instance is being created, explain to students that AWS charges for these and most resources when they are created, even when not in use. This instance is billed for by the second until it's turned off and deleted. Students will learn how to delete these resources later in today's class.

* Once the notebook instance status is InService, it's ready to be used; in the Actions column, click on `Open JupyterLab` to continue.

  ![Creating an Amazon SageMaker instance - step 15](Images/sagemaker-15.png)

* After few seconds you will see the Jupyter Lab UI. Tell students that this notebook is running on the AWS cloud.

* On the Notebook section in the JupyterLab Launcher, select the `conda_python3` environment to create a new notebook.

  ![Creating an Amazon SageMaker instance - step 16](Images/sagemaker-16.png)

* On the new notebook, code a `hello world` statement in Python in the first cell as a test. Be sure that all of the class has reached this point before moving forward.

  ![Creating an Amazon SageMaker instance - step 17](Images/sagemaker-17.png)

Explain to students that it's possible to code a Jupyter Notebook from scratch on this Amazon SageMaker's notebook instance, but they can also open an existing Jupyter Notebook. Slack out to students the `monte_carlo.ipynb` starter file, and continue the demo as follows.

* This demo code runs a Monte Carlo simulation that uses the IEX API, so ask students to have their API key at hand.

* In your Amazon SageMaker notebook instance, in left icon menu, click on the Upload icon (arrow up) and select the `monte_carlo.ipynb` notebook to upload.

  ![Creating an Amazon SageMaker instance - step 18](Images/sagemaker-18.png)

* Open the `monte_carlo.ipynb` notebook. You'll probably see the message: `Select Kernel` or `Kernel not found`, select `conda_python3` and click on `Select` or `Set Kernel` to continue.

  ![Creating an Amazon SageMaker instance - step 19](Images/sagemaker-19.png)

* Run all the cells on the notebook. Tell students that now this notebook is going to run on the AWS cloud using Amazon SageMaker.

  ![Creating an Amazon SageMaker instance - step 20](Images/sagemaker-20.gif)

End the demo and answer any questions before moving on.

---

### 6. Instructor Do: Creating and Deploying a Machine Learning Model in Amazon SageMaker (15 min)

In this activity, students will learn how a machine-learning model is created, trained, deployed and evaluated in Amazon SageMaker.

**Files:**

* [rainfall_forecast.ipynb](Activities/03-Ins_SageMaker_Deployment/Unsolved/rainfall_forecast.ipynb)

* [x_austin_final.csv](Activities/03-Ins_SageMaker_Deployment/Resources/x_austin_final.csv)

* [y_austin_final.csv](Activities/03-Ins_SageMaker_Deployment/Resources/y_austin_final.csv)

Explain to students that Amazon has actually created an extensive library of machine-learning models that are optimized for the cloud. This demo will show how to use one of those models.

Tell students that in this demo, you are going to deploy one of Amazon's linear regression models to predict the amount of rain that will fall in Austin given the average temperature in degrees Fahrenheit.

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

* The data to train and test the model is loaded into two Pandas DataFrames. Next, the data is transformed to a vector as follows:

  * The `x_austin_final.csv` data is loaded into the `features` DataFrame. Next, the `TempAvgF` column, which  denotes the average temperature in Austin in degrees Fahrenheit, is taken as input variable (predictor) for the linear model.

    ```python
    # Read the weather features data
    file_path = Path("Data/x_austin_final.csv")
    features = pd.read_csv(file_path)

    # Transforming the "TempAvgF" column to a vector
    X = features["TempAvgF"].values.reshape(-1, 1)
    ```

    * The `y_austin_final.csv` data is initially loaded into the `y` DataFrame; this data represent the target variable in the linear model.

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

* To identify the data files stores in Amazon S3, a prefix is defined.

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

Once you have uploaded your data to Amazon S3, it's time to train the machine-learning model. Tell students that in this demo, you will use the Amazon SageMaker's [linear learner algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) to run a linear regression prediction model.

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

Explain to students that this step might take few minutes and it will use resources from the AWS account. Normally, this time is not billed in the two-month trial period, however, clarify to students that policies of AWS free and trial offers constantly changes, so they should always check the pricing pages for any service that they want to use. Below, a sample output is shown. You will notice that text is in red, but this does not denote an error.

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
  
  Finally, after reviewing the model evaluation's results, explain to students that the end point needs to be deleted to avoid additional AWS resources usage and extra billing.

```python
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
```

Slack out the following page to students, where they can learn more about the different Amazon SageMaker built-in algorithms.

* [Use Amazon SageMaker Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

Answer any questions before moving on.

---

### 7. Student Do: Deploying a Housing Price Prediction Model in Amazon SageMaker (20 min)

In this activity, students will calculate a linear regression model to predict the price of a house using the Boston Housing dataset and the SageMaker built-in `Linear Learner` algorithm.

**Instructions:**

* [README.md](Activities/04-Stu_Housing_Price/README.md)

**Files**:

* [boston-housing-regression.ipynb](Activities/04-Stu_Housing_Price/Unsolved/boston-housing-regression.ipynb)

---

### 8. Instructor Do: Review Deploying a Housing Price Prediction Model in Amazon SageMaker (10 min)

**Files**:

* [boston-housing-regression.ipynb](Activities/04-Stu_Housing_Price/Solved/boston-housing-regression.ipynb)

Reassure students that it's OK if this was challenging. Amazon SageMaker APIs have a learning curve, as do other AWS resources, along with machine learning in general. Tell students that they will get a lot of practice with AWS today!

Walk through the solution and highlight the following:

* The data is fetched and analyzed to become familiar with it.

* The data is split into test and train datasets and converted into to the [RecordIO-wrapped ProtoBuf format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html) used by Amazon SageMaker's algorithms.

* The prepared and formatted data is uploaded to an Amazon S3 bucket.

* The model is trained using a linear learner algorithm using the data stored in Amazon S3.

* The trained model is deployed on an Amazon SageMaker instance.

* Predictions are performed and the model's performance is scored.

Answer any questions before moving on.

---

### 9. Break (15 min)

---

### 10. Instructor Do: Pros and Cons of Deploying Machine Learning Models with Amazon SageMaker (10 min)

Lead and facilitate a discussion around deploying models in Amazon SageMaker and why a RESTful ML API is useful.

Have students share their opinions with the class and bring up the following points:

**Pros:**

* Data storage capacity: By using an Amazon S3 bucket to store the data, we could have trained a model on multiple terabytes of data, or a lot more space than would fit in our personal computer.

* Hardware/GPU: By using different Amazon SageMaker instances to train our model, we can access compute power, including GPU capabilities, making powerful hardware available to us as required.

* Cost: Using AWS resources, we only pay for what we use, we'll turn off everything before ending the class and not incur in further charges.

* Availability: By deploying our model to another Amazon SageMaker instance, we have make the prediction functionality available 24/7 through a secured endpoint to an application or to be consumed by others without having to make our computer available.

* RESTful API: As learned in previous units, APIs provide a standard mechanism to access data. Our machine-learning API can be consumed through apps and other channels in a simple form while remaining secure and allowing other constraints (authentication, authorization, rate limiting, etc.).

**Cons:**

* Data privacy and security: By uploading data to a third party, you are trusting your data to them. Certain kinds of data are subject to compliance and regulatory constraints.

* Visibility: You won't have oversight on AWS internal handling of your data and infrastructure.

* Availability: Although there are service-level agreements in place, AWS (and any other cloud provider) can and has suffered outages at times, causing data unavailability.

---

### 11. Student Do: Credit Risk Evaluation with Amazon SageMaker (20 min)

In this activity, students will train and deploy a binary classification model to predict the credit risk of a person using the [German Credit Risk dataset](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) and the SageMaker built-in `Linear Learner` algorithm.

This activity will require use of an AWS SageMaker notebook instance, the unsolved notebook will guide students through the process and indicate what the missing code snippets are.

**Instructions:**

* [README.md](Activities/05-Stu_Credit_Risk_Classification/README.md)

**Files**:

* [credit-risk-classification.ipynb](Activities/05-Stu_Credit_Risk_Classification/Unsolved/credit-risk-classification.ipynb)

* [german_credit_data.csv](Activities/05-Stu_Credit_Risk_Classification/Resources/german_credit_data.csv)

---

### 12. Instructor Do: Review Credit Risk Evaluation with Amazon SageMaker (10 min)

* Open JupyterLab in your AWS SageMaker notebook instance.

* Upload the dataset: [german_credit_data.csv](Activities/05-Stu_Credit_Risk_Classification/Resources/german_credit_data.csv).

* Upload the solved notebook: [credit-risk-classification.ipynb](Activities/05-Stu_Credit_Risk_Classification/Solved/credit-risk-classification.ipynb).

* Walk through the solved notebook, cell by cell, highlighting the following points:
  * This activity is similar the previous Housing Price Prediction; however, rather than `linear regression` we're calculating a `logistic regression` to perform a `binary classification`.
  * The output of the model prediction is a binary label (0, 1): "good" or "bad" credit risk.
  * Despite using a curated dataset, we still need to perform some data preparation tasks: split, hot-encode and scale the input features.
  * Similar to the housing price prediction, we use the AWS SageMaker built-in `linear-lerner` algorithm but change the hyper-parameter `predictor_type` to `binary_classifier`.
  * Unlike with housing price prediction, the predictions are in the `predicted_label` field in the prediction result.
  * For our model evaluation, besides the accuracy score, we use a confusion matrix to get a quick sense of the model's true-positive or negative and false-positive or negative prediction combinations.

Answer any questions before moving on.

---

### 13. Instructor Do: Delete Notebook Instance (10 min)

In this activity, students will learn how to delete their Amazon SageMaker notebook instance so that no billing charges are incurred for it after class.

Open the Amazon SageMaker console, on the left pane menu, under the Notebook section, click on Notebook instances.

![Deleting Amazon SageMaker instance - 1](Images/deleting-sm-1.png)

Select the `sm-test` notebook instance on the left circular dot. Once selected, click on the right Actions menu and select Stop.

*![Deleting Amazon SageMaker instance - 2](Images/deleting-sm-2.png)*

Refresh the page and wait for the instance `Status` to change to `Stopped`. Note: This process will take few minutes.

![Deleting Amazon SageMaker instance - 3](Images/deleting-sm-3.png)

Select the instance again on the left circular dot, click on Actions and select Delete then confirm delete.

![Notebook Instance delete](Images/notebook-confirm-delete.png)

* At the end of today's lesson, the notebook instances list should be empty and state: "There are currently no resources." Otherwise, charges will be incurred for any remaining active instances.

Lastly, go to Amazon S3 console, and remove the buckets created for the activity as follows.

* Choose the checkbox next to the bucket name, next click on the Delete button.

![Deleting Amazon SageMaker instance - 4](Images/deleting-sm-4.png)

* On the Delete bucket window, type the name of the bucket to confirm that you want to delete it. Next, click on the Confirm button to finish.

![Deleting Amazon SageMaker instance - 5](Images/deleting-sm-5.png)

Answer any questions before moving on.

### 14. Student Do: Delete AWS Resources (15 min)

In this activity, students will delete all the AWS resources created in today's class to avoid additional charges.

Explain to students that, as was mentioned before, the policies for the AWS free tier and trials constantly changes, so it's important to remove any unnecessary resources created on AWS to avoid additional charges. Specifically, remove Amazon SageMaker instances because even though they are stopped, AWS bills for hosting the instances.

Collaborate with TAs, on assisting students to delete all the AWS resources that students would like to remove. Remind students that they can save a local copy of the Jupyter Notebooks by right-clicking on the notebook name and selecting the Download option.

![Downloading a Jupyter notebook](Images/download-notebook-sm.png)

Answer any questions before finishing the class.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
