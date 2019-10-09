# Sporting Plaid (Part 1)

**Plaid** is disrupting the FinTech industry, liberating developers and consumers alike from the oppressive centralization of financial data and analytic approaches. Plaid is offering free API keys to anyone interested in joining their ranks and revolutionizing the FinTech market. A key grants you access to their Sandbox sanctuary, and it allows you to wield their technology to build your own financial applications.

Rally your troops and join Plaid's cause by signing up for their API keys. Sport their colors and chant their anthem.

## Instructions

1. Obtain your key from the [Plaid API Key Site](https://dashboard.plaid.com/account/keys).

2. Use the [keys.sh](Unsolved/Core/keys.sh) starter file to create and export environment variables for **Client ID**, **Public Key**, and **Sandbox Secret Key**.

3. Open the terminal, and use the `source` command to source the `keys.sh` file.

4. Use the `pip install` command to install the `plaid-python` SDK.

5. Open the JupyterLab [starter file](Unsolved/Core/sporting_plaid.ipynb), and import `plaid`, `os,` `datetime`, and `json` libraries.

6. Use the `os.getenv` function to bring the Plaid API key variables into Python. Store these values in Python variables.

### Challenge

Confirm that the environment variables were imported into Python correctly by checking the type or length of the Python variables the keys are stored in.

### Hint

Avoid printing variables that store keys. You don't want to push your secret key into GitHub!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
