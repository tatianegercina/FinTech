### 7. Students Do: Playing With Neurons (15 min)

In this activity, students will use TensorFlow Playground to create neural nets to classify the remaining two sets of data on the right, "exclusive or" and "spiral."

### Files

[README.md](Activities/02-Stu_Playing_With_Neurons/README.md)

---

### 8. Instructor Do: Review Playing With Neurons (10 min)

Open the Playground webpage. First, select the "exclusive or" dataset and ask students how they manipulated the input features and hidden layer neurons to minimize the loss statistic. Which combinations seemed to work well, and which did not?

* There are many potential solutions to this problem, but we'll go over two. We can try to classify the data using the first two input features, which are both linear features of the data. This results in the classification below, which shows a decent fit of the data. 

![play_1.png](Images/play_1.png)

* Intuitively, this should make sense. If the data is divided into four square blocks, then some linear approximation should be able to separate out the boundaries of the data. 

* We can add additional features, but they don't seem to decrease either training time nor the loss function to any degree. Adding features also increases our chances of overfitting the data. For example, notice that adding the squared features will tend to make the classification boundaries look circular. As a review, overfitting occurs when the model we create too closely approximates the training data (instead of some general pattern) and fails to perform as well on unseen test data. In the results above, the different between test loss and training loss gives us an idea of whether the model might be overfitting (large divergences would hint at this).

* There is an even simpler solution: the feature  x<sub>1</sub>x<sub>2</sub>, which is simply the product of the two linear features. The resulting classification is below:

![play_2.png](Images/play_2.png)

* Notice how the loss function declines to the same level as above much more quickly. The model is much more easily fit, even using fewer neurons in the hidden layer.

Ask students why they think this feature seems to perform better.

* The performance of this model is due to the fact that the data, exclusive or, is defined by the same function x<sub>1</sub>x<sub>2</sub>. This illustrates that when we know the functional form that generated the data, it's much easier to fit a good model. Of course, this won't be the case in the vast majority of problems, so we have to depend on much more tinkering with features and architecture. 

* The second data set, swirl, is much more challenging to model. Through trial and error, we reached decent results using the first five features and eight neurons in the hidden layer:

![play_3.png](Images/play_3.png)

Ask students for some alternative solutions before moving on the the next activity. 