### 2. Instructor Do: Welcome (5 mins)

Welcome the students to the first day of APIs. This lesson will require students to leverage various FinTech APIs (i.e. Quandl) to accelerate their financial analytic pipelines, as well as get access to data they otherwise would not have access to. Students will continue employing skills learned from weeks two and three, such as data cleaning, working with DataFrames, and visualizing data.

The focus of this lesson will be to demo to students some of the creative and quirky FinTech APIs that are currently available to the public. Students will learn and use these APIs to take their FinTech careers to the next level.

Be sure to have the following websites loaded prior to class so that the demo can move along. Multiple APIs will need to be demoed within the 5 minute time period.

* [Quandl API Features](https://www.quandl.com/tools/api)

* [WrapAPI](https://wrapapi.com/)

**Files:**

* [welcome-slides]()

Start the class off with a review of the introductory slide about `APIs`. Highlight the following:

* Application programming interfaces, or `APIs`, are functions and procedures that enable users to gain access to features and data of an underlying system.

* APIs work as endpoints, like old school telephone operators. A request or call is submitted by a user to be connected to another entity. The API interprets the request and transmits the request to the target entity. The user then receives a response.

* APIs are made by individual developers like the students, as well as private companies and corporations. For this reason, some APIs are free and others require payment for services.

* There are a large number of FinTech APIs are available that accelerate day-to-day financial analytics and data acquisition. These include `Quandl` and `Wrap API`, just to name a few.

Introduce `Quandl` and briefly demonstrate to students how to use an internet browser to submit a Quandl API call.

* `Quandl` is a data mart of financial data. Quandl collects data from various sources, consolidates the data,and then makes it available to users. `Quandl` is a great product to use to extract financial data to calculate ROI, risk-to-reward ratio, etc. Quandl's data can be accessed by users via their API. The API supports multiple programming languages, including Python.

  ![quandl_flow.gif](Images/quandl_flow.gif)

Navigate to the [Quandle API Overview](https://www.quandl.com/tools/api) page, and scroll down to the `API Features` section.

* Show students the URL used to submit a Quandl API request. Underscore the fact that API requests work just like regular URLs. Also indicate that the `request URL` can be configured to specify the output format (i.e. CSV, JSON, or XML); state that JSON will be used for this class.

  ![quandl_url.png](Images/quandl_url.png)

* Submit Quandl API to get AAPL's stock prices using an internet browser and the link below. Show students the data, and bring attention to the AAPL stock prices in the output.

  ```
  https://www.quandl.com/api/v3/datasets/OPEC/ORB.json
  ```

  ![quandl_request_output.png](Images/quandl_request_output.png)

Finish the demo of Quandl with the following reflective question:

* We've extracted historical stock data in the past using the NASDAQ website. How does using the `Quandl` API compare? How is it different?

  > "Quandl is easier and quicker to use than Nasdaq. As long as the URL is known, less steps are needed. Limitation is that the request URL has to be known. Less steps are required to get data from Quandl compared to NASDAQ as well."

* If you wanted to automate the extraction of historical stock price, what's the better tool: NASDAQ.com or Quandl?

  > "Quandl would be the best tool to use to automate extraction of historical stock data. It would be easier than automating the NASDAQ.com process."

If time remains, communicate to students that if they wanted to automate the NASDAQ process, they could use the really cool[WrapAPI](https://wrapapi.com/). Open the site and show students the Yelp gifs.

* Explain that the `WrapAPI` provides a functionality that allows users to record a series of actions on a website and automate them. This includes actions like signing into Facebook, as well as extracting data from NASDAQ.com. It can also scrape data from a website!

* Convey what's happening in each gif.

  1. Actions are recorded

  2. Actions/requests are executed

  2. Action/request output is reviewed

* The `WrapAPI` could actually be used to submit Quandl API requests via a web browser as well. `WrapAPI` could automate the process of copying and pasting the request URL into the browser.

Before ending this activity, let students know that this is just the beginning in terms of available APIs for use. Ask if there are any questions prior to moving onto the next activity.
