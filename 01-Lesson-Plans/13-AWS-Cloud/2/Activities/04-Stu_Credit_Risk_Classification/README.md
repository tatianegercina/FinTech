# Credit Risk Classification with Amazon SageMaker

In this activity, you will train and deploy a binary classification model using the popular [_German Credit Risk Dataset_](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) and an Amazon SageMaker built-in algorithm.

## Dataset

The "German Credit Risk Dataset," classifies people described by a set of attributes as good or bad credit risks. Due to the complex encoding of the original dataset, we will be using a curated version of the dataset from Kaggle.

<https://www.kaggle.com/uciml/german-credit>

**Original source:** [Professor Dr. Hans Hofmann. Institut f"ur Statistik und "Okonometrie Universit"at Hamburg. FB Wirtschaftswissenschaften. Von-Melle-Park 5. 2000 Hamburg 13.](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)

## Instructions

This activity will require the use of Amazon SageMaker Studio. Follow each cell, complete the missing code on the starter notebook as you are guided through the process.

1. Open Amazon SageMaker Studio and upload the provided `credit-risk-classification.ipynb` notebook to the root folder.

2. Upload the provided `german_credit_data.csv` data file to the `Data` folder in Amazon SageMaker Studio.

3. Walkthrough the cell steps and add any missing code.

4. Once the model is deployed, predict the credit risk given an input set of attributes.

The notebook will guide you through the process to create, train and deploy a supervised classification model using the Amazon SageMaker's built-in `Linear Learner` algorithm.

Take a look at the [Amazon SageMaker Linear Learner Algorithm documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) if you have any questions about how it works.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
