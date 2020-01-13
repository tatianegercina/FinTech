### 6. Instructor Do: Intro to the ROC Curve and AUC (15 min)

In this activity, students will learn how to measure the performance of a binary classification from by fetching metrics from keras to plot and interpret the ROC curve and AUC.

**Files:**

* [austin_coffee_sentiment.ipynb](Activities/03-Ins_ROC_AUC/Solved/austin_coffee_sentiment.ipynb)

* [austin_coffee_shops_reviews.csv](Activities/03-Ins_ROC_AUC/Resources/austin_coffee_shops_reviews.csv)

Explain to students that besides the metrics you gather from Keras in the previous activity, there are some additional ones that can be used to assess the performance of a classification model.

Open the lesson slides and navigate to the "Introducing ROC Curve and AUC" section and highlight the following:

* ROC stands for "Receiver Operating Characteristic".

* The ROC curve shows the performance of a classification model as its discrimination threshold is varied.

* To plot a ROC curve, we use two parameters: true positive rate (`TPR` - also known as recall) and the false positive rate (`FPR`).

* The `TPR` is calculated as follows:

  ![rnn-sentiment-6](Images/rnn-sentiment-6.png)

* The `FPR` is calculated as follows:

  ![rnn-sentiment-7](Images/rnn-sentiment-7.png)

* Every point in the ROC curve represents the `TPR` Vs. `FPR` at different thresholds. The following image a typical ROC Curve.

  ![ROC Curve](Images/roc-curve.png)

* Interpreting the ROC curve may be challenging; fortunately, we have the `AUC` that measures the area underneath the entire ROC curve (from `(0,0)` to `(1,1)`.

  ![AUC](Images/auc.png)

* The value of `AUC` ranges from `0` to `1`. A model whose predictions are `100%` wrong has an `AUC=0.0` of 0.0; in contrast, a model whose predictions are `100%` correct has an `AUC=1.0`.

Point out that these metrics are part of [the Keras metrics module](https://www.tensorflow.org/api_docs/python/tf/keras/metrics?version=stable) and that these are the same metrics students are already familiar from previous units when binary classification was introduced. The only new metric is `AUC` that will be explained next in the model's evaluation.

Explain to students that the `name` parameter is used to quickly identify each parameter during the training process and the model evaluation phase.

```python
# Compile the model
model.compile(
 loss="binary_crossentropy",
 optimizer="adam",
 metrics=[
 "accuracy",
 tf.keras.metrics.TruePositives(name="tp"),
 tf.keras.metrics.TrueNegatives(name="tn"),
 tf.keras.metrics.FalsePositives(name="fp"),
 tf.keras.metrics.FalseNegatives(name="fn"),
 tf.keras.metrics.Precision(name="precision"),
 tf.keras.metrics.Recall(name="recall"),
 tf.keras.metrics.AUC(name="auc"),
 ],
)
```

Time to fit the model! Explain to students that we will use a `batch_size = 1000` to speed-up the training process along `10` epochs. Point out that you are introducing the `validation_data` parameter to the `fit` method, explain to students that this parameter specifies a dataset that is used to validate the model's performance along the training process, excluding the validation data sample as training data.

```python
# Training the model
batch_size = 1000
training_history = model.fit(
 X_train,
 y_train,
 validation_data=(X_val, y_val),
 epochs=10,
 batch_size=batch_size,
 verbose=1,
)
```

Execute the compilation code and highlight the following.

![rnn-sentiment-3](Images/rnn-sentiment-3.gif)

* Note that the training runs on `3868` samples and the validation on `1290` samples.

* As you can see, each epoch takes around `20` seconds, so running `10` epochs will take close to five minutes, so be patient.

* Also note that all the metrics are calculated on each epoch for the training and validation data. The validation metrics have the `val_` prefix.

* The model training results will be saved in the `training_history` variable for further analysis.

Continue the demo with the model performance assessment, explain to students that you will start by plotting two metrics that they are already familiar with: `loss` and `accuracy`. Highlight the following.

* The metrics results of the training process are stored in the `history` dictionary of the `training_history` object.

* You can access each metric using the names we define when compiling the model.

* To plot the metrics results, we are going to create a DataFrame using the `history` dictionary and plotting using the `plot()` method of the Pandas DataFrame.

  ![rnn-sentiment-4](Images/rnn-sentiment-4.png)

  ![rnn-sentiment-5](Images/rnn-sentiment-5.png)

Explain to students that the third metric to plot is AUC that stands for Area Under the ROC Curve.

Come back to the Jupyter notebook and plot the value of `AUC` along the training process.

![rnn-sentiment-8](Images/rnn-sentiment-8.png)

Explain to students that as they can note, the `AUC` value is better in the validation test and improves as the accuracy also increases.

Highlight the following about using `AUC` to assess a model's performance.

* `AUC` is may be desirable since it's scale-invariant. It measures how well predictions are ranked instead of their absolute values.

* `AUC` is classification-threshold-invariant. It measures the quality of the model's predictions regardless of the threshold.

Explain to students that [`sklearn` has a method in the `metrics` module called `roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html) that calculates the values needed to plot the ROC curve for binary classification models.

Point out that we will use this method along with `matplotlib` to plot the ROC curve as follows.

```python
# Create a function to plot the ROC Curve
from sklearn.metrics import roc_curve

def plot_roc(name, labels, predictions, **kwargs):
 fpr, tpr, thresholds = roc_curve(labels, predictions)

 plt.plot(fpr, tpr, label=name, linewidth=2, **kwargs)
 plt.xlabel("False positives rate")
 plt.ylabel("True positives rate")
 plt.title("ROC Curve")
 plt.xlim([0,1])
 plt.ylim([0,1])
 plt.grid(True)
 ax = plt.gca()
 ax.set_aspect("equal")
```

Explain to students that the `roc_curve` method takes as parameters the actual labels and the predicted labels, to compute the false positive rate (`fpr`), true positive rate (`tpr`), and thresholds. Once we compute these values, we use the `fpr` and `tpr` to create the plot.

Highlight the following about creating the ROC curve.

* After creating the plot, we need to make some predictions using the training and testing data.

* We will use the `predict()` method of the LSTM RNN model that will return a vector with the probability of each review comment to be positive (`1`).

* To create the ROC curve, it's crucial to have the same number of predictions with the training and validation datasets, so a `batch_size=1000` is defined.

  ```python
  # Making predictions to feed the roc_curve module
  train_predictions = model.predict(X_train, batch_size=1000)
  test_predictions = model.predict(X_test, batch_size=1000)
  ```

* Once we have the prediction, we create the ROC curve plot by calling the `plot_roc` function that we defined.

  ![ROC curve plot](Images/roc-curve-plot.png)

Continue the demo by coding the model evaluation using the `evaluate()` method. Explain to students that the evaluation results will be stored in the `scores` that it's going to be used to create a `metrics` dictionary with the evaluation results.

![rnn-sentiment-9](Images/rnn-sentiment-9.png)

Point out to students that these are the results from the model's evaluation and that we will use these values for further analysis.

Continue the model's evaluation by creating a confusion matrix using the metrics obtained from the validation. A Pandas DataFrame is used to display the matrix.

![rnn-sentiment-10](Images/rnn-sentiment-10.png)

Now it's time to test our model by making some predictions. To do that, explain to students that we are going to use a sample of ten integer-encoded review comments from the testing set.

To predict the sentiment of each review comment, point out that we will use the `predict_classes()` method that returns the predicted class.

```python
# Make sentiment predictions
predicted = model.predict_classes(X_test[:10])
```

Finally, a DataFrame is created with the actual and predicted sentiments to contrast the prediction results versus the actual values.

![rnn-sentiment-11](Images/rnn-sentiment-11.png)

Answer any questions before moving on.

---
