### 8. Student Do: Plotting in Parallel (15 mins)

Students complete a bridge activity where they revisit a previously used data set that was visualized using scatter plots. Students now visualize the data using a **parallel coordinates** plot.

This will be the students' first time working with **parallel coordinate** plots. Instruct TAs to circulate to provide assistance. Encourage students who finish early to assist their classmates.

**Instructions:**

* [README.md](Activities/08-Stu_Parallel_Coordinates/README.md)

**Files:**

* [plotting_in_parallel.ipynb](Activities/08-Stu_Parallel_Coordinates/Unsolved/Core/plotting_in_parallel.ipynb)

### 9. Instructor Do: Parallel Coordinates Activity Review (5 mins)

**Files:**

* [plotting_in_parallel.ipynb](Activities/08-Stu_Parallel_Coordinates/Solved/Core/plotting_in_parallel.ipynb)

Kick off the review session by asking some of the below guided questions.

* What's the function used to create a **parallel coordinate** plot?

  * **Answer** `plotly.express.parallel_coordinates()`

* What's the difference between a **scatter plot** and **parallel coordinate** plot?

  * **Answer** **Scatter plots** visualize the relationship between two data points as an intersection. **Parallel coordinate** plots visualize the relationship between two data points as parallel axes.

  * **Answer** **Scatter plots** inherently use two axes. Whereas **parallel coordinate** are built for multivariate analysis and can have 2+ axes.

* In terms of interaction, which plot do you feel allows you to gain more value from interaction?

  * **Answer** The **parallel coordinate** plot offers limited opportunities for interaction, which makes the **scatter plot** more fitted for interacting with plots. However, **parallel coordinate** plots structurally allow for relationships to be traced more effectively and efficiently.

* What is the difference between the types of interactions provided by these different plots?

  * **Answer** **Parallel coordinate** plots can only be sorted and filtered/highlighted. **Scatter plots** can be zoomed, panned, filtered, etc.

If time remains, open the solution, and highlight the following:

* Parallel Coordinate plots present plot axes in a parallel fashion. This allows data points to be traced from one axes/variable to the next.

  * Increases and decreases can be visually spotted by the lines that connect data points to one another. This structure allows variables to be analyzed in relation to another.

  ![parallel_relationships.gif](Images/parallel_relationships.gif)

Ask for any remaining questions before moving on.
