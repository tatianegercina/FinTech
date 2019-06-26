## 5.2 Lesson Plan - API Mania!

---

### Overview

Today's class will focus on exposing students to the exciting and innovative **FinTech APIs** that have been disrupting the industry. Students will get hands on experience using **APIs** in a Python environment, requesting and leveraging **API keys**, and correctly storing **API keys and credentials** as **environment variables** (variables that exist at the operating system level). Students will programmatically submit API requests using the Python `requests` library and API **Software Development Kits** (SDKs).

**APIs** used in this lesson include **Quandl**, an API that provides programmatic access to historical stock data, and **Plaid**, an API that brokers connections multiple financial institutions in order to create a unified view of personal, financial information and accelerate the extraction of data from multiple financial accounts.

### Class Objectives

By the end of class, students will be able to:

* Register for an API key and use the key to fetch authenticated requests using the Requests Library

* Set/Export environment variables in Windows and Mac and retrieve them in Python

* Explain the difference between an API and SDK

* Set authentication for the Plaid SDK

* Use a Python SDK to fetch data from Plaid

* Use SDK's to analyze personal financial data

### Instructor Notes

* This lesson includes the demonstration and use of two APIs that require users to have accounts and API keys. You, students, and TAs will all need to have created and accounts and received **API keys** prior to this lesson. The following links can be used to sign up for accounts and get keys. Slack these links out to TAs and students before the beginning of the lesson so they have ample time to sign up. Students were instructed to sign up at the end of 5.1. There will be an activity dedicated to confirming that each student has signed up.

  * [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

  * [Plaid](https://dashboard.plaid.com/signup)

* Since this lesson will work with **API keys**, it is important that you and students do not **hardcode** or **print** any **API keys** or request URLs with keys. All keys must be stored in **environment variables** and then referenced with an `os.getenv` function call in Python.

* This lesson has a dependency on the **Quandl** and **Plaid** APIs being up and running. Visit each site and execute pre-emptive API calls to ensure connectivity. It is imperative to confirm that the APIs used in this lesson are executing as expected.

* Some students may have previous experience working with making API calls. Keep an eye out for any students who might be advanced with APIs and could help assist with review activities. Allowing advanced students to conduct reviews and help their peers is a great way to keep them engaged and interested in the material.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

Day 2 takes students to the next step in using APIs. Students will transition from using the Python `requests` library to using **SDKs** that provide practical use cases for FinTech analysis.

**Files:**

* [welcome-slides]()

Welcome students to the second day of APIs by highlighting the following talking points:

* Communicate that today's lesson will be a continuation of the last session; however, there will be more emphasis and focus on using FinTech APIs in a practical manner.

* Underscore that practical APIs work just like the fun APIs (i.e. Python BlackJack). A client submits a request, and a server responds. Ask the students a quick refresher question:

    **Question** What is the name or conceptual phrase for this interaction/relationship between a client and an API.

    **Answer** Client-server model.

* There are a number of FinTech APIs available that grant users the ability to create and execute analytic pipelines on various forms of financial data.

* Because APIs often offer practical services, they may require subscriptions or payment. Companies use **API keys** and **user accounts** to ensure billing and secure transmission of financial/confidential information.

Transition into a dry demonstration (just visit the site) of a practical FinTech API that will be used later in the lesson: **Plaid**.

* Navigate to the [Plaid](https://plaid.com/) website.

* Explain that **Plaid** is an API that allows users to connect multiple bank accounts to one platform, and provides a unified view of a person's financial ecosystem. This allows users to manage and analyze their accounts and financial information from one spot.

* Communicate that **Plaid** was designed as a tool for developers to accelerate their FinTech development. Developers can use **Plaid** to provide services to their users and consumers without having to worry about making API calls to each individual bank or financial entity.

* Because **Plaid** handles the behind-the-scenes handshakes with each financial institution, developers are able to focus on designing and developing a program that will:

  1. Make calls to **Plaid**

  2. Analyze data by either extracting financial information from Plaid or by using **Plaid's** out of the box capabilities.

  ![plaid_services.PNG](Images/plaid_services.PNG)
