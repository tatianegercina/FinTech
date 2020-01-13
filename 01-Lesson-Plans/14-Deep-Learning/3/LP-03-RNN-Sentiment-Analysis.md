### 3. Instructor Do: RNNs for NLP - Sentiment Analysis (15 min)

In this activity, students will learn how to define an LSTM RNN model for sentiment analysis using Keras. Also, data preparation for using LSTM models for natural language processing is introduced.

**Files:**

* [austin_coffee_sentiment.ipynb](Activities/01-Ins_Sentiment_Analysis/Solved/austin_coffee_sentiment.ipynb)

* [austin_coffee_shops_reviews.csv](Activities/01-Ins_Sentiment_Analysis/Resources/austin_coffee_shops_reviews.csv)

Explain to students that you will start exploring the LSTM RNNs by creating a model for sentiment analysis using the Keras API of TensorFlow.

Open the unsolved Jupyter notebook, live code the solution, and highlight the following.

* For this demo, we are going to use a dataset that contains `6878` customer reviews of Coffee Shops at Austin, Texas. The reviews were taken from Yelp; however, the names of the Coffee Shops were anonymized for privacy reasons.

* The dataset has the following columns:

  * `coffee_shop_name`: The anonymized name of the coffee shop.

  * `full_review_text`: The customers reviews.

  * `sentiment`: The sentiment of each customer's review. `0` - Negative, `1` - Positive.

Create a new Pandas DataFrame named `reviews_df` and load the data from the `CSV` file provided.

![rnn-sentiment-1](Images/rnn-sentiment-1.png)

* As you can see, the names of the coffee shops are anonymized, the review comments are in plain English, and the sentiment of each customer review is already scored as positive (`1`) or negative (`0`).

Explain to students that RNNs, like any other neural network model, require an array data type, so the `full_review_text` column will be transformed into the `X` array and the "sentiment" column into the `y` array.

```python
# Creating the X and y vectors
X = reviews_df["full_review_text"].values
y = reviews_df["sentiment"].values
```

Explain to students that to train the RNN model, the text data should be encoded as an integer. This transformation can be done using [the Keras preprocessing modules](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing).

Import the `Tokenizer` and `pad_sequences` modules and highlight the following.

```python
# Import Keras modules for data encoding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
```

* The customers' review comments need to be tokenized by creating a `Tokenizer` object and fitting it with all the text comments in the `X` variable.

  ```python
  # Create an instance of the Tokenizer and fit it with the X text data
  tokenizer = Tokenizer(lower=True)
  tokenizer.fit_on_texts(X)
  ```

* We will use `lower=True` argument to convert all the text into lowercase to ensure data consistency.

* The `Tokenizer` object generates a dictionary that creates a list of words (tokens) that maps every unique word in the text with a unique integer. This list is going to be an encoded dictionary of the universe of particular words in the dataset; this dictionary is similar to the bag of words technique described in the NLP Unit.

  ```python
  # Print the first five elements of the encoded vocabulary
  for token in list(tokenizer.word_index)[:5]:
    print(f"word: '{token}', token: {tokenizer.word_index[token]}")
  ```

* Once the list of tokens is created, we need to transform every text review comment into a numerical sequence; this task is accomplished using the `texts_to_sequences()` method.

  ![rnn-sentiment-2](Images/rnn-sentiment-2.png)

* First, the text should be tokenized by fitting the Tokenizer class on the data set. As you can see, I use "lower = True" argument to convert the text into lowercase to ensure consistency of the data. Afterward, we should map our list of words (tokens) to a list of unique integers for each unique word using texts_to_sequences class.

* The RNN model requires that all the values of the `X` vector have the same length; the `pad_sequences` method will ensure that all integer encoded reviews have the same size. Each entry in `X` will be shortened to `140` integers, or pad with `0's` in case it's shorter.

  ```python
  # Padding sequences
  X_pad = pad_sequences(X_seq, maxlen=140, padding="post")
  ```

Explain to students that once the data is encoded, we will create training, validation, and testing sets.

```python
# Creating training, validation, and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_pad, y, random_state=78)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=78)
```

Highlight the following about these sets:

* First of all, we create the training and testing sets as we usually do.

* The next step is to create the validation set, we split the initial training set, to create a new training set to fit the model and a validation test which data is going to be used during the training process to verify the model's metrics.

Now it's time to start building the model using Keras. Explain to students that we will use the `Sequential` as have been done before; however, there are two new types of layers that are needed: `Embedding` and `LSTM`.

```python
# Import Keras modules for model creation
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
```

Highlight the following about these new types of layers.

* [`Embedding` layer](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding?version=stable): It's a type of layer that is used in neural networks to process encoded text data.

* [`LSTM` layer](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM?version=stable): It's used to add an LSTM layer to the model.

Explain to students that the `Embedding` layer requires at least three parameters as follows. The `vocabulary_size` refers to the size of the vocabulary in the text that is going to be processed; this variable is set at the total number of words in the `tokenizer` dictionary plus `1`. The second parameter needed by this layer is the `input_length`; this parameter is set at `140` (`max_words` variable) that is the value defined for padding the reviews. Finally, the third parameter is the `embedding_size`; this parameter specifies how many dimensions will be used to represent each word. As a rule-of-thumb, a multiple of eight could be used; for this demo, tuning the model value `64` delivered the best result.

```python
# Model set-up
vocabulary_size = len(tokenizer.word_counts.keys()) + 1
max_words = 140
embedding_size = 64
```

After setting these initial variables, the model's structure is defined. Explain to students that the LSTM RNN model will have two layers, start coding the model structure and comment on the following.

```python
# Define the LSTM RNN model
model = Sequential()

# Layer 1
model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))

# Layer 2
model.add(LSTM(units=280))

# Output layer
model.add(Dense(1, activation="sigmoid"))
```

* The model is defined as a `Sequential` instance.

* The first layer is an `Embedding` type, this layer process the integer-encoded sequence of each review comment to create a dense vector representation that will be used by the `LSTM` layer.

* Next, we add an `LSTM` layer with `280` units (the double of the `max_words` variable as initial test value). This layer transforms the dense vector into a single vector that contains information about the entire sequence that will be used by the activation function in the `Dense` layer to score the sentiment.

* Potentially, adding more `LSTM` layers and input units can lead to better results.

* Finally, we add a `Dense` output layer with a sigmoid activation function to predict the probability of a review being positive.

After defining our LSTM RNN, it's time to compile the model. Explain to students that we will include several metrics to verify the model's performance during the training phase using the validation test.

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
  tf.keras.metrics.Recall(name="recall")
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

Continue the demo with the model performance assessment, explain to students that you will plot four metrics that they are already familiar with: `loss`, `accuracy`, `precision`, and `recall`. Highlight the following.

* The metrics results of the training process are stored in the `history` dictionary of the `training_history` object.

* You can access each metric using the names we define when compiling the model.

* To plot the metrics results, we are going to create a DataFrame using the `history` dictionary and plotting using the `plot()` method of the Pandas DataFrame.

  ![rnn-sentiment-4](Images/rnn-sentiment-4.png)

  ![rnn-sentiment-5](Images/rnn-sentiment-5.png)

  ![rnn-sentiment-12](Images/rnn-sentiment-12.png)

  ![rnn-sentiment-13](Images/rnn-sentiment-13.png)

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
