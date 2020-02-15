### 2. Instructor Do: Intro to the ROC Curve and AUC (10 min)

In this activity, students will learn how to assess the performance of a binary classification model by interpreting the ROC curve and AUC.

Explain to students that they will start Today's class by learning some advanced evaluation metrics, such as the ROC curve and AUC, that will be used to evaluate deep learning models.

Open the lesson slides and navigate to the "Introducing the ROC Curve and AUC" section and highlight the following:

* The confusion matrix is one method that can be used to assess the performance of a binary classification model.

  ![Confusion matrix components](Images/confusion-matrix.png)

* Let's recall the four components of this matrix:

  * TP (True Positives): Refers to the positive values that were correctly classified as positive by the model.

  * TN (True Negatives): Refers to the negative values that were correctly classified as negative by the model.

  * FP (False Positives): Refers to the negative values that were incorrectly classified as positive by the model.

  * FN (False Negatives): Refers to the positive values that were incorrectly classified as negative by the model.

* The ROC Curve and AUC are a couple of techniques that use the values from the confusion matrix to check and visualize the performance of a classification model

* ROC stands for "Receiver Operating Characteristic."

* The ROC curve shows the performance of a classification model as its discrimination threshold is varied.

* To plot a ROC curve, we use two parameters: true positive rate (`TPR` - also known as recall) and the false positive rate (`FPR`).

* The `TPR` is calculated as follows:

  ![rnn-sentiment-6](Images/rnn-sentiment-6.png)

* The `FPR` is calculated as follows:

  ![rnn-sentiment-7](Images/rnn-sentiment-7.png)

* Every point in the ROC curve represents the `TPR` Vs. `FPR` at different thresholds. The following image is a typical ROC Curve.

  ![ROC Curve](Images/roc-curve.png)

* Interpreting the ROC curve may be challenging; fortunately, we have the `AUC` that measures the area underneath the entire ROC curve (from `(0,0)` to `(1,1)`.

  ![AUC](Images/auc.png)

* The value of `AUC` ranges from `0` to `1`. A model whose predictions are `100%` wrong has an `AUC = 0.0`; in contrast, a model whose predictions are `100%` correct has an `AUC = 1.0`.

* An `AUC=1` is a paradox since it means that the model is perfect, but you may not trust in your model since it could be overfitted. A model with this `AUC` value correctly distinguishes between positive and negative classes.

* An `AUC=0.50` means that the model is unable to distinguish between positive and negative classes.

* Ideally, we may want to have `AUC` values ranging between `0` and `1`, where higher the AUC, better the model is at predicting `0s` as `0s` and `1s` as `1s`.

* So, a model with an `AUC=0.90` may be better than a model with an `AUC=0.65`.

  ![Different AUC values](Images/auc-for-roc-curves.png)

Explain to students that they will learn how to perform this analysis using python next. Answer any questions before moving on.

---
