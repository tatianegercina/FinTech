## Finally Functioning

You, Harold, and Sam have been working together after hours to harden your Fintech skills and automate your day jobs. While fine-tuning your algorithms, you realize that you've written the logic to calculate compound annual growth rate three times: once for 2016, 2017, and 2018. You're annoyed that you've re-invented the wheel each time, and you're growing concerned that if you make any changes to the algorithm, you'll have to make changes in three different places. This cannot be maintained. You decide to begin refactoring all of your code to make it as modular and reusable as possible.

For this activity, define a function named `calculate_compound_growth_rate` that will accept three arguments (`beginning_balance`, `ending_balance`, and `years`). The function should output a float as `growth_rate`. You want to modularize this code so that you can dynamically calculate compound annual growth rate (CAGR) by simply calling a function with the required inputs. The results will indicate how you've been functioning as a trader!

CAGR is valuable as it calculates/predicts the growth rate earnings/percent increase or decrease of a stock, portfolio, or bank account. This will be useful when trying to evaluate portfolio/stock performance or when choosing which savings account might produce the most return.

* Compound Annual Growth Rate Formula

    ![Readme_Stu_Functions_CAGR.png](Images/Readme_Stu_Functions_CAGR.png)

## Instructions

Using the [starter-file](Unsolved/finally_functioning.py) provided, complete the following steps:

1. Define a function `calculate_compound_growth_rate` that takes in `beginning_balance`, `ending_balance`, and `years` as input. Output `growth_rate`.

2. Initialize `beginning_balance` to 29000.00.

3. Initialize `ending_balance` to 45000.00.

4. Initialize `years` 1.0.

5. Call calculate_compound_growth_rate() and capture results with above values as `year_one_growth`.

6. Update `beginning_balance` to 45000.00.

7. Update `ending_balance` to 47000.00.

8. Call calculate_compound_growth_rate() and capture results as `year_two_growth`.

9. Update `beginning_balance` to 47000.00.

10. Update `ending_balance` to 48930.00.

11. Call calculate_compound_growth_rate() and capture results as `year_three_growth`.

12. Use the Python round() function to round `year_one_growth`, `year_two_growth`, and `year_three_growth`. Capture these new values as new variables.

13. Use string formatting to print `year_one_growth`, `year_two_growth`, and `year_three_growth` as percents.

14. Quickly review the values printed on the screen, and identify the year with the highest rate of return.

### Challenge

Instead of saving the `year_one_growth`, `year_two_growth`, and `year_three_growth` values in variables, add `growth_rate` to a global list named `growth_rates`. Write this logic in a new function `calculate_compound_growth_rate_list`.

## **Hint**

* Instead of returning the local `growth_rate` variable, store it in the `growth_rates` global list object.

* Refer to the w3 schools documentation [here](https://www.w3schools.com/python/ref_func_round.asp) for the Python round function.
