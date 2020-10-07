# Composing Masterpieces

You just received an email notification from your mom. Her email is below:

```
Hi honey!

Thank you so much for doing research on the states with the cheapest diabetes care. Your father and I have looked at the charts, and we're thinking about taking a look at properties in Delaware since it's in the top 10 low-cost states for diabetes care. It was quite fun playing around with the charts. I've never seen such a thing before!

The reason I'm writing you is because I showed your nifty report to Marilyn down the street. You remember her, right? She's the one with the two boys, Sean and Kiran. Well, she just got promoted at her real-estate firm, and is looking to add someone to her team to help with data visualizations and analytic reporting. She wants you to come in with a portfolio and interview for the role. I think you could be the perfect fit! 

Let me know if you're interested, and I'll give you her phone number.

Love,

Mom

P.S. Please give Marilyn's offer some serious thought–real estate is such a good industry to get into!
```

Start working on some sample visualizations as a portfolio to showcase to Marilyn. Use the [real-estate loan](Resources/state_loan_data.csv) data you found online as the underlying data for visualization. Make sure to pay particular attention to aesthetic details; this portfolio will need to be a masterpiece!

## Instructions

1. Open the [starter file](Unsolved/composing_masterpieces.ipynb).  The data has been grouped, summed and stored in a DataFrame named `loan_data` for your use in this activity.

2. Using the `hvplot` function, create a **bar** plot to visualize the total average loan amount by state. Name this plot `plot_state_avgs`. 

2. Create two separate **line** plots visualizing the sum of average loan amounts for years 2015–2016 and years 2010–2014. Name these plots `plot_2015_2016` and `plot_2010_2014`.

3. Compose plots `plot_2015_2016` and `plot_2010_2014` using the `+` operator.

4. Use the `+` layout operator to compose plots `plot_state_avgs`, `plot_2015_2016`, and `plot_2010_2014`.

5. Use the `*` overlay operator to overlay `plot_state_avgs`, `plot_2015_2016`, and `plot_2010_2014`.

### Hint

Composing plots of different kinds can help users visualize differences in data points. Consider composing plots of different kinds to help underscore similarities and differences in trends.

Also, remember to sort data before plotting and leverage labels. This will help users glean better insights from the visualization.



© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
