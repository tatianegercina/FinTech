# Dotenv, Asyncio, and Streamz Installation Guide

This guide serves as a step by step process for setting up and validating the asyncio and streamz Python libraries. Without these libraries, class activities and their associated code will not be able to perform the necessary operations for asynchronous programming and data streaming, respectively.

All packages should be installed into the `algotrading` virtual environment.  If you have not already created an `algotrading` virtual environment you can do so by typing the following commands in your terminal:

  ```shell
  conda create -n algotrading python=3.7 anaconda
  ```

## Installation

To avoid library dependencies conflicts, we strongly recommend to create a fresh virtual environment for this Unit. You will use environment variables, so if you are creating a new virtual environment, be sure tha all of the dependencies are satisfied. The dependencies list can be found below for reference.

* [`asyncio`](https://pypi.org/project/asyncio/)

* [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Open a terminal, and execute the following commands to install `python-dotenv`, `asyncio`, and `streamz`, respectively.

* Use the `pip install` command to download the `python-dotenv` module.

  ```shell
  pip install python-dotenv
  ```

* Activate your `algotrading` virtual environment.

  ```shell
  conda activate algotrading
  ```

* Use the `pip install` command to download the `asyncio` module.

  ```shell
  pip install asyncio
  ```

  ![asyncio-install](Images/asyncio-install.png)

* Use the `conda install` command to download the `streamz` module.

  ```shell
  conda install -c conda-forge streamz
  ```

  ![streamz-install](Images/streamz-install.png)

## Verify Installation

Once the `python-dotenv`, `asyncio`, and `streamz` modules are downloaded and installed, verify that both installations completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `asyncio` and `python-dotenv` libraries installed successfully.

  ```shell
  pip list | grep -E "asyncio|python-dotenv"
  ```

  ![asyncio-verify](Images/asyncio-verify.png)

* Use the `conda list` function with a `grep` argument to identify if the `streamz` library installed successfully.

  ```shell
  conda list | grep streamz
  ```

  ![streamz-verify](Images/streamz-verify.png)

## Troubleshooting

It can be frustrating when packages do not install correctly, therefore use the below approaches to troubleshoot any installation or usage issues.

### Update Conda Environment

An out-of-date Anaconda environment can create issues when trying to install new packages. Follow the below steps to update your conda environment.

1. Deactivate your current conda environment. This is required in order to update the global conda environment. Be sure to quit any running applications, such as Jupyter, prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update conda.

    ```shell
    conda update conda
    ```

3. Create a fresh conda environment to use with `python-dotenv`, `asyncio`, and `streamz`.

    ```shell
    conda create -n algotrading python=3.7 anaconda
    ```

5. Activate the new environment.

    ```shell
    conda activate algotrading
    ```

5. Install the `python-dotenv`, `asyncio`, and `streamz` packages.

    ```shell
    pip install python-dotenv
    ```

    ```shell
    pip install asyncio
    ```

    ```shell
    conda install -c conda-forge streamz
    ```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
