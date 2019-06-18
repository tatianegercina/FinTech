# Under Lock and Key

You and Harold have developed a Python application that will extract historical stock data from **Quandl** for a given ticker and calculate the sharpe ratio for that stock. So far, only you two have been using the application, but your manager now wants you to find a way to make the application usable by the entire team. You know that **Quandl** allows API calls to be submitted without an API key, but the limit is 50 calls a day. You're worried that the scale of this initiative will push you and your users over the rate limits for API calls made without an API key.

Create a new Python application that passes an API key with the request URL so that **Quandl** can manage and track rate limits.

## Instructions

1. Navigate to the Quandl [Account Settings](https://www.quandl.com/account/profile) page to retrieve API key.

2. Import Python requests library.

3. Save **API key** as a variable named `api_key`.

4. Concatenate **request_url** with the **api_key** variable.

5. Execute a `GET` request using newly created **request_url**.

6. Display content to screen using **content** attribute.
