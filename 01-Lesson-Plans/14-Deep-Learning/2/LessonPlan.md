## 14.2 Lesson Plan: Deep learning

### Overview

In this lesson, students will be introduced to deep learning basic concepts. Also, they will create deep learning models using Keras and deploy machine learning models in the cloud using Google Colaboratory.

### Class Objectives

By the end of class, students will be able to:

* Explain the difference between neural networks and deep neural networks.

* Build deep learning models using Keras.

* Save trained deep learning models built in Keras for further usage.

* Deploy models in the cloud using Google Colaboratory.

### Instructor Notes

* Slack out the [Streamz Installation Guide](../../15-Algorithmic-Trading/Supplemental/Asyncio_Streamz_Install_Guide.md) and the [CCXT Installation Guide](../../15-Algorithmic-Trading/Supplemental/CCXT_Install_Guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* Deep learning has a lot of technical concepts that are beyond the scope of this lesson. Students should be able to obtain a high-level understanding of deep neural network architectures through a series of hands-on activities.

* This class uses the new TensorFlow 2.0 framework for the activities, so be sure to test the install and setup for this before class.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [14.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2bd77952-1001-4f38-9c08-aaf8002299ae) Note that this video may not reflect the most recent lesson plan.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/13YjMJO9cpmfUJBXCnPtuBN4w7jhBdEoGQyGBCKc2PPk/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students to the second day of the deep learning unit! Open the lesson slides and move to the _What is Deep Learning?_ slide and highlight the following:

* Today, we will dive into constructing deep learning models with real-world data.

* Generally speaking, deep learning models are neural networks with more than one hidden layer.

* Deep neural networks are much more effective than traditional machine learning approaches at discovering nonlinear relationships among data and thus are often the best-performing choice for complex or unstructured data like images, text, and voice.

Explain to students that deep neural networks allow creating computational models composed of multiple layers that can learn representations of data with multiple levels of abstraction.

* For example, in image recognition, each layer can identify different features of an input image to decide what it's about.

Explain to students that deep neural networks are fun! Open the [Quick, Draw! web application](https://quickdraw.withgoogle.com) in your browser and slack out the URL to students. Explain to students that they are going to play a Pictionary-like game using the power of deep learning.

* _Quick, Draw!_ is an application that can identify an image from a trace.

* The game asks you to draw something in less than 20 seconds while the deep learning algorithm tries to guess what the trace could be.

  ![Quick,Draw! demo](Images/quick-draw.gif)

Draw a couple of traces in the game, and tell students that this is an example of the power of neural networks in real-time. Explain that even though this is just an example of a game, deep learning has been the tool that has really allowed machine learning to transform FinTech. Advances in deep learning are powering applications that were once considered science fiction.

Ask if there are any questions before moving on.

---

### 2. Instructor Do: Intro to Deep Learning (15 min)

Using the slides, move to the _Understanding Deep Learning_ section and highlight the following:

* As we have seen, neural networks work by calculating the weights of various input data and passing them on to the next layer of neurons. This proceeds until we get to the output layer, which makes the final decision on the predicted category or numerical value of an instance.

* The number of layers that are included in a neural network model determine whether it is a "deep" learning model or not. While definitions vary, networks with more than one "hidden" layer can be classified as "deep." The prevalence of these deep learning models have been facilitated in recent years by the abundance and decreasing cost of computing power.

* The advantages of adding layers lie in the fact that each additional layer of neurons makes it possible to model more complex relationships and concepts. Imagine we are trying to classify whether a picture contains a cat. Conceptually, the first step in solving this problem might involve checking whether there exists some animal in the picture. Drilling deeper, the model might detect the presence of paws, pointed ears, etc. This breaking down of the problem continues until we reach the raw input of the model, which are the individual pixels in the picture. If this problem is correctly specified, each conceptual layer would need its own layer of neurons.

* Deep learning models are capable of solving very complex problems where classical models would fail. Deep learning makes it possible to solve difficult problems with high accuracy, like image classification or natural language processing.

Open the TensorFlow playground [using this link](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=8&seed=0.14370&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false), click on the _Play_ button to run the simulation, and use the model to demonstrate the effects of adding layers of neurons to a neural network and go through the following talking points.

* We can see the benefits of adding additional layers in the TensorFlow playground - this is apparent with the more complex classification datasets, such as _spiral_. We see a lack of convergence below with one layer of neurons.

![playground_1_layers](Images/playground_1_layers.PNG)

Add a second hidden layer with six neurons to the model and highlight the following:

* After adding a second layer, the model converges to a much lower loss metric.

![playground_2_layers](Images/playground_2_layers.PNG)

Add a third hidden layer with four neurons to the model and highlight the following:

* Adding layers does not always guarantee better performance. Some layers can be redundant if the problem is not complex enough to warrant them. Of course, we rarely know this beforehand, and since there is not an easy analytical way of arriving at the number of layers we should use, the only solution to specifying the "correct" number of layers is to use trial and error.

![playground_3_layers](Images/playground_3_layers.PNG)

* Adding more layers than is necessary may cause overfitting, since the model might fit a far more complex function than the one that actually generated the data.

Ask for volunteers to answer the questions below as a check for understanding.

* What are some examples of classification or regression problems that might benefit from a deep learning model?

    **Sample Answer**: Facial recognition; medical diagnoses; natural language generation for chatbots.

* What is one way we can see whether a neural network may have too many layers of neurons?

    **Sample Answer**: Signs of overfitting - for example, test accuracy is far lower than training accuracy.

Answer any questions before moving on.

---

### 3. Everyone Do: Deep Learning with Keras (15 min)

In this activity, students will build a deep learning model to predict the quality score of different wines.

**Files:**

* Solved: [deeplearning.ipynb](Activities/01-Ins_Deep_Learning/Solved/deeplearning.ipynb)

* Unsolved: [deeplearning.ipynb](Activities/01-Ins_Deep_Learning/Unsolved/deeplearning.ipynb)

If you are confident with the code, open the unsolved notebook, and have everyone follow along while you live code. Otherwise, walk through the solved notebook and give students the following talking points.

* In this activity, we will use a deep neural network to predict wine quality scores using some features of the wine.

* The features are assigned to `X`, and the target labels are assigned to `y`.

  ```python
  # Read in data
  data = Path("../Resources/winequality.csv")
  df = pd.read_csv(data, delimiter=";")

  # Create the features (X) and target (y) sets
  X = df.iloc[:, 0:11].values
  y = df["quality"].values
  ```

* As always, the data needs to be scaled first.

  ```python
  # Scale the data
  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler().fit(X)
  X = scaler.transform(X)
  ```

* First, we'll create a shallow, one hidden layer network to accomplish the task. Note that the activation function in the output layer is set to `linear`.

  ```python
  # Define the model - shallow neural net
  number_hidden_nodes = 8
  number_input_features = 11

  nn = Sequential()
  # Hidden layer
  nn.add(
      Dense(units=number_hidden_nodes, input_dim=number_input_features, activation="relu")
  )
  # Output layer
  nn.add(Dense(units=1, activation="linear"))
  ```

* The model is compiled and trained.

  ```python
  # Compile the model
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Train the model
  model_1 = nn.fit(X, y, validation_split=0.3, epochs=200)
  ```

* The `mean_squared_error` loss function is used to compile the model since the output is continuous because this is a regression model. Also, as an additional metric, we defined `mse`.

* Note that in the  `fit()` method the `validation_split` parameter is used. This parameter is a float number between `0` and `1` that reserves a fraction of the data for validation; it can be used as an alternative to the `train_test_split` method of `sklearn`.

* When the `validation_split` parameter is used, the model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch.

* From plotting the loss function, it seems to converge to a very small loss quickly. Can a deeper network do better?

  ![deep1](Images/deep1.PNG)

* Defining a deep neural net is very easy - all we have to do is add another layer of hidden neurons, using the same activation function as the first, and normally with fewer neurons than the first hidden layer. Of course, we can and should experiment with many different potential architectures if our goal is to minimize the loss metric.

  ```python
  # Define the model - deep neural net
  number_input_features = 11
  hidden_nodes_layer1 = 8
  hidden_nodes_layer2 = 4

  nn = Sequential()
  # First hidden layer
  nn.add(
      Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
  )
  # Second hidden layer
  nn.add(Dense(units=hidden_nodes_layer2, activation="relu"))
  # Output layer
  nn.add(Dense(units=1, activation="linear"))
  ```

* After defining and overlaying the results of the deep learning model on the shallow model, it seems that adding a layer increases the training speed (as measured by the slope of the loss metric over epochs) and slightly decreases the loss metric the model converges to.

  ![deep2](Images/deep2.PNG)

* This does not seem to come at the price of overfitting, as both models perform equally well on validation data, which is unseen at training.

  ![deep3](Images/deep3.PNG)

  ![deep4](Images/deep4.PNG)

Answer any questions before moving on.

---

### 4. Student Do: Sound of Music (20 min)

In this activity, students will build a model to predict the geographical origins of a musical composition.

**Instructions:**

* [README.md](Activities/02-Stu_Sound_of_Music/README.md)

**Files:**

* [music.ipynb](Activities/02-Stu_Sound_of_Music/Unsolved/sound_of_music.ipynb)

---

### 5. Instructor Do: Review Sound of Music (10 min)

**Files:**

* [sound_of_music.ipynb](Activities/02-Stu_Sound_of_Music/Solved/sound_of_music.ipynb)

* The dataset is loaded and split into features `X` and target `y` sets.

  ```python
  # Read in data
  data = Path("../Resources/music.csv")
  df = pd.read_csv(data, header=None)

  # Create the features set (X) and the target set (y)
  X = df.iloc[:, 0:68].values
  y = df.iloc[:, 68:70].values
  ```

* The features data is scaled using the `StandardScaler`.

  ```python
  # Scale the data of the features set using the StandardScaler
  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler().fit(X)
  X = scaler.transform(X)
  ```

* The first model we define has one hidden layer with `8` neurons, and it is fitted with `800` epochs.

  ```python
  # Create a shallow, 1 hidden layer, neural network
  nn = Sequential()

  # Hidden layer
  nn.add(Dense(units=8, input_dim=68, activation="relu"))

  # Output layer
  nn.add(Dense(units=2, activation="linear"))

  # Compile the model
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Fit the model
  model_1 = nn.fit(X, y, validation_split=0.3, epochs=800, verbose=0)
  ```

* The second model we define has two hidden layers, with 8 and 4 neurons, respectively. This model is fitted with `800` epochs as well.

  ```python
  # Define the model - deep neural network with two layers
  nn = Sequential()

  # First hidden layer
  nn.add(Dense(units=8, input_dim=68, activation="relu"))

  # Second hidden layer
  nn.add(Dense(units=4, activation="relu"))

  # Output layer
  nn.add(Dense(units=2, activation="linear"))

  # Compile the model
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Fit the model
  model_2 = nn.fit(X, y, validation_split=0.3, epochs=800, verbose=0)
  ```

* When the plot of the loss function of the two models is created, the second model converges to a lower loss metric at a slightly faster rate of training.

  ![music1](Images/music1.PNG)

* However, when we compare validation losses, it is clear that both models have severe overfitting problems after 100 or so epochs of training. The simpler model has a less drastic increase in the validation loss over time, which intuitively should make sense; the simpler model does not overfit quite as much because the function it can create is less complex.

  ![music2](Images/music2.PNG)

  ![music3](Images/music3.PNG)

Explain to students, that in this instance, we may prefer the first (shallow) model due to better performance on validation (or test) data, unless there is some way of preprocessing the data or tuning the model that would limit the effects of overfitting, like performing PCA or adding more nodes to the hidden layer.

Ask students for any questions before moving on.

---

### 6. Instructor Do: Model Persistence (10 min)

To use a neural net model in a production setting, we often need to save the model and have it predict outcomes on unseen data at a future date. In this demo, we will show students how to persist in a neural net model.

**Files:**

* [model_persistence.ipynb](Activities/03-Ins_Model_Persistence/Solved/model_persistence.ipynb)

Open the solved notebook and go through each cell, stopping for questions.

* Let us say we have created a model that seems to do well on the training and test data. Now we want to put it into production so that it can be used to make actual predictions. To do this, we need to save the model somewhere so that it can be called when needed.

* In the first few blocks of code, we have defined a model to predict the quality of wine similar to the one we created in the last demo.

* To save the model, we take advantage of the `to_json()` function, which represents the parameters and hyperparameters of the model in a `JSON` format. Students should be familiar with this format as it is a common API output standard.

  ```python
  # Save model as JSON
  nn_json = nn.to_json()

  file_path = Path("../Resources/model.json")
  with open(file_path, "w") as json_file:
      json_file.write(nn_json)
  ```

* Once the model is saved, it can be read and accessed again by code. However, it is now also viewable by humans, since JSON is human-readable. Open the file that the model was saved to, and ask students to identify parameters.

![json_model](Images/json_model.PNG)

* Note that the model does not contain the weights that were trained, i.e., the parameters within each neuron that dictate how variables are used to predict outcomes. We also need to save the model weights, this time in an HDF file.

* [Hierarchical Data Format (HDF or h5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) files, contain multidimensional arrays of data.

  ```python
  # Save weights
  file_path = Path("../Resources/model.h5")
  nn.save_weights(file_path)
  ```

* To load the models, we need to call the `model_from_json` function from Keras.

  ```python
  # Load the saved model to make predictions from tensorflow.keras.models import model_from_json

  # load json and create model
  file_path = Path("../Resources/model.json")
  with open("../Resources/model.json", "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  # load weights into new model
  file_path = Path("../Resources/model.h5")
  loaded_model.load_weights("../Resources/model.h5")
  ```

* Finally, we can use the loaded model's `predict()` function to make predictions on unseen data.

  ![Predicted values](Images/predicted_values.png)

Ask students for questions before moving on to the practice activity.

---

### 6. Instructor Do: Model Persistence (10 min)

**Corresponding Activity:** [03-Ins_Model_Persistence](Activities/03-Ins_Model_Persistence)

To use a neural net model in a production setting, we often need to save the model and have it predict outcomes on unseen data at a future date. In this demo, we will show students how to persist in a neural net model.

**Files:**

* [model_persistence.ipynb](Activities/03-Ins_Model_Persistence/Solved/model_persistence.ipynb)

Open the solved notebook and go through each cell, stopping for questions.

* Let us say we have created a model that seems to do well on the training and test data. Now we want to put it into production so that it can be used to make actual predictions. To do this, we need to save the model somewhere so that it can be called when needed.

* In the first few blocks of code, we have defined a model to predict the quality of wine similar to the one we created in the last demo.

* To save the model, we take advantage of the `to_json()` function, which represents the parameters and hyperparameters of the model in a `JSON` format. Students should be familiar with this format as it is a common API output standard.

  ```python
  # Save model as JSON
  nn_json = nn.to_json()

  file_path = Path("../Resources/model.json")
  with open(file_path, "w") as json_file:
      json_file.write(nn_json)
  ```

* Once the model is saved, it can be read and accessed again by code. However, it is now also viewable by humans, since JSON is human-readable. Open the file that the model was saved to, and ask students to identify parameters.

![json_model](Images/json_model.PNG)

* Note that the model does not contain the weights that were trained, i.e., the parameters within each neuron that dictate how variables are used to predict outcomes. We also need to save the model weights, this time in an HDF file.

* [Hierarchical Data Format (HDF or h5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) files, contain multidimensional arrays of data.

  ```python
  # Save weights
  file_path = "../Resources/model.h5"
  nn.save_weights(file_path)
  ```

**Note:** To save the model, we set a relative file path using a string variable since the `patlib` library has some known issues when working with Keras functions to save and load models.

* To load the models, we need to call the `model_from_json` function from Keras.

  ```python
  # Load the saved model to make predictions from tensorflow.keras.models import model_from_json

  # load json and create model
  file_path = Path("../Resources/model.json")
  with open("../Resources/model.json", "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  # load weights into new model
  file_path = "../Resources/model.h5"
  loaded_model.load_weights(file_path)
  ```

* Finally, we can use the loaded model's `predict()` function to make predictions on unseen data.

  ![Predicted values](Images/predicted_values.png)

Ask students for questions before moving on to the practice activity.

---

### 7. Student Do: After Training (15 min)

**Corresponding Activity:** [04-Stu_After_Training](Activities/04-Stu_After_Training)

In this activity, students will create a deep learning model from the music geographies data, save it, and load it to evaluate its performance on unseen data.

**Instructions:**

* [README.md](Activities/04-Stu_After_Training/README.md)

**Files:**

* [after_training.ipynb](Activities/04-Stu_After_Training/Unsolved/after_training.ipynb)

---

### 8. Instructor Do: Review After Training (10 min)

**Files:**

* [after_training.ipynb](Activities/04-Stu_After_Training/Solved/after_training.ipynb)

Open the notebook and walk through the code, stopping for any questions.

* After the data is loaded, we split the data into training and testing sets.

  ```python
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
  ```

* The data is scaled before creating the model.

  ```python
  # Scale the data for the features set X_tain and X_test
  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler().fit(X_train)

  X_train_scaled = scaler.transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```

* We use a shallow neural net to predict the geographical coordinates and limit overfitting.

  ```python
  # Create a neural network with 1 hidden layer
  nn = Sequential()

  nn.add(Dense(units=8, input_dim=68, activation="relu"))
  nn.add(Dense(units=2, activation="linear"))
  ```

* After compiling and fitting the model, we save it to a JSON file. We save the weights to an H5 store.

  ```python
  # Save model as JSON
  nn_json = nn.to_json()
  file_path = Path("../Resources/model.json")
  with open(file_path, "w") as json_file:
      json_file.write(nn_json)

  # Save weights
  file_path = "../Resources/model.h5"
  nn.save_weights(file_path)
  ```

* To load the model, first we read the JSON file. Then, we use the model object to load the weights from its file path.

  ```python
  # Load the model to predict values
  from tensorflow.keras.models import model_from_json

  # Load json and create model
  file_path = Path("../Resources/model.json")
  with open(file_path, "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  # Load weights into new model
  file_path = "../Resources/model.h5"
  loaded_model.load_weights(file_path)
  ```

* All that's left to do is to use the model for prediction. After this, we can use sklearn's MSE metric function to calculate the difference between predicted and observed values for the test set.

```python
# Predict values using the testing data
from sklearn.metrics import mean_squared_error

y_pred = loaded_model.predict(X_test_scaled)

# Evaluate the model with the MSE metric
print(mean_squared_error(y_test, y_pred))
```

Answer any questions before moving on.

---

### 9. BREAK (15 min)

---

### 10. Everyone Do: Colaboratory, a Cloud-based Environment for Sharing ML Projects (20 min)

**Files:**

* [connecting_neurons.ipynb](Activities/05-Evr_Colab/Solved/connecting_neurons.ipynb)

In this activity, students will learn how to create and share Jupyter Notebooks on Google Colaboratory (aka Colab), a cloud platform oriented toward machine learning.

Explain to students that Colaboratory is a Google-sponsored environment for running Jupyter Notebooks on the Cloud. It is specifically tailored for running and sharing deep learning experiments. Colab Notebooks have access to specialized computing architectures such as Google's self-developed Tensor Processing Units (TPUs) in addition to general-purpose memory and RAM. TPUs designed specifically by Google to train and run TensorFlow models.

[Open this three minutes introductory video](https://youtu.be/inN8seMm7UI) and reproduce it in the class. After playing the video, highlight the following:

* Colab allows us to do machine learning on the web using Google Cloud resources.

* We can use this environment to create Jupyter Notebooks just as we would on our local computers.

* Colab makes it easy to share projects and results with potential employers, and you can save Notebooks right to your Google Drive.

* More importantly, you get access to cloud computing resources, including RAM, memory, and Google's proprietary hardware solution for deep learning - Tensor Processor Units (TPUs).

Navigate to the [Colab website](https://colab.research.google.com), slack out the URL to students and explain the following points about Colaboratory to students:

* To use Colab, students will need a Google account.

* To create a new Jupyter notebook, click on `NEW PYTHON3 NOTEBOOK`:

  ![Images/colab02.png](Images/colab02.png)

  * The notebook will be saved to your Google Drive.

  * Like any other file on Google Drive, you can control the sharing, editing, and collaboration of your notebook.

* Now you are ready to start using Colab.

Type the following command in the first cell, and click on the _Run_ button or press `SHIFT` + `ENTER` on your keyboard to execute the code in the cell.

  ```python
  print("Hello Colab!")
  ```

  ![Images/colab03.png](Images/colab03.png)

* Code snippets provide useful boilerplate code for many tasks, such as building a plot.

* To add a code snippet, open the left bar and type the kind of task you want to accomplish, for example, creating a bar chart.

* Once the code snippet appears, click on _INSERT_ to add the code to your notebook.

  ![Images/colab04.gif](Images/colab04.gif)

* For unusually large datasets or intensive tasks, Colab offers free hardware acceleration. To enable it, go to `Edit` and select `Notebook settings`, then choose `GPU` as the Hardware Accelerator.

  ![Images/colab12.png](Images/colab12.png)

  ![Images/colab13.png](Images/colab13.png)

* To locate in Google Drive where your notebook is stored, click on the _File_ menu, and continue by choosing the _Locate in Drive_ option.

  ![Images/colab05.gif](Images/colab05.gif)

* You can also import Jupyter Notebooks from your local drive. Click on the _File_ menu and choose the _Upload notebook...` option, then browse your local drive for the Jupyter notebook you want to upload.

  ![Images/colab06.png](Images/colab06.png)

For this demo, a notebook with dummy data is going to be used. Slack out the notebook for this activity to students, while you import the file to Colab.

* Once the file is imported, a new window showing the notebook will be opened.

Explain to students that this particular example is using `hvplot` which is not installed by default in Colab. To avoid potential errors, these lines are just commented out for now.

  ![Images/colab07.png](Images/colab07.png)

Run all the cells by clicking on the _Runtime_ menu and choose the _Run all_ option.

  ![Images/colab08.png](Images/colab08.png)

* After a few seconds, all of the cells will run on the Google cloud!

* The default settings for Google Colab currently install TensorFlow v1, though this will change in the near future.  Students may get the following error after running their imports, despite having upgraded or installed Tensorflow v2:
![Images/colab02.png](Images/colab16.png)

* Though the notebook should still run all cells as intended, the defaults can be updated to avoid potential issues in the future.  This can be done by running the following code, selecting `y` when prompted, and then restarting the runtime:

```python
!pip uninstall tensorflow
!pip install tensorflow==2.0.0
```

* Students can check then verify their Tensorflow version using the following code:

```python
import tensorflow as tf
print(tf.__version__)
```

Explain to students that it's possible to install new libraries in Google Colab by running the following command

```python
!pip install <library_name>
```

Add a new code text below the title cell of the notebook, type and execute the following code to install `hvplot` and make it run in Google Colab. Note that `bokeh` is also installed to ensure we are using the last version.

```python
!pip install hvplot
!pip install -U bokeh
```

![Images/colab09.gif](Images/colab09.gif)

* Once you have installed these libraries, you may be asked to restart the restart your runtime.

  ![Images/colab10.png](Images/colab10.png)

  ![Images/colab11.png](Images/colab11.png)

After the installation finish, remove the comments from the initial imports.

```python
# Initial imports
import pandas as pd
import numpy as np
import hvplot.pandas # <--- Uncomment this line
import holoviews as hv # <--- Uncomment this line
from sklearn.datasets.samples_generator import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```

Also, remove the comments from the cell where the plot is created. Note that for hvplots to render correctly inside Google Colab, the line `hv.extension("bokeh")` must be run in each cell where a plot is displayed.

```python
# Plotting the nonlinear dummy data
hv.extension("bokeh")
plot = df_moons.hvplot.scatter(x="Feature 1", y="Feature 2", by="Target")
plot
```

Delete the cell where you run `pip` and run all the notebook's cells to show students that the plot is now displayed in the notebook just like it was in the Jupyter Notebooks.

![Images/colab14.gif](Images/colab14.gif)

Explain to students that there are plenty of examples created by the Colab community using an assortment of data that are available through the platform. These Notebooks can be found on the [Seedbank website](https://research.google.com/seedbank/). Slack out the Seedbank URL to students and highlight the following:

* Projects can be searched by tags or keywords.

* These projects can be useful for learning by example, a source of inspiration for your projects, or just a helpful repository of code to copy snippets from.

Type `Classify movie reviews using tf.keras` in the Seedbank search box and press `ENTER` to look for this project.

Once the project appears in the search results, open it and click on the _Run seed in Colab_ button; explain to students that this is how they can import a _seed project_ to their Colab workspace, and start studying it and customizing the code.

![Images/colab15.gif](Images/colab15.gif)

Stop for questions before moving on to the next activity.

---

### 11. Student Do: Deep Learning on the Web (30 min)

In this activity, students will use the text classification demo notebook to understand and modify a deep learning classification model with Colab.

**Instructions:**

* [README.md](Activities/06-Stu_Colab/README.md)

---

### 12. Instructor Do: Review Deep Learning on the Web (15 min)

Open the [_Text Classification with Movie Reviews_ notebook](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/text_classification.ipynb).

Walk students through the notebook, pausing to highlight the various sections of code.

Ask one student to volunteer to summarize for the class what this model is doing and the steps it takes to do it.

Ask volunteers to give examples of ways they changed the architecture, and why. Compare final accuracy and loss metrics.

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
