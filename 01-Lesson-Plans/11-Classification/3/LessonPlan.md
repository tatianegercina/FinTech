## 11.3 Lesson Plan: Imbalanced Classes

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

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1qaiDAlthQE0ECwlJYmm0zaYtCoBM9C17BUNcdHybFhI/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back to the third day of machine learning for classification. Now that we've talked about some techniques to create classification models, we're ready to take the next step and talk about real-world problems. One prominent problem in many classification tasks is class imbalance, which occurs when the training data you use to build your classification model is unevenly split. Some examples include fraud detection, churn prediction, and medical diagnoses - ask students if they can think of any more. We'll talk about the challenges this creates for model creation and evaluation, and then get into how to techniques for dealing with these challenges.

First, though, we're going to do a little review of concepts from Day 1 of this unit, in which we talked about the confusion matrix and some metrics for evaluating models.

**Files:**

* [Unit 13.3 slides](https://docs.google.com/presentation/d/1DJ8LXYZikGc4K8bnOi57Et64ztWVSxdv9zY7wnxLUsA/edit#slide=id.p)

### 2. Instructor Review: Model Evaluation (10 min)

This activity will give students a chance to refresh the concepts of model evaluation, which we first went over in the first day of this unit.

**Files:**

* [review_model_eval.ipynb](Activities/01-Ins_Review_Eval_Metrics/Solved/review_model_eval.ipynb)

Walk through the first few blocks of the notebook.

* We created two classes in this data, with two important features. First, one class is much larger than the other. Second, the classes have significant variation, so neither is cleanly distinguishable from the other.

  ![eval_1.png](Images/eval_1.PNG)

* Using a logistic regression mode, we try to predict the class, purple or yellow, with the coordinates of a point.

Ask a student to help you interpret the output of the confusion matrix. Refer to the slide to reveal the correct answer.

![eval_2png](Images/eval_2.PNG)

* Looking only at this matrix, it seems that the model does reasonably well. While there are some false positives, the vast majority of data points are classified correctly.

Move on to the next block, and ask a student to define the three metrics that are shown here. Once again, refer to the slide to confirm the student's answers.

![eval_3png](Images/eval_2.PNG)

* Precision is the proportion of predicted positives that are accurate. Recall is the proportion of actual positive that were predicted as positive. The F1 metric is a blended average of the two.

Ask students to evaluate the performance of this model. How do they think it did?

* While the confusion matrix and evaluation metrics do give us some insight into performance, this is a bit of a trick question. Whether or not the model is "good" depends on context. What are we trying to predict? What are the cost of false positives, or false negatives?

### 3. Students Do: Hypothetical Models (15 min)

In this activity, students will discuss the relative importance of false positives/negatives and weigh the pros and cons of using each evaluation metric for a set of hypothetical classification models.

**Instructions:**

* [README.md](Activities/02-Stu_Do_Hypothetical_Models/README.md)

### 4. Instructor Do: Review Hypothetical Models (10 min)

Open the slides and walk through each scenario with the students.

Ask a volunteer to talk the class through each scenario before outlining our answers below.

* In the first case, if we define spam emails as positives, false positives are more costly than false negatives (a spam email getting through is not the end of the world, while an important email that gets flagged as spam might be disastrous for the user). Precision and specificity are important to consider for this reason. Spam emails probably make up a relatively small (but not tiny) proportion of all emails. Because of this, a high accuracy or F1 score might be misleading.

* False positives and false negatives should probably be weighted fairly evenly in this situation, but true positives are likely to be a small proportion of true negatives. In this situation, high accuracy may still be misleading, but all other evaluation metrics should be examined for different models to understand the relative strengths and weaknesses of each.

* For the third example, there doesn't seem to be any obvious reason why false negatives or positives should be weighted more than the other. Assuming a random, representative sample, we would expect the two classes to be roughly equal in size. Therefore, accuracy or the F1 score would likely be a effective summary metric to compare models.

* In the fourth example, if we define rain as positive, false negatives are likely to be more costly than false positives. This makes recall a metric of special interest. Since the classes are likely to be imbalanced, but not overwhelmingly so (in most climates, a sizable minority days probably have rain). The F1 score is likely a useful measure to compare metrics.

* For the final example, false negatives are likely to be viewed as more costly than false positives, as VCs invest with the knowledge that the majority of companies will fail but get large returns from those that don't. Recall is likely to be the metric of most interest in this case.

Tell the class that though we highlighted particular metrics for each of these examples, it is always beneficial to look at the confusion matrix and all the metrics to understand the strengths and weaknesses of any particular model, even if some may be more useful than others for any given data.

### 5. Instructor Do: Imbalanced Data (5 min)

Continue in the slides to the imbalanced data slide.

* Imbalanced data describes cases when one or more classes in the data is much more or less frequent than the other class(es). We will be working with binary (two class) classification tasks for simplicity, but imbalanced data is a problem in multi-class tasks as well.

* Imbalanced data is problematic for two main reasons. First, it can cause your model to be biased towards the majority class. Basically, the model will be better at predicting the majority class compared to the minority class because model fitting algorithms are designed to minimize the number of total incorrect classifications. For a concrete example, imagine a data set with two classes A and B. There are 100 instances of A in the training sample, and only 10 instances of B. Imagine a naive model that always picks A. If the data were perfectly balanced, this would result in an accuracy of 50%. However, because this data is imbalanced, this naive model would achieve an accuracy of 100/110, or over 90%! If the two classes are not easily separable, the resulting model will lean towards the naive model and be much better at predicting the majority class than the minority class.

* As you have seen in the previous activity, imbalanced classes like cancer/non-cancer can cause metrics like accuracy to be unreliable as a proxy for the "goodness" of a model. The example above illustrates why.

* The rest of the class will go over strategies to deal with imbalanced classes. We will work mostly with over and under-sampling methods, in which we sample the minority class with greater than random chance or sample the majority class with less than random chance. We will also explain why ensemble methods may be more suitable for imbalanced data than other classification methods, and introduce a classification report specifically created for imbalanced data.

### 6. Instructor Do: Oversampling (10 min)

**Files:**

[oversampling.ipynb](Activities/03-Ins_Do_Oversampling/Solved/oversampling.ipynb)

Continue through the slides to the oversampling slide.

* Oversampling is intuitive - if we think one class has too few instances in the training sample, then we should choose more instances from that class for training than we normally would.

* There are a few ways we can do this; we'll talk about two types of oversampling techniques, random and SMOTE (Synthetic Minority Oversampling Technique). Random oversampling replicates the existing training set, randomly choosing additional instances of the minority class with replacement until the minority class is equal to the majority class in size. SMOTE generates synthetic data by first identifying cluster centers in the minority data and then randomly introducing variations to those centers to create new instances.

* Random oversampling is more likely to create overfitting problems in the model, due to the lack of variation in the repeated instances.

Open the notebook and walk through the cells one by one.

* First, we implement random oversampling on the generated dataset. One important note is that prior to the oversampling process, we want to split up the data into training and test sets as we would normally do. This is because even though we would like the *training* set to be oversampled to account for imbalance, we should always make sure that the *test* set to be "real" - that is, data that actually is actually observed. We would therefor not want to oversample the entire dataset.

* This initial train-test split gives us the following imbalanced data.

![overs_1](Images/overs_1.PNG)

* Note that we specify a random_state parameter for the random oversampler so that the sampling is replicable - if we want to repeat the same "random" oversampling, we just need to specify the same random_state in the future.

* After oversampling, we can see that the two classes are now balanced.

![overs_2](Images/overs_2.PNG)

* We apply logistic regression to the training set and then use the model to predict the values of y from the test set. The confusion matrix and the accuracy score should be familiar to students, but we introduce another function useful for imbalanced evaluation: the imbalanced classification report, which includes more evaluation metrics and produces them separately for the two classes.

* We can see below that the minority class has low precision and therefor a lower F1 score in spite of oversampling. This may be due to overfitting in the training set.

![overs_3](Images/overs_3.PNG)

Pause for any questions before moving on to the implementation of SMOTE oversampling.

* The code for SMOTE oversampling is very similar, with the only difference being the choice of sampling function.

* As we can see from the evaluation metrics below, the model created from the SMOTE oversampled data is marginally better than the randomly oversampled model.

![overs_4](Images/overs_4.PNG)

* There are several reasons why we shouldn't necessarily read too much into the results from this example. First, the data is artificially generated in the first place; real-life data would not normally have these properties. Second, the test set is relatively small, and individual instances being correct or wrong, especially in the minority class, can lead to large changes in the evaluation metrics.

Pause for questions before moving on to the next activity.

### 7. Students Do: More Loans (15 min)

In this activity, students will practice using random and SMOTE oversampling in combination with logistic regression to predict whether or not someone is likely to default on their credit card loans in a given month given demographic information.

**Files:**

[more_loans.ipynb](Activities/04-Stu_Do_More_Loans/Unsolved/more_loans.ipynb)

[README.md](Activities/04-Stu_Do_More_Loans/README.md)

**Dataset:**

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480. (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients#)

Introduce students to the dataset they will be using for this activity. Each row represents a person with a credit card account. ln_balance_limit is the log of the maximum balance they can have on the card; 1 is female, 0 male for sex; the education is denoted: 1 = graduate school; 2 = university; 3 = high school; 4 = others; 1 is married and 0 single for marriage; default_next_month is whether the person defaults in the following month (1 yes, 0 no).

### 8. Instructor Review: More Loans (5 min)

**Files:**

[more_loans.ipynb](Activities/04-Stu_Do_More_Loans/Solved/more_loans.ipynb)

Since this activity is almost an exact replica of the oversampling demonstration, you can likely go through this review quickly.

* First, we need to identify the variable that we are trying to predict, which is whether a person defaults on their credit card loan in the next month - this variable is default_next_month. We create the dependent and independent variables in the following code:

```python
x_cols = [i for i in df.columns if i != 'default_next_month']
X = df[x_cols]
y = df['default_next_month']
```

* Again, we split the data into train and test sets *before* doing oversampling. This is so that we maintain a purely observed test set.

* After running the oversampling and logistic regression functions, these are the evaluation metrics we receive:

Random Oversampling

![stovers_1](Images/stovers_1.PNG)

SMOTE Oversampling

![stovers_2](Images/stovers_2.PNG)

Ask students how they interpreted the evaluation metrics. What are some reasons why the evaluation metrics using both oversampling methods might both be relatively low?

* SMOTE is not guaranteed to outperform random oversampling in all applications. The threat of overfitting due to repeated samples with random oversampling is not as great when the imbalance in classes is not as extreme, as is the case in this data set. Moreover, the fact that SMOTE samples are mostly artificial can actually decrease model performance if the generated data does not have the same structure as the observed data does.

### 9. Instructor Do: Undersampling (10 min)

Continue in the slides to the undersampling slide.

* If we have imbalanced classes, we can purposefully use more of the minority class for training - this is oversampling. However, we can also take fewer instances of the majority class than would be indicated by a proportional sampling method - this is called undersampling.

* In undersampling, we take only as many instances of the majority class as there are instances in the minority class training set.

* Undersampling is only practical when there is enough data in the training set that a model can be suitably estimated with the reduced number of total training data.

* However, undersampling does have the advantage that all data in the training set are actual observed data, and potential model biases that come from replicating training data or creating synthetic data will not exist, as they might with oversampling.

* Just like oversampling, there are numerous methods for undersampling. We will go over random undersampling and cluster-centroid undersampling.

* In random undersampling, the algorithm randomly chooses majority class instances to take out of the training set until the number of instances of the majority class is equal to the number of instances in the minority class training set.

* In cluster centroid undersampling, the algorithm first creates `n` clusters in the majority class training data using the K-means clustering strategy, where `n` is equal to the number of minority class training instances, and then takes the centroids of those clusters to be the majority class training set. This is meant to ensure that the sampled data is "representative" of the majority set, as compared to a random set.

Pause for students' questions before moving on to the next activity.

### 10. Students Do: Undersampling (15 min)

In this activity, students will research and practice undersampling with the imbalanced-learn library.

**Files:**

[undersampling.ipynb](Activities/05-Stu_Do_Undersampling/Unsolved/undersampling.ipynb)

[README.md](Activities/05-Stu_Do_Undersampling/README.md)

**Dataset:**

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480. (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients#)

### 11. Instructor Review: Undersampling (5 min)

**Files:**

[undersampling.ipynb](Activities/05-Stu_Do_Undersampling/Solved/undersampling.ipynb)

Open the solved notebook and go through the code. Since the structure of this activity is very similar to the oversampling activity, you should focus on the evaluation metrics obtained from the two undersampling methods.

* The results from random undersampling seem to be worse than those from oversampling across the board. This might signal that the additional data provided by oversampling was necessary to train a good model.

![unders_1](Images/unders_1.PNG)

* Results from cluster centroid undersampling are even worse than those from random undersampling. This difference is most likely due to random variation.

![unders_2](Images/unders_2.PNG)

Ask students which sampling method they prefer for this data given the evaluation results they have seen. Is there ever an argument for using a sampling methdology that results in worse evaluation metrics?

* Holding all else equal, we would want to use the sampling methdology that results in the best evaluation metrics. However, we have not tried alternative models which might provide better fits for this dataset. If the training set seems large enough to use undersampling, we might want to try different models, such as tree-based or ensemble classifiers, before determining that oversampling is the better methodology.

---

### 12. BREAK (15 min)

---

### 13. Instructor Do: Combination Sampling (10 min)

One of the downsides of oversampling with SMOTE is that, because it doesn't see the overall distribution of the data, it can create new points from the data that are heavily influenced by outliers and therefor very noisy. As we've mentioned before, undersampling is not always an option due to small sample sizes. One way of dealing with these challenges is using a combination sampling strategy.

**Files:**

[combination_sampling.ipynb](Activities/06-Ins_Do_Combination_Sampling/Solved/combination_sampling.ipynb)

Advance through the slides to the combination sampling slide.

* The downsides of SMOTE can be overcome with an additional step.

* The ENN in SMOTEENN stands for the edited nearest neighbor rule, which looks at the labels for the sampled data and removes instances that are surrounded by data points of the other class. This prunes data points that are noisy (or at least indistinct).

Pause for questions, then open the solved notebook and go through the code.

* The generated data is imbalanced, but also notice that there is significant overlap between the two classes, which makes classification difficult.

* This quality of the data is also reflected in the SMOTE-sampled data, even though the two classes are balanced.

![comb_1](Images/comb_1.PNG)

* Now compare the SMOTE-sampled data to the SMOTEENN sampled data, which is significantly more differentiated and removes some of the outliers from each class.

![comb_2](Images/comb_2.PNG)

Walk through the rest of the code and pause for questions before moving on to the next activity.

### 14. Students Do: Combination Sampling (15 min)

In this activity, students will research and practice combination sampling with the imbalanced-learn library.

**Files:**

[combination_sampling.ipynb](Activities/07-Stu_Do_Combination_Sampling/Unsolved/combination_sampling.ipynb)

[README.md](Activities/07-Stu_Do_Combination_Sampling/README.md)

**Dataset**

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480. (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients#)

### 15. Instructor Review: Combination Sampling (5 min)

**Files:**

[combination_sampling.ipynb](Activities/07-Stu_Do_Combination_Sampling/Solved/combination_sampling.ipynb)

Open the solved notebook and go through the code. Since the structure of this activity is very similar to the oversampling activity, you should focus on the evaluation metrics from the combination sampling method.

### 16. Instructor Do: Precision-Recall Curve (10 min)

**Files:**

[pr_curve.ipynb](Activities/08-Ins_Do_Precision_Recall_Curve/Solved/pr_curve.ipynb)

Open the slides to precision-recall curves and cover the following points.

* In addition to changing the training sample to deal with imbalanced classes, we can also change the models that we use. Ensemble learners, which overweight instances of data that are infrequently seen or hard to classify, are better suited to imbalanced data. When we want to compare multiple models, classification metrics can become hard to use as as different models have different strengths.

* One alternative is the precision recall curve.

* Recalling that models classify binary outcomes by setting a threshold for the likelihood of the positive class - this is usually set at 50%, but can be higher or lower depending on whether false positives or negatives are more costly.

* The precision recall curve plots the precision and recall scores for a given model at different thresholds. For almost all models, an increase in precision (the % of predicted positives that are classified correctly) leads to a fall in recall (the % of actually true positives that are classified correctly).

* A model that has a curve which curves above another model (or, to put it another way, has a greater area under its PR curve), is the superior model.

Pause for questions, then continue on to the notebook.

* We compare two models - one is the logistic regression model using SMOTE oversampled data, and the other is the balanced random forest classifier (an ensemble learner which oversamples the smaller class) using the original training data. The classification metrics are shown below.

Logistic Regression:

![pr_2.png](Images/pr_2.PNG)

Balanced Random Forest:

![pr_3.png](Images/pr_3.PNG)

* At the default threshold, it looks like the two models perform similarly. However, depending on the relative cost of positive and false negatives, we might want to change the threshold. This is when a precision-recall curve becomes useful.

* The PR curve below shows that the random forest classifier outperforms the logistic regression model at almost all thresholds.

![pr_1.png](Images/pr_1.PNG)

### 17. Students Do: Credit Card Fraud (15 min)

In this activity, students will practice resampling techniques and use different models to classify credit card transactions as fraud or not fraud.

**Files:**

[cc_fraud.ipynb](Activities/09-Stu_Do_Credit_Card_Fraud/Unsolved/cc_fraud.ipynb)

[README.md](Activities/09-Stu_Do_Credit_Card_Fraud/README.md)

**Dataset:**

https://www.kaggle.com/mlg-ulb/creditcardfraud/downloads/creditcardfraud.zip/3

Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015

Dal Pozzolo, Andrea; Caelen, Olivier; Le Borgne, Yann-Ael; Waterschoot, Serge; Bontempi, Gianluca. Learned lessons in credit card fraud detection from a practitioner perspective, Expert systems with applications,41,10,4915-4928,2014, Pergamon

Dal Pozzolo, Andrea; Boracchi, Giacomo; Caelen, Olivier; Alippi, Cesare; Bontempi, Gianluca. Credit card fraud detection: a realistic modeling and a novel learning strategy, IEEE transactions on neural networks and learning systems,29,8,3784-3797,2018,IEEE

Dal Pozzolo, Andrea Adaptive Machine learning for credit card fraud detection ULB MLG PhD thesis (supervised by G. Bontempi)

Carcillo, Fabrizio; Dal Pozzolo, Andrea; Le Borgne, Yann-Aël; Caelen, Olivier; Mazzer, Yannis; Bontempi, Gianluca. Scarff: a scalable framework for streaming credit card fraud detection with Spark, Information fusion,41, 182-194,2018,Elsevier

Carcillo, Fabrizio; Le Borgne, Yann-Aël; Caelen, Olivier; Bontempi, Gianluca. Streaming active learning strategies for real-life credit card fraud detection: assessment and visualization, International Journal of Data Science and Analytics, 5,4,285-300,2018,Springer International Publishing

Bertrand Lebichot, Yann-Aël Le Borgne, Liyun He, Frederic Oblé, Gianluca Bontempi Deep-Learning Domain Adaptation Techniques for Credit Cards Fraud Detection, INNSBDDL 2019: Recent Advances in Big Data and Deep Learning, pp 78-88, 2019

Fabrizio Carcillo, Yann-Aël Le Borgne, Olivier Caelen, Frederic Oblé, Gianluca Bontempi Combining Unsupervised and Supervised Learning in Credit Card Fraud Detection Information Sciences, 2019

### 18. Instructor Review: Credit Card Fraud (5 min)

**Files:**

[cc_fraud.ipynb](Activities/09-Stu_Do_Credit_Card_Fraud/Solved/cc_fraud.ipynb)

For this review, go around the class and ask students which methods they tried, both in terms of sampling strategies as well as different algorithms. Which ones worked the best?Which didn't work so well? Which results were surprising?

After surveying the class, open the solved notebook and walk through our solution. Stress that this is only one (most likely non-optimal) way of solving the problem.

* We found the SMOTEENN sampling method to generate the best classification metrics when restricting the model to logistic regression. Note, however, that oversampling also produced high precision and recall scores for both classes, indicating that fraudulent and non-fraudulent transactions are relatively easily separable using these features.

* We chose a balanced random forest implementation for the ensemble model. The performance seems comparable to the logistic regression after resampling.

* The PR curve looks very similar, with the logistic regression results seemingly a little better at thresholds that produce higher recall - i.e., lower thresholds for predicting a the fraud class.

Ask students if there are any questions about this activity before ending the class.

### 19. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
