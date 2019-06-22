### 12. Instructor Do: Plaid Demo (15 mins)

Students will receive an instructor-led demo of the Plaid API. The instructor will demonstrate to students how to connect to the Plaid sandbox from a Python environment.

Have the `keys.sh` file prepared before class so that it does not need to be created during the activity.

**Files:**

* [keys.sh](Activities/12-Ins_Plaid_Demo/Solved/keys.sh)

* [plaid_demo.ipynb](Activities/12-Ins_Plaid_Demo/Solved/plaid_demo.ipynb)

Emphasize to students that one of the really cool things about **Plaid** is that it provides a developers **sandbox** for users to get started running with. The **sandbox** contains account data that can be used to test out connectivity to Plaid, as well as test out some of Plaid's functionality.

* The **sandbox** is great because it gives developers a space to play with **Plaid** without having to connect to personal bank accounts. This grants developers the ability to focus on what they intend to build rather than how they're going to get their data.

#### Prepare environment variables

Open the [keys.sh starter file](Activities/12-Ins_Plaid_Demo/Solved/keys.sh), and set up your environment variables. If possible, complete this step prior to class.

* **Plaid** uses three types of API keys (**client id**, **public key**, and **sandbox secret key**). Each of these need to be saved as environment variables in a `keys.sh` file. Log into [Plaid](https://dashboard.plaid.com/account/keys) to retrieve them.

  ```shell
  export client_id="5d0a5ac0d5fa000013be98df"
  export public_key="ce06372ecdf57655eef8a1acf3cf2a"
  export sbx_secret_key ="e47940ef0912660ded9f636d9c3b16"
  ```

* Once complete, the `keys.sh` file will need to be sourced.

  ```shell
  source ./keys.sh
  ```

* Ask students if they have any questions before continuing.

#### Install Plaid Library

Because **Plaid** is offered as an SDK, the Python **requests** library doesn't need to be used. The functions provided by the **Plaid** SDK can be used to broker the same connection as the **requests** library. **Plaid** can be installed using the `pip install` command.

* Open a terminal, and execute the following command:

  ```shell
  pip install plaid-python
  ```

* Once **Plaid** is installed, it can be imported into Jupyter Lab.

#### Execute Plaid Request

Open the Jupyter [starter file](Activities/12-Ins_Plaid_Demo/Solved/plaid_demo.ipynb), and live code the following:

* After the **Plaid** SDK is installed, it can be imported into Python using the `import` command. Also import other libraries needed for this activity, including `os`, `json`, and `datetime`.

  ```python
  import plaid
  import os
  import datetime
  import json
  ```

* In order to make a request to the **Plaid** API, a `client` object needs to be created. This object will serve as the **client** in the **client/server model**. The `client` object will specify the API keys, as well as the desired **Plaid** environment. **Plaid** offers three different environments for developers: sandbox, development, and production. The **sandbox** and **development** environments are unrestricted; however, **Plaid** bills for the use of the production environment.

  ```
  client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')
  ```

* Since the client object requires the **Plaid** keys, the keys will need to be extracted using the `os.environ.get` function. Once these are stored as Python variables, they can be passed to the `client` object.

  ```python
  # Extract API keys from environment variables
  PLAID_CLIENT_ID = os.environ.get("client_id")
  PLAID_PUBLIC_KEY = os.environ.get("public_key")
  PLAID_SBX_SECRET_KEY = os.environ.get("sbx_secret_key")

  # Create client object
  client = Client(client_id=PLAID_CLIENT_ID, secret=PLAID_PUBLIC_KEY, public_key=PLAID_SBX_SECRET_KEY
  , environment='sandbox')
  ```

Explain that data can be extracted from **Plaid** using the `GET` function. The **Plaid** **sandbox** comes pre-loaded with financial data ready and available for use. **Sandbox** data includes institution data, account information, transactions, investment records, and more. However, in order to extract data, there are a few data attributes that are needed first.

* Generate a list all of the institutions that have been loaded into the sandbox. This can be done by using the `Institutions.get` function, which accepts **count** as an argument.

  ```python
  # Fetch institutions
  client.Institutions.get(2)

  # Select an institution for processing
  INSTITUTION_ID = "ins_109512"
  ```

* Knowing the institutions available in the **sandbox** allows one to extract account data for that institution. In order to extract account data, **Plaid** will need to perform another level of authentication. This level of authentication requires the generation and exchange of a **public token** for an **access token**.

  * Create a public token using an institution from the sandbox (i.e. ins_109512). The `client.Sandbox.public_token.create` function will create and return a **public token** for **Houndstooth Bank**. The function accepts two arguments: **institution** and **products**. **Products** can be understood as the types of datasets **Plaid** has available. These include, but are not limited to, transactions, income, and assets.

    ```python
    # Create public token to be exchanged for institution access token
    create_tkn_response = client.Sandbox.public_token.create(INSTITUTION_ID, ['transactions','income','assets'])
    ```

* **Public tokens** can be exchanged for **access tokens**. **Access tokens** are needed to be able to access account details such as transactions. The exchange serves as an additional round of security. The `client.Item.public_token.exchange` function handles the exchange and returns an **access token**, **item id**, and **request id**. The `client.Item.public_token.exchange` function accepts one argument: the public_token returned in `create_tkn_response`.

  ```python
  # Exchange public token for access token
  exchange_response = client.Item.public_token.exchange(create_response['public_token'])
  ```

* The exchange response will contain the **access token** needed to get data from the `item` object.

  ```python
  # Store access token as variable
  access_token = exchange_response['access_token']
  ```

#### Wielding Plaid

Once the **access token** is at hand, you can really start using **Plaid** to its fullest potential. You'll have access to a bunch of different accounts and transactions, all available for use. All that is needed is that **access token**.

* Fetch all accounts at an institution

  ```python
  # Get accounts associated with institution
  client.Accounts.get(access_token)
  ```

* Fetch transactions for a date range. Python date objects can be used to specify **start** and **end** dates.

  ```python
  # Get transactions for institution for specific date range
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())

  # Get transactions for date range
  transaction_response = client.Transactions.get(access_token,start_date,end_date)

  # Print JSON output
  print(json.dumps(transaction_response['transactions'][:2],indent=4, sort_keys=True))
  ```

Take some time to emphasize what it means to have this type of data provided by **Plaid**. Use FinTech use cases to help ground the discussion.

* Imagine wanting to create some type of monitoring tool that flags transactions based off of certain rules (i.e. time of day, amount, time since last transaction, etc). Banks provide some of this functionality with their mobile apps, but rarely do they ever allow users to create custom rules. A developer could create an app that does just this, and he or should could use **Plaid** as their foundation. The sandbox data in **Plaid** could be used to begin development and testing. And once the app is ready for production, **Plaid** can be the mechanism that consumers use to connect their accounts.

* Imagine wanting to create a digital dashboard for personal spending. **Plaid** is what can make this happen, providing the outlet for connecting to personal accounts, as well as a means to consolidate and extract data for aggregation. This means as developers we can provide our consumers with the look, feel, and functionality that we want: a financial digital dashboard for the people, by the people.

If time remains, ask students for any thoughts or questions.
