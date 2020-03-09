# Loan Portfolio
# Assume that all of the loans in this list were issued on the same date.



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

#-----------------------------------------------------

#Warm-up

#Print the USD total amount of the loans issued.
#Determine what percentage the pkr, kes and inr loans are of the overall portfolio.

total_usd = 0
loans_pkr = 0
loans_kes = 0
loans_inr = 0

for loan in portfolio_mf:

    total_usd += loan['loan_value_usd']

    if loan['local_currency'] == 'pkr':
        loans_pkr +=  loan['loan_value_usd']

    elif loan['local_currency'] == 'kes':
        loans_kes += loan['loan_value_usd']

    else:
        loans_inr += loan['loan_value_usd']



print('The size fo the portfolio in USD is $%.2f.'% total_usd)
print('The percent of PRK loans in the portfolio is %.2f%%.' % ((loans_pkr/total_usd)*100))
print('The percent of KES loans in the portfolio is %.2f%%.' % ((loans_kes/total_usd)*100))
print('The percent of INR loans in the portfolio is %.2f%%.' % ((loans_inr/total_usd)*100))

#-----------------------------------------------------

#Part 1 - Lesson - Jupyter Notebook; Lesson 2-variables, loops; Lesson 3-lists & dictionaries

#Calculate the foreign currency amount that was distributed on issue date. Add that key:value pair to each object.
#For example, the key for portfolio_pkr should read 'loan_value_local'.
#Calculate the total amount of loans in the local currency that was distributed on the issue date.


total_loans_pkr = 0
total_loans_kes = 0
total_loans_inr = 0



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




print(portfolio_mf[1])
print('The total amount of PKR loans issued was %.0f.'% total_loans_pkr)
print('The total amount of KES loans issued was %.0f.'% total_loans_kes)
print('The total amount of INR loans issued was %.0f.'% total_loans_inr)

#-----------------------------------------------------

# Part 2 - De-anualizing interest rates

# Determine what the foreign NET cash flow will be in the the portfolio for only month 6 of the issuance.
# From the introduction assume that the operational costs for the month will be 12%.
# FYI - the repayment-interval "bullet" assumes that principle and interest will be paid on the due date.

cashflow_month6 = []

def flow_calcs_6(loan, cashflow_month6):
    dm = loan['term_in_months']
    rm = loan['annual_interest_rate']/12
    dq = loan['term_in_months']/4
    rq = loan['annual_interest_rate']/4
    db = loan['term_in_months']
    rb = (loan['annual_interest_rate']/12)*db

    if loan['repayment_interval'] == 'monthly':
        #print('monthly')
        monthly_payment = int(loan['loan_value_local'])*((rm*((rm+1)**dm))/(((rm+1)**dm)-1))
        #print('Monthly Payment: %.0f'%monthly_payment)
        cashflow_month6.append(round(monthly_payment))
        #print('Cashflow month in 6:', cashflow_month6)

    elif loan['repayment_interval'] == 'quarterly':
        if loan["term_in_months"] == 6:
            #print('quarterly')
            quarterly_payment = int(loan['loan_value_local'])*((rq*((rq+1)**dq))/(((rq+1)**dq)-1))
            #print('Quarterly Payment: %.0f'%quarterly_payment)
            cashflow_month6.append(round(quarterly_payment))
            #print('Cashflow month in 6:', cashflow_month6)
    else:
        if loan['term_in_months'] == 6:
            #print('bullet')
            bullet_payment =int(loan['loan_value_local'])*(1 + rb)
            #print('Bullet Payment: %.0f with a local loan of %.0f and an interest rate of %.4f' % (bullet_payment, int(loan['loan_value_local']), rb))
            cashflow_month6.append(round(bullet_payment))
            #print('Cashflow month in 6:', cashflow_month6)

    return cashflow_month6

#-------
cashflow_month6_pkr = []

def calcs_pkr():
    cashflow_month6 = []

    for loan in portfolio_mf:
        if loan['local_currency']=='pkr'and loan['term_in_months'] > 5:

            flow_calcs_6(loan, cashflow_month6)

    cashflow_month6_pkr.extend(cashflow_month6)

calcs_pkr()
print('PKR6', cashflow_month6_pkr)

#-------

cashflow_month6_kes = []

def calcs_kes():
    cashflow_month6 = []

    for loan in portfolio_mf:
        if loan['local_currency']=='kes'and loan['term_in_months'] > 5:
            flow_calcs_6(loan, cashflow_month6)

    cashflow_month6_kes.extend(cashflow_month6)

calcs_kes()
print('KES6', cashflow_month6_kes)

#-------
cashflow_month6_inr = []

def calcs_inr():
    cashflow_month6 = []

    for loan in portfolio_mf:
        if loan['local_currency']=='inr' and loan['term_in_months'] > 5:
            flow_calcs_6(loan, cashflow_month6)

    cashflow_month6_inr.extend(cashflow_month6)

calcs_inr()
print('INR6', cashflow_month6_inr)

#-------

cash_flow_usd_p = 0
cash_flow_usd_k = 0
cash_flow_usd_i = 0
cash_flow_usd = 0

#print('PKR6', cashflow_month6_pkr)
current_fx_pkr = 154.30

for flow in cashflow_month6_pkr:
    usd_flow = flow/current_fx_pkr
    #print(flow, usd_flow)
    cash_flow_usd_p += usd_flow
    #print(round(cash_flow_usd_p))

#print('----------')

#print('KES6', cashflow_month6_kes)
current_fx_kes = 102.70

for flow in cashflow_month6_kes:
    usd_flow = flow/current_fx_kes
    #print(flow, usd_flow)
    cash_flow_usd_k += usd_flow
    #print(round(cash_flow_usd_k))

#print('----------')

#print('INR6', cashflow_month6_inr)
current_fx_inr = 74.14

for flow in cashflow_month6_inr:
    usd_flow = flow/current_fx_inr
    #print(flow, usd_flow)
    cash_flow_usd_i += usd_flow
    #print(round(cash_flow_usd_i))

#print('----------')

cash_flow_usd = cash_flow_usd_p + cash_flow_usd_k + cash_flow_usd_i

print('The cash flow in USD for month 6 less operating costs is $%.2f.' % (round(cash_flow_usd) * (1-(.12/12))))


#-----------------------------------------------------


# Loop through the portfolio_mf array and generate the NPV for the portfolio.

discount_rate = .20
npv_total = 0

def npv_month_usd(loan, monthly_payment):
    npv_full = (loan['term_in_months']*(monthly_payment/((1+(discount_rate/12))**loan['term_in_months'])))
    npv_usd = round(npv_full, 2)
    print('npv us', npv_usd)
    return npv_usd

def npv_quarter_usd(loan, quarterly_payment):
    npv_full = (loan['term_in_months']*(quarterly_payment/((1+(discount_rate/4))**(loan['term_in_months']/3))))
    npv_usd = round(npv_full, 2)
    print('npv us', npv_usd)
    return npv_usd

def npv_bullet_usd(loan, bullet_payment):
    npv_full = bullet_payment / ((1+(discount_rate/12))**loan['term_in_months'])
    npv_usd = round(npv_full, 2)
    print('npv us', npv_usd)
    return npv_usd




def period_payment_usd(loan):
    dm = loan['term_in_months']
    rm = loan['annual_interest_rate']/12
    dq = loan['term_in_months']/4
    rq = loan['annual_interest_rate']/4
    db = loan['term_in_months']
    rb = (loan['annual_interest_rate']/12)*db

    if loan['repayment_interval'] == 'monthly':
        #print('monthly')
        monthly_payment_full = int(loan['loan_value_usd'])*((rm *((rm+1)**dm))/(((rm+1)**dm)-1))
        monthly_payment = round(monthly_payment_full, 2)
        print('Monthly Payment: %.2f'% monthly_payment)
        npv = npv_month_usd(loan, monthly_payment)
        return npv

    elif loan['repayment_interval'] == 'quarterly':
        #print('quarterly')
        quarterly_payment_full = int(loan['loan_value_usd'])*((rq*((rq+1)**dq))/(((rq+1)**dq)-1))
        quarterly_payment = round(quarterly_payment_full, 2)
        print('Quarterly Payment: %.2f'%quarterly_payment)
        npv = npv_quarter_usd(loan, quarterly_payment)
        return npv


    else:
        #print('bullet')
        bullet_payment_full = int(loan['loan_value_usd'])*(1 + rb)
        bullet_payment = round(bullet_payment_full, 2)
        #print('Bullet Payment: %.0f with a local loan of %.0f and an interest rate of %.4f' % (bullet_payment, int(loan['loan_value_local']), rb))
        npv = npv_bullet_usd(loan, bullet_payment)
        return npv



for loan in portfolio_mf:

    npv_total += period_payment_usd(loan)
    print(npv_total)

print('The NPV of the total USD loan portfolio less expected transactional costs is $%.0f.' % npv_total)

#-----------------------------------------------------

#Twilio - Utilize Twilio to advise your investor if the portfolio meets their investment criteria
