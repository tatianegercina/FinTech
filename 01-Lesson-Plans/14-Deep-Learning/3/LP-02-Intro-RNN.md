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

  * **Answer:** The short answer for this question is _No_; if you try to predict the direction of a car only with the information of a still image, you don't have enough information to predict beyond of a _random guess_.

Explain to the class that without knowledge of where the car has been, you wouldn't have enough data to predict where the car is going.

Highlight the following reasons that ANNs are not suitable for detecting patterns over time:

* If we record in movement, we may have enough information to make a better prediction since we can have a sequence of images representing the car's movement.

* A new challenge arises, ANNs don't have a memory mechanism to store the different states of a sequence of images _per se_.

* This is where RNNs comes into action! RNNs are good at modeling sequence data thanks to their sequential memory.

* Following the example in the slides, using RNNs, we can predict that the car is moving to the right.

Explain to class, that in contrast to an ANN, an RNN can remember previous data thanks to a feedback loop. This feedback loop allows information to flow from one step to the next along the sequence.

![ANNs Vs. RNNs](Images/ann_vs_rnn.png)

* For the car-in-motion example, the feedback loop of the RNN allows us to save the position of the car from one step to the next one as long as we have sequence data about the car's location.

Use an example from Natural Language Processing to explain how RNNs work:

* When a person reads a sentence such as `I want to invest for retirement`, the brain starts to make associations among the words as the person reads the sentence.

  ![RNN words](Images/rnn-words.png)

* The brain can decode the phrase and understand it because the architecture of our brain has memory to capture the sequence of the words in time. RNNs attempt to replicate this behavior.

* If we pass the sentence to an RNN, the sentence is split into individual words and the following steps are performed:

  * The first step is to feed `I` into the RNN. The RNN encodes `I` and produces an output (`01`).

  * For the next step, we feed the word `want` and the hidden state from the previous step. The RNN now has information on both the word `I` and `want`.

  * This process is repeated until the final step. By the last step, the RNN has encoded information from all the words in previous steps.

  * The final output (`06`) was created from the rest of the sequence. To predict what the phrase means, we take the final output and pass it to the feed-forward layer of the RNN to classify the intent.

  ![RNN prediction](Images/rnn_prediction.png)

Explain to students that the memory in an RNN has limitations; they only remember the most recent few steps of a sequence.

* The vanishing gradient in the hidden states illustrates this issue known as _short-term memory_.

  ![Vanishing gradient](Images/rnn_gradient.png)

* It can be seen that the RNN remembers a lot from the _brown state_, but just a little from the _red state_.

* This _short-term-memory_ issue is solved by using Long-Short-Term Memory Recurrent Neural Networks (aka LSTM or LSTM-RNN).

Explain to the class that we are not going over the math complexity of LSTMs. However, the key point is to know that an LSTM RNN works like an original RNN. The critical difference is that an LSTM can selectively decide which types of longer-term events are worth remembering and which are OK to forget.

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
