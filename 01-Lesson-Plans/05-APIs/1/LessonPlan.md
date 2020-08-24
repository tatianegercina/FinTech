## 5.1 Lesson Plan: APIs

### Overview

For the past three weeks, students have been immersed in the world of Python and common Python libraries that are included in the Anaconda environment (i.e., Pandas and Matplotlib). They've also learned some key techniques for analyzing financial data, such as calculating daily returns and risk-reward ratios. It's now time for students to take it to the next level and enter into the world of application programming interfaces (APIs). There are a number of FinTech APIs available that will allow students to perform more powerful analytics. They will also expose students to datasets they would not typically be able to easily access or consolidate. Now, students will learn the basics of APIs and API requests so that they can begin incorporating APIs into their work.

Today's class will teach students what APIs are, what they're used for, and why they are valuable. Students will also learn, from a high level, what the client-server model is and how it works. Students will submit API calls with Postman (a development environment for APIs) and Python, and they'll learn how to decipher and parse API JSON output. Lastly, students will submit API calls with parameters in order to improve response time and filter and narrow down API output. Learning how to make API calls and parse API output using Postman and Python will prepare students for getting their hands dirty with APIs in the professional world.

Before students leave at the end of the class, instruct them to sign up for the APIs that are going to be used in the next class. These APIs will require that students have API keys. Links are provided below. Remember to slack the links to the students, so they have a resource to sign up with.

* [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

* [Alpaca Markets](https://app.alpaca.markets)

### Class Objectives

By the end of class, students will be able to:

* Describe the client-server model.

* Read the documentation and identify endpoints from a given API.

* Perform a GET request and view the JSON response using the Postman client.

* Interpret the JSON structure from a GET request response.

* Use the requests library to request JSON data from an API within Python.

* Parse a JSON response and print a selected field using Python.

* Query an API using URL Parameters with the requests library.

### Instructor Notes

* Slack out the [Alpaca and Quandl Installation Guide](../Supplemental/AlpacaMarkets_Installation-Guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. This should help catch installation issues with Alpaca outside of class time.

* This class will focus on the fundamentals of APIs and the process of submitting APIs. This class is a great opportunity for students to be impressed and inspired by FinTech. There are a number of fun and creative FinTech APIs, such as Quandl and World of Bank, will be used to drive student engagement. This lesson is the perfect opportunity to get students excited about FinTech again!

* The first half of the lesson will include instructor demonstrations of submitting requests to different FinTech APIs using Postman. Each demo should be focused on showcasing FinTech APIs and getting students excited about contributing to the wealth of APIs that are already out there. Make sure to create accounts for these APIs:

  * [Postman](https://www.postman.com/)

  * [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/889386-developer-information-overview)

  * [Quandl](https://www.quandl.com/)

  * [Alpaca](https://alpaca.markets/)

* Students should have already downloaded Postman prior to class. Use the welcome activity to identify any students who may not have already downloaded Postman, and have the TAs help them get it installed.

* The welcome class module will be dedicated to demoing some of the previously mentioned FinTech APIs.

* Working with APIs can be challenging for anyone using them, especially when documentation is limited. Whenever introducing students to a new API, slack out the link to the documentation so that students have access to it for reference.

Be sure to set the pace for the class. Encourage students to attend office hours if they feel lost or stuck. Also, encourage students to work with partners.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

---

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [5.1 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=01b5d2b5-75ae-4414-a9ec-aaaf00fb4e47) Note that this video may not reflect the most recent lesson plan.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [5.1 Slides](https://docs.google.com/presentation/d/1o2QoZbtZ2GZ3xU3Gn-e6A45Seh51q_3hrS4rIvVU4gE/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 mins)

Welcome the students to the first day of APIs. This lesson will require students to leverage various FinTech APIs (e.g., Quandl) to accelerate their financial analytic pipelines, as well as get access to data they otherwise would not have access to. Students will continue employing skills learned from weeks two and three, such as data cleaning, working with DataFrames, and visualizing data.

The focus of this lesson will be to demo to students some of the creative and quirky FinTech APIs that are currently available to the public. Students will learn and use these APIs to take their FinTech careers to the next level.

Before initiating the demo, ask if there are any students who do not have Postman installed. Instruct TAs to help these students install Postman. Postman will be needed for the first few modules of the lesson.

Be sure to have the following websites loaded prior to class so that the demo can move along. Multiple APIs will need to be demoed within the 5 minute time period.

* [Quandl API Features](https://www.quandl.com/tools/api)

* [WrapAPI](https://wrapapi.com/)

Open the lesson slides, move to the "Introduction to APIs section", and highlight the following:

* Application programming interfaces, or APIs, are functions and procedures that enable users to gain access to features and data of an underlying system.

* APIs work as endpoints, like old-time telephone operators. A request or call is submitted by a user to be connected to another entity. The API interprets the request and transmits the request to the target entity. The user then receives a response.

* APIs are made by individual developers like the students, as well as private companies and corporations. Some APIs are free, and others require payment for services.

* There are a large number of FinTech APIs available that accelerate day-to-day financial analytics and data acquisition. These include Quandl and Wrap API, just to name two.

Introduce Quandl and briefly demonstrate to students how to use an internet browser to submit a Quandl API call.

* Quandl is a data mart of financial data. Quandl collects data from various sources, consolidates the data, and then makes it available to users. Quandl is a great product to use to extract financial data to calculate ROI, risk-to-reward ratio, etc. Users can access Quandl's data via their API. The API supports multiple programming languages, including Python.

  ![quandl_flow.gif](Images/quandl_flow.gif)

Navigate to the [Quandl API Overview](https://www.quandl.com/tools/api) page, and scroll down to the **API Features** section.

Show students the URL used to submit a Quandl API request. Underscore the fact that API requests work just like regular URLs. Also indicate that the **request URL** can be configured to specify the output format (e.g., CSV, JSON, or XML); highlight that JSON will be used for this class.

![quandl_url.png](Images/quandl_url.png)

Submit a request to the Quandl API to get OPEC oil prices using an internet browser and the link below. Show students the data, and bring attention to the OPEC oil prices in the output. Note that you need to include your Quandl API key as a parameter in the URL to make the API call work.

```text
https://www.quandl.com/api/v3/datasets/OPEC/ORB.json?api_key=[YOUR-KEY-HERE]
```

  ![quandl_request_output.png](Images/quandl_request_output.png)

Finish the demo of Quandl with the following reflective questions:

* We've extracted historical stock data in the past using the Nasdaq website. How does using the `Quandl` API compare? How is it different?

  **Answer:** Quandl is easier and quicker to use than Nasdaq. As long as the URL is known, fewer steps are needed. A limitation is that the request URL has to be known.

* If you wanted to automate the extraction of historical stock prices, what's the better tool: nasdaq.com or Quandl?

  **Answer:** Quandl would be the best tool to use to automate the extraction of historical stock data. It would be easier than automating the nasdaq.com process.

If time remains, communicate to students that if they wanted to automate the Nasdaq process, they could use the cool [WrapAPI](https://wrapapi.com/). Open the site and show students the Yelp GIFs.

* Explain that WrapAPI provides functionality that allows users to record a series of actions on a website and automate them. This includes actions like signing into Facebook and extracting data from nasdaq.com. It can also scrape data from a website!

* Convey what's happening in each GIF.

  1. Actions are recorded

  2. Actions and requests are executed

  3. Action and request output is reviewed

* WrapAPI could be used to submit Quandl API requests via a web browser as well. WrapAPI could automate the process of copying and pasting the request URL into the browser.

Before ending this activity, let students know that this is just the beginning in terms of available APIs for use. Ask if there are any questions before moving on to the next activity.

---

### 2. Instructor Do: Review Homework (10 min)

Students will receive a demo of the homework from the instructor.

**Files:**

* [README.md](../../../02-Homework/05-APIs/Instructions/README.md)

Explain to students that this unit's homework focuses on exposing them to some of the most valuable and cutting edge APIs in FinTech. The homework tasks students with creating Python applications that integrate multiple APIs to create innovative and powerful FinTech solutions.

Walkthrough the homework instructions and highlight the following:

* In this unit's homework, you will create two financial analysis tools using the Alpaca API and the Free Crypto API, a personal financial planner, and a retirement planning tool.

* The personal financial planner will allow you to visualize personal expenses from the last 90 days to assess the current financial health by comparing the monthly household income versus the monthly expenses.

* Using the financial planner, you also will be able to analyze savings composed by investments in shares and cryptocurrencies.

* After creating the personal financial planner, you will transition to forecast financial goals. This section uses a Monte Carlo simulation to predict retirement portfolio performance to determine if a customer's initial retirement contribution will cover their future income.

* Lastly, you will analyze the retirement planner activity output and summarize assumptions and findings in a financial analysis report created using markdown that you will upload to your GitHub repository.

Ask the students if there are any questions related to the homework before continuing with the next activity.

---

### 3. Instructor Do: Client-Server Model (5 min)

Now that students know what APIs are and how to execute them, it's time they learn what goes on in the back end when an API request is sent. Students will learn the various components of the client-server model through instructor demonstration.

Part of the demonstration will include showing students the client-server model by pinging Yahoo Finance. Make sure to have a terminal open and ready for the demo.

Navigate to the 5.1 slides for the client-server model, and highlight the following:

* Explain the client-server model architecture. Indicate that the model encompasses the relationship between clients and servers.

  ![client_server_model.jpg](Images/client_server_model.png)

* Define the client-server model as a structure that outlines the relationship and flow of communication between two components: a client and a server.

  * A **client** is any tool or application that is used to connect to or communicate with a server. This includes internet browsers, mobile devices, and command-line terminals, just to name a few. Clients submit requests to servers, and clients receive responses from servers.

  * A **server** is a computer program, device, or hardware. Servers run some form of application and are tasked with interacting and providing functionality to clients. Servers receive requests from clients, and servers send responses back to clients.

* Inform students that client-server requests are commonly `GET` and `POST` requests. `GET` requests fetch data from servers. `POST` requests transmit data (like user credentials for authorization) to servers.

* Communicate that the client-server model is what handles all traffic and requests sent to a server. This includes websites, APIs, and databases. The client-server model architecture ensures that request calls and tasks made to servers are handled appropriately and effectively. When students check Yahoo Finance or log in to Facebook.com, they're enacting the client-server model.

If time remains, demonstrate the client-server model by using the terminal to ping Yahoo Finance.

* Open a terminal.

* Use the ping command to send a request to Yahoo Finance. Explain to students that the ping is a utility used to test connectivity to a server.

  ```shell
  ping finance.yahoo.com
  ```

* Explain the output from the `ping` command. Underscore that with every execution of the client-server model, data is transmitted over a network. This data is inside **packets**. An example of data contained inside packets is user credentials for a website. When the transmission is successful, the number of packets sent will match the number of packets received.

  ![client_server_ping.png](Images/client_server_ping.png)

Ask students the following questions. (If time did not permit for the ping demo, skip the Yahoo Finance question.)

* In this scenario, what is the client and what is the server?

  **Answer**: The terminal is the client, and Yahoo Finance provides the server.

* Was the request sent to Yahoo Finance via the terminal a successful execution of the client-server model based on packets sent and received?

  **Answer**: Yes, all packets that were sent to the server were received.

Ask students if there are any questions before moving on.

---

### 4. Students Do: Eavesdropping on the Server (10 min)

**Corresponding Activity:** [01-Stu_Eavesdropping_On_Server](Activities/01-Stu_Eavesdropping_On_Server)

This activity drives home the discussion on the client-server model by having students surf the web with the browser's developer console open. Students will visit websites like Facebook and Yahoo, as well as complete a Google search. They will read the standard output from the console to get a better idea of what data is sent between the client and server as students navigate sites. This will communicate to students that every click and API request brokers a connection between client and server, allowing data to be exchanged between the two.

**Instructions:**

* [README.md](Activities/01-Stu_Eavesdropping_On_Server/README.md)

---

### 5. Instructor Do: Eavesdropping on the Server Activity Review (5 min)

**Files:**

* [eavesdropping.md](Activities/01-Stu_Eavesdropping_On_Server/Solved/client_server_model.md)

Open the solution and walk through the following:

* Firefox, Chrome, and Safari all offer developer consoles that allow users to see requests being exchanged between clients and servers.

* Requests sent from a client to a server are commonly either `GET` or `POST`. `GET` requests retrieve data from a server. `POST` requests submit data to a server.

  ![console_comm.png](Activities/01-Stu_Eavesdropping_On_Server/Images/console_comm.png)

* Both types of requests are submitted using URLs. These URLs can be customized to specify what should be retrieved with the `GET` function and what should be submitted with the `POST` request. For example, searching on Google submits a `GET` request, and the search term or query is transmitted to the Google servers with the `GET` request.

  ![console_search.png](Activities/01-Stu_Eavesdropping_On_Server/Images/console_search.png)

Engage students by asking some of the following review questions:

* Website images are saved on website servers. When an image loads, what type of request is sent from the client to the server?

  **Answer:** `GET` request

* Explain the client-server model from the perspective of emails.

  **Answer:** Servers provided by companies like Google, Yahoo, Microsoft, etc. are used to store and distribute email messages. Email applications and internet browsers are clients that are used to specify who emails are sent to and the body of emails. Clients are used to submit email content to servers, and then servers distribute the message to the corresponding email targets.

* If time remains, round-robin and ask some students to give details about the data they saw transmitted. This will allow students to compare what they saw with what others saw. It will also help students understand some of the common data exchanges, such as user credentials and search queries.

  **Answer:** `GET` requests

  **Answer:** `POST` requests

  **Answer:** Calls to fetch images

Ask for any remaining questions before moving on.

---

### 6. Instructor Do: Postman (5 min)

In this activity, students will learn how to use Postman. The instructor will demo, making Quandl API calls with Postman rather than through a browser. This will highlight the advantages of using Postman, such as access to a UI, request logs, and tools that format API output for ease of use.

Be sure to have the Postman client installed prior to beginning this activity. Consult the Postman Install Guide for instructions on how to install (link is listed below).

**Files:**

* [Postman Install Guide](../Supplemental/PostmanInstallGuide.md)

Briefly recap on how APIs have been submitted so far. Ask the students:

* We submitted Quandl API requests earlier in the class. What tool did we use to submit the API call?

  **Answer**: An internet browser.

Explain to students that an internet browser is a sufficient tool to submit API requests. But a service like Postman is much more efficient and effective.

* Define Postman as a service that provides users with a UI to submit and store API calls and requests.

* Communicate that Postman is a development environment for APIs. API requests can be submitted and tested within Postman. Servers can also be spun up in Postman in order to develop or host APIs.

Open Postman and perform a live demonstration of submitting an API request to Quandl for AAPL stock data. Use this as an opportunity to bridge back to the previous assignments where requests were submitted via a browser rather than a tool like Postman. Highlight the following:

* Creating a request in Postman is easy; it's just the click of a button. Selecting Request in the Create New window will open a screen where information can be put in for the request and the request saved.

  ![create_request.png](Images/create_request.png)

* Postman allows users to save API requests to what they call **collections**. This allows requests to be created once but ran many times. It also allows requests to be scheduled. In order to save a request, a request must be saved with a name, description, and collection.

  ![save_request.png](Images/save_request.png)

* Another way to create a request is to create a new **tab**. Once the tab is created, the request URL can be input.

  ![new_request.png](Images/new_request.png)

* Submit an API call to Quandl using the Postman submit button. Use the below request URL.

  * https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json

  ![postman_get.png](Images/postman_get.png)

* The output from an API call is returned in the Postman client. Postman presents users with the ability to choose the format of the output (e.g., JSON vs. XML). Indicate that the format of the output on the screen is called JSON (JavaScript Object Notation).

  ![postman_submit.png](Images/postman_submit.png)

* Postman allows users to save or download the results of an API call. This is one of the advantages of using Postman to work with APIs. The Postman environment supports creating, storing, and retrieving API requests, as well as API results.

  ![save_output.png](Images/save_output.png)

Ask if there are any questions before moving onto the next module.

In the next activity, students will leverage the steps from this demonstration in order to make their first API call using Postman. Students will make a Get request to **Quandl** for **AAPL** historical stock data.

---

### 7. Students Do: I Spy an API (15 min)

**Corresponding Activity:** [02-Stu_I_Spy_An_Api](Activities/02-Stu_I_Spy_An_Api)

It's time students stopped learning about APIs and started playing with some! In this activity, students will go through a list of FinTech APIs and test out their functionality using Postman. This will give students a better understanding of what Postman is and how it should be used, and it will expose students to one of the most common tools used in the FinTech industry.

Instruct TAs to make rounds to ensure all students have Postman installed. Postman should have been installed prior to the class. Have TAs provide assistance and troubleshooting to any students experiencing issues getting started.

Recommend that students save their API requests in Postman, so they do not have to continually execute the same request.

Slack out the supplemental `Postman Install Guide` to students, so they have a step-by-step process for installing and getting started.

Instruct students to inform the TAs when they are finished. The next activity will require students to work in pairs, so everyone will need to have completed this activity before the next activity can begin.

**Files:**

* [PostmanInstallGuide.md](../Supplemental/PostmanInstallGuide.md)

**Instructions:**

* [README.md](Activities/02-Stu_I_Spy_An_Api/README.md)

---

### 8. Students Do: Parlez-vous le JSON? (5 min)

**Corresponding Activity:** [03-Stu_Parlez_Vous_Le_Json](Activities/03-Stu_Parlez_Vous_Le_Json)

In this activity, students will choose a sub-selection of the JSON output to decipher. They will then explain the sub-selection to a peer. The key to working with APIs is being able to decipher their output. Because API output is commonly in JSON format, students will need practice deciphering JSON structures and syntax.

Walk around and instruct TAs to circulate during this activity so that students can ask questions as they make sense of the JSON data, including its structure and syntax. Some students will have had little to no exposure to JSON data in the past. It can be frustrating trying to interpret JSON data when the structure and syntax is foreign.

**Instructions:**

* [README.md](Activities/03-Stu_Parlez_Vous_Le_Json/README.md)

---

### 9. Instructor Do: Parlez-vous le JSON Activity Review (5 min)

Instructor and students will review the JSON turn and teach activity. The instructor will complete a live demo of submitting an API request and deciphering the JSON output.

Open Postman and submit the below request to Quandl. Then, conduct a live deciphering of the JSON data, emphasizing the following:

* https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json

* Name/value pairs are used to make deciphering JSON data easy because it does a single map between **name** and **value**. Point out an example of a name (e.g., the `description` field). Then, identify the corresponding value.

* Point out **JSON Array** and **JSON Objects** in order to compare them.

  ![decipher_json.png](Images/decipher_json.png)

* JSON Objects are contained within curly braces `{}`. These objects often contain multiple name-value pairs, like a row (e.g., `{"ticker":"GOOG","close_price":192.57}`).

* JSON Arrays are identified by brackets `[]`. An example of a JSON Array is the `column_names` object returned from the Quandl API call.

If time permits, ask the students the following questions. Sample answers have been provided.

* We've seen a number of APIs in action (e.g., WrapAPI, Quandl, World Bank, Coinbase). Which API did everyone find the most interesting?

  **Answer:** WrapAPI. While it is not FinTech related, it's unique and has a number of different use cases. Of all of the APIs, WrapApi seems the most flexible and all-encompassing.

* Ask students to write down two things they like about APIs and the client-server model. Ask for two volunteers to present their answers.

  **Answer:** The client-server model is simple, easy to understand, and used almost everywhere. APIs are cool because they eliminate the need of having to reinvent the wheel.

* Ask students to write down one thing they do not like or find challenging about APIs and the client-server model. Ask one student to volunteer an answer.

  **Answer**: Not all APIs have good documentation. It's difficult to gauge exactly what an API can do or how it should be used.

Before moving forward, ask the students if there are any remaining questions.

---

### 10. Instructor Do: Python Requests (10 min)

**Corresponding Activity:** [04-Ins_Python_Requests](Activities/04-Ins_Python_Requests)

Submitting APIs with Postman is useful, but API requests are better sent with Python code. Instructors will demonstrate to students how to submit an API request with Python instead of Postman. Emphasis will be placed on the similarities between the two processes, as well as the advantages of sending requests through Python.

The World Bank API (GDP extraction) should be used for this instructor demonstration activity.

**Files:**

* [python_requests.ipynb](Activities/04-Ins_Python_Requests/Solved/python_requests.ipynb)

Navigate to the 5.1 slides, and highlight the following:

* Just as API **requests** can be sent through Postman, they can also be sent through Python. Python offers a `requests` package that can be used to submit API requests through a protocol known as `HTTP`. The `requests` library supports `GET`, `POST`, and `PUT` requests, just to name a few. `GET` requests will be the focus for this class.

* Each type of request serves a different purpose.

  * `GET` requests are used to extract and acquire data from a server.

  * `POST` requests are used to push new or updated data to the server.

  * `PUT` requests are used to overwrite content on the server.

* APIs play a key role in analytic data pipelines, often being the source of data or a means to analyze data. By submitting requests in Python, APIs can be used in-line with other processing. For example, data can be pulled from Coinbase to calculate cumulative returns, sharpe ratios, and beta for a set of cryptos. Similarly, data could be extracted from the Quandl API to complete portfolio simulations. Instead of switching back and forth between Postman and Python, everything can just be completed in Python.

Demonstrate with live code how to use the Python `requests` library, and use the following discussion points:

* The `requests` library has to be imported in order to be used.

  ```python
  import requests
  ```

* The first step to using the requests library after importing it is to declare a variable that will hold the URL.

  ```python
  url = "http://api.worldbank.org/v2/country/us/indicator/NY.GDP.MKTP.CD"
  ```

* Because most APIs support multiple output formats, the next step is to specify the desired output format. This can be added to the URL with a format tag, `?format=`. Common formats used are JSON, CSV, and XML. For this lesson, JSON will be the focus. The format tag will need to be appended to the URL string previously created; ask students if anyone remembers how to append to a string. (Answer: concatenation.)

  ```python
  url = url + "?format=json"
  ```

* `GET` requests can be sent using the `requests.get` function. The function accepts the request URL as an argument.

  ```python
  # Execute GET request
  requests.get(url)
  ```

  ![request_response.png](Images/request_response.png)

* Most APIs incorporate programming that will return code with each server response. These are called **response codes**. A list of common response codes and their meanings can be found below.

  ```
  Common Response Codes

  200s: Success
  400s: Error
  500s: Request accepted but error occurred server side
  ```

* Output from a `GET` request is best saved as a variable. This allows for the output to be parsed and manipulated down the road.

  ```python
  # Execute GET request and store response
  response_data = requests.get(url)
  ```

* The actual data returned from the server, called **content**, can be accessed with the `content` attribute.

  ```python
  # Get content
  response_content = response_data.content
  print(response_content)
  ```

  ![submit_python_request.png](Images/submit_python_request.png)

* The `json` function from the `json` library can be used to format API output in true JSON format.

  ```python
  import json

  # Format JSON
  data = response_data.json()
  ```

* To improve visual formatting, even more, the `json.dumps` function can be used to add indentations to the JSON data to make the JSON levels and hierarchies more apparent. The `json.dumps` function accepts an argument `indent`, which can be configured to change the indents. `indent=4` is commonly used. Communicate to students  that the `json.dumps` function only visually formats the JSON output on the screen; it does not alter the underlying JSON structure.

  ```python
  # Add indents to JSON and output to screen
  print(json.dumps(data, indent=4))
  ```

  ![json_with_indent.png](Images/json_with_indent.png)

* JSON data has to be selected based on levels and hierarchies. For example, some JSON objects are organized by JSON object -> JSON array -> attribute. Some have multiple objects, and others have multiple JSON arrays. Either way, accessing JSON data is just like accessing data in a dictionary. Brackets `[]` are used with **keys** to retrieve values.

  ```python
  # Select country and GDP value for second row
  country = data[1][1]['country']['value']
  gdp_value = data[1][1]['value']

  print(country)
  print("GDP Value: " + str(gdp_value))
  ```

  ```
  Country: United States
  GDP Value: 20544343456936.5
  ```

  ![selecting_json.png](Images/selecting_json.png)

Ask if there are any remaining questions before moving forward.

---

### 11. Students Do: Ice Breakers on Request (20 min)

**Corresponding Activity:** [05-Stu_Ice_Breakers_on_Request](Activities/05-Stu_Ice_Breakers_on_Request)

In this activity, students are given a list of **request URLs** to execute using the Python `requests` library. Students will also receive the opportunity to put their JSON knowledge to use by interpreting JSON output. Students will interpret the JSON output to find an interesting fact or joke to tell the class.

Walk around with TAs to provide assistance to students with parsing JSON data. Students may need assistance parsing JSON output. Make sure every student has been able to successfully execute a request and find an interesting fact or joke to share, even if the fact has to relate to their own experiences using Python requests.

**Files:**

* [python_requests.ipynb](Activities/05-Stu_Ice_Breakers_on_Request/Unsolved/python_requests.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Ice_Breakers_on_Request/README.md)

---

### 12. Students Do: Engagement Activity (15 min)

In this activity, have each student reveal an interesting fact or joke they discovered while working with APIs. Round robin and have each student volunteer a fact or joke.

If a student doesn't find a fact or joke they feel like sharing, ask them to do one of the following:

* Discuss their opinions regarding using the Python `requests` library to make API calls instead of Postman.

* Identify one advantage of using the Python `requests` library over using Postman.

**Answer** The `requests` library allows API calls to be made in-line with the rest of the code and processing. Postman requires users to transition from one development environment to another.

Transition into a reflective Q&A session. Ask the students the following questions:

* Having seen a range of FinTech and quirky APIs, what API can you see yourself implementing on your own accord?

* Are there specific types or categories of APIs you'd be interested in working with?

* What type of APIs are you interested in creating?

* Deciphering and parsing JSON can be frustrating and challenging, especially when the data isn't formatted in the best way. Did the `json.dumps` improve your ability to decipher the JSON data?

If time remains, tell students about some of the APIs you've worked with and how they've added to your professional success. Encourage students to take advantage of as many open source APIs as possible. Take this time to recommend any APIs that you feel students might be interested in.

Ask students if there are any comments or questions they'd like to make regarding their experiences working with APIs so far. Then transition into a formal review of the Python Requests activity.

---

### 13. Instructor Do: Ice Breakers on Request Activity Review (10 min)

**Files:**

* [python_requests.ipynb](Activities/05-Stu_Ice_Breakers_on_Request/Solved/python_requests.ipynb)

Open the solution and conduct a dry walk-through review, highlighting the following discussion points:

* The Python `requests` library can be used to submit API requests. Just like Postman, the `requests` library will submit the request to the server, and then wait for the response. In order to use the library, it has to be imported.

  ```python
  import requests
  ```

* The `requests` library comes with a `GET` function that can be used to execute a request URL.

  ```python
  request_data = requests.get(prog_joke_url)
  ```

* Each Python request generates a response code. The response code indicates whether or not the response was successful and details whether there were any errors.

  ```python
  print(request_data)
  ```

  ```
  <Response [200]>
  ```

* The content from a request can be accessed using the `content` attribute.

  ```python
  # Store response using `content` attribute
  response_content = response_data.content
  ```

* The `JSON` function is used to format the API response into JSON format.

  ```python
  # Get content as JSON
  data = response_data.json()
  ```

* `json.dumps` can be used to format the JSON output in a way that is easy to decipher and interpret visually. The indent argument is used to specify how many indentations should be used when formatting. Indents help delineate JSON levels and hierarchies.

  ```python
  import json

  # Use json.dumps with argument indent=4 to format data
  print(json.dumps(data, indent=4))
  ```

  ![json_dumps.png](Images/json_dumps.png)

* Data from the API can be extracted from its JSON format by using brackets `[]` to specify the desired element in fully qualified format (i.e., [parent][index][child]). Depending on the JSON format, the parent and index levels may not be applicable.

  ```python
  # Select a programming joke
  selected_value = data[0]['setup']
  selected_value_2 = data[0]['punchline']
  ```

  ![access_json_data.png](Images/access_json_data.png)

---

### 14. BREAK (15 min)

---

### 15. Instructor Do: URL Parameters (5 min)

**Corresponding Activity:** [06-Ins_URL_Parameters](Activities/06-Ins_URL_Parameters)

In this activity, students learn how to customize API requests with parameters through instructor demonstration. The [Numbers API](http://numbersapi.com) will be used for the demonstration, so make sure the API is still up and running prior to class.

**Files:**

* [url_parameters.ipynb](Activities/06-Ins_URL_Parameters/Solved/url_parameters.ipynb)

Navigate to the 5.1 slides, and highlight the following:

* Each API call supports a set of parameters. These parameters can be used to help direct the API toward the data needed or be used to reduce the amount of data being returned by the server.

  * Ask the students: We've already made some API requests using parameters. Can anyone remember any examples?

    **Answer**: When using the `?format=json` tag.

* **Parameters** can be specified in one of two ways. Parameters can follow `/` forward slashes or be specified by parameter name and then by the parameter value.

  ```
  Parameter provided after /
  http://numbersapi.com/42
  ```

  ```
  Parameter provided using parameter name and value
  http://numbersapi.com/random?min=10?json
  ```

* When used with parameter names, URL parameters have to be separated from the request URL with the `?` symbol.

  ```
  http://numbersapi.com/random?min=10
  ```

* Multiple parameters can be passed in with the same URL by separating each parameter with an `&` symbol

  ```
  http://numbersapi.com/random?min=10&max=20
  ```

Open the solution, and conduct a dry walkthrough of the following solution. Touch upon the following discussion points:

* The requests `GET` function can be used to submit a parameterized request to the Numbers API to get trivia facts about the number 42.

  ```python
  import requests
  import json

  # Create parameterized url
  request_url = "http://numbersapi.com/42?json"

  # Submit and format request
  response_data = requests.get(request_url).json()
  print(json.dumps(response_data, indent=4))

  # Select fact
  response_data['text']
  ```

  ![url_parameters.png](Images/url_parameters.png)

Open the starter file, and live code the following:

* The Numbers API URL can be parameterized to execute for the number `8` instead of `42`.

  ```python
  # Create parameterized url
  request_url = "http://numbersapi.com/8?json"

  # Submit and format request
  response_data = requests.get(request_url).json()
  print(json.dumps(response_data, indent=4))

  # Select fact
  response_data['text']
  ```

  ![url_parameters_8.png](Images/url_parameters_8.png)

Ask the class the following question:

* What kind of parameters should be used when working with financial APIs? One example is dates. What are others? Hint: Think attributes related to people, stocks, bank accounts, credit scores, etc.

  **Answer:** Names, birthdays, Social Security numbers, tickers, trade limits, number of shares to buy, limit order dollar amounts, routing numbers, checking accounts, etc.

Ask the students if they have any remaining questions before moving on.

---

### 16. Students Do: House of Requests (25 min)

**Corresponding Activity:** [07-Stu_House_of_Requests](Activities/07-Stu_House_of_Requests)

This activity is dedicated to giving the students an opportunity to use a fun API. Students play a game of blackjack using the Deck of Cards API. The key skills reinforced in this activity include the execution of `GET` requests using the Python `requests library`, extraction of JSON elements, and parameterization of API request URLs.

Students can play the game against a classmate or imaginary dealer. Students are encouraged to work as partners so they can pair-program and play against one another.

**Files:**

* [url_parameters.ipynb](Activities/07-Stu_House_of_Requests/Unsolved/url_parameters.ipynb)

**Instructions:**

* [README.md](Activities/07-Stu_House_of_Requests/README.md)

---

### 17. Instructor Do: House of Requests Activity Review (5 min)

**Files:**

* [url_parameters.ipynb](Activities/07-Stu_House_of_Requests/Solved/url_parameters.ipynb)

Facilitate a dry walkthrough of the solution utilizing the following discussion points:

* Passing parameters to APIs through request URLs gives users the ability to configure and control API actions. By passing parameters to the request URLs for the Deck of Cards API, users can create and shuffle a deck of cards. Parameters also allow users to draw `n` number of cards from the deck.

  ```python
  create_deck_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"
  draw_cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
  shuffle_deck_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
  ```

  ![parameters.png](Images/parameters.png)

* The Deck of Cards API has some parameters that need to be specified using a forward slash `/`. There are other parameters that need to be passed using the `?` symbol.

  ![parameter_formats.png](Images/parameter_formats.png)

* String interpolation is a common way to pass parameters to request URLs. This allows for parameters to be assigned to variables and those variables to be interpolated into the request URLs. This also enables dynamic configuration of parameters and removes instances of hard-coded parameter values.

  ```python
  draw_cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
  shuffle_deck_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
  print(draw_cards_url)
  print(shuffle_deck_url)
  ```

  ```
  https://deckofcardsapi.com/api/deck/epigy7ynp5yi/draw/?count=2
  https://deckofcardsapi.com/api/deck/epigy7ynp5yi/shuffle/
  ```

* **Parameterized request URLs** are submitted like any other URL: using the `GET` request. Parameters help simplify the amount of data being returned from the output. This makes parsing JSON objects and rows easy, especially since JSON data often times has to be iterated. The more parameters used, the less data returned.

  ```python
  # Draw two cards
  drawn_cards = requests.get(draw_cards_url).json()
  ```

* In order to parse JSON data, the structure of the JSON data needs to be understood. JSON data includes parent objects, one or many JSON objects, and elements and attributes for each JSON object. Each of these has to be specified when extracting values from JSON output.

  ```python
  # Select returned card's value and suit (e.g., 3 of clubs)
  player_1_card_1 = drawn_cards['cards'][0]['value'] + " of " + drawn_cards['cards'][0]['suit']
  player_1_card_2 = drawn_cards['cards'][1]['value'] + " of " + drawn_cards['cards'][1]['suit']

  # Print player cards
  print(player_1_card_1)
  print(player_1_card_2)
  ```

  ```
  3 of HEARTS
  QUEEN of CLUBS
  ```

  ![parse_json.png](Images/parse_json.png)

Transition the class into a review session. Ask the following questions:

* In addition to `deck_id`, what other parameter values should be interpolated for the `draw_cards_url`?

  **Answer:** Count.

* If you were to contribute to the Deck of Cards API, what type of features or functionality would you want to enhance or add?

  **Answer:** Game options (e.g., poker, Go Fish, War, etc.).

  **Answer**: Automated dealing based off of game type (e.g., poker, Texas Hold'em, etc.)

  **Answer:** Game specific interactions (e.g., playing War compares player cards turn by turn).

  **Answer:** Turn-based gaming.

  **Answer:** Scoring.

* Has URL parameters made APIs more challenging to use or easier to use?

Ask if there are any remaining questions or comments before continuing.

---

### 18. Instructor Do: Recap (10 min)

This activity will conclude APIs Day 1. Recap the skills and concepts learned throughout the lesson. Engage the students by having students lead the recap as much as possible.

* Ask if there's a student who would like to volunteer to summarize what was learned today.

* Ask if any volunteers would like to add to what the previous student stated.

Guide students and the recap session. Use the below sample statements and questions to guide students if student engagement and participation is low. Only use these if necessary; let the students drive the session as much as possible.

* Some of the APIs used in the lesson were Quandl, World Bank, Numbers API, Deck of Cards, U.S. Spending Stats, Random Jokes, etc. What APIs did you find to be the most interesting?

* What APIs were the most useful? In what ways could you continue to use these APIs, especially in everyday life?

Ask students to identify two things they'd like to practice on from today's lesson that they might have struggled with conceptually. Encourage them to do additional practice and reading outside of class to reinforce their knowledge and skill.

Finish the recap with a few statements of encouragement.

Tell students they need to give themselves, yet again, a round of applause. They've added yet another valuable tool to their developer's toolkit.

Remind students that completing this amount of work in this time period already means they've proven their aptitude. It's just growth from here.

The next step for APIs is to work with authenticated APIs, as well as software development kits (SDKs) like Alpaca, an API for stock trading. This is where the class will get heavy into accessing and using financial data via APIs.

Before students leave for the end of the day, give them a small homework assignment. Instruct students to sign up for the below APIs. Students will need to sign up for these APIs before coming to the next class; these APIs will be used in Lesson 5.2. Slack out the links so that students will have them. Students who do not have access will not be able to complete all of Lesson 5.2's activities.

Emphasize to students that they should be signing up for free development accounts following the install guide. There is no need to purchase any services.

* [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

* [Alpaca](https://app.alpaca.markets/signup)

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
