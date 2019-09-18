### 15. Instructor Do: Support Vector Machines (10 mins)

Students receive a demonstration and lecture on how to use support vector machine algorithm. The goal of this activity is to illustrate to students the different approaches that can be taken to come up with the same classification engine.

**Files:** [support_vector_machine.ipynb](Activities/06-Ins_SVM/Solved/support_vector_machine.ipynb)

Open the slideshow to the SVM section, and highlight the following:

* In the previous activity, a Logistic Regression model was used to classify loan eligibility. Logistic Regression is just one model that can be used to classify data points. Another algorithm that can be used is **support vector machines (SVM)**.

* Define **SVM** as a **supervised learning** model that can be used for classification and regression analysis. Explain that SVM separates classes of data points into multidimensional space. The space is segmented by a line or plane that groups data points into their respective classes.

  ![svm.png](Images/svm.png)

* Unlike **Logistic Regression**, **SVM** can employ both a linear and non-linear approach when predicting outcomes. **SVM** focuses on dimensionality.

  * The number of dimensions needed for the model is dependent on the number of features in the data set. Each feature is a dimension.

* Explain that the **SVM** learning algorithm operates by plotting data points with dimensions. Once all data points are plotted, a **hyperplane** is created.

* Define a **hyperplane** as a dimensional vector used to separate data points into different classes.

  * A **hyperplane** is a line that delineates data points into their corresponding classes. All items to the left of the line belong to class A. Items to the right belong to class B.

  * The goal with hyperplanes is to get the margin of the **hyperplane** equidistance to the data points for all classes. This distance is considered the **margin of separation**.

    * Explain to students that the margin is considered optimal when the distance from the hyperplane and the support vectors are equidistant.

      ![margin_of_separation.png](Images/margin_of_separation.png)

  * The data closest to/within the margin of the hyperplane are called **support vectors**, and they are used to define boundaries of the hyperplane.

    * These points are sometime the most difficult to classify because they live closest to the margin and could belong to either class.

    ![support_vectors.png](Images/support_vectors.png)

Educate students on the different orientations for **hyperplanes**. Provide understanding on how the orientation and position of the hyperplane is decided.

![hyperplane_orientation.png](Images/hyperplane_orientation.png])

* Hyperplanes can be 2D, clearly delineating classes with non-overlapping data points or outliers.

* Hyperplane also supports what's considered **0 tolerance with perfect partition**, which is a non-linear hyperplane that will position and orient the hyperplane to correctly classify overlapping or outlying data points.

  * This hyperplane could be a curved line or a circle, depending on the data points and their proximity to one another.

  * In order to establish **0 tolerance with perfect partition**, the SVM model may introduce a new `z-axis` dimension for non-linear hyperplanes.

* The `kernel` parameter is used to identify the orientation of the **hyperplane**. **Kernelling** and how to use the `kernel` parameter will be addressed later in the demo.

Transition into the live coding exercise by opening the starter file and demonstrating to students how to create a **SVM** model with **sklearn**.

* In order to create a SVM model, the **sklearn** `svm.SVC` module must be imported.

    ```python
    from sklearn.svm import SVC
    ```

* Like any other supervised learning model, a data set is needed to learn from. The `make_blobs` function can be used to create the data set that the model will use to train/learn from.

    ```python
    from sklearn.datasets.samples_generator import make_blobs
    X, y = make_blobs(n_samples=40, centers=2, random_state=42, cluster_std=1.25)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="bwr");
    plt.show()
    ```

  ![plot_classification.png](Images/plot_classification.png)

Indicate to students that the `svm.svc` module is used to create a **SVM** model.

* The SVC constructor supports a number of arguments, with the `kernel` argument being the most important. Provide students with a brief overview of the `kernel` argument and what **kerneling** is.

* The `kernel` argument is used to express the dimensionality of the model. It's basically the degree of dimensionality needed to separate the data into classes.

* Communicate to students that a **linear** `kernel` value should be used for data sets with two classes. This will create a **hyperplane** that is a line. Non-linear data will result in a hyperplane that is an actual plane.

* The `kernel` argument accepts a number of values. These are listed and explained below. Advise students to consult the documentation to get additional detail on these parameter values.

  * rbf - creates a non-linear hyperplane

  * linear - creates a linear, 2D hyperplane

  * poly - creates a non-linear hyperplane

    ```python
    model = SVC(kernel='linear')
    ```

* Once the model has been created, it can be trained using the blob data created in the previous step. The model is trained using the **sklearn** `fit` function.

    ```python
    model.fit(X, y)
    ```

    ![svm_model.png](Images/svm_model.png)

* A common practice is to identify the decision boundary/hyperplane for the already identified data points prior to making predictions. This provides a visual representation of the already existing classes and their margin of separation.

  * The decision boundary is dictated by the min and max values within the provided data set (feature columns only). These values are known as **support vectors** and can be plotted to render a visual of the classes.

    ```python
    # Plot the decision boundaries
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    print(x_min, x_max, y_min, x_max)
    ```

    ![min_max_boundaries.png](Images/min_max_boundaries.png)

* The NumPy `mesh_grid` function can be used to store the coordinates in a vector. These will be referenced later when running the `decision_function` to identify the boundaries of the hyperplane.

    ```python
    # Create mesh grid
    XX, YY = np.mgrid[x_min:x_max, y_min:y_max]
    ```

    ![mesh_grid.png](Images/mesh_grid.png)

* The mesh grid data can then be scored by the classifier using the `decision_function` function. The `decision_function` operates similar to predict; however, instead of providing the classification outcome (i.e yes or no), the `decision_function` returns the classifier score for the data point (i.e. -1.38402 and 1.323), which can be used to figure out which side of the hyperplane the data point will fall.

    ```python
    # Use the decision_function function to identify sides of the hyperplane
    Z = model.decision_function(np.c_[XX.ravel(), YY.ravel()])
    print(Z)

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    # plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k', s=100)
    plt.show()
    ```

    ![plotting_hyperplane.png](Images/plotting_hyperplane.png)

* Emphasize to students that data will not always be equidistant with a wide margin. Explain that **support vectors** can fall within the margin of the hyperplane. These values should be considered errors and the classification should not be relied on.

  * Remind students that margins should always be maximized

  * Indicate that when support vectors are too close to the margin, there's a 50% change the classification can go either this. This is why these results are not reliable.

  ![overlap.png](Images/overlap.png)

  ![classification_errors.png](Images/classification_errors.png)

* Now that the pre-existing data has been visualized into the corresponding classes, separated by a hyperplane, the model can be used to predict the classification of new data points. Just like with the Logistic Regression model, the `predict` function can be used to make label predictions.

    ```python
    # Create new data set to predict
    X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=.95)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="bwr");
    plt.show()

    # Fit to the training data and predict
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    ```

    ![predictions.png](Images/predictions.png)

* The predictions can then be evaluated using **sklearn's** classification report. As made clear by the precision, recall, and f-1 metrics, the model performed well.

  * Remind students that the SVM model provides a higher accuracy than some of the other models. The accuracy of the model is evidenced in the performance metrics.

    ```python
    # Calculate classification report
    from sklearn.metrics import classification_report
    print(classification_report(y_test, predictions,
                                target_names=["blue", "red"]))
    ```

    ![model_performance.png](Images/model_performance.png)

Explain to students why SVM might be used over a Logistic Regression model.

* SVM is more beneficial than Logistic Regression because the model supports classification of outliers and overlapping data points

* SVM also provides higher accuracy with less computation power.

Instruct students to review the below documentation/articles to get additional detail on how to use the SVC constructor and its various parameters. Remember to slack the resources out.

* [In-depth Parameter Tuning for SVC](https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769)

If time remains, remind students that most of the code they saw today is boilerplate and can be reused with little to no changes. From a high level, the steps to implement an SVM model include:

1. Create the model with appropriate `kernel` parameters

2. Fit the model

3. Extract min and max decision boundaries and store in a mesh grid

4. Execute the `decision_function` to get classifier scores for pre-exiting data points

5. Run the `predict` function to classify new data points

Ask for any questions before moving forward.