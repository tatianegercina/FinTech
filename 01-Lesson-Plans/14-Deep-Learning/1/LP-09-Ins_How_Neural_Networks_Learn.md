### 9. Instructor Do: How Neural Networks Learn (15 min)

Open the slides for this unit and use the How Neural Networks Learn section to guide students through this lecture. This section introduces a few new terms and concepts, so proceed slowly and ask for questions often. It may also be useful to refer to the Tensorflow Playground page at various points to highlight or visualize certain ideas. 

* Students may have noticed the "activation function" setting in the Playground. This selection refers to the shape of the function we are using in each neuron to transform inputs to outputs. One popular activation function is the sigmoid, which also happens to be the function associated with logistic regression

![sigmoid.png](Images/sigmoid.png)

* It's a little confusing, but there are usually two activation functions associated with neural nets with at least one hidden layer. One is for the hidden layer(s), and the other for the output layer. The hidden layer's activation function will always be a non-linear function, such as sigmoid or ReLU - this is to ensure that the neural network can learn complex, non-linear models. The output layer's activation function depends on the problem we are trying to solve: regression problems require a linear activation, while classification problems usually use a non-linear function. This is because the linear function can output a continuous numerical variable, which is needed for a regression problem. The activation function choice in the Playground controls the function for the hidden layer. 

* The process by which the activated neurons pass on their output to the next layer is called forward propagation. Each neuron takes in data, multiplies the variables by its weights and adds a bias, and passes this number through the activation function to get an output. This output is passed on to the neurons in the next layer as input. 

* The output eventually makes its way through the layers to the output layer, where it is compared against the actual outcome variable to see how well it fits the data. As we have previously said, this goodness of fit is approximated by a cost or loss function. For regression problems, we typically use mean squared error, whereas a cross-entropy loss metric is more appropriate for classification problems. Regardless, this loss metric tells us how off the model is from the true outcome. 

* The loss metric is then fed back through the neural network through a process called backpropagation. Through this process, each neuron's weights and biases are changed by a little bit in the direction that minimizes the loss function.

* The fitting process called optimization, and one algorithm generally used to optimize the fit of the data is stochastic gradient descent. 

* An important parameter associated with the optimization step is the learning rate, which controls the rate at which the weights and biases are changed every time in backpropagation. If a model is learning slowly, it may be a good idea to increase the learning rate. However, if we increase it by too much we might cause the model to output wildly different outputs as it learns. This is called non-convergence, and may also cause the neural net to become less efficient or accurate. 

* A neural network is actually trained on the training data not all at once but in chunks; each chunk is called a mini-batch. Once all the forward and back-propagation is complete and the weights and biases of each neuron are updated, the process begins again with a new mini-batch. Once the training data is all used up, another cycle is started. Theoretically, these cycles should continue until the loss function seems to converge to a minimum; practically, we need to set one before the model is run and observe the loss function afterwards. Each cycle is called an epoch. The number of epochs it takes for the loss metric to converge is a measure of the model's efficiency. 

* The learning rate, activation function, epochs of training, and size of mini-batches are collectively called hyperparameters. These hyperparameters should be tuned through informed trial and error to arrive at the best model. 

Stop for questions before going on to the next activity. 