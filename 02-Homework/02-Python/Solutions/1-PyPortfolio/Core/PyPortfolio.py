# -*- coding: utf-8 -*-

# # Phase 1 - PyPortfolio - Core

# PyPortfolio is Phase 1 of the PyLending Challenge.

# In this part of the challenge you will be focused on using the building blocks
#  of Python to  evaluate some of the basic information of the potential
# investment portfolio.

# Follow the instructions detailed in each of the 3 parts to complete this phase.

# NOTE - This is a Core activity so all parts should be completed.

print('--------Part 1------------')

# Part 1 - Warmup - Iterating Through a List

# In this activity, you are provided with a list that contains the only the USD
# values of the total microfiance portfolio. Iterate through this list to
# determine the total USD value being lent.


# MicroFinance Portfolio in USD as a Python List

portfolio_usd = [1000, 2500, 400, 750, 500, 250, 500, 1000, 2500, 300, 750,
                 1250, 500, 200, 800, 1000, 800]


# Instructions
# Using a loop,  iterate through portfolio_usd to determine the total USD value
# of the loans.

# Print the total value of loans using an f-string.


# @TODO
# Create a global variable that will hold the total value in usd.

total_usd = 0


# @TODO
# Write the loop that will iterate through portfolio_usd.


for loan in portfolio_usd:

    # @TODO
    # Inside the for loop, write the equation that will add each loan to the
    # total US dollar global variable.

    total_usd += loan

# @TODO
# Write the print statement that will display the total of the loans in USD.
# Use f-strings to construct the print statement.

print(f'The total of the loans in USD is ${total_usd}')


print('--------Part 2------------')


#  Part 2 - Iterating Through an List of Dictionaries

# You will notice that your microfinance portfolio has now been presented as a
# list of dictionaries, rather than as the USD list detailed above. Each
# dictionary has been expanded to contain all of the information relevant to
# the loan and our activities:

# A description of all of the dictionary keys is as follows:

#  loan_value_usd - The value of the loan in US dollars. This can also be
#  calledthe _principle_ of the loan.

#  term_in_months - This is the length of the loan. It can also be called
# the 'duration' of the loan.

#  annual_interest_rate - The is the expected return value of the loan for a
#  period of 1 year.

#  repayment_interval - This is the period at which you are expecting
#  payment on the loan. Our loan payment will contain principle and
#  interest. There are several repayment intervals represented in your
#  portfolio:

#   monthly - repayment will occur every month for the duration of the loan.
#   quarterly - repayment will occur every 3 months, or once every quarter,
#   for the duration of the loan.
#   bullet - full repayment of principle and interest at the end of the
#   term of the loan.

#  local_currency - This is the currency of the country in which the person
#  receiving the loan resides, or the local currency of the loan recipient.
#  The loans are grouped by these currencies. Your loan has 3 different
#  local currencies:
#   pkr - Pakistani Rupee
#   kes - Kenyan Schilling
#   inr - Indian Rupee

#  usd_fx_issue - This number represents the foreign exchange rate between
#  USD and the local currency on the date that the loan was issued. All 3
#  of our foreign currencies are quoted indirectly, that is 1 usd to the
#  amount of foreign currency. To calculate the local value, or PKR value,
#  of the first loan you would multiply:

# > local_value_usd * usd_fx_issue = loan_local_value
# > 1000 usd * 162.76 fx = 162,760 pkr

# This activity is focused on iterating through lists as well as accessing
# specific key:value pairs within a dictionary.


# Full Microfinance portfolio as a Python List of Dictionaries (or dicts).

microfinance_portfolio_data = [
    {'loan_value_usd': 1000, 'term_in_months': 9, 'annual_interest_rate': 0.37,
     'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 2500, 'term_in_months': 6, 'annual_interest_rate': 0.40,
     'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 400, 'term_in_months': 4, 'annual_interest_rate': 0.35,
     'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.3825,
     'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 500, 'term_in_months': 12, 'annual_interest_rate': 0.395,
     'repayment_interval': 'bullet', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 250, 'term_in_months': 12, 'annual_interest_rate': 0.45,
     'repayment_interval': 'monthly', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 500, 'term_in_months': 9, 'annual_interest_rate': 0.375,
     'repayment_interval': 'monthly', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.425,
     'repayment_interval': 'quarterly', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 2500, 'term_in_months': 3, 'annual_interest_rate': 0.70,
     'repayment_interval': 'bullet', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 300, 'term_in_months': 6, 'annual_interest_rate': 0.45,
     'repayment_interval': 'bullet', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 750, 'term_in_months': 12, 'annual_interest_rate': 0.35,
     'repayment_interval': 'quarterly', 'local_currency': 'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 1250, 'term_in_months': 12, 'annual_interest_rate': 0.30,
     'repayment_interval': 'monthly', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 500, 'term_in_months': 6, 'annual_interest_rate': 0.25,
     'repayment_interval': 'quarterly', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 200, 'term_in_months': 3, 'annual_interest_rate': 0.35,
     'repayment_interval': 'bullet', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.325,
     'repayment_interval': 'monthly', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 1000, 'term_in_months': 6, 'annual_interest_rate': 0.30,
     'repayment_interval': 'monthly', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 800, 'term_in_months': 12, 'annual_interest_rate': 0.35,
     'repayment_interval': 'quarterly', 'local_currency': 'inr', 'usd_fx_issue': 69.18},
]

# Instructions

# In this next activity, you will interate through the full microfinance
# portfolio's list of dicts.

# The goal of this activity is to find 4 values:
# 1. The total value of the portfolio in USD.
# HINT: this should match your number from above.
# 2. The percentage of the total portfolio that consists of loans issued in 'pkr'.
# 3. The percentage of the total portfolio that consists of loans issued in 'kes'.
# 4. The percentage of the total portfolio that consists of loans issued in 'inr'.

# Finally, print the results of these 4 values using f-strings.

# NOTE - Review the problem and then attempt to pseudocode the solution in terms
# of the Python building blocks (variables, loops and conditionals) before
# writing any code.


# @TODO
# Create the 4 global variables you will need to hold the overall total in usd,
# and each of the totals in the three currencies.  For example the variable
# associated with the PRK loans could be loans_prk.

# NOTE - As these variables involve currencies, it would make sense to
# instantiate them as floating point numbers.

total_usd = 0.0
loans_pkr = 0.0
loans_kes = 0.0
loans_inr = 0.0


# @TODO
# Construct the for loop that will allow you to iterate through the
# microfinance_portfolio_data

for loan in microfinance_portfolio_data:

    # @TODO
    # Inside the for loop, write the code that will loop through each loan,
    # summing the usd value of the whole portfolio.

        # HINT - You are now iterating through a list of dicts. You will need to
        #  use bracket notation to access the value of the key:value pair in question.

    total_usd += loan['loan_value_usd']

    # @TODO
    # Now focus on totaling the three local_currency values issued across the
    # portfolio of loans.

    # 1. Start by writing the 3 conditional statements that will differentiate
    # loans by currency, either pkr, kes or inr.

    # HINT: Think 'if' statement, an 'elif' statement and
    # and 'else'.

    # HINT:You will need to utilize the "double equal" in order to
    #  compare values.

    # 2. With 3 conditional statements written, add the code that will
    # sum the loan_value_usd of each respective currency.

    if loan['local_currency'] == 'pkr':
        loans_pkr += loan['loan_value_usd']

    elif loan['local_currency'] == 'kes':
        loans_kes += loan['loan_value_usd']

    else:
        loans_inr += loan['loan_value_usd']

# @TODO
# 1. Using an 'f' string modifier, code the print statements that will display the
# total value of the portfolio in USD.

# 2. Using an 'f' string modifier, code the print statements the display the
# percentage that each block of foreign currency loans make up of the total.

# Bonus - round the percentage values to only 2 decimal places.


print(f'The size fo the portfolio in USD is ${total_usd}.')
print(f'The % of PRK loans in the portfolio: {round((loans_pkr/total_usd)*100, 2)}%.')
print(f'The % of KES loans in the portfolio: {((loans_kes/total_usd)*100): .2f}%.')
print(f'The % of INR loans in the portfolio: {((loans_inr/total_usd)*100): .2f}%.')


print('--------Part 3------------')


# Part 3 - Calculating Loan Local Value

# Instructions:

# In the final activity of PyPortfolio, you are going to:

# 1. Calculate the local currency value of each of the loans
# 2. Update the loan's dictionary entry with a key:value pair with the value
# of the calculation.
# Bonus - calculate the total amount of each local currency that was
# distributed on issue date.

# An example of the calculation:
# loan_value_usd *  usd_fx_issue = loan_value_pkr

# A simplified example of the dictionary update:
# loan['loan_value_local'] = {loan_value_pkr}

# This activity is designed to give you additional practice with createing the
# appropriate variables, working with for loops and conditional statements,
# and calculating value using Python.

# NOTE - Read through all of the instructions and then pseudocode the
# solution in terms of the Python building blocks (variables, loops and
# conditionals) before writing any code.

# @TODO
# If you are doing the Bonus, create the 3 global variables that will each
# hold the local currency total of the loan currencies: pkr, kes and inr. .

# NOTE - As these variables involve currencies, it would make sense to
# instantiate them as floating point numbers.

total_loans_pkr = 0.0
total_loans_kes = 0.0
total_loans_inr = 0.0


# @TODO
# Create the for-loop that will iterate through microfinance_portfolio_data.

for loan in microfinance_portfolio_data:

    # @TODO
    # Inside the for loop, create the 3 conditional statements that will sort
    # for the currency of the loan under review. Start with currency 'pkr'.

    # HINT - These should be the same conditional statements written in Part 2.

    if loan['local_currency'] == 'pkr':

        # @TODO
        # Inside each conditional statements, write the code that calculates the
        # local value of the loan. For example:
        # loan_value_pkr = loan['loan_value_usd'] * loan['usd_fx_issue']

        loan_value_pkr = loan['loan_value_usd'] * loan['usd_fx_issue']

        # @TODO
        # Again inside each conditional statement, update the loan dictionary
        # with a key:value pair where the key is always **loan_value_local**
        # and the value is the value of the loan calculated in the prior step.
        # Bonus - round the loan value to a whole number.

        loan['loan_value_local'] = f'{loan_value_pkr: .0f}'

        # @TODO
        # If you are doing the Bonus, add the calculated local loan value of
        # global variable created to hold the total amount of loans in that
        # currency.

        total_loans_pkr += loan_value_pkr

    # @TODO
    # Follow the steps detailed above for the KES currency loans

    if loan['local_currency'] == 'kes':
        loan_value_kes = loan['loan_value_usd'] * loan['usd_fx_issue']
        loan['loan_value_local'] = f'{loan_value_kes: .0f}'
        total_loans_kes += loan_value_kes

    # @TODO
    # Follow the steps detailed above for the INR currency loans

    if loan['local_currency'] == 'inr':
        loan_value_inr = loan['loan_value_usd'] * loan['usd_fx_issue']
        loan['loan_value_local'] = f'{loan_value_inr: .0f}'
        total_loans_inr += loan_value_inr


# @TODO
# Write the print statement for the first loan in microfinance_portfolio_data to
# confirm that you have added the **loan_value_local** key:value pair to the
# dictionary.

first_loan = microfinance_portfolio_data[0]
print(f'The first loan in the portfolio is: {first_loan}.')


# @TODO
# If undertaking the Bonus, write print statements that show the total loans
# issues in each of the respective currencies.
# Be sure to use f-strings for the print statements.

print(f'The total of PKR loans issued was {total_loans_pkr: .0f}.')
print(f'The total of KES loans issued was {total_loans_kes: .0f}.')
print(f'The total of INR loans issued was {round(total_loans_inr)}.')
