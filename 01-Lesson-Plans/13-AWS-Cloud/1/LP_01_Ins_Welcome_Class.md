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

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.1 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

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
