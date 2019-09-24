### 10. Students Do: Smarter Learning (15 min)

In this activity, students will use TensorFlow Playground to create neural nets to optimize results for a classifcation and regression problem. 

**Instructions:**

* [README.md](Activities/03-Stu_Smarter_Learning/README.md)

**Files:**

---


### 11. Instructor Review: Smarter Learning (10 min)

Open the Playground webpage. First, select the "swirl" dataset and ask students how they manipulated the input features and hidden layer neurons to minimize the loss statistic. Which combinations seemed to work well, and which did not?

* We did not see any improvements in changing hyperparameters over the original configuration for "swirl." Although the learning was relatively slow, increasing the learning rate seem to have negative consequences for the loss metric - the model does not seem to converge. Moreover, changing the activation function to ReLU helped us attain a similar loss function with similar epochs of training. 

Now select the "swirl" dataset and ask students how they manipulated the input features and hidden layer neurons to minimize the loss statistic. Which combinations seemed to work well, and which did not?

![play_4.png](Images/play_1.png)

* Both sigmoid and ReLU activation functions performed well on the regression problem. We chose the first two features; adding more did not seem to help the accuracy of the model and seemed to make it less efficient. Increasing the learning rate seemed to make the model converge faster. 