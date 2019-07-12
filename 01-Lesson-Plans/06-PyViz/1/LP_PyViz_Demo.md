### 7. Instructor Do - PyViz Demo (10 minutes)

By the end of this activity, students will have a solid understanding of how to install PyViz and import it into a development environment.

**Files**

* [Slides]()

* [PyViz Installation Guide]()

Navigate to the 6.1 slides, and highlight the following:

* As an ecosystem, PyViz had a number of packages that can be used to create data visualizations.

* Each of the technologies in the ecosystem are accessed with the PyViz package. They don't have to be installed individually.

* In order to get access to these packages, the PyViz package has to be downloaded and installed correctly.

  ![pyviz_ecosystem.png](Images/pyviz_ecosystem.png)

Transition to the live walkthrough, and highlight the following:

* It's important to ensure the conda environment is up to date before installing PyViz and its dependencies. This will ensure version compatability.

  ```shell
  conda update conda
  conda update anaconda
  ```

* Indicate to students that compatability errors might be thrown if the environment is not updated to the latest version first.

* Once the Anaconda env has been updated, the PyViz dependencies will need to be downloaded. This includes nodejs5 and dpm.

  ```shell
  pip install nodejs
  pip install npm
  ```

* The actual PyViz packages will need to be installed after all dependencies have been acquired. The key packages are Plotly Express and Panel.

  ```shell
  conda install -c plotly_express
  conda install -c pyviz panel
  ```

* After the package have been installed, the Jupyter extensions need to be set up as well. Installing these extensions will ensure the interactive visualizations are accessible and viewable in JupyterLab.

  ```shell
  jupyter labextension install @jupyterlab/plotly-extension
  jupyter labextension install @pyviz/jupyterlab_pyviz
  ```

Ask students if they have any questions before moving forward.
