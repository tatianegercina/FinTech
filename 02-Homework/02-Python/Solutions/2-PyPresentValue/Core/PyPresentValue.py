# -*- coding: utf-8 -*-

# Phase 2 - PyPresetValue - Core

# In Phase 2 of the PyLending challenge, you are looking to evaluate the present
# value of the portfolio. You are looking to determine if, at the present value,
# the portfolio meets your investment return critera of approximately 15%.

# The portfolio being evaluated is the same as from Phase 1, only it includes
# the 'loan_local_value' key:value pair in each dictionary.

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


# As examined in our lessons, determining the present value of a
# loan, like a bond, involves calculating the present value of a series of
# cash flows, or loan payments, based on a specified discount rate.

# In order to calculate the present values of each loan, we must first determine
# the the repayment amount per period that will be made to pay back each loan.

# For the purposes of this Phase, you can assume that the payments will
# include both principle and interest.

# The formula for determing the period payment of loan is as follows:

# > Payment = loan value * interest_rate_per_period /
#  1 - (1 + rate per period)**-number_payment_periods

# Examining the loan data, note that there are 3 different repayment intervals:

#  monthly - a payment will be made each MONTH for the duration of the loan
#  quarterly - a payment will be made each QUARTER (or once every 3 months)
#  for the duration of the loan
#  bullet - a SINGLE PAYMENT of principle and interest will be made at the
#  end of the loan's term.

# In order to correctly calculate the cash flows for each loan, these repayment
# intervals will need to be taken into account.

# Because these loans were made to the individuals in local currency, these
# repayment calculations will need to be made using the loan_local_value.


print('--------Activity 1------------')


# Activity 1 -  Calculating Period Payments per Loan

# This is a Core part of the Phase and must be completed.


# Instructions:

# In this exercise, the goal is to create the function for calculating the
# amount the borrower has to repay at each stated repayment interval. The
# variable used to hold this amount should be called period_payment.

# For loans with a 'monthly'  repayment_interval, the loan will be repaid
# in equal interval_repayment_amounts will be make every month.
# For loans with a 'quarterly' repayment_interval, the loan will be repaid
# in equal interval_repayment_amounts make every 3 months.
# For the 'bullet' repayment_interval, there will be one payment at the end
# of the term that includes principle and interest.

# Once the period_payment is calculated, append key:value pair to the loans
# dictionary. The key should be called 'interval_repayment_amount'.

# NOTE: Before beginning to code, read through the the entire problem and
# attempt pseudocode the program.


# @TODO
# Write the for loop that iterates through the microfinance portfolio

for loan in microfinance_portfolio_data:

    # @TODO
    # Write the 3 conditional statements that differentiate the microfinance
    # portfolio by repayment_intervals.

        # HINT - Don't forget that each loan is a dictionary. Use bracket
        # notation to access keys.
        # HINT - Use "double equal" to compare values.

    if loan['repayment_interval'] == 'monthly':

        # @TODO
        # Inside each conditional statement:
            # 1. Create an equation that calculates the interest_interest_rate_per_period.
                # The duration of our loans is less than 1 year so the
                # annual_interest_rate will only need to be divided by the
                # repayment period to determine the rate per period.

                # For 'monthly' the divisor will be 12.

                # For 'quarterly', the divisor will be 4.

                # 'Bullet' payments are more challenging. The rate will need to
                # be divided by 12 but that that calculation will need to be
                # multiplied by the length in months of the loan.

        interest_rate_per_period = loan['annual_interest_rate'] / 12

        # 2. Create a variable for the number_payment_periods. Set it equal
        # to the relationship between the loan's term_in_months and the
        # repayment_interval.
        # For instance, if the term_in_months of the loan is 6 and the
        # repayment_interval is 'quarterly', the number_payment_periods
        # is 2.
        # For a 'monthly' loan, the number of payment periods is the
        # length in months of the loan.
        # For a 'bullet' loan, there is only one payment.

        number_payment_periods = loan['term_in_months']

        # 3. Create an equation for the interval_repayment_amount using the
        # set it equal to the equation detailed below using
        # loan_local_value for the value of the loan.
        # Payment = loan value * interest_rate_per_period /
        #   1 - (1 + rate per period)**-number_payment_periods

        interval_repayment_amount = (loan['loan_local_value'] *
                                     interest_rate_per_period) /
        (1 - (1 + interest_rate_per_period)**-number_payment_periods)

        # 4. Update date the loan dictionary with a key called
        # interval_repayment_amount and a value equal to the
        # interval_repayment_amount calculation from step 5.

        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

    # @TODO
    # Calculate the interval_repayment_amount for the loans with a "quarterly"
    # cycle using the above instructions.

    if loan['repayment_interval'] == 'quarterly':
        interest_rate_per_period = loan['annual_interest_rate'] / 4

        number_payment_periods = loan['term_in_months'] / 3

        interval_repayment_amount = (loan['loan_local_value'] *
                                     interest_rate_per_period) /
        (1 - (1 + interest_rate_per_period)**-number_payment_periods)

        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

    # @TODO
    # Calculate the interval_repayment_amount for the loans with a "bullet", or
    # singly payment, cycle using the above instructions.

    if loan['repayment_interval'] == 'bullet':
        interest_rate_per_period = (loan['annual_interest_rate'] / 12) *
        loan['term_in_months']

        number_payment_periods = 1

        interval_repayment_amount = (loan['loan_local_value'] *
                                     interest_rate_per_period) /
        (1 - (1 + interest_rate_per_period)**-number_payment_periods)

        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

# @TODO
# Confirm that the key:value pairs have been added to the dictionaries properly
# by printing out one loan from each foreign currency.

check_loan_pkr = microfinance_portfolio_data[0]
check_loan_kes = microfinance_portfolio_data[5]
check_loan_inr = microfinance_portfolio_data[11]

print(f'Confirming that the PKR loans have a interval_repayment_amount: {check_loan_pkr}')
print(f'Confirming that the KES loans have a interval_repayment_amount: {check_loan_kes}')
print(f'Confirming that the INR loans have a interval_repayment_amount: {check_loan_inr}')


print('--------Activity 2------------')


# Activity 2 -  Discounted Cash Flow Valuation - Single Portfolio

# This is a Core part of the Phase and must be completed.

# With the local interval_repayment_amount value in place for each dictionary,
# it should be easier to calculate the present value of the portfolio.

# To determine the present value of these loans, utilize the discounted
# cash flow (discounted_cash_flow) model. Take the sum of each of the
# future cash payments as viewed through the lense of an assigned discount rate
# and the time period of the payment.


# > discounted_cash_flow = interval_repayment_amount /(1 + discount_rate)^1st_period
#  + interval_repayment_amount / (1 + discount_rate)^2nd_period
#  + ...
#  + interval_repayment_amount/(1 + discount_rate)^last_period


# The discount rate is very important to discounted_cash_flow calculations. Two
# factors inform the basis of the discount rate - the time value of money and
# uncertainty risk. The higher the discount rate the larger the uncertainty of
# the investment. When valuing a company the discount rate is often determined
# by an educated guess.

# For valuing bonds, the discount rate used is usually the Federal Reserve's
# lending rate.

# For this activity, a discount rate of 20% should be used. This is the average
# rate of microfinance loans in the US, which is your most likely investment
# alternative to this international loan portfolio.

# NOTE : The goal is to arrive at the valuation in US dollars, though most of the
# calculations will have to be done in the local currency.

# Instructions:

# Rather than jumping in to calculating the fair value of the entire portfolio,
# start by calculating the fair value of the first loan.

# The following print statement will detail the elements associated with the
# first loan in the list.

first_loan = microfinance_portfolio_data[0]

print(f'For reference, the first portfolio is: {first_loan}')

# Based on the information provided above about the DCF valuation model, try to
# pseudocode the solution before attempting to write any code.


# @TODO
# Create the global variables needed for the analysis.

# Variable might include the discount rate, one to iterate through the time
# period calculation,  one to hold the local value of the discounted cash flow,
# and one to hold the US dollar value of the valuation.

discount_rate = .2
period = 1
discounted_cash_flow = 0.0
usd_discounted_cash_flow = 0.0

# @TODO
# Create 3 variables that capture the required information from the particular
# loan being examined.
# The variables are: loan_term_in_months, loan_interval_repayment_amount,
# and loan_fx_rate_at_loan_issue

# Example: loan_term_in_months = int(microfinance_portfolio_data[0]['term_in_months'])

# HINT: Some of the string values will need to be incovered into integers.

loan_term_in_months = int(microfinance_portfolio_data[0]['term_in_months'])

loan_interval_repayment_amount =
int(microfinance_portfolio_data[0]['interval_repayment_amount'])

loan_fx_rate_at_loan_issue = microfinance_portfolio_data[0]['fx_rate_at_loan_issue']

local_discounted_cash_flow = 0


# @TODO
# As in prior activities, a loop is needed, in this case, to cycle through the
# number of repayment periods.
# The loop will run as long a the period iterator variable is less than the
# number of periods required by the term of the loan.
# Write the code of a loop that will iterate through the periods WHILE that
# value is less than the term of the loan.

while period <= loan_term_in_months:

    # @TODO
    # Inside the while loop:
    # 1. Write the local_discounted_cash_flow equation using the following
    # formula as a guide:
    # > discounted_cash_flow = interval_repayment_amount /
    # (1 + discount_rate)^1st_period

    local_discounted_cash_flow += loan_interval_repayment_amount /
    (1 + (discount_rate / 12)) ** period

    # 2. Increment the period value so that the dcf calculation is performed for
    # the next time period

    period += 1

# @TODO
# Write a print statement that confirms the local currency amount of the
# discounted cash flow

print(f'The foreign currency amount of the discounted_cash_flow model is
      {local_discounted_cash_flow: .0f}.')

# @TODO
# Calculate the value of the US dollar amount of the discounted cash flow by
# dividing the local_discount_cash flow by the loan_fx_rate_at_loan_issue.

usd_discounted_cash_flow = local_discounted_cash_flow / loan_fx_rate_at_loan_issue


# @TODO
# Create a print statement that displays the US dollar value of the DCF cash
# flow. Round the value to 2 decimal places.

print(f'The USD loan value based on the DCF model is ${usd_discounted_cash_flow: .2f}.')


print('--------PyPresentValue_Extension------------')

# Congratulations on working through the 2 activities associated with the Core
# components of Phase 2 of the PyLending Challenge.

# To work through the Extension activities, navigate to the Extension folder
# and the PyPresentValue_Extension.py starter code.

# REMINDER: Extension activities are designed to stretch your knowledge and
# abilities. Your grade will not be penalized for not completing these
# activities, but they should be attempted.
