# PyViz Installation Guide

PyViz is a Python visualization package that provides a single platform to access multiple visualization packages, including Matplotlib, Plotly Express, hvPlot, Panel, d3.js, etc.

Follow the below steps in order to install and setup PyViz in your Python environment. These steps should be completed outside of class.

1. Download the PyViz dependencies **nodejs** and **dpm** dependencies.

    ```shell
    conda install nodejs
    conda install npm
    ```

2. Use the `conda install` command to install the following packages: hvPlot, Plotly Express, and Panel.

    ```shell
    conda install -c pyviz hvplot
    conda install -c plotly.express
    conda install -c pyviz panel
    ```

3. PyViz installation also requires installation of Jupyter Lab extensions. These extensions are used to render PyViz plots in Jupyter Lab. THe below commands will install the necessary extensions for PyViz and Plotly Express.

    ```shell
    jupyter labextension install @pyviz/jupyterlab_pyviz
    jupyter labextension install @jupyterlab/plotly-extension
    ```
