# Student Do: Preventing credit card defaults with neural networks

In this activity, you will train a neural network model to predict whether a credit card holder will default in the next month.

The dataset provided contains `30,000` anonymous records of credit default status with `23` features columns and one binary target column entitled DEFAULT, where `1` represents a defaulted credit card.

The `23` features include demographic info (age, gender, marital status, etc.), credit limit, past payment details, and other relevant information.

You are tasked to create a neural network model to predict if a credit card holder will default.

## Instructions

1. Load the data in a Pandas DataFrame.

2. Define the features set `X` by including all the columns of the DataFrame except the `DEFAULT` column.

3. Create the target vector `y` by assigning the values of the `DEFAULT` column of the DataFrame.

4. Create the training and testing sets using the `train_test_split` function from `sklearn`.

5. Scale the features data using the `StandardScaler` from `sklearn`.

6. Create a neural network model with `23` inputs, one hidden layer with `69` units, and an output layer with a single output. Use the `relu` activation function for the first layer and `sigmoid` for the second layer.

7. Compile the neural network model using the `binary_crossentropy` loss function, the `adam` optimizer, and `accuracy` as an additional metric.

8. Fit the model with `100` epochs.

9. Plot the loss function and accuracy.

10. Evaluate the model using testing data and the `evaluate` method.

## Challenge

For this challenge section, you have to figure out how the model you created could be modified to improve the accuracy.

1. Review the Keras documentation about activation functions, and decide if there is anything that could be used instead of `sigmoid`.

2. Change any other parameter that you believe could improve the model's accuracy.

3. Evaluate the model's accuracy and loss and write down your conclusions.

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
