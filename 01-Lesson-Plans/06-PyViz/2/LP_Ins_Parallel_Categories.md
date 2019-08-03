### 11. Instructor Do: Parallel Categories (5 mins) (Critical)

In this activity, students continue learning about more advanced, statistical plots, like the **Parallel Categories** plot by way of an instructor demo. The instructor will demonstrate to students how to create a **parallel categories** plot, as well as highlight the differences between **parallel categories** and **parallel coordinates**.

**Files:**

* [parallel_categories.ipynb](Activities/11-Ins_Parallel_Categories/Solved/parallel_categories.ipynb)

Navigate to the 6.2 slides, and highlight the following:

* Whereas **parallel coordinate** plots are used for multivariate analysis and mapping relationships between variables, **parallel categories** plots are used to perform **multidimensional** analysis.

  * An example of multidimensional analysis would be looking at sales and foreclosures data by housing type, region, and number of units. Housing type, region, and number of units would be good dimensions to consider.

* **Dimensions** are considered to be **categories**. **Parallel categories** plots focus on connecting the dots between each category and assessing the nuances per category, as well as the impact of categories on other categories.

Open the [starter file](Activities/11-Ins_Parallel_Categories/Solved/parallel_categories.ipynb), and live code the following:

* Parallel Categories plots can be created using the `parallel_categories` function.

  ```python
  # Prep Data
  housing_type= ['Single Family','Multi-Family','Apartment']
  region= ['North East','Tri-State']
  prop_size= ['Large','Medium','Small']

  df= pd.DataFrame({
      "foreclosed":np.random.randint(300,303,25),
      "sold":np.random.randint(999,1002,25),
      "year":np.random.randint(2010,2013,25),
      "type": np.random.choice(housing_type, 25),
      "region": np.random.choice(region, 25),
      "prop_size": np.random.choice(prop_size, 25)}).sort_values(['year','type','region','prop_size'])
  df.head()
  px.parallel_categories()
  ```

  ![parallel_categories.png](Images/parallel_categories.png)

* To make sure plots are structured the correct way, use the `dimensions` parameter to hard code what the **dimensions** should be.

  ```python
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno)
  ```

* The labels parameter can be used to customize the labels shown on the plot. It will also add a highlight feature to the label names so they can be read.

  ```python
  px.parallel_categories(df, dimensions=['type','region','prop_size'], color='year',
                        color_continuous_scale=px.colors.sequential.Inferno,
                        labels={'type':'Type of Dwelling', 'region':'Region', 'prop_size':'Property Size'})
  ```

* Similar to parallel coordinates plot, the **parallel categories** plot axes can be sorted by clicking and dragging to the desired location.

  ![sort_categories.gif](Images/sort_categories.gif)
