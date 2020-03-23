# Unit 14: Deep Learning

## RNN LSTM for Time Series

* [How to Develop LSTM Models for Time Series Forecasting](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)

* [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)

## RNN LSTM for NLP

* [How to Use Word Embedding Layers for Deep Learning with Keras](https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/)

* [How does Keras 'Embedding' layer work?](https://stats.stackexchange.com/questions/270546/how-does-keras-embedding-layer-work)

* [tf.keras.layers.Embedding](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding?version=stable)

* [Text classification with preprocessed text: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification)

* [Understanding LSTM and a Quick Implementation for Sentiment Analysis in Keras](https://towardsdatascience.com/understanding-lstm-and-its-quick-implementation-in-keras-for-sentiment-analysis-af410fd85b47)

* [Research paper: Learning Word Vectors for Sentiment Analysis](http://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf)

* [Research paper: Financial Sentiment Lexicon Analysis](https://www.researchgate.net/publication/324957692_Financial_Sentiment_Lexicon_Analysis)

* [Research paper: Comparative Study of Sentiment Analysis with Product Reviews Using Machine Learning and Lexicon-Based Approaches](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1051&context=datasciencereview)

* [Research paper: Comparison of VADER and LSTM for Sentiment Analysis](https://www.ijrte.org/wp-content/uploads/papers/v7i6s/F03040376S19.pdf)

* [Research paper: Application of Sentiment Lexicons on Movies Transcripts to Detect Violence in Videos](https://thesai.org/Downloads/Volume10No2/Paper_47-Application_of_Sentiment_Lexicons_on_Movies.pdf)

## Tuning RNN LSTM Models

* [How to use Different Batch Sizes when Training and Predicting with LSTMs](https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/)

* [How to Tune LSTM Hyperparameters with Keras for Time Series Forecasting](https://machinelearningmastery.com/tune-lstm-hyperparameters-keras-time-series-forecasting/)

## ROC Curve and AUC

* [Understanding AUC - ROC Curve](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)

* [Classification: ROC Curve and AUC - Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

* [sklearn.metrics.roc_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)
### FAQs

<details>
<summary>What is the difference between supervised learning and unsupervised learning?</summary><br>
<blockquote>
<details>
<summary>Supervised Learning</summary><br>

Supervised machine learning uses labeled data with input variables (feature data) and output variables (target data) and uses the feature data to predict the target data. Because the data is labeled, the outcome is known. This data can be fed to the model, and if the model guesses incorrectly, the error can be used to fine tune the model until it makes highly accurate guesses.<br>

An example of this is using tuning forks to tune a piano. Tuning forks produce very precise tones. These tones are your known output. You can press a piano key and compare the piano's tone (model output) to the tuning fork (known y value). If the piano's tone is too low then you can tighten the piano wire to make the piano better at matching the tuning fork. This process of adjusting the model to make the output match the known output is essentially supervised learning.
<br>
</details>
<details>
<summary>Unsupervised Learning</summary><br>

Unsupervised learning models are given only input variables and must work to make connections to the data without predicting a labeled target. These types of models are often clustering models that uncover connections in the data and group all the features into classes accordingly.<br>
<br>
An example of unsupervised learning would be to use website purchase data to group customers into two classes based on their spending habits. This clustering might reveal that class 1 more spends more with a coupon incentive, while class 2 spends more on targeted advertising on social media.
</details>

</blockquote>
</details>

<details>
<summary>What are Artificial Neural Networks (ANNs) and what types exist?</summary><br>

Neural networks are a set of algorithms that are modeled after the human brain. They’re designed to recognize patterns and interpret sensory data through a kind of machine perception, labeling, or clustering raw input. ANNs complete this task through the use input and output layers.  The data goes into a layer, where mathematical computation is completed, then those results are fed into the next layer.  There are many different types of neural networks.  For purposes of this class, we focus on Perceptron, Deep Neural Network, Recurrent Neural Network (RNN), and Long short-term memory (LSTM).



<blockquote>
<details>
<summary>Perceptron</summary><br>

The original neural network - the perceptron - is a single layer neural network created by Frank Rosenblatt in 1958 and further developed in 1969 by Marvin Minsky and Seymour Papert. It is the most basic model of an artificial nueron, taking inputs, applying weights, and calculating a binary weighted sum prediction.  Perceptron are very rigid with their predictions, because they can only predict binary classifications, such as True/False, Yes/No, etc.

![perceptron](Images/harsh_perceptron.png)
</details>

<details>
<summary>Deep Neural Network</summary><br>

Deep Neural Networks are neural networks that have more than one hidden layer. A simplistic way to visualize this is think of a multi-layer perceptron.

</details>

<details>
<summary>Recurrent Neural Network (RNN)</summary><br>

</details>

<details>
<summary>Long short-term memory (LSTM)</summary><br>
</details>
</blockquote><br>
</details>
<details>
<summary>How is Training and Testing Data Utilized?</summary><br>

When working with models, data is divided into training and testing sets. The training set is used to teach (supervise!) the model so it learns how the input data is connected to the output data and can make predictions. The testing data set is used to validate how well the model performs on data it has not seen before, by running the model on the testing feature data, and comparing it's predictions to the testing target data.<br>

</details>
<details>
<summary>How does `train_test_split()` work?</summary>

The `train_test_split()` function makes splitting data for testing easy!  The function outputs four sets of data points - two sets each of target and feature data where one set is for training, and one set is for testing.  This is why the variables that define the function are typically `X_train, X_test, y_train, y_test`.  The most important parameters of the function are the `X` and `y`.  During preprocessing, we separate our data into the feature data, or `X`, and the target data - `y`.

The `y` data are the values we wish to predict, and the `X` data are the values we use to influence our predictions.  If our data is stored in a DataFrame, we just break it out and store it in variables.  The values we wish to predict are stored as `y` and the features we are using to make our predictions are stored as `X`.  We then feed these into the `train_test_split()` function.

Other parameters include: `stratify`, `test_size`, `train_size`, `random_state`, and `shuffle`.

If the `y` values consists of binary data (for example, male/female), and 25% of those values are male, and 75% of those values are female, then setting the `stratify` parameter to `y` will ensure the test and train data have the same ratio of male to female as the entire data set.

The specific `test_size` and `train_size` can also be set to override the default sizes.  The default for these parameters will select sizes that complement the data set.  The defaults can be overridden using either `int` or `float` values.  If the parameter is set to `int`, then this will indicate a specific sample size you wish to include in the test or train set.  If the parameter is set to `float` then it will indicate a percentage of the total dataset you wish to include in the test or train set.

When using the `shuffle` parameter, the data is shuffled (randomized) prior to being divided into train and test sets.

When using this function, the data is split each time randomly; however, if the `random_state` parameter is set, the same random split will be selected each time.  To use this parameter, any number can be used as the `random_state` as long as it is used each time you run the model.  Using this parameter will always ensure the same split is obtained even if `shuffle` is set to `True`.

An example of implementing a `train_test_split()` instance is as follows:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, shuffle=True)
```

</details>


<details>
<summary>How do you preprocess data for classification?</summary>
Most categorical data is text-based and must be converted to numerical so that computations can be ran.  For example, if your categories are male and female, you could convert them to 0 and 1.  Scikit-learn offers functions that can handle this conversion simply.  Two options are `LabelEncoder()` and `OneHotEncoder()`.

<blockquote>
<details>
<summary><strong>Preprocessing Target Data</strong></summary>

Using `LabelEncoder()` from scikit-learn, we can convert categorical data to numerical.  We begin with a simple DataFrame showing 6 countries:

![country_df1](Images/country_df1.PNG)

Then we import `LabelEncoder` from sklearn.preprocessing, after which we instantiate the `LabelEncoder()` object, then run a `.fit()` followed by `.transform()`.  The results are stored in a new variable `encoded_y` and inserted into the DataFrame.

```python
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoder.fit(df.Country)
encoded_y = encoder.transform(df.Country)
df['Encoded'] = encoded_y
```
Now you can see that the encoded values are numerical representations of the original countries:

![country_df2](Images/country_df2.PNG)

</details>

<details>
<summary><strong>Preprocessing Feature Data</strong></summary>

There are situations when using `Labelencoder()` is not appropriate.  If you are encoding target values (the values you wish to predict), then using the label encoder is great, however, if you are encoding feature values, this method can cause accidental bias in your model prediction.  This is because the numerical representations of the data will be interpreted as values by the model.  A category of 5 will be given more weight than a category of 1.  This is where the `.get_dummies()` pandas function used in Unit 10 comes into play.  The function works by splitting the categorical column of data into multiple columns of separate data with a 1 or 0 representation.  In the below example we use `.get_dummies()` to convert the same country data as before:

```python
encoded_data = pd.get_dummies(df.Country, columns='Country')
```
![country_df3](Images/country_df3.PNG)
</details>
<details>
<summary><strong>Scaling Feature Data</strong></summary>
In our previous example, we converted feature data to binary to avoid introducing bias into the model.  For the same reason, we should scale data that have large numerical variance between features, so that all features are weighted the same.  For example, let's suppose that our country DataFrame also includes an average number of children, average life expectancy, and average salary by country.  The average number of children is a very small number compared to average life expectancy, which is a very small number compared to the average salary by country.  These values vary greatly and need to be scaled, because the higher numbers may result in more weight bias.

![country_df4](Images/country_df4.PNG)

Using the `StandardScaler()` from scikit-learn, we will scale the data.  First we instantiate the `.StandardScaler()` instance, then fit it to the data, then transform the data and show it in a new DataFrame:

```python
data_scaler = StandardScaler()
data_scaler.fit(df)
data_scaled = data_scaler.transform(df)
```
The new DataFrame shows the scaled data in place of the former values.  Now all the values are standardized:

![country_df5](Images/country_df5.PNG)

</details>
</blockquote>
</details>

<details><summary>
What is .reshape() and why do I have to use it?</summary>

When working with Pandas, we often pass Series objects into our model.  The shape of values in a Pandas Series object is a 1d array.  This has to be converted into a 2d array which is essentially an array of arrays - or list of lists. .  This is done using the `.reshape()` function.  The matrix values we desire are passed into this function.  In the following example we reshape our list into a 2d array using `.reshape(3,4)`, where 3 is the number of lists and 4 is the number of values in each list:

![2d_arrayImages](Images/2d_array.PNG)

Many models require the 2d array to be formatted such that each value is in a list by itself. If we were inserting the above sample data into a model, it would be converted using `.reshape(-1,1)`, where -1 indicates an unknown number of rows, and 1 indicates the number of values in each list.  The -1 will allow the function to generate the amount of rows necessary to hold the data.  The output looks like this:

![2d_array_reshape](Images/2d_array_reshape.PNG)

</details>

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
