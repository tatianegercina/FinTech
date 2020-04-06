# Deploying Machine Learning Model in Amazon SageMaker Studio

In this guide, you will learn how to create, train, deploy, and evaluate a built-in machine learning model in Amazon SageMaker Studio.

If you have not created an Amazon SageMaker Studio instance yet, please follow the ["Create an Amazon SageMaker Studio Instance"](Create-Amazon-SageMaker-Studio-Instance.md) supplemental guide first.

**Files:**

* [rainfall_forecast.ipynb](Resources/Deploy-ML-Models-SageMakerStudio/rainfall_forecast.ipynb)

* [x_austin_final.csv](Resources/Deploy-ML-Models-SageMakerStudio/Data/x_austin_final.csv)

* [y_austin_final.csv](Resources/Deploy-ML-Models-SageMakerStudio/Data/y_austin_final.csv)

Amazon provides an extensive library of machine learning models that are optimized for the cloud. This guide will show you how to use one of Amazon's linear regression models to predict the amount of rain that will fall in Austin, given the average temperature in Fahrenheit degrees.

Log-in into the AWS Management Console using your `administrator` IAM user and continue by opening Amazon SageMaker Studio. Remember to switch to the `US East (Ohio)` region before opening the Amazon SageMaker Studio control panel.

![Deploy SageMaker Model - step 0](Images/deploy-sagemaker-0.gif)

Open the Amazon SageMaker Studio UI, create a folder called `Data` and upload the following `CSV` files.

* `x_austin_final.csv`, this file contains historical weather conditions in Austin, Texas, along 1319 days.

* `y_austin_final.cvs`, this file contains the precipitations sum in inches in Austin, Texas, along 1319 days.

![Deploy SageMaker Model - step 1](Images/deploy-sagemaker-1.gif)

Navigate to the main folder on Amazon SageMaker Studio, and import the unsolved version of the Jupyter notebook.

![Deploy SageMaker Model - step 2](Images/deploy-sagemaker-2.gif)

Open the `rainfall_forecast.ipynb` notebook, select the `Python 3 (Data Science) kernel and follow the next steps:

* In the `Initial imports` section, some well-known libraries are imported. The `sklearn` library will be used to split the dataset in training and testing sets, as well as to evaluate the model.

  ```python
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

    # Transform the "TempAvgF" column to a vector
    X = features["TempAvgF"].values.reshape(-1, 1)
    ```

  * The `y_austin_final.csv` data is initially loaded into the `y` DataFrame; this data represents the target variable in the linear model.

    ```python
    # Read the target data (precipitation sum inches)
    file_path = Path("Data/y_austin_final.csv")
    y = pd.read_csv(file_path, names=["PrecipitationSumInches"], header=None)

    # Transform y into a vector
    y = y.iloc[:, 0].values
    ```

* The data is split into a training and testing DataSets using the `train_test_split()` function from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

Once the data is loaded, the next step is to create the linear regression model. The process starts with some initial configurations as follows:

* The training and testing data should be stored in an Amazon S3 bucket, so a variable to store the name of the bucket we created before is defined. Set the `bucket` variable to the name of the private bucket you created previously, e.g. `sm-models-20200330-1244`.

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

Now it's time to upload the data to Amazon S3. To train a machine learning model using Amazon SageMaker, the training and testing data should pass through an Amazon S3 Bucket formatted using the [protobuf recordIO format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html#td-serialization).

The profobuf recordIO format, is a method to serialize structured data (similar to `JSON`), to allow different applications to communicate with each other or for storing data.

Using the profobuf recordIO format, allows you to take advantage of "Pipe mode" when training the algorithms that support it. In "Pipe mode," your training job streams data directly from Amazon S3. Streaming can provide faster start times for training jobs and better throughput.

Continue with the following code, to format the training data as a protobuf recordIO, and upload it to the Amazon S3 bucket.

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

When you provide test data, the algorithm logs include the test score for the final model.

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

Once you have uploaded your data to Amazon S3, it's time to train the machine learning model. In this demo, you will use the Amazon SageMaker's [_linear learner algorithm_](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) to run a linear regression prediction model.

Create the instance of the linear learner algorithm as follows:

* The instance of the `linear learner` is created using the `get_image_uri()` method from the `sagemaker` library.

  ```python
  container = get_image_uri(boto3.Session().region_name, "linear-learner")
  ```

* Before creating the estimator container, an Amazon SageMaker's session should be started.

  ```python
  sess = sagemaker.Session()
  ```

* The estimator container is an AWS EC2 instance that will store and run the model. The estimator container is created using a `ml.m4.xlarge` instance type for training the model.

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

* The model is trained using the `fit` method of the Amazon SageMaker estimator.

  ```python
  linear.fit({'train': s3_train_data, 'test': s3_test_data})
  ```

Fitting the model may take up to 5 minutes since Amazon SageMaker is provisioning not only a machine learning model but also a series of virtual machines (EC2 instances) to compute the model.

The model fitting process will use resources from the AWS account. Typically, this time is not billed in the two months trial period. However, policies of the AWS free and trial offer change regularly, so you should always check the pricing pages for any service that you want to use.

Below, a sample output is shown; you will notice that the output text is in blue.

![Deploy SageMaker Model - step 3](Images/deploy-sagemaker-3.gif)

Once the `linear-learner` model was trained, it can be deployed to make predictions of the rainfall in Austin. Proceed as follows:

* In order to make predictions, the model should be deployed; a `ml.t2.medium` instance type is defined since this is the instance type we have available for deployment as part of the free tier offer.

  ```python
  linear_predictor = linear.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
  ```

**Important Note:** This step may take up to 8 minutes, it may take less time with an instance type with more computing power, but by doing date, we may incur additional costs beyond the limits of the free tier offer.

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

Once you have the predictions, the model can be evaluated using the techniques we covered in previous units. First, a plot to contrast the predicted rainfall values versus the real values is created.

![Deploy SageMaker Model - step 4](Images/deploy-sagemaker-4.png)

Additionally, the `RMSE` and `R2` scores are calculated.

![Deploy SageMaker Model - step 5](Images/deploy-sagemaker-5.png)

Finally, after reviewing the model evaluation's results, it's crucial to delete the endpoint to avoid additional AWS resources usage and extra billing.

```python
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
```

Amazon SageMaker stores the prediction results and data in Amazon S3. To explore this data, click on "Services" and select Amazon S3 from the services list.

![Open the Amazon S3 console](Images/open-amazon-s3-console.gif)

Open the private bucket you created before, for example, `sm-models-20200330-1244`, Amazon SageMaker stores the model's data in a compressed format for further analysis and usage.

![Visualizing the Amazon SageMaker output files in Amazon S3](Images/amazon-sagemaker-s3-files.gif)

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
