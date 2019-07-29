### 5. Students Do: Plotting with Plotly (10 mins)

Students complete a MSMD activity where they create **scatter** plots using **Plotly Express**. This activity will reinforce to students that while **Plotly Express** has the same plotting APIs as other technologies, **Plotly Express'** provides their own flavor and twist.

**Instructions:**

* [README.md](Activities/05-Stu_Plotting_w_Plotly/README.md)

**Files:**

* [plotting_w_plotly.ipynb](Activities/05-Stu_Plotting_w_Plotly/Unsolved/Core/plotting_w_plotly.ipynb)

### 6. Instructor Do: Plotting with Plotly Activity Review (5 mins)

Students and instructor participate in a dry walk through of the solution for the previous activity.

**Files:**

* [plotting_w_plotly.ipynb](Activities/05-Stu_Plotting_w_Plotly/Solved/Core/plotting_w_plotly.ipynb)

Open the solution, and conduct a dry walk through.

* **Plotly Express** can be used to create **scatter** plots. This can be done by making a call to the `scatter` function.

  ```python
  # Read in data
  foreclosures = pd.read_csv('../../Resources/alleghany_foreclosures.csv', infer_datetime_format= True,
                            parse_dates=True, index_col='filing_date')

  # Slice data and group
  foreclosures_grp = foreclosures[['municipality','amount']].groupby([foreclosures.index.year,'municipality']).count().reset_index()
  foreclosures_grp.head()

  # Create scatter plot
  px.scatter(foreclosures_grp, x='municipality', y='amount', color='filing_date')
  ```

    ![plotly_example_scatter.png](Activities/05-Stu_Plotting_w_Plotly/Images/plotly_example_scatter.png)

Explore the data with the students. Encourage students to follow along and complete the same interactions.

* Zoom in on the municipalities with the highest number of foreclosures.

  ![explore_highest_foreclosures.gif](Images/explore_highest_foreclosures.gif)

* Zoom in on the City of Clairton data points. Use the box select widget to highlight only the City of Clairton data (which will also fade out any other data points reflected at the time). Deep dive into the data for 2014.

  * Communicate to students that the City of Clairton data for 2014 could be considered an outlier or data quality issue. Interactive visualizations allow users to get a closer look into outlying data points, which could communicate a need for further investigation/data exploration to better understand the outlier.

  * Without the ability to interact with data points via technologies like **Plotly Express**, spotting outliers could be like spotting a needle in a haystack. The process would be less efficient and arguably less effective.

  ![explore_outlier.gif](Images/explore_outlier.gif)

Ask for any remaining questions before moving on.
