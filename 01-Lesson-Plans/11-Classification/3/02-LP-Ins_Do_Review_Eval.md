### 2. Instructor Review: Model Evaluation (0:10 mins)

This activity will give students a chance to refresh the concepts of model evaluation, which we first went over in the first day of this unit. 

**Files:**

* Solved: [reiew_model_eval.ipynb](\Activities\01-Ins_Review_Eval_Metrics\Solved\review_model_eval.ipynb)

Walk through the first few blocks of the notebook. 

* We created two classes in this data, with two important features. First, one class is much larger than the other. Second, the classes have significant variation, so neither is cleanly distinguishable from the other.

![eval_1](\Images\eval_1.png)

* Using a logistic regression mode, we try to predict the class, purple or yellow, with the coordinates of a point. 

Ask a student to help you interpret the output of the confusion matrix. Refer to the powerpoint slide to reveal the correct answer.

![eval_2](\Images\eval_2.png)

* Looking only at this matrix, it seems that the model does reasonably well. While there are some false positives, the vast majority of data points are classified correctly. 

Move on to the next block, and ask a student to define the three metrics that are shown here. Once again, refer to the powerpoint slide to confirm the student's answers. 

![eval_3](\Images\eval_2.png)

* Precision is the proportion of predicted positives that are accurate. Recall is the proportion of actual positive that were predicted as positive. The F1 metric is a blended average of the two. 

Ask students to evaluate the performance of this model. How do they think it did?

* While the confusion matrix and evaluation metrics do give us some insight into performance, this is a bit of a trick question. Whether or not the model is "good" depends on context. What are we trying to predict? What are the cost of false positives, or false negatives?