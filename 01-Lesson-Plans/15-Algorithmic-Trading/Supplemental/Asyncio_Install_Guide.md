# Dotenv and Asyncio Installation Guide

This guide serves as a step by step process for setting up and validating the asyncio and streamz Python libraries. Without these libraries, class activities and their associated code will not be able to perform the necessary operations for asynchronous programming and data streaming, respectively.

All packages should be installed into the `algotrading` virtual environment.  If you have not already created an `algotrading` virtual environment you can do so by typing the following commands in your terminal:

  ```shell
  conda create -n algotrading python=3.7 anaconda
  ```

## Installation

In this unit, you will create some plots using `hvplot`. Also, you will use environment variables, so if you are creating a new virtual environment, be sure to follow all the steps to install all the libraries required for this unit.

Open a terminal, and execute the following commands to install `python-dotenv` and `asyncio` respectively.

* Activate your `algotrading` virtual environment.

  ```shell
  conda activate algotrading
  ```

* Use the `pip install` command to download the `python-dotenv` module.

  ```shell
  pip install python-dotenv
  ```

* Use the `pip install` command to download the `asyncio` module.

  ```shell
  pip install asyncio
  ```

* Before install the `hvplot` library, you need to install the `nodejs` package. Use the `conda install` command as follows.

  ```shell
  conda install -c conda-forge/label/main nodejs
  ```

* Use the `conda install` command to download the `hvplot` package.

  ```shell
  conda install -c pyviz hvplot
  ```

* Finally, install the PyViz JupyterLab extension to visualize `hvplot` charts in Jupyter lab.

  ```shell
  jupyter labextension install @pyviz/jupyterlab_pyviz
  ```

## Verify Installation

Once the libraries and packages are downloaded and installed, verify that all installations completed successfully.

* Use the `pip list` function with a `grep` argument to identify if the `asyncio` and `python-dotenv` libraries installed successfully.

  ```shell
  pip list | grep -E "asyncio|python-dotenv"
  ```

  ```text
  asyncio                            3.4.3
  python-dotenv                      0.14.0
  ```

* Use the `conda list` function to identify if the `hvplot` package installed successfully.

  ```shell
  conda list hvplot
  ```

  ```text
  # Name                    Version                     Build  Channel
    hvplot                    0.6.0                      py_0    pyviz
  ```

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

3. Create a fresh conda environment.

    ```shell
    conda create -n algotrading python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate algotrading
    ```

5. Install the `python-dotenv` and `asyncio` packages.

    ```shell
    pip install python-dotenv
    ```

    ```shell
    pip install asyncio
    ```

6. Install the `nodejs` package

    ```shell
    conda install -c conda-forge/label/main nodejs
    ```

7. Install the `hvplot` package.

    ```shell
    conda install -c pyviz hvplot
    ```

8. Finally, install the PyViz JupyterLab extension.

    ```shell
    jupyter labextension install @pyviz/jupyterlab_pyviz
    ```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
