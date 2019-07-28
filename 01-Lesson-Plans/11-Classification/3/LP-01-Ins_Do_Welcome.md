## 11.3 Imbalanced CLasses 

### Overview

Day 3 will focus on a problem that students will encounter often in classification problems: imbalanced data. This occurs when the classes they are trying to predict are represented very unequally in the data. For example, in most fraud detection problems, transactions involving fraud are much more rare than non-fraudulent transactions. We will approach this problem in two ways - through careful examination of how we use model evaluation metrics, and deliberately under or over-sampling to make the training data more equally proportioned. Students will get the opportunity in this class to practice both theory and implementation. 

### Class Objectives

By the end of class, students will be able to:

* Define model evaluation metrics and understand the pros and cons of each metric as applied to different classification problems. 
* Define class imbalance and understand why it presents a problem for classification models.
* Demonstrate the ability to under- and over-sample data with imbalanced classes.
* Demonstrate the ability to plot a precision-recall curve and use it to compare different models.

### Instructor Notes

* Today's class is relatively heavy on theory, and it's important that students understand why they might sometimes need to implement the sampling strategies used in activities. It may be useful to check for understanding by posing questions about theoretical use cases and data sets.

* Be sure to spend some time on the implementations of SMOTE and cluster centroids undersampling, and encourage students to read the documentation for these modules so that they understand how it's working under the hood. 

* It's important for this class to make use of the slides, since concepts like confusion matrices or the precision-recall curve may be easier for many students to understand visually.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students back to the third day of machine learning for classification. Now that we've talked about some techniques to create classification models, we're ready to take the next step and talk about real-world problems. One prominent problem in many classification tasks is class imbalance, which occurs when the training data you use to build your classification model is unevenly split. Some examples include fraud detection, churn prediction, and medical diagnoses - ask students if they can think of any more. We'll talk about the challenges this creates for model creation and evaluation, and then get into how to techniques for dealing with these challenges. 

First, though, we're going to do a little review of concepts from Day 1 of this unit, in which we talked about the confusion matrix and some metrics for evaluating models. 

#### Files

* [13.3 slides](https://docs.google.com/presentation/d/1DJ8LXYZikGc4K8bnOi57Et64ztWVSxdv9zY7wnxLUsA/edit#slide=id.p)