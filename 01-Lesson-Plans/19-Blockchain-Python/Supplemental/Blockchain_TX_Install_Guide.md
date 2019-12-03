# Blockchain Transactions Install Guide

This guide serves as a step by step process for setting up and validating the `web3.py`, `bit`, and `hd-wallet-derive` libraries used to programmatically send and receive transactions over a blockchain network via virtual wallets. Without these libraries, class activities and their associated code will not be able to perform the necessary operations.

## Installation

Open a terminal and execute the following commands to install `web3.py` and `bit`, respectively.

* Use the `pip install` command to download the `web3.py` module.

  ```shell
  pip install web3
  ```

  ![web3-install](Images/web3-install.png)

* Use the `pip install` command to download the `bit` module.

  ```shell
  pip install bit
  ```

  ![bit-install](Images/bit-install.png)

## Verify Installation

Once the `web3.py` and `bit` modules are downloaded and installed, verify that both installations completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `web3` library installed successfully.

  ```shell
  pip list | grep web3
  ```

  ![web3-verify](Images/web3-verify.png)

* Use the `conda list` function with a `grep` argument to identify if the `bit` library installed successfully.

  ```shell
  pip list | grep bit
  ```

  ![bit-verify](Images/bit-verify.png)

## Troubleshooting

It can be frustrating when packages do not install correctly, therefore use the below approaches to troubleshoot any installation or usage issues.

### Install Microsoft Visual C++ Build Tools

In some cases, the `Web3.py` library may fail to install due to the need for Microsoft Visual C++ Build Tools. In such an event, following the below steps to resolve the issue:

1. Go to: https://visualstudio.microsoft.com/downloads/

2. Scroll down the page and click on "Tools for Visual Studio 2019" to reveal the sub-options.

3. Download the "Build Tools for Visual Studio 2019" package.

    ![vs-build-tools](Images/vs-build-tools.png)

4. Run the package file and select the C++ build tools option. Then click install.

5. This process takes about 15 minutes

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

3. Create a fresh conda environment to use with `web3` and `bit`.

    ```shell
    conda create -n ethereum python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate ethereum
    ```

5. Install the `web3` and `bit` packages.

    ```shell
    pip install web3
    ```

    ```shell
    pip install bit
    ```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.