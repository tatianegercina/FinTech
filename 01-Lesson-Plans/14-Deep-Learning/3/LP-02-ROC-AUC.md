### 2. Instructor Do: Intro to the ROC Curve and AUC (15 min)

In this activity, students will learn how to measure the performance of a binary classification model by fetching metrics from Keras, as well as plotting and interpreting the ROC curve and AUC.

**Files:**

* [roc_auc_loans.ipynb](Activities/01-Ins_ROC_AUC/Solved/roc_auc_loans.ipynb)

* [transactions.csv](Activities/01-Ins_ROC_AUC/Resources/transactions.csv)

Explain to students that you will start Today's class by learning some advanced evaluation metrics, such as the ROC curve and AUC, that will be used to evaluate deep learning models.

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

* The value of `AUC` ranges from `0` to `1`. A model whose predictions are `100%` wrong has an `AUC = 0.0`; in contrast, a model whose predictions are `100%` correct has an `AUC = 1.0`.

Open the unsolved version of the Jupyter notebook and highlight the following while you live code the demo.

* For this demo, we will use a dataset that contains anonymous information about `284807` credit card transactions made by European credit cardholders in September 2013 to create a fraud detection model using a deep neural network.

* The dataset contains nine numerical variables, which are the result of PCA transformation to protect the confidentiality of credit cardholders. Only the transaction amount can be seen as is.

Import the dataset into a Pandas DataFrame called `transactions_df` and show the head.

![roc-auc-1](Images/roc-auc-1.png)

Continue the data preprocessing and highlight the following:

* The features set `X` will contain all the variables, from `V1` to `V9` and the `Amount`.

* The target vector `y` will contain the values of the `Class` column. It's set to `0` for non-fraudulent transactions, and to `1` for the fraudulent ones.

  ```python
  # Creating the X and y sets
  X = transactions_df.iloc[:, 0:10].values
  y = transactions_df["Class"].values
  ```

* Since the numerical features are in different scales, the `StandardScaler` from `sklearn` will be use to scaled the data of `X`.

  ```python
  # Import the StandardScaler from sklearn
  from sklearn.preprocessing import StandardScaler

  # Scale the data
  scaler = StandardScaler().fit(X)
  X = scaler.transform(X)
  ```

* Now that the data is scaled, the training, validation, and testing sets will be created using the `train_test_split` method from sklearn.

  ```python
  # Creating training, validation, and testing sets
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

  X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=78)
  ```

* We split the initial training set, to create a new training set to fit the model and a validation test which data is going to be used during the training process to verify the model's metrics.

* Now it's time to define our deep neural network, we will use a `Sequential` model and two `Dense` layers.

* First at all, we will define the number of inputs and the number of hidden nodes for each layer.

  ```python
  # Model set-up
  number_input_features = 10
  hidden_nodes_layer1 = 15
  hidden_nodes_layer2 = 5
  ```

* Next, we will define the model structure as follows.

  ```python
  # Define the LSTM RNN model
  model = Sequential()

  # Layer 1
  model.add(
      Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
  )

  # Layer 2
  model.add(Dense(units=hidden_nodes_layer2, activation="relu"))

  # Output layer
  model.add(Dense(1, activation="sigmoid"))
  ```

Explain to students that we are using the `sigmoid` activation function since we have a binary output, `1` for fraud or `0` for no-fraud.

Next the the model is compiled. Explain to students that the `binary_crossentropy` loss function is used since want to create a binary classification model.

Point out that we are defining some metrics to assess the model. These metrics are part of [the Keras metrics module](https://www.tensorflow.org/api_docs/python/tf/keras/metrics?version=stable) and that these are the same metrics students are already familiar from previous units when binary classification was introduced. The only new metric is `AUC` that will be explained next in the model's evaluation.

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

Time to fit the model! Explain to students that we will use a `batch_size = 1000` to speed-up the training process along `50` epochs. Point out that you are introducing the `validation_data` parameter to the `fit` method, explain to students that this parameter specifies a dataset that is used to validate the model's performance along the training process, excluding the validation data sample as training data.

```python
# Training the model
batch_size = 1000
epochs = 50
training_history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=epochs,
    batch_size=batch_size,
    verbose=1,
)
```

Execute the compilation code and highlight the following.

![roc-auc-2](Images/roc-auc-2.gif)

* Note that the training runs on `160203` samples and the validation on `53402` samples.

* As you can see, each epoch takes around `2` seconds, so running `50` epochs will take close to two minutes, so be patient.

* Also note that all the metrics are calculated on each epoch for the training and validation data. The validation metrics have the `val_` prefix.

* The model training results will be saved in the `training_history` variable for further analysis.

Continue the demo with the model performance assessment, explain to students that you will start by plotting two metrics that they are already familiar with: `loss` and `accuracy`. Highlight the following.

* The metrics results of the training process are stored in the `history` dictionary of the `training_history` object.

* You can access each metric using the names we define when compiling the model.

* To plot the metrics results, we are going to create a DataFrame using the `history` dictionary and plotting using the `plot()` method of the Pandas DataFrame.

  ![roc-auc-3](Images/roc-auc-3.png)

  ![roc-auc-4](Images/roc-auc-4.png)

Explain to students that the third metric to plot is `AUC` that stands for "Area Under the ROC Curve". Highlight the following.

![roc-auc-5](Images/roc-auc-5.png)

* The `AUC` value is better in the validation data and improves as the accuracy also increases.

* `AUC` may be desirable since it is scale-invariant. It measures how well predictions are ranked instead of their absolute values.

* `AUC` is classification-threshold-invariant. It measures the quality of the model's predictions regardless of the threshold.

Continue to the ROC curve plot. Explain to students that [`sklearn` has a method in the `metrics` module called `roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html) that calculates the values needed to plot the ROC curve for binary classification models. We will also going to use the `auc` method from `sklearn` in this part of the demo.

```python
# Import the roc_curve and auc metrics from sklearn
from sklearn.metrics import roc_curve, auc
```

Highlight the following as you continue live coding the demo.

* To create the ROC curve, it is crucial to get the predictions from the training and validation datasets.

  ```python
  # Making predictions to feed the roc_curve module
  train_predictions = model.predict(X_train, batch_size=1000)
  test_predictions = model.predict(X_test, batch_size=1000)
  ```

* The `roc_curve` method takes as parameters the actual labels and the predicted labels, to compute the false positive rate (`fpr`), true positive rate (`tpr`), and `thresholds`.

  ```python
  # Calculate the ROC curve and AUC for the training set
  fpr_train, tpr_train, thresholds_train = roc_curve(y_train, train_predictions)
  auc_train = auc(fpr_train, tpr_train)
  auc_train = round(auc_train, 4)

  # Calculate the ROC curve and AUC for the testing set
  fpr_test, tpr_test, thresholds_test = roc_curve(y_test, test_predictions)
  auc_test = auc(fpr_test, tpr_test)
  auc_test = round(auc_test, 4)
  ```

* Once we compute these values, we will use the `fpr` and `tpr` to create a pair of DataFrames to plot the ROC curve.

  ```python
  # Create a DataFrame with the fpr and tpr results
  roc_df_train = pd.DataFrame({"FPR Train": fpr_train, "TPR Train": tpr_train,})

  roc_df_test = pd.DataFrame({"FPR Test": fpr_test, "TPR Test": tpr_test,})
  ```

* We will plot the ROC curve using the `plot()` method from the Pandas DataFrame, we are also including the `AUC` value in the title for further analysis.

  ![roc-auc-6](Images/roc-auc-6.png)

* Plotting the training and testing data ROC curves is a visual technique to validate how the model behave with different data. It is also a way to see if my results with test data are relatively similar to train data or not.

* In this case both curves are quite similar, usually this is the expected behavior of the training and testing ROC curves.

Continue the demo by coding the model's evaluation using the `evaluate()` method. Explain to students that the evaluation results will be stored in the `scores` objetc that it's going to be used to create a `metrics` dictionary with the evaluation results.

![roc-auc-7](Images/roc-auc-7.png)

Point out to students that these are the results from the model's evaluation and that we will use these values for further analysis.

Continue the model's evaluation by creating a confusion matrix using the metrics obtained from the validation. A Pandas DataFrame is used to display the matrix.

![roc-auc-8](Images/roc-auc-8.png)

Next, the classification report is created using the `classification_report` method from `sklearn`.

![roc-auc-9](Images/roc-auc-9.png)

Finally, point out to students that these techniques can be used to compare the performance of a single model using different hyperparameters, as well as to compare different model for the same problem.

Answer any questions before moving on.

---
