### 7. Instructor Do: Evaluating Logistic Regression Predictions (5 min)

In this activity, students and instructor will engage in a facilitated discussion evaluating the results of logistic regression predictions. The focus of this activity will be the evaluation of diabetes predictions.

**Files**

* [Slides]()

Open the 11.1 slides, and highlight the following:

* We used a logistic regression model to predict whether or not an individual has diabetes, based off of a set of diagnostic metrics provided as a data set. The logistic regression model was validated using a scoring feature, revealing that the model is somewhat accurate. But can you trust that the prediction is correct?

  * Ask students how sure they are that their models can actually predict diabetes.

    * **Answer** 75 percent sure, as described by the scored accuracy.

  * Ask students if anyone would feel comfortable giving the diagnosis of diabetes based off of the predictions of the model. Why or why not?

    * **Answer** No. The prediction is not 100% accurate. There is room for error, as well as false positives.

  * Asks students if they'd rather have a model that incorrectly flags diabetes for patients that didn't actually have the disease, or would you rather miss predicting the disease in some patients? What is better: the **false positive** or **false negative**?

    * **Answer** Neither option is preferred. Both leave opportunity for inaccuracy.

    * **Answer** A model that incorrectly flags diabetes for patients that don't actually have the disease. Additional tests can be ran to refine the prediction and filter out individuals who do not have diabetes. This way, anyone with hte potential of having it can be given the treatment and attention they need.

* Explain to students that in order to evaluate a model, they must do more than score/measure the model for accuracy. In addition to **accuracy**, a model must be measured for **precision** and **recall**, both of which can be used to eliminate **false positives** and **false negatives**.

Ask if there are any questions before moving on.
