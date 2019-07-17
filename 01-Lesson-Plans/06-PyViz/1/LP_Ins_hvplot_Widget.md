### 15. Instructor Do: hvplot Widgets (10 mins)

By the end of this activity, students and instructor will have deep dived into the different interactions possible with hvPlots. While students may have used some of the widgets already, this activity will serve as a formal review of each button and interaction.

**Files:**

* [Slides]()

* [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Explain to students plot interactions all happen with the hvPlot widget bar.

* The widget bar includes several buttons for different user interactions.

* The widget bar will be present for all plots created using the `hvplot` function.

  ![hvplot_widget.png](Images/hvplot_widget.png)

Transition into a demo of the widget bar by opening the solution file, and highlighting the following:

* The hvPlot widget bar gives users the ability to choose how they want to interact with the data.

* The widgets bar includes buttons for the following interactions:

  * Panning

  * Box Zoom

  * Wheel Zoom

  * Save visualization

  * Hover

* Panning allows users to move the data on the screen in all directions. This is particularly valuable when trying to view dat across time, outlying data points, or even high volume. Instead of having to zoom out to see all data, panning brings data into the forefront of the visualization as needed.

  ![hvplot_pan.gif](Images/hvplot_pan.gif)

* The box zoom interaction zooms into data points based off of a selection drawn.

  ![hvplot_box_zoom.gif](Images/hvplot_box_zoom.gif)

* Wheel zoom works similar to box zoom; however, the click wheel is used magnify data points.

  ![hvplot_wheel_zoom.gif](Images/hvplot_wheel_zoom.gif)

* Another way to interact with visualizations is to save them. hvPlot allows visualizations to be saved as html documents for later use.

  ![hvplot_save.gif](Images/hvplot_save.gif)

* Hovering is also a key interaction. Hovering over a value in a visualization shows the actual value for that data point.

  ![hvplot_hover.gif](Images/hvplot_hover.gif)

* hvPlot also includes a reset widget button, which resets all visualization interactions. If the visualization was previously zoomed in at 110%, the reset will bring the zoom percentage back to 100%.

  ![hvplot_reset.gif](Images/hvplot_reset.gif)

* Lastly, explain to students that widget activities can be combined. Clicking pan, wheel, and hover buttons enables users to pan, zoom, and get details by hovering all at the same time.

  * Note to students that certain widgets cannot be used with other widgets. For example, users cannot pan and box zoom at the same time. One action has to occur first, and then the second widget option can be chosen.

  ![hvplot_all_actions.png](Images/hvplot_all_actions.gif)

Ask if there are any questions, and then continue to the student activity.
