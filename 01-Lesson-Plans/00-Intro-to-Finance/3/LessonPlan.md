## Prework Module 3: Investing

---

### Overview

In this module we will we will begin introducing some of the core concepts related to investing, why we want to invest, and some of the ways we can compare potential investments.

### Module Objectives

By the end of this module, you should be able to:

* Identify reasons for making investments and how risk influences profits

* Understand the importance of the time value of money, and how to discount a future value to a present One

* Understand the key concepts of Modern Portfolio Theory and how the efficient frontier allows us to optimize a portfolio's risk/return profile


### Reading: Inflation and Investing

For a [variety of reasons](https://en.wikipedia.org/wiki/Inflation#Causes) the cost of goods and services in an market will increase over time, which subsequently decreases the purchasing power of a money. We refer to this process of the devaluing of a money over time as **inflation**. We often measure inflation using the [consumer price index](https://www.bls.gov/cpi/), which the government also utilizes to control inflation through manipulation of the money supply.

Due to a combination of inflation and a desire to generate profits, individuals and companies  seek to make **investments** - a purchase of an asset that will be worth a higher value at a later date or produce continual profits. All investments involve some amount of risk, and thus are expected to make comensurate returns that are higher than the rate of inflation. In some investments, like loans, the interest rate is directly related to the amount of risk associated with the investment. In that vein, many investments in the equity of a company are considered highly risky - and thus are tend to have higher returns compared to loans. Generally speaking, investmensts in equity (ownership of an asset) outperforms investment in debt (giving out loans) in long term scenarios.

### Student Activity: Inflation Reflection

See instructions in [activity file](Activities/01-Stu_Inflation_Reflection/README.md)


### Reading: Time Value of Money

Is it better to have $10,000 today or $10,500 tomorrow? In general, it is better to have money today in order to be prepared for possible opporunities that may arise.


```
FV = PV * [1+(i/n)]^(n*t)
```

Where FV is the future value, PV is the past value, i is the interest rate, n is the number of compounding periods within a year, and t is the number of years. We will often rearrange this formula to solve for the past value, which we refer to the as the discounted value.

For example, you have an investment opportunity that will be worth $12,000 next year, compounding once at 5%, and another that is also worth the same future value, but compounds twice at 4%. Which would you want to invest in, provided that they offer similar levels of risk?

```
PV = $12,000 / [1 + (0.05/1)] ^ (1 * 1) = $11,428

PV = $12,000 / [1+ (0.04/2)] ^ (1*2) = $11,534
```

From solving the TVM equation, we can see that the first investment *discounts* our present cash more, that is, the second investment assigns a higher value to our current cash. Thus, in this scenario we would take the second investment.

### Student Activity: Calculate TVM

See instructions in [activity file](Activities/02-Stu_Calculating_TVM/README.md)

### Modern Portfolio Theory

Now that we’ve talked about both risk and investments, we should discuss how to manage them together as part of a larger portfolio.

Imagine a portfolio containing three stocks that each have a return of five percent. However, all three of those stocks have a tendency to trend together - meaning that if one increases in value, they all do; but the reverse is also true. What kind of risk does this pose for your portfolio?

A portfolio is not only evaluated on the basis of the returns that it makes, but also on how the different investments within it move together. Modern portfolio theory (MPT) helps us to optimize our return for a given risk tolerance. The combination of different investments allows us to mitigate risks of any single given investment to allow us to create a lower-risk portfolio.

Within MPT we often analyze the variance of individual stocks in order to understand their risk. This gives us a good idea of the volatility associated with the stock and how it may fit into a larger portfolio. In MPT we also evaluate the the correlation between each pair of assets in the portfolio in order to assess how risk between each individual asset behaves. By balancing the assets in a portfolio, the risk associated with any given asset is partially mitigated by other assets. An ideal portfolio should attempt to not only stay ahead of inflation, but also minimize risk both as a whole (low variance) as well as between assets that comprise the portfolio (low correlation).

One of the most central ideas of MPT is the concept of an Efficient Frontier. When plotting the projected returns for an amount of risk for a portfolio, we can derive a curve that gives us an idea of the portfolio weightings that optimize the return for a given level of risk. We call the very edge of this curve the **efficient frontier** and in general when we are constructing a portfolio we will avoid making investments that are not along this curve.

### Student Activity:

See instructions in [activity file](Activities/03-Stu_Portfolio_Comparisons/README.md)
