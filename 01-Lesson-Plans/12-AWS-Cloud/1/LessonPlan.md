## 12.3 Lesson Plan: Introduction to APIs / Cloud Infrastructure (AWS)

### Overview

In today's class, students will be introduced to APIs and Cloud Infrastructure with Amazon Web Services (AWS) and will learn how to leverage some cloud computing services for machine learning.

### Class Objectives

By the end of class, students will be able to:

* Understand how AWS SageMaker can be used for Machine Learning
* ...

### Instructor Notes

This lesson introduces new content rapidly. Students may express frustration at learning new cloud technologies. Remind students that while the learning curve may be steep at first, AWS and cloud experience is highly sought-after and well worth the effort required to become comfortable with it.

Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 mins)

...

### 0. Instructor Do: Introduce AWS SageMaker (10 mins)

Visit the SageMaker homepage and cover the following points.  
https://aws.amazon.com/sagemaker/

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

* First, students login to the AWS Console: https://console.aws.amazon.com
* Find and visit SageMaker in the Services menu.  
Remind students that SageMaker might not be available on all AWS regions, but `us-east-1 (N. Virginia)` is sure to have it.  
Direct link: https://console.aws.amazon.com/sagemaker/home?region=us-east-1
* Now students can explore the main components on the left pane menu.  
* Have TA's ensure all students are able to login.


### 0. Everyone Do: Create a SageMaker Notebook Instance (5 mins)

SageMaker uses a compute instance to run notebooks, the create process will configure multiple settings behind the scenes.

Have students follow along executing the next steps to create a SageMaker Notebook Instance.

First, create the required AWS resources for SageMaker.
* From the main AWS Console, find the `S3` service: https://s3.console.aws.amazon.com
* Create a bucket for SageMaker:
  S3 -> Buckets -> click `Create Bucket` and fill in details as follows:
  * Section: **Name and region**
    + Bucket name: *sagemaker-`<CURRENT-DATE+TIME>`* (for example: `sagemaker-20190701-1820`)
    + Region: `(same as SageMaker instance)`
    + Click: "Next" (leave defaults)
  * Section: **Configure options**
    + Click: "Next" (leave defaults)
  * Section: **Set permissions**
    + Click: "Next" (leave defaults)
  * Section: **Review**
    + Click: `Create bucket`
* Note down (copy/paste/save) the name of bucket for use in the following section.

Next, create the SageMaker Instance.
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


### 0. Everyone Do: Create a new Jupyter Notebook (5 mins)

Show students how to create a new Jupyter notebook in SageMaker's notebook instance.

* Once the Notebook Instance has status `InService`, go to "Actions" and click on `Open JupyterLab`.  
![Notebook Instance actions](Images/06-notebook-instance-actions.png)  

* On JupyterLab Launcher, select notebook `conda_python3` to create a new notebook.
![Notebook Environment](Images/07-jupyterlab-env-conda_python3.png)  

* Enter and execute python code to demonstrate functionality.  
![Untitled Notebook](Images/08-notebook-untitled.png)


### 0. Everyone Do: Open an existing Jupyter Notebook (5 mins)

Show students how to open an existing Jupyter notebook in SageMaker's notebook instance.

* From the main `JupyterLab` view, use the `Upload` icon (arrow up) on the left and select an existing notebook.  
For example: `04-Pandas/3/Activities/16-Stu_Portfolio_Planner_Part_II/Unsolved/portfolio_planner_part_2.ipynb`  
Select the local notebook file to upload.  
![Upload Notebook](Images/09-upload-notebook.png)

* Open the notebook. You'll probably see the message: `Select Kernel` or `Kernel not found`, select `conda_python3` and click `Select` or `Set Kernel`  
![Notebook Kernel not found](Images/10-notebook-select-kernel-1.png)

![Notebook Kernel not found](Images/10-upload-nb-kernel-not-found-2.png)

* Now you can run commands on the notebook cells.  
Note: you might need to make some of the `CSV` input files available by also uploading them to the right location).


### 0. Everyone Do: Create and Deploy a Machine Learning Model (15 mins)

Show students how a Machine Learning model is created, trained and deployed in SageMaker.

* Open the following Jupyter Notebook (__TBD: or a custom/similar notebook with modified steps__):  

* From the main `Jupyter` view, select `SageMaker Examples`, then scroll to `Introduction to Amazon Algorithms`, then find: `linear_learner_mnist.ipynb`

* Run through the notebook.

* TBD.


### 0. Everyone Do: Delete Notebook Instance (5 mins)

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


- - -

Answer any questions before ending class.

### End Class

- - -

### Copyright

© 2019 Trilogy Education Services
