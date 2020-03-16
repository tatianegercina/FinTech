#!/usr/bin/env python3
# coding: utf-8

# Phase 2 - PyPresetValue

# In Phase 2 of the PyLending challenge, you are looking to evaluate the current net present value (NPV) of the portfolio. You are looking to determine if, at the present NPV, the portfolio meets your investment return critera of approximately 15%.

# This activity is designed to give you practice with building and calling functions.

# The portfolio being evaluated is the same as from Phase 1, only it includes the 'loan_local_value' key:value pair in each object.

microfinance_portfolio_data = [
    {'loan_value_usd': 1000, 'term_in_months': 9, 'annual_interest_rate': 0.37, 'repayment_interval': 'monthly',
        'local_currency': 'pkr', 'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 162760},
    {'loan_value_usd': 2500, 'term_in_months': 6, 'annual_interest_rate': 0.40, 'repayment_interval': 'monthly',
        'local_currency': 'pkr', 'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 406900},
    {'loan_value_usd': 400, 'term_in_months': 4, 'annual_interest_rate': 0.35, 'repayment_interval': 'monthly',
        'local_currency': 'pkr', 'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 65104},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.3825, 'repayment_interval': 'monthly',
        'local_currency': 'pkr', 'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 122070},
    {'loan_value_usd': 500, 'term_in_months': 12, 'annual_interest_rate': 0.395, 'repayment_interval': 'bullet',
        'local_currency': 'pkr', 'fx_rate_at_loan_issue': 162.76, 'loan_local_value': 81380},
    {'loan_value_usd': 250, 'term_in_months': 12, 'annual_interest_rate': 0.45, 'repayment_interval': 'monthly',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 25820},
    {'loan_value_usd': 500, 'term_in_months': 9, 'annual_interest_rate': 0.375, 'repayment_interval': 'monthly',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 51640},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.425, 'repayment_interval': 'quarterly',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 103280},
    {'loan_value_usd': 2500, 'term_in_months': 3, 'annual_interest_rate': 0.70, 'repayment_interval': 'bullet',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 258200},
    {'loan_value_usd': 300, 'term_in_months': 6, 'annual_interest_rate': 0.45, 'repayment_interval': 'bullet',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 30984},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly',
        'local_currency': 'kes', 'fx_rate_at_loan_issue': 103.28, 'loan_local_value': 77460},
    {'loan_value_usd': 1250, 'term_in_months': 12, 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 86475},
    {'loan_value_usd': 500, 'term_in_months': 6, 'annual_interest_rate': 0.25, 'repayment_interval': 'quarterly',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 34590},
    {'loan_value_usd': 200, 'term_in_months': 3, 'annual_interest_rate': 0.35, 'repayment_interval': 'bullet',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 13836},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.325, 'repayment_interval': 'monthly',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 55344},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 69180},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly',
        'local_currency': 'inr', 'fx_rate_at_loan_issue': 69.18, 'loan_local_value': 55344},
]


# As examined in our lessons, we know that determining the present value of a loan involves calculating the present value of a series of cash flows (or loan payments) based on a specified discount rate.

# Therefore, in order to calculate the present values of each loan, we must first determine the the repayment amount per period that will be made to pay back each loan.

# The formula for determing the period payment of loan is as follows:

# > Payment = loan value * interest_rate_per_period / 1 - (1 + rate per period)**-number_payment_periods

# Examining the loan data, note that there are 3 different repayment intervals:

#  monthly - a payment will be made each month for the duration of the loan
#  quarterly - a payment will be made each quarter (or once every 3 months) for the duration of the loan
#  bullet - a single payment of principle and interest will be made at the end of the loan

# In order to correctly calculate the cash flows for each loan, we will need to take these repayment intervals into account.

# Because these loans were made to the individuals in local currency, you will want to make these payment calculations using the loan_local_value.

# With this information and the formula in hand, it is time to determine the period payment associated with each of the loans.

# Note:  For the purposes of this activity, you can assume that the payments will include both principle and interest.


# Part 1 -  Calculating Period Payments

# In this exercise, you are going to create the function for calculating the 'paymet per period', or the amount the borrower has to pay to the lender at the stated repayment interval.

# For loans with a 'monthly'  repayment_interval, the loan will be repaid in equal interval_repayment_amounts will be make every month.
# For loans with a 'quarterly' repayment_interval, the loan will be repaid in equal interval_repayment_amounts make every 3 months.
# For the 'bullet' repayment_interval, there will be one payment at the end of the term that includes principle and interest.

# Once the period payment is calculated, append a interval_repayment_amount' key:value pair to the dictionary.

# Before beginning to code, read through the steps and attempt to work through the program using pseudocode.


# Instructions


# @TODO
# Write the for loop that iterates through the microfinance portfolio

for loan in microfinance_portfolio_data:

    # @TODO
    # Write the three conditional statements that segment the microfinance portfolio by repayment_intervals.

        # HINT - Don't forget that each loan is a dictionary. You will need to use bracket notation to access keys.
        # HINT - You will need to utilize the "double equal" in order to compare values.

    if loan['repayment_interval'] == 'monthly':

        # @TODO
        # Inside each conditional statement:
            # 1. Create an equation that calculates the interest_interest_rate_per_period.
                # The duration of our loans is less than 1 year so the annual_interest_rate will only need to be divided by the repayment period to determine the rate per period.
                # For 'monthly' the divisor will be 12. For 'quarterly', the divisor will be 4.
                # 'Bullet' payments are more challenging. The rate will need to be divided by 12 but that that calculation will need to be multiplied by the length in months of the loan.
            # 2. Create a variable for the number_payment_periods. Set it equal to the relationship between the loan's term_in_months and the repayment_interval.
                # For instance, if the term_in_months of the loan is 6 and the repayment_interval is 'quarterly', the number_payment_periods is 2.
                # For a 'monthly' loan, the number of payment periods is the length in months of the loan.
                # For a 'bullet' loan, there is only one payment.
            # 3. Create an equation for the interval_repayment_amount using the set it equal to the equation detailed below using loan_local_value for the value of the loan.
                # Payment = loan value * interest_rate_per_period / 1 - (1 + rate per period)**-number_payment_periods
            # 4. Update date the loan dictionary with a key called interval_repayment_amount and a value equal to the interval_repayment_amount calculation from step 5.

        interest_rate_per_period = loan['annual_interest_rate'] / 12
        number_payment_periods = loan['term_in_months']
        interval_repayment_amount = (loan['loan_local_value'] * interest_rate_per_period) / (1 - (1 + interest_rate_per_period)**-number_payment_periods)
        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

    # @TODO
    # Calculate the interval_repayment_amount for the loans with a "quarterly" cycle using the above instructions.

    if loan['repayment_interval'] == 'quarterly':
        interest_rate_per_period = loan['annual_interest_rate'] / 4
        number_payment_periods = loan['term_in_months'] / 3
        interval_repayment_amount = (loan['loan_local_value'] * interest_rate_per_period) / (1 - (1 + interest_rate_per_period)**-number_payment_periods)
        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

    # @TODO
    # Calculate the interval_repayment_amount for the loans with a "bullet", or singly payment, cycle using the above instructions.

    if loan['repayment_interval'] == 'bullet':
        interest_rate_per_period = (loan['annual_interest_rate'] / 12) * loan['term_in_months']
        number_payment_periods = 1
        interval_repayment_amount = (loan['loan_local_value'] * interest_rate_per_period) / (1 - (1 + interest_rate_per_period)**-number_payment_periods)
        loan['interval_repayment_amount'] = f'{interval_repayment_amount: .0f}'

# @TODO
# Confirm that the key:value pairs have been added to the dictionaries properly by printing out one loan from each foreign currency.

check_loan_pkr = microfinance_portfolio_data[0]
check_loan_kes = microfinance_portfolio_data[5]
check_loan_inr = microfinance_portfolio_data[11]

print(f'Confirming that the PKR loans have a interval_repayment_amount: {check_loan_pkr}')
print(f'Confirming that the KES loans have a interval_repayment_amount: {check_loan_kes}')
print(f'Confirming that the INR loans have a interval_repayment_amount: {check_loan_inr}')

print('--------------------')


# Part 2 -  Discounted Cash Flow Valuation - Single Portfolio


# Now that the local interval_repayment_amount value is in place for each dictionary, it should be much easier to calculate the present value of the portfolio.

# To determine the present value of these loans you will utilize the discounted cash flow (discounted_cash_flow) model. You will take the sum of each of the future cash payments as viewed through the lense of an assigned discount rate and the time period of the payment.


# > discounted_cash_flow = interval_repayment_amount/(1 + discount_rate)^1st_period + interval_repayment_amount/(1 + discount_rate)^2st_period  +...+ interval_repayment_amount/(1 + discount_rate)^last_period


# The discount rate is very important to discounted_cash_flow calculations. Two factors form the basis of the discount rate - the time value of money and uncertainty risk. The higher the discount rate the larger the uncertainty of the investment. generally thought of as the alternative investment rate. When valuing a company the discount rate is often determined by an educated guess.

# For valuing loans, the discount rate used is usually the Federal Reserve's lending rate.

# For this activity, a discount rate of 20% should be used. This is the average rate of microfinance loans in the US, which is your most likely investment alternative to this international loan portfolio.

# Rather than jumping in to calculating the fair value of the entire portfolio, start by calculating the fair value of the first loan.


# Instructions

# This activity will focus on calculating the discounted cash flow valuation of a single loan.

# Ultimately, the goal is to arrive at the valuation in US dollars, though most of the calculations will have to be done in the local currency.

# The following print statement will detail the elements associated with the first loan in the list.  These elements will be used in coding the discounted_cash_flow valuation model.

first_loan = microfinance_portfolio_data[0]

print(f'For reference, the first portfolio is: {first_loan}')

# Based on the information provided above about the discount cash flow valuation model, try to pseudocode the solution to determing the DCF valuation of the first bond before attempting to write any code.


# @TODO
# Create the global variables needed for the analysis.

# HINT - Suggestions would include a variable to hold the discount rate, one to iterate through the time period calculation one to hold the local value of the discounted cash flow, and one to hold the US dollar value of the valuation.

discount_rate = .2
period = 1
discounted_cash_flow = 0.0
usd_discounted_cash_flow = 0.0

# @TODO
# Create 3 variables that capture the required information from the particular loan being examined.
# The variables are: loan_term_in_months, loan_interval_repayment_amount, and loan_fx_rate_at_loan_issue

# For example: loan_term_in_months = int(microfinance_portfolio_data[0]['term_in_months'])

# HINT - Some of the string values will need to be incovered into integers.

loan_term_in_months = int(microfinance_portfolio_data[0]['term_in_months'])
loan_interval_repayment_amount = int(microfinance_portfolio_data[0]['interval_repayment_amount'])
loan_fx_rate_at_loan_issue = microfinance_portfolio_data[0]['fx_rate_at_loan_issue']
local_discounted_cash_flow = 0


# @TODO
# As in prior activities, a loop is needed, in this case, to cycle through the number of repayment periods. The loop will run as long a the period iterator variable is less than the number of periods required by the term of the loan.
# Write the code of a loop that will iterate through the periods WHILE that value is less than the term of the loan.

while period <= loan_term_in_months:

    # @TODO
    # Inside the while loop:
    # 1. Write the local_discounted_cash_flow equation using the following formula as a guide:

    # > discounted_cash_flow = interval_repayment_amount/(1 + discount_rate)^1st_period

    # 2. Increment the period value so that the dcf calculation is performed for the next time period

    local_discounted_cash_flow += loan_interval_repayment_amount / (1 + (discount_rate / 12)) ** period
    period += 1

# @TODO
# Write a print statement that confirms the local currency amount of the discounted cash flow

print(f'The foreign currency amount of the discounted_cash_flow model is {local_discounted_cash_flow: .0f}.')

# @TODO
# Calculate the value of the US dollar amount of the discounted cash flow by dividing the local_discount_cash flow by the loan_fx_rate_at_loan_issue.

usd_discounted_cash_flow = local_discounted_cash_flow / loan_fx_rate_at_loan_issue


# @TODO
# Create a print statement that displays the US dollar value of the DCF cash flow. Round it to decimal places.

print(f'The USD value of the loan based on the discounted_cash_flow model is ${usd_discounted_cash_flow: .2f}.')


print('--------------------')


# Challenge - Part 3 - DCF Valuation of the Portfolio using Functions

# The goal of a function is to reformulate a code block that does a single task into a code block that can process an action repeatedly.

# Understandably, creating functions is extremely important to the concept of automation.

# The goal in the challenge section of this activity is to covert the code block that handles the discounted cash flow model for a single loan into one that can process the discounted_cash_flow model for the total number of loans in the portfolio.

# Instructions

# Utilizing the code block built in the step above, write a function that takes in the whole loan portofolio
# and processes the discounted_cash_flow calculation for each loan individually and then nets them together to produce a single discounted_cash_flow value.

# @TODO
# Start by recreating 2 global variables: the discount rate and usd_discounted_cash_flow_total.

discount_rate = .2
usd_discounted_cash_flow_total = 0.0


# Writing the Function


# @TODO
# Start by creating a function called discounted_cash_flow_valuation. At this stage, it is also worth putting the function call at the bottom of this code cell. The function should take one argument, the portfolio of loans.

#   TEST YOUR FUNCTION- Pass the microfinance_loan_portfolio_data into the function and print it. Incremental testing saves time in the long run.

#   HINT - Set your function call equal to the variable usd_discounted_cash_flow_total. The will make the return value of your function easier to access.


def discounted_cash_flow_valuation(portfolio):
    """Calculates the the present value of the loan based on the discounted cash flow model and the repayment amounts of each loan."""

    # @TODO
    # Inside the function, create a global variable called usd_discounted_cash_flow_total and assign it a value of 0.0. This variable is needed to prevent a 'referenced before assignment' error.

    usd_discounted_cash_flow_total = 0.0

    # @TODO
    # Inside the function, create a for loop that iterates through the loans in the portfolio pass in as an argument to the function.

    for loan in portfolio:

        # @TODO
        # Create the variables that you will need to utilize over the course of determing the DCF values. These will similar to those created in Part 2.

        period = 1
        local_discounted_cash_flow = 0
        usd_discounted_cash_flow = 0

        loan_repayment_interval = loan['repayment_interval']
        loan_term_in_months = int(loan['term_in_months'])
        loan_interval_repayment_amount = int(loan['interval_repayment_amount'])
        loan_fx_rate_at_loan_issue = loan['fx_rate_at_loan_issue']

        # @TODO
        # As we have seen from prior activities, when working with monthly payment data it is important to sort based on the repayment_interval. Write the 3 conditional statements that sort the loan by repayment intervals.

        if loan_repayment_interval == 'monthly':

            # @TODO
            # With the loans imported to the function and the conditional statements written, it is time to address the discounted_cash_flow value calculation. Inside each of the conditional statements, copy the while loop written in the prior activity.

                # Hint - Be sure to change the syntax so the while loop is accessing data for all the loans rather than just the single one from the prior step.

                # HINT - Be sure to adjust the syntax for the discounted_cash_flow calculation to address the differences in monthly, quarterly and bullet payment periods.

            while period <= loan_term_in_months:
                local_discounted_cash_flow += loan_interval_repayment_amount / (1 + (discount_rate / 12))**period
                period += 1

            # @TODO
            # Because each loan has its own currency, the coversion from the foreign discounted_cash_flow value to the usd_discounted_cash_flow value needs to be executed inside the while loop using the fx_rate_at_loan_issue. This will need to be written inside each conditional.

            usd_discounted_cash_flow = local_discounted_cash_flow / loan_fx_rate_at_loan_issue

        if loan_repayment_interval == 'quarterly':

            while period <= (loan_term_in_months / 3):
                local_discounted_cash_flow += loan_interval_repayment_amount / (1 + (discount_rate / 4))**period
                period += 1

            usd_discounted_cash_flow = local_discounted_cash_flow / loan_fx_rate_at_loan_issue

        if loan_repayment_interval == 'bullet':

            local_discounted_cash_flow += loan_interval_repayment_amount / (1 + (discount_rate))

            usd_discounted_cash_flow = local_discounted_cash_flow / loan_fx_rate_at_loan_issue

        # @TODO
        # While still inside the function, add the newly calculated usd_discounted_cash_flow for a single loan to the usd_discounted_cash_flow_total variable that will hold the DCF value for the total portolio.

        usd_discounted_cash_flow_total += round(usd_discounted_cash_flow, 2)
        print('usd_discounted_cash_flow_total', round(usd_discounted_cash_flow_total, 2))

    # @TODO
    # When the function completes, return the usd_discounted_cash_flow_total figure so that it can be utilized outside the portfolio.

    return usd_discounted_cash_flow_total


# @TODO
# Create the call for the discounted_cash_flow_valuation function. Pass the microfinance_portfolio_data into the function.

    # HINT - It might make sense to set the function call equal to a variable so it can be utilized. A suggestion for a variable name is usd_discounted_cash_flow_total.

usd_discounted_cash_flow_total = discounted_cash_flow_valuation(microfinance_portfolio_data)

# @TODO
# Write the print statement that provides the US dollar value of the Discounted Cash Flows for the microfinance portfolio. Be sure to round the value to 2 decimal places.

print(f'Given a discount rate of .20, the fair value of this loan portfolio is ${usd_discounted_cash_flow_total: .2f}.')


# Challenge - Part 3 - Evaluation

# Given the number that resulted from your present value calculation, does the opportunity to invest in this
# microfinance portfolio meet your criteria?

# Do you think that any parameters should be changed when doing this analysis? Would that change the outcome of your investment decision?

# Please provide your thoughts and analysis in a separate text file that should also be included with your submission.
