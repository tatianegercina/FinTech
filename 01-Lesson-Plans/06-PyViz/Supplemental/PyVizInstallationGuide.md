# PyViz Installation Guide

PyViz is a Python visualization package that provides a single platform to access multiple visualization packages, including Matplotlib, Plotly Express, hvPlot, Panel, D3.js, etc.

Follow the below steps to install and setup PyViz in your Python environment. These steps should be completed outside of class.

1. Download the PyViz dependencies **nodejs** and **npm** (included in nodejs).

    ```shell
    conda install -c conda-forge nodejs
    ```

2. Use the `conda install` command to install the following packages: hvPlot, Plotly Express, and Panel.

    ```shell
    conda install -c pyviz hvplot
    conda install -c plotly plotly
    conda install -c pyviz panel
    ```

3. PyViz installation also requires installation of Jupyter Lab extensions. These extensions are used to render PyViz plots in Jupyter Lab. Execute the below commands to install the necessary Jupyter Lab extensions for PyViz and Plotly Express.

    ```shell
    jupyter labextension install @pyviz/jupyterlab_pyviz
    jupyter labextension install @jupyterlab/plotly-extension
    ```

4. Use the `conda list | grep pyviz` function to confirm installation of all PyViz packages. Look for `hvplot`, `panel`, and `pyviz_comms`.

    ```shell
    conda list | grep pyviz
    ```

    ```
    hvplot                    0.4.0                      py_0    pyviz
    panel                     0.6.0                      py_0    pyviz
    pyviz_comms               0.7.2                      py_0
    ```

5. Use the `conda list | grep plotly` function to confirm all Plotly packages are available. Confirm `plotly` and `plotly express` are listed.

  ```shell
  conda list | grep plotly
  ```

  ```
  plotly                    4.0.0                      py_0
  plotly_express            0.4.0                      py_0    plotly
  ```

Now you're all set to get started creating visual masterpieces using PyViz technologies!





© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.