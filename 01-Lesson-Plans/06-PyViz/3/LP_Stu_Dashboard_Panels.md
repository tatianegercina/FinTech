### 8. Student Do: The Judge's Panel (15 mins)

Students complete a Find the Path activity where they execute insert, update, and remove operations on Panel **panels**.

Since students have not been taught how to manipulate **panels** using insert, update, and remove functions, make sure to circulate with TAs to provide assistance. Also encourage students to work together pairs of two.

**Instructions:**

* [README.md](Activities/08-Stu_Dashboard_Panels/README.md)

**Files:**

* [judges_panel.ipynb](Activities/08-Stu_Dashboard_Panels/Unsolved/judges_panel.ipynb)

### 9. Instructor Do: Judge's Panel Activity Review (10 mins)

**Files:**

* [judges_panel.ipynb](Activities/08-Stu_Dashboard_Panels/Solved/judges_panel.ipynb)

Open the solution and explain the following:

* **Rows**, **columns**, and **tabs** are used to create a dashboard layout in Panel. Media/content can be added to each of these objects using the standard Python list functions, such as `append`.

* Row objects insert content into a horizontal container, allowing each object to be placed adjacent to the other. The `pn.Row` function can be used to create this horizontal container.

  ```python
  # Put parallel plots in a single row
  row_of_parallel = pn.Row(parallel_categories, parallel_coordinates)
  ```

  ![panel_row.png](Images/panel_rows.png)

* Column objects store content into a vertical container. Column panels work just like **row** objects, except data is stored vertically rather than horizontally.

  ```python
  # Insert row_of_parallel and row_of_Bar into a column object with Markdown text
  plots_as_column = pn.Column("# Alleghany Real Estate Dashboard", row_of_parallel, row_of_bar)
  plots_as_column
  ```

  ![panel_column.png](Images/panel_columns.png)

* Tab objects allow media/content to be segmented into different views. Tabs are a key feature that allow dashboards to have more than one report. Each tab can be considered a report or view, and each view can have its own reporting/analytic approach for gaining insights.

  ```python
  # Create tabs
  tabs = pn.Tabs(
      ("All Plots", plots_as_column),
      ("General Plots", row_of_bar),
      ("Statistical Plots", row_of_parallel)
  )
  tabs
  ```

  ![panel_tab.gif](Images/panel_tab.gif)

Ask for any remaining questions before moving on.

- - -

### 10. BREAK (40 mins)

- - -
