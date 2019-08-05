## 6. Instructor Do: Oversampling

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
