#!/usr/bin/env python
# coding: utf-8

# # PyFlows
#
# In this activity you are going to import a file that contains a larger portfolio of loans.
#
# Once imported, the focus of your analysis will be to determine the amount of USD flows generated each month.
#
# Because, as investor who is passionate about microfinancing, you want to be able to turn these monthly cash in flows into additional loans.
#
# The first step in this activity will be to import CSV file containint the newest portfolio information.

# In[ ]:


# Instructions

# @TODO
# Import the Path library and module as well as the csv library

from pathlib import Path
import csv

# @TODO
# Create a variable that will initialize the line number variable for use when reviewing the csv file
# Initial a loans list to be build off of the loans in the csv file.

line_num = 0
loans = []


# @TODO
# Create a variable and assign it the module and file location of the csv file downloaded for this activity.

csvpath = Path('./Resources/mf_loans_csv.csv')


#@TODO
# Write the code that opens, reads, and prints the CSV file for review.

with open(csvpath, 'r') as csvfile:

    print(type(csvfile))

    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))

    header = next(csvreader)
    line_num +=1
    print(f'{header} <---HEADER')

    for row in csvreader:

        print(row)
        loans.append(row)

print('loans', loans)


 Loan Portfolio Format
#
# You will notice that our loan portfolio is in a slightly different format now.
#
# In the markdown box that follows, highlight the biggest difference between the format of the loan portfolio in the previous activity and the one you will be working with in this Phase.
#

Loan Portfolio Format -  Answer
#
# - Now a list of lists, rather than a list of dictionaries.
# - Key:Value pairs are gone; have to reference values by their index position.
# - Numerical values are strings rather than numbers. They will have to be converted.

# ## USD Receipts by Month
#
# In goal of this activity is to automate the process of accessing the approximate amount of US dollars to be received as payments for each month of the loan cycle.
#
# Because we want to automate this process to work with any loan portoflio, it makes sense to build a function that
#
# The function should take in three arguments, the loan portfolio, the month in question and return the
# US value of the loan payments.
#
# It would also make sense to utilize current fx rates for the three currencies so that the projected USD value is as current as possible.
#
#

# In[ ]:


# Instructions

# Fortunately, our loan portfolio has the period_payment value attached to each of the loans.
# With that, our function will focus on sorting through the repayment interval and term_in_months values to
# make out calculations.

# You also want to be able to apply current fx rates to the payments, this will reqire a second level sort on
# local_currency.

# As always, attempt to pseudocode the solution before writing the code.

# @TODO

# Initialize the variables for the current fx rates for each of the currencies.
    #HINT -  You will be able to access the current rates on Google.
# rates on Yahoo.
# Initialize the variable for the monthly USD inflow.

curr_fx_pkr = 157.15
curr_fx_kes = 102.48
curr_fx_inr = 74.06



# @TODO

# 1. Create the  monthly flows function as well as creating the function all. As mentioned, the function will
# take in 2 parameters, the loan portfolio and the month of the flows you would like calculate.


def convert_flow(loan):
    print('loan_cf', loan[7], loan[4])
    fx_flow = 0

    if loan[4]  == 'pkr':
        fx_flow = int(loan[7]) / curr_fx_pkr
        #print('flow', fx_flow)


    if loan[4]  == 'kes':
        fx_flow = int(loan[7]) / curr_fx_kes
        #print('flow', fx_flow)

    if loan[4]  == 'inr':
        fx_flow = int(loan[7]) / curr_fx_inr
        #print('flow', fx_flow)

    return fx_flow


def monthly_flows(portfolio, month):
    #print(portfolio)
    flow_total_usd = 0


    for loan in portfolio:

        if loan[3] == 'monthly':

            if month <= int(loan[1]):

                flow = int(loan[7])
                #print('flow-m', flow)

                flow_usd = convert_flow(loan)
                print('usd_m', flow_usd)



        if loan[3] == 'quarterly':

            if month <= int(loan[1]) and month % 3 == 0:

                flow = int(loan[7])
                #print('flow-q', flow)

                flow_usd = convert_flow(loan)
                print('usd_q', flow_usd)



        if loan[3] == 'bullet':

            if month == int(loan[1]):

                flow = int(loan[7])
                #print('flow-b', flow)

                flow_usd = convert_flow(loan)
                print('usd_b', flow_usd)


        flow_total_usd += flow_usd
        print('ft-in', flow_total_usd)

    return flow_total_usd

flow_total = monthly_flows(loans, 6)
print(f'The total USD flows for the month are ${round(flow_total, 2)}.')


# In[ ]:
