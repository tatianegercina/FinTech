### 16. Students Do: Mapping Adventures (20 mins)

Students repeat the steps demonstrated by the instructor in order to create their own PlotLy/MapBox scatter plots. Students will integrate Plotly and MapBox to create their first geographical visualizations.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/dataset/areas-of-interest-gis).

**Instructions:**

* [README.md](Activities/16-Stu_Mapping_Adventures/README.md)

**Files:**

* [mapping_adventures.ipynb](Activities/16-Stu_Mapping_Adventures/Unsolved/Core/mapping_adventures.ipynb)

### 17. Instructor Do: It's a Map Plot Activity Review (10 mins)

This review activity will consist of two parts. The first part will be a dry walk through of the Mapping Adventures student assignment. The second will consist of a facilitated discussion/student presentation of the top places they'd go to for Harold's birthday.

**Files:**

* [mapping_adventures.ipynb](Activities/16-Stu_mapping_adventures/Solved/Core/mapping_adventures.ipynb)

Open the solution and conduct a dry walk through:

* The marriage between Plotly Express and Mapbox has enabled developers to create interactive map visualizations.

* Using Mapbox's API, Plotly can render geographic plots, such as the **scatter mapbox** plot. The **scatter mapbox** plot is the classic scatter plot overlayed on top of a map.

  ![plotting_adventures.gif](Images/plotting_adventures.gif)

* The **scatter mapbox** plot can be created using the `scatter_mapbox` function. The function has three key parameters: DataFrame, **latitude** field, and **longitude** field. **Color** is also an acceptable argument, which accepts a DataFrame column as its value.

  ![scatter_mapbox.png](Images/scatter_mapbox.png)

Next, transition into the presentation portion of the review.

* Ask if there are any students who would like to present the three places they'd choose to go to. If no one volunteers, go around the room round robin.

  * **Answer** Prospect park, botanic garden, and botanic garden.

Ask for any remaining questions before moving on.
