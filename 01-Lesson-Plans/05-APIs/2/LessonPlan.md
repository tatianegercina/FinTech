## 5.2 Lesson Plan: API Mania!

---

### Overview

Today's class will focus on exposing students to the exciting and innovative FinTech APIs that have been disrupting the industry. There are so many groundbreaking APIs in the FinTech industry that it's almost impossible not to get excited about them. APIs used in this lesson include **Quandl**, an API that provides access to historical stock data, and **Plaid**, an API that brokers connections between multiple financial institution to create a unified view of personal, financial information and accelerate the extraction of data from multiple financial accounts. Both of these services help democratize and decentralize financial data stores and analytic approaches. And this just the beginning. New APIs and SDKs (software development kits) are released regularly, which means there's always new technologies to use to enhance and advance the FinTech industry. It's a new world, and it's a world to be excited about!

This lesson presents students with hands-on experience using APIs in a Python environment, requesting and leveraging API keys, and securely storing API keys and credentials as **environment variables** (variables that exist at the operating system level). Students will programmatically submit API requests to Quandl using the Python `requests` library and Plaid's software development kit, a library packaged to provide developers with access to Plaid's endpoints and functions.

### Class Objectives

By the end of class, students will be able to:

* Register for an API key and use the key to fetch authenticated requests using the Requests Library.

* Set/Export environment variables in Windows and Mac and retrieve them in Python.

* Explain the difference between an API and SDK.

* Set authentication for the Plaid SDK.

* Use a Python SDK to fetch data from Plaid.

* Use SDKs to analyze personal financial data.

### Instructor Notes

* Slack out the [IEXFinance Installation Guide](../Supplemental/IEXFinance_Installation_Guide.md) (again) and the [PyViz Installation Guide](../../06-PyViz/Supplemental/PyVizInstallationGuide.md). Tell students to complete the installation and verify it with a TA before the end of the next class.

* This lesson includes the demonstration and use of two APIs that require users to have accounts and API keys. You, students, and TAs will all need to have created and accounts and received API keys prior to this lesson. The following links can be used to sign up for accounts and get keys. Slack these links out to TAs and students before the beginning of the lesson so they have ample time to sign up. Students were instructed to sign up at the end of 5.1. There will be an activity dedicated to confirming that each student has signed up.

  * [Quandl](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

  * [Plaid](https://dashboard.plaid.com/signup)

* Since this lesson will work with API keys, it is important that you and students do not hardcode or print any API keys or request URLs with keys. All keys must be stored in environment variables and then referred to with an `os.getenv` function call in Python.

* This lesson has a dependency on the Quandl and Plaid APIs being up and running. Visit each site and execute preemptive API calls to ensure connectivity. It is imperative to confirm that the APIs used in this lesson are executing as expected.

* Some students may have experience working with making API calls. Keep an eye out for any students who might be advanced with APIs and could help with review activities. Allowing advanced students to conduct reviews and help their peers is a great way to keep them engaged and interested in the material.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [5.2 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=50ef1953-f071-47b8-8bb3-aab10107ea41) Note that this video may not reflect the most recent lesson plan.

---

### 1. Instructor Do: Welcome Class (5 min)

Day 2 takes students to the next step in using APIs. Students will transition from using the Python `requests` library to using SDKs that provide practical use cases for FinTech analysis.

**Files:**

* [welcome-slides](https://docs.google.com/presentation/d/1l0JmnichhnQ4RkI5Boe-zrEE5uuCehC2YTqxlTAudsA/edit?usp=sharing)

Welcome students to the second day of APIs by highlighting the following talking points:

* Communicate that today's lesson will be a continuation of the last session; however, there will be more emphasis and focus on using FinTech APIs in a practical manner.

* Underscore that practical APIs work just like the fun APIs (e.g., Python Blackjack). A client submits a request, and a server responds. Ask the students a quick refresher question:

    **Question:** What is the name or conceptual phrase for this interaction or relationship between a client and an API.

    **Answer:** Client-server model.

* There are a number of FinTech APIs available that grant users the ability to create and execute analytic pipelines on various forms of financial data.

* Because APIs often offer practical services, they may require subscriptions or payment. Companies use API keys and user accounts to ensure billing and secure transmission of financial and other confidential information.

Transition into a dry demonstration (just visit the site) of a practical FinTech API that will be used later in the lesson: Plaid.

* Navigate to the [Plaid](https://plaid.com/) website.

* Explain that Plaid is an API that allows users to connect multiple bank accounts to one platform and provides a unified view of a person's financial ecosystem. This allows users to manage and analyze their accounts and financial information from one spot.

* Communicate that Plaid was designed as a tool for developers to accelerate their FinTech development. Developers can use Plaid to provide services to their users and consumers without having to worry about making API calls to each individual bank or financial entity.

* Because Plaid handles the behind-the-scenes handshakes with each financial institution, developers are able to focus on designing and developing a program that will:

  1. Make calls to Plaid.

  2. Analyze data by either extracting financial information from Plaid or by using Plaid's out-of-the-box capabilities.

  ![plaid_services.png](Images/plaid_services.png)

---

### 2. Instructor Do: API Keys (5 min) (Critical)

In this activity, students and instructor will participate in a facilitated discussion regarding API keys. Students will learn the what, why, and how of API keys.

Guided questions are provided to help facilitate discussion. Use these questions as time permits.

Navigate to the `API Keys` section of the 5.2 slides and introduce students to API keys.

* Many companies that offer APIs require users to sign up for API keys. **API keys are access tokens that serve as a form of credential (like a user name or password) that grants users privileges and permissions needed to submit API requests. API keys are unique identifiers used by APIs to recognize which users submitted which requests.

* **API keys are like the keys to a house or a car. Without a key, one cannot gain access or make use of the services provided by an API. APIs that require keys will reject any request that does not include an API key.

  ![API Key](Images/api-key.png)

* Explain the main reason why companies use API keys is to monitor and control user requests and receive compensation for their services and intellectual property. Because API keys detail permissions and privileges for users, companies can programmatically disable and enable API privileges based on  number of requests submitted.

Initiate a facilitated discussion by communicating the following guided questions and discussion points. Choose two or three questions to ask, depending on available time.

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

### 3. Instructor Do: Keys to the FinTech Kingdom (10 min)

Over the next couple activities, students will be working with APIs that require keys for access. Use this time to engage them with an API keys facilitated review discussion.

Engage the students with the following review questions:

* Do *all* APIs require API keys?

  **Answer:** No. Only some APIs require keys to be used. Others allow users to submit requests for free (with rate limits).

* Why require users to have an API key when requests can be sent without APIs?

  **Answer:** API keys allow companies monitor, analyze, and enforce rate limits.

* What happens when the `?api_key=` tag is used? Is a function executed or is a parameter passed.

  **Answer:** A parameter is being passed.

* Can more than one user have the same API key?

  **Answer:** No. API keys are unique identifiers. Each key is assigned to one user.

* Do you think API keys are naturally secure?

  **Answer:** No, they are not. API keys are transmitted across network and are not naturally encrypted. API keys can be encrypted to make them private.

* Is there a problem with sharing an API key?

  **Answer:** Yes. Rate limits are tied to API keys. Sharing an API key would mean sharing the total number of requests allowed with another individual. Sharing keys could also result in someone else charging your account for billable services.

Excite students about FinTech APIs by highlighting the following points.

* Communicate that many APIs, like Plaid, are disrupting the financial industry and market. Many APIs have grassroots initiatives, meaning they are creating tools and technologies for people rather than companies and corporations. These efforts echo the open-source movement.

* Reiterate that even though many APIs require keys, their services are often free. Obtaining an API key is like getting the keys to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please. There are limitations, but services are often still free.

Ask if there are any questions or comments before moving on.

---

### 4. Instructor Do: Creating Environment Variables (5 min) (Critical)

In the previous activity, students confirmed that they have their API keys. In this activity, they will learn how to create a `keys.sh` file to store their keys as environment variables. This demo will also include exporting environment variables so that the variables can be used in Python and in other applications and programs.

**Files:**

* [keys.sh](Activities/01-Ins_Create_Env_Variables/Unsolved/keys.sh)

Open the 5.2 slides, and highlight the following discussion points:

* Exporting an environment variable exposes it to all applications and programs sharing the same parent process (e.g., a terminal or Python kernel). Each application and program inherits the variable, which allows developers to make calls using `os.getenv` to access the data stored in the variable.

* The best way to export environment variables is to create a `keys.sh` file. The `keys.sh` shell script will contain commands that will create and export environment variables. The `keys.sh` approach is faster than exporting the variables individually.

Open the [starter file](Activities/01-Ins_Create_Env_Variables/Unsolved/keys.sh), and perform a live demo of creating and exporting environment variables with the `keys.sh` file.

* Enter the following command into `keys.sh` file.

  ```shell
  export QUANDL_API_KEY="ENTER YOUR API KEY HERE"
  ```

* Once the `keys.sh` file has been created, it has to be executed. Execution can occur manually or it can be scheduled. Navigate to where `keys.sh` is saved, and execute the following shell command:

  ```shell
  . ./keys.sh
  ```

* Execute an `echo` command to output the value of variable to the screen.

  ```shell
  echo $QUANDL_API_KEY
  ```

Ask if there are any questions, and then move on to the next activity.

---

### 5. Instructor Do: Calling Environment Variables (5 min) (Critical)

This activity involves students learning, by way of an instructor live demo, how to store API keys in environment variables, as well as how to call and use the environment variables in Python code. Teaching students how to store API keys as environment variables will help ensure that API keys are not hard-coded in Python scripts.

**Files:**

* [env_variables.ipynb](Activities/02-Ins_Call_Env_Variables/Solved/env_variables.ipynb)

Introduce students to the concept of environment variables by asking the following question:

* Imagine you signed up for 10 APIs, and each API gave you a key. It'd be extremely difficult to commit each key to memory, so you need to find some way to save the keys. What are some possible approaches?

  **Answer:** One approach would include tracking the keys in an Excel document. The document could be password protected to preserve confidentiality.

  **Answer:** Variables could be created, and the keys could be stored in the variables.

Navigate to the 5.2 slides, and touch point on each of the below discussion points.

* Environment variables are variables just like Python variables; however, instead of being created in a Python application, they're created on a user's computer. environment variables are operating-system level variables that are accessible by all programs and applications.

* Environment variables are given a name, and they can hold any string value. It is important to note that environment variables can only hold strings.

* Like with Python variables, data within environment variables can be accessed by making a call to the variable.

* An easy, convenient, and secure way to store any data that needs to be accessed across programs and applications is to use environment variables. This includes API keys, as well as user credentials, and program installation paths (e.g., Python).

* Once an environment variable is declared, it can be called using the `os.environ.get` function. The input to the `os.environ.get` function is the name of the environment variable. The output should then be stored as a Python variable to be used at a later time.

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  ```

* If an environment variable does not exist, Python will return None as the value. An empty environment variable will cause an API call to fail. If an API doesn't seem to be working right, double check your environment variable using the `type` command. This will indicate if the environment variable is of type None (null) or string  (not null).

  ```python
  api_key = os.getenv("MY_QUANDL_API_KEY")
  type(api_key)
  ```

  ```
  NoneType
  ```

* Emphasize to students that they need to make sure that the environment variable `print` statement is not pushed into Git, or any other repository, as it would expose their API keys to anyone who has access to the repository.

Ask students if there are any questions before continuing.

---

### 6. Students Do: Under Lock and Key (20 min)

The previous modules focused on the instructor demoing how to create, store, and use API keys with environment variables. Students now engage in a bridge activity that involves retrieving a Quandl API key, and submitting a Quandl API request with the key stored as an environment variables. This will be the students' first opportunity for hands-on practice with API keys and environment variables.

Working with environment variables can be a little tricky, especially if they are not declared and exported correctly. Make sure both TAs and you are circulating during this activity to help resolve any technical issues students may face.

If students finish early, use the extra time to review the final two guided review questions from the next activity.

**Files:**

* [env_variables.ipynb](Activities/03-Stu_Under_Lock_And_Key/Unsolved/env_variables.ipynb)

* [keys.sh](Activities/03-Stu_Under_Lock_And_Key/Solved/keys.sh)

**Instructions:**

* [README.md](Activities/03-Stu_Under_Lock_And_Key/README.md)

---

### 7. Instructor Do: Under Lock and Key Activity Review (5 min)

**Files:**

* [keys.sh](Activities/03-Stu_Under_Lock_And_Key/Solved/keys.sh)

* [env_variables.ipynb](Activities/03-Stu_Under_Lock_And_Key/Solved/env_variables.ipynb)

Kick off the activity review session by asking students to summarize the process of creating and using environment variables with APIs. Engage the students with the following questions:

* After acquiring an API key, what's the first thing that should be done?

  **Answer:** The key should be stored as an environment variable using a `keys.sh` file.

* Once an environment variable has been exported, what should happen next?

  **Answer:** The `keys.sh` file should be executed. When executing, the `source` command should be used.

* What should be done after the `keys.sh` file has been executed and sourced**?

  **Answer:** The environment variable should be called in Python using the `os.environ.get` function.

* Is there ever a time where an API key  should be hard-coded within a Python script?

  **Answer:** No. The best practice for keeping API keys secure is to store them in environment variables. This practice should always be used.

Open the [solution](Activities/03-Stu_Under_Lock_And_Key/Solved/env_variables.ipynb), and end the review session with a quick dry walk-through of the solution.

* The `export` command is used to create environment variables. Once created, the environment variables are then shared with all child processes. For example, when the `keys.sh` file is executed, the export command will ensure the `QUANDL_API_KEY` variable is accessible by all processes running in the terminal that executed the `keys.sh` file.

  ```shell
  export QUANDL_API_KEY="ENTER YOUR KEY HERE"
  ```

* Once a `key.sh` file is created, it has to be executed for the `export` commands to execute. Supplying a `source` command before the `key.sh` file will source the variables and load the `keys.sh` file/`export` command.

  ![source_keys.png](Images/source_keys.png)

* Environment variables can be accessed in Python with the os library. The library has to be imported before it can be used. The os library has an `os.getenv` function that can be used to retrieve environment variables from the operating system. Once retrieved, the value can be saved as a Python variable (e.g.,  `api_key`).

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  type(api_key)
  ```

* Once stored as a Python variable, the environment variable value can be used for processing. In this case, the `QUANDL_API_KEY` is stored as Python variable api_key and then concatenated with the request URL. The concatenated request URL will then be used to submit a request to the Quandl API.

  ```python
  request_url = "https://www.quandl.com/api/v3/datasets/WIKI/AMD.json?api_key="

  # Concatenate request_url and api_key. Store as new variable
  request_url_rfd = request_url + api_key
  ```

If time remains, ask two final, guided questions:

* If a user were to export environment variable `QUANDL_API_KEY` using a Git Bash terminal but then launched Jupyter Lab in a different terminal window, would Jupyter Lab be able to retrieve the environment variable?

  **Answer:** No. Environment variables are sourced to current and child processes. Because a new terminal window is used to launch Jupyter Lab, the environment variable `QUANDL_API_KEY` will be out of scope.

* If environment variables are inherited through parent-child processes, what happens when a parent process is terminated?

  **Answer:** The environment variable is deleted and no longer available for use.

Ask for any remaining questions before moving on.

---

### 8. Instructor Do: Intro to SDKs (5 min) (Critical)

The past two lessons have focused on students using the Python requests library to submit API requests. Students will now learn how to use proprietary software development kits (SDKs) to submit API calls and streamline development efforts.

Communicate to students that while the Python requests library is a great tool with which to submit requests to APIs, there are more sophisticated APIs out there that offer tools called software development kits that provide a packaged way to access API endpoints and submit calls.

Navigate to the 5.2 slides for SDKs, and initiate a facilitated discussion by highlighting the following:

* SDKs offer programmatic ways to access API endpoints without using the requests library. Instead of using the requests library to execute API calls, users would use functions provided by the SDK. For example, an SDK would provide a GET function similar to the `requests.get` function offered by the Python requests library. The SDK might also provide additional attributes and functions for filtering and calculating data.

* Example companies that offer SDKs are Quandl, Plaid, Investors Exchange, Google, and AWS.

* Pose the following question to facilitate discussion:

  * What type of operations can you imagine being offered by SDKs? We already know GET operations are one of them. What are some others?

    **Answer:** Create, update, and delete operations.

* Working with SDKs removes the need to build API request URLs. Instead of using request URLs to make parameterized API calls, SDK functions and attributes are used.

  ```
  quandl.get("WIKI/AAPL", rows=5)

  vs.

  requests.get("https://www.quandl.com/api/v3/datasets/WIKI/AMD")
  ```

Ask students the following guided question:

* Why would companies create SDKs when Python provides users with the requests library?

    **Answer:** By creating SDKs, companies allow users to interact with their APIs in a more powerful way. The requests library only supports so many functions (GET, POST, etc.). However, by providing users with an SDK, companies can give users access to in-house built attributes and functions that can provide more value than the functions in the requests library.

    **Answer:** When writing a Python script, using a Python SDK can often be cleaner and easier to understand and integrate in one's code. SDKs allow developers to use syntax and language features that often simplify and clean up code. A decent example of this is evidenced when comparing the URL request to Quandl with the `quandl.get('AAPL')` function. Both will extract historical stock; however, the `quandl.get` function is easier to use and looks cleaner.

* Because SDKs provide out-of-the-box functions that can be used with the API, developers do not have to worry about reinventing the wheel. What is an example of a function or operation a FinTech SDK might provide?

  **Answer:** A FinTech SDK might provide a function that calculates sharpe ratios, which means users would not need to create this functionality themselves; they'd be able to use the SDK to extract historical stock data AND calculate sharpe ratios. The requests library would only support data extraction.

Ask students if there are any questions before moving on.

---

### 9. BREAK (15 min)

---

### 10. Instructor Do: Intro to Plaid (10 min)

Navigate to the `Plaid SDK` section of the 5.2 slides, and introduce the Plaid by highlighting how it is disrupting the FinTech data industry:

* According to a [Forbes](https://www.forbes.com/sites/donnafuscaldo/2019/02/06/plaid-and-quovo-just-scratching-the-surface-with-data-aggregation/#6e169e401841) article from February 2019, FinTech is transforming into a new data industry that focuses on and specializes in the democratization of financial services. This is largely due the startup **Plaid**, a company seeking to enrich and empower consumers through financial data and technology.

* Whether intentional or not, Plaid is becoming the Magellan of this new FinTech market, circumnavigating the centralized FinTech powers that be and plotting the course for a new, democratized approach to financial services.

* As a FinTech company, Plaid has two customers in mind: the everyday person seeking to take ownership and control over their finances, and the developers seeking to design and build robust FinTech applications that enable financial analysis.

* Plaid is tipping the financial scales by breaking down barriers and providing a self-service platform not for FinTech professionals but for FinTech consumers: a platform offering data and analytic needs  to promote the decentralization of financial analytics. Plaid literally bestows upon users the processing power and data access points previously reserved just for financial elites.

* What exactly does Plaid do? Plaid brokers connections to users' bank accounts to create a one-stop shop experience for financial management. Typically when analyzing data across multiple accounts, one would have to visit each financial institution and extract the desired data. Plaid streamlines this process by offering a platform that will broker the request for data extraction so users do not have to manually do it. Plaid also offers analytics and insights products as well, helping users better understand trends in their data.

* Plaid offers the following services:

  * Help users monitor, budget, and gain insights from their personal finances.

  * Help users manage data from multiple accounts (e.g.,  savings, equity, investments, retirement) in one platform.


Up until now, students have been solely conducting quantitative analysis on investments.

  ![plaid_services.png](Images/plaid_services.png)

Facilitate discussion with the following talking points and guided questions:

* Plaid can be used to analyze financial data in a more comprehensive and holistic view. Plaid takes the data from each financial account and consolidates it to create an overarching portfolio that encompasses savings, investments, retirement funds, loans, etc. What types of analysis can be done with these datasets?

  **Answer:** Net worth analysis would require data to be extracted from all financial accounts.

* Plaid was created as a tool to assist developers in designing FinTech applications. By brokering connections to financial institutions, Plaid allows developers to focus on designing analytic pipelines for consumers that provide insight and drive financial budgeting decisions. If you had access to your savings, investment, and retirement account data, what would you do with it?

  **Answer:** Calculate rate of cumulative returns daily, quarterly, and yearly to show cumulative returns over time. This insight could be used to change the types of funds, bonds, and individualized stocks used in each account.

  **Answer:** Calculate beta to compare individualized stock and retirement portfolio volatility.

* By leveraging the data provided by Plaid, consumers no longer have to rely on financial services professionals or big companies to give them insights into their data. Furthermore, developers no longer have to concern themselves with data acquisition and brokering communication with financial institutions. Instead, both parties can just use Plaid.

---

### 11. Instructor Do: Plaid Demo (15 min)

Students will receive an instructor-led demo of the Plaid API. The instructor will demonstrate to students how to connect to the Plaid sandbox from a Python environment.

Have the `keys.sh` file prepared before class so that it does not need to be created during the activity.

**Files:**

* [keys.sh](Activities/04-Ins_Plaid_Demo/Solved/keys.sh)

* [plaid_demo.ipynb](Activities/04-Ins_Plaid_Demo/Solved/plaid_demo.ipynb)

Emphasize to students that one of the really cool things about Plaid is that it provides a developers sandbox for users to get started running. The sandbox contains account data that can be used to test connectivity to Plaid, as well as test some of Plaid's functionality.

* The sandbox is great because it gives developers a space to play with Plaid without having to connect to personal bank accounts. This grants developers the ability to focus on what they intend to build rather than how they're going to get their data.

#### Prepare Environment Variables

Open the [keys.sh starter file](Activities/04-Ins_Plaid_Demo/Solved/keys.sh), and set up your environment variables. If possible, complete this step prior to the lesson.

* Plaid uses three types of API keys (**client id**, **public key**, and **sandbox secret key**). Each of these needs to be saved as environment variables in a `keys.sh` file. Log into [Plaid](https://dashboard.plaid.com/account/keys) to retrieve them.

  ```shell
  export PLAID_CLIENT_ID="ENTER YOUR KEY HERE"
  export PLAID_PUBLIC_KEY="ENTER YOUR KEY HERE"
  export PLAID_SBX_SECRET_KEY="ENTER YOUR KEY HERE"
  ```

* Once complete, the `keys.sh` file will need to be sourced.

  ```shell
  source ./keys.sh
  ```

* Ask students if they have any questions before continuing.

#### Install Plaid Library

Because Plaid is offered as an SDK, the Python requests library doesn't need to be used. The functions provided by the Plaid SDK can be used to broker the same connection as the requests library. Plaid can be installed using the `pip install` command.

* Open a terminal, and execute the following command:

  ```shell
  pip install plaid-python
  ```

* Once Plaid is installed, it can be imported into Jupyter Lab.

#### Execute Plaid Request

Open the Jupyter [starter file](Activities/04-Ins_Plaid_Demo/Solved/plaid_demo.ipynb), and live code the following:

* After the Plaid SDK is installed, it can be imported into Python using the `import` command. Also import other libraries needed for this activity, including `os`, `json`, and `datetime`.

  ```python
  import plaid
  import os
  import datetime
  import json
  ```

* In order to make a request to the Plaid API, a `client` object needs to be created. This object will serve as the client in the client-server model. The `client` object will specify the API keys, as well as the desired Plaid environment. Plaid offers three different environments for developers: sandbox, development, and production. The sandbox and development environments are unrestricted; however, Plaid bills for the use of the production environment.

  ```
  client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')
  ```

* Since the client object requires the Plaid keys, the keys will need to be extracted using the `os.getenv` function. Once these are stored as Python variables, they can be passed to the `client` object.

  ```python
  # Extract API keys from environment variables
  PLAID_CLIENT_ID = os.getenv("client_id")
  PLAID_PUBLIC_KEY = os.getenv("public_key")
  PLAID_SBX_SECRET_KEY = os.getenv("sbx_secret_key")

  # Create client object
  client = Client(client_id=PLAID_CLIENT_ID, secret=PLAID_PUBLIC_KEY, public_key=PLAID_SBX_SECRET_KEY
  , environment='sandbox')
  ```

Explain that data can be extracted from Plaid using the `GET` function. The Plaid sandbox comes preloaded with financial data ready and available for use. Sandbox data includes institution data, account information, transactions, investment records, and more. However, to extract data, there are a few data attributes that are needed first.

* Generate a list all of the institutions that have been loaded into the sandbox. This can be done by using the `Institutions.get` function, which accepts count as an argument.

  ```python
  # Fetch institutions
  client.Institutions.get(2)

  # Select an institution for processing
  INSTITUTION_ID = "ins_109512"
  ```

  ![plaid_institutions.png](Images/plaid_institutions.png)

* Knowing the institutions available in the sandbox allows one to extract account data for that institution. In order to extract account data, Plaid will need to perform another level of authentication. This level of authentication requires the generation and exchange of a **public token** for an **access token**.

  * Create a public token using an institution from the sandbox (e.g.,  ins_109512). The `client.Sandbox.public_token.create` function will create and return a public token for Houndstooth Bank. The function accepts two arguments: institution and products. Products can be understood as the types of datasets Plaid has available. These include, but are not limited to, transactions, income, and assets.

    ```python
    # Create public token to be exchanged for institution access token
    create_tkn_response = client.Sandbox.public_token.create(INSTITUTION_ID, ['transactions','income','assets'])
    ```

* Public tokens can be exchanged for access tokens. Access tokens are needed to be able to access account details such as transactions. The exchange serves as an additional round of security. The `client.Item.public_token.exchange` function handles the exchange and returns an access token, item id, and request id. The `client.Item.public_token.exchange` function accepts one argument: the public_token returned in `create_tkn_response`.

  ```python
  # Exchange public token for access token
  exchange_response = client.Item.public_token.exchange(create_tkn_response['public_token'])
  ```

  ![token_exchange.png](Images/token_exchange.png)

* The exchange response will contain the access token needed to get data from the `item` object.

  ```python
  # Store access token as variable
  access_token = exchange_response['access_token']
  ```

#### Wielding Plaid

Once the access token is in hand, you can really start using Plaid to its fullest potential. You'll have access to a bunch of different accounts and transactions, all available for use. All that is needed is that access token.

* Fetch all accounts at an institution

  ```python
  # Get accounts associated with institution
  client.Accounts.get(access_token)
  ```

  ![get_accounts.png](Images/get_accounts.png)

* Fetch transactions for a date range. Python date objects can be used to specify start and end dates.

  ```python
  # Get transactions for institution for specific date range
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())

  # Get transactions for date range
  transaction_response = client.Transactions.get(access_token,start_date,end_date)

  # Print JSON output
  print(json.dumps(transaction_response['transactions'][:2],indent=4,sort_keys=True))
  ```

  ![get_transactions.png](Images/get_transactions.png)

Take some time to emphasize what it means to have this type of data provided by Plaid. Use FinTech use cases to help ground the discussion.

* Imagine wanting to create some type of monitoring tool that flags transactions based off certain rules (e.g., time of day, amount, time since last transaction). Banks provide some of this functionality with their mobile apps, but rarely do they ever allow users to create custom rules. A developer could create an app that does just this, and he or she could use Plaid as their foundation. The sandbox data in Plaid could be used to begin development and testing. And once the app is ready for production, Plaid can be the mechanism that consumers use to connect their accounts.

* Imagine wanting to create a digital dashboard for personal spending. Plaid is what can make this happen, providing the outlet for connecting to personal accounts, as well as a means to consolidate and extract data for aggregation. This means as developers we can provide our consumers with the look, feel, and functionality that we want: a financial digital dashboard for the people, by the people.

If time remains, ask students for any thoughts or questions.

---

### 12. Students Do: Sporting Plaid—Part 1 (20 min)

This activity is the first part of a two part mini-project activity. Students will create environment variables for Plaid API keys and install the Plaid SDK, which will be used in the next activity to extract transaction data.

Instruct TAs to confirm that each student has Plaid API keys and can authenticate with Plaid. Circulate through the room to help troubleshoot any challenges related to environment variables and API keys.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment.

**Files:**

* [keys.sh](Activities/05-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/keys.sh)

* [sporting_plaid.ipynb](Activities/05-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/05-Stu_Sporting_Plaid_Pt_1/README.md)

---

### 13. Instructor Do: Emotional Break (10 min)

Facilitate discussion by asking students about their experiences working with API keys and SDKs.

* Ask students about the pace of the class. Is it going too fast, too slow, or just right?

* Empower students to continue on by emphasizing that they're one step away from adding Plaid to their toolkit. Reiterate that Plaid is going to help them acquire the data they need to perform financial analysis, and it will broker the communication channel between banks and FinTech application servers.

* Remind students that they are making excellent progress. Not only are they submitting requests to an API, they're submitting authenticated requests in a programmatic way using SDKs.

If time remains, ask the following questions:

* What data type can environment variables be stored as?

  **Answer:** String

* Are environment variables inherited?

  **Answer:** Yes. Parent processes pass environment variables down to child processes. The `export` and `source` commands ensure that child processes inherit the environment variables.

* Why is Plaid considered a FinTech disrupter?

  **Answer:** Plaid is changing the way developers and consumers can get access to FinTech data. Not only is Plaid providing a technology platform to get access to FinTech data, it is also providing analytic and insight products to help consumers understand their data and make data-driven decisions.

* How glad are you that SDKs don't require users to build long, parameterized request URLs like the Python `requests` library?

Ask students if they have any questions before moving on.

---

### 14. Students Do: Sporting Plaid—Part 2 (25 min)

It's time the students donned some Plaid again, as they will be extracting financial data from the Plaid sandbox. In order to complete this assignment, students will submit requests to the Plaid API and parse JSON output.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment. If a student or team finishes early, ask if they'd be willing to conduct a dry walk-through of the solution and explain what steps were taken and why.

Circulate through the room and provide assistance while students are working. Students may run into difficulty parsing through multiple JSON indexes.

**Files:**

* [keys.sh](Activities/06-Stu_Sporting_Plaid_Pt_2/Unsolved/key.sh)

* [sporting_plaid.ipynb](Activities/06-Stu_Sporting_Plaid_Pt_2/Unsolved/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/06-Stu_Sporting_Plaid_Pt_2/README.md)

---

### 15. Instructor Do: Sporting Plaid Activity Review (15 min)

**Files:**

* [sporting_plaid.ipynb](Activities/06-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb)

Students will just have completed a lengthy activity of installing and using the Plaid SDK to extract financial data. End the class with a reflection exercise to reinforce the conceptual information learned.

* Give students 2 minutes to pick one data element from the Plaid transactions data that they'd like to analyze. Call on each student in round-robin fashion and ask them to volunteer a data point of interest. Allow the students to suggest different types of analysis they'd like to do with Plaid's data.

  **Answer:** Example data elements include amount of interest payments, number of restaurant purchases, number of travel purchases across time, etc.

* Ask students to create a summarized list of the steps needed to properly and securely export environment variables. Ask if there is anyone who would like to volunteer an answer; if not, ask students to call the steps out in unison.

  **Answer:** Steps for properly and securely exporting environment variables include:

    1. Creating `keys.sh` file.

    2. Enter `export` command for each environment variable.

    3. Use the `source` command to load environment variables.

* Engage students by asking what they see for the future of FinTech when companies like Plaid are striving to democratize financial data and analytics, including trends, consequences, and paradoxical effects?

  **Answer:** More peer-to-peer payment services driven by Plaid and crypto alt coins.

  **Answer:** Data generators and synthetic financial data will no longer be needed.

  **Answer:** Daily financial monitoring will focus on a unified view of all accounts rather than a microcosmic deep-dive into one account.

  **Answer:** Plaid will become the one-stop-shop for all financial data needs. This includes daily monitoring and ad-hoc reporting. Instead of checking in with a bank app for one's current account balance or most recent transaction, Plaid will be used.

  **Answer:** Instead of democratizing FinTech, Plaid could become the new centralized entity for FinTech data and decision-making. This could lead to reduced rate limits and more expensive premiums.

  **Answer:** Hackers will be given the tools to attack less mature FinTech applications using Plaid.

If a student or team of students were chosen to conduct a review, instruct them to perform a dry walk-through using the [solution](Activities/06-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb). Otherwise, use the [solution](Activities/06-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb) to complete the dry walk-through yourself.

* The Plaid SDK functions offer a great way to submit requests without having to create and customize or concatenate request URLs.

* Plaid has a Client object that is used to communicate with the Plaid servers. This object stores the **client id**, **secret**, and **public** keys, and it is used to execute each API request.

  ```python
  # Create client object
  client = plaid.Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SBX_SECRET_KEY, public_key=PLAID_PUBLIC_KEY, environment='sandbox')
  ```

  ![client_obj_arguments.png](Images/client_obj_arguments.png)

* Plaid offers two types of tokens: **public** and **access**. Public tokens are public and not very secure. Access tokens are secure and are used when authenticating with bank accounts.

  ```python
    # Select an institution for processing
  INSTITUTION_ID = "ins_109512"

  # Create public token to be exchanged for institution access token
  create_tkn_response = client.Sandbox.public_token.create(INSTITUTION_ID, ['transactions','income','assets'])

  # Exchange public token for access token
  exchange_response = client.Item.public_token.exchange(create_tkn_response['public_token'])

  # Store access token as variable
  access_token = exchange_response['access_token']
  ```

  ![plaid_tokens.png](Images/plaid_tokens.png)

* SDK functions replace the need for request URLs. Instead of creating a URL, a simple call is made to the API.

  ```python
  # Extract Transactions with date range
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-365))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
  transactions_response = client.Transactions.get(access_token, start_date, end_date)
  ```

  ![sdk_functions.png](Images/sdk_functions.png)

* JSON data returned from SDK calls are in the same format as response data from request URLs. Data elements are accessed by key/value pairs.

  ```python
  # Iterate and parse JSON response
  for transactions in transactions_response['transactions']:
      if transactions['name'] == 'INTRST PYMNT':
          print(json.dumps(transactions['amount'], indent=4, sort_keys=True))
  ```

  ![parse_json.png](Images/parse_json.png)

Underscore to students that working with Plaid does not mean just working within the sandbox. They could go home and begin analyzing their own financial data across multiple accounts as soon as tonight!

Ask if there are any remaining questions.

---

### 16. Recap (10 min)

Woo-hoo! You've reached the end of APIs Day 2. Over the past two days, the class has been bombarded with an array of APIs, ranging from APIs that allow users to play fun games to APIs that provide users with a unified view of data across all financial accounts. The importance of API keys has been drilled home, as has as the need to store them as environment variables.

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

  * To process social media data in real time, a streaming service API will be needed. (e.g., Kafka-Python).

Highlight that students have shown themselves to be cutting edge by working with technologies like Plaid, which are disrupting the FinTech data world.

* In order to be cutting edge, a developer has to keep up with emerging technologies.

* This requires developers to be able to write code that connects and integrates multiple APIs and SDKs to create unique interactions.

* Reinforce to students that this is exactly what they did today in class. With the skills they've learned today, they'll be able to keep up with emerging technologies.

Communicate to students that the applications they've completed today should be discussed during interviews and added to their resumes.

* They've created reusable data extraction tools, which are valuable artifacts in the FinTech industry.

* With the right parameterization, the Quandl and Plaid APIs could easily evolve into engines and frameworks.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
