### 3. Instructor Do: Neurons (10 mins)

Use the "Neurons" section of the slides to go over the following points:

* Neurons are the units of a neural net, and each neuron sends signals to others. Collectively, they can learn very complex functions. 

* A single neuron is very similar to a logistic regression model. Like a logistic regression model, a neuron tries to estimate coefficients (called weights) and an intercept (called a bias) to best fit training data, which includes inputs and outputs. 

Ask volunteers to answer the following questions, which should be a review from logistic regression.

* What types of outcomes do logistic regressions predict?

**Answer:** Logistic regressions predict discrete (categorical) variables, in many cases binary (1 or 0) variables. 

* What are inputs and outputs of logistic regressions?

**Answer** Logistic regressions can have multiple explanatory variables as inputs, and output a number from 0 to 1 that can be interpreted as the probability of that variable being either 0 or 1. The higher the probability, the more likely the probability of 1. 

* How do logistic regressions learn their coefficients and intercepts?

**Answer** Coefficients and intercepts, the parameters of the regression, are learned by minimizing a "loss function" which tells us how far away predicted results are from actual results. 

Tell students that we won't be going into the mathematical definitions of how logistic regressions/neurons work, but it's important to understand intuitively what's going on when a neuron is being trained in order to adjust some of the hyperparameters of a neural net. 

* To construct a neural net, neurons are arranged so that the outputs of some neurons feed as inputs to others, so that functions can be stacked on top of one another to become more complex functions. 

Check if students have questions before continuing to the next section. 