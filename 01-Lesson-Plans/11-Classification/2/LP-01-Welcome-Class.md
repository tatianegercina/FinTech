## 11.2 Lesson Plan: Trees and Regression

---

### Overview

By the end of Today's class, students will recognize the benefits of using tree based algorithms for classifications problems, also students will gain hands on experience with random forests and ensemble methods such as bagging and boosting.

Today´s lesson also introduce students on dealing with categorical data in machine learning, students will be able to identify when is worth to use categorical data as a feature in a model.

### Class Objectives

By the end of the unit, students will be able to:

* Identify when categorical variables are useful for a machine learning algorithm.

* Perform feature engineering on categorical features and convert labels to numerical class representations.

* Recognize the type of business cases where decision trees and random forests are a suitable solution for classifications problems.

* Demonstrate how random forest performs better than decision trees by avoiding overfitting.

* Identify the pros and cons of tree based algorithms.

* Understand the implications of overfitting and how boosting and bagging can help to deal with it.

* Apply Gradient Tree Boosting models in classification problems.

---

### Instructor Notes

* Today's class is focused on teaching students how tree based algorithms can be used for classification problems, however feature engineering with categorical variables is also covered at the beginning of the class.

* Tree based algorithms have a wide range of applications, Today's class will use them on risk analysis scenarios.

* Some demos of Today's class, uses a lot of memory to train the models; some warning messages may be seen in Jupyter and may provoke questions from students, explain them that these messages are not critical and can be ignored.

* Overfitting is a common problem in machine learning, take your time to understand its implications and how the techniques covered in this class can help to avoid it.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 11.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Day 2 takes students to a new family of machine learning algorithms, students will learn about tree based algorithms and how they can be used in classification problems.

Open the lesson slides, and welcome students to day 2 by highlighting the following:

* Today a new family of machine learning algorithms is going to be introduced: _Tree based algorithms_.

* Tree based algorithms are supervised learning methods that are mostly used for classifications and regression problems.

* This class will cover the following algorithms and methods:

  * Decision trees
  * Random forest
  * Weak learners
  * Ensemble methods

Explain to students, that sometimes you need to deal with categorical data inputs in machine learning problems, for example gender, locations names or risk categories.

Tell students that in this class, they will learn how to deal with categorical data and how to discern if it's worth to include categorical features or not.

Answer any questions before moving on.
