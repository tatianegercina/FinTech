## 14.3 Lesson Plan: Recurrent Neural Networks

---

### Overview

Today's class will introduce students to ...

### Class Objectives

By the end of the unit, students will be able to:

*

### Instructor Notes

* How you expect the class to feel.

* Advice or Warnings

* Thematic Scripting - We are introducing students to the world of big data...

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1NoW5ZXlmW-lz4tbG6kU07zuR0cTryVSZIsLRAskyB1E/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to the third day of deep learning! Today students will be introduced to recurrent neural networks (RNN), a type of neural nets that are able to remember the past and its decisions are influenced by what it has learnt from the past.

Open the lesson slides, move to the _Intro to Recurrent Neural Networks_ section and highlight the following:

* RNNs are good for sequential patterns recognition, some examples include:

  * Natural Language Processing

  * DNA sequences

  * Time series data

  * Music composition

Answer any questions before moving on.

---

### 2. Instructor Do: Intro to Recurrent Neural Networks (15 min)

In this lecture, students will be introduced to the general functioning of RNNs and LSTMs. The complex math behind these kind of neural networks is beyond the scope of this lesson, but additional resources will be shared for those students interested in learning more them.

Continue in the _Intro to Recurrent Neural Networks_ section of the lesson slides, and highlight the following:

* Before going deep into RNNs, it's important to understand the general differences between artificial neural networks (ANNs) and RNNs.

* As we already know, we can use ANNs to identify the type of car from a still image.

* However, can we predict the direction of a car in movement?

Explain to students that the short answer for this question is _No_; if you try to predict the direction of a car only with the information of a still image, you don't have enough information to make a prediction beyond of a _random guess_.

Comment to the class, that without knowledge of where the car has been, you wouldn’t have enough data to predict where the car is going.

* If we record in movement, we may have enough information to make a better prediction since we can have a sequence of images representing the car's movement.

* A new challenge arises, ANNs don't have a memory mechanism to store the different states of a sequence of images _per se_.

* This is where RNNs comes into action! RNNs are good at modeling sequence data thanks to their sequential memory.

* Following the example in the slides, using RNNs we can predict that the car is moving to the right.

Explain to class, that in contrast to an ANN, an RNN is able to remember thanks to a feedback loop that allows information to flow from one step to the next along the sequence.

![ANNs Vs. RNNs](Images/ann_vs_rnn.png)

* Following the example of the car in motion, thanks to the feedback loop of the RNN, we can save the position of the car from one step to the next one as long as we have sequence data about the car's position.

* In order to explain how RNNs work, an example from NLP is going to be used.

* When a person reads a sentence, for example `I want to invest for retirement`, the brain starts to make associations among the words as the person reads the sentence.

  ![RNN words](Images/rnn-words.png)

* The brain is able to decode the phrase and understand it because the neurons have memory like RNNs.

* If we pass the sentence to a RNNs, the sentence is split into individual words and the following steps are performed:

  * The first step is to feed `I` into the RNN. The RNN encodes `I` and produces an output (`01`).

  * For the next step, we feed the word `want` and the hidden state from the previous step. The RNN now has information on both the word `I` and `want`.

  * This process is repeated until the final step. By the final step the RNN has encoded information from all the words in previous steps.

  * The final output (`06`) was created from the rest of the sequence, to predict what the phrase means, we take the final output and pass it to the feed-forward layer of the RNN to classify the intent.

    ![RNN prediction](Images/rnn_prediction.png)

Explain to students that RNNs memory has a limitation, they only remember the most recent few steps of a sequence.

* The vanishing gradient in the hidden states illustrates this issue known as _short-term memory_.

  ![Vanishing gradient](Images/rnn_gradient.png)

* It can be seen that the RNN remembers a lot from the _brown state_, but just a little from the _red state_.

* This _short-term-memory_ issue is solved by using Long-Short-Term Memory Recurrent Neural Networks (aka LSTM or LSTM-RNN).

Explain to the class that we are not going over the math complexity of LSTMs, the key point is to know that an LSTM RNN works like an original RNN, but it decides selectively which types of longer-term events are worth remembering, and which are OK to forget.

* Thanks to LSTMs we will be able to use the power or RNNs in longer time windows.

* LSTMs are capable of learning long-term dependencies using a mechanism called _gates_.

Open your web browser and navigate to the [Talk to Transformer](https://talktotransformer.com/) website; slack out the URL to the students and explain them that you will show them how RNNs can be used for automatic text generation, this is part of the _magic_ behind intelligent bots.

![Automatic text generator](Images/auto_text_gen.gif)

Once you open the _Talk to Transformer_ website, highlight the following:

* When you type `I want to`, these sentence is passed as initial parameter to the RNN.

* After processing the initial phrase, the algorithm starts to automatically create a paragraph based on the sequence of the previous words and the knowledge from its corpus.

* When we type a longer sentence like `I want to invest for retirement`, we are also including an intention in the phrase.

* Since this new sentence has a better semantic meaning, the algorithm creates a more complex text.

* This is just an example of how RNNs and LSTMs can be used for NLP.

For those students that may be interested in learning more about this matter, slack out the [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks) hosted by Stanford University.

Answer any questions before moving on.

---

### 3. Everyone Do: Data Preparation for LSTM (15 min)

In this activity, students will learn how to prepare the training and testing data for a LSTM model.

**Files:**

* [lstm_predictor_part_1.ipynb](Activities/01-Evr_RNN_Part_1/Unsolved/lstm_predictor_part_1.ipynb)

* [stock_data.csv](Activities/01-Evr_RNN_Part_1/Resources/stock_data.csv)

* [vnq_hist_prices.csv](Activities/01-Evr_RNN_Part_1/Resources/vnq_hist_prices.csv)

Explain to students that we are going to focus the class on learning how to create LSTM model using Keras, since these kind of models are widely used in industry.

Comment to students that Today's class is going to be an interactive guided session, were you will go through the process of building a LSTM model from data preparation to model design and creation using Keras.

Slack out the unsolved version of the Jupyter notebook, and conduct a guided live demo by highlighting the following.

* In this activity, we will use closing prices from different stocks to make predictions of future closing prices based in the temporal data of each stock.

* Before start creating LSTM models, we will learn how to prepare training and testing data for these type or neural networks.

* We start the exercise by importing the following libraries for data manipulation.

  ```python
  # Initial imports
  import numpy as np
  import pandas as pd
  from path import Path
  import hvplot.pandas
  ```

* When you are prototyping models, it's a common practice to set the random seed to ensure reproducibility; the random seed is set for `numpy` and `tensorflow` as follows.

  ```python
  from numpy.random import seed
  seed(1)

  from tensorflow import random
  random.set_seed(2)
  ```

* The data is loaded into a Pandas DataFrame. Note that the index is set to the column containing the date of the time series and the `infer_datetime_format` and `parse_dates` parameters are set to `True`.

  ![Data Prep 1](Images/data-prep-1.png)

Explain to students that the first step towards preparing the data is to create the input features vectors `X` and the target vector `y`.

Comment to students that we will use the `window_data()` function to create these vectors and highlight the following.

```python
def window_data(df, window, feature_col_number, target_col_number):
    """
    This function accepts the column number for the features (X) and the target (y).
    It chunks the data up with a rolling window of Xt - window to predict Xt.
    It returns two numpy arrays of X and y.
    """
    X = []
    y = []
    for i in range(len(df) - window - 1):
        features = df.iloc[i : (i + window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).reshape(-1, 1)
```

* This function chunks the data up with a rolling window of _X<sub>t</sub> - window_ to predict _X<sub>t</sub>_.

* The function returns two `numpy` arrays:

  * `X`: The input features vectors.

  * `y`: The target vector.

* The function has the following parameters:

  * `df`: The original DataFrame with the time series data.

  * `window`: The window size in days of previous closing prices that will be use for the prediction.

  * `feature_col_number`: The column number from the original DataFrame where the features are located.

  * `target_col_number`: The column number from the original DataFrame where the target is located.

Explain to students, that in the forthcoming activities, we will predict closing prices using a `5` days windows of previous _T-Bonds_ closing prices, so that, we will create the `X` and `y` vectors by calling the `window_data` function and defining a window size of `5` and setting the features and target column numbers to `2` (this is the column with the _T-Bonds_ closing prices).

![Data Prep 2](Images/data-prep-2.png)

* To create the training and testing dataset, the data is manually split using arrays slicing to avoid randomizing data when creating the samples.

```python
# Use 70% of the data for training and the remainder for testing
split = int(0.7 * len(X))
X_train = X[: split - 1]
X_test = X[split:]
y_train = y[: split - 1]
y_test = y[split:]
```

Once the training and test dataset are created, explain to students that we need to scale the data before training the LSTM model. We will use the `MinMaxScaler` from `sklearn` to scale all values between `0` and `1`. Note that we scale both, features and target sets.

```python
# Use the MinMaxScaler to scale data between 0 and 1.
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
scaler.fit(y)
y_train = scaler.transform(y_train)
y_test = scaler.transform(y_test)
```
