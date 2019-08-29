## 13.2 Lesson Plan: Deploying ML Models with SageMaker

### Overview

In today's class, students will be introduced to some Amazon Web Services (AWS) tools and will learn how to leverage some cloud computing services for machine learning using Amazon SageMaker.

### Class Objectives

By the end of class, students will be able to:

* Describe the pros and cons of using cloud services to deploy machine learning models.

* Orchestrate a cloud solution by combining different AWS services.

* Understand how Amazon SageMaker works and how it can be used to deploy machine learning models.

### Instructor Notes

* This lesson introduces new content rapidly. Students may express frustration at learning new cloud technologies. Remind students that while the learning curve may be steep at first, AWS and Cloud experience is highly sought-after and well worth the effort required to become comfortable with it.

* **Important!** Slack out the disclaimer for [AWS Free Tier](../Supplemental/AWS-Free-Tier.pdf) services prior to class. Take some time at the beginning of class to explain that while we are only using free tier services in class, students should review this documentation in order to avoid accidentally incurring charges.

* Note that in the past, AWS content has appeared differently for some instructional teams. It seems that AWS does A/B testing on their UI. If your AWS views _don’t_ match up with the views in the lesson plan, check that you've pulled the latest updates from github or look in the Slack Instructional Team channel for announcements regarding this.

* Check prior to class that all students has a an AWS account and are able to login.

* Today's class should be a fun one. Students will put together many different technologies covered so far and learn how they can interact with cloud services.

* There are a few activities that require setup. Have the class follow along and ask questions as you go.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome class to day 2 of Unit 13, this should be a fun one since students will go deeper on using AWS to deploy machine learning models.

Explain students that along this unit, we will use the free tier of AWS, as well as, the trial period for some of the services. Slack out the following resources to be used as reference to understand how the free offer of AWS works.

* [AWS Free Tier Supplemental](../Supplemental/AWS-Free-Tier.pdf)

* [AWS Free Tier Documentation](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23ai-ml)

Open the [AWS Free Tier Supplemental](../Supplemental/AWS-Free-Tier.md) and briefly explain to students the limits we will have for the services they will learn in this unit.

| Amazon SageMaker (Free Trial)                                                    | Amazon Lex (12 Months Free)       | AWS Lambda (Always Free)                              | Amazon S3 (12 Months Free) |
| -------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------- | -------------------------- |
| `250` hours per month of `t2.medium` notebook usage for the first **two months** | `10,000` text requests per month  | `1,000,000` free requests per month                   | `5` GB of Standard Storage |
| `50` hours per month of `m4.xlarge` for training for the first **two months**    | `5,000` speech requests per month | Up to `3.2` million seconds of compute time per month | `20,000` Get Requests      |
| `125` hours per month of `m4.xlarge` for hosting for the first **two months**    |                                   |                                                       | `2,000` Put Requests       |

Answer any questions before moving on.

### 2. Instructor Do: Introduce AWS SageMaker (10 mins)

* **Important!** Slack out the disclaimer for [AWS Free Tier](Activities/00-AWS_Free_Tier/AWS-Free-Tier.pdf) services prior to class. Take some time at the beginning of class to explain that while we are only using free tier services in class, students should review this documentation in order to avoid accidentally incurring charges. All resources created in class should be stopped and deleted at the end of class to ensure no usage fees. The last activity goes over this.

Visit the AWS SageMaker homepage and cover the following points.
<https://aws.amazon.com/sagemaker/>

SageMaker is a _platform service_ which consists of three main components that work together or independently:

* Build - Notebook service to explore and prepare the data
* Train - Model training environment and infrastructure
* Deploy - Publish and host a model on an HTTP API endpoint or execute a batch prediction / inference.

Additionally, SageMaker includes layers that work across the components:

* Ground Truth - Data labeling service
* Tuning - Automatic Model Tuning - Search hyper-parameter values for best model fit
* Algorithms - Built-in algorithms (k-NN, k-Means, PCA, Forecasting, and many more)
* Frameworks - Deep learning framework containers (Scikit-learn, TensorFlow, MXNet, PyTorch, and others)
* Docker containers - Bring your own model or algorithm container and publish to [AWS ECR](https://aws.amazon.com/ecr/)
* Marketplace -  SageMaker integrates with AWS Marketplace to find, buy and deploy third-party algorithms and models

Review some of the advantages of using SageMaker:

* SageMaker provides tools that streamline a typical workflow for creating a machine learning model
* SageMaker infrastructure enables growth at scale with on-demand compute instances and dynamic storage
* SageMaker pricing for building, training and hosting is billed by the second, no minimum fees and no upfront commitments
* SageMaker advertises "One-click Training" and "One-click Deployment"
* SageMaker comes with built-in security, which includes access controls and monitoring

### 0. Students Do: Explore SageMaker (5 mins)

Give students a few minutes to explore SageMaker.

* First, students login to the AWS Console: <https://console.aws.amazon.com>
* Find and visit SageMaker in the Services menu.
Remind students that SageMaker might not be available on all AWS regions, but `us-east-1 (N. Virginia)` is sure to have it.
Direct link: <https://console.aws.amazon.com/sagemaker/home?region=us-east-1>
* Now students can explore the main components on the left pane menu.
* Have TA's ensure all students are able to login.

### 0. Instructor Do: Create a SageMaker Notebook Instance (15 mins)

SageMaker uses a compute instance to serve `Jupyter` notebooks, the create instance process will configure multiple settings behind the scenes.

Have students follow along executing the next steps to create a SageMaker Notebook Instance.

First, create the required AWS resources for SageMaker.

* From the main AWS Console, find the `S3` service: <https://s3.console.aws.amazon.com>
* Create a bucket for SageMaker:
![Create S3 bucket](Images/00-create-bucket.png)
Go to S3 -> Buckets -> click `Create Bucket` and fill in details as follows:

  * Section: **Name and region**
    * Bucket name: *sagemaker-`<CURRENT-DATE+TIME>`* (for example: `sagemaker-20190701-1820`)
    * Region: `(same as SageMaker instance)`
    * Click: "Next" (leave defaults)
  * Section: **Configure options**
    * Click: "Next" (leave defaults)
  * Section: **Set permissions**
    * Click: "Next" (leave defaults)
  * Section: **Review**
    * Click: `Create bucket`
* Note down (copy/paste/save) the name of bucket for use in the following section.

* From the SageMaker console, use the left pane menu and visit: Notebook -> [Notebook instances](https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances)
* On the right side, click: [Create notebook instance](https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances/create)
![Create notebook instance](Images/01-create-notebook-instance-1.png)
* Fill in the required values, leaving most defaults unchanged, for example:

  * Notebook instance name: `sm-test`
  * Notebook instance type: `ml.t2.medium`
  * Elastic Inference: `none`
  * IAM role: `Create a new role` (enter the name of the previously create *S3 bucket* in "Specific S3 buckets", then click `Create role`)
  ![Create IAM Role success](Images/02-iam-role-create-success.png)
  * Root access - `Enable - Give users root access to the notebook` (remind students that this is less safe but allows more control over the instance)

* Click: `Create notebook instance`
Note: the `IAM Role` is required, if this or another required field value is missing the process won't proceed until addressed. If all required values where provided you'll see a success message.
![Create Notebook Instance success](Images/03-notebook-instance-create-success.png)

* Click on the Notebook Instance to view further details
![Notebook Instance details](Images/04-notebook-instance-details.png)

* Back in the Notebook Instance list, refresh the page and wait for the status of the new instance to be: `InService`
![Create Notebook Instance success](Images/05-notebook-instance-status.png)

* Remind students that AWS charges for these and most resources as they are created, event when not in use, this instance is billed for by the second until it's turned off and deleted.

### 0. Instructor Do: Create a new Jupyter Notebook (5 mins)

* Once the Notebook Instance has status `InService`, go to "Actions" and click on `Open JupyterLab`.
![Notebook Instance actions](Images/06-notebook-instance-actions.png)


* On the `Notebook` section in the JupyterLab `Launcher`, select `conda_python3` to create a new notebook.
![Notebook Environment](Images/07-jupyterlab-env-conda_python3.png)

* On the new notebook, enter python code in the first cell to test and demonstrate the functionality.
![Untitled Notebook](Images/08-notebook-untitled.png)

### 0. Instructor Do: Open an existing Jupyter Notebook (5 mins)

Show students how to open an existing Jupyter Notebook in the new SageMaker Notebook instance.
For this example we'll use a notebook in our local machine, from a previous activity.

* In your SageMaker notebook instance, from the main `JupyterLab` view, use the `Upload` icon (arrow up) on the left and select an existing notebook.
For example: `04-Pandas/3/Activities/16-Stu_Portfolio_Planner_Part_II/Unsolved/portfolio_planner_part_2.ipynb`
Select the local notebook file to upload.
![Upload Notebook](Images/09-upload-notebook.png)

* Open the notebook. You'll probably see the message: `Select Kernel` or `Kernel not found`, select `conda_python3` and click `Select` or `Set Kernel`
![Set Notebook Kernel](Images/10-notebook-select-kernel-1.png)

![Notebook Kernel not found](Images/10-upload-nb-kernel-not-found-2.png)

* Now you can run commands on the notebook cells.
Note: you might need to make some of the `CSV` input files available by also uploading them to the right location).

### 0. Students Do: Housing Price Prediction (20 mins)

* In this activity, students will calculate a regression line to predict the price of a house using the Boston Housing dataset and the SageMaker built-in `Linear Learner` algorithm.

* **File**: [boston-housing-regression.ipynb](Activities/02-Stu_Housing_Linear_Regression/Unsolved/boston-housing-regression.ipynb)

* **Instructions:** [README.md](Activities/02-Stu_Housing_Linear_Regression/README.md)

  * Upload the provided notebook to SageMaker's JupyterLab and run each cell to build, train, deploy the model. After this

### 0. Instructor Do: Review Activity (10 mins)

* Reassure students that it's okay if this was difficult. SageMaker APIs have a learning curve, as do other AWS resources, along with Machine Learning in general. They will get a lot of practice with this today!

* Open up [boston-housing-regression.ipynb](Activities/02-Stu_Housing_Linear_Regression/Solved/boston-housing-regression.ipynb)

* During the review, the high level steps are as follows:

  * We get the data and become familiar with it.
  * Split the data into _Test_ and _Train_ and convert it to the [ProtoBuf format](https://developers.google.com/protocol-buffers/) used by SageMaker algorithms.
  * Upload the prepared and formatted data to an `AWS S3` bucket.
  * Train the model using a linear learner algorithm on the data in `S3`.
  * Deploy the trained model on a SageMaker instance.
  * Perform predictions and score the model's performance.
  * Cleanup. Remove the model-hosting instance and the S3 bucket.

* Cover the bonus in the following activity.

### 0. Instructor Do: Discuss Pros and Cons of deploying ML models with SageMaker (10 mins)

Leads and facilitate a discussion around deploying models in SageMaker and why a RESTful ML API is useful.

Have students share their opinions with the class and bring up the following points:

Pros:

* Data storage capacity: by using an `S3 bucket`, to store the data we could have trained a model on multiple terabytes of data, or a lot more space than would otherwise have fit in our personal computer.
* Hardware / GPU: By using another instance to train our model, we can access compute power including GPU capabilities, making powerful hardware available to us as required.
* Cost: Using AWS resources, we only pay for what we use, we'll turn off everything before ending the class and not incur in further charges.
* Availability: By deploying our model to another instance, we have make the prediction functionality available 24/7 through a secured endpoint to an application or to be consumed by others without having to make our computer available.
* RESTful API: As learned in previous units, APIs provide a standard mechanism to access data, our ML API can be consumed through apps and other channels in a simple form while remaining secure and allowing other constraints (for example: authentication, authorization, rate limiting, etc.).

Cons:

* Data privacy / security: by uploading data to a third party, you are trusting your data on them. Certain kinds of data are subject to compliance and regulatory constraints.
* Visibility: you won't have oversight on AWS internal handling of your data and infrastructure.
* Availability: although there are SLAs in place, AWS (and other cloud providers) can and have suffered outages at times, causing data unavailability.

### 0. Instructor Do: Create and Deploy a Machine Learning Model (15 mins)

Show students how a Machine Learning model is created, trained and deployed in SageMaker.

* Open the following Jupyter Notebook (__TBD: or a custom/similar notebook with modified steps__):

* From the main `JupyterLab` view, select `SageMaker Examples`, then scroll to `Introduction to Amazon Algorithms` and find: `linear_learner_mnist.ipynb`

![SageMaker Sample Notebooks](Images/11-examples-linear-lerner.png)

* Run through the notebook.

* TBD.

### 0. Instructor Do: Delete Notebook Instance (5 mins)

Show students how to delete their SageMaker notebook instance so that no billing charges are incurred for it after class.

* From the SageMaker console, use the left pane menu and visit: Notebook -> [Notebook instances](https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances)

* Select the the Notebook Instance (or follow this process for all) on the left circular dot.
![Notebook Instance list](Images/notebook-instance-list.png)

* Once selected, click on the right `Actions` menu and select `Stop`.

* Refresh the page and wait for the instance `Status` to change to `Stopped`.
![Notebook Instance actions](Images/notebook-instance-actions.png)

* Select the instance again, click on `Actions` and select `Delete` then confirm delete.
![Notebook Instance delete](Images/notebook-confirm-delete.png)

* At the end of the lesson, the notebook instances list should be empty and state: "There are currently no resources.", otherwise charges will be incurred for any remaining active instances.

* Lastly, go to S3 <https://s3.console.aws.amazon.com> and remove the buckets created for the activity.

- - -

Answer any questions before ending class.

### End Class

- - -

### Copyright

© 2019 Trilogy Education Services
