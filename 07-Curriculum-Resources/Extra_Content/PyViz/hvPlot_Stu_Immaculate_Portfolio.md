### 19. Student Do: The Immaculate Portfolio (20 mins)

For the final activity, students will take everything they've learned in the day and use it to enhance their current REMAX portfolio with more sophisticated and statistics related visualizations (i.e. **scatter** and **area** plots).

Communicate to students that they should work together on this activity; however, each student will need to complete their own notebook.

Also, let students know that the review activity will consist of student volunteers presenting their notebooks to the class. Indicate that the first two students to finish early will have the option to volunteer.

* Ask the first volunteer to focus the review on the approach taken to create **scatter** and **area** plots, as well as how the plots should be analyzed.

* Ask the second volunteer to present on the customizations made to brand the portfolio as their own. Let this student know that depending on time, the presentation may not be required.

Have TAs circulate to provide assistance to students facing challenges.

**Instructions:**

* [README.md](Activities/11-Stu_Immaculate_Portfolio/README.md)

**Files:**

* [immaculate_portfolio.ipynb](Activities/11-Stu_Immaculate_Portfolio/Unsolved/immaculate_portfolio.ipynb)

### 20. Instructor Do - Immaculate Portfolio Activity Review (5 mins)

This review activity will be facilitated by the instructor but led by the students. Two student volunteers will be asked to present their portfolio to the class.

**Files:**

* [immaculate_portfolio.ipynb](Activities/11-Stu_Immaculate_Portfolio/Solved/immaculate_portfolio.ipynb)

Begin the review activity by asking one of the two student volunteers to present their portfolio. Have the students open the solution and highlight the following:

* **Scatter** plots are used to visualize the relationship between two data points/variables. **Scatter** plots enable viewers to assess the relationship and effect one variable has on another.

  ```python
  # Read in loan data
  loan_data = pd.read_csv("../Resources/state_loan_data.csv")

  # Create scatter plot
  correlation_data = loan_data[['2017','2015 * 2016']]

  correlation_data.reset_index().hvplot.scatter(
    y='2017',
    x='2015 * 2016',
    c='State Code',
    xformatter='%.0f',
    yformatter='%.0f',
    title='Correlation of 2015 * 2016 & 2017 Average Loan Amounts'
  )
  ```

  ![scatter_comparison.png](Images/scatter_comparison.png)

* **Area** plots are best suited at graphically portraying the change in data over time as it relates to other data elements/variables. **Area** plots are commonly used whenever time series or data changes over time are of importance. Because **area** plots focus on **time**, a time dimension is needed in the data.

  ```python
  # Data for area plot
  tri_state_loan_data = pd.DataFrame({
      "NJ": loan_data.loc['NJ'],
      "PA": loan_data.loc['PA'],
      "DE": loan_data.loc['DE']
  }).loc[['2010 * 2014','2015 * 2016','2017']]

  # Create area plot
  tri_state_loan_data.hvplot.area(
    stacked=False,
    yformatter='%.0f',
    title='Tri-State Region Average Loan Amounts'
  )
  ```

  ![area_progression.png](Images/area_progression.png)

If time remains, ask the second volunteer to present. Ask the second volunteer to focus in on their approach to customizing the visualizations. Guide the presentation by asking the following questions:

* What types of visualization changes did you make?

  * Added axes label rotation

  * Changed color scheme

  * Formatted labels

* When should you use the customization attributes (i.e. xlabel) vs. `opts` function (i.e opts(xlabel=))?

  * **Answer** Customization attributes can be used as the plot is being declared. The `opts` function should be used if the plot has already been instantiated.

Ask for any remaining questions before moving on.
