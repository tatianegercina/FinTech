### 1. Instructor Do: Random Forest Trading (15 min)

In this activity, students will learn how to use a set of trading signal features generated from raw BTC/USD data to train a random forest machine learning model that will autonomously make predictions and corresponding trades.

**File:** [random_forest_trading.ipynb](Activities/01-Ins_Random_Forest_Trading/Solved/random_forest_trading.ipynb)

Open the slideshow and quickly discuss the following:

* What is a Random Forest model?

  **Answer:** A Random Forest model is among one of the best supervised algorithms in terms of its ability to predict outcomes. The Random Forest model utilizes a combination of multiple decision tree models to "average away" or minimize the impact of any single decision tree with high variance, thereby creating a more reliable predicted result derived from the strongest features. For example, in regards to portfolio optimization, combining the concept of sharp ratios and portfolio diversification tends to create a portfolio of maximum expected return with minimal variance or risk due to the tendency for non-correlated stock to "cancel" out each other's variances.

* Why is it called a Random Forest?

  **Answer:** A Random Forest model is a combination of many decision tree models with each decision tree or "tree" randomly selecting a subset of the observations and features to train itself on. The result is a final prediction that is an average across this "forest" of random tress.

* How does a Random Forest model work?

  **Answer:** Specifically, a random forest is a collection of bagged decision tree models that split on a subset of features (rather than all the features in the model) at each split. In other words, each decision tree model gets a different view (different data, different variables) and what is left as the final prediction is an average result of all the decision tree models in which the mistakes of each individual tree is "averaged away" with only the strongest features remaining.

Then, open the solution file and discuss the following:

* As always, before proceeding to generating the multiple features or trading signals of the Random Forest model, the following will first have to be done: importing the relevant libraries, reading in the data as a Pandas DataFrame, and preparing/cleaning the data.

  ![data-prep-1](Images/data-prep-1.png)

  ![data-prep-2](Images/data-prep-2.png)

  ![data-prep-3](Images/data-prep-3.png)

  ![data-prep-4](Images/data-prep-4.png)
