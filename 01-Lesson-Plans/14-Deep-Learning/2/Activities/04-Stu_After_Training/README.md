# After Training

In this activity, you will create a deep learning model from the music geographies data, save it, and load it to evaluate its performance on unseen data.

## Instructions

1. Split the data into training and test sets using the `train_test_split` method from `sklearn`.

2. Using the training set, construct a neural net model to predict the geographical origins of music features (you can use the same model that you constructed in the _Sound of Music_ Activity).

3. Save the model and its weights.

4. Load the model and its weights, and use this loaded model to predict points for the test data and print the mean squared error metric for the predicted points vs. the actual points.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
