## 13.1 Lesson Plan: Unsupervised Learning and K-Means

### Overview

Today's class will introduce students to unsupervised learning and the K-Means algorithm, one of the most used unsupervised ML algorithms for clustering. Additionally, students will learn how to speed up ML algorithms by using principal component analysis (PCA), as well as to recognize and to explain at least three main differences between supervised and unsupervised machine learning algorithms.

As a prelude for next class, an introduction to Amazon Web Services (AWS) and AWS SageMaker is given the end of the day.

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

* There are several theoretical aspects behind the K-Means algorithm, focus the class on the practical application of this algorithm for customer segmentation and share the additional references presented on the slides for those students interested on having a deeper understanding.

* Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. Also encourage students to work with partners.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.1 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 mins)

After an introduction to machine learning and NLP, students are eager to learn more about this matter. In this activity, students will be introduced to unsupervised machine learning and its most relevant applications.

**Files:**

* [Lesson 13.1 Slides]()

Welcome the class to Unit 13, explain students that on this unit they will learn about unsupervised machine learning, also they will recognize the importance of the cloud and cloud services to deploy enterprise machine learning applications.

Open the lesson slides, move to the _Introduction to Unsupervised Learning_ section and highlight the following:

* In general terms, machine learning has two main areas of application, supervised and unsupervised learning.

Students are already familiar to supervised machine learning algorithms and applications, so highlight to students the main differences between these types of learning.

| Supervised Learning                      | Unsupervised Learning                    |
| ---------------------------------------- | ---------------------------------------- |
| Input data is labeled                    | Input data is unlabeled                  |
| Uses training datasets                   | Uses just input datasets                 |
| **Goal:** Predict a class or value label | **Goal:** Determine patterns or grouping |

* A fruit basket could be used as a quotidian example to understand these types of learning. The _supervised learning_ approach will try to answer the question `Is that fruit an apple?`, whereas using an _unsupervised learning_ approach, we will try to answer the question `How the different fruits can be classified on the basket?`.

* The main applications of unsupervised machine learning on industry are:

  * **Clustering:** It allows to automatically split the dataset into groups according to similarity. It can be used for customer segmentation and targeting.

  * **Anomaly Detection:** Automatically discovers unusual data points in a dataset. It's useful in identifying fraudulent transactions, discovering faulty pieces of hardware, or identifying an outlier caused by a human error during data entry.

As an icebreaking activity, conduct a facilitated discussion about how companies are using customer segmentation to create personalized customer experiences. Start by sharing the following stats and ask students what they think about them:

* 75% of Netflix viewer activity is driven by recommendation ([Source](http://blog.springtab.com/personalization-examples-netflix/)).
* 35% of Amazon’s sales are generated through their recommendation engine ([Source](https://www.martechadvisor.com/articles/customer-experience-2/recommendation-engines-how-amazon-and-netflix-are-winning-the-personalization-battle/)).
* Netflix’s recommendation system saves the company an estimated $1Billion per year through reduced churn ([Source](https://dl.acm.org/citation.cfm?id=2843948)).

You can ask the following questions to class:

* How a bank could use customer segmentation to improve their products?

  **Sample Answer:** Instead of having a generic offer of credit cards, a bank could use customer segmentation to offer credit cards according to demographics such as: age, geography, gender, generation (e.g. Millennials and Baby Boomers), income level, marital status, etc.

* How an investment portfolio can be improved using customer segmentation?

  **Sample Answer:** Using customer segmentation a portfolio can be categorized by industry, location, revenue, account size, and number of employees to reveal where risk and opportunity live within the portfolio. These patterns can provide key measurable data for more predictive credit risk management.

Close the dialogue commenting to students that, unsupervised learning and algorithms like K-Means, are the tools behind this kind of magic that is perceived by customers.

Answer any pending question an continue to the next activity.
