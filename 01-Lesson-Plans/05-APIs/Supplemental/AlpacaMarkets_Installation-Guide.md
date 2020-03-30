# Alpaca Markets (python-sdk) Installation Guide

This guide serves as a step by step process for setting up and validating the `Alpaca Markets trade API` Python SDK. Without this library, class activities and code will not be able to extract historical stock data and therefore, will not be able to be completed.

## Install

In order to install the `alpaca-trade-api` package, all of the dependencies must be satisfied. The dependencies list can be found below for reference.

* Pandas

* Requests

Open a terminal and execute the following command to install `alpaca-trade-api`.

* Use the `pip install` command to download the `alpaca-trade-api` module.

  ```shell
  pip install alpaca-trade-api
  ```

  ![alpaca_install.png](Images/alpaca_install.png)

## Verify Installation

Once the `alpaca-trade-api` download is complete, verify the installation completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `alpaca-trade-api` library installed successfully.

  ```shell
  pip list | grep alpaca-trade-api
  ```

  ![alpaca_verify](Images/alpaca-verify.png)

## Set ALPACA_API_KEY and ALPACA_SECRET_KEY environment variables

In order to use the Alpaca trade SDK, you will need to set your `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` environment variables prior to using the library, as Alpaca communicates with the Alpaca API.

Go to [Alpaca Markets](https://app.alpaca.markets) and login to your account. After logging in click the `Go to Paper Account` link in the navigation sidebar.

  ![alpaca-token](Images/alpaca_go_to_paper.png)

Now click on the `Your API Keys` section and grab your `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`.

  ![alpaca-token](Images/alpaca-token.png)

Next, open or create a new `.env` file where you will store your keys and use the following syntax.

**Note**: Make sure your environment variables are specifically named `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`.

  ![alpaca-token-verify](Images/alpaca-env.png)

Save this file in the same folder as your python script or jupyter notebook file. If the file is not already created save it as `.env`.

  ![alpaca-env-save](Images/alpaca-env-save.png)

  ![env-folder](Images/env-folder.png)

## Enabling Hidden Files

To work with `.env` files on your machine you will need to be able to view hidden files on your machine.

  * Windows

    * Type `folder` in search bar.
    * Select `File Explorer Options`.
    * Click the `View` tab in the pop up box, then click `Show hidden files, folders and drives` as shown below:

    ![Windows-hidden-files](Images/Windows-hidden-file.png)

  * Mac OSX

    * Open Finder

    * Press Command + Shift + Dot

  * Linux (Ubuntu)

    * Open your file manager

    * Press Ctrl + H

## Usage

Lastly, run `jupyter-lab`. You may have to restart `jupyter-lab` if it is already running in the terminal in order for `jupyter-lab` to re-scan the environment for new variables.

## Troubleshooting

It can be frustrating when packages do not install correctly, therefore use the below approaches to troubleshoot any installation or usage issues.

### Update Conda Environment

An out-of-date Anaconda environment can create issues when trying to install new packages. Follow the steps below to update your conda environment.

1. Deactivate your current conda environment. This is required in order to update the global conda environment. Be sure to quit any running applications, such as Jupyter, prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update conda.

    ```shell
    conda update conda
    ```

3. Create a fresh conda environment to use with alpaca.

    ```shell
    conda create -n alpacaenv python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate alpacaenv
    ```

5. Install the **alpaca-trade-api** package.

    ```shell
    pip install alpaca-trade-api
    ```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
