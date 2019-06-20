### 9. Instructor Do: Intro to SDKs (5 mins) (Critical)

The past two lessons have focused on students using the Python **requests** library to submit API requests. Students will now learn how to use proprietary **Software Development Kits** (SDKs) to submit API calls and streamline development efforts.

**Files:**

* [Slides]()

Communicate to students that while the Python **requests** library is a great tool to submit requests to APIs, there are more sophisticated APIs out there that offer tools called **Software Development Kits** that provide a packaged way to access API endpoints and submit calls.

Navigate to the 5.2 slides for **SDKs**, and initiate a facilitated discussion by highlighting the following:

* **SDKs** offer programmatic ways to access API endpoints without using the **requests** library. Instead of using the requests library to execute API calls, users would leverage functions provided by the **SDK**. For example, an **SDK** would provide a **GET** function similar to the `requests.get` function offered by the Python requests library. The **SDK** might also provide additional attributes and functions for filtering and calculating data.

* Example companies that offer **SDKs** are **Quandl**, **Plaid**, **Investors Exchange**, **Google**, and **AWS**.

* Pose the following question to facilitate discussion:

  * What type of operations can you imagine being offered by **SDKs**? We already know **GET** operations are one of them. What are some others?

    **Answer** Create, update, and delete operations.

* Working with **SDKs** removes the need to build API **request urls**. Instead of using **request urls** to make parameterized API calls, **SDK** functions and attributes are used.

  ```
  quandl.get("WIKI/AAPL", rows=5)

  vs.

  requests.get("https://www.quandl.com/api/v3/datasets/WIKI/AMD")
  ```

Ask students the following guided question:

* Why would companies create **SDKs** when Python provides users with the **requests** library?

    **Answer** By creating **SDKs**, companies allow users to interact with their APIs in a more powerful way. The **requests** library only supports so many functions (i.e. **GET**, **POST**, etc.). However, by providing users with an **SDK**, companies can give users access to in-house built attributes and functions that can provide more value than the functions in the **requests** library.

* Because **SDKs** provide out-of-the-box functions that can be used with the API, developers do not have to worry about reinventing the wheel. What is an example of a function/operation a FinTech **SDK** might provide?

  **Answer** A FinTech **SDK** might provide a function that calculates **sharpe ratios**, which means users would not need to create this functionality themselves; they'd be able to use the **SDK** to extract historical stock data **AND** calculate **sharpe ratios**. The **requests** library would only support data extraction.

Ask students if there are any questions before moving on.
