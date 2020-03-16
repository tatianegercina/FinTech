# Deploying a Machine Learning Model in Amazon SageMaker Using the Free Tier

## Important Considerations

Using the AWS Free Tier is excellent since it offers a chance to test the cloud services by virtually not being charged in your credit card; however, some particularities are worth to keep in mind while using Amazon SageMaker.

The first thing you should be aware of is that Amazon SageMaker offer during the Free Tier period is a two-months free trial that will allow you to use `250` Hours
per month of `t2.medium` notebook instances for the first two months of your Free Tier offer.

Having `t2.medium` instances available means that any notebook instance you create should be this size, as you will see in the next section.

The second fact to keep in mind is that those `250` hours per month includes having your notebook instance hosted in AWS, regardless it's running or stopped. So you may save your notebooks locally and delete the instances you are not going longer use if you want to avoid unwanted charges to your credit card.

Be sure to set the Free Tier alerts as it's explained in the ["Create and Activate an AWS Account" guide](1-Create-and-Activate-an-AWS-Account.md).

## Deploying a Machine Learning Model

In this section, you will learn how to create, train, deploy, and evaluate a machine learning model in Amazon SageMaker.

For this demo, you will use one of Amazon's linear regression models to predict the amount of rain that will fall in Austin, given the average temperature in Fahrenheit degrees.

In the [`Resources` folder][Resources/], you will find the complete code used in this guide as a reference.

If you don't have a notebook instance in Amazon SageMaker, start by creating a new `ml.t2.medium` notebook instances as follows.

* Navigate to the AWS Management Console homepage, on the _Find Services_ search box type _sagemaker_, and select Amazon SageMaker from the list.

  ![Creating an Amazon SageMaker instance - step 7](Images/sagemaker-7.png)

* On the Amazon SageMaker console, be sure to select the region where your S3 bucket is located; we will use `Oregon` for this demo. Next, on the left pane menu, under _Notebook_ section, choose _Notebook instances_.

  ![Creating an Amazon SageMaker instance - step 8](Images/sagemaker-8.png)

* On the _Notebook instances_ page, click on the _Create notebook instance_ button.

  ![Creating an Amazon SageMaker instance - step 9](Images/sagemaker-9.png)

* Fill in the following values on the _Create notebook instance_ page:

  * **Section: Notebook instance settings**

    * _Notebook instance name:_ Set a name for your notebook instance, we use `sm-test` for this demo

    * _Notebook instance type:_ It's is essential to choose `ml.t2.medium` as long as you want to use the Free Tier offer.

    * _Elastic Inference:_ `none`.

    ![Creating an Amazon SageMaker instance - step 10](Images/sagemaker-10.png)

  * **Section: Permissions and encryption**

    * _IAM role:_ On the dropdown list, select the `Create a new role` option.
    ![Creating an Amazon SageMaker instance - step 11](Images/sagemaker-11.png)

    * Under the _S3 buckets you specify - optional_ section, choose _Specific S3 buckets_ and type the name of the Amazon S3 bucket you created (e.g. `sagemaker-20190903-1026`), click on _Create role_ to continue.
    ![Creating an Amazon SageMaker instance - step 12](Images/sagemaker-12.png)

    * _Root access:_ Be sure that the `Enable - Give users root access to the notebook` option is selected.
    ![Creating an Amazon SageMaker instance - step 13](Images/sagemaker-13.png)

* Scroll down and click on the _Create notebook instance_ button to continue. Grab a cup of coffee and wait since the creation process takes up to five minutes to finish.

* Once the notebook instance status is _InService_, it's ready to be used; on the _Actions_ column, click on `Open JupyterLab` to continue.

  ![Creating an Amazon SageMaker instance - step 15](Images/sagemaker-15.png)

* After a few seconds, you will see the Jupyter Lab UI running on the AWS Cloud.

Once you created your notebook instance, you can start deploying your machine learning model as follows:

* Create a new folder called `Data`.

  ![Deploy SageMaker Model - step 1](Images/deploy-sagemaker-1.png)

* Open the `Data` folder and upload the `CSV` files provided.

  * `x_austin_final.csv`, this file contains historical weather conditions in Austin, Texas, along 1319 days.

  * `y_austin_final.cvs`, this file contains the precipitations sum in inches in Austin, Texas, along 1319 days.

    ![Deploy SageMaker Model - step 2](Images/deploy-sagemaker-2.png)

* Navigate to the main folder on Jupyter lab, and import the provided Jupyter notebook to your Amazon SageMaker notebook instance.

* In the `Initial imports` section, some well-known libraries are imported. The `sklearn` library will be used to split the dataset in training and testing sets, as well as to evaluate the model.

  ```python
  import os
  import io
  import json
  import numpy as np
  import pandas as pd
  from path import Path
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import mean_squared_error, r2_score
  ```

* To use Amazon SageMaker, the following libraries are needed.

  ```python
  import sagemaker
  import sagemaker.amazon.common as smac
  from sagemaker.predictor import csv_serializer, json_deserializer
  from sagemaker import get_execution_role
  from sagemaker.amazon.amazon_estimator import get_image_uri
  import boto3
  ```

* Along with the `sagemaker` modules, the `boto3` library is imported; `boto3` is the [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

* The data to train and test the model, is loaded into two Pandas DataFrames, next, the data is transformed into a vector as follows:

  * The `x_austin_final.csv` data is loaded into the `features` DataFrame, the `TempAvgF` column that denotes the average temperature in Austin in Fahrenheit degrees is taken as an input variable (predictor) for the linear model.

    ```python
    # Read the weather features data
    file_path = Path("Data/x_austin_final.csv")
    features = pd.read_csv(file_path)

    # Transforming the "TempAvgF" column to a vector
    X = features["TempAvgF"].values.reshape(-1, 1)
    ```

  * The `y_austin_final.csv` data is initially loaded into the `y` DataFrame; this data represents the target variable in the linear model.

    ```python
    # Read the target data (precipitation sum inches)
    file_path = Path("Data/y_austin_final.csv")
    y = pd.read_csv(file_path, names=["PrecipitationSumInches"], header=None)

    # Transforming y into a vector
    y = y.iloc[:, 0].values
    ```

* The data is split into a training and testing DataSets using the `train_test_split()` function from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  ```

* The next step is to create the linear regression model. The process starts with some initial configurations as follows:

  * The training and testing data should be stored in an Amazon S3 bucket, so a variable to store the name of the bucket we created before is defined.

    ```python
    bucket = "sagemaker-bucket-name-here"
    ```

  * To identify the data files stored in Amazon S3, a prefix is defined.

    ```python
    prefix = "austin-rainfall-regression"
    ```

  * The current role of the IAM user running the notebook is stored in the `role` variable.

    ```python
    role = get_execution_role()
    ```

* Now it's time to upload the data to Amazon S3. To train the machine learning model using Amazon SageMaker, the training and testing data should pass through an Amazon S3 Bucket formatted using the [protobuf recordIO format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html#td-serialization).

* The profobuf recordIO format, is a method to serialize structured data (similar to `JSON`), to allow different applications to communicate with each other or for storing data.

* Using the profobuf recordIO format, allows you to take advantage of _Pipe mode_ when training the algorithms that support it.

* In _Pipe mode_, your training job streams data directly from Amazon S3. Streaming can provide faster start times for training jobs and better throughput.

* The following code formats the training data as a protobuf recordIO, and upload it to the Amazon S3 bucket.

  ```python
  # Encode the training data as Protocol Buffer
  buf = io.BytesIO()
  vectors = np.array(X_train).astype("float32")
  labels = np.array(y_train).astype("float32")
  smac.write_numpy_to_dense_tensor(buf, vectors, labels)
  buf.seek(0)

  # Upload encoded training data to Amazon S3
  key = 'linear_train.data'
  boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "train", key)).upload_fileobj(buf)
  s3_train_data = "s3://{}/{}/train/{}".format(bucket, prefix, key)
  print("Training data uploaded to: {}".format(s3_train_data))
  ```

* If you provide test data, the algorithm logs include the test score for the final model.

  ```python
  # Encode the testing data as Protocol Buffer
  buf = io.BytesIO()
  vectors = np.array(X_test).astype("float32")
  labels = np.array(y_test).astype("float32")
  smac.write_numpy_to_dense_tensor(buf, vectors, labels)
  buf.seek(0)

  # Upload encoded testing data to Amazon S3
  key = "linear_test.data"
  boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "test", key)).upload_fileobj(buf)
  s3_test_data = "s3://{}/{}/test/{}".format(bucket, prefix, key)
  print("Testing data uploaded to: {}".format(s3_test_data))
  ```

* Once you have uploaded your data to Amazon S3, it's time to train the machine learning model. We will use the Amazon SageMaker's [_linear learner algorithm_](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) to run a linear regression prediction model.

* Create the instance of the linear learner algorithm as follows:

  * The instance of the `linear learner` is created using the `get_image_uri()` method from the `sagemaker` library.

    ```python
    container = get_image_uri(boto3.Session().region_name, "linear-learner")
    ```

  * Before creating the estimator container, an Amazon SageMaker's session should be started.

    ```python
    sess = sagemaker.Session()
    ```

  * The estimator container is an AWS EC2 instance that will store and run the model. The estimator container is created using an `ml.m4.xlarge` instance type for training the model.

    ```python
    linear = sagemaker.estimator.Estimator(
      container,
      role,
      train_instance_count=1,
      train_instance_type="ml.m4.xlarge",
      output_path="s3://{}/{}/output".format(bucket, prefix),
      sagemaker_session=sess
      )
    ```

  * **Important Note:** Despite we created our notebook instance choosing the `ml.t2.medium` type, we have the `ml.m4.xlarge` instance type for training purposes in the two-month trial period.

  * The linear learner hyperparameters are defined next, it's important to highlight that the `feature_dim` parameter should match with the number of predictors in `X`, in this case since we only have one predictor its value is `1`.

    ```python
    # Define linear learner hyperparameters
    linear.set_hyperparameters(
      feature_dim=1,
      mini_batch_size=100,
      predictor_type="regressor",
      epochs=10,
      num_models=32,
      loss="absolute_loss"
      )
    ```

  * The model is trained using the `fit` method of the Amazon SageMaker estimator. **Note:** This step might take a few minutes.

    ```python
    linear.fit({'train': s3_train_data, 'test': s3_test_data})
    ```

* A sample output of this step is shown below; you may notice that the output text is in blue.

* **Important Note:** This step may take up to `15` minutes since Amazon SageMaker is provisioning not only a Jupyter notebook but also a series of virtual machines (EC2 instances) to compute the model.

![Deploy SageMaker Model - step 3](Images/deploy-sagemaker-3.gif)

* Once the `lineal-learner` model was trained, it can be deployed to make predictions of the rainfall in Austin.

* To make predictions, the model should be deployed; a `ml.t2.medium` instance type is defined since this is the instance type we selected when we created the notebook that is part of the free tier offer.

  ```python
  linear_predictor = linear.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
  ```

* Some configurations should be made to specify the type of data files that are going to be used and to define how the data is going to be serialized and deserialized.

  ```python
  linear_predictor.content_type = 'text/csv'
  linear_predictor.serializer = csv_serializer
  linear_predictor.deserializer = json_deserializer
  ```

* To make predictions, we use the `predict()` method of the model. We will make predictions using the testing data; results are stored in the `y_predictions` array.

  ```python
  result = linear_predictor.predict(X_test)
  y_predictions = np.array([r["score"] for r in result["predictions"]])
  ```

* Once you have the predictions, the model can be evaluated using the techniques you already know. First, a plot to contrast the predicted rainfall values versus the real values is created.

  ![Deploy SageMaker Model - step 4](Images/deploy-sagemaker-4.png)

* Additionally, the `RMSE` and `R2` scores are calculated.

  ![Deploy SageMaker Model - step 5](Images/deploy-sagemaker-5.png)

* Finally, the endpoint needs to be deleted to avoid additional AWS resources usage and extra billing.

  ```python
  sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
  ```

You can learn more about the different Amazon SageMaker built-in algorithms in the following page:

* [Use Amazon SageMaker Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

## Troubleshooting Guide

When you run an Amazon SageMaker notebook instance, you may see an error message similar to this one:

![Amazon SageMaker Error](Images/sagemaker-error.png)

If you see this error message, you may be asked to contact AWS Support to increase the limit of your notebook instances, despite the fact that you can do it, it's not necessary since you can fix this issue by checking the following:

1. Be sure you selected the `ml.t2.medium` instance type when you create your notebook instance.

    ![Check the notebook instance type](Images/sagemaker-10.png)

2. Ensure that the estimator container is created using an `ml.m4.xlarge` instance type for training the model.

    ```python
    linear = sagemaker.estimator.Estimator(
      container,
      role,
      train_instance_count=1,
      train_instance_type="ml.m4.xlarge",
      output_path="s3://{}/{}/output".format(bucket, prefix),
      sagemaker_session=sess
      )
    ```

3. Be sure that you selected a `ml.t2.medium` instance type in the `deploy()` method if the model. This is the instance type you selected when you created the notebook instance.

    ```python
    linear_predictor = linear.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
    ```

Once you verify these configurations, you may be able to deploy your models in Amazon SageMaker. If the issue persists, contact your instructional staff for support.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
