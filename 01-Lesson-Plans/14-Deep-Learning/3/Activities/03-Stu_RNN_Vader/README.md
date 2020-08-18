# Student Do: Sentiment Analysis - RNNs vs. VADER

In this activity you will use two different models to score sentiment, using the performance metrics and techniques you've learned in order to decide which model performs better: VADER or RNN LSTM.

## The Dataset: IMBD Movie Reviews

The dataset provided contains `25000` movie reviews based on [the data shared by Andrew Mass from Stanford University](http://ai.stanford.edu/~amaas/data/sentiment/).

The movie reviews are split evenly into `12500` positive reviews and `12500` negative reviews.

You can learn more about this dataset in the following research paper: [Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng and Christopher Potts. (2011). **Learning Word Vectors for Sentiment Analysis**. The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011)](http://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf).

## Instructions

Use the starter notebook and complete the following tasks.

### Data Preprocessing

1. Load the provided dataset in a Pandas DataFrame entitled `df_reviews` and show the first `10` records.

2. Create the features set `X` and the target vector `y` by assigning the `comment` column to `X` and the `sentiment` column to `y`.

3. Use the `train_test_split` method from `sklearn` to create the training, testing, and validation sets.

## Scoring Sentiment Using VADER

In this section, you will use VADER sentiment from the `nltk` library to score the sentiment of the testing set. Later, you will assess model performance using metrics such as accuracy, precision, and recall, among others.

1. Start by downloading or updating the VADER lexicon.

2. Create an instance of the `SentimentIntensityAnalyzer` and name it `analyzer`.

3. Define two lists to store the sentiment scoring results, as follows:

  * `y_vader_pred` will save the scored sentiment, `1` for positive or `0` for negative.

  * `y_vader_prob` will store the normalized value of the `pos` polarity score.

4. Create a `for` loop to iterate across all the comments in the `X` set and score the sentiment of each review comment. Update the two lists for sentiment scores as follows:

  * Append the `pos` score to the `y_vader_prob`; you will normalize this list's values later.

  * To score a review comment as positive or negative, we will use the `compound` polarity score. As you may remember from the NLP unit, the `compound` score ranges between `-1` (most extreme negative) and `+1` (most extreme positive). Following the recommendations from [this research paper](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1051&context=datasciencereview), we will define a threshold of `0.1` to label a review as positive, if the `compound` score is greater than or equal to `0.1`, the review comment will be positive (append `1` to `y_vader_pred`); if the `compound` score is below `0.1`, the review comment will be negative (append `0` to `y_vader_pred`).

You will use the values from the `pos` polarity score to plot the ROC curve; we will consider the `pos` score as the probability of a review comment to be positive. To plot the ROC curve, these probabilities should range from `0` to `1`, so the values of the `y_vader_prob` list will be normalized using [min-max normalization](https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)).

* Normalize the data stored in the `y_vader_prob` list and save the resulting normalized values in a variable called `y_vader_prob_norm`.

_Hint:_ To normalize the data, you can use the `MinMaxScaler` method from `sklearn`, or you can code the min-max normalization formula using a comprehension list.

## Scoring Sentiment Using RNN LSTM

In this section, you will build an RNN LSTM model to score the sentiment of the review comments. You will fit the model using the training and validation sets, and finally, you will get some predictions using the testing set for further performance assessment and comparison with VADER.

1. Start encoding the review comments using the `Tokenizer` method from Keras.

2. Create an instance of the `Tokenizer`, and fit it with all the review comments that you stored in `X`.

3. For testing proposes, print the first five elements of the encoded vocabulary created with the `Tokenizer`.

4. To fit the RNN LSTM model for sentiment scoring, the text data in `X` should be encoded as sequences. Use the `text_to_sequence()` method of the `tokenizer` to transform the text data to numerical sequences, and save the sequences in a variable called `X_seq`.

5. For testing proposes, compare the text representation of a movie review with its numerical representation, by printing the first text review in `X` and the first encoded element in `X_seq`.

6. Recall that RNN LSTM models need equal size inputs, so that, pad the sequences stored in `X_pad` up to `140` integers using the `pad_sequences` method from Keras. Store the pad size in a variable called `max_words`.

**Note:** You may use a bigger padding size; however, using a bigger value will increase the time that takes fitting the RNN LSTM model.

### Create the Training, Validation, and Testing Sets

* You need to create suitable training, validation, and testing sets for fitting and testing the RNN LSTM model using the encoded review comments. Use the `train_test_split` method from `sklearn` to create these sets.

### Build and Train the RNN LSTM Model

Remember that we use `Embedding` layers to analyze text data in RNN LSTM models, so this section starts by setting up some initial variables needed for the RNN LSTM to score sentiment.

As it's defined in the [Embedding layer documentation of the Keras API](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding?version=stable), you should set the `input_dim` parameter to the size of your vocabulary, so we set the `vocabulary_size` variable to the length of the number of words in the `tokenizer`, plus `1`.

Also, we define a variable called `embedding_size` to specify how many dimensions will be used to represent each word.

```python
# Import Keras modules for model creation
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Model set-up
vocabulary_size = len(tokenizer.word_counts.keys()) + 1
embedding_size = 64
```

1. Define an RNN LSTM model as follows:

  * _Layer 1:_ Add an `Embedding` layer using the `vocabulary_size` and `embedding_size` variables as the first two parameters, and setting `input_length=max_words` (the same size as the padding).

  * _Layer 2:_ Add an LSTM layer with `280` units.

  * _Output Layer:_ Add a `Dense` layer with `1` unit and `sigmoid` as activation function.

2. Compile the model using the `binary_crossentropy` loss function, the `adam` optimizer, and fetch the following metrics: Accuracy, True positives, True negatives, False positives, False negatives, Precision, Recall, and AUC.

3. Display the summary of the model using the `summary` method of the model.

4. Train the RNN LSTM model using a batch size equal to `1000` and 10 epochs. Remember to set the `validation_data` parameter to use your validation sets.

5. Use the `predict_classes` method of your model to score the sentiment setting `batch_size=1000`.

## Models Comparison

In this section, you will assess the performance of VADER and the RNN LSTM to score sentiment in order to decide which one is better.

### Accuracy

* Use the `accuracy_score` method from `sklearn` to calculate the accuracy of each model. Display the results for further analysis.

### Confusion Matrix

Scoring the sentiment of the movie reviews as positive or negative is a binary classification problem, so use the `confusion_matrix` method from `sklearn` to calculate the confusion matrix for VADER and the RNN LSTM model.

#### Confusion Matrix for VADER

* Create the confusion matrix for VADER passing the `y_test` and `y_vader_pred` variables as parameters.

#### Confusion Matrix for the RNN LSTM Model

* Create the confusion matrix for the RNN LSTM model passing the `y_test_rnn` and `y_rnn_pred` variables as parameters.

### Classification Report

* Use the `classification_report` from `sklearn` and generate a report for each model.

### Plotting the ROC Curve

In this section, you will visually analyze the performance of both models by plotting the ROC curve. You will use the `roc_curve` and `auc` methods from `sklearn` to gather the data needed to plot this curve.

#### ROC Curve - VADER

1. Use the `roc_curve` method from `sklearn` to calculate the false positives (`fpr`) and true positives (`tpr`) rates passing as parameters the testing target sentiments (`y_test`) and the normalized values of `y_vader_prob` (e.g. `y_vader_prob_norm`).

2. After calculating the `fpr` and `tpr` for VADER, use the `auc` method of `sklearn` to calculate the AUC for VADER. Round the final result up to `4` decimals.

3. Once you gather all the data needed to plot the ROC curve, create a DataFrame with the `fpr` and `tpr` data from VADER.

4. Using the `plot()` method of the DataFrame, plot the ROC curve in the colour red, and show the AUC value in the plot title, as you can see below.

  ![ROC curve plot from VADER](Images/roc-curve-vader.png)

_Hint:_ You can pass `xlim=([-0.05, 1.05])` as a parameter to the `plot()` method to better adjust the curve.

#### ROC Curve RNN LSTM

1. Use the `predict()` method from the RNN LSTM model to predict the sentiment of the testing data `X_test_rnn`. Set `batch_size=1000` to speed up the predictions and store the results in a variable called `test_predictions_rnn`.

2. Use the `roc_curve` method from `sklearn` to calculate the false positives (`fpr`) and true positives (`tpr`) rates passing as parameters the testing target sentiments (`y_test_rnn`) and the predictions you compute using the testing data (`test_predictions_rnn`).

3. After calculating the `fpr` and `tpr` for the RNN LSTM model, use the `auc` method of `sklearn` to calculate the AUC for this model. Round the final result up to `4` decimals.

4. Once you gather all the data needed to plot the ROC curve, create a DataFrame with the `fpr` and `tpr` data from the RNN LSTM model.

5. Using the `plot()` method of the DataFrame, plot the ROC curve in the colour blue, and show the AUC value in the plot title, as you can see below.

  ![ROC curve plot from the RNN LSTM model](Images/roc-curve-rnn-lstm.png)

_Hint:_ You can pass `xlim=([-0.05, 1.05])` as a parameter to the `plot()` method to better adjust the curve.

## Results Analysis and Conclusions

Review all the metrics you computed, evaluate the ROC curve plots, and the AUC values to answer the following question:

* Which model performed best scoring sentiments?

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
