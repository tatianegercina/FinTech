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


### 5. Instructor Do: Intro to Deep Learning

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

### 6. Instructor Do: Deep Learning with Tensorflow

**Files:**

* Solved: [deeplearning.ipynb](Activities/03-Ins_Deep_Learning/Solved/deeplearning.ipynb)




---

### 7. Students Do: Sound of Music (15 mins)

In this activity students will build a model to predict the geographical origins of a musical composition. 

**Instructions:**

* [README.md](Activities/04-Stu_Sound_of_Music/README.md)

**Files:**

* [music].ipynb]((Activities/04-Stu_Sound_of_Music/Unsolved/music.ipynb)
