## 14.1 Lesson Plan: Neural Networks

### Overview

Today's class introduces students to neural networks, a new member of the machine learning algorithms that can be used for classification and regression problems but are perhaps uniquely able to learn very complex, nonlinear models.

Conceptually, neural networks were inspired by neurons in the human brain, and have a similar property of scaling to meet the complex environments where they operate.

Neural networks are very flexible in their applications, but they are not necessarily meant to be "plug-and-play". From preprocessing input data to constructing a neural network architecture, students will learn the process to build and use neural networks successfully.

### Class Objectives

By the end of class, students will be able to:

* Explain the concept of neural networks, including how a neuron is akin to logistic regression.

* Explain the intuition of how weights of neurons are determined.

* Understand how the choice of inputs and hidden layers apply to problems with regression and classification.

* Experiment with neural networks' architecture in the TensorFlow playground.

* Preprocessing data for neural network models.

* Identify the Python libraries available to build neural networks.

* Describe what the pros and cons of using Keras for building neural networks are.

* Implement neural networks with the Python Keras API.

### Instructor Notes

* Today's activities will be concept-heavy, so students should be prepared to discuss and think, and not merely to practice steps for implementation.

* Allow students to ask questions, and when necessary, have students save questions for the review sessions or office hours.

* Today should also be fun since we will be playing with neural nets in several ways to experiment with input, architecture, and algorithms.

* A thorough understanding of neural networks would require math that is beyond the scope of this class. Luckily, we only need an intuitive understanding of the underlying algorithms to implement a neural network. Some details will necessarily need to be glossed over, but we will provide some additional materials for those students who are inclined to dig deeper.

* In the introduction to neural networks, a demo is made using the [Teachable Machine project from Google](https://teachablemachine.withgoogle.com/), be sure to practice the demo before class. If you are not familiar with this project, we encourage you to [watch this video](https://youtu.be/3BhkeY974Rg).

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/11gh-YowNqHBx_WEm-OBHJypKImSc51zo71vEYohNdqY/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Open the lesson slides and welcome students to the first day of deep learning! Indicate that today's class will begin with an introduction to the basic unit of neural networks before moving on to constructing simple neural nets.

As an ice-breaking activity, open the class by asking the following questions to students:

* What do you think a neural network is?

  * **Sample Answer:** It's a computer representation of a human neuron.

  * **Sample Answer:** It's a method to create artificial intelligence software.

  * **Sample Answer:** Neural networks are machine learning algorithms that can learn to solve a problem.

* Do you know some cool applications of neural networks?

  * **Sample Answer:** Autonomous cars.

  * **Sample Answer:** Image processing in cancer detection.

  * **Sample Answer:** Banning inappropriate content on social networks.

  * **Sample Answer:** Automated trading based on artificial intelligence.

Ask for two or three volunteers to share their insights, and explain to students that today they will answer these questions.

Ask if there are any questions before moving on.

---

### 2. Instructor Do: Neural Networks are Cool! (15 min)

In this activity, students will be introduced to neural networks and some of their applications.

Open the lesson slides and move to the Neural Networks are Cool! Section.

Start the presentation by showing students the following image from the [Rorschach Inkblot Test](https://en.wikipedia.org/wiki/Rorschach_test), and ask them the next question:

* What do you see in this image?

  ![Rorschach Test Card](Images/Rorschach_blot_05.jpg)

Allow students to play around for a few seconds sharing what they see, continue the presentation by telling students that there is no precise answer to this question.

Continue to the "How our brain works" slide, and explain to students that any similarity they could find between the image and a real object is possible because our brain uses thousands of neurons connections to find a match between the visual input and a mental representation of an object.

Follow to the slide titled "Our brain as inspiration for artificial neural nets," and explain to students that this power of our brain to process information and make predictions or interpretations is the fact that inspires neurophysiologists and mathematicians to start the development of artificial neural networks (ANN).

* In the same way biological neurons receive input signals through the dendrites, an ANN can receive input variables and process those inputs using an activation function to compute an output, akin the neuron nucleus in the brain.

* The concept of ANNs was presented for the first time in 1943 when [Warren McCulloch and Walter Pitts](https://doi.org/10.1007/BF02478259
) created a computational model for neural networks that they implemented using electrical circuits.

* From that initial idea of a single neuron, the concept evolved the last decades to more complex models that propose creating connections between neurons to the point of creating what we know today as neural networks.

Follow to the slide "The Future is here: applications of neural nets" and highlight the following:

* Neural networks are here to stay, and applications become more common every day.

* Companies like Google or Tesla are using neural networks to develop self-driving cars.

* Using the power of neural networks, today you can talk in any language thanks to the automated translation of instant messaging applications like Skype.

* Memories from the past that were captured in black and white can take a new perspective through automatic image colorization.

* Neural networks are also used to create a better world, not only for humans but also for wildlife thanks to projects like one led by the U.S. National Oceanic and Atmospheric Administration to save whales by tracking the North Atlantic right whales population using neural networks for image recognition.

As you continue to the slide called "Neural Networks in Finance", explain to students that the financial sector is leading in the use of neural networks, and highlight the following applications:

* **Fraud detection:** According to Javelin Strategy & Research, errors on fraud detection can cost a bank $118 billion in lost revenue.

* **Risk Management:** The banking sector, insurance, and stock exchanges are building more robust and efficient techniques for credit management thanks to neural networks.

* **Money Laundering Prevention:** Money laundering activity around the world is estimated to be between 2% to 5% of global GDP; financial institutions are using neural nets to serve as a new weapon in their fight against financial crime.

* **Algorithmic Trading:** Thanks to algorithmic trading, you can automate your trading strategies and increase your trading profits.

Explain to students that there are several deep mathematical concepts behind neural networks that are beyond the scope of today's class.

Explain to students that this week, we will give an intuitive introduction to the components that make up a neural network and how they work together to learn.

Open your web browser and navigate to [the Teachable Machine website](https://teachablemachine.withgoogle.com). This web application shows the fundamental mechanism of a neural network by training a model that recognizes gestures from your webcam to predict one of three classes.

Once you open the Teachable Machine website, follow the next steps to conduct the demo.

* Click on the _skip the tutorial_ option to start the demo.

  ![Teachable Machine - Step 1](Images/intro_nns_1.png)

* Allow the web application to use your webcam and microphone.

  ![Teachable Machine - Step 2](Images/intro_nns_2.png)

* Explain to students that now you are going to train the neural network model.

* Raise your left hand and press the _TRAIN GREEN_ button for few seconds and explain to students that your current image is the input data for the neural network. It's learning that these visual patterns correspond to a cute kitten.

  ![Teachable Machine - Step 3](Images/intro_nns_3.gif)

* Continue to train the purple class by posing seriously to the camera. Press the _TRAIN PURPLE_ button for a few seconds, and explain to students that now the neural network is learning that your poker face corresponds to a furry dog.

  ![Teachable Machine - Step 4](Images/intro_nns_4.gif)

* Finally, train the orange class by making a funny face and pressing the _TRAIN ORANGE_ button for few seconds. Explain to students that you are telling the neural network that this funny pose corresponds to a little bunny.

  ![Teachable Machine - Step 5](Images/intro_nns_5.gif)

Now that you train the model, play around by making several poses and faces to the camera:

* Rise your right hand and explain to students that despite that the neural network was trained to recognize your left hand raised, these kinds of models are continuously learning and are capable of recognizing and learning new patterns.

* Make a tricky test by partially raising your left hand; explain to students that the neural network gets confused but is still learning as can be seen on the confidence bars; finally, the model can decide on your partially raised hand.

![Teachable Machine - Step 6](Images/intro_nns_6.gif)

Explain to students that this funny experiment is just an example of the power of neural networks, instead of matching gestures with silly pets, you can use this kind of technology for business applications like building security systems.

Answer any questions before moving on.

---

### 3. Instructor Do: Anatomy of a Neuron (15 min)

After going more in-depth with neural networks, this activity will explain to students how single artificial neurons work.

Open the lesson slides. Move to the "Anatomy of a Neuron" Section and highlight the following:

* Neurons are the most fundamental units of a neural network.

* In 1958, [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt), an American psychologist, proposed the classical perceptron model.

* The model proposed by Rosenblatt was refined in 1969 by [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky) and [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert), who defined the first model of computational perceptron that is presented in the slides.

  ![Perceptron](Images/perceptron.png)

* The perceptron mimics the functioning of a biological neuron, it receives input data signals (_X<sub>n</sub>_) that can take boolean or numeric values.

* Every input data signal is weighted according to the relevance of each one under the context of the problem the perceptron was designed.

* The perceptron took a weighted sum of the inputs and set the output as `1` only when the sum is more than an arbitrary threshold.

* The _bias_ is added as a particular input labeled as _X<sub>0</sub>=1_ with a negative weight.

After this brief technical introduction to the perceptron, continue with the following quotidian example to illustrate how the perceptron works.

* Consider the task of predicting whether or not a person would watch a random movie on Netflix using the behavioral data available.

* Let us assume the decision depends on `3` binary inputs (binary for simplicity).

* In this perceptron model, _w<sub>0</sub>_ is called the bias because it represents the prejudice that can influence the final decision.

* A cinephile may have a low threshold and will be willing to watch any movie regardless of its genre, release date, or the awards the film received (`bias = 0`).

* In contrast, a father that wants to spend time with his daughter watching a movie may choose the latest children's film by default (`bias = 2`).

* In the case of the father, the model may give a lot of importance (high weight) to the `isNewRelease` and `isForChildren` inputs, and penalize the weights of the `isAwardWinning` input.

* The key point is the weights and the bias will depend on the data available, the viewing history in this case.

Continue to the slide entitled "The perceptron may be harsh" and highlight the following:

* In real life, if you want to choose a movie, you are not as strict as the perceptron could be.

* For example, if you base your decision only in one input variable, such as `isNewRelease`, the bias is set to `0.5` and _w<sub>1</sub> = 1_ then our perceptron would look as follows.

  ![Harsh perceptron](Images/harsh_perceptron.png)

* Using this model, the decision for a movie with `isNewRelease = 1` will be _Yes!_, and the decision for a movie with `isNewRelease = 0` will be _No!_.

* This decision may be too harsh since we are losing the chance of enjoying classic movies, or the Oscar awarded films from last year; this is where the activation function comes to the scene.

Move to the slide entitled _Activation Function_ and highlight the following:

* The neurons we use nowadays to build neural networks are an updated version of the perceptron proposed in 1969.

  ![Current neuron structure](Images/neuron_structure.png)

* The difference is the **activation function** that adds a dose of reality to neurons decisions. It is a mathematical function with a characteristic _S-shaped_ curve, also called the sigmoid curve.

  ![Sigmoid functions](Images/sigmoid_functions.png)

* Using an activation function, the output is a probability.

* Instead of _yes/no_ decision, with an activation function, we get the probability of yes, similar to using logistic regression.

* Following our example, using an activation function we can get a decision similar to real life, the final decision of watching a movie is a probability based on the input variables (what we know about the movie) and influenced by the bias (our personal preferences).

Explain to students that now you are going to demo how a single neuron works using the _TensorFlow Playground_.

Click on the [pre-configured link](https://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=1&seed=0.13671&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=true&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false) in the slide to open the _TensorFlow Playground_, slack out the link to students, and highlight the following.

![tfp_home.png](Images/tfp_home.png)

* [TensorFlow Playground](http://playground.tensorflow.org) is a website where users can train a neural network and visualize both the model creation process and the resulting predictions.

Take a moment to explain the layout of the page to the class.

* The _play_ button in the top left corner of the page, starts training the network.

  ![tf_play.png](Images/tf_play.png)

* In the same row as the play button, there are dropdowns for **Learning Rate**, **Activation Function**, **Regularization**, etc. These options affect how quickly a network learns and influences the goodness of its predictions.

* **Problem Type** is also on this row, and allows us to select whether we want the neural net to solve a regression or classification problem. We will demonstrate a classification problem for now.

* Below this row are headings for **Data**, **Features**, **Hidden Layers**, and **Output**.

* Under **Data**, we can select the data set on which to train the model. The options are two-dimensional data, which are easy to visualize. The two blobs in the bottom left are selected for this demo.

  ![two_blobs.png](Images/two_blobs.png)

* The **Features** section allows the user to specify properties to look for in the input data and is also the input layer of neurons in the network. Each additional neuron that we add in this layer represents another feature of the data. We have three inputs for this demo.

  ![Neuron's features](Images/neuron_features.png)

* **Hidden Layers** are layers of neurons that take the output of the layer before them as inputs, allowing the network to identify "higher-order" patterns and correlations among input features. For now, we'll use only one hidden layer with a single neuron, which results in a very simple architecture.

  ![tfp_hidden_layer.png](Images/tfp_hidden_layer.png)

* Finally, note the **Output** image, which plots the network's decision boundaries and generates a chart of the loss function. As the neural net learns, the loss function will decrease, and the decision boundaries will shift. The faster the loss function decreases, the more efficient the model; the lower the loss function becomes, the better it performs.

  ![Neuron's output](Images/neuron_output.png)

Emphasize that this data set is **linearly separable**; that is, we can easily draw a straight line between the two classes in this data.

Click on the _Play_ button to start training the network, and call attention to the output image on the right-hand side of the page. Point out that, right after the play button is pressed, the fit _changed_ over time.

* The network draws a linear decision boundary, as expected.

  ![Neuron's demo](Images/tfp_neuron_demo.gif)

Recall to students that this is not new, a variety of `sklearn` classifiers already covered in class can draw this boundary just fine. Logistic regression is one example.

* This example shows that neural networks can easily solve linear problems, but doesn't demonstrate their efficacy at nonlinear modeling problems.

* The real power or neural networks can be seen when we add more than one neuron, especially dealing with nonlinear data. This is going to be explored later in Today's class.

Answer any questions before moving on.

---

### 4. Everyone Do: Activating your first artificial neuron (15 min)

In this activity, students are introduced to Keras and how they can use this library to start building neural networks.

**Files:**

* [artificial-neuron.ipynb](Activities/01-Evr_Keras_Intro/Solved/artificial-neuron.ipynb)

Open the lesson slides, go to the _Activating Your First Artificial Neuron_ section and highlight the following:

* There are two ways to code a neuron:

  * You can do all the math and code it from scratch using Python, Pandas, and NumPy.

  * Or, you can use an industry-standard API or framework to speed up your implementation and focus your efforts on improving your model and have a better understanding of the business problem you want to solve.

* We are going to use [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) to build our Neural Networks.

* TensorFlow is an end-to-end open-source platform for machine learning, that allows us to run our code across multiple platforms in a highly efficient way.

* Keras is an abstraction layer on top of TensorFlow that makes it easier to build models. You can relate this to using Plotly Express to create charts instead of using the more verbose Matplotlib library.

* Using Keras and TensorFlow, we can use the standard `model -> fit -> predict` interface that students are used to seeing.

Ask students if they have already installed TensorFlow, if there are some students who don't, slack out the [installation guide](../Supplemental/deep_learning_installation_guide.md) and have your TAs to assist students in the process while you continue to the demo.

This demo is an Everyone Do activity where students are encouraged to follow your steps as you code, slack out the unsolved version of the Jupyter Notebook before continue.

Open the unsolved version of the Jupyter Notebook, explain to students that you are going to demo how a neural network with a single neuron can be made using Keras, encourage the class to replicate your live coding and highlight the following:

* We are going to use Keras through TensorFlow, so we import the Keras modules as follows:

  ```python
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense
  ```

* There are two types of models in Keras.

  * The `Sequential` model is a linear stack of layers, where data flows from one layer to the next as we saw in the TensorFlow playground.

  * The functional `Model` class, allows the creation of sophisticated and more customizable models.

* The `Sequential` model is going to be used in this class.

* The `Dense` class is used to add layers to the neural network.

Explain to students that we will start coding a neural network with a single neuron, to solve a binary classification problem similar to the example presented in the TensorFlow playground demo.

* A dummy dataset is created for this demo using the `make_blobs` function from `sklearn`.

  ```python
  X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=78)
  ```

* This dummy dataset contains 1000 samples with two features that are split into two groups.

* A DataFrame is created with the dummy data to create a plot using `hvplot`.

  ```python
  # Creating a DataFrame with the dummy data
  df = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
  df["Target"] = y

  # Plotting the dummy data
  df.hvplot.scatter(x="Feature 1", y="Feature 2", by="Target")
  ```

  ![Two blobs dummy data](Images/neuron-two-blobs.png)

* As we did with other machine learning algorithms, the data is split into training and testing datasets.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
  ```

Explain to students that before using a neural network, it is important to normalize or standardize the data. Neural networks typically perform better when each of the input features are on the same scale. This makes it easier for the neural network to stabilize and adjust the weights in the network.

* Scikit-Learn's `MinMaxScaler` or `StandardScaler` are commonly used to scale and normalize input features. The `StandardScaler` is used here to scale the features data. There is no need to scale the target data (`y`) since it's already encoded as `0` and `1`.

  ```python
  # Create scaler instance
  X_scaler = StandardScaler()

  # Fit the scaler
  X_scaler.fit(X_train)

  # Scale the data
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Once the data is scaled, explain to students that now we are going to create our first neural network.

* An instance of the `Sequential` model is created in the `neuron` variable.

  ```python
  neuron = Sequential()
  ```

* The `neuron` variable will store the architecture of our model.

* The next step is to add the first layer of our neural network using the `add()` method and the `Dense()` class.

  ![First Layer](Images/tensorflow-neuron-layer-1.png)

  ```python
  # First layer
  number_inputs = 2
  number_hidden_nodes = 1

  neuron.add(Dense(units=number_hidden_nodes, activation="relu", input_dim=number_inputs))
  ```

Explain to students, that as it was mentioned before, the `Dense()` class is used to add layers to the neural networks; since this is the first layer, we define the number of inputs in the `input_dim` parameter and the number of neurons in the first hidden layer in the `units` parameter.

* The `activation` parameter defines the activation function that is going to be used to process the values of the input features as they are passed to the first hidden layer. In this demo, the [rectified linear unit (relu) function is used](https://keras.io/activations/#relu).

* It's recommendable to add an activation function in this first layer, to add nonlinearity to our network, and enable it to learn nonlinear relationships while the neural network is trained.

* We finish creating our neural network by adding the output layer.

  ![Output layer](Images/tensorflow-neuron-output-layer.png)

  ```python
  # Output layer
  number_classes = 1

  neuron.add(Dense(units=number_classes, activation="sigmoid"))
  ```

* We use the `sigmoid` activation function in this layer since this is the output layer, there are no inputs to define, we only specify the number of `units` we want.

* The `summary()` method shows the architecture of the neural network model.

  ![Neuron summary](Images/tf_neuro_summary.png)

Explain to students that once that the structure of the model has been defined, it is compiled using a loss function and optimizer.

```python
neuron.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
```

* The `binary_crossentropy` loss function is used since this is a binary classification problem.

* Optimizers are algorithms that shape and mold a neural network while it's trained, to its most accurate possible for by updating the model in response to the output of the loss function. The `adam` optimizer is used in this demo.

* An additional training metric, `accuracy`, is also specified.

* After the model is compiled, it is fit (trained) using the dummy data.

  ```python
  model = neuron.fit(X_train_scaled, y_train, epochs=100)
  ```

* Training consists of using the optimizer and loss function to update weights during each iteration of your training cycle. This training using 100 iterations or epochs.

* After each epoch, the results of the loss function and the accuracy are displayed.

  ![Neuron training results](Images/neuron_binary_training.png)

* After the training ends, the model is evaluated by plotting the loss function and the accuracy across all epochs.

* To create the plots, a DataFrame is created using the `history` dictionary. This dictionary stores the `loss` and `accuracy` results of all epochs.

  ![Results plot from binary classification](Images/neuron_results_plot.png)

* Using this simple one-neuron neural network, it can be seen that loss function decreases as expected, and the accuracy is drastically improved to `1.0` in the first epochs.

* The model is evaluated using the `evaluate` method and the testing data.

  ![Neuron evaluate](Images/neuron_evaluate.png)

* Finally, some predictions are made using new dummy sample data and the `predict_classes` method.

  ![Neuron predictions](Images/neuron_predictions.png)

Explain to students that using this simple one-neuron neural network is just an example to show them how a neural network can be constructed using Keras. This model is as effective as logistic regression for linear data, now the question that arises is, how good this model could be for nonlinear data?

Continue the demo to demonstrate what happens when we use this model with nonlinear data.

* A nonlinear dummy dataset is created using the `make_moons()` function from `sklearn`, and a DataFrame is created to plot the data.

  ```python
  # Creating dummy nonlinear data
  X_moons, y_moons = make_moons(n_samples=1000, noise=0.08, random_state=78)

  # Transforming y_moons to a vertical vector
  y_moons = y_moons.reshape(-1, 1)

  # Creating a DataFrame to plot the nonlinear dummy data
  df_moons = pd.DataFrame(X_moons, columns=["Feature 1", "Feature 2"])
  df_moons["Target"] = y_moons
  ```

  ![Non-linear data plot](Images/non_linear_data_plot.png)

Since students are already familiar with the neural network creation workflow, explain to students that you are going to follow a similar process than before, but now, you are going to use the nonlinear data to train the same model.

```python
# Create training and testing sets
X_moon_train, X_moon_test, y_moon_train, y_moon_test = train_test_split(
    X_moons, y_moons, random_state=78
)

# Create the scaler instance
X_moon_scaler = StandardScaler()

# Fit the scaler
X_moon_scaler.fit(X_moon_train)

# Scale the data
X_moon_train_scaled = X_moon_scaler.transform(X_moon_train)
X_moon_test_scaled = X_moon_scaler.transform(X_moon_test)

# Training the model with the nonlinear data
model_moon = neuron.fit(X_moon_train_scaled, y_moon_train, epochs=100, shuffle=True)
```

* After training the model with the nonlinear data, it can be seen that the performance is worse than in the previous example, especially the accuracy is lower.

  ![Non-linear data plots](Images/neuron_plot_non_linear.png)

* The model is evaluated with 10 new dummy samples, it can be corroborated that results aren't as good as the ones obtained with linear data, this is because using only one-single neuron is not unveiling the power of neural networks to find nonlinear patterns.

  ![Non-linear data evaluation](Images/non_linear_loss_accuracy.png)

Explain to students that in the next activity, they will learn how they can create more complex networks that can handle more complexity and nonlinearity in the data.

Answer any questions before moving on.

---

### 5. Instructor Do: Connecting neurons (15 min)

In this activity, students will learn how to build more complex neural networks using Keras.

**Files:**

* [connecting_neurons.ipynb](Activities/02-Ins_Connecting_Neurons/Solved/connecting_neurons.ipynb)

Explain to students that now they will learn how to create more complex neural networks.

For this demo, comment to the class that you are going to use nonlinear dummy data to show how neural networks deal with it.

Open the unsolved version of the Jupyter Notebook, live code the demo, and highlight the following:

* Some dummy nonlinear data is created using the `make_moons()` function from `sklearn`.

  ```python
  # Creating dummy nonlinear data
  X_moons, y_moons = make_moons(n_samples=1000, noise=0.08, random_state=78)

  # Transforming y_moons to a vertical vector
  y_moons = y_moons.reshape(-1, 1)
  ```

* A DataFrame is created to plot the dummy data using `hvplot`.

  ```python
  # Creating a DataFrame to plot the nonlinear dummy data
  df_moons = pd.DataFrame(X_moons, columns=["Feature 1", "Feature 2"])
  df_moons["Target"] = y_moons
  ```

  ![Non-linear data plot](Images/nn_1.png)

* The data is split into training and testing sets, and it is scaled prior to building and testing the neural network.

  ```python
  # Create training and testing sets
  X_moon_train, X_moon_test, y_moon_train, y_moon_test = train_test_split(
      X_moons, y_moons, random_state=78
  )

  # Create the scaler instance
  X_moon_scaler = StandardScaler()

  # Fit the scaler
  X_moon_scaler.fit(X_moon_train)

  # Scale the data
  X_moon_train_scaled = X_moon_scaler.transform(X_moon_train)
  X_moon_test_scaled = X_moon_scaler.transform(X_moon_test)
  ```

Explain to students that now you are going to create a more complex neural network by adding a hidden layer with six neurons.

![Neural net sample](Images/simple-nn.png)

Explain to students that the rule-of-thumb for a neural network is to have triple the amount of nodes in the hidden layer as the number of inputs, this is not true of deep learning, but it's a good point to start prototyping a neural network.

Start building the neural network and highlight the following.

* A sequential model is created to define the neural network.

  ```python
  nn = Sequential()
  ```

* The first layer is added by defining two input features and six hidden nodes. The `relu` activation function is used.

  ![First layer in the neural network](Images/simple-nn-layer-1.png)

  ```python
  # First layer
  number_inputs = 2
  number_hidden_nodes = 6

  nn.add(Dense(units=number_hidden_nodes, activation="relu", input_dim=number_inputs))
  ```

* The output layer is added by defining one unit. The `sigmoid` activation function is used to show students how, by only adding more neurons to the network, the model accuracy improves.

  ![Second layer in the neural network](Images/simple-nn-layer-2.png)

  ```python
  # Output layer
  number_classes = 1

  nn.add(Dense(units=number_classes, activation="sigmoid"))
  ```

* After presenting the model summary, it's compiled and trained with `100` epochs to compare the results with the previous example where only one neuron was used.

```python
# Compile model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Training the model with the nonlinear data
model_moon = nn.fit(X_moon_train_scaled, y_moon_train, epochs=100)
```

* After evaluating the model, it can be seen that after adding more neurons to the model, the accuracy improves.

  ![Neural network evaluation](Images/nn_2.png)

Ask students the following question:

* How do you think we can improve the model accuracy?

  * **Sample Answer:** We can add more neurons to the hidden layer.

  * **Sample Answer:** We can add a second hidden layer.

  * **Sample Answer:**  We may test with different activation functions.

Collect a couple of answers from the class and highlight the following:

* Adding more neurons to the model is a possible solution; however, we can overfit the model.

* Adding a second layer is also a suitable solution; this is part of deep learning, and it is going to be covered next class.

* Testing with different activation functions is one of the most used initial solutions, especially when dealing with nonlinear data.

* Using more epochs for training is another strategy to improve the model's accuracy.

Explain to students that modeling neural networks is part science and part and art; the best model will be the result of several tests by playing around with the number of neurons and testing different activation functions.

Answer any questions before moving on.

---

### 6. Student Do: Preventing credit card defaults with neural networks (20 min)

In this activity, students will train a neural network model to predict whether a credit card holder will default in the next month.

**Instructions:**

* [README.md](Activities/03-Stu_CC_Default/README.md)

**Files:**

* [credit-card-default.ipynb](Activities/03-Stu_CC_Default/Unsolved/credit-card-default.ipynb)

---

### 7. Instructor Do: Review Preventing credit card defaults with neural networks (10 min)

**Files:**

* [credit-card-default.ipynb](Activities/03-Stu_CC_Default/Solved/credit-card-default.ipynb)

Walk through the solution and highlight the following:

* After the data is read in a DataFrame, it is split and scaled using the `StandardScaler()` function from `sklearn`.

* The neural network is defined, adding two layers as follows.

  ```python
  # Define the model
  number_inputs = 23
  number_hidden_nodes = 69

  nn = Sequential()
  nn.add(Dense(units=number_hidden_nodes, input_dim=number_inputs, activation='relu'))
  nn.add(Dense(1, activation='sigmoid'))
  ```

* The first layer has the `23` features as input dimensions, following the rule-of-thumb mentioned before, the triple amount of nodes were defined in the hidden network (`69` units).

* The model is compiled and trained using `100` epochs. Due to the number of records, the training process takes a few minutes to finish.

* The model is evaluated by plotting the loss function, the accuracy, and executing the `evaluate()` method.

  ![Model evaluation](Images/cc-results.png)

* The accuracy is not great, but it also is not as bad to discard the model. It could be used in a real-world scenario to run a pilot project.

Explain to students that for the challenge section, different approaches could be taken, for this demo, the `tanh` activation function is used in the output layer, and the model is trained with `50` epochs.

```python
# Define the model
number_inputs = 23
number_hidden_nodes = 69

nn_2 = Sequential()
nn_2.add(Dense(units=number_hidden_nodes, input_dim=number_inputs, activation='relu'))
nn_2.add(Dense(units=1, activation='tanh'))

# Compile model
nn_2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model_2 = nn_2.fit(X_train_scaled, y_train, epochs=50)
```

* As it can be seen in the model's evaluation, the accuracy improves a little bit. Having more epochs not always make accuracy better.

Answer any questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Preparing Data for Neural Networks (15 min)

In this section, we will go over some necessary transformations of data before it can be fed into a neural network.

**Files:**

* [04-Ins/preparing_data.ipynb](Activities/04-Ins_Preparing_Data/Solved/preparing_data.ipynb)

Open the lesson slides, move to the _Preparing Data for Neural Networks_ and highlight the following:

* Like any machine learning model, neural networks require some preprocessing of data to be used effectively.

* Neural networks cannot deal with categorical variables in their raw forms, and explanatory variables that are represented in different units or have vastly different scales of magnitude can make models difficult to train.

* To solve the first problem, we apply one-hot encoding to categorical values to transform them into binary variables. To deal with the second, we use standardization.

* One hot encoding involves taking a categorical variable, such as color with labels "red," "white," and "blue," and creating three new variables of the colors, with each instance of the data now showing a `1` if it corresponds to that color and `0` if it does not.

* Scikit-learn offers an implementation of one-hot encoding in the [`OneHotEncoder` module](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html).

Open the unsolved Jupyter Notebook and ask students to follow along as your live code one-hot encoding and model scaling.

* For this demo, the iris dataset is used. The data is loaded into a DataFrame.

  ![Loading data](Images/ohe-1.png)

* The `class` column is going to be used to demonstrate how one-hot-encoding works in `sklearn`.

* An instance of the `OneHotEncoder` module is created

  ```python
  enc = OneHotEncoder()
  ```

* To encode the iris classes, the encoder is fit with the values of the `class` column. Note that the values are reshaped as a one-column vector.

  ```python
  class_values = data["class"].values.reshape(-1, 1)
  enc.fit(class_values)
  ```

* Once the encoder is fit, the `categories_` attribute stores the categories that were found by the encoder.

  ![Categories identified by the encoder](Images/ohe-2.png)

* The `class` column data is encoded using the `transform` method; the result is stored as an array.

  ```python
  class_encoded = enc.transform(class_values).toarray()
  ```

* Once the data is encoded, a DataFrame is created that can be used to store the encoded data as a `CSV` for further usage.

  ![One-hot encoded data](Images/ohe-3.png)

* After the data is encoded, each categorical variable is represented as a sequence of `1's` and `0's`.

  ![Sample encoded data](Images/ohe-4.png)

Ask the class to restate what we have accomplished with one-hot encoding.

* **Sample Answer**: We've transformed one categorical variable into many binary (numerical) variables, each corresponding to a category.

Switch back to the lesson slides, continue with the slide entitled _Data Standardization_ and highlight the following:

* Another critical preprocessing task is to standardize the numerical variables in the dataset.

* Standardization involves de-meaning the variables, that is, make it so that each numerical variable has a mean of `0`, and constant variance of `1`.

* This makes it so that the variables all have approximately the same size, and reduces the likelihood that outliers or variables in different units will negatively affect model performance.

* Students are already familiar with the `StandardScaler` from Scikit-learn, which offers an easy way to standardize variables.

Come back to the Jupyter Notebook to recall data standardization, live code the demo, and highlight the following.

* To demonstrate data standardization, the iris numerical features are used.

  ```python
  data_to_scale = data.iloc[:, :4]
  ```

* Once the data to scale is selected, it is scaled using the `StandardScaler` following the steps that students are familiar with.

```python
# Create the StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
scaler.fit(data_to_scale)

# Scale the data
scaled_data = scaler.transform(data_to_scale)

# Create a DataFrame with the scaled data
features_scaled_data = pd.DataFrame(scaled_data, columns=data.iloc[:, :4].columns)
```

Ask students if they have any questions before moving on to the next activity.

---

### 10. Students Do: Smartphone Activity Detector (30 min)

In this activity, students will create a neural network to predict the activity of the user based on their smartphone's accelerometer data.

**Files:**

* [Smartphone_Activity_Detector.ipynb](Activities/05-Stu_Smartphone/Unsolved/Smartphone_Activity_Detector.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Smartphone/README.md)

---

### 11. Instructor Do: Review Smartphone Activity Detector (10 min)

**Files:**

* [Smartphone_Activity_Detector.ipynb](Activities/05-Stu_Smartphone/Solved/Smartphone_Activity_Detector.ipynb)

Open the solution and highlight the following points about the data preparation:

* The dataset consists of 561 input features that are obtained from the smartphone. Many of these features are actually transformations of the original smartphone accelerometer data. The complete explanation of input features can be found from the source URL for the dataset.

* While this particular dataset appears to already be in a normalized form, it may be safer to scale the input features using StandardScaler or MinMaxScaler.

  ```python
  # Scale the training and testing input features using StandardScaler
  X_scaler = StandardScaler()
  X_scaler.fit(X_train)

  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

* There are 12 target activity labels that can be identified using the `value_counts` function.

  ```python
  y.activity.value_counts()
  standing              1423
  laying                1413
  sitting               1293
  walking               1226
  walking_upstairs      1073
  walking_downstairs     987
  stand_to_lie            90
  sit_to_lie              75
  lie_to_sit              60
  lie_to_stand            57
  stand_to_sit            47
  sit_to_stand            23
  Name: activity, dtype: int64
  ```

* The target labels must be converted to one-hot encoded vectors before the model can be trained. The `OneHotEncoder` can be used to make this transformation.

  ```python
  # Apply One-hot encoding to the target labels
  enc = OneHotEncoder()
  enc.fit(y_train)

  encoded_y_train = enc.transform(y_train).toarray()
  encoded_y_test = enc.transform(y_test).toarray()
  encoded_y_train[0]
  ```

Next, walk through the process of building and training the model. Highlight the following:

* A Keras Sequential model is used to create the neural network.

  ```python
  model = Sequential()
  ```

* The first layer specified for the neural network actually defines both the input layer and the hidden layer. There are 561 input nodes defined by `input_dim` and 100 nodes in the hidden layer. Each of the hidden layer neurons uses a `relu` activation function, which is a common activation function.

  ```python
  model.add(Dense(100, activation='relu', input_dim=X_train_scaled.shape[1]))
  ```

* In this case, the choice of 100 nodes is somewhat arbitrary, but it provides enough complexity to sufficiently predict the activity type. Because this number was much less than the number of input features, it is very likely that many of the input features are not useful or needed to predict the activity type. Further experimentation with dimensionality reduction techniques such as PCA could show that a smaller number of input features could be used.

* The final output layer consists of 12 nodes (one node for each activity type) with a softmax activation type. This choice matches the one-hot encoding that was used on the target labels.

  ```python
  model.add(Dense(number_outputs, activation="softmax"))
  ```

* `Categorical Crossentropy` was chosen for the loss function. This is common for building a neural network classifier, but there are other [loss function options available in Keras](https://keras.io/losses/):

  * `binary_crossentropy` is used for binary classification.

  * `categorical_crossentropy` is used for classification models.

  * `mean_squared_error` is used for regression models.

* The `adam` optimizer is a popular choice for neural networks. Again, other options are available and documented on the Keras homepage, but `adam` is typically a safe choice to use.

Take a moment to show the model summary and the number of total trainable parameters in the model. Highlight the following:

* This neural network is very large due to the number of input features and the choice of 100 hidden notes. Each input feature is connected to each hidden node, so that results in the total number of training parameters in the model.

* Dimensionality reduction techniques such as PCA may improve the model performance and model size.

Show students the code to fit the model and explain that the model converges to a high accuracy very quickly.

Warn students that large neural networks like this are often prone to over-fitting. Adjusting the network architecture and the number of training epochs may help prevent overfitting. Neural Network architectures should always be validated to ensure that they are not over-fitting to the training data and thus performing poorly on new data values.

Show how the classification report can be used to evaluate the model performance for each activity type.

```python
from sklearn.metrics import classification_report
print(classification_report(results.Actual, results.Predicted))
                    precision    recall  f1-score   support

            laying       1.00      1.00      1.00       355
        lie_to_sit       0.76      0.87      0.81        15
      lie_to_stand       0.80      0.73      0.76        11
        sit_to_lie       0.89      0.74      0.81        23
      sit_to_stand       1.00      0.75      0.86         4
           sitting       0.95      0.97      0.96       337
      stand_to_lie       0.74      0.78      0.76        18
      stand_to_sit       0.93      0.93      0.93        15
          standing       0.97      0.95      0.96       367
           walking       1.00      0.99      0.99       300
walking_downstairs       0.99      0.99      0.99       230
  walking_upstairs       0.99      1.00      0.99       267

          accuracy                           0.97      1942
         macro avg       0.92      0.89      0.90      1942
      weighted avg       0.97      0.97      0.97      1942
```

Explain to students that this is a really good example of how neural networks can be used to transform FinTech. Consider providing an example such as the following:

> A hypothetical FinTech company is interested in providing a mobile application for micro renewable energy investments yielding ~4-8% per year with small investments. The company wants to remind users to make additional investments when they are the most likely to see and respond to the smartphone notifications. A neural network activity predictor could be used to detect the optimal activity types in which a user responds to the notification.

Ask students if they can think of any additional FinTech uses for an activity detector like this.

Ask for any remaining questions before moving on.

---

### 12. Instructor Do: Homework Demo (10 min)

In this activity, the instructor will conduct a demonstration of the homework.

**Files:**

* [README.md](../../../02-Homework/14-Deep-Learning/Instructions/README.md)

Open the lesson slides, move to the _Unit 14 Homework Solution Demo_ and highlight the following:

* Cryptocurrencies are gaining the attention of investors; however, due to its volatility and nature, conventional indicators and metrics are not always suitable.

* The [Crypto Fear and Greed Index (FNG)](https://alternative.me/crypto/fear-and-greed-index/) is an instrument used to assess cryptocurrencies.

* FNG attempts to use a variety of data sources to produce a daily value for cryptocurrency, based on sentiment from social media and news articles to help guide trading strategies.

* In this Unit's homework assignment, you will build and evaluate deep learning models, using both the FNG values and simple closing prices, to determine if the FNG indicator provides a better signal for cryptocurrencies than the normal closing price data.

Open the homework solutions and explain to students that in this unit, they will learn how to deal with time series using Long short-term memory (LSTM) recurrent neural networks (RNN); this special type of neural networks will be a key part to develop the homework's solution.

Answer any questions before moving on.

---

### 13. Instructor Do: Reflect (5 min)

This day may be hard for students since several new concepts were covered, spend a few minutes with the class reflecting on what they learn today.

* Recall students that modeling neural networks is part art and part science, so they should be patient while defining models.

* There are several frameworks to implement neural networks, Keras is a business class framework they can trust in for prototyping or deploy production models.

* Mastering neural networks take time; however, thanks to frameworks like Keras, you don't need to have a Ph.D. to start using neural networks to solve real-world problems.

* Neural networks are not the panacea; they are just other options in the machine learning realm; in the end, the only way to find a solution is by testing and benchmarking different algorithms.

Congratulate students on learning a new skill that will add value to their professional portfolio; answer any questions before ending the class.

## End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
