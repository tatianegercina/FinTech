# -*- coding: utf-8 -*-

# Phase 3 - PyFlows - Core


# As investor who is passionate about micro-financing, you are interested in
# determining if the interest generated for the newly-expanded loan portfolio
# can finance additional purchases of new loans.
#
#  The inquiry will require you to determine the US dollar cash flows generated
# by the portfolio each month.


print('--------Activity 1------------')


# Activity 1 - Importing the CSV

# No longer is there a Python List containing the portfolio information. The
# number of loans in the portfolio has grown and it is not kept in a CSV file.

# The first step in this activity will be to import the CSV from the Resources
# folder.

# Instructions

# Utilizing the instructions from the curriculum content...


# @TODO
# Import the Path library and module as well as the csv library

from pathlib import Path
import csv

# @TODO
# Create a variable that will initialize the line number variable for use when
# reviewing the csv file
# Initial a loans list to be build off of the loans in the csv file.

line_num = 0
microfinance_loan_portfolio = []


# @TODO
# Create a global variable and assign it the module and file location of the CSV
# file for this activity. You will find the CSV file located in the Resources
# folder for the Phase.

csvpath = Path('../Resources/microfinance_loan_portfolio.csv')


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

# @TODO
# Write the print statement that displays the imported portfolio.

print(f"The imported microfinance loan portfolio looks like: {microfinance_loan_portfolio}")


print('--------Activity 2------------')



# Activity 2 - Loan Portfolio Format

# You will notice that the loan portfolio is in a slightly different format now.

# In a separate text file, compare and contrast the differences between the newly
# imported file and and the one with which you had previously been working.


# ANSWERS - Loan Portfolio Format
# Now a list of lists, rather than a list of dictionaries.
# Key:Value pairs are gone; have to reference values by their index position.
# Numerical values are strings rather than numbers. They will have to be
# converted.


print('--------PyCashFlow_Extension------------')

# Congratulations on getting the CSV file imported! 
# The loan portfolio is required for the PyCashFlows_Extension activities.
# There will be a place to copy/paste this code into the Extension file. 

# To work through the Extension activities, navigate to the Extension folder
# and the PyCashFlows_Extension.py starter code.

# REMINDER: Extension activities are designed to stretch your knowledge and
# abilities. Your grade will not be penalized for not completing these
# activities, but they should be attempted.
