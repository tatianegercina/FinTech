#!/usr/bin/env python
# coding: utf-8

# # Phase 1 - PyPortfolio
#
# PyPortfolio is Phase 1 of the PyLending Challenge.
#
# In this part of the challenge you will be focused on using the building blocks of Python to  evaluate some of the basic information of the potential investment portfolio
#
# Follow the instructions detailed in each cell to complete this phase.
#

# ## Warmup - Iterating Through a List
#
# In this activity, you are provided with a list that contains the only the USD values of the total microfiance portfolio. Iterate through this list to determine the total USD value being lent.

# In[ ]:


# Micro-Finance Portfolio in USD as a Python List

portfolio_usd = [1000, 2500, 400, 750, 500, 250, 500, 1000, 2500, 300, 750, 1250, 500, 200, 800, 1000, 800]


# In[ ]:


# Instructions
# Using a loop,  iterate through portfolio_usd to determine the total USD value of the loans.
# Print the total value of loans using an f-string.


# @TODO
# Create your variable that will hold the total value in usd.

total_usd = 0


# @TODO
# Write the loop that will iterate through portfolio_usd and total up the value of the loans.

for loan in portfolio_usd:
    total_usd += loan

# @TODO
# Write the print statement that will display the total of the loans in USD.
# Use f-strings to construct the print statement.

print(f'The total of the loans in USD is ${total_usd}')


# ## Warmup - Bonus - Iterating Through an List of Dictionaries
#
# You will notice that your microfinance portfolio has now been presented as a list of dictionaries, rather than as the USD list detailed above. Each dictionary has been expanded to contain all of the information relevant to the loan and our activities:
#
#  * **loan_value_usd** - The value of the loan in US dollars. This can also be called the _principle_ of the loan.
#
#  * **term_in_months** - This is the length of the loan. It can also be called the _duration_ of the loan.
#
#  * **annual_interest_rate** - The is the expected return value of the loan for a period of 1 year.
#
#  * **repayment_interval** - This is the period at which you are expecting payment on the loan. Our loan payment will contain principle and interest. There are several repayment intervals represented in your portfolio:
#    * monthly - repayment will occur every month for the duration of the loan.
#    * quarterly - repayment will occur every 3 months, or once every quarter, for the duration of the loan.
#    * bullet - full repayment of principle and interest at the end of the term of the loan.
#
#  * **local_currency** - This is the currency of the country in which the person receiving the loan resides, or the local currency of the loan recipient. The loans are grouped by these currencies. Your loan has 3 different local currencies:
#    * pkr - Pakistani Rupee
#    * kes - Kenyan Schilling
#    * inr - Indian Rupee
#
#  * **usd_fx_issue** - This number represents the foreign exchange rate between USD and the local currency on the date that the loan was issued. All 3 of our foreign currencies are quoted in directly. To calculate the local value, or PKR value, of the first loan you would multiply:
#
# > local_value_usd * usd_fx_issue = loan_local_value ==> 1000 usd * 162.76 fx = 162,760 pkr
#
# This activity is focused on iterating through lists as well as accessing specific key:value pairs within a dictionary.

# In[ ]:


# Full Microfinance portfolio as a Python List of Dictionaries (or dicts).

portfolio_mf = [
    {'loan_value_usd': 1000,'term_in_months': 9 , 'annual_interest_rate': 0.37, 'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 2500,'term_in_months': 6 , 'annual_interest_rate': 0.40, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 400 ,'term_in_months': 4 , 'annual_interest_rate': 0.35, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 750 ,'term_in_months': 12, 'annual_interest_rate': 0.3825, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 500 ,'term_in_months': 12, 'annual_interest_rate': 0.395, 'repayment_interval': 'bullet', 'local_currency':'pkr', 'usd_fx_issue': 162.76},
    {'loan_value_usd': 250 ,'term_in_months': 12 , 'annual_interest_rate': 0.45, 'repayment_interval': 'monthly', 'local_currency':'kes','usd_fx_issue': 103.28},
    {'loan_value_usd': 500 ,'term_in_months': 9 , 'annual_interest_rate': 0.375, 'repayment_interval': 'monthly', 'local_currency':'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 1000,'term_in_months': 6 , 'annual_interest_rate': 0.425, 'repayment_interval': 'quarterly', 'local_currency':'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 2500,'term_in_months': 3 , 'annual_interest_rate': 0.70, 'repayment_interval': 'bullet', 'local_currency':'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 300 ,'term_in_months': 6 , 'annual_interest_rate': 0.45, 'repayment_interval': 'bullet', 'local_currency':'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 750 ,'term_in_months': 12 , 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly', 'local_currency':'kes', 'usd_fx_issue': 103.28},
    {'loan_value_usd': 1250 , 'term_in_months': 12 , 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 500 , 'term_in_months': 6 , 'annual_interest_rate': 0.25, 'repayment_interval': 'quarterly','local_currency': 'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 200 ,'term_in_months': 3 , 'annual_interest_rate': 0.35, 'repayment_interval': 'bullet', 'local_currency':'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 800 ,'term_in_months': 12 , 'annual_interest_rate': 0.325, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 1000 ,'term_in_months': 6 , 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18},
    {'loan_value_usd': 800 ,'term_in_months': 12 , 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly', 'local_currency':'inr', 'usd_fx_issue': 69.18},
]


# In[ ]:


# Instructions
# In this next activity, you will interate through the full microfinance portfolio's list of dicts.
# The goal of this activity is to find 4 values:
    # The total value of the portfolio in USD (hint: this should match your number from above.)
    # The percentage of the total portfolio that consists of loans issued in 'pkr'.
    # The percentage of the total portfolio that consists of loans issued in 'kes'.
    # The percentage of the total portfolio that consists of loans issued in 'inr'.
# Print the results of these 4 values using f-strings.

# REMEMBER - Pseudocode the solution in terms of the Python building blocks (variables, loops and conditionals)
# before writing any code.


# @TODO
# Create the 4 variables you will need to hold the overall total in usd, and each of the totals in the currencies.

total_usd = 0
loans_pkr = 0
loans_kes = 0
loans_inr = 0


# @TODO
# 1. Construct the for loop that will allow you to iterate through portfolio_mf

# 2. Write the code that will total the usd value of the portfolio.

    # HINT - You are now iterating through a list of dicts. You will need to use bracket notation to access
    # the value of the key:value pair in question.

    # HINT - You will need to utilize the "double equal" in order to compare values.

# 3. Once you confirm that the usd value is totaling correctly, write the conditional statements that allow
# you to total the usd value of all the loans issued in pkr, kes and inr, respectively.

# HINT - You will need an **if** statement, an **elif** statement and and **else**.

for loan in portfolio_mf:

    total_usd += loan['loan_value_usd']

    if loan['local_currency'] == 'pkr':
        loans_pkr +=  loan['loan_value_usd']

    elif loan['local_currency'] == 'kes':
        loans_kes += loan['loan_value_usd']

    else:
        loans_inr += loan['loan_value_usd']

# @TODO
# Use f-strings to display the values.
# 1. Code the print statements that will display the total value of the portfolio in USD.

# 2. Code the print statements the display the percentage that each block of foreign currencies makes
# up of the total.

# Challenge - round the percentage values to only 2 decimal places.


print(f'The size fo the portfolio in USD is ${total_usd}.')
print(f'The percent of PRK loans in the portfolio is {round((loans_pkr/total_usd)*100, 2)}%.')
print(f'The percent of KES loans in the portfolio is {round((loans_kes/total_usd)*100, 2)}%.')
print(f'The percent of INR loans in the portfolio is {round((loans_inr/total_usd)*100, 2)}%.')


# ## Calculating Loan Local Value
#
# In the final activity associated with the first part of this week's challenge, you will be asked to calculate the local currency value of each of the loans and then add that calculation to the respective dictionary.
#
# For instance, the loan_value_pkr is calculated by multiplying the loan_value_usd by usd_fx_issue.
#
# This activity is designed to give you additional practice with createing the appropriate variables, working with for loops and conditional statements, and calculating value using Python.

# In[ ]:


# Instructions
# In this next exercise, calculate the local currency value for each of the loans.
    # Designate the local value loan_value_pkr, loan_value_kes and loan_value_inr.
# Once calculated, add that value to the respective dictionary.
# Challenge - calculate the total amount of each local currency that was distributed on issue date.


# REMEMBER - Read through all of the instructions and then pseudocode the solution in terms of the
# Python building blocks (variables, loops and conditionals) before writing any code.


# @TODO
# If undertaking the challenge: create the 3 variables that will hold the local currency total
# of each of the loan currencies: pkr, kes and inr. .

total_loans_pkr = 0
total_loans_kes = 0
total_loans_inr = 0



# @TODO
# 1. Create the for-loop that will iterate through portfolio_mf.

# 2. Create the conditional statements that will allow you to determine the currency of the loan under review.

    # HINT - You are working with dictionary and will need to use the bracket notation to access the keys.
    # HINT - You will need to utilize the "double equal" in order to compare values.

# 3. Write the code that calculates the value of the loan. You will need to assign the calculation to a variable.
# For example:  loan_value_pkr = loan['loan_value_usd'] * loan['usd_fx_issue']

# 4. **Update** the loan dictionary with a key:value pair where the key is always **loan_value_local**
# and the value is the value of the loan calculated in the prior step.

# 5. If you are undertaking the challenge, add the loan's value in local currency to the total value of the
# loans in that currency.




for loan in portfolio_mf:
    if loan['local_currency'] == 'pkr':
        loan_value_pkr = loan['loan_value_usd'] * loan['usd_fx_issue']
        loan.update({'loan_value_local': '%.0f'%loan_value_pkr})
        total_loans_pkr += loan_value_pkr

    if loan['local_currency'] == 'kes':
        loan_value_kes = loan['loan_value_usd'] * loan['usd_fx_issue']
        loan.update({'loan_value_local': '%.0f'%loan_value_kes})
        total_loans_kes += loan_value_kes

    if loan['local_currency'] == 'inr':
        loan_value_inr = loan['loan_value_usd'] * loan['usd_fx_issue']
        loan.update({'loan_value_local': '%.0f'%loan_value_inr})
        total_loans_inr += loan_value_inr



# @ TODO
# Write the print statement for the first loan in portfolio_mf to confirm that you have added the
# **loan_value_local** key:pair to the dictionary.

print(portfolio_mf[0])


# @ TODO
# If undertaking the challenge, write print statements that show the total loans issues in each of
# the respective currencies.
# Be sure to use f-strings.

print(f'The total amount of PKR loans issued was {round(total_loans_pkr)}.')
print(f'The total amount of KES loans issued was {round(total_loans_kes)}.')
print(f'The total amount of INR loans issued was {round(total_loans_inr)}.')


# In[ ]:
