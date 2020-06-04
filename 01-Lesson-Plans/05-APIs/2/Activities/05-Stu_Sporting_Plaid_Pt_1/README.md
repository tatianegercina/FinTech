# Sporting Plaid (Part 1)

**Plaid** is disrupting the FinTech industry, liberating developers and consumers alike from the oppressive centralization of financial data and analytic approaches. Plaid is offering free API keys to anyone interested in joining their ranks and revolutionizing the FinTech market. A key grants you access to their Sandbox sanctuary, and it allows you to wield their technology to build your financial applications.

Rally your troops and join Plaid's cause by signing up for their API keys. Sport their colours and chant their anthem.

## Instructions

1. Obtain your key from the [Plaid API Key Site](https://dashboard.plaid.com/account/keys).

2. Create a `.env` file based on the `example.env` starter file to create and export environment variables for **Client ID**, **Public Key**, and **Sandbox Secret Key**.

3. Use the `pip install` command to install the `plaid-python` SDK if you haven't installed it yet in your virtual environment.

4. Open the Jupyter notebook starter file and import `plaid`, `os,` `datetime`, and `json`, and `dotenv` libraries.

5. Read and set the environment variables defined in your `.env` using the `load_dotenv` method.

6. Use the `os.getenv` function to bring the Plaid API key variables into Python. Store these values in Python variables.

### Challenge

Confirm that the environment variables were imported into Python correctly by checking the type or length of the Python variables where you stored the keys.

### Hint

Avoid printing variables that store keys. You don't want to push your secret key into GitHub!

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
