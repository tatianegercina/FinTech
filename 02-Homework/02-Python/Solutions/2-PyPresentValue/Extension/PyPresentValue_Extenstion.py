# -*- coding: utf-8 -*-

# Phase 2 - PyPresetValue - Extension

# In Extension activities associated with Phase 2 of the PyLending challenge,
# the focus shifts to evaluating the present value of the portfolio, rather than
# just a single loan.

# REMINDER: Extension activities are designed to stretch your knowledge and
# abilities. Your grade will not be penalized for not completing these
# activities, but they should be attempted.


# The portfolio portfolio from the the Phase 2 - Core activities is found below.

microfinance_portfolio_data = [
    {'loan_value_usd': 1000, 'term_in_months': 9, 'annual_interest_rate': 0.37,
     'repayment_interval': 'monthly', 'local_currency': 'pkr',
     'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 162760},
    {'loan_value_usd': 2500, 'term_in_months': 6, 'annual_interest_rate': 0.40,
     'repayment_interval': 'monthly', 'local_currency': 'pkr',
     'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 406900},
    {'loan_value_usd': 400, 'term_in_months': 4, 'annual_interest_rate': 0.35,
     'repayment_interval': 'monthly', 'local_currency': 'pkr',
     'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 65104},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.3825,
     'repayment_interval': 'monthly', 'local_currency': 'pkr',
     'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 122070},
    {'loan_value_usd': 500, 'term_in_months': 12, 'annual_interest_rate': 0.395,
     'repayment_interval': 'bullet', 'local_currency': 'pkr',
     'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 81380},
    {'loan_value_usd': 250, 'term_in_months': 12, 'annual_interest_rate': 0.45,
     'repayment_interval': 'monthly', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 25820},
    {'loan_value_usd': 500, 'term_in_months': 9, 'annual_interest_rate': 0.375,
     'repayment_interval': 'monthly', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 51640},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.425,
     'repayment_interval': 'quarterly', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 103280},
    {'loan_value_usd': 2500, 'term_in_months': 3, 'annual_interest_rate': 0.70,
     'repayment_interval': 'bullet', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 258200},
    {'loan_value_usd': 300, 'term_in_months': 6, 'annual_interest_rate': 0.45,
     'repayment_interval': 'bullet', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 30984},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.35,
     'repayment_interval': 'quarterly', 'local_currency': 'kes',
     'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 77460},
    {'loan_value_usd': 1250, 'term_in_months': 12, 'annual_interest_rate': 0.30,
     'repayment_interval': 'monthly', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 86475},
    {'loan_value_usd': 500, 'term_in_months': 6, 'annual_interest_rate': 0.25,
     'repayment_interval': 'quarterly', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 34590},
    {'loan_value_usd': 200, 'term_in_months': 3, 'annual_interest_rate': 0.35,
     'repayment_interval': 'bullet', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 13836},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.325,
     'repayment_interval': 'monthly', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 55344},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.30,
     'repayment_interval': 'monthly', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 69180},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.35,
     'repayment_interval': 'quarterly', 'local_currency': 'inr',
     'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 55344}
]


print('--------Activity 3------------')


# Activity 3 - DCF Valuation of the Portfolio using Functions - Extension


# The goal of a function is to reformulate a code block that does a single task
# into a code block that can process an action repeatedly.

# Understandably, creating functions is extremely important to the concept of
# automation.

# The goal in the challenge section of this activity is to covert the code block
# that handles the discounted cash flow model for a single loan into one that
# can process the discounted_cash_flow model for any number of loans in the
# portfolio.

# Instructions

# Utilizing the code built in Phase 2 - Activity 2 , write a function that takes
# in the full loan portofolio and processes the discounted_cash_flow calculation
# for each individual loan then nets them together to produce a single
# discounted_cash_flow value.

# Again, calculations will need to be done in the local currency of each loan
# and then coverted into US dollars.

# @TODO
# Start by recreating 2 global variables:  the discount rate and
# usd_discounted_cash_flow_total.

discount_rate = .2
usd_discounted_cash_flow_total = 0.0


# Writing the Function


# @TODO
# Start by creating a function called discounted_cash_flow_valuation. At this
# stage, it is also worth putting the function call at the bottom of this code
# block. The function should take in one argument, the portfolio of loans.

# TEST YOUR FUNCTION- Pass the microfinance_loan_portfolio_data into the
# function and print it to the screen. Incremental testing of our code saves
# time. Print statements are an excellent way to confirm code is working as
# intended.

# HINT - Set your function call equal to the variable
# usd_discounted_cash_flow_total. The will make the return value of your
# function easier to access.

def discounted_cash_flow_valuation(portfolio):
    """Calculates the the present value of the loan based on the discounted cash
    flow model and the repayment amounts of each loan."""

    # @TODO
    # Inside the function, create a variable called
    # usd_discounted_cash_flow_total and assign it a value of 0.0.
    # This variable will eventually hold the total of US dollar payments.

    usd_discounted_cash_flow_total = 0.0

    # @TODO
    # Inside the function, create a for loop that iterates through the loans in
    # the portfolio.

    # REMEMBER: Use the same variable name for the portfolio as that used
    # as the function argument.

    for loan in portfolio:

        # @TODO
        # Create function-scope variables needed for the DCF value calculations.
        # These will be similar to those created in Activity 2 - Core.

        period = 1
        local_discounted_cash_flow = 0
        usd_discounted_cash_flow = 0

        loan_repayment_interval = loan['repayment_interval']
        loan_term_in_months = int(loan['term_in_months'])
        loan_interval_repayment_amount = int(loan['interval_repayment_amount'])
        loan_fx_rate_at_loan_issue = loan['fx_rate_at_loan_issue']

        # @TODO
        # When working with payment data it is important to sort based
        # on the repayment_interval.
        # Write the 3 conditional statements that differentiate by repayment
        # intervals.

        if loan_repayment_interval == 'monthly':

            # @TODO
            # With the loans imported to the function and the conditionals
            # written, address the discounted_cash_flow value calculation.
            # Inside each of the conditional statements, copy the while loop
            # written in Activity 2 - Core.

                # HINT: Be sure to change the syntax so the while loop is
                # accessing data for ALL the loans rather than just the single
                # loan from the Activity 2 - Core.

                # HINT: Be sure to adjust the syntax for the
                # discounted_cash_flow calculation to address the differences
                # in monthly, quarterly and bullet payment periods.

            while period <= loan_term_in_months:
                local_discounted_cash_flow += loan_interval_repayment_amount /
                (1 + (discount_rate / 12))**period
                period += 1

            # @TODO
            # Because of the foreign currencies, the coversion from the
            # foreign discounted_cash_flow value to the usd_discounted_cash_flow
            # value needs to be executed inside the while loop. Execute the
            # conversion from local to US dollars by using fx_rate_at_loan_issue.
            # This code will need to be written inside each conditional.

            usd_discounted_cash_flow = local_discounted_cash_flow /
            loan_fx_rate_at_loan_issue

        # @TODO
        # Calculate the usd_discounted_cash_flow for the loans with a "quarterly"
        # cycle using the above instructions.

        if loan_repayment_interval == 'quarterly':

            while period <= (loan_term_in_months / 3):
                local_discounted_cash_flow += loan_interval_repayment_amount /
                (1 + (discount_rate / 4))**period
                period += 1

            usd_discounted_cash_flow = local_discounted_cash_flow /
            loan_fx_rate_at_loan_issue

        # @TODO
        # Calculate the usd_discounted_cash_flow for the loans with a "bullet"
        # cycle using the above instructions.

        if loan_repayment_interval == 'bullet':

            local_discounted_cash_flow += loan_interval_repayment_amount /
            (1 + (discount_rate))

            usd_discounted_cash_flow = local_discounted_cash_flow /
            loan_fx_rate_at_loan_issue

        # @TODO
        # Still inside the for loop, add the usd_discounted_cash_flow value for
        # each loan to the usd_discounted_cash_flow_total variable.

        usd_discounted_cash_flow_total += round(usd_discounted_cash_flow, 2)
        print(f'usd_dcf_total {usd_discounted_cash_flow_total: .2f}')

    # @TODO
    # Once the for loop finishes processing all of the loans and the total US
    # dollar present value calculated, return the usd_discounted_cash_flow_total
    # figure so that it can be utilized of the function.

    return usd_discounted_cash_flow_total


# @TODO
# Create the call for the discounted_cash_flow_valuation function. Pass the
# microfinance_portfolio_data into the function.

    # HINT - Set the function call equal to a variable so the return value can
    # be utilized. Use the same name as the variable returned from the function.

# This figure represents the present value of the microfinance loan portfolio
# given the 20% discount rate.

usd_discounted_cash_flow_total =
discounted_cash_flow_valuation(microfinance_portfolio_data)

# @TODO
# Write the print statement that provides the US dollar value of the DCF
# valuation for the microfinance portfolio.
# Be sure to round the value to 2 decimal places.

print(f'Given a discount rate of .20, the present value of this loan portfolio
      is ${usd_discounted_cash_flow_total: .2f}.')


print('--------Activity 4------------')


# Part 4 - Portfolio Evaluation - Extension

# Please provide your thoughts and analysis in a separate text file that should
# also be included with your submission.

# Questions 1:

# Given the number that resulted from your present value calculation, does the
# opportunity to co-invest in this microfinance portfolio meet your criteria?
# Does the answer change when you take into account 12% operational costs?
# What if the a default rate of the portfolio is 7%?

# Question 2:

# How would you alter in the code base if the present value of the portfolio
# needed to be evaluated for different discount rates?
