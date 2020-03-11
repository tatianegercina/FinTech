#!/usr/bin/env python
# coding: utf-8

# # Phase 2 - PyNPV
#
# In Phase 2 of the PyLending challenge, you are looking to evaluate the current net present value (NPV) of the portfolio. You are looking to determine if, at the present NPV, the portfolio meets your investment return critera of approximately 15%.
#
# This activity is designed to give you practice with building and calling functions.

# In[ ]:


# Note that the portfolio we will be evaluating is the same as from Phase 1, only it includes
# the 'loan_local_value' key:value pair in each object.

portfolio_mf = [
    {'loan_value_usd': 1000,'term_in_months': 9 , 'annual_interest_rate': 0.37, 'repayment_interval': 'monthly', 'local_currency': 'pkr', 'usd_fx_issue': 162.76, 'loan_local_value': 162760 },
    {'loan_value_usd': 2500,'term_in_months': 6 , 'annual_interest_rate': 0.40, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76, 'loan_local_value': 406900},
    {'loan_value_usd': 400 ,'term_in_months': 4 , 'annual_interest_rate': 0.35, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76, 'loan_local_value': 65104},
    {'loan_value_usd': 750 ,'term_in_months': 12, 'annual_interest_rate': 0.3825, 'repayment_interval': 'monthly', 'local_currency':'pkr', 'usd_fx_issue': 162.76, 'loan_local_value': 122070},
    {'loan_value_usd': 500 ,'term_in_months': 12, 'annual_interest_rate': 0.395, 'repayment_interval': 'bullet', 'local_currency':'pkr', 'usd_fx_issue': 162.76, 'loan_local_value': 81380},
    {'loan_value_usd': 250 ,'term_in_months': 12, 'annual_interest_rate': 0.45, 'repayment_interval': 'monthly', 'local_currency':'kes','usd_fx_issue': 103.28, 'loan_local_value': 25820},
    {'loan_value_usd': 500 ,'term_in_months': 9 , 'annual_interest_rate': 0.375, 'repayment_interval': 'monthly', 'local_currency':'kes', 'usd_fx_issue': 103.28, 'loan_local_value': 51640},
    {'loan_value_usd': 1000,'term_in_months': 6 , 'annual_interest_rate': 0.425, 'repayment_interval': 'quarterly', 'local_currency':'kes', 'usd_fx_issue': 103.28, 'loan_local_value': 103280},
    {'loan_value_usd': 2500,'term_in_months': 3 , 'annual_interest_rate': 0.70, 'repayment_interval': 'bullet', 'local_currency':'kes', 'usd_fx_issue': 103.28, 'loan_local_value': 258200},
    {'loan_value_usd': 300 ,'term_in_months': 6 , 'annual_interest_rate': 0.45, 'repayment_interval': 'bullet', 'local_currency':'kes', 'usd_fx_issue': 103.28, 'loan_local_value': 30984},
    {'loan_value_usd': 750 ,'term_in_months': 12, 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly', 'local_currency':'kes', 'usd_fx_issue': 103.28, 'loan_local_value': 77460},
    {'loan_value_usd': 1250,'term_in_months': 12, 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 86475},
    {'loan_value_usd': 500 ,'term_in_months': 6 , 'annual_interest_rate': 0.25, 'repayment_interval': 'quarterly','local_currency': 'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 34590},
    {'loan_value_usd': 200 ,'term_in_months': 3 , 'annual_interest_rate': 0.35, 'repayment_interval': 'bullet', 'local_currency':'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 13836},
    {'loan_value_usd': 800 ,'term_in_months': 12, 'annual_interest_rate': 0.325, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 55344},
    {'loan_value_usd': 1000,'term_in_months': 6 , 'annual_interest_rate': 0.30, 'repayment_interval': 'monthly', 'local_currency':'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 69180},
    {'loan_value_usd': 800 ,'term_in_months': 12, 'annual_interest_rate': 0.35, 'repayment_interval': 'quarterly', 'local_currency':'inr', 'usd_fx_issue': 69.18, 'loan_local_value': 55344},
]


# ## Before PV, Period Payments
#
#
# As examined in our lessons, we know that determining the NPV of a loan involves calculating the present value of a series of cash flows (or loan payments) based on a specified discount rate.
#
# Based on that statement, in order to calculate the present values of each loan, we must first determine the the payment per period that will be made to pay back each loan.
#
# The formula for determing the period payment of loan is as follows:
#
# > Payment = loan value * rate_per_period / 1 - (1 + rate per period)**-number_payment_periods
#
# In examining our loan data, we note that there are 3 different repayment intervals:
#  * monthly - a payment will be made each month for the duration of the loan
#  * quarterly - a payment will be made each quarter (or once every 3 months for the duration of the loan
#  * bullet - a single payment of principle and interest will be made at the retirement of the loan
#
# In order to correctly calculate the cash flows for each loan, we will need to take these repayment intervals into account.
#
# Because these loans were made to the individuals in local currency, you will want to make these payment calculations using the loan_local_value.
#
# With this information and the formula in hand, it is time to determine the period payment associated with each of the loans.
#
#
# Note:  For the purposes of this activity, you can assume that the payments will include both principle and interest.
#
#

# In[ ]:


# Instructions
# In this exercise, you are going to work through the function for calculating the period payments
# for each loan. Once the period payment is calculated, you will want to append a
# 'period_payment' key:value pair to the dictionary.

# Before beginning to code, read through the steps and attempt to work through the program using pseudocode.


# @TODO
# 1. Create the for loop to iterate through each loan in the portfolio_mf list.

# 2. Create a series of conditional statements that take into account the repayment_interval of the
# as that will effect our calculation.

    # HINT - Don't forget that each loan is a dictionary. You will need to use bracket notation to access keys.
    # HINT - You will need to utilize the "double equal" in order to compare values.

# 3. Once your conditional statements are in place, begin to focus on determining the values you will need for
# the payment calculation formula: loan value, rate per period, and the number of periods (or duration) of the loan.

    # Create a variabel called rate_per_period inside each of the conditional statements. Assign that variable
    # the value equal to the annual_interest_rate divided by the number of payments per year.


    # HINT -  the duration of our loans is less than 1 year so the annual_interest_rate will only
    # need to be divided by the repayment period to determine the rate per period.

    # HINT - The annual_interest_rate is already quoted as a decimal so it will not need to be converted.

# 4. Create a second variable inside each conditional called number_payment_periods. The value assigned should
#reflect the relations ship between the term_in_months of the loan and the number for payments expected for the
#year. For instance, if the term_in_months of the loan is 6 and the repayment_interval is quarterly,
# the number_payment_periods is 2.

# 5. Under each conditional, Create a variable called period_payment and set it equal to the equation detailed above
# using loan_local_value for the value of the loan.

# 6. Update date the loan dictionary with a key called period_payment and a value equal to the
# period_payment calculation from step 5.

# 7. As the last step, print out a dictionary from portfolio_mf that details each of the repayment_intervals so you
# can confirm that each now contians a period_payment key.

for loan in portfolio_mf:

    if loan['repayment_interval'] == 'monthly':
        rate_per_period = loan['annual_interest_rate']/12
        number_payment_periods = loan['term_in_months']
        period_payment = (loan['loan_local_value'] * rate_per_period) / (1 - (1 + rate_per_period)**-number_payment_periods)
        loan.update({'period_payment': '%.0f'%period_payment})




    if loan['repayment_interval'] == 'quarterly':
        rate_per_period = loan['annual_interest_rate']/4
        number_payment_periods = loan['term_in_months'] / 3
        period_payment = (loan['loan_local_value'] * rate_per_period) / (1 - (1 + rate_per_period)**-number_payment_periods)
        loan.update({'period_payment': '%.0f'%period_payment})




    if loan['repayment_interval'] == 'bullet':
        rate_per_period = (loan['annual_interest_rate']/12)*loan['term_in_months']
        number_payment_periods = 1
        period_payment = (loan['loan_local_value'] * rate_per_period) / (1 - (1 + rate_per_period)**-number_payment_periods)
        loan.update({'period_payment': '%.0f'%period_payment})


print(portfolio_mf[0])
print(portfolio_mf[5])
print(portfolio_mf[11])


# # Now,  Present Value
#
# Now that you have the local period_payments value in place for each dictionary, it should be much easier to calculate the present value of the porfolio.
#
# To determine the fair value, or present value, of these loans you will utilize the discounted cash flow (DCF) model. You will take the sum of each of the future cash payments as viewed through the lense of an assigned discount rate and the time period of the payment.
#
# > FV = period_payment/(1 + discount_rate)^1st_period + period_payment/(1 + discount_rate)^2st_period  +...+ period_payment/(1 + discount_rate)^last_period
#
# The discount rate is very important to DCF calculations. Two factors form the basis of the discount rate - the time value of money and uncertainty risk. The higher the discount rate the larger the uncertainty of the investment. generally thought of as the alternative investment rate. When valuing a company the discount rate is often determined by an educated guess. For valuing loans, the discount rate used is often the Federal Reserve's lending rate.
#
# For this activity, you are going to use a discount rate of 20%. This is the average rate of microfinance loans in the US, which is your most likely investment alternative to this international loan portfolio.
#
# Rather than jumping in to calculating the fair value of the entire portfolio, you will start by calculating the fair value of the first loan.
#

# In[ ]:


# Instructions

# Step 1 one in determining the fair value of the bond portfolio will involve calculating the fair value of
# the first bond.

# The following print statement will allow you to see the values that we will be using in the DCF model.

print(portfolio_mf[0])

# As always, try to pseudocode the problem before writing the code. If you understand the flow on paper, it will
# make much more sense as you try to trouble shoot issue.


# @TODO
# Start by creating the variables you will need.
    # It would make sense to have one to hold the discount rate, one to iterate through the time period
    # calculation and one to hold the value of the discounted cash flow.

discount_rate = .2
period = 1
dcf = 0
usd_dcf = 0

# @TODO
# 1. Start by constructing the loop that will iterate throught the time periods. Up to now, we have used for loops,
# this activity will require a while loop. The while loop should contain and indexing variable AND a
# condition statement based of the term_in_months key.

# WARINING - don't forget to increment the index variable (time period) inside the while loop or it will
# never meet the condition.

# 2. Define the expression that will calculate the dcf amount based on the formula provided above. You should
# be using the 'period_payment' key to calculate the cash flow.

# 3. The current value flowing to the dcf variable is in the foreign currency. It would make sense to evaluate
# the cash flows in terms of US dollars. Add an if statementto process a fx coversion back to USD.
# At this stage, you can just use the usd_fx_issue key.

# HINT - You will most likely need to add an additional global variable to capture the USD value.

# 4. Print your USD dcf value.

#Does the number you see make sense with regard to the initial USD value of the loan?
#If so, move on to the step of coverting this code into a function that can loop through
# all of the loans.




while period <= int(portfolio_mf[0]['term_in_months']):
    dcf += int(portfolio_mf[0]['period_payment']) / (1 + (discount_rate/12))**period
    #print('dcf', dcf )
    period += 1


print(f'The foreign currency amount of the dcf model is {round(dcf)}.')

usd_dcf = dcf / portfolio_mf[0]['usd_fx_issue']

print(f'The USD value of the loan based on the dcf model is ${round(usd_dcf, 2)}.')





# ## Functions
#
# The goal of a function is to reformulate a code block that does a single task into a code block that can
# process an action repeatedly.
#
# Understandably, creating functions is extremely important to the concept of task automation.
#
# The goal of this part of the activity is to covert the code block that handles the dcf model for a single loan
# into one that can process the dcf model for any number of loans in the portfolio.

# In[ ]:


# Instructions

# Utilizing the code block built in the step above, write a function that takes in the loan portofolio
# and process the dcf calculation for each loan individually and then add them together to produce a
# single dcf value.

# @TODO
# Start by recreating your global variables from the step above.

discount_rate = .2
usd_dcf_total = 0
usd_dcf_total_list = []

total = 0

# @TODO

# 1. Start by creating a function called dcf_valuation. At this stage, it is also worth putting the function call
# at the bottom of this code cell. Pass the loan portfolio into the function and print it. It is always good
# to test that the information you want to use will be available.

# 2. Given that we are passing in a full portfolio of loans into the function, write the code that will allows
# access just one loan in that portfolio at a time.

# 3. As we have seen from prior activities, when working with monthly payment data it is important to sort based
# on the repayment_interval. Add the conditional statements that allow for that sorting as you process each loan.

# 4. With the loans imported to the function and the ability to access and sort them in place, it is time to
# address the dcf value calculation. Copy the while loop from the above step inside each conditional statement.

# Hint - Be sure to change the syntax so the while loop is accessing data for all the loans rather than
#just the single one from the prior step.

# 5. Adjust the syntax for the dcf calculation to address the differences in monthly, quarterly and bullet
# payment periods.

# 6. Because each loan has its own currency, the coversion from the foreign dcf value to the usd dcf value needs
# to be executed inside the while loop using the loan's fx rate.

# 7. Add the code that nets each calculation


def dcf_valuation(portfolio):
    usd_dcf_total = 0

    for loan in portfolio:
        period = 1
        dcf = 0
        usd_dcf = 0

        if loan['repayment_interval'] == 'monthly':

            while period <= int(loan['term_in_months']):
                dcf += int(loan['period_payment']) / (1 + (discount_rate/12))**period
                print('dcf', dcf )
                period += 1

            usd_dcf = dcf / loan['usd_fx_issue']
            print('usd_dcf', usd_dcf)



        if loan['repayment_interval'] == 'quarterly':

            while period <= int((loan['term_in_months']/3)):
                dcf += int(loan['period_payment']) / (1 + (discount_rate/4))**period
                print('dcf', dcf )
                period += 1

            usd_dcf = dcf / loan['usd_fx_issue']
            print('usd_dcf', usd_dcf)



        if loan['repayment_interval'] == 'bullet':

            dcf += int(loan['period_payment']) / (1 + (discount_rate))
            print('dcf', dcf )
            period += 1

            usd_dcf = dcf / loan['usd_fx_issue']
            print('usd_dcf', usd_dcf)



        usd_dcf_total += round(usd_dcf, 2)
        print('usd_dcf_total', round(usd_dcf_total, 2))

        usd_dcf_total_list.append(round(usd_dcf, 2))
        print('usd_dcf_total_list', usd_dcf_total_list)


    return usd_dcf_total

usd_dcf_total= dcf_valuation(portfolio_mf)
print('outside', usd_dcf_total)

print(f'Given a discount rate of .20, the fair value of this loan portfolio is ${round(usd_dcf_total, 2)}.')



#for amt in usd_dcf_total_list:
    #print(amt)
    #total += amt

#print('total', total)


# ## Evaluation
#
# Given the number that resulted from your present value calculation, does the opportunity to invest in this
# microfinance portfolio meet your criteria?
#
# Do you think that any parameters should be changed when doing this analysis? Would that change the outcome of your investment decision?
#
# Please provide your thoughts and analysis in the markdown box provided.

# ### Evaluation Answer
#
# Investment Criteria:
#
#
# Changes in Analysis Parameters:

# In[ ]:


# Testing Cell

period_payment = 15000 * (.2/12) / (1 - (1 + (.2/12))**-9)
print(period_payment)


# In[ ]:
