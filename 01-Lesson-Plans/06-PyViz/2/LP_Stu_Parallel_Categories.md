### 11. Student Do: Categorical Property Evaluation (15 mins)

Students complete a MSMD activity and code out a **parallel categories** plot. Students will use the plot to visualize the dimensions/categories evaluated during real estate property assessments.

Encourage students to work in teams and collaborate on the information seeking process. Indicate that even when working in teams each student will still need to complete the activity.

* Instruct the TAs to circulate to provide the teams with any troubleshooting assistance.

Additionally, keep an eye out during the activity for students who finish early. Find a student volunteer who is wiling to present and describe the story being told by the documentation. Explain to the volunteer that they will have to present their plot to the class and tell the story of the data by interacting with the plot.

Data for this activity was acquired from [catalog.data.gov](https://catalog.data.gov/dataset/allegheny-county-property-assessments).

**Instructions:**

* [README.md](Activities/11-Stu_Categorical_Evaluation/README.md)

**Files:**

* [Categorical_Evaluation.ipynb](Activities/11-Stu_Categorical_Evaluation/Unsolved/categorical_evaluation.ipynb)

### 12. Students Do: Categorical Assessments Activity Review (5 mins)

This activity involves a student volunteering to tell the story of Alleghany property assessments. A student will present the parallel categories plot from the student activity, and provide some findings regarding dimensional patterns.

**Files:**

* [categorical_property_evaluation.ipynb](Activities/11-Stu_Categorical_Evaluation/Solved/categorical_evaluation.ipynb)

Open the solution and ask the student volunteer to present the plot and relay their findings. Use the below discussion points to help facilitate the review.

* The **parallel categories** plot is created using the `parallel_categories` function provided with **Plotly.express** package.

    ```python
    # Plot data
    px.parallel_categories(data, dimensions=['USEDESC','TOTALROOMS','BEDROOMS','FULLBATHS'], color='LOCALTOTAL')
    ```

    ![stu_parallel_categories.png](Images/stu_parallel_categories.png)

* Since **paralell categories** plots involve multidimensional analysis, dimensions can be specified using the `dimensions` attribute.

  ![stu_parallel_categories_dimensions.png](Images/stu_parallel_categories_dimensions.png)

* The line coloring of the plot can be changed using the `color` attribute. This will help spot trends in the data.

  ![stu_parallel_categories_color.png](Images/stu_parallel_categories_color.png)

If time remains, initiate the story telling piece of the review by asking the student some of the following guided questions:

* Are there any identifiable patterns at the dimension level?

  * **Answer** Most sales were single family homes

  * **Answer** Most homes have 3 bedrooms.

* How many bedrooms and full bathrooms do single family homes tend to commonly have?

  * **Answer** Three bedrooms one bath.

* What type of patterns can be seen when correlating **total number of rooms** and **bedrooms**?

  * **Answer** The homes that have evaluated at the highest local price are the ones that have twice as many total rooms as bedrooms.

  * **Answer** Housing value is more affected by **total number of rooms** and **bedrooms** than **full baths**.

* Is there an identifiable story being told through the data? What is the story?

  * **Answer** Total number of rooms, bedrooms, and bathrooms are all used to assess a property and its value. The more rooms and bedrooms, the higher the sale price. Lastly, most single family homes being assessed in Allgehany county 2019 have around 6 total rooms, 3 bedrooms, and 1 full bath.

  * **Answer** The houses evaluated at the highest costs tend to have more than 5 total rooms,
