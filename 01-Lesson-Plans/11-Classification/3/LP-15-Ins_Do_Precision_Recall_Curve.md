## 15. Instructor Do: Precision-Recall Curve

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

![pr_2.png](Images/pr_2.png)

Balanced Random Forest:

![pr_3.png](Images/pr_3.png)

* At the default threshold, it looks like the two models perform similarly. However, depending on the relative cost of positive and false negatives, we might want to change the threshold. This is when a precision-recall curve becomes useful. 

* The PR curve below shows that the random forest classifier outperforms the logistic regression model at almost all thresholds. 

![pr_1.png](Images/pr_1.png)

