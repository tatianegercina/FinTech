## 5.2 Lesson Plan: API Mania!

---

### Overview

Today's class will expose students to the exciting and innovative FinTech APIs that have been disrupting the industry. There are so many groundbreaking APIs in the FinTech industry that it's almost impossible not to get excited about them. APIs used in this lesson include **Quandl**, an API that provides access to historical stock data, and **Alpaca**, an API for stock trading. Both of these services help democratize and decentralize financial data stores and analytic approaches. And this is just the beginning. New APIs and SDKs (software development kits) are released regularly, which means there's always new technologies to use to enhance and advance the FinTech industry. It's a new world, and it's a world to be excited about!

This lesson presents students with hands-on experience using APIs in a Python environment, requesting and leveraging API keys, and securely storing API keys and credentials as **environment variables** (variables that exist at the operating system level). Students will programmatically submit API requests to Quandl using the Python `requests` library and Alpacas' software development kit, a library packaged to provide developers with access to Alpacas's endpoints and functions.

### Class Objectives

By the end of today's class, students will be able to:

* Use an API key to fetch authenticated requests using the Requests Library.

* Set/Export environment variables in Windows and Mac and retrieve them in Python.

* Explain the difference between an API and SDK.

* Set authentication for a Python SDK.

* Use a Python SDK to fetch financial data.

* Use SDKs to analyze financial data.

* Retrieve historical stock information using the Quandl API.

* Acknowledge the general regulations for FinTech companies in Canada.

### Instructor Notes

* Slack out the [PyViz Installation Guide](../../06-PyViz/Supplemental/PyVizInstallationGuide.md). Tell students to complete the installations and verify them with a TA before the end of the next class.

* This lesson includes the demonstration and use of two APIs that require users to have accounts and API keys. You, students, and TAs will all need to have created accounts and received API keys prior to this lesson. The following links can be used to sign up for accounts and get keys. Slack these links out to TAs and students before the beginning of the lesson, so they have ample time to sign up if they haven't. There will be an activity dedicated to confirming that each student has signed up.

  * [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

  * [Alpaca](https://app.alpaca.markets/signup)

* Since this lesson will work with API keys, it is important that you and the students do not hardcode or print any API keys or request URLs with keys. All keys must be stored in environment variables and then referred to using the `python-dotenv` Python library.

* This lesson has a dependency on the Quandl and Alpaca APIs being up and running. Visit each site and execute preemptive API calls to ensure connectivity. It is imperative to confirm that the APIs used in this lesson are executing as expected.

* Some students may have experience working with making API calls. Keep an eye out for any students who might be advanced with APIs and could help with review activities. Allowing advanced students to conduct reviews and help their peers is a great way to keep them engaged and interested in the material.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [5.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=50ef1953-f071-47b8-8bb3-aab10107ea41) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 5.2 Slides](https://docs.google.com/presentation/d/1bVZNg1ZPB_x-JVVnQAFxvQpdQTamJX2OPn-49QLw4NA/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Today will take students to the next step in using APIs. Students will transition from using the Python `requests` library to using SDKs that provide practical use cases for FinTech analysis.

Welcome students to the second day of APIs. Open the lesson slides, review the class objectives, then move to "The Rise of APIs" section, highlighting the following points:

* While today's class will be a continuation of the last session, there will be a stronger emphasis on how to use FinTech APIs effectively.

* There are several FinTech APIs available that grant users the ability to create and execute analytic pipelines on various forms of financial data.

* Because APIs often offer practical services, they may require subscriptions or payment. Companies use API keys and user accounts to ensure billing and secure transmission of financial and other confidential information.

* You will get hands-on experience using Quandl (to fetch historical stock data) and Alpaca (a trading API).

Explain to students that Canada's Department of Finance and Provincial Finance Regulators are responsible for providing a financial regulatory framework. However, the monetary policy for the Canadian FinTech industry is still under development according to [a report released by the Competition Bureau](https://www.competitionbureau.gc.ca/eic/site/cb-bc.nsf/eng/04322.html).

* Within the general regulatory framework, any company interested in providing technology-led financial services should, at the minimum, comply with [The Personal Information Protection and Electronic Documents Act (PIPEDA)](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) and [Canada's Anti-Money Laundering and Anti-Terrorist Financing Regime (AML/CT)](https://www.fintrac-canafe.gc.ca/fintrac-canafe/antimltf-eng).

* Companies interested in offering financial services related to cryptocurrencies or tokens should follow the guidance published by the Canadian Securities Administrators (CSA) in the [Staff Notice 46-308 about Securities Law Implications for Offerings of Tokens](https://www.securities-administrators.ca/aboutcsa.aspx?id=1704).

Answer any questions before moving on.

---

### 2. Instructor Do: API Keys (10 min) (Critical)

In this activity, students and the instructor will participate in a facilitated discussion regarding API keys. Students will also learn the "what, why, and how" of API keys.

Guided questions are provided to help facilitate discussion. Use these questions as time permits.

Navigate to the "API Keys" section of the lesson slides and highlight the following:

* Many companies that offer APIs require users to sign up for API keys. **API keys** are access tokens that serve as a credential (like a user name or password) granting users the privileges and permissions needed to submit API requests. APIs use keys as unique identifiers, in order to recognize which users submitted which requests.

* **API keys** are like the keys to a house or a car. Without a key, one cannot gain access or make use of the services provided by an API. APIs that require keys will reject any request that does not include an API key.

* The main reason why companies use API keys is to monitor and control user requests, and receive compensation for their services and intellectual property. Because API keys detail permissions and privileges for users, companies can programmatically disable and enable API privileges based on the requests submitted.

* Obtaining an API key is like getting the key to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please.

Now, initiate a facilitated discussion with the following guided questions and discussion points. Choose two or three questions to ask, depending on the time available.

* Ask the students: API keys are submitted with all API requests. Does it seem safe to transmit a unique key over the internet with every request? If no, why not?

  * **Answer:** It is not safe. This is because API keys transmitted over the internet are not considered a proper security layer. If someone were to intercept client-server communications, they'd be able to retrieve a user's API key.

* Ask: If API keys can be intercepted with every submitted request, why use them?

  * **Answer:** API keys are used because they prohibit nonregistered users from making requests. When an API requires a key, a key must be provided for the API to execute. This forces users to register for the API and request an API key, which permits the owner of the API to monitor that person's usage and charge for services.

* Pose the following question: What type of privileges and permissions could be tied to an API key? (Hint: CRUD.)

  * **Answer:** Create, read, update, delete.

* Ask: Is there anything that can be done to securely transmit an API key so that others cannot gain access to the key? If yes, provide an example of how.

  * **Answer:** API keys can be made secure through encryption. Many companies offering APIs, like Amazon Web Services, provide users with API keys as well as **secret keys**. Secret keys work much like API keys; however, they're typically encrypted so they can be kept private.

* Ask: Any guesses regarding how to submit a request with an API key?

  * **Answer:** Submit the key with the request URL as a parameter.

End the activity by asking the students if they have any further questions.

---

### 3. Instructor Do: Keys to the FinTech Kingdom (5 min)

Over the next couple of activities, students will work with APIs that require keys for access. Use this time to engage with them on API keys through a facilitated discussion.

Navigate to the "Keys to the FinTech Kingdome" section of the slides and ask students the following review questions:

* Do *all* APIs require API keys?

  **Answer:** No. Only some APIs require keys to be used. Others allow users to submit requests for free (with rate limits).

* Why require users to have an API key, when requests can be sent without APIs?

  **Answer:** API keys allow companies to monitor, analyze, and enforce rate limits.

* What happens when the `?api_key=` tag is used? Is a function executed, or is a parameter passed?

  **Answer:** A parameter is passed.

* Can more than one user have the same API key?

  **Answer:** No. API keys are unique identifiers. Each key is assigned to one user.

* Do you think API keys are naturally secure?

  **Answer:** No, they are not. API keys are transmitted across the network and are not naturally encrypted. API keys can be encrypted to make them private.

* Is there a problem with sharing an API key?

  **Answer:** Yes. Rate limits are tied to API keys. Sharing an API key would mean sharing the total number of requests allowed with another individual. Sharing keys could also result in someone else charging your account for billable services.

Get students excited about FinTech APIs by highlighting the following points:

* Many APIs, like Plaid, are disrupting the financial industry. Many APIs have grassroots initiatives, meaning they are creating tools and technologies for people, rather than corporations. These efforts echo the open-source movement.

* Even though many APIs require keys, their services are often free. Obtaining an API key is like getting the keys to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please. There are limitations, but services are often still free.

Ask if there are any questions or comments before moving on.

---

### 4. Instructor Do: Creating Environment Variables (10 min) (Critical)

In this activity, students will learn how to create a `.env` file to store their keys as environment variables. This demo will also include exporting environment variables, so that they can be used in Python as well as other applications and programs.

**Files:**

* [example.env](Activities/01-Ins_Create_Env_Variables/Unsolved/example.env)

Open the lesson slides, move to the "Environment Variables" section, and highlight the following discussion points:

* Exporting an environment variable exposes it to all applications and programs sharing the same parent process (e.g., a terminal or Python kernel). Each application and program inherits the variable, which allows developers to make calls using `os.getenv` to access the data stored in the variable.

* A common way to export environment variables is to create a `.env` file. The `.env` file will define the environment variables that you would like to export within the environment of your local projects. The `.env` approach is faster than exporting the variables individually.

* Because environment variables are at the operating system level, variables can be passed down from parent processes to child processes.

* An environment variable created in Python cannot be accessed by a terminal; in contrast, an environment variable created in a terminal can be accessed by Python.

* You can set environment variables in Mac or Windows.

Open a plain text editor, such as VSCode or Sublime Text, and create a new blank file. Perform a live demo of creating and exporting environment variables with the `.env` file by highlighting the following:

* Now, we will create a `.env` file to store the API keys as environment variables.

* To set an environment variable, you have to define a name for that variable. Let's start by creating a variable to store the Quandl API key.

* Set the variable name as `QUANDL_API_KEY` and assign your API key to it.

  ```text
  QUANDL_API_KEY="ENTER YOUR API KEY HERE"
  ```

* Once you set your brand new environment variable, save the file as `.env`. You may receive a warning message that states that the file will be hidden.

  ![create_env_file](Images/create_env_file.gif)

* Once the `.env` file has been created, it must be loaded into memory by a package like `python-dotenv` so that the environment variables can be sourced. We will discuss methods of loading a `.env` in the next activity.

Ask if there are any questions, and then move on to the next activity.

---

### 5. Instructor Do: Calling Environment Variables (10 min) (Critical)

In this activity, students will learn how to call API keys as environment variables using the `dotenv` Python package.

**Important Note:** Ensure that you have a local `.env` file containing your `QUANDL_API_KEY` into the `Solved` folder before running the demo.

**Files:**

* [env_variables.ipynb](Activities/02-Ins_Call_Env_Variables/Solved/env_variables.ipynb)

Have students recall the concept of environment variables by asking the following question:

* Imagine you signed up for 10 APIs, and each API gave you a key. It would be hard to memorize each key, so you'd need to find some way to save the keys. What are some possible approaches?

  **Answer:** One approach could include tracking the keys in an Excel document. The document could be password protected, to preserve confidentiality.

  **Answer:** Environment variables could be created, and the keys could be stored in the variables.

Referring to the slides, explain the process of calling environment variables.

* In order to make environment variables inheritable, they have to be exported and sourced.

* To do this, we call upon the `os.getenv` function.

Open the solved version of the Jupyter notebook. Next, run the code on every cell and highlight the following:

* Environment variables are variables just like Python variables are; however, instead of being created in a Python application, they're created on a user's computer.

* Environment variables are operating-system-level variables that are accessible by all programs and applications with access to that environment.

* Environment variables are given a name, and they can hold any string value. It is important to note that environment variables can only hold `strings`.

* Like with Python variables, data within environment variables can be accessed by making a call to the variable.

* An easy, convenient, and secure way to store any data that needs to be accessed across programs and applications is to use environment variables. This includes API keys, as well as user credentials, and program installation paths (e.g., Python).

* For reading our `.env` file and setting its defined environment variables in our local environment, we import the `load_dotenv()` method from the `python-dotenv` package.

  ```python
  # Import dotenv package for setting environment variables
  from dotenv import load_dotenv
  ```

* For fetching our environment variables from the local environment and loading them into an in-memory python variable, we import the `os` package.

  ```python
  # Import os package
  import os
  ```

* Setting the environment variables in our `.env` file is as easy as calling the `load_dotenv()` method.

  ```python
  # Set environment variables from the .env in the local environment
  load_dotenv()
  ```

* Keep in mind that unless a file location `string` is passed, `load_dotenv` will look for a `.env` in the root directory from which your Python code is executing.

* Once an environment variable is declared, it can be called using the `os.getenv` function. The input to the `os.getenv` function is the name of the environment variable. The output should then be stored as a Python variable to be used at a later time.

  ```python
  # Retrieve API key and store as Python variable
  api_key = os.getenv("QUANDL_API_KEY")
  ```

* A way to check if the environment variable was correctly loaded is to print the data type of the Python variable.

* If the environment variable exists, Python will return `str` as the data type.

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  type(api_key)
  ```

  ```text
  str
  ```

* If an environment variable does not exist, Python will return `NoneType` as the data type. An empty environment variable will cause an API call to fail.

  ```python
  # Retrieve an environment variable that doesn't exist
  api_key_bis = os.getenv("MY_QUANDL_API_KEY")
  type(api_key_bis)
  ```

  ```text
  NoneType
  ```

* If an API key doesn't seem to be working right, double-check your environment variable by reviewing your `.env` file.

* The variable name created in the `.env` file must match the string value passed to the `os.getenv` function.

Emphasize to students that they need to make sure that the environment variable `print` statement is not pushed into Git, or any other repository, as it would expose their API keys to anyone who has access to the repository.

Ask students if there are any questions before continuing.

---

### 6. Student Do: Under Lock and Key (20 min)

The previous modules focused on the instructor demoing how to create, store, and use API keys with environment variables. Students will now engage in a bridge activity that involves retrieving a Quandl API key, and submitting a Quandl API request with the key stored as environment variables. This will be students' first opportunity for hands-on practice with API keys and environment variables.

Working with environment variables can be a little tricky, especially if they are not declared and exported correctly. Make sure that you and the TAs are circulating during this activity to help resolve any technical issues students face.

If students finish early, use the extra time to review the final two guided review questions from the next activity.

**Files:**

* [env_variables.ipynb](Activities/03-Stu_Under_Lock_And_Key/Unsolved/env_variables.ipynb)

* [example.env](Activities/03-Stu_Under_Lock_And_Key/Solved/example.env)

**Instructions:**

* [README.md](Activities/03-Stu_Under_Lock_And_Key/README.md)

---

### 7. Instructor Do: Under Lock and Key Activity Review (10 min)

**Important Note:** Ensure that you have saved a local `.env` file containing your `QUANDL_API_KEY` in the `Solved` folder before running the solution.

**Files:**

* [env_variables.ipynb](Activities/03-Stu_Under_Lock_And_Key/Solved/env_variables.ipynb)

Kick off the activity review session by asking students to summarize the process of creating and using environment variables with APIs. Engage the students with the following questions:

* After acquiring an API key, what's the first thing that should be done?

  * **Answer:** The key should be stored as an environment variable in your projects `.env` file.

* Once an environment variable has been defined in your `.env` file, what should happen next?

  * **Answer:** The `.env` file should be read using the `load_dotenv()` method and the environment variables exported/set.

* What should be done after the `.env` file has been sourced?

  * **Answer:** The environment variable should be called in Python using the `os.getenv` function.

* Is there ever a time where an API key should be hard-coded within a Python script?

  * **Answer:** No. The best practice for keeping API keys secure is to store them in environment variables. This practice should always be used.

Open the solution and end the review session with a quick walkthrough of the solution.

* Once created, the environment variables are then shared with all child processes. For example, when the `load_dotenv()` method is executed, it will ensure the `QUANDL_API_KEY` variable is accessible by all processes running in the environment that executed the Python file process.

  ```shell
  QUANDL_API_KEY="ENTER YOUR KEY HERE"
  ```

* Environment variables can be accessed in Python with the `os` library. The library has to be imported before it can be used. The `os` library has an `os.getenv` function that can be used to retrieve environment variables from the operating system. Once retrieved, the value can be saved as a Python variable (e.g., `api_key`).

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  ```

* Once stored as a Python variable, the environment variable value can be used for processing. In this case, the `QUANDL_API_KEY` is stored as the Python variable `api_key`, and then concatenated with the request URL. The concatenated request URL will then be used to submit a request to the Quandl API.

  ```python
  # Define the base request URL
  request_url = "https://www.quandl.com/api/v3/datasets/WIKI/MSFT.json?api_key="

  # Concatenate request_url and api_key. Store as new variable
  request_url = request_url + api_key
  ```

If time remains, ask two final, guided questions:

* If a user were to export the environment variable `QUANDL_API_KEY` using a terminal, but then launched Jupyter Lab in a different terminal window, would Jupyter Lab be able to retrieve the environment variable?

  * **Answer:** No. Environment variables are sourced to current and child processes. Because a new terminal window is used to launch Jupyter Lab, the environment variable `QUANDL_API_KEY` will be out of scope.

* If environment variables are inherited through parent-child processes, what happens when a parent process is terminated?

  * **Answer:** The environment variable is deleted and no longer available for use.

Ask for any remaining questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Intro to SDKs (10 min) (Critical)

The past two lessons have focused on students using the Python requests library to submit API requests. Students will now learn how to use proprietary software development kits (SDKs) to submit API calls and streamline development efforts.

Communicate to students that while the Python requests library is a great tool with which to submit requests to APIs, there are more sophisticated APIs out there that offer tools called software development kits that provide a packaged way to access API endpoints and submit calls.

Navigate to the "SDKs" section of the slides and initiate a facilitated discussion by highlighting the following:

* SDKs offer programmatic ways to access API endpoints without using the requests library. Instead of using the requests library to execute API calls, users would use functions provided by the SDK. For example, an SDK would provide a GET function similar to the `requests.get` function offered by the Python requests library. The SDK might also provide additional attributes and functions for filtering and calculating data.

* Example companies that offer SDKs are Quandl, Alpaca, Investors Exchange, Google, and AWS.

* Pose the following question to facilitate discussion:

  * What type of operations can you imagine being offered by SDKs? We already know GET operations are one of them. What are some others?

    **Answer:** Create, update, and delete operations.

* Working with SDKs removes the need to build API request URLs. Instead of using request URLs to make parameterized API calls, SDK functions and attributes are used.

* The following code depicts an example of the differences between using a request URL and an SDK.

  ```python
  # Using the Python requests library
  requests.get("https://www.quandl.com/api/v3/datasets/WIKI/AMD?api_key=1A3")

  # Using the Quandl SDK
  quandl.get("WIKI/AMD", rows=5)
  ```

Explain to students that in the code above, they can note that using an SDK looks more straightforward and cleaner. Also, it's more secure since SDKs add an additional layer of security by avoiding passing sensitive parameters, like API keys, as plain text in a request URL.

Ask students the following guided question:

* Why would companies create SDKs when Python provides users with the requests library?

    **Answer:** By creating SDKs, companies allow users to interact with their APIs in a more powerful way. The requests library only supports so many functions (GET, POST, etc.). However, by providing users with an SDK, companies can give users access to in-house built attributes and functions that can provide more value than the functions in the requests library.

    **Answer:** When writing a Python script, using a Python SDK can often be cleaner and easier to understand and integrate in one's code. SDKs allow developers to use syntax and language features that often simplify and clean up code. A decent example of this is evidenced when comparing the URL request to Quandl with the `quandl.get("WIKI/AMD", rows=5)` function. Both will extract historical stock; however, the `quandl.get` function is easier to use and looks cleaner.

* Because SDKs provide out-of-the-box functions that can be used with the API, developers do not have to worry about reinventing the wheel. What is an example of a function or operation a FinTech SDK might provide?

  **Answer:** A FinTech SDK might provide a function that calculates Sharpe ratios, which means users would not need to create this functionality themselves; they'd be able to use the SDK to extract historical stock data AND calculate Sharpe ratios. The requests library would only support data extraction.

Explain to students that in the FinTech industry, they will face APIs that provide SDKs and others that do not. That's why they need to understand how to access an API via a request URL using the Python requests library, and how to install and operate an SDK.

Ask students if there are any questions before moving on.

---

### 10. Instructor Do: Intro to Alpaca (15 min)

Navigate to the "Introduction to Alpaca" section of the lesson slides, and introduce the Alpaca SDK by highlighting how it is disrupting the FinTech data industry:

* According to a [Forbes article from December 2019](https://www.forbes.com/sites/bernardmarr/2020/12/30/the-top-5-fintech-trends-everyone-should-be-watching-in-2020/#5ce0c02b4846), FinTech is transforming into a new data industry that focuses on and specializes in the democratization of financial services. This is mainly due to startups like **Alpaca**, that are seeking to enrich and empower consumers through financial data and technology.

* SDKs provide out-of-the-box functions that can be used with the API so that developers do not have to worry about reinventing the wheel. [Alpaca](https://alpaca.markets/) exemplifies a great API that eases the work involved in data retrieval through APIs by using its SDK.

* Alpaca is a trading API that encapsulates banking, security, and regulatory complexity, allowing FinTech startups to build brokerage apps on top for free and quickly.

* In addition to its trading capabilities, Alpaca is an example of a financial API that you can use, as a FinTech professional, to fetch current stock market data free of charge from five different exchanges (IEX, NYSE National, NYSE Chicago, Nasdaq BX, and Nasdaq PSX). Today, you will learn how to use Alpaca to retrieve stock data that can be used to develop financial applications.

Remind students that to access the Alpaca API, they need to install the `alpaca-trade-api` SDK and set their API and the secret keys in a `.env` file as it's indicated in the introduction lesson.

Take a couple of minutes to verify if everyone in the class is ready with the Alpaca SDK installed and the Alpaca keys on-hand. Ask your TAs to kindly assist any student who may not be prepared to continue, in the meantime, open the Alpaca website and highlight the following.

* To start using Alpaca, you need to sign up to have access to your Alpaca keys.

* Once you are signed up, you can log in to the Alpaca dashboard to fetch your keys.

Continue by logging into the Alpaca dashboard using your personal account.

![alpaca-login](Images/alpaca-login.gif)

After logging into your Alpaca dashboard, explain to students that they will need to access their "Paper Account", then they'll a find a section named "Your API Keys" where they can view their keys by clicking on the "View" button.

![alpaca-keys-section](Images/alpaca-keys-section.png)

Explain to students that the first time that they click on the "View" button, they will see their `API Key ID` and `Secret Key`. This is the only time when they will see both keys, so it's crucial to record the keys in their `.env` file at this time.

![alpaca-keys](Images/alpaca-keys.png)

The secret key will disappear when they log out or navigate to a different page of the Alpaca dashboard. If they lost their `Secret Key`, it can be regenerated by clicking on the "View" button to show the `API Key ID`. Next, they need to click on the "Regenerate Key" button to create a brand new pair of keys. It's important to remark that the previous keys will be invalidated.

![alpaca-keys-regeneration](Images/alpaca-keys-regeneration.gif)

Answer any questions students may have, and be sure that all the students have created their keys and installed the Alpaca SDK before continuing to the next activity.

---

### 11. Instructor Do: Alpaca Demo (15 min)

In this activity, students will receive an instructor-led demo of the Alpaca SDK. The instructor will demonstrate to students how to connect to the Alpaca paper account from a Python environment.

Have the `.env` file prepared with your Alpaca API Keys before class so that it does not need to be created during the activity.

**Files:**

* [alpaca-demo.ipynb](Activities/04-Ins_Alpaca_Demo/Solved/alpaca-demo.ipynb)

Emphasize to students that one of the cool things about Alpaca is that it provides developers with a paper trading account for users to get started. The paper account provides a real-time simulation environment where they can test their code using free, real-time market data.

Explain to students that the paper account is excellent because it gives developers a space to play with Alpaca without having to incur charges. This grants developers the ability to focus on what they intend to build rather than how they're going to get their data.

Open the unsolved version of the Jupyter notebook and live code the demo. Continue by leading students on the environment preparation by highlighting the following:

* To start using the Alpaca SDK, you need to import the `tradeapi` class from the `alpaca_trade_api` library and some other well-known libraries we have already used.

  ```python
  # Initial imports
  import os
  import requests
  import pandas as pd
  from dotenv import load_dotenv
  import alpaca_trade_api as tradeapi

  %matplotlib inline
  ```

* Since we are going to make an authenticated connection to the Alpaca API through its SDK, we need to store our Alpaca API and secret keys into our `.env` file and name them as `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` respectively.

* After importing the required Python libraries, we have to load the environment variables using the `load_dotenv()` function and store the Alpaca keys as Python variables.

  ```python
  # Load .env enviroment variables
  load_dotenv()

  # Set Alpaca API key and secret
  alpaca_api_key = os.getenv("ALPACA_API_KEY")
  alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
  ```

* Now we are ready to connect to Alpaca! To use the Alpaca SDK, we need to create an object that will encapsulate the entire Alpaca functionality.

* To generate the alpaca object to retrieve stock market data, we will use the `tradeapi.REST()` function by passing the Alpaca keys as arguments and setting the API version we want to use. The current Alpaca API version is 2.0.

  ```python
  # Create the Alpaca API object
  alpaca = tradeapi.REST(
      alpaca_api_key,
      alpaca_secret_key,
      api_version="v2")
  ```

* Now, let's fetch the current closing price of Facebook (`FB`) and Twitter (`TWTR`), two technology stocks that may be interesting to invest in. First, we need to set a variable with the current date in the ISO format.

  ```python
  # Format current date as ISO format
  today = pd.Timestamp("2020-07-14", tz="America/New_York").isoformat()
  ```

* To define the current date as an ISO format date, we use the `TimeStamp` function from Pandas to transform the current date that is passed as a string argument using the `YEAR-MONTH-DAY` format. Next, we link the `isoformat()` function to format the date following the ISO standard.

**Note:** While you follow this example, you may want to change the date to today.

* Using the Alpaca API, we can retrieve stock data from up to `200` ticker names. We need to pass the symbols as a Python list. Let's create a list of the tech companies we want to invest in.

  ```python
  # Set the tickers
  tickers = ["FB", "TWTR"]
  ```

* Another important parameter we need to define to fetch stock data is the time frame we want to use. We can set the `timeframe` parameter in minutes (`1Min`, `5Min`, `15Min`) or one day (`1D`). We will create a variable called `timeframe` to set this parameter as `1D`.

  ```python
  # Set timeframe to one day ('1D') for the Alpaca API
  timeframe = "1D"
  ```

* We are all set! Let's fetch the current closing prices for `FB` and `TWTR` using the `alpaca.get_barset()` function. Alpaca Python SDK automatically converts the resulting JSON response to a Pandas DataFrame if you use the `df` property.

  ```python
  # Get current closing prices for FB and TWTR
  df_portfolio = alpaca.get_barset(
      tickers,
      timeframe,
      start = today,
      end = today
  ).df

  # Display sample data
  df_portfolio
  ```

  ![fetch-current-alpaca-stock-data](Images/fetch-current-alpaca-stock-data.png)

Explain to students that the `get_barset()` function from the `Alpaca` SDK takes in the following parameters that can be used to refine the query results: `symbols`, `timeframe`, `limit`, `start`, `end`, `after`, and `until`.

Slack out the following links and encourage students to learn more about the details of this function:

1. [Alpaca bars API documentation:](https://alpaca.markets/docs/api-documentation/api-v2/market-data/bars/) Here you can learn more about the values that can be set to each parameter.

2. [Market Data Examples:](https://alpaca.markets/docs/api-documentation/how-to/market-data/) This page provides code examples of the `get_barset()` function in several programming languages.

Continue the demo highlighting the following.

* Note in the previous code, that to retrieve the current closing price of `FB` and `TWTR`, we set the `start` and `end` day as today's date. Suppose you want to analyze the daily returns of these tech companies to start assessing if they are a good investment option, and you want to retrieve the closing prices from the last year. As you may guess, it's as simple as setting the `start` and `end` parameters to a one year period.

  ```python
  # Format start and end dates as ISO format for one year period
  start = pd.Timestamp("2019-07-14", tz="America/New_York").isoformat()
  end = pd.Timestamp("2020-07-14", tz="America/New_York").isoformat()
  ```

* We take advantage of the benefits of using an SDK, and we create a new DataFrame using the `alpaca_getbarset()` method by modifying the start and end dates.

  ```python
  # Get closing prices for FB and TWTR from the last year
  df_portfolio_year = alpaca.get_barset(
      tickers,
      timeframe,
      start = start,
      end = end
  ).df

  # Display sample data
  df_portfolio_year.head(10)
  ```

  ![fetch-yearly-alpaca-stock-data](Images/fetch-yearly-alpaca-stock-data.png)

* To analyze the closing prices, let's create a new DataFrame containing only the closing prices from Facebook and Twitter over the last year.

  ```python
  # Create and empty DataFrame for closing prices
  df_closing_prices = pd.DataFrame()

  # Fetch the closing prices of FB and TWTR
  df_closing_prices["FB"] = df_portfolio_year["FB"]["close"]
  df_closing_prices["TWTR"] = df_portfolio_year["TWTR"]["close"]

  # Drop the time component of the date
  df_closing_prices.index = df_closing_prices.index.date

  # Display sample data
  df_closing_prices.head(10)
  ```

  ![fetch-yearly-closing-prices](Images/fetch-yearly-closing-prices.png)

* Note that the DataFrame created by the Alpaca API is multi-indexed. To pick the `FB` and `TWTR` closing prices from the `df_portfolio_year` DataFrame we use column keys.

* Finally, we compute the daily returns using the Pandas `pct_change()` function and plot the results.

  ```python
  # Compute daily returns
  df_daily_returns = df_closing_prices.pct_change().dropna()

  # Display sample data
  df_daily_returns.head()
  ```

  ![fb-twtr-daily-returns](Images/fb-twtr-daily-returns.png)

  ```python
  # Plot daily returns
  df_daily_returns.plot(title="Daily Returns of FB and TWTR over the Last Year")
  ```

  ![fb-twtr-daily-returns-plot](Images/fb-twtr-daily-returns-plot.png)

* It seems like Twitter had some bad times throughout the last year, but now, both stocks look like an attractive investment option, don't you think?

Ask students for any thoughts and answer any questions before moving on.

---

### 12. Students Do: Investment Value (25 min)

In this activity, students will use the Alpaca SDK to calculate the present value of a stock portfolio.

**Files:**

* [example.env](Activities/05-Stu_Investment_Value/Unsolved/example.env)

* [investment-value.ipynb](Activities/05-Stu_Investment_Value/Unsolved/investment-value.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Investment_Value/README.md)

---

### 13. Instructor Do: Emotional Break (10 min)

Facilitate discussion by asking students about their experiences working with API keys and SDKs.

Ask students about the pace of the class. Is it going too fast, too slow, or just right?

Empower students to continue on by emphasizing that they're one step away from adding Alpaca to their toolkit. Reiterate that Alpaca is going to help them acquire the data they need to perform financial analysis, and it will broker the communication channel between stock exchanges and FinTech application servers.

Remind students that they are making excellent progress. Not only are they submitting requests to an API, but they're also submitting authenticated requests in a programmatic way using SDKs.

If time remains, ask the following questions:

* What data type can environment variables be stored as?

  **Answer:** String

* Why might Alpaca be considered a FinTech disrupter?

  **Answer:** Alpaca is changing the way developers and consumers can get access to FinTech data. Not only is Alpaca providing a technology platform to get access to FinTech data, but it is also providing analytic and insight products to make data-driven decisions.

* How glad are you that SDKs don't require users to build long, parameterized request URLs like the Python `requests` library?

Ask students if they have any questions before moving on.

---

### 14. Instructor Do: Investment Value Activity Review (10 min)

**Files:**

* [example.env](Activities/05-Stu_Investment_Value/Solved/example.env)

* [investment-value.ipynb](Activities/05-Stu_Investment_Value/Solved/investment-value.ipynb)

Open the solved version of the Jupyter notebook and conduct a dry walkthrough review of the solution by highlighting the following.

* As you have experienced in this activity, SDKs and APIs are great complements to your current Python skills.

* Now you know how to retrieve financial data to boost your finance application and start creating analytical tools to better understand financial data.

* To solve this activity, we start by importing the required libraries.

  ```python
  # Initial imports
  import os
  import requests
  import pandas as pd
  from dotenv import load_dotenv
  import alpaca_trade_api as tradeapi

  %matplotlib inline
  ```

* To compute the value of the stock portfolio, we start by creating a DataFrame to store the number of `MSFT` and `AAPL` shares in the portfolio.

  ```python
  # Set current amount of shares data
  shares_data = {
      "shares": [200, 320]
  }

  # Set the tickers
  tickers = ["MSFT", "AAPL"]

  # Create the shares DataFrame
  df_shares = pd.DataFrame(shares_data, index=tickers)

  # Display shares data
  df_shares
  ```

  ![number-shares](Images/number-shares.png)

* Next, we load the Alpaca keys that we have stored as environment variables.

  ```python
  # Load .env environment variables
  load_dotenv()
  ```

  ```text
  True
  ```

  ```python
  # Set Alpaca API key and secret
  alpaca_api_key = os.getenv("ALPACA_API_KEY")
  alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

  # Verify that Alpaca key and secret were correctly loaded
  print(f"Alpaca Key type: {type(alpaca_api_key)}")
  print(f"Alpaca Secret Key type: {type(alpaca_secret_key)}")
  ```

  ```text
  Alpaca Key type: <class 'str'>
  Alpaca Secret Key type: <class 'str'>
  ```

* Note that we printed the Alpaca keys data type as a mechanism to validate if they were successfully imported.

* The next step is to create the Alpaca API object.

  ```python
  # Create the Alpaca API object
  alpaca = tradeapi.REST(
      alpaca_api_key,
      alpaca_secret_key,
      api_version="v2")
  ```

* Since we will compute the current value in dollars of our stock portfolio, we create a variable called `today` with the current date using the ISO format.

  ```python
  # Format current date as ISO format
  today = pd.Timestamp("2020-07-14", tz="America/New_York").isoformat()
  ````

* We will fetch daily data, so we set a `timeframe` variable as `1D` to fetch closing prices on a daily basis.

  ```python
  # Set timeframe to one day ('1D') for the Alpaca API
  timeframe = "1D"
  ```

* We retrieve the current closing prices using the `get_barset()` function from the Alpaca SDK and passing the `tickers`, `timeframe`, and `today` variables as parameters.

  ```python
  # Get current closing prices for MSFT and AAPL
  df_portfolio = alpaca.get_barset(
      tickers,
      timeframe,
      start = today,
      end = today
  ).df

  # Display sample data
  df_portfolio
  ```

  ![current-tickers-closing-prices](Images/current-tickers-closing-prices.png)

* To calculate the current value in dollars of the stock portfolio, we fetch the closing prices of `MSFT` and `AAPL` by picking the values using the column keys of the multi-indexed DataFrame.

  ```python
  # Fetch the current closing prices from the DataFrame
  msft_price = float(df_portfolio["MSFT"]["close"])
  aapl_price = float(df_portfolio["AAPL"]["close"])
  ```

* Once we retrieve the current value of shares, we compute the present value of the stock portfolio by multiplying the number of each share by its value in dollars.

  ```python
  # Compute the current value in dollars of the stock portfolio
  msft_value = msft_price * df_shares.loc["MSFT"]["shares"]
  aapl_value = aapl_price * df_shares.loc["AAPL"]["shares"]

  # Print the current value of the stocks portfolio
  print(f"The current value of the {df_shares.loc['MSFT']['shares']} MSFT shares is ${msft_value:0.2f}")
  print(f"The current value of the {df_shares.loc['AAPL']['shares']} AAPL shares is ${aapl_value:0.2f}")
  ```

  ```text
  The current value of the 200 MSFT shares is $41678.00
  The current value of the 320 AAPL shares is $124227.20
  ```

* To visualize the portfolio composition, we create a DataFrame to store each stock's current value as columns. Having the stock value in columns will ease the creation of the plot.

  ```python
  # Set the data for the shares value DataFrame
  value_data = {
      "MSFT": [msft_value],
      "AAPL": [aapl_value]
  }

  # Create a DataFrame with the current value of shares
  df_value = pd.DataFrame(value_data)

  # Display DataFrame data
  df_value
  ```

  ![charts-df](Images/charts-df.png)

* Now, we create a pie chart to show the proportion of stocks in the portfolio and a bar plot to present the current value in dollars of each ticker.

  ```python
  # Create a pie chart to show the proportion of stocks in the portfolio
  df_shares.plot.pie(y="shares", title="Stocks Portfolio Composition")
  ```

  ![pie-chart](Images/pie-chart.png)

  ```python
  # Create a bar plot to show the value of shares
  df_value.plot.bar(title="Current Value in Dollars of Stock Portfolio")
  ```

  ![bar-chart](Images/bar-chart.png)

Ask if there are any remaining questions.

---

### 15. Recap (10 min)

Woo-hoo! You've reached the end of APIs Day 2. Over the past two days, the class has been bombarded with an array of APIs, ranging from APIs that allow users to play fun games to APIs that provide users with a unified view of data across all financial accounts. The importance of API keys has been drilled home, as has the need to store them as environment variables.

Recap by asking students to summarize with one word or a three-word phrase what they learned today. Ask for volunteers, and then eventually go round-robin if necessary.

 **Answer:** Disruptive

 **Answer:** Open-source

 **Answer:** Democratization

 **Answer:** Keys, keys, keys

 **Answer:** Decentralization

 **Answer:** For the people

 **Answer:** Data Extraction

 **Answer:** Development kit

Underscore to students that their progress in learning how to programmatically submit API calls using the Python `requests` library and SDKs is going to have real-world benefits. These skills are practical and could be employed to solve a number of FinTech use cases.

* Software development requires applications to support integration with APIs. Cloud (e.g., Amazon Web Services), big data (e.g., Hadoop), and data science (e.g., Data Science Toolkit ) technologies all require some form of API or SDK be used to use their services, platform, and data.

  * For example, in order to write a machine-learning algorithm that gets data from the Amazon cloud, an AWS SDK will be needed.

  * To process social media data in real-time, a streaming service API will be needed. (e.g., Kafka-Python).

Highlight that students have shown themselves to be cutting edge by working with technologies like Alpaca, which are disrupting the FinTech data world.

* In order to be cutting edge, a developer has to keep up with emerging technologies.

* This requires developers to be able to write code that connects and integrates multiple APIs and SDKs to create unique interactions.

Reinforce to students that this is exactly what they did today in class. With the skills they've learned today, they'll be able to keep up with emerging technologies.

Communicate to students that the applications they've completed today should be discussed during interviews and added to their resumes.

* You've created reusable data extraction tools, which are valuable artifacts in the FinTech industry.

* With the right parameterization, the Quandl and Alpaca APIs could easily evolve into engines and frameworks.

Ask if there are any remaining questions before ending the class.

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
