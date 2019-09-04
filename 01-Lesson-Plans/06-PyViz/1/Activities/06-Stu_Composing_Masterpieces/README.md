# Composing Masterpieces

You just received an email notification from your mom. Her email is below:

```
Hi honey!

Thank you so much for doing research on the states with the cheapest Diabetes care. Your father  and I have looked at the charts, and we're thinking about taking a look at properties in Delaware since its one of the top 10 lowest states for Diabetes care. It was snazzy being able to play with the charts. I've never seen such a thing before!

The reason I'm writing you is because I showed your nifty little report to Marilyn from down the street. You remember her right? She's the one with the two sons, Sean and Kiran. Well, she just got promoted at REMAX, and she's looking to add someone to her team who can help with data visualizations and analytic reporting both full time and as needed. She wants you to come in with a portfolio and interview for the role. She thinks you're a perfect fit! Fingers crossed!

Let me know if you're interested, and I'll give you her phone number!

Love,

Mom

P.S. Make sure to really consider Marilyn's offer! Real estate is such a good industry to get into.
```

Start working on some sample visualizations as a portfolio to showcase to Marilyn. Use the [real estate loan](Resources/state_loan_data.csv) data you found online as the underlying data for visualization. Make sure to pay particular attention to aesthetic details; this portfolio will need to be a masterpiece!

## Instructions

1. Open the [starter file](Unsolved/composing_masterpieces.ipynb), and calculate the total average loan amount by state. Plot the data, and name this plot `plot_state_avgs`. Make this plot a **bar** plot.

2. Use the `hvplot` function to create separate plots visualizing sum of average loan amounts for 2015–2016 and 2010–2014. Name these plots `plot_2015_2016` and `plot_2010_2014`.

3. Compose plots `plot_2015_2016` and `plot_2010_2014` using the `+` operator.

4. Use the `+` layout operator to compose plots `plot_state_avgs`, `plot_2015_2016`, and `plot_2010_2014`.

5. Use the `*` overlay operator to overlay `plot_state_avgs`, `plot_2015_2016`, and `plot_2010_2014`.

### Hint

Composing plots of different kinds can help users visualize differences in data points. Consider composing plots of different kinds to help underscore similarities and differences in trends.

Also, remember to sort data before plotting and leverage labels. This will help users glean better insights from the visualization.



© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.