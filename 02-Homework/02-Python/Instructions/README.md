# Unit 2 Challenge Assignment: Py Lending

## Background

The microfinance space is exploding across the globe. The idea of using small, short-term loans to effect social change in some of the poorest regions of the world is very appealing.

Your job as a newly-minted Python developer has provided you will some additional funds that are in need of an investment opportunity. A close friend heard about your interest in micro-finance and approached you with growing loan portofolio in which you could possibly become a lender.

You have just gotten your first look at the loan portfolio and realize you have to make some calculations before you can determine if this is an investment you are willing to undertake. You understand how bonds work, but throwing micro-finance specifics and foreign exchange into the mix makes the portfolio evaluation more challenging.

With a little bit of research, you came up with the following information on some important topics to help you in the evaluation process.


### Topic 1 - Microfinance vs Traditional Lending

The emerging microfinance field differs from the traditional lending market in several ways.

 - The typical international microfinance loan only averages about $525 dollars.

Contrast this amount to a typical microfinance loan in the US which avarages about $10,000. For additional context, the average small business loan in the US is 20,000. The average school loan is $37,000. the average autoloan is approximately $30,000. And the average mortgage loan approximately is $300,000.

In the world of international microfinance, a small amount of money can potentially help a lot of individuals.

 - Microfinance interest rates are much higher than typically encountered averaging approximately 37% worldwide.

Rates of microfinance loans in the US average 20%, and can reach upwards of 70% in some developing countries.

A portion of these larger rates is due to a higher risk of default in the lending pool, but operational costs are a more influential factor. Almost 12% of the microfinance interest rates can be attributed to the increased transaction costs incurred by the lender. Despite scale efficiencies, it is very expensive to manage the operations for such a large number of very small loans.

- Lending periods are typically very short in the microfinance market averaging out to 4 months across the globe.

Given the nature of the loan and its borrower's rapidly changing circumstances, it is unusual to find loans that stretches past a single year.

- Mobile technology has made microfinancing and financial inclusion possible in regions that are removed from a typical banking infrastructure.

Where almost no one in the 2nd, and certainly the 3rd world, has access to what we think of as traditionally banking, almost all of them have access to a cell phone. This has enabled the proliferation of mobile credit for those that are most in need.

### Topic 2 - The 411 on Foreign Exchange

Foreign exchange is essentially the conversion of one currency for another. The foreign exchange rate is the amount of one currency per a unit of another currency.

From our lesson, _direct_ fx rates_ quote the price of one unit of foreign currency is expressed in terms of the domestic currency. In contrast, _indirect_ fx rates quote the price of one unit of domestic currency in terms of the foreign currency.

For this exercise, the domestic currency will be the US dollar (USD) we will be using the foreign currencies of Pakistani Rupee (PKR), Kenyan Shilling (KES) and Indian Rupee (INR). All three will be quoted in direct terms.

For instance, the rate of 162.76 PKR means that each $1 is worth 162.76 PKR.

To calculate the value of a $1,000 USD loan in PKR terms is:  $1,000 x 162.76 = 162,760 PKR.

The same calculations apply to the currencies KES and INR.


Armed with this new information, the challenge of evaluating our investment opportunity will take place in 4 phases:

1. PyPortfolio - basic portofolio calculations
2. PyNPV - evaluating the overall NPV of the portfolio
3. PyFlows - looking at specifc period cash flows
4. PyMobile - this bonus activity involves the Twilio SMS protocol


## Instructions

You have just been received this micro-finance loan portfolio for your review.  You can assume that all of the loans in this portfolio were issued on the same date. You have determined that there are several steps that you need to undertake to appropriately evaluate this investing opportunity.

### Phase 1 - PyPortfolio

In this phase you just want to get an overall feel for the investmet portfolio as presented. The goals of you analysis are to:

 * Iterate through a List to determine the value of the portfolio in US dollars.
 * Utilize variables, loops and conditional statements to determine the percentage that each of the foreign currency investments make up of the total portfolio.
 * Combine the building blocks of Python with basic financial calculations to determine the amount of the loans in each foreign currency that was issued.


### Phase 2 - PyNPV

You have just been informed that size of the portfolio has grown since you analysis started. There are enough loans in the portfolio to require an external file.

As your Python knowledge allows for you to work with external files, you will proceed with your analysis for the current portfolio.

Overall, based on the information you gathered researching international microfinance, you would like to see a minimum return on your investment of 15%.

The goal of phase 2 is to:

 * Determine the net present value (NPV) of the portfolio.
 * Determine the value of the portfolio taking into account the 12% cost of operational maintenance.


### Phase 3 - PyFlows

You have just been informed that size of the portfolio has grown since Your analysis started. The fundamental structure of the loans and the same currencies are involved, but there are enough loans in the portfolio to require a CSV file.

As your Python knowledge allows for you import and analyze external files, you will proceed with your analysis for the portfolio in its new form.

After Phase 2's analysis, you are reasonably certain that this is a solid investment opportunity. On last aspect of the portfolio that you are interested in analyzing are the monthly cash flows. You are trying to determine if the amount of monthly income is enough help you to fund additional loans.

The goal of this Phase 3 is to:

* Import and examine the CSV file provided.
* Determine how much USD income is generated on a monthly basis based on current interest rates.
* Code the program so that these cash flow values are calculated automatically once new CSV files are imported.


### Bonus - PyNotification

In this bonus challenge, you will look into what it would take to set up mobile notifications for your loan recipients using the Twilio SMS functionality.



## Resources

CSV file when created.

## Hints

* f-string Formatting:

* Rounding Values:

* NPV Calculation Formula:



## Submission
