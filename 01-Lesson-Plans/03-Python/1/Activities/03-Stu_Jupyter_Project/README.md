# Create a JupyterLab Project

In this activity, you will create a project in JupyterLab and execute a Python `hello world` print statement in a Jupyter Notebook. 

## Background

Congratulations! You've been hired by a large financial investment analytics firm, and today is your first day. Your manager has asked you to test out the status of the newly installed JupyterLab environment to ensure its functionality.

In order to test that the environment is working as expected, you will need to create a project in JupyterLab and execute a Python `hello world` print statement in a Jupyter Notebook.

## Instructions

Using JupyterLab, walk through the following steps:

* Create a folder called `Jupyter-Workspace`. 

* Navigate to the `Jupyter-Workspace` folder.

* Click the **Text File** button to create a text file called `hello_world.txt`. 

* Create a Python Jupyter Notebook. 

* Type the following line of code into the notebook: 

    ```python
    print("Hello World")
    ```

* Click **Run**. 

## Bonus 

Create a text file in your `Jupyter-Workspace` directory. In this file, input a message that states whether or not the environment is up and running by following these steps:

* Create a new launcher. 

* Open a terminal.

* Identify the current directory: 

    ```shell
    pwd
    ```

* Change directories into `Jupyter-Workspace`: 

    ```shell
    cd Jupyter-Workspace
    ```

* List the files in the directory: 

    ```shell
    ls
    ```

* Echo "JupyterLab is up and running" into a text file named `jupyter_test.txt`: 


    ```shell
    echo 'Jupyter is up and running' > jupyter_test.txt
    ```

* Output the contents of `jupyter_test.txt` to the screen: 

    ```shell
    cat jupyter_test.txt
    ```

## Hints

* If you need help working in the JupyterLab environment, read the [documentation](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#) to learn more.

* Remember, a Jupyter Notebook is a web-based interactive development environment that allows users to code, execute programs and scripts, and create visualizations and documents. Notebooks can be configured to execute Python code, as well as Scala, R, and a number of other programming languages.