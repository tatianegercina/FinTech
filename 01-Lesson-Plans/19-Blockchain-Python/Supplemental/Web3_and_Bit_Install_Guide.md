# Web3.py & Bit Installation Guide

This guide serves as a step by step process for setting up and validating the `web3.py` and `bit` Python libraries. Without these libraries, class activities and their associated code will not be able to perform the necessary operations for communicating with blockchain networks programmatically.

## Installation

Open a terminal, and execute the following commands to install `web3.py` and `bit`, respectively.

* Use the `pip install` command to download the `web3.py` module.

  ```shell
  pip install web3
  ```

  ![asyncio-install](Images/asyncio-install.png)

* Use the `pip install` command to download the `bit` module.

  ```shell
  pip install bit
  ```

  ![streamz-install](Images/streamz-install.png)

## Verify Installation

Once the `web3.py` and `bit` modules are downloaded and installed, verify that both installations completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `asyncio` library installed successfully.

  ```shell
  pip list | grep asyncio
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

3. Create a fresh conda environment to use with `asyncio` and `streamz`.

    ```shell
    conda create -n algotrading python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate algotrading
    ```

5. Install the `asyncio` and `streamz` packages.

    ```shell
    pip install iexfinance
    ```

    ```shell
    conda install -c conda-forge streamz
    ```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
