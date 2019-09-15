### 15. Instructor Do: Support Vector Machines (10 mins)

Students receive a demonstration and lecture on how to use support vector machines to create the same loan approver seen in the previous activity. However, instead of using a Logistic Regression approach, the instructor will show students how to classify loan eligibility using the support vector machines algorithm.

The goal of this activity is to illustrate to students the different approaches that can be taken to come up with the same classification engine. Another objective is to highlight the strengths and weaknesses of each algorithm so students can learn how to identify the best approach based off of use case.

**Files:** [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Open the starter file, and highlight the following while doing a live coding session:

* In the previous activity, a logistic regression model was used to classify loan eligibility. This is just one way of implementing the loan approver model. Another algorithm that can be used is support vector machines (SVM).

* Similar to the **Logistic Regression** algorithm, the **SVM** algorithm can be used for classification and regression analysis.

* Unlike **Logistic Regression**, **SVM** takes a non-linear approach when predicting classes and outcomes. Instead, **SVM** focuses on dimensionality.

  * The number of dimensions needed for the model is dependent on the number of features in the data set. Each feature is a dimension.

* Explain that the **SVM** learning algorithm operates by plotting data points with dimensions. Once all data points are plotted, a **hyperplane** is created.

* Define a **hyperplane** as a dimensional vector used to separate data points into different classes.

  * A hyperplane is a line that delineates data points into their corresponding classes. All items to the left of the line belong to class A. Items to the right belong to class B.

  * The goal with hyperplanes is to get the margin of the **hyperplane** equidistance to the data points for all classes.

Provide understanding on how the orientation and position of the hyperplane is decided.

*

*

*

Demonstrate to students how to create a SVM model using sklearn.

* In order to create a SVM model, the **sklearn** `svm.SVC` module must be imported.

    ```python
    from sklearn.svm import SVC
    ```

* Once SVC has been imported, it can be used to create an SVM model.

    ```python
    model = SVC(kernel='linear')
    ```

* The SVC constructor supports a number of arguments, with the `kernel` argument being the most important. The `kernel` argument is used to express the dimnesionality of the model. It's basically the degree of the polynomial used to find the hyperplane to split the data. The polynomial used will be specific to the number of dimensions/features in the model.

  * The kernel argument accepts a number of values. These are listed and explained below:

    * rbf - creates a non-linear hyperplane

    * linear - creates a linear, 2D hyperplane

    * poly - creates a non-linear hyperlane

Explain to students why SVM might be used over a Logistic Regression model.
