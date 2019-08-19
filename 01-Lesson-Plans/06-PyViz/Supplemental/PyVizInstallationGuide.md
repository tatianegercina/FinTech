# PyViz Installation Guide

PyViz is a Python visualization package that provides a single platform to access multiple visualization packages, including Matplotlib, Plotly Express, hvPlot, Panel, d3.js, etc.

Follow the below steps to install and setup PyViz in your Python environment. These steps should be completed outside of class.

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

3. PyViz installation also requires installation of Jupyter Lab extensions. These extensions are used to render PyViz plots in Jupyter Lab. Execute the below commands to install the necessary Jupyter Lab extensions for PyViz and Plotly Express.

    ```shell
    jupyter labextension install @pyviz/jupyterlab_pyviz
    jupyter labextension install @jupyterlab/plotly-extension
    ```

4. Use the `conda list` function to confirm installation of all PyViz packages. Look for `pyviz_comms` and `panel`.

  ```shell
  conda list | grep pyviz
  ```

  ```
  panel                     0.6.0                      py_0    pyviz
  param                     1.9.1                      py_0    pyviz
  pyct                      0.4.6                      py_0    pyviz
  pyct-core                 0.4.6                      py_0    pyviz
  pyviz_comms               0.7.2                      py_0    pyviz
  ```
