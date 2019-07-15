### 11. Students Do: Plotting a Visual Takeover (15 minutes)

In this activity, students re-visit plots they made earlier in the class using Matplotlib and they re-create them as hvplots. This bridge assignment aims to demonstrate the similarities between hvplot plot API and Matplotlib's.

**Instrutions**

* [README.md](Activities/11-Stu_Visual_Takeover/README.md)

**Files**

* [visual_takeover.ipynb](Activities/11-Stu_Visual_Takeover/Unsolved/Core/visual_takeover.ipynb)

- - -

### 12. BREAK (15 minutes)

- - -

### 13. Instructor Do: Plotting a Visual Takeover Activity Review (5 minutes)

**Files:**

* [visual_takeover.ipynb](Activities/11-Stu_Visual_Takeover/Solved/Core/visual_takeover.ipynb)

Open the solution, and conduct a dry walkthrough of the solution while explaining the following:

* The hvplot library can be used to create interactive plot visualizations.

* hvplot has attributes that can be used to explicitly create line and bar plots. Otherwise, the `hvplot` function can be used.

  ```python
  # Plot a hvplot bar chart of the top 20 market cap companies
  top_20_market_cap.hvplot()
  top_20_market_cap.hvplot.line(title='Top 20 Market Cap Companies (in billions)')
  top_20_market_cap.hvplot.line(title='Top 20 Market Cap Companies (in billions)')
  ```

If time remains, transition into a small review session. Ask the following questions:

* How do hvplots differ from Panads/Matplotlib?

  * **Anwer** hvplot visualizations are interactive rather than static. THey also come equipped with widgets that allow users to manage how they want to interact with the data.

* What are example ways in which a user can interact with an hvplot visualization?

  * **Answer** Zooming, panning, hovering, filtering

* Since Matplotlib/Pandas and hvplot plotting APIs work the same way, is hvplot reinventing the wheel by maintaining their own visualization technology?

  * **Answer** No. hvplot abstracts over Pandas/Matplotlib and inherits the objects and attributes already created by these technologies. hvplot leverages pre-existing code rather than creating new code from scratch.

Ask for any remaining questions before moving on.
