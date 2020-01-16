# Sporting Plaid (Part 2)

You've joined the **Plaid** ranks and have refused to bend the knee to the privatization of financial data and financial services. Now that you've equipped your Plaid API keys disrupt the FinTech market even more by designing a prototype that monitors credit card interest payments and provides consumers with an on-demand list of all interest payments within the past 365 days.

## Instructions

1. Open the JupyterLab [starter file](Unsolved/sporting_plaid.ipynb), and create a Plaid `Client` object using the `plaid.Client` constructor.

2. Pass values for arguments `client_id`, `secret`, and `public key` to the `Client` object using the previously created environment variables.

3. Set `Client` object `environment` argument to equal `sandbox`.

4. Use **institution id** `ins_109512` and the `client.Sandbox.public_token.create` function to create a **public token**. Return the following products: **transactions**, **income**, and **assets**.

5. Use the `public_token` and the `client.Item.public_token.exchange` function to acquire an **access token**. Hint: `public_token` can be retrieved by calling the response key "public_token" (i.e. create_response['public_token']).

6. Parse the JSON output, and store the access token as a Python variable.

7. Extract the list of transactions for all accounts using the `client.Transactions.get` function for the past 365 days.

8. Parse JSON output for the amounts of all transactions with the name `INTRST PYMNT` for the past 365 days.

### Challenge

The first group to finish can volunteer to conduct a dry walk-through of the solution for the class in the next activity.

### Hint

When parsing Plaid transactions, use a `for` loop to iterate over the `transactions_response['transactions']` object.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
