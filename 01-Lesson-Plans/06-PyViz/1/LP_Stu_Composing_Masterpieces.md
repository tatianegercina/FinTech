### 16. Students Do: Composing Masterpieces (10 mins)

Students will complete a MSMD activity where they use the information learned in the instructor demo to customize their hvPlots. Students will use a range of options to customize the color, labels, and axis alignments.

Circulate through the room while students are completing the activity. Look to identify a student who completes the activity first or who seems to be helping peers. Ask this student if they'd like to volunteer and do a dry walk through activity session.

Encourage students who finish early to help their classmates with one-on-one troubleshooting.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/usda-rural-development-single-family-section-502-direct-active-loans-by-congressional-dist).

**Instructions:**

* [README.md](Activities/16-Stu_Composing_Masterpieces/README.md)

**Files:**

* [composing_masterpieces.ipynb](Activities/16-Stu_Composing_Masterpieces/Unsolved/composing_masterpieces.ipynb)

### 17. Instructor Do: Composing Masterpieces Activity Review (5 mins)

The instructor will ask a student volunteer to conduct a dry walkthrough of the Composing Masterpieces solution.

**Files:**

* [composing_masterpieces.ipynb](Activities/16-Stu_Composing_Masterpieces/Solved/composing_masterpieces.ipynb)

Initiate the review session by asking the first student who completed the student solution to conduct a dry walkthrough. If no student was identified to perform the walkthrough, conduct a dry walkthrough yourself. If the student needs assistance facilitating the review, ask guided questions such as:

* How many different ways can you compose plots? What are the operators?

  * **Answer** Two. `+` and `*`.

* What does the `+` operator do?

  * **Answer** Create a layout where each plot is placed adjacent to one another.

* What does the `*` operator do?

  * **Answer** Overlay plots where each plot is placed along the same axis.

* How many widget bars are created when plotting? One, or one for each plot?

  * **Answer** One.

Indicate to the student to open the solution. The student should highlight the following. Use the above guided questions to help facilitate the review session, when needed.

* The `+` operator is used to compose plots adjacent to one another. This creates a single plot that contains more than one visualization.

  ```python
  # Slice data for Total Average Loan Amount by 2015-2016 and 2010-2014 date ranges
  loan_data_range_1 = loan_data['2015 - 2016']
  loan_data_range_2 = loan_data['2010 - 2014']
  loan_data_range_grp = loan_data_range_1.sort_values()
  loan_data_range_grp_2 = loan_data_range_2.sort_values()

  # Plot data for date ranges
  plot_2015_2016 = loan_data_range_grp.hvplot(label='2015 - 2016')
  plot_2010_2014 = loan_data_range_grp_2.hvplot(label='2010 - 2014')

  # Compose plots
  plot_2015_2016 + plot_2010_2014
  ```

  ![compose_layout.png](Images/compose_layout.png)

* The `*` operator is used to overlay plots along the same axis. This results in one plot with multiple subplots rather than plots that are adjacent to another (like when using the `+` operator).

  ```python
  # Overlay plots
  plot_state_avgs * plot_2015_2016 * plot_2010_2014
  ```

  ![compose_overlay.png](Images/compose_overlay.png)

* When plots are composed, only one widget menu is provided. This single menu can be used to control each of the plots.

  ![single_widget_bar.gif](Images/single_widget_bar.gif)

Ask for any remaining questions before moving on.
