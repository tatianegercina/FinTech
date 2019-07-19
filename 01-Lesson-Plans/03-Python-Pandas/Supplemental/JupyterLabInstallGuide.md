## JupterLab Install Guide

**Pre-requisites:**

* [Anaconda Install](AnacondaInstallGuide.md)

This guide walks through the installation and configuration process for JupyterLab.

* Verify Anaconda dev environment is activated

* Install JupyterLab

* Launch JupyterLab

Install JupyterLab

* Update the Anaconda environment to ensure the latest packages are installed.

  ```shell
  conda update conda
  conda update anaconda
  ```

* Activate Anaconda dev environment.

  ```shell
  conda activate dev
  ```

* Install JupyterLab using `conda install` command. `conda install` will connect to the JupyterLab github repository, named `conda-forge`, and download the JupyterLab package.

  ```shell
  conda install -c conda-forge jupyterlab
  ```

Launch JupyterLab

* Execute the JupyterLab launch command from the Anaconda terminal.

  ```shell
  jupyter lab
  ```

* The JupyterLab UI should open automatically. If it does not, copy and paste the URL provided in the Anaconda Terminal into an internet browser.

  ![Jupyter_Lab_Web_Url.png](Images/Jupyter_Lab_Web_Url.png)

Explore JupyterLab

* Take note of the following components of the JupyterLab interface:

  * File Explorer

  * Launcher

  * Python Notebook

  * Terminal

  * Text File Kernel
