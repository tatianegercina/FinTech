### 2. Instructor Do: Introduction to Unsupervised Learning (10 mins)

After an introduction to machine learning and NLP, students are eager to learn more about this matter. In this activity, students will be introduced to unsupervised learning and its most relevant applications.

**Files:**

* [Lesson 13.1 Slides]()

Open the lesson slides and go to the _Introduction to Unsupervised Learning_ section.

Start the presentation by explaining to students that, in general terms, machine learning has two main areas of application, supervised and unsupervised learning.

Students are already familiar with supervised learning algorithms and its applications, highlight to students the main differences between these types of learning.

| Supervised Learning                      | Unsupervised Learning                    |
| ---------------------------------------- | ---------------------------------------- |
| Input data is labeled                    | Input data is unlabeled                  |
| Uses training datasets                   | Uses just input datasets                 |
| **Goal:** Predict a class or value | **Goal:** Determine patterns or grouping data |

Start a short facilitated discussion with students, take one or two answers from the class by asking the following question.

* If unsupervised learning deals with unlabeled data, what kind of questions or business problems do you think can we afford?

  **Sample Answer:** We can group customers on a retail chain by shopping habits, so we can send customized offers by e-mail or using a mobile app to increase sales.

  **Sample Answer:** Having thousands of transactions per day on credit card operations, it's hard to identify anomalous or fraudulent transactions, we can use unsupervised learning to find patters among transactions data to identify anomalies and potential fraudulent transactions.

  **Sample Answer:** We can use unsupervised learning to cluster stocks data, so we can create investment portfolios according to the resulting groups.

As an example, a customer clustering problem is followed; continue with the presentation on the slide entitled _How can we understand our customers?_, move forward by highlighting the following:

* Beyond the typical segmentation variables, such as age, gender, income or zip code, nowadays understanding customers is crucial on every sector.

* Supervised learning is very helpful predicting the future based on labeled historic data, however, there are some hidden patters on data that supervised learning is unable to find.

* Unsupervised learning enhances customers understanding, we can cluster data to find hidden or unknown patterns that can be used, for example, to develop a customized offer that responses to the needs identified on every group.

* The main applications of unsupervised learning on industry are:

  * **Clustering:** It allows to automatically split the dataset into groups according to similarity. It can be used for customer segmentation and targeting.

  * **Anomaly Detection:** Automatically discovers unusual data points in a dataset. It's useful in identifying fraudulent transactions, discovering faulty pieces of hardware, or identifying an outlier caused by a human error during data entry.

* Customer segmentation is one of the most popular applications of unsupervised learning. It is the division of potential customers in a given market into discrete groups.

* Thanks to unsupervised learning algorithms, we can group customers based similarities such as:

  * Customer needs (e.g. a particular product can satisfy some of them).
  * Responses to online marketing channels.
  * Buying habits (e.g. best day for buying, weekly spend)

Comment to students, that customer segmentation is driving revenue in leading companies such as Netflix and Amazon as it's presented on the slides.

  * 75% of Netflix viewer activity is driven by recommendation ([Source](http://blog.springtab.com/personalization-examples-netflix/)).
  * 35% of Amazon’s sales are generated through their recommendation engine ([Source](https://www.martechadvisor.com/articles/customer-experience-2/recommendation-engines-how-amazon-and-netflix-are-winning-the-personalization-battle/)).
  * Netflix’s recommendation system saves the company an estimated $1Billion per year through reduced churn ([Source](https://dl.acm.org/citation.cfm?id=2843948)).

End the presentation with a closing facilitated discussion, ask the following questions to students:

* How a bank could use customer segmentation to improve their products?

  **Sample Answer:** Instead of having a generic offer of credit cards, a bank could use customer segmentation to offer credit cards according to demographics such as: age, geography, gender, generation (e.g. Millennials and Baby Boomers), income level, marital status, etc.

* How an investment portfolio can be improved using customer segmentation?

  **Sample Answer:** Using customer segmentation a portfolio can be categorized by industry, location, revenue, account size, and number of employees to reveal where risk and opportunity live within the portfolio. These patterns can provide key measurable data for more predictive credit risk management.

Comment to students that, unsupervised learning and algorithms like K-Means, are the tools behind this kind of magic that is perceived by customers.

Answer any questions before moving on.
