## 14.3 Lesson Plan: Recurrent Neural Networks

---

### Overview

Today's class will introduce students to recurrent neural networks (RNN).

### Class Objectives

By the end of the unit, students will be able to:

* Identify the differences between ANN, RNN, and LSTM RNN models.

* Prepare data to fit LSTM RNN models.

* Create LSTM RNN models for predicting prices.

* Evaluate LSTM RNN models to discriminate against the best architecture for a given problem.

### Instructor Notes

* Today's class is brief but may be challenging for students. Take extra time during the activities today to ensure that students can follow along.

* A few students may want to go even deeper into the theory and math behind RNNs, but it would be best to direct those in-depth discussions to office hours. Encourage students to review the reference links and to think about ways that they might be able to incorporate RNNs into their projects.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1NoW5ZXlmW-lz4tbG6kU07zuR0cTryVSZIsLRAskyB1E/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to the third day of deep learning!

Open the lesson slides, and briefly cover today's agenda and class objectives. Explain to students that they will learn about recurrent neural networks (RNN), a type of neural network that can remember the past and combine that knowledge with new inputs to make decisions.

---

### 2. Instructor Do: Intro to Recurrent Neural Networks (15 min)

In this lecture, students will be introduced to the general concepts behind RNNs and LSTMs. The complex math behind these types of neural networks is beyond the scope of this lesson, but additional resources will be shared for those students interested in learning more about them.

Use the _Intro to Recurrent Neural Networks_ section of the lesson slides to highlight the following:

* RNNs are suitable for sequential pattern recognition, some examples include:

  * Natural Language Processing

  * DNA sequences

  * Time series data

  * Music composition

Before going deep into RNNs, it's essential to understand the general differences between artificial neural networks (ANNs) and RNNs. Pose the following question to students:

* ANNs can be used to identify the type of car from a still image. However, can we predict the direction of a car in movement?

  * **Answer:** The short answer for this question is _No_; if you try to predict the direction of a car only with the information of a still image, you don't have enough information to make a prediction beyond of a _random guess_.

Explain to the class that without knowledge of where the car has been, you wouldn’t have enough data to predict where the car is going.

Highlight the following reasons that ANNs are not suitable for detecting patterns over time:

* If we record in movement, we may have enough information to make a better prediction since we can have a sequence of images representing the car's movement.

* A new challenge arises, ANNs don't have a memory mechanism to store the different states of a sequence of images _per se_.

* This is where RNNs comes into action! RNNs are good at modeling sequence data thanks to their sequential memory.

* Following the example in the slides, using RNNs, we can predict that the car is moving to the right.

Explain to class, that in contrast to an ANN, an RNN is able to remember previous data thanks to a feedback loop. This feedback loop allows information to flow from one step to the next along the sequence.

![ANNs Vs. RNNs](Images/ann_vs_rnn.png)

* For the car-in-motion example, the feedback loop of the RNN allows us to save the position of the car from one step to the next one as long as we have sequence data about the car's position.

Use an example from Natural Language Processing to explain how RNNs work:

* When a person reads a sentence such as `I want to invest for retirement`, the brain starts to make associations among the words as the person reads the sentence.

  ![RNN words](Images/rnn-words.png)

* The brain is able to decode the phrase and understand it because the architecture of our brain has memory to capture the sequence of the words in time. RNNs attempt to replicate this behavior.

* If we pass the sentence to an RNN, the sentence is split into individual words and the following steps are performed:

  * The first step is to feed `I` into the RNN. The RNN encodes `I` and produces an output (`01`).

  * For the next step, we feed the word `want` and the hidden state from the previous step. The RNN now has information on both the word `I` and `want`.

  * This process is repeated until the final step. By the final step, the RNN has encoded information from all the words in previous steps.

  * The final output (`06`) was created from the rest of the sequence. To predict what the phrase means, we take the final output and pass it to the feed-forward layer of the RNN to classify the intent.

    ![RNN prediction](Images/rnn_prediction.png)

Explain to students that the memory in an RNN has limitations; they only remember the most recent few steps of a sequence.

* The vanishing gradient in the hidden states illustrates this issue known as _short-term memory_.

  ![Vanishing gradient](Images/rnn_gradient.png)

* It can be seen that the RNN remembers a lot from the _brown state_, but just a little from the _red state_.

* This _short-term-memory_ issue is solved by using Long-Short-Term Memory Recurrent Neural Networks (aka LSTM or LSTM-RNN).

Explain to the class that we are not going over the math complexity of LSTMs. However, the key point is to know that an LSTM RNN works like an original RNN. The key difference is that an LSTM can selectively decide which types of longer-term events are worth remembering and which are OK to forget.

* Thanks to LSTMs, we will be able to use the power of RNNs in longer time windows.

* LSTMs are capable of learning long-term dependencies using a mechanism called _gates_.

Open your web browser and navigate to the [Talk to Transformer](https://talktotransformer.com/) website; slack out the URL to the students and explain to them that you will show them how RNNs can be used for automatic text generation, this is part of the _magic_ behind intelligent bots.

![Automatic text generator](Images/auto_text_gen.gif)

Once you open the _Talk to Transformer_ website, highlight the following:

* When you type `I want to`, this sentence is passed as an initial parameter to the RNN.

* After processing the initial phrase, the algorithm starts to automatically create a paragraph based on the sequence of the previous words and the knowledge from its corpus.

* When we type a longer sentence like `I want to invest for retirement`, we also include an intention in the phrase.

* Since this new sentence has a better semantic meaning, the algorithm creates a more complex text.

* This is just an example of how RNNs and LSTMs can be used for NLP.

For those students that may be interested in learning more about this matter, slack out the [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks) hosted by Stanford University.

Answer any questions before moving on.

---

### 3. Everyone Do: RNN Part 1 (15 min)

In part 1 of this activity, students will learn how to prepare the training and testing data for an LSTM model.

**Files:**

* [lstm_predictor_part_1.ipynb](Activities/01-Evr_RNN_Part_1/Unsolved/lstm_predictor_part_1.ipynb)

* [stock_data.csv](Activities/01-Evr_RNN_Part_1/Resources/stock_data.csv)

Explain to the class that the entire class is going to work together to build a complete LSTM RNN model using Keras. Ask the students to follow along if they want, or to just observe and ask questions. Be sure to take plenty of time to live code this activity and discuss the major talking points during the process.

Explain to students that this activity will be broken into 3 sections:

1. Prepare the data.
2. Build and train the model.
3. Evaluate the model and make predictions.

Slack out the unsolved version of the Jupyter notebook. Live code the data preparation section with the class, and highlight the following:

* This activity will use a history of closing prices to make prediction about the next closing price.

* The first step to solving this problem is to prepare the data for the model. This process typically requires the following steps:

1. Load and clean the data (clean if needed).
2. Window the data.
3. Split the data into training and testing datasets.
4. Scale and Normalize the data with `StandardScaler` or `MinMaxScaler`.
5. Reshape the inputs for the model.

* When prototyping models, it's a common practice to set the random seed to ensure reproducibility; the random seed is set for `numpy` and `tensorflow` as follows.

  ```python
  from numpy.random import seed
  seed(1)

  from tensorflow import random
  random.set_seed(2)
  ```

* The data is loaded into a Pandas DataFrame. Note that the index is set to the column containing the date of the time series, and the `infer_datetime_format` and `parse_dates` parameters are set to `True`.

  ![Data Prep 1](Images/data-prep-1.png)

Explain to students that the first step towards preparing the data is to create the input features vectors `X` and the target vector `y`.

Explain to students that we will use the `window_data()` function to create these vectors and highlight the following.

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

* To create the training and testing dataset, the data is manually split using array slicing to avoid randomizing data when creating the samples. This is because the sequency of data in time is important when training the model, so random sampling and shuffling should be avoided.

```python
# Use 70% of the data for training and the remainder for testing
split = int(0.7 * len(X))
X_train = X[: split - 1]
X_test = X[split:]
y_train = y[: split - 1]
y_test = y[split:]
```

Once the training and test datasets are created, explain to students that we need to scale the data before training the LSTM model. We will use the `MinMaxScaler` from `sklearn` to scale all values between `0` and `1`. Note that because this is a regression problem (we are predicting a closing price), we scale both the features **AND** the target data. If the output target was categorical, the `y` data would not need to be scaled.

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

Pause here to allow students to catch up and ask any remaining questions.

Ask the TAs to send out the solution for this section of the code so that everyone has a working copy for part 1 of the solution.

---

### 4. Everyone Do: RNN Part 2 (15 min)

In part 2 of the activity, students will learn how to build and train an LSTM RNN model using TensorFlow and Keras.

**Files:**

* [lstm_predictor_part_2.ipynb](Activities/02-Evr_RNN_Part_2/Unsolved/lstm_predictor_part_2.ipynb)

* [stock_data.csv](Activities/02-Evr_RNN_Part_2/Resources/stock_data.csv)

Slack out the part 2 unsolved notebook in case any student wants to start with a fresh copy before moving to part 2 of the solution.

Explain to students that we are now going to build and train an LSTM RNN model using TensorFlow and Keras.

Ask the students to follow along as you live code the next section and highlight the following points:

* The LSTM RNN model in Keras uses the `Sequential` model just like in the deep learning activities. However, there are two new types of layers in the LSTM:

  * `LSTM`: This adds an LSTM layer to the model.

  * `Dropout`: Dropout is a regularization technique for reducing overfitting in neural networks. It simply drops a certain percentage of the connections to avoid overfitting.

Open the lesson slides, and move to the _Introduction to Dropout_ section to give a brief explanation about this concept to the class.

* For simplicity, the concept of dropout will be explained using a simple neural network design with just one layer.

* Dropout consists of removing units from the hidden layers. It achieves this by randomly selecting a fraction of the hidden nodes and sets their output to zero, regardless of the input. This effectively removes those connections from contributing to the decision logic.

* The dropout layer will randomly select a different subset of units for each training input.

* In Keras, a dropout is implemented by adding a layer after each `LSTM` layer and defining the fraction of nodes to drop as the layer parameter.

Switch back to the Jupyter notebook and continue the solution:

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

* The `return_sequences` parameter needs to set to `True` every time we add a new `LSTM` layer, excluding the final layer. This is just how Keras knows to connect each layer.

* The `input_shape` is the number of time steps and the number of indicators. In this example, the number of time steps is equal to the window specified earlier (5) while the number of indicators is related to how many input features are used to predict the final price. In this case, only the past 5 closing prices are used to predict the next closing price, so the input shape is `(5, 1)`. Another way to remember this is `input_shape=(window_size, number_of_features)`.

* After each `LSTM` layer, we add a `Dropout` layer to prevent overfitting.

* The parameter passed to the `Dropout` layer is the fraction of nodes that will be drop on each epoch.

* For this demo, we will use a dropout value of `0.2`. It means that on each epoch we will randomly drop `20%` of the units.

* The number of units in each `LSTM` layers, is equal to the size of the time window, in this demo, we are taking five previous `T-Bonds` closing prices to predict the next closing price.

Explain to students that the optimizer and loss parameters need to be specified in order to compile the model. For a regression problem, a good starting choice for these parameters is to use `adam` for the optimizer and `mean_squre_error` for the loss function. Further information about these can be found on the Keras website.

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

Take a moment to pause and allow students to catch up. Slack out the solution to Part 2 of the activity and answer any remaining questions before moving on.

---

### 5. Everyone Do: RNN Part 3 (15 min)

In part 3 of the activity, students will evaluate the LSTM-RNN model using the test data.

**Files:**

* [lstm_predictor_part_3.ipynb](Activities/03-Evr_RNN_Part_3/Unsolved/lstm_predictor_part_3.ipynb)

* [stock_data.csv](Activities/03-Evr_RNN_Part_3/Resources/stock_data.csv)

With the class, live code the final part of the solution and highlight the following:

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

  * **Sample Answer:** It's difficult to trust in this model as is because the error between the real and predicted values looks big.

Explain that if you wanted to use this model despite the initial error size, it might be good to re-run the notebook using different iterations of training and testing data. Be sure to re-run the experiment without the random seed to gain additional randomness in the experiment.

Finally, explain to students that this model could be enhanced as follows:

* We can test different window sizes, for example, from `5` to `10`.

* We can test different dropout parameters, for example, between `0.2` and `0.5`.

* We may want to add or remove additional LSTM layers.

* When training the model, we can test different batch sizes and adjust the training epochs.

Explain to student that they will have a chance to test these different approaches in the homework assignment.

Answer any questions before moving on.

---

### 6. BREAK (40 min)

---

### 7. Instructor Do: Machine Learning Review (2:15 min)

The remainder of today's class is intended to review any topics, activities, or concepts covered in any of the previous machine learning units.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
