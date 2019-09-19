## 11.1 Lesson Plan: Classical Classification

### Overview

In the last unit, students learned how to use advanced statistical models and algorithms in order to predict and forecast outcomes using time series data. Students used statistical approaches; such as linear regression, **Hodrick-Prescott filter**, and **GARCH** and **EGARCH** model; to forecast investment returns, volatility, and out-of-sample predictions.

In unit 11, students will dive deeper into statistics and machine learning by working with **classification** algorithms in order to promote and enable supervised machined learning. **Classification** is the act of discovering whether or not a particular feature or element belongs to a given feature class; **classification** derives categorical conclusions based off of classified/modeled data. By the end of this unit, students will be competent in the execution and evaluation of **classification** models (i.e logistic regression and decision trees) for drawing categorical conclusions and outcomes.

Today's class will introduce students to **classification** models by explaining what classification is and delineating the various classification models/approaches. Then, students will be taught how to use Scikit-learn to train models and make them more efficient and effective in determining probability/outcome predictions.

Before students leave at the end of the class, encourage them to continue independently researching and learning more about the various ways to implement classification models, especially some of the ones not demonstrated in class (i.e. neural networks).

* [Ten Applications of AI to FinTech](https://towardsdatascience.com/ten-applications-of-ai-to-fintech-22d626c2fdac)

* [Types of Classification Algorithms](https://medium.com/@Mandysidana/machine-learning-types-of-classification-9497bd4f2e14)

* [FICO: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

### Class Objectives

By the end of class, students will be able to:

* Define classification in the context of machine learning.

* Model and fit several classification models (Logistic Regression and SVM) using Scikit-Learn.

* Evaluate classification algorithms using a confusion matrix and classification report.

* Convert categorical data to input vectors.

### Instructor Notes

* Today's class will be a great deal of hands on work training and evaluating classification models. Because the content will be heavy in statistics and machine learning, it's important that you remind students of value and application of these skills/concepts to **FinTech**. Whenever appropriate, remind students that **classification** models enables financial companies to make faster and smarter data driven decisions and outcomes (i.e. credit risk and worthiness, money laundering and fraud identification, longevity and return for a particular investment, and loan recommendations).

* The world of **classification** is a large one. All forms and concepts of classification cannot be covered in one class. Ensure to pace the class and be cognizant of how long it takes to explain concepts. The key is to stay rooted in real world and practical examples of how classification can be used. Avoid getting bogged down in the statistical and mathematical detail for the algorithms. Focus should be placed on

  * What the algorithm/model is

  * What the algorithm/model does and FinTech use case

  * How to train/enhance the algorithm/model

  * How to test algorithms/models and correctly handle false negatives and positives

* This week's activities will use tools such as **imbalance-learn**, **scikit-learn**, and the **Lending Club**.

  * **Imbalance-learn** and **scikit-learn** will need to be added to everyone's Python environments. Modules will need to be installed. Students can consult the [classification ecosystem install guide]() for steps on how to verify both packages have been installed correctly.

  * **Lending club** will be used as a data source for this unit. Accounts will need to be created in order for data to be accessed.

  * Slack out the following links to students to use as resources. There will be no time dedicated for in-class installation.

    * [Imbalance-Learn](https://imbalanced-learn.readthedocs.io/en/stable/)

    * [Scikit-Learn](https://scikit-learn.org/stable/)

* Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. You might find that some students need additional assistance with the statistical concepts, and other students might need help with the application of machine learning models.

  * Encourage students to work with partners for all assignments in order to promote collaborative information seeking.

  * Remind students that additional research and practice will be required outside of class in order to reinforce and build competence in learning and evaluating trained models.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome (10 min)

The instructor starts class with an introduction to **classification** and its use cases within FinTech. Students will receive the who, what, when, why, and how of FinTech **classification**.

Open the slideshow, and begin the class by welcoming students back to the second week of machine learning!

* Explain to students that Unit 11 kicks off the second week of machine learning and advanced analytics. Highlight that this unit will focus on using machine learning algorithms and pipelines to draw categorical conclusions and predictions about probable financial outcomes.

* Briefly explain what **classification** is. Indicate that **classification** is used to draw categorical conclusions about data. Instead of forecasting quantitative numbers, **classification** uses a binary (**true-positive**/**true-negative**) approach to predict categorical membership (i.e. will the outcome be of type A or type B).

  * Communicate that **classification** models can be used to identify a loan applicant as credit worthy or a credit risk. Tell students that they will be learning how to perform classification using, all of which will be explained in more detail in upcoming activities.

    * Logistic/Linear Regression

    * Support Vector Machines

* Highlight to students that **classification** models have drastically improved financial efforts to properly classify applicants, predict market decline, and classify fraudulent transaction or suspicious activity.

  * Most large financial institutions are using some form of machine learning to monitor and predict fraudulent activities. This is how banks know when to flag and decline transactions due to suspicion of fraud.

    * Ask students if they've ever received a call from their bank because a transaction was flagged as fraudulent. Explain that the call was triggered by a probability prediction identifying the transaction as fraudulent.

    * For example, FICO credit scoring currently uses a **classification** model for their cognitive fraud analytics platform. Classification engines have allowed the financial industry to become more proactive rather than reactive. Outcomes can be predicted with probable surety, which allows for more effective and efficient mitigation. Slack out the below link as an article of interest for students to review outside of class.

      * [FICO Falcon: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

* Indicate to students their mission for the remainder of this week is to build and train robust classification models in order to automate predictive analytics.

If time remains, ask students emotionally guided questions to get a feel for their current emotional state and give them a space to address any points of excitement, interests, and/or concerns.

* **Machine learning** can be used to automate financial pipelines, forecast time series data and market volatility, predict fraud, analyze sentiment and parse documents, and automate day trading and make investment recommendations. But what exactly is **machine learning**?

  * **Answer** Machine learning is an approach to programming that leverages libraries that provide statistical algorithms and libraries. The machine learning community has developed tried and tested statistical libraries (like **scikit-learn** and **imbalanced-learn**) that offer statistical functions for algorithmic and statistical modeling.

* Last week, you used time series analysis techniques to forecast market returns and volatility. This week we will be exploring **classification** and predicting categorical outcomes. What are you excited about to learn next?

  * **Answer** How to use a **classification** model to predict fraudulent transactions

  * **Answer** How to use a **classification** model to identify best type of line of credit for a consumer

* Do you have any concerns or questions about the content already covered?

  * **Answer** Concerned about not having any background knowledge or experience in statistics

* Underscore to students that the journey into the world of **classification** models and algorithms is both challenging and rewarding.

  * Remind students that everyone in the room will be on the journey together and that resources will be provided to ensure every student has the materials needed to competently train, execute, model, and test classification algorithms.

Ask if there are any questions before moving forward.

- - -

### 2. Instructor Do: Demo Homework (10 mins)

Students will receive a brief demonstration of the Unit 11 homework. The first half of this activity should be dedicated to giving a 5 minute overview. The second half should be to answer one or two questions.

**Homework Instructions:** [README.md](../../../02-Homework/11-Machine-Learning/Instructions/README.md)

Open the homework instructions, and provide a brief dry walk through of the instructions.

* Reveal that this week's homework focuses on creating a classification model focused on predicting and categorizing credit risk.

* Multiple models will be used for this assignment (i.e linear regression and decision trees). Explain to students that these models will be made available with the `Scikit-Learn` package, which was also used in Unit 10.

* Underscore to students that the goal behind the assignment is two fold:

  * Create a classification model that will categorize credit risk

  * Compare and contrast the various machine learning models that can be used to classify credit risk (i.e. resampling vs. ensemble learning). Each model used in the homework can essentially be used to come up with the same prediction: the goal is to identify which model is more accurate and precise.

* Explain that data for this activity will be from the **Lending Club**, a service that allows users to participate in peer-to-peer lending. **Lending club** has a great wealth of loan performance data that can be used to train machine learning algorithms for **classification**. The homework will include using data points such as loan amount, interest rate, loan balance, etc to make predictions about credit risk.

* Note to students that this homework will use the `imbalanced-learn` and `scikit-learn` tools. These tools need to be properly installed and functional.

End the activity by opening the floor for students to ask questions about the homework. Dedicate the next 5 minutes to answering these questions.

- - -

### 1. Instructor Do: Intro to Classification (0:10)

By the end of this activity, students will be able to summarize what classification is within the machine learning space, as well as name one or two common classification algorithms.

Kick off the activity by asking for a student to try summarizing what **classification** is. If there are no volunteers, ask a specific student.

* **Answer** **Classification** is the prediction of discrete outcomes. Outcomes are identified as labels, which serve to categorize bi-class and multi-class features.

* Promote student confidence and engagement by thanking the student for volunteering the summary and emphasizing the parts of the answer that are correct. Use the student's answer as a transition into formal lecture.

Navigate to the 11.1 slideshow, and walk through the content on the **Intro to Classification** slide:

* Provide students with the official definition of **classification**, as described by the Oxford English dictionary:

  > The action or process of classifying something according to shared qualities or characteristics

* Explain to students that in the scope of machine learning, the act of **classification** takes place through a process of supervised learning, where an algorithm is used that enables an application to analyze historical data sets and learn from the data in order to predict categorical membership and future outcomes.

  * Remind students that classification is used to forecast and predict financial outcomes, automate underwriting and insurance premiums, detect and categorize health issues/overall health.

* Underscore to students that there are a number of libraries available that make **classification** as easy as data cleaning. All that is needed is a series of calls to several functions. Assure students that training and running a **classification** model is as simple as:

  1. Prepping and wrangling their data sets (used to train and fit models)

  2. Using machine learning libraries and functions that are already available

* Highlight that there are multiple approaches to **classification**. These include **Logistic Regression** and **Support Vector Machines**, all of which will be explained in further detail throughout the day.

If time remains, let students know there's time for one question.

* If there's a question, answer it, and then move onto the next activity. Assure students that the upcoming activities will shed more light on **classification** and that there will be additional time for questions during review sessions.

- - -

### 2. Instructor Do: Making Predictions with Logistic Regression (10 mins)

Having been introduced to classification, students will now receive a demonstration of how to use logistic regression to make linear predictions for categorical outcomes. This demo will contain two parts: a brief explanation of preprocessing and a more in-depth explanation of model fitting and execution.

**Files:**

[logistic_regression.pptx](Activities/01-Ins_Logistic_Regression/logistic_regression.pptx)

[Ins_Logistic_Regression.ipynb](Activities/01-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb)

Walk through the slideshow and highlight the following points:

* Communicate that Logistic Regression is a statistical method for predicting binary outcomes from data. With linear regression, our linear model may provide a numerical output such as age. With logistic regression, the numerical value for age could be translated to a probability between 0 and 1. This discrete output could then be labeled as "young" vs "old". The same approach can be used to predict the probability of credit worthiness based off of credit score, number of missed payments, number of public records, and credit age.

  ![logistic_1.png](Images/logistic_1.png)
  ![logistic_2.png](Images/logistic_2.png)
  ![logistic_3.png](Images/logistic_3.png)
  ![logistic_4.png](Images/logistic_4.png)

* Emphasize to students that running a logistic regression model involves 4 steps, which can be applied when running any machine learning model:

  1. Preprocess

  2. Train

  3. Validate

  4. Predict

* We can use logistic regression to predict which category or class a new data point should be classified as.

After presenting the slideshow, open the Jupyter notebook and complete a dry walk through of running logistic regression with  Scikit-Learn (sklearn). Quickly run through the next bullet points, emphasizing that classification algorithms require data to be clustered into classes/groups.

* Communicate to students that the only way to run a logistic regression model is to first prepare a dataset to be used for training the model. In order for a logistic regression model to learn on its own, it must be given data that is clustered in classes/groups.

  * For example, two classes can be created that represent credit risk: **low risk** (purple) and **high risk** (yellow). Logistic regression can then be used to classify new data points/applicants.

    ```python
    from sklearn.datasets import make_blobs

    X, y = make_blobs(centers=2, random_state=42)
    ```

    ![make-blobs.png](Images/make-blobs.png)

* Depending on time, further explain that the process of clustering data points into classes/groups is called **centering**.

  * Explain to students that **centering** is a a part of the pre-process step of advanced analytics that helps dictate the number of classes/groups to create. **Centering** improves the performance of logistic regression models by ensuring that all data points share the same starting mean value. Data points with the same starting mean value are clustered together.

  ![make_blobs_fx.png](Images/make_blobs_fx.png)

* The last step of preprocessing is splitting data into **training** and **testing** data sets. The **training** subset will be used to train the model and help it self learn. The testing data set will be used to evaluate and test the accuracy of the algorithm and its predictions.

  * Emphasize to students that the **training** and **testing** data sets can come from a single data set or two different ones. The **sklearn** `model_selection.train_test_split` module can be used to split a single data set into **training** and **testing** subsets. This will create four data sets:

    * X train

    * X test

    * Y train

    * Y test

    ```python
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    ```

Transition into the next part of the demo by explaining to students that once the preprocessing work has been completed, the logistic regression model can be ran. Demonstrate and explain how logistic regression models are trained and executed.

* **Logistic Regression** can be implemented using the sklearn `LogisticRegression` class. This module is a part of the **linear model** package, a package commonly chosen by developers to run linear regression. The object returned from the `LogisticRegression` class will be  a **classifier** object, which is used to train, validate, and make predictions.

  ![logistic_regression_class.png](Images/logistic_regression_class.png)

* Once a Logistic regression model has been created, it can be **trained**/**fitted**. The model can be **trained** by using the `train` function provided by the `LogisticRegression` object. As stated previously, **classification** is a form of **supervised learning**. In order for the algorithm to learn, it must be given data to learn from. This process is fitting/training.

    ```python
    # Train the data
    classifier.fit(X_train, y_train)
    ```

    ![train_model.png](Images/train_model.png)

The next step after training the model is **validating** it. A common approach is the Train/Test Split approach. Walk students through how this approach is used.

* In order to validate a model, it must be scored, which the **sklearn** `score` function can do. The **testing** data sets are passed to the `score` function, and the function evaluates results. Explain to students that the scoring process takes the predictions made using the training data and compares it to the predictions made using the test data. If the predictions are the same and the score is **1.0**, the model is considered accurate.

* It's important to note to students that two things need to be scored: the **training** AND **test** data.

  * When scoring the training data, the accuracy of the model is applied against the training data it was created with. The more data is trained, the higher the accuracy.

  * Scoring of test data consists of applying the model against the test data. The test data is considered new data the model has not seen. If score will reflect the accuracy of the predictions made by the model using the test data.

  * If the training score is more accurate than the testing score, the model is considered overtrained. **Overtraining** the model can result in **overfitting**, where the model learned rules for predictions that apply mostly just for the training data set. The goal is to have the scores as close to each other in accuracy as possible.

    ```python
    # Score the model
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")
    ```

    ![testing_model.png](Images/testing_model.png)

Once the model is proven to be accurate for both the training and test data, the last step is to actually make predictions using an entirely new data set. Explain to students how the **sklearn** package can be used to make **logistic regression** predictions.

* The **sklearn** `predict` function can be used to apply the model against a new data set. The model will predict which class the new data points will fall into (i.e. low credit risk or high credit risk).

    ```python
    # Generate a new data point (the red circle)
    import numpy as np
    new_data = np.array([[-2, 6]])
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.scatter(new_data[0, 0], new_data[0, 1], c="r", marker="o", s=100)

    # Predict the class (purple or yellow) of the new data point
    predictions = classifier.predict(new_data)
    print("Classes are either 0 (purple) or 1 (yellow)")
    print(f"The new point was classified as: {predictions}")
    ```

    ![predict_new_data.png](Images/predict_new_data.png)

If time remains, show students the results of the predictions made using the test data. Students did not see this because the `score` function executes predictions behind the scenes when calculating accuracy.

* When applying the model against the test data, the `score` function automatically calculates predictions behind the scenes. The **sklearn** `predict` function can be used see the actual predictions made from the data points in the test data set.

    ```python
    # Predict outcomes for test data set
    predictions = classifier.predict(X_test)
    pd.DataFrame({"Prediction": predictions, "Actual": y_test})
    ```

    ![predict_test.png](Images/predict_test.png)

Ask students if there are any questions before moving on. This was a heavy activity, so there will most likely be a number of questions. Try and answer one or two questions if timing permits. If not, ask students to save questions for review, and reiterate the following to students:

* When running a logistic regression model, or any model, follow these simple steps:

  1. Preprocess (i.e. centering)

  2. Train

  3. Validate

  4. Predict

Ask if there are any questions, and then move to the next activity.

- - -

### 3. Students Do: Predicting Diabetes (15 mins)

In this activity, students will use the **sklearn** library to execute **logistic regression** models in order to predict whether or not an individual has diabetes. Students will leverage the material covered in the corresponding instructor demo activity to complete this MSMD activity.

**Instructions:**

* [README.md](Activities/02-Stu_Diabetes/README.md)

**Files:**

* [diabetes_lr.ipynb](Activities/02-Stu_Diabetes/Unsolved/diabetes_lr.ipynb)

- - -

### 4. Instructor Do: Predicting Diabetes Activity Review (10 mins)

**Files:**

* [diabetes_lr.ipynb](Activities/02-Stu_Diabetes/Solved/diabetes_lr.ipynb)

Open the solution and complete a dry walk through of the solution . Answer any questions that students have.

* Reiterate to students that in order to run a logistic regression model, a training and testing data set are required. A single data set can be split into these two subsets using the **sklearn** `train_test_split` function. Explain that these two data sets will be used to validate the accuracy of the model.

    ```python
    # Use the train_test_split function to create training and testing data sets
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    ```

* In order to run a logistic regression model, a logistic regression model object is needed. The **sklearn** `LogisticRegression` module is a common module used.

    ```python
    # Use the LogisticRegression module from the sklearn package to create a model
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state=1)
    classifier
    ```

    ![create_lr_model.png](Images/create_lr_model.png)

* Once a model is created, it has to be trained. After training, the model can be scored, and it can then be used to make predictions for new data points.

    ```python
    # Fit the model
    classifier.fit(X_train, y_train)

    # Score the model
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")

    # Make predictions
    predictions = classifier.predict(X_test)
    results = pd.DataFrame({"Prediction": predictions, "Actual": y_test}).reset_index(drop=True)
    results
    ```

    ![running_lr.png](Images/running_lr.png)

If time remains, facilitate a discussion around model evaluation using the following questions. Be mindful of pacing. Also encourage students to ask any of their own questions.

* How well did your model perform?

* How do you know? Did you count the results?

* If you were asked to diagnose a patient, how confident would you be in your model's prediction?

Explain to students that in addition to the accuracy score, there are other metrics that we can use for model evaluation such as precision and recall.

Ask if there are any questions before moving forward.

- - -

### 7. Instructor Do: Evaluating Logistic Regression Predictions (5 min)

In this activity, students and instructor will engage in a facilitated discussion evaluating the results of logistic regression predictions. The focus of this activity will be the evaluation of diabetes predictions.

Open the 11.1 slides, and highlight the following:

* We used a logistic regression model to predict whether or not an individual has diabetes, based off of a set of diagnostic metrics provided as a data set. The logistic regression model was validated using a scoring feature, revealing that the model is somewhat accurate. But can you trust that the prediction is correct?

  * Ask students how sure they are that their models can actually predict diabetes.

    * **Answer** 75 percent sure, as described by the scored accuracy.

  * Ask students if anyone would feel comfortable giving the diagnosis of diabetes based off of the predictions of the model. Why or why not?

    * **Answer** No. The prediction is not 100% accurate. There is room for error, as well as false positives.

  * Asks students if they'd rather have a model that incorrectly flags diabetes for patients that didn't actually have the disease, or would you rather miss predicting the disease in some patients? What is better: the **false positive** or **false negative**?

    * **Answer** Neither option is preferred. Both leave opportunity for inaccuracy.

    * **Answer** A model that incorrectly flags diabetes for patients that don't actually have the disease. Additional tests can be ran to refine the prediction and filter out individuals who do not have diabetes. This way, anyone with hte potential of having it can be given the treatment and attention they need.

* Explain to students that in order to evaluate a model, they must do more than score/measure the model for accuracy. In addition to **accuracy**, a model must be measured for **precision** and **recall**, both of which can be used to eliminate **false positives** and **false negatives**.

Ask if there are any questions before moving on.

- - -

### 8. Instructor Do: Accuracy, Precision, Recall (10 min)

The instructor provides a formal lecture explaining to students what accuracy, precision, and recall is in relation to logistic regression models, as well as how to measure each metric.

**Files**

* [Slides]()

Navigate to the 11.1 slides, and highlight the following:

* Explain to students that **accuracy**, **precision**, and **recall** are especially important for **classification** models, which a **binary decision problem**. **Binary decision problems** have two possible correct answers: **True Positive** and **True Negative**.

  * Inaccurate and imprecise models result in models returning false positives and false negatives.

* When running a classification model, or any statistical model, it is important that the model is evaluated for **accuracy**, **precision**, and **recall**.

* Accuracy is how often the model is correct: the ratio of correctly predicted observations to the total number of observations. As demonstrated previously, the **accuracy** of a model can be evaluated by scoring the model using training and testing data sets. Scoring will reveal how accurate the model. However, it does not communicate how precise it is.

  * Accuracy can be very susceptible to imbalanced classes. In the case of the homework assignment, the number of good loans greatly outweighs the number of at-risk loans. In this case, it can be really easy for the model to only care about the good loans because that has the biggest impact on accuracy. However, we also care about the at-risk loans, so we need a metric that can help us evaluate each class prediction.

  * **Calculation:** (TP + TN) / (TP + TN + FP + FN)

* **Precision** is the ratio of correctly predicted positive observations to the total predicted positive observations (i.e. of all the samples classified as having diabetes or a credit risk, how many actually have diabetes/are a credit risk).

  * Another example of **precision** is of all of the individuals that were classified by the model as being a credit risk, how many actually were a credit risk? The question at hand: did we classify comprehensively and correctly?

  * A similar example would be of all the loans predicted to be in good standing, how many actually are? Of the loans predicted to be at-risk, are they actually at-risk?

  * High precision relates to a low **false positive** rate.

  * **Calculation:** TP / (TP + FP)

* **Recall** is the ratio of correctly predicted positive observations to all predicted observations for that class (i.e. of all of the actual diabetes/credit risk samples, how many were correctly classified as having diabetes/being a credit risk). The question at hand: did we classify all samples correctly, leaving little room for **false negatives**.

  * A better way to understand **recall** is of all of the individuals that are a credit risk, how many were classified by the model as being a credit risk?

  * High recall relates to a more comprehensive output and a low **false negative** rate.

  * **Calculation:** TP / (TP + FN)

Encourage students to consult the following [documentation](https://blog.exsilio.com/all/accuracy-precision-recall-f1-score-interpretation-of-performance-measures/) if they need additional explanation of precision and recall and how they are calculated.

Use the remaining time to answer any questions about logistic regression models and evaluating predictions. Then, move forward with the next activity.

- - -

### 9. Instructor Do: Confusion Matrix & Classification Report (10)

Students receive a live demonstration of how to create and use a confusion matrix and classification report to evaluate models for error.

**Files:** [confusion_matrix.ipynb](Activities/03-Ins_Confusion_Matrices/Solved/confusion_matrix.ipynb)

Open the starter-file, and highlight the below discussion points while live coding how to use a **confusion matrix**.

* A **confusion matrix** is used to measure and gauge the success of a model. Confusion matrices reveal the number of true negatives and true positives (actuals) for each categorical class and compares it to the number of predicted values for each class. These values are then individually summed by column and row. The aggregate sums are then compared to gauge accuracy and precision. If the aggregates match, the model can be considered accurate and precise.

  ![confusion_matrix_table.png](Images/confusion_matrix_table.png)

* Confusion matrices are great because they describe the performance of the classification model. By looking at the confusion matrix, one can determine whether or not the model has been correctly trained to produce comprehensive accurate and precise predictions.

* For binary classifiers like the **logistic regression** classifier, a **confusion matrix** would measure the number of positive and negative predictions. These will then be compared in relation to the actuals.

* So now the question is, how does one get data loaded into a confusion matrix for model evaluation? Most models will come equipped with a confusion matrix module, like the **sklearn** `metrics.confusion_matrix` module. The **sklearn** `confusion_matrix` function accepts two arguments, one data set containing the predicted values and another containing the actual data points.

Transition to the live coding aspect of the demo, and demonstrate how to use and interpret the **sklearn** `confusion_matrix` function.

* The `confusion_matrix` function can be imported into the Python environment from the `metrics` package. Once imported, it can be executed using the actual and predicted data points. The output is a two dimensional array. Columns reflect binary classes (high credit risk or low credit risk), and the rows represent the number of samples/data points that actually belong to that class.

    ```python
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)
    ```

    ![confusion_matrix.png](Images/confusion_matrix.png)

Communicate to students that a **classification report** can also be used to evaluate a model. When evaluating a model, the **accuracy**, **precision**, and **recall** must all be evaluated to ensure the rate of false positive sand false negatives are minimal. The results from these tests can be stored within a **classification report**, which can be used to assess and evaluate number of predicted occurrences for each class.

* Classification reports calculate the precision, recall, and f1 score (accuracy in relation to precision and recall). Classification reports can be generated using the **sklearn** `metrics.classification_report` module. All that is required to execute the `classification_report` function is the actual data points and predicted data points.

  * The **classification report** will automatically calculate precision, recall, and accuracy.

    ```python
    from sklearn.metrics import classification_report
    target_names = ["Class Purple", "Class Yellow"]
    print(classification_report(y_test, predictions, target_names=target_names))
    ```

    ![classification_report.png](Images/classification_report.png)

Finish the activity by asking students if there are any questions, and then transition to the student activity.

- - -

### 10. Students Do: Diagnosing the Model (10 min)

Students complete a bridge activity where they return to the model they created to predict diabetes and will use a **confusion matrix** and **classification report** to evaluate and diagnose the model. Emphasis needs to be placed on how to interpret confusion matrices and classification reports in order to diagnose issues in the model.

**Files**

* [README.md](Activities/04-Stu_Diagnosing_the_Model/README.md)

* [diagnosis.ipynb](Activities/04-Stu_Diagnosing_the_Model/Unsolved/diagnosis.ipynb)

- - -

### 11. Instructor Do: Diagnosing the Model Activity Review (10 min)

Students receive a dry walk through of the solution and are given the opportunity ask questions about creating and interpreting **confusion matrices** and **classification reports**.

**Files:** [diagnosis.ipynb](Activities/04-Stu_Diagnosing_the_Model/Solved/diagnosis.ipynb)

Engage the class with a brief Q&A session. Ask students if they have any questions about **confusion matrices** and **classification reports**. If students do not pose any questions, ask some of the below guided questions. Spend no more than 5 minutes on the Q&A session.

* What is a **confusion matrix**?

  * **Answer** A table used to describe the performance of the model. The **confusion matrix** will highlight differences in the number of samples predicted to belong to a specific class with the actual number of samples that do belong to that class.

* Would a user aggregate the columns or rows of a **confusion matrix**?

  * **Answer** Both. Values for columns and rows will be aggregated and then compared. Columns will reflect the sum of predicted categorical outcomes, and the rows will reflect the actual sum of outcomes.

* What is a **classification report**?

  * **Answer** A report that details the precision, recall, and accuracy of the predicted data points for each categorical class. A **classification report** can be used to determine the rate of false positives, false negatives, and the quality of the predictions.

Transition to the dry walk through by opening the solution file, and highlight the below discussion points. Go through this section quickly as students should be well versed in creating **confusion matrices** and **classification reports**.

* A **confusion matrix** is a table that describes the performance of a model by looking at the total number of outcomes for each class. Confusion matrices look at the total number of actual outcomes and juxtaposes them with predicted outcomes.

  * For example, with a confusion matrix, you can aggregate the number of actual positives and compare it to the number of predicted positives. The closer the values, the better the model. The same can be said with negative outcomes.

  * **Confusion matrices** can be a little difficult to understand at first. If students have questions/difficulty understanding, and or seem lost, use the following scenario to help reinforce how a confusion matrix is used:

    ```python
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)
    ```

    ![reading_confusion_matrix.png](Images/reading_confusion_matrix.png)

* Similarly, the **classification report** reveals the precision, recall, and accuracy of the predicted values for each class. These ratios are calculated using the actual and predicted data points.

    ```python
    from sklearn.metrics import classification_report
    target_names = ["No Diabetes", "Diabetes"]
    print(classification_report(y_test, predictions, target_names=target_names))
    ```

Next, transition into the interpretation part of the review activity. Ask students guided questions that will require them to interpret the results from the matrix and report.

* Ask students to interpret the **classification report**. What does it mean for the **diabetes** class to have a lower recall score compared to **no diabetes**?

  * **Answer** The **diabetes** predictions have a lower recall rate which means a higher rate of false negatives. There are individuals being predicted as not having diabetes that actually do. However, the data points predicting no diabetes have a higher recall score which means a lower rate of false negatives.

  * **Answer** The model is arguably precise but could benefit from additional training/fitting to improve predictions and reduce false negatives.

* Reassure students that even if the differences between **precision** and **recall** seem a little fuzzy right now, the difference will eventually make more sense as they interpret more classification reports.

Ask if there are any questions before moving forward.

- - -

### 12. Student Do: Build Loan Approver (15 mins)

Students will participate in a bag of tricks activity where they apply the machine learning concepts and technical skills learned thus far to create a model for approving loans.

**Instructions:** [README.md](Activities/05-Stu_Loan_Approver/README.md)

**Files:** [starter-code.js](Activities/05-Stu_Loan_Approver/Unsolved/loan_approver.ipynb)

- - -

### 13. BREAK (15 min)

- - -

### 14. Instructor Do: Build Loan Approver Activity Review (10 min)

The instructor leads a facilitated review discussion on the loan approver. The review will be a dry walk through with accompanying guided/review questions.

**Files:** [loan_approver.ipynb](Activities/05-Stu_Loan_Approver/Solved/loan_approver.ipynb)

In order to ensure pacing of the activity, do not ask all of the below questions. Use these questions as prompts to engage students and increase discussion.

Begin the review session with a few guided questions:

* Using the confusion matrix and classification report to evaluate the model, would you trust the predictions made by this model to decide when and when you should not loan out money? Should a bank trust it?

  * **Answer** The model in its current state is not optimized for accuracy. It should not be trusted to make predictions.

* What can we do to improve the accuracy of the model?

  * **Answer** Train the model with more data.

Open the solution and transition to a dry walk through of the activity. Remind students of the following:

* In order to build a supervised model and make predictions, data has to be provided that can be used to predict outcomes. This data set must contain **features** and a **target**.

  * Features are the fields that relate to credit worthiness (i.e. **assets**, **liabilities**, **income**, and **credit score**).

  * The target is the predicted outcome (i.e. approve or deny status.)

* Since features can vary in scale and range, features have been normalized (i.e. a candidate's income can be a value 100,000; however, their credit score's max value can only be 900). This ensures differences in scale do not sway predictions. Values have been normalized between 0 and 1.

* **Sklearn's** `LogisticRegression` module that can be used to create a logistic regression model. This model is needed in order to classify categorical outcomes.

  * The `LogisticRegression` module comes with functions to support preprocessing and model execution, such as `train_test_split`, `fit`, and `predict`.

* Fitting a model requires train and test data. The **sklearn** `train_test_split` function can be used to split a single data into these subsets. The model will then use the train and test data to make predictions and evaluate performance.

* Training/fitting a model with **sklearn** is as simple as running a single function: `fit`. The `fit` function has two main parameters: the features training data and the target training data.

* Using the model to make predictions is just as easy. The **sklearn** `predict` function accepts a single argument: the features to use to predict.

Continue the next part of the review by asking students questions and then explaining how the answer is implemented in the code:

* When measuring the performance and reliability of a model, machine learning engineers need to consider the precision of the model. What is precision?

  * **Answer** Precision is the ratio of correctly predicted positive outcomes out of all predicted positive outcomes.

* Recall is another performance metric that can be considered. What does recall measure? What does recall reveal about the model's predictions?

  * **Answer** Recall measures the number of correct positive predictions out of all predictions. The recall reveals that our model predicts more correct denies than approves.

* Based off of the precision and recall returned from the classification report, how has this model performed?

  * **Answer** The model would benefit from additional fitting/training. The model currently denies users more than it approves, even when it should approve. The accuracy averages only to ~50%.

* What is the difference between the confusion matrix and the classification report?

  * **Answer** The confusion matrix identifies the number of categorical outcome predictions made by the model and juxtaposes it against the actual results. Confusion matrices are perfect for evaluating false positives and false negatives. The classification report uses accuracy, precision, and recall to measure the performance and success of the model.The focus is on the ratio of correctly and incorrectly predicted values against all predictions.

* Ask students to provide examples of when accuracy can be sacrificed?

  * **Answer** When running a model where speed is more important than accuracy. A good example is when detecting fraud. It's more important to try and predict faster than to be more accurate. Time spent running a model for accuracy could result in a fraudulent transaction being processed and not flagged in time.

Ask for any remaining questions before moving on.

- - -

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

If time permits, illustrate to students how to define a decision boundary. A common practice to identify the decision boundary/hyperplane for the already identified data points prior to making predictions. This provides a visual representation of the already existing classes and their margin of separation.

* Emphasize to students that this practice of plotting the decision boundary is just illustrative. If you're short on time, do not review the code. Just show the students the visualization in the solution notebook. The goal is just to illustrate to students what a hyperplane is and the importance of wide margins.

* Also communicate to students that plotting the decision boundary with contour is only effective when there are two **features** in the data.

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

Emphasize to students that data will not always be equidistant with a wide margin. Explain that **support vectors** can fall within the margin of the hyperplane. These values should be considered errors and the classification should not be relied on.

* Remind students that margins should always be maximized

* Indicate that when support vectors are too close to the margin, there's a 50% change the classification can go either this. This is why these results are not reliable.

  ![overlap.png](Images/overlap.png)

  ![classification_errors.png](Images/classification_errors.png)

Now that the pre-existing data has been visualized into the corresponding classes, separated by a hyperplane, the model can be used to predict the classification of new data points. Just like with the Logistic Regression model, the `predict` function can be used to make label predictions.

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

- - -

### 16. Students Do: SVM Loan Approver (15 mins)

Students are asked to update their loan approver with an SVM model and rerun the evaluation metrics. Students will then compare the performance of the SVM model with the Logistic Regression model.

**Instructions:** [README.md](Activities/07_Stu_SVM_Loan_Approver/README.md)

**Files:** [svm_loan_approver.ipynb](Activities/07_Stu_SVM_Loan_Approver/Unsolved/svm_loan_approver.ipynb)

- - -

### 17. Instructor Do: SVM Loan Approver Activity Review (10 mins)

The instructor leads a dry walk through of the previous activity.

**Files:**

* [ssvm_loan_approver.ipynb](Activities/07-Stu_SVM_Loan_Approver/Solved/svm_loan_approver.ipynb)

Open the solution and explain the following:

* The SVM algorithm is an alternative to the Logistic Regression model when it comes to running classification engines. The SVM algorithm is often times more more accurate than other models.

* The SVM package is a part of the `sklearn.svm` module. The `svc` constructor is used to create and configure the model.

* SVM models can be either 2D (linear) or multi-dimensional (poly). The dimension of the model is defined by the `kernel` argument.

    ```python
    # Instantiate a linear SVM model
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear')
    classifier
    ```

    ```
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto_deprecated',
    kernel='linear', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)
    ```

* Once the model is created, it has to be fit with data.

    ```python
    # Fit the data
    classifier.fit(X_train, y_train)
    ```

* The model can then be scored for accuracy.

    ```python
    # Score the accuracy
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")
    ```

* An accurate model can make precise predictions. The **sklearn** `predict` function is used make predictions off of the new data.

    ```python
    # Make predictions using the test data
    predictions = classifier.predict(X_test)
    results = pd.DataFrame({"Prediction": predictions, "Actual": y_test}).reset_index(drop=True)
    results.head()
    ```

    ![prediction_results.png](Images/prediction_results.png)

* The last step is to evaluate the model. Just like with the Logistic Regression model, the `confusion_matrix` and `classification_report` libraries can be used to assess metrics and performance.

    ```python
    # Evaluate performance
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, predictions)

    from sklearn.metrics import classification_report
    print(classification_report(y_test, predictions))
    ```

  ![evaluate_svm.png](Images/evaluate_svm.png)

* Ask students which model performed better in terms of accuracy, precision, and recall.

  * **Answer** The SVM model performed better in terms of accuracy, precision, and recall.

If time remains, ask students the following guided/review questions.

* Ask students to define what support vector machines are.

  * **Answer** Data points that exist closest to the hyperplane. These points are used to help identify the position and orientation of the hyperplane, and they care called **support vectors**.

* A parameter named `kernel` is used when creating an SVM model. What does this parameter do?

  * **Answer** Identifies the orientation of the **hyperplane**, as either linear or multi-dimensional.

* What's the difference between the `decision_function` function and the `predict` function?

  * **Answer** The `decision_function` function has the classifier calculate the classification score for each data point. These values are used to classify the data points to either class. The output from `decision_function` should not be confused with the output from `predict`. `Predict` provides a classification/label. `Decision_function` returns a scalar value.

* What is `decision_function` used for?

  * **Answer** The `decision_function` function is used to identify the bounds of the **hyperplane**.

* If data points are overlapping, can their classification be trusted?

  * **Answer** No. Data points that are overlapping have a 50% chance of being classified incorrectly. The goal is to maximize the margin.

Ask if there are any questions before moving forward.

- - -

### 18. Instructor Do: Which Model is the Best? (5 min)

Throughout the day, students have implemented Logistic Regression and SVM classification algorithms to determine loan eligibility. Now it's time to evaluate both models and determine which performed better.

Engage the class with the following discussion:

* Remind students that there are a wealth of machine learning algorithms that can classify outcomes. Explain that both the Logistic Regression and SVM models were both able to predict outcomes; however, the improtant question is which model performed best.

* Ask students if anyone has any suspicions regarding which algorithm performed best: Logistic Regression or SVM.

  * **Answer** SVM

  * **Answer** Logistic Regression

* Ask students what they think the best approach would be to evaluate both models.

  * **Answer** Compare the confusion matrices and classification reports.

* Open the slideshow and navigate to the last slide, which contains the confusion matrix and classification report for both models. Give students a moment to review, and then ask which model performed best.

  * **Answer** The SVM model performed best. Precision, recall, and accuracy were all higher for the SVM loan approver. Interestingly enough, recall percentage for deny is the same for the SVM and Logistic Regresion loan approver, meaning both algorithms correctly predicted the same number of true positive denies.

  ![which_is_best.png](Images/which_is_best.png)

  ![which_is_best_2.png](Images/which_is_best_2.png)

End the activity by congratulating the students on learning two new machine learning algorithms. Let students know they've done a great job ramping up to new statistical calculations and classification algorithms. This is a significant milestone!

* Remind the students that these algorithms can be used for a range of classification use cases, from fraud detection to medical diagnosis, computer vision and election results.

* Assure students that a lot of the statistical concepts covered will be re-used and re-emphasized in upcoming lessons. This will provide plenty of opportunity to re-enforce  the teachings.

Ask if there are any questions before ending the class.
