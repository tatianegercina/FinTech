## 5.2 Lesson Plan: API Mania!

---

### Overview

Today's class will expose students to some exciting and innovative FinTech APIs that have truly disrupted the industry. **Quandl** is an API that provides access to historical stock data, while **Plaid** connects multiple financial institutions for a unified view of personal financial information. Both APIs help democratize and decentralize financial data stores and analytic approaches. But that's not all–new APIs and software development kits (SDKs) are released regularly to help enhance and advance the FinTech industry. It's a whole new world, and one to be excited about!

This lesson presents students with hands-on experience using APIs in a Python environment, requesting and leveraging API keys, and securely storing API keys and credentials as **environment variables** (variables that exist at the operating system level). Students will programmatically submit API requests to Quandl using the Python `requests` library and Plaid's software development kit, a library packaged to provide developers with access to Plaid's endpoints and functions.

### Class Objectives

By the end of today's class, students will be able to:

* Register for an API key and use it to fetch authenticated requests using the `requests` library.

* Set/export environment variables in Windows and Mac, and retrieve them in Python.

* Explain the difference between an API and SDK.

* Set authentication for the Plaid SDK.

* Use a Python SDK to fetch data from Plaid.

* Use SDKs to analyze personal financial data.

* Retrieve historical stock information using the Quandl API.

* Acknowledge the general regulations for FinTech companies in Canada.

### Instructor Notes

* Slack out the [Alpaca Installation Guide](../Supplemental/AlpacaMarkets_Installation-Guide.md) (again) and the [PyViz Installation Guide](../../06-PyViz/Supplemental/PyVizInstallationGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class.

* This lesson includes the demonstration, and use of, two APIs that require users to have accounts and API keys. You, students, and TAs should all have created accounts and received API keys prior to this lesson. (Students were instructed to sign up at the end of Lesson 5.1.) The following links can be used to sign up for accounts and get keys. Slack these links out to TAs and students before the beginning of the lesson, so they have ample time to sign up. There is an activity dedicated to confirming that each student has signed up.

  * [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

  * [Plaid](https://dashboard.plaid.com/signup)

* Since this lesson works with API keys, you and the students must not hardcode or print any API keys, or request URLs with keys. All keys must be stored in environment variables and then referred to with an `os.getenv` function call in Python.

* This lesson is dependent upon the Quandl and Plaid APIs being up and running. Visit each site and execute preemptive API calls to ensure connectivity. It is imperative to confirm that the APIs used in this lesson are executing as expected.

* Some students may have experience working with making API calls. Keep an eye out for these more advanced students so they can potentially assist with review activities; allowing them to help their peers is a great way to keep them engaged and interested in the material.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [5.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=50ef1953-f071-47b8-8bb3-aab10107ea41) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 5.2 Slides](https://docs.google.com/presentation/d/1UasSrvZ-Qp8RoVsA0t54zlNUAg3o3OR-SaKFz8tOsPQ/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Day 2 takes students to the next step in using APIs. Students will transition from using the Python `requests` library to using SDKs that provide practical use cases for FinTech analysis.

Welcome students to the second day of APIs. Open the lesson slides, move to "The Rise of APIs" section, and highlight the following points:

* While today's class will be a continuation of the last session, there will be a stronger emphasis on how to use FinTech APIs effectively.

* There are several FinTech APIs available that grant users the ability to create and execute analytic pipelines on various forms of financial data.

* Because APIs often offer practical services, they may require subscriptions or payment. Companies use API keys and user accounts to ensure billing and secure transmission of financial and other confidential information.

* You will get hands-on experience on using Plaid (a banking API), Quandl (to fetch historical stock data) and Alpaca (a trading API).

Explain to students that the Department of Finance and the Provincial Finance Regulators are responsible for providing a financial regulatory framework for Canada. However, the monetary policy for the Canadian FinTech industry is still under development according to [a report released by the Competition Bureau](https://www.competitionbureau.gc.ca/eic/site/cb-bc.nsf/eng/04322.html).

* Within the general regulatory framework, any company interested in providing technology-led financial services should, at the minimum, comply with [The Personal Information Protection and Electronic Documents Act (PIPEDA)](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) and the [Canada's Anti-Money Laundering and Anti-Terrorist Financing Regime (AML/CT)](https://www.fintrac-canafe.gc.ca/fintrac-canafe/antimltf-eng).

* Companies interested in offering financial services related to cryptocurrencies or tokens should follow the guidance published by the Canadian Securities Administrators (CSA) in the [Staff Notice 46-308 about Securities Law Implications for Offerings of Tokens](https://www.securities-administrators.ca/aboutcsa.aspx?id=1704).

Now, transition into a dry demonstration (just visit the site) of a practical FinTech API that will be used later in the lesson: Plaid.

Navigate to the [Plaid](https://plaid.com/) website and highlight the following:

* The Plaid API allows users to connect multiple bank accounts to one platform and provides a unified view of a person's financial ecosystem. It enables users to manage and analyze their accounts and financial information from one spot.

* Plaid was designed as a tool for developers to accelerate their FinTech development. Developers can use Plaid to provide services to their users and consumers without having to worry about making API calls to each bank or financial entity.

* Because Plaid handles any needs behind-the-scenes with each financial institution, developers can focus on designing and developing a program that will:

  1. Make calls to Plaid.

  2. Analyze data by either extracting financial information from Plaid, or by using Plaid's out-of-the-box capabilities.

* [Plaid is available in Canada since May 2019](https://blog.plaid.com/plaid-in-canada/).

Answer any questions before moving on.

---

### 2. Instructor Do: API Keys (5 min) (Critical)

In this activity, students and the instructor will participate in a facilitated discussion regarding API keys. Students will learn the what, why, and how of API keys.

Guided questions are provided to help facilitate discussion. Use these questions as time permits.

Navigate to the "API Keys" section of lesson slides and introduce students to API keys. Highlight the following:

* Many companies that offer APIs require users to sign up for API keys. **API keys** are access tokens that serve as a form of credential (like a user name or password) that grants users privileges and permissions needed to submit API requests. API keys are unique identifiers used by APIs to recognize which users submitted which requests.

* **API keys** are like the keys to a house or a car. Without a key, one cannot gain access or make use of the services provided by an API. APIs that require keys will reject any request that does not include an API key.

* The main reason why companies use API keys is to monitor and control user requests and receive compensation for their services and intellectual property. Because API keys detail permissions and privileges for users, companies can programmatically disable and enable API privileges based on some requests submitted.

* Obtaining an API key is like getting keys to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please.

Initiate a facilitated discussion by communicating the following guided questions and discussion points. Choose two or three questions to ask, depending on the available time.

* Ask the students: API keys are submitted with all API requests. Does it seem safe to transmit a unique key over the internet with every request? If no, why not?

  * **Answer:** It is not safe. It is because API keys are transmitted over the internet that they are not considered a proper security layer. If someone were to intercept the client-server communications, they'd be able to retrieve a user's API key.

* Ask: If API keys can be intercepted with every submitted request, why use them?

  * **Answer:** API keys are used because they prohibit nonregistered users from making requests. When an API requires a key, a key must be provided for the API to execute. This forces users to register for the API and request an API key, which also allows the owner of the API to monitor that user's usage and charge for services.

* Pose the following question: What type of privileges and permissions could be tied to an API key? (Hint: CRUD.)

  * **Answer:** Create, read, update, delete.

* Ask: Is there anything that can be done to securely transmit an API key so that others cannot gain access to the key? If yes, provide an example of how.

  * **Answer:** API keys can be made secure through encryption. Many companies offering APIs, like Amazon Web Services, provide users with API keys as well as **secret keys**. Secret keys work much like API keys; however, they're typically encrypted so they can be kept private.

* Ask: Any guesses regarding how to submit a request with an API key?

  * **Answer:** Submit the key with the request URL as a parameter.

End the activity by asking the students if they have any further questions.

---

### 3. Instructor Do: Keys to the FinTech Kingdom (5 min)

Over the next couple of activities, students will be working with APIs that require keys for access. Use this time to engage them with API keys facilitated review discussion.

Engage the students with the following review questions:

* Do *all* APIs require API keys?

  **Answer:** No. Only some APIs require keys to be used. Others allow users to submit requests for free (with rate-limits).

* Why require users to have an API key when requests can be sent without APIs?

  **Answer:** API keys allow companies to monitor, analyze, and enforce rate limits.

* What happens when the `?api_key=` tag is used? Is a function executed, or is a parameter passed?

  **Answer:** A parameter is being passed.

* Can more than one user have the same API key?

  **Answer:** No. API keys are unique identifiers. Each key is assigned to one user.

* Do you think API keys are naturally secure?

  **Answer:** No, they are not. API keys are transmitted across the network and are not naturally encrypted. API keys can be encrypted to make them private.

* Is there a problem with sharing an API key?

  **Answer:** Yes. Rate limits are tied to API keys. Sharing an API key would mean sharing the total number of requests allowed with another individual. Sharing keys could also result in someone else charging your account for billable services.

Excite students about FinTech APIs by highlighting the following points.

* Many APIs, like Plaid, are disrupting the financial industry and market. Many APIs have grassroots initiatives, meaning they are creating tools and technologies for people rather than companies and corporations. These efforts echo the open-source movement.

* Even though many APIs require keys, their services are often free. Obtaining an API key is like getting the keys to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please. There are limitations, but services are often still free.

Ask if there are any questions or comments before moving on.

---

### 4. Instructor Do: Creating Environment Variables (10 min) (Critical)

In this activity, students will learn how to create a `.env` file to store their keys as environment variables. This demo will also include exporting environment variables so that the variables can be used in Python and other applications and programs.

**Files:**

* [example.env](Activities/01-Ins_Create_Env_Variables/Unsolved/example.env)

Open the lesson slides, move to the "Environment Variables" section and highlight the following discussion points:

* Exporting an environment variable exposes it to all applications and programs sharing the same parent process (e.g., a terminal or Python kernel). Each application and program inherits the variable, which allows developers to make calls using `os.getenv` to access the data stored in the variable.

* A common way to export environment variables is to create a `.env` file. The `.env` file will define the environment variables that you would like to export within the environment of your local projects. The `.env` approach is faster than exporting the variables individually.

* Because environment variables are at the operating system level, variables can be passed down from parent processes to child processes.

* An environment variable created in Python cannot be accessed by a terminal; in contrast, an environment variable created in a terminal can be accessed by Python.

* You can set environment variables either in Mac or Windows.

Open a plain text editor, such as VSCode or Sublime Text, and create a new blank file. Perform a live demo of creating and exporting environment variables with the `.env` file by highlighting the following:

* Now, we will create a `.env` file to store the API keys as environment variables.

* To set an environment variable, you have to define a name for that variable; let's start creating a variable to store the Quandl API key.

* Set the variable name as `QUANDL_API_KEY` and assign your API key to it.

  ```text
  QUANDL_API_KEY="ENTER YOUR API KEY HERE"
  ```

* Once you set your brand new environment variable, save the file as `.env`. You may receive a warning message that states that the file will be hidden.

  ![create_env_file](Images/create_env_file.gif)

* Once the `.env` file has been created; it must be loaded into memory by a package like `python-dotenv` so that the environment variables can be sourced. We will be discussing methods of loading a `.env` in the next activity.

Ask if there are any questions, and then move on to the next activity.

---

### 5. Instructor Do: Calling Environment Variables (5 min) (Critical)

In this activity, students will learn how to call API keys as environment variables using the `dotenv` Python package.

**Important Note:** Ensure that you have a local `.env` file containing your `QUANDL_API_KEY` into the `Solved` folder before running the demo.

**Files:**

* [env_variables.ipynb](Activities/02-Ins_Call_Env_Variables/Solved/env_variables.ipynb)

Recall students to the concept of environment variables by asking the following question:

* Imagine you signed up for 10 APIs, and each API gave you a key. It'd be challenging to commit each key to memory, so you need to find some way to save the keys. What are some possible approaches?

  **Answer:** One approach would include tracking the keys in an Excel document. The document could be password protected to preserve confidentiality.

  **Answer:** Environment variables could be created, and the keys could be stored in the variables.

Open the solved version of the Jupyter notebook. Next, run the code on every cell and highlight the following:

* Environment variables are variables just like Python variables; however, instead of being created in a Python application, they're created on a user's computer.

* Environment variables are operating-system-level variables that are accessible by all programs and applications with access to that environment.

* Environment variables are given a name, and they can hold any string value. It is important to note that environment variables can only hold `strings`.

* Like with Python variables, data within environment variables can be accessed by making a call to the variable.

* An easy, convenient, and secure way to store any data that needs to be accessed across programs and applications is to use environment variables. This includes API keys, as well as user credentials, and program installation paths (e.g., Python).

* For reading our `.env` file and setting it's defined environment variables in our local environment we import the `load_dotenv()` method from the `python-dotenv` package.

  ```python
  # Import dotenv package for setting environment variables
  from dotenv import load_dotenv
  ```

* For fetching our environment variables from the local environment and loading them into an in-memory python variable, we are importing the `os` package.

  ```python
  # Import os package
  import os
  ```

* Setting the environment variables in our `.env` file is as easy as calling the `load_dotenv()` method.

  ```python
  # Set environment variables from the .env in the local environment
  load_dotenv()
  ```

* Keep in mind unless a file location `string` is passed `load_dotenv` will look for a `.env` in the root directory from which your Python code is executing.

* Once an environment variable is declared, it can be called using the `os.getenv` function. The input to the `os.getenv` function is the name of the environment variable. The output should then be stored as a Python variable to be used at a later time.

  ```python
  # Retrieve API key and store as Python variable
  api_key = os.getenv("QUANDL_API_KEY")
  ```

* A way to check if the environment variable was correctly loaded, is to print the data type of the Python variable.

* If the environment variable exists, Python will return `str` as the data type.

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  type(api_key)
  ```

  ```text
  NoneType
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

Emphasize to students that they need to make sure that the environment variable `print` statement is not pushed into Git, or any other repository, as it would expose their API keys to anyone who has access to the repository.

Ask students if there are any questions before continuing.

---

### 6. Students Do: Under Lock and Key (20 min)

The previous modules focused on the instructor demoing how to create, store, and use API keys with environment variables. Students now engage in a bridge activity that involves retrieving a Quandl API key, and submitting a Quandl API request with the key stored as environment variables. This will be the students' first opportunity for hands-on practice with API keys and environment variables.

Working with environment variables can be a little tricky, especially if they are not declared and exported correctly. Make sure both TAs and you are circulating during this activity to help resolve any technical issues students may face.

If students finish early, use the extra time to review the final two guided review questions from the next activity.

**Files:**

* [env_variables.ipynb](Activities/03-Stu_Under_Lock_And_Key/Unsolved/env_variables.ipynb)

* [example.env](Activities/03-Stu_Under_Lock_And_Key/Solved/example.env)

**Instructions:**

* [README.md](Activities/03-Stu_Under_Lock_And_Key/README.md)

---

### 7. Instructor Do: Under Lock and Key Activity Review (5 min)

**Important Note:** Ensure that you have a local `.env` file containing your `QUANDL_API_KEY` into the `Solved` folder before running the solution.

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

Open the solution and end the review session with a quick-dry walk-through of the solution.

* Once created, the environment variables are then shared with all child processes. For example, when the `load_dotenv()` method is executed, it will ensure the `QUANDL_API_KEY` variable is accessible by all processes running in the environment that executed the python file process.

  ```shell
  QUANDL_API_KEY="ENTER YOUR KEY HERE"
  ```

* Environment variables can be accessed in Python with the `os` library. The library has to be imported before it can be used. The `os` library has an `os.getenv` function that can be used to retrieve environment variables from the operating system. Once retrieved, the value can be saved as a Python variable (e.g., `api_key`).

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  ```

* Once stored as a Python variable, the environment variable value can be used for processing. In this case, the `QUANDL_API_KEY` is stored as Python variable api_key and then concatenated with the request URL. The concatenated request URL will then be used to submit a request to the Quandl API.

  ```python
  # Define the base request URL
  request_url = "https://www.quandl.com/api/v3/datasets/WIKI/MSFT.json?api_key="

  # Concatenate request_url and api_key. Store as new variable
  request_url = request_url + api_key
  ```

If time remains, ask two final, guided questions:

* If a user were to export environment variable `QUANDL_API_KEY` using a terminal but then launched Jupyter Lab in a different terminal window, would Jupyter Lab be able to retrieve the environment variable?

  * **Answer:** No. Environment variables are sourced to current and child processes. Because a new terminal window is used to launch Jupyter Lab, the environment variable `QUANDL_API_KEY` will be out of scope.

* If environment variables are inherited through parent-child processes, what happens when a parent process is terminated?

  * **Answer:** The environment variable is deleted and no longer available for use.

Ask for any remaining questions before moving on.

---

### 8. Instructor Do: Intro to SDKs (5 min) (Critical)

The past lesson has focused on students using the Python `requests` library to submit API requests. Students will now learn how to use proprietary software development kits (SDKs) to submit API calls and streamline development efforts.

Explain to students that while the Python requests library is a great tool with which to submit requests to APIs, there are more sophisticated APIs out there that offer tools called software development kits that provide a packaged way to access API endpoints and submit calls.

Open the lesson slides, and navigate to the "SDKs" section, initiate a facilitated discussion by highlighting the following:

* SDKs offer programmatic ways to access API endpoints without using the `requests` library. Instead of using the `requests` library to execute API calls, users would use functions provided by the SDK. For example, an SDK would provide a GET function similar to the `requests.get` function offered by the Python `requests` library. The SDK might also provide additional attributes and functions for filtering and calculating data.

* Some companies, like Plaid, offer Software Development Kits as a means to submit requests to their APIs.

* In addition to the generic GET and POST functions though, SDKs offer functions that are specific to their services/API. For example, the Plaid SDK lets you execute a function that returns bank transactions.

Pose the following question to facilitate discussion:

* What type of operations can you imagine being offered by SDKs? We already know GET operations are one of them. What are some others?

  * **Answer:** Create, update, and delete operations.

Explain to students that working with SDKs removes the need to build API request URLs. Instead of using request URLs to make parameterized API calls, SDK functions and attributes are used.

  ```
  quandl.get("WIKI/AAPL", rows=5)

  vs.

  requests.get("https://www.quandl.com/api/v3/datasets/WIKI/AMD")
  ```

Ask students the following guided question:

* Why would companies create SDKs when Python provides users with the requests library?

  * **Answer:** By creating SDKs, companies allow users to interact with their APIs more effectively. The requests library only supports so many functions (GET, POST, etc.). However, by providing users with an SDK, companies can give users access to in-house built attributes and functions that can offer more value than the functions in the requests library.

  * **Answer:** When writing a Python script, using a Python SDK can often be cleaner and easier to understand and integrate into one's code. SDKs allow developers to use syntax and language features that often simplify and clean up code. A decent example of this is evidenced when comparing the URL request to Quandl with the `quandl.get("AAPL")` function. Both will extract historical stock; however, the `quandl.get` function is easier to use and looks cleaner.

* Because SDKs provide out-of-the-box functions that can be used with the API, developers do not have to worry about reinventing the wheel. What is an example of a function or operation a FinTech SDK might provide?

  * **Answer:** A FinTech SDK might provide a function that calculates Sharpe ratios, which means users would not need to create this functionality themselves; they'd be able to use the SDK to extract historical stock data and calculate Sharpe ratios. The `requests` library would only support data extraction.

Ask students if there are any questions before moving on.

---

### 9. BREAK (15 min)

---

### 10. Instructor Do: Intro to Plaid (10 min)

Navigate to the "Plaid SDK" section of the lesson slides, and introduce the Plaid SDK by highlighting how it is disrupting the FinTech data industry:

* According to a [Forbes article from February 2019](https://www.forbes.com/sites/donnafuscaldo/2019/02/06/plaid-and-quovo-just-scratching-the-surface-with-data-aggregation/#6e169e401841), FinTech is transforming into a new data industry that focuses on and specializes in the democratization of financial services. This is mainly due the startup **Plaid**, a company seeking to enrich and empower consumers through financial data and technology.

* Whether intentional or not, Plaid is becoming the Magellan of this new FinTech market, circumnavigating the centralized FinTech powers that be and plotting the course for a new, democratized approach to financial services.

* As a FinTech company, Plaid has two customers in mind: the everyday person seeking to take ownership and control over their finances, and the developers trying to design and build robust FinTech applications that enable financial analysis.

* Plaid is tipping the financial scales by breaking down barriers and providing a self-service platform, not for FinTech professionals but FinTech consumers: a platform offering data and analytic needs to promote the decentralization of financial analytics. Plaid bestows upon users the processing power and data access points previously reserved just for financial elites.

* What exactly does Plaid do? Plaid brokers connections to users' bank accounts to create a one-stop-shop experience for financial management. Typically when analyzing data across multiple accounts, one would have to visit each financial institution and extract the desired data. Plaid streamlines this process by offering a platform that will broker the request for data extraction, so users do not have to do it manually. Plaid offers analytics and insights products as well, helping users better understand trends in their data.

* The Plaid API allows users to:

  * Connect multiple bank accounts to the Plaid platform.

  * Get account balances.

  * Extract data from Plaid at the institution and account level.

  * Create an asset report.

Up until now, students have been solely conducting quantitative analysis of investments. Facilitate discussion with the following talking points and guided questions:

* Plaid can be used to analyze financial data in a more comprehensive and holistic view. Plaid takes the data from each financial account and consolidates it to create an overarching portfolio that encompasses savings, investments, retirement funds, loans, etc. What types of analysis can be done with these datasets?

  * **Answer:** Net worth analysis would require data to be extracted from all financial accounts.

* Plaid was created as a tool to assist developers in designing FinTech applications. By brokering connections to financial institutions, Plaid allows developers to focus on designing analytic pipelines for consumers that provide insight and drive financial budgeting decisions. If you had access to your savings, investment, and retirement account data, what would you do with it?

  * **Answer:** Calculate the rate of cumulative returns daily, quarterly, and yearly to show cumulative returns over time. This insight could be used to change the types of funds, bonds, and individualized stocks used in each account.

  * **Answer:** Calculate beta to compare individualized stock and retirement portfolio volatility.

Explain to students that by leveraging the data provided by Plaid, consumers no longer have to rely on financial services professionals or big companies to give them insights into their data. Furthermore, developers no longer have to concern themselves with data acquisition and brokering communication with financial institutions. Instead, both parties can just use Plaid.

Answer any questions before moving on.

---

### 11. Instructor Do: Plaid Demo (15 min)

In this activity, students will receive an instructor-led demo of the Plaid API. The instructor will demonstrate to students how to connect to the Plaid sandbox from a Python environment.

Have the `.env` file prepared with you Plaid API Keys before class so that it does not need to be created during the activity.

**Files:**

* [plaid_demo.ipynb](Activities/04-Ins_Plaid_Demo/Solved/plaid_demo.ipynb)

Emphasize to students that one of the cool things about Plaid is that it provides developers with a sandbox for users to get started running. The sandbox contains account data that can be used to test connectivity to Plaid, as well as test some of Plaid's functionality.

Explain to students that the sandbox is excellent because it gives developers a space to play with Plaid without having to connect to personal bank accounts. This grants developers the ability to focus on what they intend to build rather than how they're going to get their data.

Continue the demo by leading students on the environment preparation by highlighting the following:

* Before start using the Plaid SDK, you should install it in your virtual environment using pip-install.

  ```shell
  pip install plaid-python
  ```

* Once you installed the Plaid SDK, the next step is to prepare your environment variables.

* Plaid uses three types of API keys (**client id**, **public key**, and **sandbox secret key**). Each of these needs to be saved as environment variables in a `.env` file.

* To retrieve your keys, log into the [Plaid Dashboard](https://dashboard.plaid.com/account/keys); on the main menu, click on "Team Settings" and choose the "Keys" option.

  ![retrieve_plaid_keys](Images/retrieve_plaid_keys.png)

* Copy your `client_id`, `public_key`, and sandbox secret.

  ![plaid_keys](Images/plaid_keys.png)

* Create a `.env` file and define the following variables to store your Plaid keys as environment variables.

  ```shell
  PLAID_CLIENT_ID="ENTER YOUR KEY HERE"
  PLAID_PUBLIC_KEY="ENTER YOUR KEY HERE"
  PLAID_SBX_SECRET_KEY="ENTER YOUR KEY HERE"
  ```

Explain to students that now it's time to start using the Plaid SDK from Python. Open the unsolved version of the Jupyter notebook, live code the solution and highlight the following:

* After the Plaid SDK is installed, it can be imported into Python using the `import` command. Also, other libraries needed for this activity are imported, including `os`, `json`, `datetime` and `dotenv`.

  ```python
  # Initial imports
  import plaid
  import os
  import datetime
  import json
  from dotenv import load_dotenv
  ```

* The environment variables from the `.env` must be loaded and set with the `load_dotenv()` method.

  ```python
  load_dotenv()
  ```

  ```text
  True
  ```

* Once the environment variables are available, we can retrieve the Plaid keys to store them as Python variables.

  ```python
  # Extract API keys from environment variables
  PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
  PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY')
  PLAID_SBX_SECRET_KEY = os.getenv('PLAID_SBX_SECRET_KEY')
  ```

* To make a request to the Plaid API, a `client` object needs to be created. This object will serve as the client in the client-server model.

  ```python
  # Create client object
  client = plaid.Client(
      client_id=PLAID_CLIENT_ID,
      secret=PLAID_SBX_SECRET_KEY,
      public_key=PLAID_PUBLIC_KEY,
      environment="sandbox"
  )
  ```

* The `client` object will specify the API keys, as well as the desired Plaid environment. Plaid offers three different environments for developers: sandbox, development, and production. The sandbox and development environments are unrestricted; however, Plaid bills for the use of the production environment.

* We can fetch data from Plaid using the `get()` function. The Plaid sandbox comes preloaded with financial data ready and available for use. Sandbox data includes institution data, account information, transactions, investment records, and more. However, to extract data, there are a few data attributes that are needed first.

* To generate a list of all of the institutions that have been loaded into the sandbox, we can use the `Institutions.get()` function, which accepts the number of institutions to fetch as an argument.

  ![plaid_fetch_institutions](Images/plaid_fetch_institutions.png)

* Knowing the institutions available in the sandbox allows one to extract account data for that institution. To extract account data, Plaid will need to perform another level of authentication. This level of authentication requires the generation and exchange of a **public token** for an **access token**.

* You can create a public token using an `institution_id` from the sandbox (e.g., `ins_112060`). The `client.Sandbox.public_token.create()` function will create and return a public token for `1st Bank (Broadus, MT) - Personal`. The function accepts two arguments: institution and products. Products can be understood as the types of datasets Plaid has available. These include, but are not limited to, transactions, income, and assets.

  ```python
  # Select an institution for processing
  INSTITUTION_ID = "ins_112060"

  # Create public token to be exchanged for institution access token
  create_tkn_response = client.Sandbox.public_token.create(
      INSTITUTION_ID,
      ['transactions','income','assets']
  )

  # Exchange public token for access token
  exchange_response = client.Item.public_token.exchange(create_tkn_response['public_token'])

  # Store access token as variable
  access_token = exchange_response['access_token']
  ```

* Public tokens can be exchanged for access tokens. Access tokens are needed to be able to access account details such as transactions. The exchange serves as an additional round of security. The `client.Item.public_token.exchange()` function handles the exchange and returns an access token, item id, and request-id. The `client.Item.public_token.exchange()` function accepts one argument: the `public_token` returned in `create_tkn_response`.

  ![token_exchange.png](Images/token_exchange.png)

* The exchange response will contain the access token needed to get data from the `item` object.

  ```python
  # Store access token as variable
  access_token = exchange_response['access_token']
  ```

* Once the access token is in hand, you can start using Plaid to its fullest potential. You'll have access to a bunch of different accounts and transactions, all available for use. All that is needed is that access token.

* Fetch all accounts at an institution

  ![get_accounts.png](Images/get_accounts.png)

* You can fetch transactions for a date range. Python date objects can be used to specify start and end dates.

  ![get_transactions.png](Images/get_transactions.png)

Take some time to emphasize what it means to have this type of data provided by Plaid. Use FinTech use cases to help ground the discussion.

* Imagine wanting to create some type of monitoring tool that flags transactions based on specific rules (e.g., time of day, amount, time since the last transaction). Banks provide some of this functionality with their mobile apps, but rarely do they ever allow users to create custom rules. A developer could create an app that does just this, and he or she could use Plaid as their foundation. The sandbox data in Plaid could be used to begin development and testing. Furthermore, once the app is ready for production, Plaid can be the mechanism that consumers use to connect their accounts.

* Imagine wanting to create a digital dashboard for personal spending. Plaid is what can make this happen, providing the outlet for connecting to personal accounts, as well as a means to consolidate and extract data for aggregation. This means that as developers, we can provide our consumers with the look, feel, and functionality that we want: a digital financial dashboard for the people, by the people.

If time remains, ask students for any thoughts and answer any questions before moving on.

---

### 12. Students Do: Sporting Plaid—Part 1 (20 min)

This activity is the first part of a two-part mini-project activity. Students will create environment variables for Plaid API keys and install the Plaid SDK, which will be used in the next activity to extract transaction data.

Instruct TAs to confirm that each student has Plaid API keys and can authenticate with Plaid. Circulate through the room to help troubleshoot any challenges related to environment variables and API keys.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment.

**Files:**

* [example.env](Activities/05-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/example.env)

* [sporting_plaid.ipynb](Activities/05-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Sporting_Plaid_Pt_1/README.md)

---

### 13. Instructor Do: Emotional Break (10 min)

Facilitate discussion by asking students about their experiences working with API keys and SDKs.

Ask students about the pace of the class. Is it going too fast, too slow, or just right?

Empower students to continue by emphasizing that they're one step away from adding Plaid to their toolkit. Reiterate that Plaid is going to help them acquire the data they need to perform financial analysis, and it will broker the communication channel between banks and FinTech application servers.

Remind students that they are making excellent progress. Not only are they submitting requests to an API, they're programmatically sending authenticated requests using SDKs.

If time remains, ask the following questions:

* What data type can environment variables be stored as?

  * **Answer:** String

* Why is Plaid considered a FinTech disrupter?

  * **Answer:** Plaid is changing the way developers and consumers can get access to FinTech data. Not only is Plaid providing a technology platform to get access to FinTech data, but it is also providing analytic and insight products to help consumers understand their data and make data-driven decisions.

* How glad are you that SDKs don't require users to build long, parameterized request URLs like the Python `requests` library?

  * **Answer:** It's better to use an SDK since it eases the process of fetching data and reduces the chance of errors due to misspelling URLs or parameters used in the `requests` library.

Ask students if they have any questions before moving on.

---

### 14. Students Do: Sporting Plaid—Part 2 (25 min)

It's time the students donned some Plaid again, as they will be extracting financial data from the Plaid sandbox. To complete this assignment, students will submit requests to the Plaid API and parse JSON output.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment. If a student or team finishes early, ask if they'd be willing to conduct a dry walk-through of the solution and explain what steps were taken and why.

Circulate through the room and assist while students are working. Students may run into difficulty parsing through multiple JSON indexes.

**Files:**

* [example.env](Activities/06-Stu_Sporting_Plaid_Pt_2/Unsolved/example.env)

* [sporting_plaid.ipynb](Activities/06-Stu_Sporting_Plaid_Pt_2/Unsolved/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/06-Stu_Sporting_Plaid_Pt_2/README.md)

---

### 15. Instructor Do: Sporting Plaid Activity Review (15 min)

**Files:**

* [sporting_plaid.ipynb](Activities/06-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb)

Students will just have completed a lengthy activity of installing and using the Plaid SDK to extract financial data. End the class with a reflection exercise to reinforce the conceptual information learned.

Give students 2 minutes to pick one data element from the Plaid transaction data that they'd like to analyze. Call on each student in a round-robin fashion and ask them to volunteer a data point of interest. Allow the students to suggest different types of analysis they'd like to do with Plaid's data.

* **Answer:** Example data elements include the amount of interest payments, number of restaurant purchases, number of travel purchases across time, etc.

Ask students to create a summarized list of the steps needed to securely and adequately export environment variables. Ask if there is anyone who would like to volunteer an answer; if not, ask students to call the steps out in unison.

* **Answer:** Steps for securely and adequately exporting environment variables include:

  1. Creating a `.env` file.

  2. Import the `dotenv` package.

  3. Loading the `.env` file with `load_dotenv()` to set the environment variable.

Engage students by asking what they see for the future of FinTech when companies like Plaid.

* Are these companies striving to democratize financial data and analytics, including trends, consequences, and paradoxical effects?

  * **Answer:** More peer-to-peer payment services driven by Plaid and crypto alt coins.

  * **Answer:** Data generators and synthetic financial data will no longer be needed.

  * **Answer:** Daily financial monitoring will focus on a unified view of all accounts rather than a microcosmic deep-dive into one account.

  * **Answer:** Plaid will become the one-stop-shop for all financial data needs. This includes daily monitoring and ad-hoc reporting. Instead of checking in with a bank app for one's current account balance or a most recent transaction, Plaid will be used.

  * **Answer:** Instead of democratizing FinTech, Plaid could become the new centralized entity for FinTech data and decision-making. This could lead to reduced rate limits and more expensive premiums.

  * **Answer:** Hackers will be given the tools to attack less sophisticated FinTech applications using Plaid.

If a student or team of students were chosen to conduct a review, instruct them to perform a dry walk-through using the solution. Otherwise, use the solution to complete the dry walk-through yourself.

* The Plaid SDK functions offer a great way to submit requests without having to create and customize or concatenate request URLs.

* Plaid has a Client object that is used to communicate with the Plaid servers. This object stores the **client id**, **secret**, and **public** keys, and it is used to execute each API request.

  ![client_obj_arguments.png](Images/client_obj_arguments.png)

* Plaid offers two types of tokens: **public** and **access**. Public tokens are public and not very secure. Access tokens are secure and are used when authenticating with bank accounts.

  ![plaid_tokens.png](Images/plaid_tokens.png)

* SDK functions replace the need for request URLs. Instead of creating a URL, a simple call is made to the API.

  ```python
  # Extract Transactions with date range
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-365))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
  transactions_response = client.Transactions.get(access_token, start_date, end_date)
  ```

  ![sdk_functions.png](Images/sdk_functions.png)

* JSON data returned from SDK calls are in the same format as response data from request URLs. Key/value pairs access to data elements.

  ![parse_json.png](Images/parse_json.png)

Explain to students that working with Plaid does not mean just working within the sandbox. They could go home and begin analyzing their financial data across multiple accounts as soon as tonight!

Ask if there are any remaining questions.

---

### 16. Recap (10 min)

Woo-hoo! You've reached the end of APIs Day 2. Over the past two days, the class has been bombarded with an array of APIs, ranging from APIs that allow users to play fun games to APIs that provide users with a unified view of data across all financial accounts. The importance of API keys has been drilled home, as needs to store them as environment variables.

Recap by asking students to summarize with one word or a three-word phrase what they learned today. Ask for volunteers, and then eventually go round-robin if necessary.

* **Answer:** Disruptive

* **Answer:** Open-source

* **Answer:** Democratization

* **Answer:** Keys, keys, keys

* **Answer:** Decentralization

* **Answer:** For the people

* **Answer:** Data Extraction

* **Answer:** Development kit

Underscore to students that they are progressing in learning how to programmatically submit API calls using the Python `requests` library and SDKs is going to have real-world benefits. These skills are practical and could be employed to solve several FinTech use cases.

* Software development requires applications to support integration with APIs. Cloud (e.g., Amazon Web Services), big data (e.g., Hadoop), and data science (e.g., Data Science Toolkit ) technologies all require some form of API or SDK be used to use their services, platform, and data.

  * For example, to write a machine-learning algorithm that gets data from the Amazon cloud, an AWS SDK will be needed.

  * To process social media data in real-time, a streaming service API will be needed. (e.g., Kafka-Python).

Highlight that students have shown themselves to be cutting edge by working with technologies like Plaid, which are disrupting the FinTech data world.

* To be cutting edge, a developer has to keep up with emerging technologies.

* This requires developers to be able to write code that connects and integrates multiple APIs and SDKs to create unique interactions.

Reinforce to students that this is exactly what they did today in class. With the skills they've learned today, they'll be able to keep up with emerging technologies.

Communicate to students that the applications they've completed today should be discussed during interviews and added to their resumes.

* You've created reusable data extraction tools, which are valuable artifacts in the FinTech industry.

* With the right parameterization, the Quandl and Plaid APIs could quickly evolve into engines and frameworks.

Answer any questions before ending the class.

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
