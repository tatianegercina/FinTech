# Machine Learning Environment Setup Guide

This guide serves as a step by step process for setting up and validating the tools required for the machine learning portion of the curriculum. Many of these tools are needed to train and test machine learning models. Without these tools, class activities and homeworks cannot be completed.

This guide will outline how to setup and verify that the following technologies are installed within the Python environment:

* Scilearn-Kit

* Imbalance-learn

## Scikit-learn

Scilearn-kit is a package that offers machine learning objects and functions that can be used with a Python environment.

* Scilearn-kit is built on top of NumPy, SciPy, and Matplotlib

* Scilearn-kit includes statistical functions and models that an be used out-of-the-box in order to complete predictive analytics.

* Scilearn-kit can be used for:

  * Classification

  * Regression

  * Analysis

### Install Scikit-learn

Scilearn-kit can be installed using the `conda install` function.

* Execute the following command in a terminal to install scikit-learn.

    ```shell
    conda install -c anaconda scikit-learn
    ```

    ![scikitlearn_install.png](Images/scikitlearn_install.png)

* Confirm scikit-learn was installed correctly, run the following command:

    ```shell
    conda list | grep scikit-learn
    ```

    ![confirm_sckitlearn.png](Images/confirm_sckitlearn.png)

Consult the [scikit-learn](https://scikit-learn.org/stable/documentation.html) documentation for additional assistance and detail.

## Imbalance-learn

### Install

In order to install the `imbalance-learn` package, all of the dependencies must be satisfied. The dependencies list can be found below:

* Numpy (>=1.11)

* Scipy (>=0.17)

* Scikit-learn (>=0.21)

* Keras 2 (optional)

* Tensorflow (optional)

```shell
conda install -c conda-forge imbalanced-learn
```
