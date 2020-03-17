# Unit 2 Challenge Assignment: Py Lending

--------->
Insert image here
--------->

## Background

The microfinance lending space is exploding across the globe. The idea of using small, short-term loans to effect social change in some of the poorest regions of the world is very appealing.

Your job as a newly-minted Python developer has provided you with funds that are available for an investment opportunity. A close friend heard about your interest in microfinance lending and approached you with an expanding loan portofolio in which you could possibly become a participant.

You have just gotten your first look at the loan portfolio and realize you have to make some calculations before you can determine if this is an investment you are willing to undertake. You understand how bond evaluation works, but microfinance loan specifics and foreign exchange fluctuations make the portfolio evaluation more challenging.

With a little bit of research, you came up with the following information on some important topics to help in the portfolio evaluation process.


### Topic 1 - Microfinance vs Traditional Lending

The emerging microfinance field differs from the traditional lending market in several ways.

 - The typical international microfinance loan only averages about $525 dollars.

Contrast this amount to a typical microfinance loan in the US which averages about $10,000. For additional context, the average small business loan in the US is 20,000. The average school loan is $37,000. The average auto loan is approximately $30,000. And the average mortgage loan approximately is $300,000.

In the world of international microfinance, a small amount of money can potentially help a lot of individuals.

 - Microfinance interest rates are much higher than typically encountered averaging approximately 37% worldwide.

Rates of microfinance loans in the US average 20%, and can reach upwards of 70% in some developing countries.

A portion of these larger rates is due to a higher risk of default in the lending pool, but operational costs are a more influential factor. Almost 12% of the microfinance interest rates can be attributed to the increased transaction costs incurred by the lender. Despite scale efficiencies, it is very expensive to manage the operations for such a large number of very small loans.

- Lending periods are typically very short in the microfinance market averaging out to 4 months across the globe.

Given the nature of the loan and its borrower's rapidly changing circumstances, it is unusual to find loans that stretches past a single year.

- Mobile technology has made microfinancing and financial inclusion possible in regions that are removed from a typical banking infrastructure.

Where almost no one in the 2nd, and certainly the 3rd world, has access to what we think of as traditionally banking, almost all of them have access to a cell phone. This has enabled the proliferation of mobile credit for those that are most in need.

### Topic 2 - Foreign Exchange

Foreign exchange is essentially the conversion of one currency for another. The foreign exchange rate is the amount of one currency per a unit of another currency.

From our lesson, _direct_ fx rates quote the price of one unit of foreign currency in terms of the domestic currency. In contrast, _indirect_ fx rates quote the price of one unit of domestic currency in terms of the foreign currency.

For this exercise, the domestic currency will be the US dollar (USD) we will be using the foreign currencies of Pakistani Rupee (PKR), Kenyan Shilling (KES) and Indian Rupee (INR). All three will be quoted in indirect terms.

For instance, the rate of 162.76 PKR means that each $1 is worth 162.76 PKR.

To calculate the value of a $1,000 USD loan in PKR terms is:  $1,000 x 162.76 = 162,760 PKR.

The same calculations apply to the currencies KES and INR.


Armed with this new information, the challenge of evaluating our investment opportunity will take place in 3 phases:

1. PyPortfolio - This phase will focus on basic portfolio evaluation calculations.
2. PyPresentValue - Phase 2 will involve an analysis, in stages, of the overall present value of the microfinance loan portfolio.
3. PyCashFlows - The final phase will de-annualize the portfolio in an attempt to determine the cash flow generated from loan repayments for specified months.

---

### Files

---


## Instructions

You have just received the microfinance loan portfolio for your review.  You have been advised that all of the loans in this portfolio were issued on the same date.

After a quick scan, you have determined that there are several calculations need to be done to properly evaluate the overall portfolio.

### Phase 1 - PyPortfolio

In this phase you just want to get an overall feel for the investment portfolio as presented. The goals of you analysis are to:

 * Iterate through the portfolio's data structure to determine basic portfolio characteristics such as size and composition.
 * Utilize variables, loops, conditional statements and foreign exchange to calculate the local currency value of each loan issued.



### Phase 2 - PyPresentValue


As your Python knowledge allows for you to work with external files, you will proceed with your analysis for the current portfolio.

Overall, based on the information you gathered researching international microfinance, you would like to see a minimum return on your investment of 15%.

The goal of the Phase 2 activity is to:

 * Determine the loan repayment amounts to be made based on each loan's specified repayment interval.
 * Determine the present value, also known as the fair value, of a single loan in the portfolio using a discounted cash flow (DCF) model.
 * Challenge - Determine the present value of the entire portfolio using the DCF model and functions.
 * Challenge - Evaluate the investment potential of the portfolio given the numbers calculated in part 3 of the activity.


### Phase 3 - PyCashFlows

You have just been informed that the size of the portfolio has grown since your analysis started. The fundamental structure of the loans and the same currencies are involved, but there are enough loans in the portfolio to require a CSV file.

As your Python knowledge allows for you to import and analyze external files, you will proceed with your analysis for the portfolio in its new form.

After Phase 2's analysis, you are reasonably certain that this investment opportunity is of interest to you. One last aspect of the portfolio that you are interested in analyzing are the monthly cash flows.

Your goal is to determine the amount of monthly cash flows generated from loan repayments that will be available to help fund additional microfinance lending.

The goals of this Phase 3 activity are to:

* Import and examine the CSV file provided. Compare and contrast the data structures between the imported file and the one you have been working with in the prior phases.
* De-annualize the loans to determine how much USD income is generated on a monthly basis based on the current foreign exchange provided.
* Write a short evaluation of the portfolio's ability to generate new loans. Also, analyze how the code to process the calculations helps to automate the process of determining monthly flows in the current scenario and going forward.

---

## Hints and Considerations
git
* [f-string Formatting](https://realpython.com/python-f-strings/)

* [Rounding numbers in Python](https://realpython.com/python-rounding/)

* [FX information](https://admiralmarkets.com/education/articles/forex-basics/forex-direct-quote-vs-forex-indirect-quote)

> domestic or base currency / quote currency = fx rate

> us dollar value * direct fx rates = local currency value

> local currency value / direct fx rates = us dollar value

* Present Value Calculation for a loan - Determining the fair value of a loan involves evaluating each of the period cash flows in relation to the discount rate and the period of the payment.

> FV = period_payment/(1 + discount_rate)^1st_period + period_payment/(1 + discount_rate)^2st_period +...+ period_payment/(1 + discount_rate)^last_period

---

## Submission

1. Create a Github repository for this assignment called **Unit2_Python**, and clone it down to your machine.

2. Utilize the Python scripts located in the Instructions/Starter_Code to complete each of the Phases detailed in the README.md.


3. Copy the completed Python scripts into the Github repository and submit the link to the repository as instructed.
