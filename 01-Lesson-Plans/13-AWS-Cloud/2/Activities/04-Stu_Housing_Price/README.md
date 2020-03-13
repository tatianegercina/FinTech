# Housing Price Prediction on SageMaker

In this activity, you'll train and deploy a _linear regression_ model using the [_Boston house-price dataset_](http://lib.stat.cmu.edu/datasets/boston) and an Amazon SageMaker built-in algorithm.

The _Boston house-price dataset_, contains information about different houses in Boston collected at the end of the 1970's; this dataset has been used in many machine learning research papers that address regression problems, it was initially presented in [_Harrison, D. and Rubinfeld, D.L._ **Hedonic prices and the demand for clean air**, Journal of Environmental Economics & Management, vol.5, 81-102, 1978](https://doi.org/10.1016/0095-0696(78)90006-2).

## Instructions

* Open your Amazon SageMaker notebook instance, and upload the provided `boston-housing-regression.ipynb` notebook to JupyterLab.

* Walk through the cell steps and add any missing code.

* The notebook will guide you through the process to create, train and deploy a supervised regression model using the Amazon SageMaker's built-in `Linear Learner` algorithm.

* Take a look at the [Amazon SageMaker Linear Learner Algorithm documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) if you have any questions about how it works.

* Once the model is deployed, you can forecast prices of homes not included in the dataset and also review the model's performance.

* If you finish early, take a look at other Amazon SageMaker built-in algorithms [here](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html).
