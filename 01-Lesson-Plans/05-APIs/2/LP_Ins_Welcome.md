### 1. Instructor Do: Welcome Class (5 mins)

Day 2 takes students to the next step in using APIs. Students will transition from using the Python HTTP library to using SDKs. The instructor will briefly introduce students to SDKs, using Paywall and PLAID as examples. Students need to understand the basics of API authentication, practices to keep financial data and user credentials secure, and the process of acquiring and using API keys. By the end of the day, students will have skillfully and securely leveraged the PLAID API for financial analysis. This will prepare them for using APIs to securely perform real-world portfolio return analysis and portfolio simulation with market and personal financial data during Day 3.

* **Files:**

  * [welcome-slides]()

Welcome students to the second day of APIs by highlighting the following talking points:

* Communicate that today's lesson will be a continuation of the last session; however, there will be more emphasis and focus on using FinTech APIs in a practical manner.

* There are a number of FinTech APIs available that grant users the ability to create and execute analytic pipelines on various forms of financial data.

* Because APIs often offer practical services, they may require subscriptions or payment. Companies use **API keys** and **user accounts** to ensure billing and secure transmission of financial/confidential information.

Transition into a dry demonstration (just visit the site) of a practical FinTech API that will be used later in the lesson: **PLAID**.

* Navigate to the [PLAID](https://plaid.com/) website.

* Explain that **PLAID** is an API that allows users to connect multiple bank accounts to one platform, and provides a unified view of a person's financial ecosystem. This allows users to manage and analyze their accounts and financial information from one spot.

* Communicate that **PLAID** was designed as a tool for developers to accelerate their FinTech development. Developers can use **PLAID** to provide services to their users and consumers without having to worry about making API calls to each individual bank or financial entity.

* Because **PLAID** handles the behind-the-scenes handshakes with each financial institution, developers are able to focus on designing and developing a program that will:

  1. Make calls to **PLAID**

  2. Analyze data by either extracting financial information from PLAID or by using **PLAID's** out of the box capabilities.

  ![plaid_services.PNG](Images/plaid_services.PNG)
