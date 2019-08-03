### 2. Instructor Do: Really Important Demo (5 mins) (Critical)

In this activity, students continue learning about more advanced, statistical plots, like the **Parallel Categories** plot by way of an instructor demo. The instructor will demonstrate to students how to create a **parallel categories** plot, as well as highlight the differences between **parallel categories** and **parallel coordinates**.

**Files:**

* [parallel_categories.ipynb](Activities/11-Ins_Parallel_Categories/Solved/parallel_categories.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* Whereas **parallel coordinate** plots are used for multivariate analysis and mapping relationships between variables, **Parallel categories** plots are used to perform multidimensional analysis.

  * An example of multidimensional analysis would be looking at sales and foreclosures data by housing type, region, and number of units. Housing type, region, and number of units would be good dimensions to consider.

* Dimensions are considered to be "categories." **Parallel categories** plots focus on connecting the dots between each category and assessing the nuances per category, as well as the impact of categories on other categories.

Open the starter file, and live code the following:

* Parallel Categories plots can be created using the `parallel_categories` function.

```python
px.parallel_categories()
```
