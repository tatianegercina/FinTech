# IEXFinance Environment Setup Guide

This guide serves as a step by step process for setting up and validating the `iexfinance` Python SDK. Without this library, class activities and code will not be able to extract historical stock data and therefore will not be able to be completed.

This guide will include installation and verification steps for the following technologies:

* IEXFinance

## IEXFinance

### Install

In order to install the `iexfinance` package, all of the dependencies must be satisfied. The dependencies list can be found below for reference.

* Pandas

* Requests

Open a terminal, and execute the following command to install `iexfinance`.

* Use the `pip install` command to download the `iexfinance` module.

  ```shell
  pip install iexfinance
  ```

  ![iexfinance_install.png](Images/iexfinance_install.png)

### Verify Installation

Once the `iexfinance` download is complete, verify the installation completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `imbalanced-learn` library installed successfully.

  ```shell
  pip list | grep iexfinance
  ```

  ![iexfinance_verify](Images/iexfinance_verify.png)

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
    conda create -n iexenv python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate iexenv
    ```

5. Install the **iexfinance** package.

    ```shell
    pip install iexfinance
    ```

Consult the [iexfinance](https://addisonlynch.github.io/iexfinance/stable/index.html) documentation for additional information about the **iexfinance** library.
