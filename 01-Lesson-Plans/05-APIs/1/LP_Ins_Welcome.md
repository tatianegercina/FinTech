### 2. Instructor Do: Welcome (5 mins)

Welcome the students to the first day of APIs. This lesson will require students to leverage various FinTech APIs (i.e. Quandl) to accelerate their financial analytic pipelines, as well as get access to data they otherwise would not have access to. Students will continue employing skills learned from weeks two and three, such as data cleaning, working with DataFrames, and visualizing data.

The focus of this lesson will be to demo to students some of the creative and quirky FinTech APIs that are currently available to the public. Students will learn and use these APIs to take their FinTech careers to the next level.

**Files:**

* [welcome-slides]()

Start the class off with a review of the introductory slide about APIs. Highlight the following:

* Application programming interfaces, or APIs, are functions and procedures that enable users to gain access to features and data of an underlying system.

* APIs work as endpoints, like old school telephone operators. A request or call is submitted by a user to be connected to another entity. The API interprets the request and transmits the request to the target entity. The user then receives a response.

* APIs are made by individual developers like the students, as well as private companies and corporations. For this reason, some APIs are free and others require payment for services.

* There are a large number of FinTech APIs are available that accelerate day-to-day financial analytics and data acquisition. these include Quandl, World of Bank API, and Wrap API, just to name a few.

Transition into the demonstration portion of the welcome activity by showing students how to submit API requests.

* Postman is a development environment dedicated to submitting API requests.

* All that is needed to submit an API request using Postman is an API URL.

Introduce Quandl and briefly demonstrate to students how to use Postman to submit Quandl API calls.

* Quandl is a data mart of financial data. Quandl stores various types and formats of financial data for analysis. Data can be extracted from Quandl in order to calculate ROI, risk-to-reward ratio, etc.

* Submit the following request via API

> "https://www.quandl.com/api/v3/datasets/OPEC/ORB.json"

* Display to students the output of the API.
