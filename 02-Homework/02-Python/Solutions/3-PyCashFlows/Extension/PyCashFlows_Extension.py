# -*- coding: utf-8 -*-

# Phase 3 - PyFlows - Extension

# In Extension activities associated with Phase 3 of the PyLending challenge,
# the focus shifts determining the US cash flows generated each month.

# REMINDER: Extension activities are designed to stretch your knowledge and
# abilities. Your grade will not be penalized for not completing these
# activities, but they should be attempted.

print('--------Activity 3------------')

# Instructions

# As mentioned at the end of the PyCashFlow Core section, completion of these
# Extension activities will require importing the CSV file.

# Copy/Paste the code from PyCashFlow.py into this section and confirm that
# the import is operational.


from pathlib import Path
import csv
line_num = 0
microfinance_loan_portfolio = []

csvpath = Path('../Resources/microfinance_loan_portfolio.csv')


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

print(f"The imported microfinance loan portfolio looks like: {microfinance_loan_portfolio}")


print('--------Activity 4------------')


# Activity 4  - USD Receipts by Month

# The goal of this activity is to automate the process of accessing the US
# dollar amount to be received in payments for each month of the loan cycle.

# Because this is a process that will be done repeatedly for different loan
# portfolios and different months, the activity requires building a function.

# Given that the goal is to calculate the payments generated per portfolio per
# month, the function should take in two arguments:
# 1. The loan portfolio
# 2. The number of the month for which flows are wanted (numbered 1 -> 12).

# The function should return return the US dollar value of the loan repayments.

# In this activity, current fx rates will be provided for the currencies so the
# projected US dollar value is as accurate as possible.


# Instructions

# Fortunately, the loan portfolio has the period_payment included as an element
# in each of the loans.
# The function can focus on sorting through the repayment_interval and
# term_in_months values to make calculations.

# Because the function should work for all loans it will require a second level
# sort on local_currency so that currency fx values can be applied to the
# calculations.

# REMEMBER: As with the prior Phases, think through the required steps and
# attempt to pseudocode the solution before writing the code.


# Use the following FX rates when processing calculations. These rates differ
# from the ones provied at the time the loan was issued.

current_fx_rate_usdpkr = 157.15
current_fx_rate_usdkes = 102.48
current_fx_rate_usdinr = 74.06


# @TODO
# Create a function called 'calculate_monthly_cash_flows' The function will take
# in 2 arguments, the loan portfolio and the month for which you would like
# cash flow information.

# HINT:  Also create the function call and pass in the arguments to confirm
# that the required data is available inside the function.


def calculate_monthly_cash_flows(loan_portfolio, month_of_cash_flow_calculation):
    """Calculates the US dollar cash flows generated by a specified loan portfolio
    for the specified month."""

    # @TODO
    # Create a function-scoped variable to hold the usd total of the monthly flow.

    monthly_cash_flow_total_usd = 0.0

    # @TODO
    # This section will eventually be the home of a NESTED FUNCTION called
    # convert_foreign_cash_flow_to_usd

    # REMEMBER - Nested functions must be initiated before they are called.

    def convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency):
        """Converts the foreign currency cash flow amount into a US dollar amount
        using the fx rate provided."""

    # @TODO
    # Create a function scoped variable to hold the value of the flow converted
    # to USD
        flow_converted_to_usd = 0.0

        if local_currency == 'pkr':
            flow_converted_to_usd = local_cash_flow / current_fx_rate_usdpkr

        if local_currency == 'kes':
            flow_converted_to_usd = local_cash_flow / current_fx_rate_usdkes

        if local_currency == 'inr':
            flow_converted_to_usd = local_cash_flow / current_fx_rate_usdinr

        return flow_converted_to_usd

    # ##### End Nested Function Section #####

    # @TODO
    # Write the for loop that iterates through each loan in the  imported portfolio.

    # HINT - remember to reference the portfolio by the parameter used in
    # the function definition.

    for loan in loan_portfolio:

        # @TODO
        # Create descriptive variables for each of the index positions in the
        # loan and assign them to the index position of the loan.
        # This will make the elements easier to recognize and reference in the
        # function.

            # HINT - Variables names should be based off of the CVS file HEADER.
            # HINT - The CSV values are strings. It makes sense to convert the
            # relevant values into integers or floats at this stage

        loan_value_usd = int(loan[0])
        term_in_months = int(loan[1])
        annual_interest_rate = float(loan[2])
        repayment_interval = loan[3]
        local_currency = loan[4]
        fx_rate_at_loan_issue = float(loan[5])
        loan_local_value = int(loan[6])
        interval_repayment_amount = int(loan[7])

        # @TODO
        # Write a print statements that compares the loan and the variables
        # just created.

        print(f"CSV loan: {loan}")
        print(f"Variables: {loan_value_usd, term_in_months, annual_interest_rate, repayment_interval,local_currency, fx_rate_at_loan_issue , loan_local_value,interval_repayment_amount   }")

        print("")

        monthly_cash_flow_amount_in_usd = 0.0

        # @TODO
        # Create the 3 conditional statements that differentiate the loans by
        # repayment_interval. Start with "monthly"

        if repayment_interval == 'monthly':

            # @TODO
            # Inside each conditional statement, nest a second conditional that
            # verifies if the month for which the flow is being calculated is less
            # than or equal to the term_in_months of the portfolio.
            # In other words, will the portfolio make a payment for the month
            # in question.

            if month_of_cash_flow_calculation <= term_in_months:

                # @TODO
                # Inside this nested conditional, capture the local value of
                # the cash flow for the period (ie, the interval repayment amount.)
                # The local value of the cash flow needs to be converted into USD.
                # To do this...
                    # WRITE A SECOND FUNCTION OUTSIDE OF calculates_monthly_cash_flows.
                    # This function should take in two parameters:
                        # local_cash_flow & local_currency

                    # The function should sort based on local currency using
                    # conditionals

                    # The function should then calculate the US dollar amount
                    # (flow_converted_to_usd) of the flow based on the local
                    # currency amount and current_fx_rate provided for that
                    # currency.

                    # Finally, flow_converted_to_usd should be returned to the
                    # primary function.

                # Inside the primary function, this second function should be
                # set equal to the variable monthly_cash_flow_amount_in_usd

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Based on the instructions above, write teh code for the "quarterly"
        # repayment interval.

        elif repayment_interval == 'quarterly':

            if (month_of_cash_flow_calculation % 3 == 0) and (month_of_cash_flow_calculation <= term_in_months):

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Based on the instructions above, write teh code for the "bullet"
        # repayment interval.

        elif repayment_interval == 'bullet':

            if month_of_cash_flow_calculation == term_in_months:

                local_cash_flow = interval_repayment_amount

                monthly_cash_flow_amount_in_usd = convert_foreign_cash_flow_to_usd(local_cash_flow, local_currency)

            else:
                print("No flows for this month from this loan")

        # @TODO
        # Write the equation that adds the monthly_cash_flow_amount_in_usd amount
        # each loan to the monthly_cash_flow_total_usd

        monthly_cash_flow_total_usd += monthly_cash_flow_amount_in_usd

    # @TODO
    # Write the return statement for the monthly_cash_flow_total_usd so it can
    # be used outside the function.

    return monthly_cash_flow_total_usd


# @TODO
# Create the function call for the calculate_monthly_cash_flow function.
# Pass the micro-finance loan and the value of the month (1-12).

    # HINT - It might make sense to set the function call equal to a variable
    # so it can be utilized. A suggestion for a variable name is
    # total_amount_of_usd_for_month.
total_amount_of_usd_for_month = calculate_monthly_cash_flows(microfinance_loan_portfolio, 1)

# @TODO
# Write the print statement for US dollar value cash flows for the month.
# Be sure to round the value to 2 decimal places.

print(f"Total USD flows for the month: ${total_amount_of_usd_for_month: .2f}.")


print('--------Activity 5------------')


# Activity 5  - Monthly Cash Flow Evaluation

# In a separate text file, answer the following questions.

# Questions 1:

# Evaluate the premise that the current portfolio will yield enough monthly cash
# to help fund additional loans.


# Question 2:

# How do the functions written above help to automate the process of evaluating
# the monthly cash flow yield of loan portfolios?


# For this next question, you have just been given responsibility for
# identifying the monthly US dollar yield on at least 10 microfinance portfolios
# of various sizes.
# The boss wants to know the expected cash flow yield across the whole suite of
# loans for each month of the year.

# Question 3:

# What additional functions could you put in place to further help automate
# the process?
