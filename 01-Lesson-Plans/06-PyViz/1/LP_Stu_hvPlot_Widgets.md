### 16. Student Do: hvPlot Widgets (10 mins)

In this activity, students will play around with the hvPlot widgets to get more accustom to the different types of interactions supported with hvPlots. Students use hvPlot visualizations to explore hospital claims data and answer a few basic questions about the data.

**Instructions:**

* [README.md](Activities/16-Stu_hvPlot_Widgets/README.md)

**Files:**

* [hvplot_widgets.ipynb](Activities/16-Stu_hvPlot_Widgets/Unsolved/hvplot_widgets.ipynb)

### 17. Instructor Do: hvPlot Widgets Activity Review (5 mins)

The instructor will lead a facilitated review section in this activity. The emphasis will be placed on what each widget does and how they can be used in conjunction with one another to deep dive into data analysis and exploration.

Data for this activity was retrieved from [data.cms.gov](https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3).

**Files:**

* [hvplot_widgets.ipynb](Activities/16-Stu_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)

Engage the students by facilitating a review discussion. Ask the following questions:

* hvPlots have 6 standard widgets. One of them is pan. What are the other 5 widgets?

  * **Answer** Box zoom, wheel zoom, save, refresh, and hover.

* What are some of the advantages of using hvPlot over a plotting API like Matplotlib or Pandas.plot?

  * **Answer** Visualizations are interactive rather than static

  * **Answer** hvPlot dynamically handles the data so that the best visualizations can be created. The `hvPlot` function figures out the best way to visualize the data, on its own. This might mean a line vs. bar plot.

* Sometimes the text on a display is hard to read. The labels can become illegible, depending on the amount of data being plotted. What's the best way to deep dive into the data and improve clarity and understanding?

  * **Answer** Use the zoom widgets. This will limit the amount of data displayed on the screen, which will magnify the x axis and y axis values. This differs from static plots because static plots would require the width of the plot to be manipulated.

  ![enlarging_text.gif](Images/enlarging_text.gif)

Ask for any remaining questions before moving on.
