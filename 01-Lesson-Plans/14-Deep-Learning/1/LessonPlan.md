## 14.1 Lesson Plan: Neural Networks

### Overview

Today's class introduces students to a neural networks, a new member of the machine learning algorithms that can be used for classification and regression problems, but are perhaps uniquely able to learn very complex, non-linear models. Conceptually, neural networks were inspired by neurons in the human brain, and have a similar property of scaling to meet the complex environments that they operate in.

Neural networks are very flexible in their applications, but they are not necessarily meant to be "plug-and-play." From preprocessing input data to constructing a neural network architecture, students will learn the process to successfully construct and use neural networks.

### Class Objectives

By the end of class, students will be able to:

* Explain the concept of neural networks, including how a neuron is akin to logistic regression.

* Explain the intuition of how weights of neurons are determined.

* Understand how choice of inputs and hidden layers apply to problems regression and classification.

* Experiment with architecture in Tensor Flow playground.

* Preprocessing data for neural network models.

* Identify the Python libraries available to build neural networks.

* Describe what are the pros and cons of using Keras for building neural networks.

* Implement neural nets with Python Keras API.

### Instructor Notes

* Today's activities will be concept-heavy, so students should be prepared to discuss and think, and not merely to practice steps for implementation.

* Give students the opportunity to ask questions, and when necessary, have students save questions for the review sessions or office hours.

* Today should also be fun, since we'll be playing with neural nets in several ways to experiment with input, architecture, and algorithms.

* A thorough understanding of neural networks would require math that's beyond the scope of this class. Luckily, we only need an intuitive understanding of the underlying algorithms in order to implement a neural network. Some details will necessarily need to be glossed over, but we will provide some additional materials for those students who are inclined to dig deeper.

* In the introduction to neural networks, a demo is made using the [Teachable Machine project from Google][https://teachablemachine.withgoogle.com/], be sure to practice the demo before class. If you are not familiar with this project, we encourage you to watch this video.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson 14.1 Slides]().

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Open the lesson slides and welcome students to the first day of deep learning! Indicate that Today's class will begin with an introduction to the basic unit of neural networks before moving on to constructing simple neural nets.

As an icebreaking activity, open the class by asking the following questions to students:

* What do you think a neural network is?

  * **Sample Answer:** It's a computer representation of a human neuron.

  * **Sample Answer:** It's a method to create artificial intelligence software.

  * **Sample Answer:** Neural networks are machine learning algorithms that can learn to solve a problem.

* Do you know some cool applications of neural networks?

  * **Sample Answer:** Autonomous cars.

  * **Sample Answer:** Image processing in cancer detection.

  * **Sample Answer:** Banning inadequate content on social networks.

  * **Sample Answer:** Automated trading based on artificial intelligence.

Ask for two or three volunteers to share their insights, and comment to students that Today they will answer these questions.

Ask if there are any questions before moving on.

---

### 2. Instructor Do: Neural Networks are Cool! (10 min)

Open the lesson slides and move to the _Neural Networks are Cool!_ section.

Start the presentation by showing students the following image from the [Rorschach Inkblot Test](https://en.wikipedia.org/wiki/Rorschach_test), and ask them the next question:

* What do you see in this image?

  ![Rorschach Test Card](Images/Rorschach_blot_05.jpg)

Allow students to play around for few seconds sharing what they see, continue the presentation by telling students that there is no precise answer to this question.

Continue to the _How our brain works_ slide, and explain to students that any similitude they could find from the image with a real object, is possible because our brain uses thousands of neurons connections to find a match between the visual input and a mental representation of an object.

Follow to the slide entitled _Our brain as inspiration for artificial neural nets_, and comment to students that this power of our brain to process information and make predictions or interpretations is the fact that inspires neurophysiologists and mathematicians to start the development of artificial neural networks (ANN).

* In the same way biological neurons receive input signals through the dendrites, an ANN is able to receive input variables and process those inputs using an activation function to compute an output, akin the neuron nucleus in the brain.

Tell students that you will go over the details of how a neuron works in the next activity.

Continue to _The History of Neural Networks_ slide and highlight the following:

* The concept of ANNs was presented for the very first time in 1943, when Warren McCulloch and Walter Pitts opened the subject by creating a computational model for neural networks that they implemented using electrical circuits.

* From that initial idea of a single neuron, the concept evolved the last decades to more complex models that propose creating connections between neurons to the point of creating what we know Today as neural networks.

* Nowadays neural networks are discussed in almost every field, from preventing cancer or credit card frauds to creating artistic expressions using artificial intelligence or having self-driving cars.

Follow to the slide entitled _The Future is here: Awesome applications of neural nets_ and highlight the following:

* Neural networks are here to stay, and applications become more common every day.

* Companies like Google or Tesla are using neural networks to develop self-driving cars.

* Using the power of neural networks, Today you can talk in any language thanks to the automated translation of instant messaging applications like Skype.

* Memories from the past that were captured in black and white can take a new perspective through automatic image colorization.

* Neural networks are also used to create a better world, not only for humans but also for wildlife thanks to projects like the one led by the U.S. National Oceanic and Atmospheric Administration where they are saving whales by tracking the north Atlantic right whales population using neural networks for image recognition.

As you continue to the slide entitled _Neural Networks Applications in Finance_, comment to students that financial sector is leading in the use of neural networks, highlight the following applications and slack out the links of each one for further reference:

* [Credit card fraud detection](https://www.semanticscholar.org/paper/Credit-card-fraud-detection-with-a-neural-network-Ghosh-Reilly/ba70a74262adec9dcfa47b5710752d2537a07af4)

* [Foreign-Exchange-Rate Forecasting](https://www.springer.com/gp/book/9780387717197)

* [Risk Management](https://dx.doi.org/10.2991/ispcbc-19.2019.138)

* [Algorithmic Trading](https://link.springer.com/article/10.1007/s10479-019-03144-y)

* [Automated invoices processing](https://link.springer.com/chapter/10.1007/978-3-319-99695-0_29)

* [Preventing Money Laundering](https://doi.org/10.1109/ICNSC.2019.8743234)

Comment to students that there are several deep mathematical concepts behind neural networks that are beyond the scope of Today's class.

Explain to students that this week, we will give an intuitive introduction to the components that make up a neural network and how they work together to learn.

Continue to the _Python Libraries for Neural Networks_ slide, explain to students that there are several Python libraries to implement neural networks, the most used in industry and the research community are the following:

* [TensorFlow (from Google)](https://www.tensorflow.org/)

* [Microsoft Cognitive Toolkit (CNTK)](https://docs.microsoft.com/en-us/cognitive-toolkit/)

* [Apache mxnet](https://mxnet.incubator.apache.org/)

* [Pytorch](https://pytorch.org/)

* [Keras](https://keras.io/)

Comment to students that we will use Keras in the class and that an introduction comes next; in the meantime, it's time for a funny example about how neural networks work.

Open your web browser and navigate to [the Teachable Machine website](https://teachablemachine.withgoogle.com). This web application shows the fundamental mechanism of a neural network by training a model that recognizes gestures from your webcam to predict one of three classes.

Once you open the Teachable Machine website, follow the next steps to conduct the demo.

* Click on the _skip the tutorial_ option to start the demo.

  ![Teachable Machine - Step 1](Images/intro_nns_1.png)

* Allow the web application to use your webcam and microphone.

  ![Teachable Machine - Step 2](Images/intro_nns_2.png)

* Explain to students that now you are going to train the neural network model.

* Raise your left hand and press the _TRAIN GREEN_ button for few seconds, comment to students that your current image is the input data for the neural network, it's learning that these visual patterns correspond to a cute kitten.

  ![Teachable Machine - Step 3](Images/intro_nns_3.gif)

* Continue to train the purple class by posing serious to the camera, press the _TRAIN PURPLE_ button for few seconds, and explain to students that now the neural network is learning that your poker face corresponds to a furry dog.

  ![Teachable Machine - Step 4](Images/intro_nns_4.gif)

* Finally, train the orange class by making a funny face and press the _TRAIN ORANGE_ button for few seconds, comment to students that you are telling the neural network that this crazy pose corresponds to a little bunny.

  ![Teachable Machine - Step 5](Images/intro_nns_5.gif)

Now that you train the model, play around by making several poses and faces to the camera:

*  Rise your right hand and explain to students, that despite the neural network were trained to recognize your left hand raised, these kind of models are continuously learning and are capable of recognizing and learning new patterns.

* Make a tricky test by partially raising your left hand, comment to students that the neural network gets confused but is still learning as can be seen on the confidence bars, finally the model is able to make a decision about your partial hand raised.

![Teachable Machine - Step 6](Images/intro_nns_6.gif)

Comment to students that this funny experiment is just an example of the power of neural networks, instead of matching gestures with silly pets, you can use this kind of technology for business applications like building security systems.

Answer any questions before moving on.
