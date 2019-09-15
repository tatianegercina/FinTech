### 15. Instructor Do: Support Vector Machines (10 mins)

Students receive a demonstration and lecture on how to use support vector machines to create the same loan approver seen in the previous activity. However, instead of using a Logistic Regression approach, the instructor will show students how to classify loan eligibility using the support vector machines algorithm.

The goal of this activity is to illustrate to students the different approaches that can be taken to come up with the same classification engine. Another objective is to highlight the strengths and weaknesses of each algorithm so students can learn how to identify the best approach based off of use case.

**Files:** [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Open the starter file, and highlight the following during a live coding session:

* In the previous activity, a logistic regression model was used to classify loan eligibility. This is just one way of implementing the loan approver model. Another algorithm that can be used is support vector machines (SVM).

* Similar to the **Logistic Regression** algorithm, the **SVM** supervised learning algorithm can be used for classification and regression analysis.

* Unlike **Logistic Regression**, **SVM** takes a non-linear approach when predicting classes and outcomes. Instead, **SVM** focuses on dimensionality.

  * The number of dimensions needed for the model is dependent on the number of features in the data set. Each feature is a dimension.

* Explain that the **SVM** learning algorithm operates by plotting data points with dimensions. Once all data points are plotted, a **hyperplane** is created.

* Define a **hyperplane** as a dimensional vector used to separate data points into different classes.

  * A **hyperplane** is a line that delineates data points into their corresponding classes. All items to the left of the line belong to class A. Items to the right belong to class B.

  * The goal with hyperplanes is to get the margin of the **hyperplane** equidistance to the data points for all classes. This distance is considered the **margin of separation**. The data within the margin/closest to the hyperplane are called **support vectors**, and they are used to define the hyperplane.

    * Explain to students that the margin is considered optimal when the distance from the hyperplane and the support vectors are equidistant.

    * These points are sometime the most difficult to classify because they live closest to the margin and could belong to either class.

Provide understanding on how the orientation and position of the hyperplane is decided.

* Hyperplanes can be 2D, clearly delineating classes with non-overlapping data points or outliers.

  * Hyperplane also supports what's considered **0 tolerance with perfect partition**, which is a non-linear hyperplane that will position and orient the hyperplane to correctly classify overlapping or outlying data points.

    * This hyperplane could be a curved line or a circle, depending on the data points and their proximity to one another

    * In order to establish **0 tolerance with perfect partition**, the SVM model may introduce a new `z-axis` dimension for non-linear hyperplanes.

*

*

Demonstrate to students how to create a SVM model using sklearn.

* In order to create a SVM model, the **sklearn** `svm.SVC` module must be imported.

    ```python
    from sklearn.svm import SVC
    ```

* Like all other supervised learning models, the SVM model requires training and test data for fitting. The **sklearn** `model_selection.train_test_split` function can be used to split data sets into training and testing subsets.

    ```python
    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    ```

The SVC constructor supports a number of arguments, with the `kernel` argument being the most important. Provide students with a brief overview of the `kernel` argument and what **kerneling** is.

* The `kernel` argument is used to express the dimensionality of the model. It's basically the degree of dimensionality needed to separate the data into classes.

* Communicate to students that a **linear** `kernel` value should be used for data sets with two classes. This will create a **hyperplane** that is a line. Non-linear data will result in a hyperplane that is an actual plane.

* The `kernel` argument accepts a number of values. These are listed and explained below. Advise students to consult the documentation to get additional detail on these parameter values.

  * rbf - creates a non-linear hyperplane

  * linear - creates a linear, 2D hyperplane

  * poly - creates a non-linear hyperplane

    ```python
    model = SVC(kernel='linear')
    ```

* The model can then be fit using the `sklearn.fit` function. The SVM model is trained just like the **Logistic Regression** model. After the model is fit, the model can be used to make classification predictions using the `predict` function.

    ```python
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    ```

Explain to students why SVM might be used over a Logistic Regression model.

* SVM is more beneficial than Logistic Regression because the model supports classification of outliers and overlapping data points

* SVM also provides higher accuracy with less computation power.

Instruct students to review the below documentation/articles to get additional detail on how to use the SVC constructor and its various parameters. Remember to slack the resources out.

  * [In-depth Parameter Tuning for SVC](https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769)
