# Sound of Music

In this activity, you will use a deep learning model to predict the geographical origins of a musical composition.

## The Dataset

The dataset contains `68` encoded features of music composition (columns from `0` to `67`) from a music streaming service. The last two columns of the dataset (columns `68` and `69`) are the geographical coordinates where the song was played.

## Instructions

1. Create a shallow (`1` hidden layer) and deep neural network (with two layers) to predict the geographical coordinates of the compositions represented in the data. Decide on your own how many neurons you will use on each hidden layer.

2. Fit each model with at least `800` epochs, and setting `validation_split=0.3`.

3. Compare the loss metrics for the two models.

4. Compare train and test metrics for both models, and look for signs of overfitting.

## Hint

* Note that that there needs to be two regression outputs. Your model structure should reflect this.

* When fitting the model, you can set the parameter `verbose=0` in the `fit()` method to mute the printing of each epoch's results.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
