# Machine Learning Environment Setup Guide

This guide serves as a step by step process for setting up and validating the tools required for the machine learning portion of the curriculum. Many of these tools are needed to train and test machine learning models. Without these tools, class activities and homeworks cannot be completed.

This guide will outline how to setup and verify that the following technologies are installed within the Python environment:

* Imbalance-learn

## Imbalanced-learn

### Install

In order to install the `imbalanced-learn` package, all of the dependencies must be satisfied. The dependencies list can be found below:

* Numpy (>=1.11)

* Scipy (>=0.17)

* Scikit-learn (>=0.21)

* Keras 2 (optional)

* Tensorflow (optional)

Open the a terminal, and execute the following commands to install `imbalanced-learn`.

* Use the `conda install` command to download the `imbalanced-learn` module.

  ```shell
  conda install -c conda-forge imbalanced-learn
  ```

  ![imbalanced_learn_install.png](Images/imbalanced_learn_install.png)

### Verify Installation

Once the `imbalanced-learn` download is complete, verify the installation completed successfully.

* Use the `conda-list` function with a `grep` argument to identify if the `imbalanced-learn` library installed successfully.

  ```shell
  conda-list | grep imbalanced-learn
  ```

### Troubleshooting

It is common for challenges to be faced when installing a package/module. Follow the below steps to help troubleshoot any issue with an Ananaconda package.
