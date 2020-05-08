# Unit 5 - Installation Guide

In this Unit, you will learn how to use the following FinTech APIs and their software development kits (SDKs) for the Python language.

* [Quandl](https://www.quandl.com/)

* [Plaid](https://plaid.com/)

* [Alpaca](https://alpaca.markets/)

This guide serves as a step by step process for setting up and validating all the libraries needed to interact with these APIs. Without these libraries, you will not be able to follow the activities in class.

Remember to activate your virtual environment before start the installation process or create a brand new virtual environment.

## Installing `python-dotenv`

The `python-dotenv` library allows you to read key-value pairs from a `.env` file and adds them as environment variables.

You can install this library running the following command in your terminal:

```shell
pip install python-dotenv
```

## Installing the `plaid-python` SDK

Plaid is a service that allows you to analyze personal financial data. The `plaid-python` SDK will allow you to interact with the Plaid API.

You can install this library running the following command in your terminal:

```shell
pip install plaid-python
```

## Installing the `alpaca-trade-api` SDK

Alpaca is an API for stock trading. The `alpaca-trade-api` SDK will allow you to interact with Alpaca.

You can install this library running the following command in your terminal:

```shell
pip install alpaca-trade-api
```

## Verify Installation

Once the installations are complete, verify the process completed successfully.

Use the `pip list` function with a `grep` argument to identify if all the libraries installed successfully.

```shell
pip list | grep -E "python-dotenv|plaid-python|alpaca-trade-api"
```

![libraries_verify](Images/libraries_verify.png)

## Set `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` Environment Variables

To use the Alpaca trade SDK, you will need to set your `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` environment variables before using the library, as Alpaca communicates with the Alpaca API.

Go to [Alpaca Markets](https://app.alpaca.markets) and login to your account. After logging in, you will be taken to a page that looks like this and will probably display a form asking you for personal information. **YOU DO NOT NEED TO ENTER THIS INFORMATION**

![SSN_NOT_REQUIRED](Images/SSN_NOT_REQUIRED.png)

Now, click the `Go to Paper Account` link in the navigation sidebar.

  ![alpaca-token](Images/alpaca_go_to_paper.png)

Now click on the `Your API Keys` section and grab your `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`.

  ![alpaca-token](Images/alpaca-token.png)

Next, open or create a new `.env` file where you will store your keys and use the following syntax.

**Note**: Make sure your environment variables are specifically named `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`.

  ![alpaca-token-verify](Images/alpaca-env.png)

Save this file in the same folder as your python script or Jupyter notebook file. If the file is not already created save it as `.env`.

  ![alpaca-env-save](Images/alpaca-env-save.png)

  ![env-folder](Images/env-folder.png)

## Set the Plaid Keys as Environment Variables

To get your Plaid keys, first sign up for a new account by registering yourself in [this link](https://dashboard.plaid.com/signup).

![plaid_signup](Images/plaid_signup.png)

Once you created your account, navigate to [the Plaid dashboard](https://dashboard.plaid.com/overview), click on the "Team Settings" option of the main menu and choose the "Keys" option.

![open_plaid_keys](Images/open_plaid_keys.png)

Copy the `client_id`, `public_key`, and the `Sandbox` secret and paste them as variables in your `.env` file as follows:

```text
PLAID_CLIENT_ID="YOUR_CLIENT_ID"
PLAID_PUBLIC_KEY="YOUR_PUBLIC_KEY"
PLAID_SECRET="YOUR_SANDBOX_SECRET"
```

## Enabling Hidden Files

To work with `.env` files on your machine, you will need to be able to view hidden files on your computer.

* Windows

  * Type `folder` in the search bar.

  * Select `File Explorer Options`.

  * Click the `View` tab in the pop up box, then click `Show hidden files, folders and drives` as shown below:

  ![Windows-hidden-files](Images/Windows-hidden-file.png)

* Mac OSX

  * Open Finder

  * Press `Command + Shift + Dot`

* Linux (Ubuntu)

  * Open your file manager

  * Press `Ctrl + H`

## Usage

Lastly, run `jupyter-lab`. You may have to restart `jupyter-lab` if it is already running in the terminal for `jupyter-lab` to re-scan the environment for new variables.

## Troubleshooting

It can be frustrating when packages do not install correctly, therefore use the below approaches to troubleshoot any installation or usage issues.

### Update Conda Environment

An out-of-date Anaconda environment can create issues when trying to install new packages. Follow the steps below to update your Conda environment.

1. Deactivate your current Conda environment. This is required to update the global Conda environment. Be sure to quit any running applications, such as Jupyter, before deactivating the environment.

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

5. Install the libraries following the steps explained above.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
