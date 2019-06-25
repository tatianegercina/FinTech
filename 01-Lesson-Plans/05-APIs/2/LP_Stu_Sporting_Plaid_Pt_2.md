### 14. Students Do: Sporting Plaid - Part 2 (25 mins)

It's time the students donned some Plaid again, as they will be extracting financial data from the **Plaid** sandbox. In order to complete this assignment, students will submit requests to the **Plaid** API and parse JSON output.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment.

Circulate through the room and provide assistance while students are working. Students may run into difficulty parsing through multiple JSON indexes.

**Files:**

* [keys.sh](Activities/14-Stu_Sporting_Plaid_Pt_2/Unsolved/key.sh)

* [sporting_plaid.ipynb](Activities/14-Stu_Sporting_Plaid_Pt_2/Unsolved/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/14-Stu_Sporting_Plaid_Pt_2/README.md)

- - -

### 15. Instructor Do: Activity Review (15 mins)

**Files:**

* [sporting_plaid.ipynb](Activities/14-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb)

Students will just have completed a lengthy activity of installing and using the **Plaid** SDK to extract financial data. End the class with a reflection exercise to reinforce the conceptual information learned.

* Give students 2 minutes to pick one data element from the **Plaid** **transactions** data that they'd like to analyze. Call on each student in round-robin fashion and ask them to volunteer a data point of interest. Allow the students to suggest different types of analysis they'd like to do with **Plaid's** data.

  **Answer** Example data elements include amount of interest payments, number of restaurant purchases, number of travel purchases across time, etc.

* Ask students to create a summarized list of the steps needed to properly and securely export environment variables. Inquire if there is anyone who would like to volunteer an answer; if not, ask students to call the steps out in unison.

  **Answer** Steps for properly and securely exporting environment variables include

    1. Creating `keys.sh` file.

    2. Enter `export` command for each environment variable

    3. Use the `source` command to load environment variables

* Engage students by asking what they see for the future of FinTech when companies like **Plaid** are striving to democratize financial data and analytics, including trends, consequences, and paradoxical effects?

  **Answer** More peer-to-peer payment services driven by Plaid and crypto alt coins.

  **Answer** Data generators and synthetic financial data will no longer be needed.

  **Answer** Daily financial monitoring will focus on a unified view of all accounts rather than a microcosmic deep-dive into one account.

  **Answer** **Plaid** will become the one-stop-shop for all financial data needs. This includes daily monitoring and ad-hoc reporting. Instead of checking in with a bank app for one's current account balance or most recent transaction, **Plaid** will be used.

  **Answer** Instead of democratizing FinTech, **Plaid** could become the new centralized entity for FinTech data and decision making. This could lead to reduced rate limits and more expensive premiums.

  **Answer** Hackers will be given the tools to attack less mature FinTech applications using **Plaid**.

Open the [solution](Activities/14-Stu_Sporting_Plaid_Pt_2/Solved/sporting_plaid.ipynb), and conduct a dry walkthrough of the solution.

* The **Plaid** API functions offer a great way to submit requests without having to create and customize/concatenate request urls.

* **Plaid** has a **Client** object that is used to communicate with the **Plaid** servers. This object stores the **client id**, **secret**, and **public** keys, and it is used to execute each API request.

  ```python
  # Create client object
  client = plaid.Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SBX_SECRET_KEY, public_key=PLAID_PUBLIC_KEY, environment='sandbox')
  ```

  ![client_obj_arguments.png](Images/client_obj_arguments.png)

* **Plaid** offers two types of tokens: **public** and **access**. Public tokens are public and not very secure. **Access** tokens are secure and are used when authenticating with bank accounts.

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

* **SDK** functions replace the need for request urls. Instead of creating a url, a simple call is made to the API.

  ```python
  # Extract Transactions with date range
  start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-365))
  end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
  transactions_response = client.Transactions.get(access_token, start_date, end_date)
  ```

  ![sdk_functions.png](Images/sdk_functions.png)

* JSON data returned from SDK calls are in the same format as response data from request urls. Data elements are accessed by key/value pairs.

  ```python
  # Iterate and parse JSON response
  for transactions in transactions_response['transactions']:
      if transactions['name'] == 'INTRST PYMNT':
          print(json.dumps(transactions['amount'], indent=4, sort_keys=True))
  ```

  ![parse_json.png](Images/parse_json.png)

Underscore to students that working with Plaid does not mean just working within the Sandbox. They could go home and begin analyzing their own financial data across multiple accounts as early as tonight!

Ask if there are any remaining questions.
