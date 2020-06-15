# Under Lock and Key

You and Harold have developed a Python application that extracts historical stock data from **Quandl** for a given ticker and calculates the Sharpe ratio for that stock. So far, the two of you are the only ones using the program, but now your manager wants you to share the application with the entire team. You know that Quandl allows API calls to be submitted without an API key, but the limit is 50 calls a day. Quandl is diligent in their rate-limiting and keeps services under lock and key.

Since Quandl has cracked down on the number of API calls users can make to the service without an **API Key**, acquire a Quandl API key and save it as an **environment variable**. Create a Python code that retrieves the environment variable and passes the key with the request URL. This will ensure that your team can make more than 50 API calls a day, and Quandl can manage and track rate limits.

## Instructions

### Acquire and Store API key

1. Navigate to the Quandl [Account Settings](https://www.quandl.com/account/profile) page to retrieve your API key.

2. Create a new `.env` file and declare an environment variable named `QUANDL_API_KEY`.

3. Open the Jupyter Notebook starter file and import the Python `requests`, `os`, and `dotenv` libraries.

### Execute API call with API key/env variable

4. Use the `load_dotenv()` method from the `dotenv` package to load and export the environment variables.

5. Use the `os.getenv` function to retrieve the environment variable named `QUANDL_API_KEY`. Store as a Python variable named `api_key`.

6. Use the `type` function to confirm the retrieval of the API key. Hint: If `NoneType` is returned, the environment variable does not exist. Revisit steps 2 and 3.

7. Concatenate `request_url` with the `api_key` variable.

8. Execute a `GET` request using Python `requests` library and the newly created request_url.

9. Display content to screen using the content attribute.

## Hint

You may find it useful to review the [Quandl API documentation](https://www.quandl.com/tools/api).

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
