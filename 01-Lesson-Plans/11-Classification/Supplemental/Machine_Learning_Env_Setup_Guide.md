# Machine Learning Environment Setup Guide

This guide serves as a step by step process for setting up and validating the tools required for the machine learning portion of the curriculum. Many of these tools are needed to train and test machine learning models. Without these tools, class activities and code cannot be completed.

This guide will include installation and verification steps for the following technologies:

* Imbalanced-learn

## Imbalanced-learn

### Install

In order to install the `imbalanced-learn` package, all of the dependencies must be satisfied. These dependencies come packaged with every Anaconda install/distribution. The dependencies list can be found below for reference.

* Numpy (>=1.11)

* Scipy (>=0.17)

* Scikit-learn (>=0.21)

* Keras 2 (optional)

* Tensorflow (optional)

Open the a terminal, and execute the following command to install `imbalanced-learn`.

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

It can be frustrating when packages do not install correctly. Use the below approaches to troubleshoot installation issues and get your machine learning libraries up and running!

**Update Conda Environment**

An out-of-date Anaconda environment can create issues when trying to install new packages. Follow the below steps to update your conda environment.

1. Deactivate your current conda environment. This is required in order to update the global conda environment. Be sure to quit any running applications, such as Jupyter, prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update conda.

    ```shell
    conda update conda
    ```

3. Create a fresh conda environment to use with PyViz.

    ```shell
    conda create -n mlenv python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate mlenv
    ```

5. Install the **imbalanced-learn** package.

    ```shell
    conda install -c conda-forge imbalanced-learn
    ```

Consult the [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/) documentation for additional information about the **imbalanced-learn** library.
