### 7. Students Do: Sentiment Analysis - RNNs Vs. Vader (30 min)

In this activity, students will use two different models to score sentiment. The goal is to put the performance metrics and techniques students have learned into action to decide which model performs better between VADER and RNN LSTM.

**Instructions:**

* [README.md](Activities/03-Stu_RNN_Vader/README.md)

**Files:**

* [rnn_vs_vader.ipynb](Activities/03-Stu_RNN_Vader/Unsolved/rnn_vs_vader.ipynb)

* [movie_comments.csv](Activities/03-Stu_RNN_Vader/Resources/movie_comments.csv)

---

### 8. Instructor Do: Review Sentiment Analysis - RNNs Vs. Vader (10 min)

**Files:**

* Unsolved version [rnn_vs_vader.ipynb](Activities/03-Stu_RNN_Vader/Unsolved/rnn_vs_vader.ipynb)

* Solved version: [rnn_vs_vader.ipynb](Activities/03-Stu_RNN_Vader/Solved/rnn_vs_vader.ipynb)

* Dataset: [movie_comments.csv](Activities/03-Stu_RNN_Vader/Resources/movie_comments.csv)

Open the unsolved version of the Jupyter notebook, live code the solution and highlight the following:

* Scoring sentiment is adding value to financial decisions nowadays, that's why it's important to know how to score sentiment using different models.

* We used a dataset about movie reviews in this activity, but also we can use news feeds, blogs, or social media to score sentiment.

* The goal of this activity is to compare the performance of VADER sentiment Vs. an RNN LSTM model to decide which one could be better to score sentiment.

* As you already know, VADER is a natural language processing technique, whereas RNN LSTM models are a kind of deep neural networks. To compare these two models we will use some metrics that could help us to assess which model performs better.

* First at all, to compare models it's important to set the random seed of `numpy` and `tensoflow` to ensure reproducibility.

  ```python
  # Set the random seed for reproducibility
  from numpy.random import seed
  seed(1)

  from tensorflow import random
  random.set_seed(2)
  ```

* After loading the dataset into the `df_reviews` DataFrame, we define the features set `X` and the target vector `y` by assigning the `comment` column to `X` and the `sentiment` column to `y`.

  ```python
  # Create the features set (X) and the target vector (y)
  X = df_reviews["comment"].values
  y = df_reviews["sentiment"].values
  ```

* To make the model comparison fair, we will use the same training and testing data. We will use the the `train_test_split` method from `sklearn` to create the training, testing, and validation sets. Remember that it's crucial to set the `random_state` parameter for reproducibility.

  ```python
  # Create the train, test, and validation sets
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)

  X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=3)
  ```

* First, we will score the sentiment using VADER, the same technique we learn in the NLP unit.

* As a good practice, we will download or update the VADER lexicon.

  ```python
  # Download/Update the VADER Lexicon
  nltk.download('vader_lexicon')
  ```

* Next, an instance of the `SentimentIntensityAnalyzer` from `nltk` is created to score the sentiment of every movie review using VADER.

  ```python
  # Initialize the VADER sentiment analyzer
  analyzer = SentimentIntensityAnalyzer()
  ```

* We create two lists to store the sentiment scoring results.

  ```python
  # Define two lists to store vader sentiment scoring
  y_vader_pred = []
  y_vader_prob = []
  ```

* We will use the `y_vader_pred` list to save the sentiment scored by VADER as  `1` for positive, and `0` for negative.

* To plot the ROC Curve, we need the predicted probability of a review to be positive, so we will use the `y_vader_prob` list to store the value of the `pos` polarity score computed by VADER for each review comment.

* Using a `for` loop, we iterate across all the review comments in the `X` set to score the sentiment using VADER.

  ```python
  # Score sentiment of test set using Vader
  for comment in X_test:
      y_vader_prob.append(analyzer.polarity_scores(comment)["pos"])
      sentiment_score = analyzer.polarity_scores(comment)["compound"]
      if sentiment_score >= 0.1:
          y_vader_pred.append(1)
      else:
          y_vader_pred.append(0)
  ```

* Since we want to compare these two models on scoring sentiment as positive or negative, we need a way to interpret the polarity scores given by VADER.

* Following some recommendations of NLP researchers, we define a threshold of `0.1` to label a review as positive, if the `compound` score is greater or equal than `0.1`, the review comment will be positive (append `1` to `y_vader_pred`); if the `compound` score is below `0.1`, the review comment will be negative (append `0` to `y_vader_pred`).

* Once we score the sentiment using VADER, we need to normalize the values of the `y_vader_prob` list. We will use the min-max normalization algorithm.

* We can apply the min-max normalization algorithm by using the `MinMaxScaler` method from `sklearn` as follows:

  ```python
  # Option 1: Normalizing data using MinMaxScaler from sklearn
  from sklearn.preprocessing import MinMaxScaler

  scaler = MinMaxScaler()
  scaler.fit(np.array(y_vader_prob).reshape(-1,1))
  y_vader_prob_norm = scaler.transform(np.array(y_vader_prob).reshape(-1,1))
  ```

* Also, we may want to manually code the min-max algorithm using a comprehension list as follows:

  ```python
  # Option 2: Using a comprehension list
  normalized = [(x - min(y_vader_prob)) / (max(y_vader_prob) - min(y_vader_prob))
                for x in y_vader_prob]
  ```

* Either method you use, will lead to the same results of normalizing the values between `0` and `1`. We will consider the first approach for this demo.

* At this time, we have the original sentiments in `y_test`, the predicted sentiment classes in `y_vader_pred`, and the sentiment predictions in `y_vader_prob`. Not we will continue to score sentiment using an RNN LSTM model.

* As you know, RNN LSTM models work with numerical data, so need to encode the text data on the review comments to a numerical representation.

* We start by encoding the vocabulary of the dataset using the `Tokenizer` method from Keras.

  ```python
  # Import the Tokenizer method from Keras
  from tensorflow.keras.preprocessing.text import Tokenizer

  # Create an instance of the Tokenizer and fit it with the X text data
  tokenizer = Tokenizer(lower=True)
  tokenizer.fit_on_texts(X)
  ```

* For testing proposes, we print the first five elements of the encoded vocabulary.

  ![Sample encoded words using the Tokenizer method from Keras](Images/movie-reviews-encoded-vocabulary.png)

* Next, we transform all the review comments to numerical sequences using the `text_to_sequences()` method of the `Tokenizer`.

  ```python
  # Transform the text data to numerical sequences
  X_seq = tokenizer.texts_to_sequences(X)
  ```

* For testing proposes, we compare the text representation of a movie review with its numerical representation, by printing the first text review in `X` and the first encoded element in `X_seq`.

  ![Contrast of a move review comment as text and as numerical sequence](Images/text-vs-sequence.png)

* As you know, RNN LSTM models need equal size inputs, so that, we will pad the sequences stored in `X_pad` up to `140` integers using the `pad_sequences` method from Keras.

```python
# Import the pad_sequences method from Keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set the pad size
max_words = 140

# Pad the sequences using the pad_sequences() method
X_pad = pad_sequences(X_seq, maxlen=max_words, padding="post")
```

* We may use a bigger padding size; however, using a bigger value will increase the time that takes fitting the RNN LSTM model.

* After preparing the date, we create training, validation, and testing sets using the `train_test_split` method from `sklearn`.

  ```python
  # Creating training, validation, and testing sets using the encoded data
  X_train_rnn, X_test_rnn, y_train_rnn, y_test_rnn = train_test_split(X_pad, y, random_state=3)

  X_train_rnn, X_val_rnn, y_train_rnn, y_val_rnn = train_test_split(X_train_rnn, y_train_rnn, random_state=3)
  ```

* Now we can define the structure of the RNN LSTM model, since we will use an `Embedding` layer, we need to set the `input_dim` parameter to the size of the vocabulary, and define an embedding size, so we set the following initial configuration variables.

  ```python
  # Model set-up
  vocabulary_size = len(tokenizer.word_counts.keys()) + 1
  embedding_size = 64
  ```

* We will define an RNN LSTM model with three layers as follows:

  * _Layer 1:_ Add an `Embedding` layer using the `vocabulary_size` and `embedding_size` variables as the first two parameters, and setting `input_length=max_words` (the same size as the padding).

  * _Layer 2:_ Add an LSTM layer with `280` units.

  * _Output Layer:_ Add a `Dense` layer with `1` unit and `sigmoid` as activation function.

    ```python
    # Define the LSTM RNN model
    model = Sequential()

    # Layer 1
    model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))

    # Layer 2
    model.add(LSTM(units=280))

    # Output layer
    model.add(Dense(units=1, activation="sigmoid"))
    ```

* We compile the model using the `binary_crossentropy` loss function, the `adam` optimizer, and fetch the following metrics: Accuracy, True positives, True negatives, False positives, False negatives, Precision, Recall, and AUC.

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

* Once the model is compiled, it's training time. We will train this model along `10` epochs with a batch size of `1000`.

  ```python
  # Training the model
  batch_size = 1000
  epochs = 10
  model.fit(
      X_train_rnn,
      y_train_rnn,
      validation_data=(X_val_rnn, y_val_rnn),
      epochs=epochs,
      batch_size=batch_size,
      verbose=1,
  )
  ```

At this point of the solution review, switch to the solved version to continue by doing a dry walkthrough of the code since fitting the model takes up to 10 minutes. Highlight the following.

* Once the model training finishes, we predict the classes using the testing data to start the model comparison.

  ```python
  # Predict classes using the testing data
  y_rnn_pred = model.predict_classes(X_test_rnn, batch_size=1000)
  ```

* Now, we have sentiment scoring with both models, it's time to compare their performance.

* We start by comparing the models' accuracy using the `accuracy_score` method from `sklearn`.

  ![Comparing models accuracy](Images/vader-rnn-accuracy.png)

* At this point, the RNN LSTM model looks better since it has a higher accuracy, let's take a look to the confusion matrices of this two models; we use the `confusion_matrix` method from `sklearn` for this task.

* Using the `confusion_matrix` method, and passing as parameters the sentiments from the testing data and the sentiments scored by both models, we gather the data needed to create and display a confusion matrix using a Pandas DataFrame.

  ![Confusion matrix for VADER](Images/confusion-matrix-vader.png)

  ![Confusion matrix for VADER](Images/confusion-matrix-rnn.png)

* After reviewing both confusion matrices, we observe that once again the RNN LSTM model performs betters since it has less false positives and false negatives.

* Another interesting tool for comparing binary classifications models is the `classification_report` from `sklearn`, since we can analyze metrics such as precision, recall, and the F1-score.

  ![Comparison of the classification report of both models](Images/rnn-vader-classification-reports.png)

* Again, the RNN LSTM model performs better, specially by observing the F1-score.

* Finally, we make a visual analysis of model performance by plotting the ROC curve and computing the AUC. We use the `roc_curve` and `auc` methods from `sklearn`

  ```python
  # Import the roc_curve and auc metrics from sklearn
  from sklearn.metrics import roc_curve, auc
  ```

* We start by plotting the ROC curve for VADER, we use the `roc_curve` method to compute the false positive rate (fpr) and true positive rate (tpr).

  ```python
  # Data for ROC Curve - VADER
  fpr_test_vader, tpr_test_vader, thresholds_test_vader = roc_curve(y_test, y_vader_prob_norm)
  ```

* After calculating the `fpr` and `tpr` for VADER, we use the `auc` method of `sklearn` to calculate the AUC for VADER. Next, we Round the final result up to `4` decimals.

  ```python
  # AUC for VADER
  auc_test_vader = auc(fpr_test_vader, tpr_test_vader)
  auc_test_vader = round(auc_test_vader, 4)
  ```

* Once we fetch all the data needed to plot the ROC curve, we create a DataFrame with the `fpr` and `tpr` data from VADER and we plot the curve using the `plot()` method of the DataFrame.

  ```python
  # Dataframe to plot ROC Curve for VADER
  roc_df_test_vader = pd.DataFrame({"FPR Test": fpr_test_vader, "TPR Test": tpr_test_vader,})

  roc_df_test_vader.plot(
      x="FPR Test",
      y="TPR Test",
      color="red",
      style="--",
      xlim=([-0.05, 1.05]),
      title=f"Test ROC Curve - Vader (AUC={auc_test_vader})",
  )
  ```

  ![ROC Curve for VADER](Images/roc-curve-vader.png)

* After creating the ROC curve for the RNN LSTM mode, we need to make predictions using the `predict()` method of the model and the testing data.

  ```python
  # Making predictions to feed the roc_curve module
  test_predictions_rnn = model.predict(X_test_rnn, batch_size=1000)
  ```

* Next, we use the `roc_curve` method to compute the false positive rate (fpr) and true positive rate (tpr) for the RNN LSTM model.

  ```python
  # Data for ROC Curve - RNN LSTM Model
  fpr_test_rnn, tpr_test_rnn, thresholds_test_rnn = roc_curve(y_test_rnn, test_predictions_rnn)
  ```

* Now, we calculate the AUC for the RNN LSTM model as we did for VADER.

  ```python
  # AUC for the RNN LSTM Model
  auc_test_rnn = auc(fpr_test_rnn, tpr_test_rnn)
  auc_test_rnn = round(auc_test_rnn, 4)
  ```

* Finally, we create a DataFrame with the `fpr` and `tpr` data and plot the curve using the same process as with VADER.

  ```python
  # Dataframe to plot ROC Curve for the RNN LSTM model
  roc_df_test_rnn = pd.DataFrame({"FPR Test": fpr_test_rnn, "TPR Test": tpr_test_rnn,})

  roc_df_test_rnn.plot(
      x="FPR Test",
      y="TPR Test",
      color="blue",
      style="--",
      xlim=([-0.05, 1.05]),
      title=f"Test ROC Curve (AUC={auc_test_rnn})",
  )
  ```

  ![ROC Curve for the RNN LSTM model](Images/roc-curve-rnn-lstm.png)

* Now we have enough metrics to have a final conclusion about these two models performance.

* After reviewing the results, we can conclude that the RNN LSTM model has a better performance to score sentiment. The RNN model has a higher accuracy and `F1` score values. Also, its ROC Curve plot has a better shape whose area under the curve (AUC) is very close to `1`.

* Comparing models is a crucial part to make decision using machine learning algorithms, since you may want to be sure to deploy the best model for your data and for the context of your business scenario.

* You can use the techniques you employ in this activity to compare any type of binary classification algorithms, such as models to score the decision of buy or sell in a trading algorithm, or the decision to increase or decrease the sell price of a house in real state.

Answer any questions before moving on.

---
