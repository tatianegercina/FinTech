## 14.3 Lesson Plan: Recurrent Neural Networks

---

### Overview

Today's class will introduce students to ...

### Class Objectives

By the end of the unit, students will be able to:

* Identify the differences between ANN, RNN, and LSTM RNN models.

* Prepare data to fit LSTM RNN models.

* Create LSTM RNN models for predicting prices.

* Evaluate LSTM RNN models to discriminate against the best architecture for a given problem.

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

In this activity, students will learn how to prepare the training and testing data for an LSTM model.

**Files:**

* [lstm_predictor_part_1.ipynb](Activities/01-Evr_RNN_Part_1/Unsolved/lstm_predictor_part_1.ipynb)

* [stock_data.csv](Activities/01-Evr_RNN_Part_1/Resources/stock_data.csv)

Explain to students that we are going to focus the class on learning how to create the LSTM model using Keras since these kinds of models are widely used in industry.

Comment to students that Today's class is going to be an interactive guided session where you will go through the process of building an LSTM model from data preparation to model design and creation using Keras.

Slack out the unsolved version of the Jupyter notebook and conduct a guided live demo by highlighting the following.

* In this activity, we will use closing prices from different stocks to make predictions of future closing prices based on the temporal data of each stock.

* Before start creating LSTM models, we will learn how to prepare training and testing data for these types of neural networks.

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

* The data is loaded into a Pandas DataFrame. Note that the index is set to the column containing the date of the time series, and the `infer_datetime_format` and `parse_dates` parameters are set to `True`.

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

  * `window`: The window size in days of previous closing prices that will be used for the prediction.

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

Once the training and test datasets are created, comment to students that we need to scale the data before training the LSTM model. We will use the `MinMaxScaler` from `sklearn` to scale all values between `0` and `1`. Note that we scale both features and target sets.

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

Explain to students that the LSTM API from Keras needs to receive the features data as a _vertical vector_  so that we need to reshape the `X` data in the form `reshape((X_train.shape[0], X_train.shape[1], 1))`. Both sets, training, and testing are reshaped.

```python
# Reshape the features for the model
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
```

Answer any questions before moving on.

---

### 4. Everyone Do: Build and Train the LSTM RNN Model (15 min)

In this activity, students will learn how to build and train an LSTM RNN model using Keras.

This is an everyone do activity intended to be followed and commented with students, as you live code the demo.

**Files:**

* [lstm_predictor_part_2.ipynb](Activities/02-Evr_RNN_Part_2/Unsolved/lstm_predictor_part_2.ipynb)

* [stock_data.csv](Activities/02-Evr_RNN_Part_2/Resources/stock_data.csv)

Explain to students that now we are going to build and train an LSTM RNN model using Keras, also, some model design particularities will be covered.

Open the unsolved version of the Jupyter notebook, scroll down to the _Build and Train the LSTM RNN_ section, and slack out the file to students, as you live code the demo by and highlight the following.

* To build an LSTM RNN model in Keras, we will use the `Sequential` model as we did before; however, we will have two new types of layers:

  * `LSTM`: It's used to add an LSTM layer to the model.

  * `Dropout`: Dropout is a regularization technique for reducing overfitting in neural networks.

Open the lesson slides, and move to the _Introduction to Dropout_ section to give a brief explanation about this concept to the class.

* For simplicity, the concept of dropout will be explained using a simple neural network design with just one layer.

* Dropout consists of removing units from the hidden layers, by randomly select a fraction of the hidden nodes and set their output to zero, regardless of the input.

* A different subset of units is randomly selected every time we feed a training example.

* In Keras, dropout is implemented by adding a layer after each `LSTM` layer and defining the fraction of nodes to hide as parameter.

Switch back to the Jupyter notebook to build the LSTM RNN model, explain the code, and highlight the following.

```python
# Define the LSTM RNN model.
model = Sequential()

number_units = 5
dropout_fraction = 0.2

# Layer 1
model.add(LSTM(
    units=number_units,
    return_sequences=True,
    input_shape=(X_train.shape[1], 1))
    )
model.add(Dropout(dropout_fraction))
# Layer 2
model.add(LSTM(units=number_units, return_sequences=True))
model.add(Dropout(dropout_fraction))
# Layer 3
model.add(LSTM(units=number_units))
model.add(Dropout(dropout_fraction))
# Output layer
model.add(Dense(1))
```

* To create an LSTM RNN model, we will add `LSTM` layers.

* The `return_sequences` parameter needs to set to `True` every time we add a new `LSTM` layer, excluding the final layer.

* The `input_shape` is the number of time steps and the number of indicators

* After each `LSTM` layer, we add a `Dropout` layer to prevent overfitting.

* The parameter passed to the `Dropout` layer is the fraction of nodes that will be drop on each epoch.

* For this demo, we will use a dropout value of `0.2`. It means that on each epoch we will randomly drop `20%` of the units.

* The number of units in each `LSTM` layers, is equal to the size of the time window, in this demo, we are taking five previous `T-Bons` closing price to predict the next closing price.

Comment to students that once the model is defined, we compile the model, using the `adam` optimizer; as loss function, we will use `mean_square_error`, since the value we want to predict is continuous.

```python
# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
```

* Once the model is defined, we train (fit) the model using 10 epochs.

  ```python
  # Train the model
  model.fit(X_train, y_train, epochs=10, shuffle=False, batch_size=1, verbose=1)
  ```

* Since we are working with time-series data, it's important to set `shuffle=False` since it's necessary to keep the sequential order of the data.

* We can experiment with the batch_size parameter; however, smaller batch size is recommended; in this demo, we will use a batch_size=1.

Regarding the `batch_size` parameter, highlight the following point to the class:

* An epoch is one forward pass and one backward pass of all the training examples across all the nodes in the neural network.

* The batch size is the number of training examples in one forward/backward pass. The higher the batch size, the more memory space you'll need.

* The number of iterations is the number of passes, each pass consists of one forward and one backward pass, we do not count the forward pass and backward pass as two different passes.

* For example, if you have `1000` training examples, and your batch size is `500`, then it will take `2` iterations to complete `1` epoch.

Answer any questions before moving on.

---

### 5. Everyone Do: Assessing Model Performance (15 min)

In this section, students will evaluate the model using the test data.

**Files:**

* [lstm_predictor_part_3.ipynb](Activities/03-Evr_RNN_Part_3/Unsolved/lstm_predictor_part_3.ipynb)

* [stock_data.csv](Activities/03-Evr_RNN_Part_3/Resources/stock_data.csv)

Open the unsolved version of the Jupyter notebook and highlight the following:

* After training the model, it's time to evaluate our model to assess its performance.

* We will use the evaluate method using the testing data.

  ```python
  # Evaluate the model
  model.evaluate(X_test, y_test)
  ```

* To better understand the model evaluation results, we will make some predictions and plot the predicted vs. the real prices.

  ```python
  # Make some predictions
  predicted = model.predict(X_test)
  ```

* Since we scaled the original values using the `MinMaxScaler`, we need to recover the original prices to better understand of the predictions.

* We will use the `inverse_transform()` method of the scaler to decode the scaled values to their original scale.

  ```python
  # Recover the original prices instead of the scaled version
  predicted_prices = scaler.inverse_transform(predicted)
  real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))
  ```

* To plot the predicted vs. the real values, we will create a DataFrame.

  ![model-eval-1](Images/model-eval-1.png)

* Finally, we plot the predicted vs. real prices using the `plot()` method of the DataFrame.

  ![model-eval-2](Images/model-eval-2.png)

After creating the plot, ask students the following question and conduct a brief discussion about the results:

* Will you trust in this model to predict prices?

  * **Sample Answer:** It's difficult to trust in this model as is, the error between the real and predicted values looks big.

  * **Sample Answer:** I will give a chance to this model, but before start using it to make a decision, I would train it with new data.

Finally, comment to students that this model could be enhanced as follows:

* We can test different window sizes, for example, from `5` to `10`.

* We can test different dropout parameters, for example, between `0.2` and `0.5`.

* We may want to add an additional LSTM layer.

* When training the model, we can test different batch sizes and use more epochs.

Comment to student that they will have a chance to test these different approaches in the homework assignment.

Answer any questions before moving on.

---

### 6. BREAK (40 min)

---

### 7. Instructor Do: Machine Learning Review (2:15 min)

The remainder of Today's class is intended to review the topics covered in the machine learning units and clarify any doubt that may arise.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
