# PyLending

For this challenge we are going to combine the concepts of bond calculations we have covered in our Python lessons. We will also explore concepts from foreign exchange and the microfinance space.

## Foreign Exchange

From our lesson, _direct_ fx rates_ quote the price of one unit of foreign currency is expressed in terms of the domestic currency. In contrast, _indirect_ fx rates quote the price of one unit of domestic currency in terms of the foreign currency.

For this exercise, we will be using the foreign currencies of Pakistani Rupee (PKR), Kenyan Shilling (KES) and Indian Rupee (INR). All three will be quoted in direct terms.

For instance, the rate of 162.76 PKR means that each $1 is worth 162.76 PKR.

To calculate the value of a $1,000 USD loan in PKR terms is:  $1,000 x 162.76 = 162,760 PKR.

The same calculations apply to the currencies KES and INR.



## Microfinance

The emerging microfinance field differs from the traditional lending market in several ways.

 - The typical international microfinance loan averages about $525 dollars.

Contrast this amount to a typical microfinance loan in the US which avarages about $10,000. For additional context, the average small business loan in the US is 20,000. The average school loan is $37,000. the average autoloan is approximately $30,000. And the average mortgage loan approximately is $300,000.

 - Interest rates are much higher than typically encountered. Microfinance interest rates average 37% worldwide.

Rates in the US average 20%, and they can reach upwards of 70% in some developing countries. A portion of these larger rates is due to a higher risk of default in the lending pool, but, on average, 12% of the additional interest is the result of the increased transaction costs incurred by the lender. Despite scale efficiencies, it is very expensive to manage the operations for a large number of very small loans.

- Lending periods are typically very short in the microfinance market. Lending periods average out to 4 months across the globe. It is unusual to find loans that stretch out past a single year.

- Mobile technology has made microfinancing and financial inclusion possible in regions that are removed from a typical banking infrastructure.


## Instructions


This activity will be conducted from the view of the originator of a portfolio of international microfinance loans. You can assume that all of the loans in this portfolio were issued on the same date.

You will be evaluating issues such as cash flow, the effect of foreign exchange, and the net present value of the portfolios. For a challenge activity, you have the option to work with Twilio to build a simple front end application that begins to mimic a lending platform.

### Warmup - Initial Portfolio Review - Iterate Lists

Lesson 1 - Jupyter Notebook; Lesson 2 - Variables &  Loops, Lesson 3 - Iterating Lists

Given the loan portfolio provided in PYLending.ipynb:

  * Iterate and print the total amount of the loans issued in USD.
  * Determine what % the PKR, KES and INR loans make up of the total portfolio.



### Part 1 - Foreign Exchange - Manipulate Dictionaries

Lesson 2 - Variables, Loops &  Conditionals; Lesson 3 - Manipulating Dictionaries

In this part of the homework, we are going to evaluate the value of the USD loans in terms of the foreign currency.

 * Calculate the foreign currency amount that was distributed on issue date. Add that _key:value_ pair to each object. The key for portfolio_pkr should read **loan_value_local**.

 * Calculate the total amount of loans in the local currency that was distributed on the issue date.


### Part 2 - De-anualizing Interest Rates

Lesson 2 - VLC; Lesson 3 - LD; Lesson 4 - Functions; Lesson 5 - NPV

In this activity, you will be asked to look at the loans in terms of the cash-flow from the perspective of a single month rather than over the life of the loan. The activity will require you to pay careful attention to the interest rate (annual_interest_rate), timing of the payments (repayment_interval),  and the duration (term_in_months) when deciding how to structure your calculations.

 * Determine the _foreign_ NET cash flow will be for **ONLY month 6** of the portfolio.
 * When determining the net flow, assume that the cost of operation for the portfolio will be 12%.
 * FYI - the repayment_interval called **bullet** assumes that both the principle and interest will be paid in full at the _end_ of the loan.


### Part 3 - Portfolio Valuation

Lesson 2 - VLC; Lesson 3 - LD; Lesson 4 - Functions; Lesson 5 - NPV

You have recently been introduced to a Silicon Valley investor that is interested in finding a social impact opportunity with which to be involved. The investor is requiring a 20% return on her investment.

* Calculate the total value of the loan portfolio first in local currency and then convert it to USD at the current market foreign exchange rate.

Given the initial USD of the investment and the current NPV, does this portfolio meet her investing criteria?

How would fluctuating foreign exchange rates change the rate of that return?



### Bonus - Twilio

As mentioned, mobile interaction is extremely important to the microfinance industry.

For this part of the assignment, utilize the Twilio Programmable SMS API to crate an interaction between your PYLending notebook and your potential Silicon Valley Investor.

* Create the integration necessary to send her an SMS message advising her on the status of her investment opportunity with your portfolio.

* Note - Utilize your own phone number as the message recipient.
