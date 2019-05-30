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

### 0. Instructor Do: Introduce SageMaker (10 mins)

SageMaker Homepage: https://aws.amazon.com/sagemaker/

Visit the SageMaker homepage and cover the following points.

SageMaker is a _platform service_ which consists of three main components that work together or independently:
* Build - Notebook service to explore and prepare the data
* Train - Model training environment and infrastructure
* Deploy - Publish and host a model on an HTTP API endpoint or execute a batch prediction

Additionally, SageMaker includes layers that work across the components:
* Algorithms - Built-in algorithms (k-NN, k-Means, PCA, Forecasting, and many more)
* Frameworks - Deep learning framework containers (Scikit-learn, TensorFlow, MXNet, PyTorch, and others)
* Docker containers - Bring your own model or algorithm container and publish to [AWS ECR](https://aws.amazon.com/ecr/)
* Tuning - Automatic Model Tuning - Search hyper-parameter values for best model fit
* Marketplace -  SageMaker integrates with AWS Marketplace to find, buy and deploy third-party algorithms and models

Review some of the advantages of using SageMaker:
* SageMaker provides tools that streamline a typical workflow for creating a machine learning model
* SageMaker infrastructure enables growth at scale with on-demand compute instances and dynamic storage
* SageMaker pricing for building, training and hosting is billed by the second, no minimum fees and no upfront commitments
* SageMaker advertises "One-click Training" and "One-click Deployment"
* SageMaker comes with built-in security, access controls and monitoring


### 0. Everyone Do: Getting Started with SageMaker (5 mins)

Follow the steps below to create the required AWS resources for SageMaker.

0. Signup for an AWS account (if not done previously)
0. Login to the AWS Console: https://console.aws.amazon.com
0. Create an Amazon S3 Bucket for SageMaker, for example: *sagemaker-`<CURRENT-DATETIME>`*


### 0. Everyone Do: Explore SageMaker (5 mins)

Visit the SageMaker console and show the main components from the left pane menu.
https://console.aws.amazon.com/sagemaker/


### 0. Everyone Do: Explore SageMaker (10 mins)
0. Create an Amazon SageMaker Notebook Instance
0. Create a Jupyter Notebook


### 0. Everyone Do: Create and Deploy a Machine Learning Model (15 mins)

0. Open the following Jupyter Notebook (__TBD: or a custom/similar notebook with modified steps__):  
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/1P_kmeans_highlevel/kmeans_mnist.ipynb

- - -

Answer any questions before ending class.

### End Class

- - -

### Copyright

© 2019 Trilogy Education Services
