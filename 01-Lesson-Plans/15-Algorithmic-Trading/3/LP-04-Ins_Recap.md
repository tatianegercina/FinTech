### 4. Instructor Do: Recap (15 min)

In this activity, instructors will briefly re-cap the process of training and using a Random Forest trading model, discuss the ways in which the model can potentially be improved, and consider deploying the model through alternative means such as AWS' Sagemaker--a machine learning cloud service that enables users to build, train, and deploy machine learning models quickly and conveniently.

Open the slideshow and quickly re-cap the following. Engage students by having them answer the questions wherever possible:

* What did we learn today?

  **Answer:** We learned how to implement a machine learning model (Random Forest) to make predictions of next-day daily returns, given a set of trading signals derived from raw asset closing prices.

* What was the process for implementing a machine learning trading model?

  **Answer** The process for implementing a machine learning model, regardless of domain, generally includes the following: preparing the data, splitting the data into train and test datasets, fitting the x and y train data to the model, making predictions from the x test data, and comparing the predicted results to the y test data (actual results) to evaluate the performance of the overall model.

* What was the main takeaway from today's lesson?

  **Answer:** That the process for implementing a machine learning trading model can be fairly straightforward, but the ability to construct a sophisticated enough trading model that can outperform the markets will require more effort via further understanding of the markets and fine-tuning of the model (more features and therefore information).

Then, ask students if they have any further questions before moving onto the following talking points regarding model improvement:

* Admittedly, the Random Forest trading model still has room for improvement before it can be considered a robust system for automated machine learning based trading. This is because while the activities aim to simplify the process for implementation to provide beginner insight, the trade-off in complexity affects the overall performance of the model. In particular, several factors could have benefited the training and therefore overall performance of the Random Forest trading model, such as using more observations or data, more features or variables, and continuous rather than binary calculations for trading signals.

* The number of observations and features supplied to the model for training can be increased to provide more information, and therefore a better understanding for the model to make more accurate predictions. In this case, there were only 462 observations and 3 features upon which the model was trained.

  ![x-test-shape](Images/x-test-shape.png)

* In addition, for simplicity, the trading signals were output as binary calculations--either 0 or 1, do not engage in the trade or engage in the trade. However, if a scaled continuous value were used instead of a binary value, the *extent* upon which a trading signal is defined or how *far* the values differ from the crossover point, could be used therefore providing more information to train the model.

  ![continuous-vs-binary](Images/continuous-vs-binary.png)

* Lastly, a lot of effort and time is spent on collecting and preparing training data. Therefore, as an alternative solution, Amazon SageMaker, a machine learning cloud service that enables users to build, train, and deploy machine learning models quickly and conveniently, could be used to minimize the work effort spent on preparing data and instead focus on optimizing the accuracy or performance of the model. Amazon SageMaker also provides several methods for accessing its functionality such as via the AWS web GUI, specific API endpoints, or the SageMaker Python SDK.

  ![aws-sagemaker](Images/aws-sagemaker.png)
