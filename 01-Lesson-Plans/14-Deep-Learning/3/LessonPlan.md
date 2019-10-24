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
