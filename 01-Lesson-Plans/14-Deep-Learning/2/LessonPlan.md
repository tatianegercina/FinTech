## 14.2 Lesson Plan: Deep learning

### Overview


### Class Objectives

By the end of class, students will be able to:

*

### Instructor Notes

* 

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson 14.2 Slides]().

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 mins)


Welcome students to the second day of deep learning! Indicate that today students will dive into contructing deep learning models with real-world data. Deep neural networks are much more effective than traditional machine learning approaches at discovering non-linear relationships amongst data, and thus are often the best-performing choice for complex or unstructured data like images and text and. 

Ask if there are any questions before moving on.

---

### 2. Instructor Do: (15 mins)

**Files:**

* Solved:

---


### 3. Students Do: (15 mins)


---


### 4. Instructor Do: Review (10 mins)

**Files:**

* Solved:

---


### 5. Instructor Do: Intro to Deep Learning (15 mins)

Return to the slides for this class and begin with the section titled "Deep Learning." Open the Tensorflow playground to demonstrate the effects of adding layers of neurons to a neural network and go through the following talking points:

* As we've seen, neural networks work by calculating the weights of various input data and passing them on to the next layer of neurons. This proceeds until we get to the output layer, which makes the final decision on the predicted category or numerical value of an instance. 

* The number of layers that are included in a neural network model determines whether it is a "deep" learning model or not. While definitions vary, networks with more than one "hidden" layer can be classified as "deep." The prevalence of these deep learning models have been faciliated in recent years by the abundance and decreasing cost of computing power. 

* The advantages of adding layers lie in the fact that each additional layer of neurons makes it possible to model more complex relationships and concepts. Imagine we're trying to classify whether a picture contains a cat. Conceptually, the first step in solving this problem might involve checking whether there exists some animal in the picture. Drilling deeper, the model might detect the presence of paws, pointed ears, etc. This breaking down of the problem continues until we reach the raw input of the model, which are the individual pixels in the picture. If this problem is correctly specified, each conceptual layer would need its own layer of neurons. 

* Deep learning models make solving machine learning problems with high accuracy like image classification and sentiment classification possible. 

* We can see the benefits of adding additional layers in the tensorflow playground - this is apparent with the more complex classification datasets, such as "spiral." We see a lack of convergence below with one layer of neurons. 

![playground_1_layers](Images/playground_1_layers.PNG)

* When we add a second layer, the model converges to a much lower loss metric. 

![playground_2_layers](Images/playground_2_layers.PNG)

* Of course, adding layers does not always guarantee better performance. Some layers can be redundant if the problem is not complex enough to warrant them. Of course, we rarely know this beforehand, and since there is not an analytical way of arriving at the number of layers we should use, the only solution to specifying the "correct" number of layers is to use trial and error.  

![playground_3_layers](Images/playground_3_layers.PNG)

* Adding more layers than is necessary may cause overfitting, since the model might fit a far more complex function than the one that actually generated the data. 

Ask for volunteers to the questions below as a check for understanding. 

* What are some examples of classification or regression problems that might benefit from a deep learning model?

    **Sample Answer**: Facial recognition; medical diagnoses; natural language generation for chatbots. 

* What is one way we can see whether a neural network may have too many layers of neurons?

    **Sample Answer**: Signs of overfitting - for example, test accuracy is far lower than training accuracy.

---

### 6. Everyone Do: Deep Learning with Tensorflow (10 mins)

In this activity we build a deep learning model to predict the quality score of wines. 

**Files:**

* Solved: [deeplearning.ipynb](Activities/03-Ins_Deep_Learning/Solved/deeplearning.ipynb)
* Unsolved: [deeplearning.ipynb](Activities/03-Ins_Deep_Learning/Unsolved/deeplearning.ipynb)

If you are confident with the code, open the unsolved notebook and have everyone follow along while you live code. Otherwise, walk through the solved notebook and given students the following talking points. 

* In this activity we will try to use a deep neural network to predict wine quality scores using some features of the wine. 

* As always, the data needs to be scaled first. 

* First we'll create a shallow, 1 hidden layer network to accomplish the same task. 

```python
# Define the model - shallow neural net
nn = Sequential()
nn.add(Dense(8, input_dim=11, activation='relu'))
nn.add(Dense(1, activation='linear'))
```

* From plotting the loss function, it seems to quickly converge to a very small loss. Can a deeper network do better?

![deep1](Images/deep1.PNG)

* Defining a deep neural net is very easy - all we have to do is add another layer of hidden neurons, using the same activation function as the first, and normally with fewer neurons than the first hidden layer. Of course, we can and should experiment with many different potential architectures if our goal is to minimize the loss metric. 

```python
# Define the model - deep neural net
nn = Sequential()
nn.add(Dense(8, input_dim=11, activation='relu'))
nn.add(Dense(4, activation='relu'))
nn.add(Dense(1, activation='linear'))
```

* After defining and overlaying the results of the deep learning model on the shallow model, it seems that adding a layer increases the training speed (as measured by the slope of the loss metric over epochs) and slightly decreases the loss metric the model converges to. 

![deep2](Images/deep2.PNG)

* This does not seem to come at the price of overfitting, as both models perform equally well on validation data, which is unseen at training.

![deep3](Images/deep2.PNG)

![deep4](Images/deep2.PNG)

---

### 7. Students Do: Sound of Music (15 mins)

In this activity students will build a model to predict the geographical origins of a musical composition. 

**Instructions:**

* [README.md](Activities/04-Stu_Sound_of_Music/README.md)

**Files:**

* [music].ipynb]((Activities/04-Stu_Sound_of_Music/Unsolved/music.ipynb)



### 8. Instructor Do: Review Sound of Music (10 mins)

**Files:**

* [music.ipynb]((Activities/04-Stu_Sound_of_Music/Solved/music.ipynb)

* The first model we define has one hidden layer with 8 neurons. 

```python
# 1 hidden layer
nn = Sequential()
nn.add(Dense(8, input_dim=67, activation='relu'))
nn.add(Dense(2, activation='linear'))
```

* The second model we define has two hidden layers, with 8 and 4 neurons respectively. 

```python
# Define the model - shallow neural net
nn = Sequential()
nn.add(Dense(8, input_dim=67, activation='relu'))
nn.add(Dense(4, activation='relu'))
nn.add(Dense(2, activation='linear'))
```
* The second model converges to a lower loss metric at a slightly faster rate of training. 

![music1](Images/music1.PNG)

* However, when we compare validation losses, it's clear that both models have severe overfitting problems after 100 or so epochs of training. The simpler model has a less drastic increase in the validation loss over time, which intuitively should make sense; the simpler model does not overfit quite as much because the function it can create is less complex. 

![music2](Images/music2.PNG)

![music3](Images/music3.PNG)

* In this instance, we may prefer the first (shallow) model due to better performance on validation (or test) data, unless there is some way of preprocessing the data or tuning the model that would limit the effects of overfitting. 

Ask students for any questions before moving on. 


### 9. Instructor Do: Model Persistence (10 mins)

In order to use a neural net model in a production setting, we often need to save the model and have it predict outcomes on unseen data at a future date. In this demo we'll show students how to persist a neural net model.

**Files:**

* [model_persistence.ipynb]((Activities/05-Ins_Model_Persistence/Solved/model_persistence.ipynb)

Open the solved notebook and go through each cell, stopping for questions.

* Let's say we have created a model that seems to do well on the training and test data. Now we want to put it into production so that it can be used to make actual predictions. To do this, we need to save the model somewhere so that it can be called when needed. 

* In the first few blocks of code, we have defined a model to predict the quality of wine similar to the one we created in the last demo. 

* To save the model, we take advantage of the to_json function, which represents the parameters and hyperparameters of the model in a JSON format. Students should be familiar with this format as it is a common API output standard. 

```python
nn_json = nn.to_json()
with open('../Resources/model.json', 'w') as json_file:
    json_file.write(nn_json)
```

* Once the model is saved, it can be read and accessed again by code. However, it is now also viewable by humans, since JSON is human-readable. Open the file that the model was saved to, and ask students to identify parameters.

![json_model](Images/json_model.PNG)

* Note that the model does not actually contain the weights that were trained i.e., the parameters within each neuron that dictate how variables are used to predict outcomes. We also need to save the model weights, this time in a HDF store.

```python
# load weights into new model
loaded_model.load_weights('../Resources/model.h5')
```

* To load the models, we need to call the model_from_json function from Keras. 

```python
from tensorflow.keras.models import model_from_json

# load json and create model
with open('../Resources/model.json', 'r') as json_file:
    model_json = json_file.read()
loaded_model = model_from_json(model_json)

# load weights into new model
loaded_model.load_weights('../Resources/model.h5')
```

* Finally, we can use the loaded model's predict function to make predictions on unseen data. 

Ask students for questions before moving on to the practice activity. 

### 10. Students Do: After Training (15 mins)

In this activity students will create a deep learning model from the music geographies data, save it, and load it to evaluate its performance on unseen data. 

**Instructions:**

* [README.md](Activities/06-Stu_After_Training/README.md)

**Files:**

* [after_training.ipynb]((Activities/06-Stu_After_Training/Unsolved/after_training.ipynb)



### 11. Instructor Do: Review After Training (10 mins)

**Files:**

* [after_training.ipynb]((Activities/06-Stu_After_Training/Solved/after_training.ipynb)

Open the notebook and walk through the code, stopping for any questions. 

* First we train-test split the data using the below code. 

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```

* Don't forget to scale the data before creating the model.

* We use a shallow neural net to try to predict the geographical coordinates to limit overfitting.

```python
# 1 hidden layer
nn = Sequential()
nn.add(Dense(30, input_dim=67, activation='relu'))
nn.add(Dense(2, activation='linear'))
```

* To save the model, we write it to a json file. We save the weights to a H5 store.

* To load the model, first we read the json file. Then, we use the model object to load the weights from its filepath.

* All that's left to do is to use the model for prediction. After this, we can use scikit's MSE metric function to calculate the difference between predicted and observed values for the test set. 

```python
from sklearn.metrics import mean_squared_error, r2_score

y_pred = loaded_model.predict(X_test)
print(mean_squared_error(y_test, y_pred))
```

### 12. Instructor Do: Colab (15 mins)

The Colaboratory is a Google-sponsored environment for running Jupyter notebooks. It's specifically tailored for running and sharing deep learning experiments, with access to Google's self-developed Tensor Processing Units (TPUs) in addition to general purpose memory and RAM. Everything is based on the cloud, so there is no need to install or download any software or data. 

Navigate to the [Colab site](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=P-H6Lw1vyNNd) and explain the following points about Colab to students:

* Colab allows us to do machine learning on the web, using Google Cloud resources. We can use this environment to create Jupyter notebooks just as we would on our local computers. 

* Colab makes it easy to share projects and results - you can save notebooks right to your Google drive. 

* More importantly, you get access to cloud computing resources, including RAM, memory, and Google's proprietary hardware solution for deep learning - Tensor Processor Units (TPUs). 

Navigate to [this page](https://colab.research.google.com/notebooks/tpu.ipynb) to show students a demo for using TPUs in Colab. 

* The best part of Colab might be the many examples created using an assortment of data that are available through it. These notebooks can be found using [Seedbank](https://research.google.com/seedbank/). 

* We can search projects by tags or keywords. 

* These projects can be useful for learning by example, a source of inspiration for your own projects, or just a useful repository of code to copy snippets from. 

Navigate to the [text classification with movie reviews](https://colab.research.google.com/github/tensorflow/docs/blob/r2.0rc/site/en/r2/tutorials/keras/basic_text_classification.ipynb) page. Inform students that we will use this notebook for the next activity. 

Stop for questions before moving on to the next activity. 

---

### 13. Partners Do: Deep Learning on the Web (15 mins)

In this activity students will use the text classification demo notebook to understand and modify a deep learning classification model with Colab. 

**Instructions:**

* [README.md](Activities/07-Stu_Colab/README.md)


### 14. Instructor Do: Review Deep Learning on the Web (10 mins)

Open the [Text Classification with Movie Reviews notebook](https://colab.research.google.com/github/tensorflow/docs/blob/r2.0rc/site/en/r2/tutorials/keras/basic_text_classification.ipynb). Ask one partner to volunteer to summarize for the class what this model is doing and the steps it takes to do it. 

Ask volunteers to give examples of ways they changed the architecture, and why. Compare final accuracy and loss metrics. 
