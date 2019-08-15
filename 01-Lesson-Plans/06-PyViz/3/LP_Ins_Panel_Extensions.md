### 11. Instructor Do: Panel Extensions (10 mins)

In this activity, the instructor leads a formal lecture on Panel **extensions**. The goal of this lesson is to teach students how to leverage the best visualization features from different technologies in order to create the best dashboard possible.

**Files:**

* [Slides]()

Navigate to the 6.3 slides, and highlight the following:

* Panel supports a wide range of visualization technologies. Support for these technologies are managed by Panel **extensions**.

* Panel supports a number of extensions, including Plotly, Bokeh, and Matplotlib. Extensions give Panel the ability to display and use content created by other technologies.

* Each Panel extension has its own unique features and color schemes. There are also features that are shared across extensions. For this reason, multiple extensions may need to be specified if a dashboard leverages more than one technology (i.e. Plotly and Matplotlib).

* Panel **extensions** are specified using the `extension` function. The `extension` function will load in the corresponding plugin so that content produced by the technology can be rendered and used by Panel.

  ```python
  pn.extension('plotly')
  ```

* A list of **extensions** can be provided to the `extension` function. This will initialize each of the listed plugins and allow Panel to display the content as expected.

  ```python
  pn.extension('plotly','bokeh')
  ```

* Not all technologies require an **extension** be specified. For example, when working with Matplotlib, all that is required is a call to the `extension` function. Arguments do not have to be specified.

  ```python
  pn.extension()
  ```

* By specifying the extension, multiple media types cna be combined to create an informative and insightful dashboard.

Ask if there are any questions before continuing.
