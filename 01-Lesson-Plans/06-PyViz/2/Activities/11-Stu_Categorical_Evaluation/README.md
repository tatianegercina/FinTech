# Categorical Property Evaluation

On August 1st, Alleghany County released their 2019 real estate property assessment report. Read in the data using Pandas and plot it using a **parallel categories** plot in order to analyze the attributes that have a large impact on evaluated housing prices. Interact with the plot in order to identify key trends/patterns in each dimension.

If you finish early, complete the challenge section. If you're feeling confident in your story, volunteer to present your findings and lead the activity review module.

1. Open the starter file, and slice `prop_assessments` DataFrame by **LOCALTOTAL**, **USEDESC**, **TOTALROOMS**, **BEDROOMS**, and **FULLBATHS**.

2. Use the **parallel categories** function to plot the data. Color code the lines based off of the **LOCALTOTAL** field. Hint: Make sure to include the `dimensions` and `color` attributes.

3. Sort the plot so that **BEDROOMS**, **TOTALROOMS**, and **FULLBATHS** are sorted in ascending order.

### Challenge

Find a teammate who has also finished early, and work with them to analyze the data and interpret the **story** of Alleghany real estate property assessments and the evidenced trends of association.

### Hint

When completing the challenge and coming up with your story about Alleghany real estate property assessments, remember that **parallel categories** plots are used to visualize the groups and trends of associations.

Consider the below questions when thinking about the story.

* Are there any identifiable patterns at the dimension level?

* How many bedrooms and full bathrooms do single family homes tend to have?

* When there's three bedrooms, how many full bathrooms are there usually?
