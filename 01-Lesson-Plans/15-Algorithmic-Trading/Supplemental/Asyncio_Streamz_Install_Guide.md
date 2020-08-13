# Asyncio & Streamz Installation Guide

This guide serves as a step by step process for setting up and validating the asyncio. Without this library, class activities and their associated code will not be able to perform the necessary operations for asynchronous programming.

All packages should be installed into the `algotrading` virtual environment.  If you have not already created an `algotrading` virtual environment you can do so by typing the following commands in your terminal:

  ```shell
  conda create -n algotrading python=3.7 anaconda
  ```


## Installation

Open a terminal, and execute the following commands to install `asyncio`.

* Activate your `algotrading` virtual environment.

  ```shell
  conda activate algotrading
  ```

* Use the `pip install` command to download the `asyncio` module.

  ```shell
  pip install asyncio
  ```

  ![asyncio-install](Images/asyncio-install.png)

**Note** For additional functionality you could also install the `streamz` library. Streamz allows for real-time data streamining to our existing dashboards.

* Use the `conda install` command to download the `streamz` module.

  ```shell
  conda install -c conda-forge streamz
  ```

  ![streamz-install](Images/streamz-install.png)

## Verify Installation

Once the `asyncio` and `streamz` modules are downloaded and installed, verify that both installations completed successfully.

* Use the `conda list package_name` command, substituting `package_name` with `asyncio` to identify if the `asyncio` library installed successfully.

  ```shell
  conda list asyncio
  ```

  ![asyncio-verify](Images/asyncio-verify.png)

* Use the `conda list package_name` command, substituting `package_name` with `streamz` to identify if the `asyncio` library installed successfully.

  ```shell
  conda list streamz
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

3. Remove the virtual environment.

    ```shell
    conda env remove --name algotrading
    ```

4. Create a fresh conda environment to use with `asyncio` and `streamz`.

    ```shell
    conda create -n algotrading python=3.7 anaconda
    ```

5. Activate the new environment.

    ```shell
    conda activate algotrading
    ```

6. Install the `asyncio` and `streamz` packages.

    ```shell
    pip install asyncio
    ```

    ```shell
    conda install -c conda-forge streamz
    ```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
