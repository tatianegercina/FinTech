# Credit Risk Classification with Amazon SageMaker

In this activity, you will train and deploy a _binary classification_ model using the popular [_German Credit Risk Dataset_](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) and an Amazon SageMaker built-in algorithm.

### Dataset

The _German Credit Risk Dataset_, classifies people described by a set of attributes as good or bad credit risks. Due to the complex encoding of the original dataset, we will be using a *curated* version of the dataset from Kaggle.

<https://www.kaggle.com/uciml/german-credit>

__Original source:__
Professor Dr. Hans Hofmann
Institut f"ur Statistik und "Okonometrie
Universit"at Hamburg
FB Wirtschaftswissenschaften
Von-Melle-Park 5
2000 Hamburg 13

## Instructions

* Open your Amazon SageMaker notebook instance, and upload the provided `credit-risk-classification.ipynb` notebook to JupyterLab.

* Walk through the cell steps and add any missing code.

* The notebook will guide you through the process to create, train and deploy a supervised *classification* model using the Amazon SageMaker's built-in `Linear Learner` algorithm. This is similar to the `Boston house-price` activity, however here you will be solving a classification problem rather than regression. The SageMaker `linear-learner` algorithm will have the hyper-parameter: `predictor_type='binary_classifier'`.

* Take a look at the [Amazon SageMaker Linear Learner Algorithm documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) if you have any questions about how it works.

* Once the model is deployed, you can predict the credit risk given an input set of attributes.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
