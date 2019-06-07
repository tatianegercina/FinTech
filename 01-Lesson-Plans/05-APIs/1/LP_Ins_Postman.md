### 2. Instructor Do: The Postman Cometh (5 mins)

In this activity, students will learn how to use Postman. The instructor will demo making `Quandl` API calls with Postman rather than through a browser. This will highlight the advantages of using Postman, such access to a UI, request logs, and tools that format API output for ease of use.

Be sure to have the `Postman` client installed prior to beginning this activity. Consult the Postman install guide for instructions on how to install (link is listed below).

**Files:**

* [Postman Install Guide](../../Supplementary/PostmanInstallGuide.md)

* [postman.md](Activities/06-Ins_Postman/Solved/postman.md)

Briefly recap on how APIs have been submitted so far. Ask the students:

* We submitted Quandl API requests earlier in the class. What tool did we use to submit the API call?

> "An internet browser."

Explain to students that internet browsers a sufficient tool to submit adhoc API requests. While browsers are an easy way to submit API calls, using a service like `Postman` is much more efficient and effective.

* Define `Postman` as a service that provides users with a UI to submit and store API calls and requests.

* Communicate that `Postman` is a development environment for APIs. APIs requests can be submitted and tested within `Postman`. Servers can also be spun up in `Postman` in order to develop and/or host APIs.

Open `Postman` and perform a live demonstration of submitting an API request to `Quandl` for `AAPL` stock data. Use this as an opportunity to bridge back to the previous assignments where requests were submitted via a browser rather than a tool like `Postman`. Highlight the following:

* Creating a request in `Postman` is easy; it's just the click of a button. Selecting `Request` in the `Create New` window will open a screen where information can be put in for the request and the request saved.

  ![create_request.png](Images/create_request.png)

* `Postman` allows users to save API requests to what they call `collections`. This allows requests to be created once but ran many times. It also allows requests to be scheduled. In order to save a request, a request must be saved with a `name`, `description`, and `collection`.

  ![save_request.png](Images/save_request.png)

* Another way to create a request is to create a new `tab`. Once the tab is created, the request URL can be input.

  ![new_request.png](Images/new_request.png)

* Submit an API call to `Quandl` using the `Postman` submit button. Use the below request URL.

  * https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json

  ![postman_get.png](Images/postman_get.png)

* The output from an API call is returned in the `Postman` client. `Postman` presents users with the ability to choose the format of the output (i.e. JSON vs. XML). Indicate that the format of the output on the screen is called `JSON` (Javascript Object Notation).

  ![postman_submit.png](Images/postman_submit.png)

* Postman allows users to save or download the results of an API call. This is one of the advantages of using Postman to work with APIs. The Postman environment supports creating, storing, and retrieving API requests, as well as API results.

  ![save_output.png](Images/save_output.png)

Ask if there are any questions before moving onto the next module.

In the next activity, students will leverage the steps from this demonstration in order to make their first API call using `Postman`. Students will make a `GET` request to `Quandl` for `AAPL` historical stock data.
