### 6. Instructor Do: TensorFlow Playground (20 min)

Return to the slides and use the section titled TensorFlow Playground to begin the this section. 

* Now that we have some intuition on how individual neurons work, we can move on to neural networks. As mentioned before, neural network architectures take advantage of the fact that indiviual neurons can be linked so that their inputs can be converted to outputs, which become inputs for other neurons. The underlying math is outside the scope of this class, but we can still get to a good intuitive understanding of how this works through creating and tinkering with a model. Luckily, we don't even need any code to do it!

* [TensorFlow Playground](http://playground.tensorflow.org) is a website where users can train a neural network and visualize both the model creation process and the resulting predictions. 

Slack out the link included above to the students and have them follow along while you demonstrate using the playground. 

![tfp_home.png](Images/tfp_home.png)

* Take a moment to explain the layout of the page to the class.

* Note the "play" button in the top left corner of the page. Explain that clicking this starts training the network.

  ![tf_play.png](Images/tf_play.png)

* In the same row as the play button, there are dropdowns for **Learning Rate**; **Activation Function**; **Regularization**; etc. These options affect how quickly a network learns, and influence the goodness of its predictions. For now, we'll leave these options in their default states. **Problem Type** is also on this row, and allows us to select whether we want the neural net to solve a regression or classification problem. We'll demonstrate a classification problem for now. 

* Below this row are headings for **Data**; **Features**; **Hidden Layers**; and **Output**.

* Under **Data**, we can select the data set on which to train the model. The options are two-dimensional data, which are easily visualizable. First, we'll select the two blobs in the bottom left.

  ![two_blobs.png](Images/two_blobs.png)

* The **Features** section allows the user to specify properties to look for in the input data, and is also the input layer of neurons in the network. Each additional neuron that we add in this layer represents another feature of the data. We will select only x<sub>1</sub> and x<sub>2</sub>, which should be the defaults.

  ![x1_x2.png](Images/x1_x2.png)

* **Hidden Layers** are layers of neurons that take the output of the layer before them as inputs, allowing the network to identify "higher-order" patterns and correlations amongst input features. For now, we'll use only one hidden layer, which results in a very simple architecture. A common rule of thumb for 3-layer networks is to use three times as many nodes in the hidden layer as in the input layer, so we'll configure our hidden layer with 6 neurons.

  ![tfp_hidden_layer.png](Images/tfp_hidden_layer.png)

* Finally, note the **Output** image, which plots the network's decision boundaries and generates a chart of the loss function. As the neural net learns, the loss function will decrease and the decision boundaries will shift. The faster the loss function decreases, the more efficient the model; the lower the loss function becomes, the better it performs.

  ![tfp_setup.png](Images/tfp_setup.png)

* Emphasize that this data set is **linearly separable**; that is, we can easily draw a straight line between the two classes in this data. 

Start training the network, and call attention to the output image on the right-hand side of the page. Begin training the model by clicking the play button in the top left corner. Point out that, right after the play button is pressed, the fit _changed_ over time.

* The network draws a linear decision boundary, as expected.

  ![nnet_linear_classification.png](Images/nnet_linear_classification.png)

* This isn't new: A variety of sklearn classifiers already covered in class can draw this boundary just fine. Logistic regression is one example. This example shows that neural networks can easily solve linear problems, but doesn't demonstrate their efficacy at modeling nonlinearities.

Explain to students that neural nets are particularly powerful at modeling nonlinearities. This implies they should be good at distinguishing linearly separable regions, as well. Click the blob-in-circle data set on the left.

* Highlight that these two regions are highly nonlinear. The nonlinearity is due to the fact that the regions are separated by a circle, so there's no single _line_ that can be drawn to distinguish them.

  ![blob_in_circle.png](Images/blob_in_circle.png)

Now, train the network, and observe how neural nets learn nonlinearities. Click the play button in the top left.

* It takes much longer for the network to find the circular decision boundary than the linear one. However, the fact that the neural network did seem to find the correct boundaries is a better result than could be expected from models like logistic regression. 

Select the third and fourth features, and train the model once again. Note how the loss function decreases faster, and how the boundary seems more circular than before. Tell students that changing the number of neurons in the input and hidden layers can significantly affect performance. 

Take any questions before moving on to the next student activity. 