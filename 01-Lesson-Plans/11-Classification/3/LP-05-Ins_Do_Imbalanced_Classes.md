## 5. Instructor Do: Imbalanced Data

Continue in the slides to the imbalanced data slide.

* Imbalanced data describes cases when one or more classes in the data is much more or less frequent than the other class(es). We will be working with binary (two class) classifcation tasks for simplicity, but imbalanced data is a problem in multi-class tasks as well.

* Imbalanced data is problematic for two main reasons. First, it can cause your model to be biased towards the majority class. Basically, the model will be better at predicting the majority class compared to the minority class because model fitting algorithms are designed to minimize the number of total incorrect classifications. For a concrete example, imagine a data set with two classes A and B. There are 100 instances of A in the training sample, and only 10 instances of B. Imagine a naive model that always picks A. If the data were perfectly balanced, this would result in an accuracy of 50%. However, because this data is imbalanced, this naive model would achieve an accuracy of 100/110, or over 90%! If the two classes are not easily separable, the resulting model will lean towards the naive model and be much better at predicting the majority class than the minority class. 

* As you have seen in the previous activity, imbalanced classes like cancer/non-cancer can cause metrics like accuracy to be unreliable as a proxy for the "goodness" of a model. The example above illustrates why. 

* The rest of the class will go over strategies to deal with imbalanced classes. We will work mostly with over and under-sampling methods, in which we sample the minority class with greater than random chance or sample the majority class with less than random chance. We will also explain why ensemble methods may be more suitable for imbalanced data than other classification methods, and introduce a classification report specifically created for imbalanced data. 