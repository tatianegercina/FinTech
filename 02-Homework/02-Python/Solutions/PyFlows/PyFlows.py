#!/usr/bin/env python3
# coding: utf-8

# PyFlows

# In this activity you are going to import a file that contains a larger portfolio of loans.

# As investor who is passionate about microfinancing, you want to be able to turn these monthly cash in flows into additional loans. Accordingly, the focus of your analysis will be to determine the amount of USD flows generated each month.


# Part 1 - Importing the CSV

# The first step in this activity will be to import the CSV file containing the newest portfolio information.

# Instructions
# Utilizing the instructions from the curriculum content...


# @TODO
# Import the Path library and module as well as the csv library

from pathlib import Path
import csv

# @TODO
# Create a variable that will initialize the line number variable for use when reviewing the csv file
# Initial a loans list to be build off of the loans in the csv file.

line_num = 0
microfinance_loan_portfolio = []


# @TODO
# Create a variable and assign it the module and file location of the csv file downloaded for this activity.

csvpath = Path('./Resources/microfinance_loan_portfolio.csv')


# @TODO
# Write the code that opens, reads, and prints the CSV file for review.


with open(csvpath, 'r') as csvfile:

    print(type(csvfile))

    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))

    header = next(csvreader)
    line_num += 1
    print(f'{header} <---HEADER')

    for row in csvreader:

        print(row)
        microfinance_loan_portfolio.append(row)

 #print(f"The imported microfinance loan portfolio looks like: {microfinance_loan_portfolio}")

# Loan Portfolio Format
# You will notice that our loan portfolio is in a slightly different format now.

# In a separate text file, highlight at least 3 differences between the format of the loan portfolio in the previous Phases and the one just imported.

# ANSWERS - Loan Portfolio Format
# Now a list of lists, rather than a list of dictionaries.
# Key:Value pairs are gone; have to reference values by their index position.
# Numerical values are strings rather than numbers. They will have to be converted.

print('--------------------')


# Part 2 - USD Receipts by Month

# The goal of this activity is to automate the process of accessing the US dollar amount to be received in payments for each month of the loan cycle.

# Because this is a process that will be done repeatedly for different loan portfolios and different months, the activity requires building a function.

# Given that the goal is to calculate the payments generated per portfolio per month, the function should take in two arguments: the loan portfolio and the number of the month in question (numbered 1 -> 12).

# The function should return return the US dollar value of the loan payments for the specific month.

# In this activity, current fx rates will be provided for the three currencies so the projected US dollar value is as accurate as possible.


# Instructions

# Fortunately, the loan portfolio has the period_payment included as an element in each of the loans.
# With that, the function can focus on sorting through the repayment interval and term_in_months values to make calculations.

# The function will require a second level sort on currency so that currency fx values can be applied to the calculations.

# As with the prior Phases, attempt to pseudocode the solution before writing the code.


# Use the following FX rates when processing calculations. These rates differ from the ones provied at the time the loan was issued.

current_fx_rate_usdpkr = 157.15
current_fx_rate_usdkes = 102.48
current_fx_rate_usdinr = 74.06


# @TODO
# Create a function called 'calculate_monthly_cash_flows' As mentioned, the function will take in 2 parameters, the loan portfolio and the month of the flows you would like calculate.

# HINT - It might also make sense to create the function call and pass in the arguments to confirm that the required data is available inside the function.


def convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency):
    """Converts the foreign currency cash flow amount into a US dollar amount using the fx rate provided."""

    flow_converted_to_usd = 0.0

    if local_currency == 'pkr':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdpkr

    if local_currency == 'kes':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdkes

    if local_currency == 'inr':
        flow_converted_to_usd = local_cash_flow / current_fx_rate_usdinr

    return flow_converted_to_usd


def calculate_monthly_cash_flows(loan_portfolio, month_of_cash_flow_calculation):
    """Calculates the US dollar cash flows generated by a specified loan portfolio for the specified month."""

    # @TODO
    # Create a function-scoped variable to hold the usd total of the monthly flow.
    monthly_cash_flow_total_usd = 0.0

    # @TODO
    # Write the for loop that iterates through each loan in the  imported portfolio.

    # HINT - remember to reference the portfolio by the parameter used in the function definition.

    for loan in loan_portfolio:

        # @TODO
        # Create descriptive variables for each of the index positions in the loan and assign them to the index position of the loan. This will make the elements easier to recognize and reference in the code base.

            # HINT - Variables names should be based off of the CVS file HEADER information.
            # HINT - Also, of the CSV values are strings. It makes sense to convert the relevant values into integers or floats at this stage

        loan_value_usd = int(loan[0])
        term_in_months = int(loan[1])
        annual_interest_rate = float(loan[2])
        repayment_interval = loan[3]
        local_currency = loan[4]
        fx_rate_at_loan_issue = float(loan[5])
        loan_local_value = int(loan[6])
        interval_repayment_amount = int(loan[7])

        monthly_cash_flow_amount_in_usd = 0.0

        # @TODO
        # Create the 3 conditional statements that sort the loans by repayment interval's monthly, quarterly and bullet.

        if repayment_interval == 'monthly':

            # @TODO
            # Inside each repayment_inteval conditional statement, nest a second conditional that verifies if the month for which the flow is being calculated is less than or equal to the term_in_months of the portfolio.

            # In other words, will the portfolio make a payment for the month in question.

            if month_of_cash_flow_calculation <= term_in_months:

                # @TODO
                # Inside this nested conditional, capture the local value of the cash flow for the period (ie, the interval repayment amount.)
                # The local value of the cash flow needs to be converted into USD. To do this...
                # WRITE A SECOND FUNCTION OUTSIDE OF calculates_monthly_cash_flows.
                    # This function should take in two parameters: local_cash_flow & local_currency
                    # The function should sort based on local currency using conditionals
                    # The function should then calculate the US dollar amount (flow_converted_to_usd) of the flow based on the local currency amount and current_fx_rate provided for that currency.
                    # Finally, flow_converted_to_usd should be returned to the primary function.
                # Inside the primary function, this second function should be set equal to the variable monthly_cash_flow_amount_in_usd

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Recreate the code detailed for the "monthly" flow calculations for the quarterly repayment interval.

        elif repayment_interval == 'quarterly':

            if (month_of_cash_flow_calculation % 3 == 0) and (month_of_cash_flow_calculation <= term_in_months):

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Recreate the code detailed for the "monthly" flow calculations for the bullet repayment interval.

        elif repayment_interval == 'bullet':

            if month_of_cash_flow_calculation == term_in_months:

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Write the equation that adds the monthly_cash_flow_amount_in_usd amount each loan to the monthly_cash_flow_total_usd

        monthly_cash_flow_total_usd += monthly_cash_flow_amount_in_usd

    # @TODO
    # Write the return statement for the monthly_cash_flow_total_usd so it can be used outside the function.

    return monthly_cash_flow_total_usd


# @TODO
# Create the function call for the calculate_monthly_cash_flow function. Pass the microfinance load and the value of the month (1-12) for which you want to calculate the flows.

    # HINT - It might make sense to set the function call equal to a variable so it can be utilized. A suggestion for a variable name is total_amount_of_usd_for_month.

total_amount_of_usd_for_month = calculate_monthly_cash_flows(microfinance_loan_portfolio, 1)

# @TODO
# Write the print statement that provides the US dollar value cash flows for the month. Be sure to round the value to 2 decimal places.

print(f"The total USD flows for the month are ${total_amount_of_usd_for_month: .2f}.")


print('--------------------')


# Part 3 - Evaluation

# In a separate text file, evaluate the premise that the current portfolio will yield enough monthly cash to help fund additional loans. The file will be a required part of the submission.

# Question 1:

# How do the functions written above help to automate the process of evaluating the monthly cash flow yield?


# For this next question, you have just been given responsibility for identifying the monthly US dollar yield on at least 10 microfinance portfolios of various sizes. The boss wants to know the expected cash flow yield across the whole suite of loans for each month of the year.

# Question 2.

# What additional functions would you put in place to further help automate the process?
