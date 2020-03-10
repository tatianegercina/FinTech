# Case Study Proposal: Equifax NeuroDecision Technology

## What Is It

Equifax NeuroDecision Technology is a neural network that computes credit scores (a.k.a. credit ratings) for individuals, those all-important numbers that determine your fate when you apply for a loan. In the past, neural network models have been used for credit scoring much less than might be expected, given their ability to identify the non-linear relationships in typical inputs to scoring models. This is because the basis on which traditional neural networks generate their results is not readily explainable, a situation that regulators, such as the U.S. Consumer Financial Protection Bureau and the European General Data Protection Regulation, find unacceptable. Equifax’s technology offers the power of a well trained neural net, but one with the ability to explain its decision making.

## Why This Matters

Equifax is one of the “big three” credit rating agencies, each of which provide prospective lenders with a numerical score that indicates the credit worthiness of just about any prospective U.S. borrower. These numbers play an important role in deciding the rate at which the loan would be extended and even whether credit would be extended at all. Thus, the calculation of these scores affects many millions of people.

Accurate calculation of such scores is therefore of primary importance. Yet, in the past, such scores were computed via logistic regression, a technique that attempts to partition the data using linear functions. However, nonlinear relationships are embedded in the data that might predict the likelihood of defaulting on, say, credit card debt (Such an example might be the relationship between income and default probability: once income gets above a certain level, people are less likely to have to choose between credit card payments and feeding their children.). Neural nets certainly solve this problem, but they do so by “learning” an obscure and nonlinear weighting scheme. NeuroDecision technology attempts to identify the reasons why its neural net’s calculations turn out the way they do.

Also, machine learning cannot now be used in many other applications that seem to be begging for it. For example, IBM’s Watson failed miserably when it was marketed to the oncology departments of hospitals, as doctors and patients lost faith in it, partly because of Watson’s inability to explain its recommendations. “Explainable AI” may well provide at least a partial answer, so it is currently very hot.

## Why This May Be Interesting

* Many people have some kind of debt and many more will likely take on debt in the near future (cars, houses, etc.). One can most likely relate to credit rating technology, and especially to rating technology that isn’t opaque.

* Machine learning using neural networks is undoubtedly of interest, regardless of application.

* Credit related applications, in particular, are of great interest to the financial community, so students who can make themselves useful to such projects should be able to find highly paid employment. In addition to credit bureaus and lenders (including many FinTech start-ups), large consultancies, such as the Boston Consulting Group, and accounting firms, such as KPMG, actively recruit machine learning specialists.

## Things to Keep in Mind for a Case Study

* An explanation of the problem domain, i.e. inputs, such as payment history, estimated income, estimated assets, etc., and outputs, including the difference between the Equifax credit score and the (in)famous FICO score.

* A brief discussion of the limitations of logistic regression, which was the way that Equifax did credit scoring prior to NeuroDecision.

* A brief discussion of neural networks, why they might work better than logistic regression, and how a neural network might be implemented to do credit scoring.

* A brief discussion about the opacity of neural net decision making and why that’s a problem, including the failure of IBM Watson on cancer wards. Include also that neural net decision making is sometimes “brittle”, in that it chooses the wrong variables on which to base its decision. A classic example is the neural net that distinguished between pictures of babies and pictures of adults using the size of the head in the frame. It turns out that people like to take close-ups of babies.

* A brief discussion of regulatory constraints in deploying neural networks for credit scoring.

* How NeuroDecision actually worked in the field.

## Resources

* [Equifax’s explanation of their technology, including a useful video](https://www.equifax.com/videos/introduction-neurodecision/ )

* [The bad news about IBM Watson and cancer](https://www.statnews.com/2017/09/05/watson-ibm-cancer/)

* [Example of regulatory guidance surrounding scoring models. This document states the requirement that “Once designed and prior to implementation, the model is evaluated for integrity, reliability, and accuracy by a party independent of its design.” This is difficult, if not impossible to do with a traditional neural net](https://www.fdic.gov/regulations/examinations/credit_card/pdf_version/ch8.pdf)

* [Article about how the European General Data Protection Regulation bans most “black boxes”](https://www.computerweekly.com/news/252452183/GDPR-a-challenge-to-AI-black-boxes)

* [A good start in understanding “explainable AI”](https://www.kdnuggets.com/2019/01/explainable-ai.html)

* [Successful innovation in AI drives customer success for Equifax](https://www.prnewswire.com/news-releases/successful-innovation-in-ai-drives-customer-success-for-equifax-300816043.html)

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
