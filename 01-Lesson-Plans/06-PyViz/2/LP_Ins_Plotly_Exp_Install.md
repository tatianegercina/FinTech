### 3. Instructor Do: Plotly Express Install (5 mins) (Critical)

TAs and students work together to ensure everyone has Plotly Express installed. In parallel, the instructor will facilitate a student led refresher activity that will recap the installation process for **Plotly Express**.

Since students should have already installed **Plotly Express** emphasis needs to be placed on providing an opportunity for troubleshooting, as well as reviewing the installation process.

**Files:**

* [PyViz Install Guide]()

Instruct TAs to circulate through the room ensure all students have **Plotly Express** installed.

* Communicate to TAs that they should provide troubleshooting for any students facing difficulties.

Engage the class with a short refresher activity. First, ask if there's a student who'd like to lead the refresher activity. Indicate to the volunteer that they should ask questions regarding the installation process of **Plotly Express**, for the Python and Jupyter Lab environments. Use the following questions to help guide the discussion, if needed.

If no one volunteers, ask the below questions yourself. Ask the students:

* What are the installation steps for **Plotly Express**?

  1. Acquire all PyViz dependencies (i.e. nodejs and npm).

  2. Execute the `pip install` or `conda install` commands for **Plotly Express**

      ```shell
      conda install -c plotly plotly_express
      ```

* What needs to be done to allow Plotly Express figures to render in Jupyter Lab?

  * **Answer** The Jupyter Lab extension needs to be installed.

      ```shell
      jupyter labextension install @jupyterlab/plotly-extension
      ```

Ask if there are any questions before moving on.
