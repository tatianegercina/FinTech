# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# National Bank of Canada: 327
# Toronto-Dominion Bank: 302
# Royal Bank of Canada: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# Canadian Imperial Bank of Commerce: 83
# TD Bank: 108
# Bank of Montreal: 67
# Capital One: 47
# FNB Corporation: 4
# Laurentian Bank of Canada: 3
# Ally Financial: 12
# Montreal Trust Company: 145
# Canadian Western Bank: .97

# Initialize a dictionary of banks and market caps (in billions)
banks = {
    "National Bank of Canada": 327,
    "Toronto-Dominion Bank": 302,
    "Royal Bank of Canada": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "Canadian Imperial Bank of Commerce": 83,
    "TD Bank": 108,
    "Bank of Montreal": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "Laurentian Bank of Canada": 3,
    "Ally Financial": 12,
    "Montreal Trust Company": 145,
    "Canadian Western Bank": .97
}

# Change the market cap for 'Citigroup'
banks['Royal Bank of Canada'] = 170

# Add a new bank and market cap pair
banks['Scotiabank'] = 33

# Remove a bank from the dictionary
del banks['Montreal Trust Company']

# Print the modified dictionary
print(banks)
