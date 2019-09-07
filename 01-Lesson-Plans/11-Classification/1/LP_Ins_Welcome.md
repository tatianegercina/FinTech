## 11.1 Lesson Plan: Classical Classification

### Overview

In the last unit, students learned how to use advanced statistical models and algorithms in order to predict and forecast outcomes using time series data. Students used statistical approaches; such as linear regression, **Hodrick-Prescott filter**, and **GARCH** and **EGARCH** model; to forecast investment returns, volatility, and out-of-sample predictions.

In unit 11, students will dive deeper into statistics and machine learning by working with **classification** algorithms in order to promote and enable supervised machined learning. **Classification** is the act of discovering whether or not a particular feature or element belongs to a given feature class; **classification** derives categorical conclusions based off of classified/modeled data. By the end of this unit, students will be competent in the execution and evaluation of **classification** models (i.e logistic regression and decision trees) for drawing categorical conclusions and outcomes.

Today's class will introduce students to **classification** models by explaining what classification is and delineating the various classification models/approaches. Then, students will be taught how to use Scikit-learn to train models and make them more efficient and effective in determining probability/outcome predictions.

Before students leave at the end of the class, encourage them to continue independently researching and learning more about the various ways to implement classification models, especially some of the ones not demonstrated in class (i.e. neural networks).

* [Ten Applications of AI to FinTech](https://towardsdatascience.com/ten-applications-of-ai-to-fintech-22d626c2fdac)

* [Types of Classification Algorithms](https://medium.com/@Mandysidana/machine-learning-types-of-classification-9497bd4f2e14)

* [FICO: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

### Class Objectives

By the end of class, students will be able to:

* Understand how to calculate and apply regression analysis to datasets.

* Describe the difference between linear and non-linear data.

* Demonstrate how to quantify and validate linear models.

* Apply scaling and normalization as part of the data preprocessing step in machine learning.

* Draw categorical conclusions from classification model output.

* Identify the similarties, differences, and painpoints associated with linear regression, decision trees, ensemble learning,

### Instructor Notes

* Today's class will be a great deal of hands on work training and evaluating classification models. Because the content will be heavy in statistics and machine learning, it's important that you remind students of value and application of these skills/concepts to **FinTech**. Whenever appropriate, remind students that **classification** models enables financial companies to make faster and smarter data driven decisions and outcomes (i.e. credit risk and worthiness, money laundering and fraud identification, longevity and return for a particular investment, and loan recommendations).

* The world of **classification** is a large one. All forms and concepts of classification cannot be covered in one class. Ensure to pace the class and be cognizant of how long it takes to explain concepts. The key is to stay rooted in real world and practical examples of how classification can be used. Avoid getting bogged down in the statistical and mathematical detail for the algorithms. Focus should be placed on

  * What the algorithm/model is

  * What the algorithm/model does and FinTech use case

  * How to train/enhance the algorithm/model

  * How to test algorithms/models and correctly handle false negatives and positives

* This week's activities will use tools such as **imbalance-learn**, **scikit-learn**, and the **Lending Club**.

  * **Imbalance-learn** and **scikit-learn** will need to be added to everyone's Python environments. Modules will need to be installed. Students can consult the [classification ecosystem install guide]() for steps on how to verify both packages have been installed correctly.

  * **Lending club** will be used as a data source for this unit. Accounts will need to be created in order for data to be accessed.

  * Slack out the following links to students to use as resources. There will be no time dedicated for in-class installation.

    * [Imbalance-Learn](https://imbalanced-learn.readthedocs.io/en/stable/)

    * [Scikit-Learn](https://scikit-learn.org/stable/)

* Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. You might find that some students need additional assistance with the statistical concepts, and other students might need help with the application of machine learning models.

  * Encourage students to work with partners for all assignments in order to promote collaborative information seeking.

  * Remind students that additional research and practice will be required outside of class in order to reinforce and build competence in learning and evaluating trained models.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome (10 min)

The instructor starts class with an introduction to **classification** and its use cases within FinTech. Students will receive the who, what, when, why, and how of FinTech **classification**.

**Files:**

* [Welcome Slides]()

Open the 11.2 slides, and begin the class by welcoming students back to the second week of machine learning!

* Explain to students that Unit 11 kicks off the second week of machine learning and advanced analytics. Highlight that this unit will focus on using machine learning algorithms and pipelines to draw categorical conclusions and predictions about probable financial outcomes.

* Briefly explain what **classification** is. Indicate that **classification** is used to draw categorical conclusions about data. Instead of forecasting quantitative numbers, **classification** uses a binary (**true-positive**/**true-negative**) approach to predict categorical membership (i.e. will the outcome be of type A or type B).

  * Communicate that **classification** models can be used to identify a loan applicant as credit worthy or a credit risk. Tell students that they will be learning how to perform classification using, all of which will be explained in more detail in upcoming activities.

    * Logist/Linear Regression

    * Support Vector Machines

    * Nearest Neighbor

* Highlight to students that **classification** models have drastically improved financial efforts to properly classify applicants, predict market decline, and classify fraudulent transaction or suspicious activity.

  * Most large financial institutions are using some form of machine learning to monitor and predict fraudulent activities. This is how banks know when to flag and decline transactions due to suspicion of fraud.

    * Ask students if they've ever received a call from their bank because a transaction was flagged as fraudulent. Explain that the call was triggered by a probability prediction identifying the transaction as fraudulent.

    * For example, FICO credit scoring currently uses a **classification** model for their cognitive fraud analytics platform. Classification engines have allowed the financial industry to become more proactive rather than reactive. Outcomes can be predicted with probable surety, which allows for more effective and efficient mitigation. Slack out the below link as an article of interest for students to review outside of class.

      * [FICO Falcon: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

* Indicate to students their mission for the remainder of this week is to build and train robust classification models in order to automate predictive analytics.

If time remains, ask students emotionally guided questions to get a feel for their current emotional state and give them a space to address any points of excitement, interests, and/or concerns.

* **Machine learning** can be used to automate financial pipelines, forecast time series data and market volatility, predict fraud, analyze sentiment and parse documents, and automate day trading and make investment recommendations. But what exactly is **machine learning**?

  * **Answer** Machine learning is an approach to programming that leverages libraries that provide statistical algorithms and libraries. The machine learning community has developed tried and tested statistical libraries (like **scikit-learn** and **imbalanced-learn**) that offer statistical functions for algorithmic and statistical modeling.

* Last week, you used time series analysis techniques to forecast market returns and volatility. This week we will be exploring **classification** and predicting categorical outcomes. What are you excited about to learn next?

  * **Answer** How to use a **classification** model to predict fraudulent transactions

  * **Answer** How to use a **classification** model to identify best type of line of credit for a consumer

* Do you have any concerns or questions about the content already covered?

  * **Answer** Concerned about not having any background knowledge or experience in statistics

* Underscore to students that the journey into the world of **classification** models and algorithms is both challenging and rewarding.

  * Remind students that everyone in the room will be on the journey together and that resources will be provided to ensure every student has the materials needed to competently train, execute, model, and test classification algorithms.

Ask if there are any questions before moving forward.
