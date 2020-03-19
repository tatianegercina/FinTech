# Unit 2 Challenge Assignment: PyLending

--------->
Insert image here
--------->

## Background

The micro-finance lending space is exploding across the globe. The idea of using small, short-term loans to effect social change in some of the poorest regions of the world is very appealing.

Your job as a newly-minted Python developer has provided you with funds that are available for an investment opportunity. A close friend heard about your interest in micro-finance lending and approached you with the idea of co-investing in a portfolio of micro-finance loans with them.

You have just gotten your first look at the loan portfolio and realize you have to make some calculations before you can determine if this is an investment you are willing to undertake. You understand how to value bonds and loans, but micro-finance specifics and foreign exchange fluctuations make the portfolio evaluation more challenging.

With a little bit of research, you came up with the following information on some important topics to help in the portfolio evaluation process.


### Topic 1 - Micro-finance vs Traditional Lending

The emerging micro-finance field differs from the traditional lending market in several ways.

 - The typical international micro-finance loan only averages about $525 dollars.

Contrast this amount to a typical micro-finance loan in the US which averages about $10,000. For additional context, the average small business loan in the US is 20,000. The average school loan is $37,000. The average auto loan is approximately $30,000. And the average mortgage loan approximately is $300,000.

In the world of international micro-finance, a small amount of money can potentially help a lot of individuals.

 - Micro-finance interest rates are much higher than typically encountered averaging approximately 37% worldwide.

Rates of micro-finance loans in the US average 20%, but can reach upwards of 70% in some developing countries.

A portion of this difference is the higher risk of default in developing countries, but operational costs are a more influential factor: as a proportion of the loan amount, it can be very expensive to evaluate borrowers and collect money on every single loan amount. This is especially true in locations where there is no access to a traditional banking infrastructure.


- Lending periods are typically very short in the micro-finance market averaging out to 4 months across the globe.

Given the nature of the loan and its borrower's rapidly changing circumstances, it is unusual to find loans that stretches past a single year.

- Mobile technology has made microfinancing and financial inclusion possible in regions that are removed from a typical banking infrastructure.

Where almost no one in the 2nd, and certainly the 3rd world, has access to what we think of as traditionally banking, almost all of them have access to a cell phone. This has enabled the proliferation of mobile credit for those that are most in need.

### Topic 2 - Foreign Exchange

Foreign exchange is essentially the conversion of one currency for another. The foreign exchange rate is the amount of one currency per a unit of another currency.

From our lesson, direct fx rates quote the price of one unit of foreign currency in terms of the domestic currency. In contrast, indirect fx rates quote the price of one unit of domestic currency in terms of the foreign currency. Basically, it refers to which exchange rate is the numerator and which is the denominator.

For this exercise, the domestic currency will be the US dollar (USD) we will be using the foreign currencies of Pakistani Rupee (PKR), Kenyan Shilling (KES) and Indian Rupee (INR). All three will be quoted in indirect terms.

For instance, the rate of 162.76 PKR means that each $1 is worth 162.76 PKR.

To calculate the value of a $1,000 USD loan in PKR terms is:  $1,000 x 162.76 = 162,760 PKR.

The same calculations apply to the currencies KES and INR.


Armed with this new information, the challenge of evaluating our investment opportunity will take place in 3 phases:

1. PyPortfolio - Phase 1 will begin with basic calculations to evaluate the portfolio.
2. PyPresentValue - Phase 2 involves a present value analysis to figure out a "fair price" to pay if investing in this micro-finance loan portfolio.
3. PyCashFlows - In Phase 3 we will apply some financial calculations to determine whether the interest generated from an expanded loan portfolio can finance the issuance of some additional loans.

---

### Files

---


## Instructions

You have just received the micro-finance loan portfolio for your review.  You have been advised that all of the loans in this portfolio were issued on the same date.

After a quick scan, you have determined that there are several calculations need to be done to properly evaluate the overall portfolio.

NOTE - Activities designated as 'Core' are required. The 'Extension' activities are designed to stretch your knowledge and abilities. Your grade will not decrease if they are not completed successfull, but it is recommended you attempt them.

### Phase 1 - PyPortfolio

In this phase you just want to get an overall feel for the investment portfolio as presented.

The goals of the Phase 1 activities are:

 * Core - Iterate through the portfolio's data structure to determine basic portfolio characteristics such as size and composition.
 * Core - Utilize variables, loops, conditional statements and foreign exchange to calculate the local currency value of each loan issued.



### Phase 2 - PyPresentValue


As your Python knowledge allows for you to work with external files, you will proceed with your analysis for the current portfolio.

Overall, based on the information you gathered researching international micro-finance, you would like to see a minimum return on your investment of 15%.

The goals of the Phase 2 activity are:

 * Core - Use each loan's repayment interval determine the amounts paid.
 * Core - Use Discount Cash Flow (DCF) calculations to determine the fair value of a single loan in the portfolio.
 * Extension - Use DCF calculations to determine the fair value, or present value, of the entire portfolio.
 * Extension - Evaluate the investment potential of the portfolio given the numbers calculated in the Extension activity above.


### Phase 3 - PyCashFlows

The micro-finance portfolio you are a co-investor in has just grown. The fundamental structure of the loans and the currencies involved ar the same, but the portfolio information now resides in a CSV file.  The will require you to import the CSV file before proceeding with your analysis.

In this last phase of the portfolio analysis,  you are interested in analyzing the monthly cash flows

Your goal is to determine the amount of monthly cash flows generated from loan repayments that will be available to purchase additional loans for the portfolio.

The goals of this Phase 3 activity are:

* Core - Import and examine the CSV file provided. Compare and contrast the imported portfolio and the one you have been previously working with.
* Core - De-annualize the loan interest rates an convert the proceeds to dollars to determine how much dollar income is generated on a monthly basis.
* Extension - Write a short evaluation of the portfolio's ability to use it monthly income to generate new loans. Additionally, analyze how you might use the code to automate the process of determining these monthly flows, reinvestment amounts and loan portfolio value.

---

## Hints and Considerations

* [f-string Formatting](https://realpython.com/python-f-strings/)

* [Rounding numbers in Python](https://realpython.com/python-rounding/)

* [FX information](https://admiralmarkets.com/education/articles/forex-basics/forex-direct-quote-vs-forex-indirect-quote)

For the 3 phases, domestic currency is the US dollar. The Local currency will be either Pakistani Rupee (pkr), the Kenyan Schilling (), or the Indian Rupee (inr).

> domestic currency  / quote in local currency  = foreign exchange rate


> domestic currency * foreign exchange rate rates = local currency value

> local currency value / foreign exchange rate rates = us dollar value

* Present Value Calculation for a loan - Determining the fair value of a loan involves evaluating each of the period cash flows in relation to the discount rate and the period of the payment.

> FV = period_payment/(1 + discount_rate)^1st_period + period_payment/(1 + discount_rate)^2st_period +...+ period_payment/(1 + discount_rate)^last_period

---

## Submission

1. Create a Github repository for this assignment called **Unit2_Python**, and clone it down to your machine.

2. Utilize the Python scripts located in the Instructions/Starter_Code to complete each of the Phases detailed in the README.md.

3. Copy the completed Python scripts into the Github repository and submit the link to the repository as instructed.
