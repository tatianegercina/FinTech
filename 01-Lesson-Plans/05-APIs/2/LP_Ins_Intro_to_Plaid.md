### 11. Instructor Do: Intro to Plaid (5 mins)

**Files:**

* [Slides]()

Navigate to the 5.2 slides, and introduce the **Plaid** API by providing a brief overview:

* **Plaid** is an API that brokers connections to users' bank accounts to create a one-stop shop experience for financial management. Typically when analyzing data cross multiple accounts, one would have to visit each financial institution and extract the desired data. **Plaid**  streamlines this process by offering a platform that will broker the request for data extraction so users do not have to manually do it.

* **Plaid** offers the following services:

  * Help users monitor, budget, and gain insights from their personal finances

  * Help users manage data from multiple accounts (i.e. savings, equity, investments, retirement) in one platform

  * Up until now, students have been solely conducting quantitative analysis on investments.

    ![plaid_services.png](Images/plaid_services.png)

Facilitate discussion with the following talking points and guided questions:

* **Plaid** can be used to analyze financial data in a more comprehensive and holistic view. **Plaid** takes the data from each financial account and consolidates it to create an overarching portfolio that encompasses savings, investments, retirement funds, loans, etc. What types of financial analysis would require data to be extracted from more than one type of financial account?

  **Answer** Net worth analysis would require data to be extracted from all financial accounts.

* **Plaid** was created as a tool to assist developers in designing FinTech applications. By brokering connections to financial institutions, **Plaid** allows developers to focus on designing analytic pipelines for consumers that provide insight and drive financial budgeting decisions. If you had access to your savings, investment, and retirement account data, what would you do with it?

  **Answer** Calculate rate of cumulative returns daily, quarterly, and yearly to identify a baseline of cumulative returns over time. This insight could be used to change the types of funds, bonds, and individualized stocks used in each account.

  **Answer** Calculate **beta** to compare individualized stock and retirement portfolio volatility.

* By leveraging the data provided by **Plaid**, developers no longer have to concern themselves with data acquisition/brokering communication with financial institutions. Instead, developers can use the functions provided by the **Plaid** **SDK** to broker these connections. This means that developers are fully empowered to focus on designing innovative and valuable processes for consumers.
