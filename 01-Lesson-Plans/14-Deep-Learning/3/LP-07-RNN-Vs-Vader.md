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

* We define a threshold of `0.1` to label a review as positive, if the `compound` score is greater or equal than `0.1`, the review comment will be positive (append `1` to `y_vader_pred`); if the `compound` score is below `0.1`, the review comment will be negative (append `0` to `y_vader_pred`).
