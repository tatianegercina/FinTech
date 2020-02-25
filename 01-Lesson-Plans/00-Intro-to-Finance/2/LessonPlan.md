## Prework Module 2: What is Risk?

---

### Overview
In this module we will explore the concepts of risk and its relationship with returns for investments.

### Module Objectives

By the end of this module, you should be able to:

* Describe several different kinds of risk, and how they are calculated

* Be able to articulate the differences between systematic and non-systematic risk, and know which can be mitigated most easily

* Describe Sharpe, Sortino, and Information Ratios

### Reading: Defining Financial Risk

In investing, there is always some unpredictability in the outcome which we refer to as **uncertainty**. Several different types of financial instruments, we will calculate the **volatility** of the instrument over a period of time as the measure of unpredictability. Volatility can be calculated by finding the standard deviation of all of the [returns](https://www.investopedia.com/terms/r/return.asp) over the period.

This uncertainty can lead to large gains or losses in capital, which we refer to as **risk**. In many cases, we will use the calculated volatility as a stand-in for risk. However, depending on the specific type of risk we would like to model, we may approximate it in different ways. This module will cover several of the most commonly discussed types of risk.

### Student Activity: Self-Research

See instructions in [activity file](Activities/01-Stu_Self_Research/README.md)

### Reading: Types of Risk

In securities trading (the stock market) there are two principal types of risk we are concerned with: **systematic** and **non-systematic risk**. Systematic risk (not "systemic") is the risk associated with the market as a whole, and cannot be diversified away in any particular market. Consider an index such as the S&P500 which tracks the top 500 companies by market cap. If the index plummets, it suggests that the *overall* market is losing value simultaneously. Non-systematic risk, sometimes referred to as idiosyncratic risk, is associated with an individual instrument. For example, if you own shares of Tesla and the value fluctuates wildly relative to the CEO publishing tweets. This risk can be diversified away (mitigated) by including the instrument in a portfolio with other investments.

One of the ways banks make profit is by making loans to individuals or families. However, how can they know that they will be paid back? Any company that makes loans is likely to assess the credit risk of those they make loans to. In the U.S. we often utilize a calculation created by the Fair Isaac Company (FICO Score) to assess "creditworthiness". Any method of assessing a person's likelihood of paying back a loan is fair, as long as the features used in the assessment do not violate legal statutes for specific types of discriminatory practices.

Imagine you own a real-estate company. After you have received your seed capital, you rush out and buy up as many properties as possible in order to establish yourself in a region, and in the process, you completely exhaust your cash on hand. Later, a large bill comes in the mail, which you are incapable of paying because you have no cash on hand. You now have to sell one or more of your properties to raise enough cash to pay for this bull, however, it will take some time to be able to receive the cash from the sale due to how slow real estate transactions operate - which refer to as the “illiquidity” of the market. In order to accelerate finding a buyer, you may need to sell one of your properties at a loss. The risk of finding yourself in the situation without enough cash on hand to cover debts is referred to as the liquidity risk. Liquidity risk is important for all companies to assess (especially banks) as they may need to take out high-interest short-term loans in order to cover debts in the near term, which can affect profits.

### Student Activity: Risk Reflection

See instructions in [activity file](Activities/02-Stu_Risk_Reflection/README.md)

### Risk vs Return

If were given a choice of three different portfolios that all had the same estimated return, how would you decide which was best to invest in? Generally the investment that gives the most return *per its amount of risk* is considered the smart choice. To make this assessment we will often calculate the Sharpe ratio of the investment, which is simply dividing the total return by the volatililty of the investment. We can also calculate a similar metric known as the Sortino ratio, which only incorporates the downside risk. A third ratio we may utilize is the Information ratio (IR), which will compare performance relative to some benchmark like the S&P 500.

In addition to these ratios, we can also utilize the Capital Asset Pricing Model (CAPM) to model the expected return of an investment relative to its risk. The model can be expressed at a high-level as:

```
Expected Return = (Risk-Free Rate) + (Beta * Market Risk Premium)

```

Where the risk-free rate is often the long-term yield of a government bond, Beta is equity beta (relative volatility of a single asset to the market's volatililty), and the market risk premium is the difference between the risk free rate and the expected return of the market. The market risk premium can be considered to be a descriptor of the amount of return expected for the risk of investment.

### Student Activity: Ratio Deep Dive

See instructions in [activity file](Activities/03-Stu_Ratio_Deep_Dive/README.md)
