### 6. Student Do: No Pane, No Gain (15 mins)

In this activity, students complete a MSMD activity where they create a Plotly plot and convert it to a Panel **pane**. The goal of this activity is to reinforce to students the importance of Panel **panes** and their role in the dashboard creation process.

**Instructions:**

* [README.md](Activities/06-Stu_Dashboard_Components/README.md)

**Files:**

* [no_pane_no_gain.ipynb](Activities/06-Stu_Dashboard_Components/Unsolved/Core/no_pane_no_gain.ipynb)

### 7. Instructor Do: No Pane, No Gain Activity Review (10 mins)

The instructor will conduct a dry walk through of the solution to highlight the different approaches that can be taken to create a **pane** object.

**Files:**

* [no_pane_no_gain.ipynb](Activities/06-Stu_Dashboard_Components/Solved/no_pane_no_gain.ipynb)

Open the solution, and explain the following:

* There are two ways in which a Panel **pane** can be created. One way is to use panel helper functions like `interact` and `panel.panel`, which converts media types to Panel **panes**. `interact` does this specifically so that it can create an interactive widget.

  * Ask students the following question: What is the purpose behind the `interact` function? What does it do?

    * **Answer** The `interact` function creates an interaction sliding widget that serves as a way for users to customize data presented on a plot. The `interact` widget is an alternative to hardcoding argument values, and it serves as separate mechanism for getting user input.

  * In order for panel to create the interaction widget, it has to convert the plot to a **pane** object. The `interact` function handles this conversion behind the scenes.

  ```python
  # Use interact function to create interaction widget
  interact(create_parallel_categories_plot, number_of_records=30)
  ```

  ![panes_with_interact.gif](Images/panes_with_interact.gif)

* Another method used to create Panel **panes** is to use the media specific pane functions (i.e. panel.pane.Plotly). These functions will execute a process dedicated to converting that media type into a Panel **pane**.

  ```python
  # Use panel.pane.Plotly function to convert plot to pane
  plot_panel = pn.pane.Plotly(create_parallel_categories_plot(30))
  plot_panel
  ```

  ![panel_pane_plotly.png](Images/panel_pane_plotly.png)

* To confirm the **pane** type, the Panel `pprint` function can be used. The function will return the **pane** type (i.e. Plotly figure).

  ```python
  # Check the pane type using the pprint() function
  plot_panel.pprint()
  ```

  ![pprint.png](Images/pprint.png)

* Explain that an alternative to using the media specific pane function is to use the `pn.panel` helper function. Plots and other media types are passed to this function as arguments. The function will then infer the type of **pane** to create.

Ask for any remaining questions before moving on.
