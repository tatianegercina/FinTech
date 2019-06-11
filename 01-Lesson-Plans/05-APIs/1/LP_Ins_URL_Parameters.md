### 15. Instructor Do: URL Parameters (5 mins)

In this activity, students learn how to customize API requests with `parameters` through instructor demonstration. The [Numbers API](http://numbersapi.com) will be used for the demonstration, so make sure the API is still up and running prior to class.

**Files:**

* [url_parameters.ipynb](Activities/15-Ins_URL_Parameters/Solved/url_parameters.ipynb)

Navigate to the 5.1 slides, and highlight the following:

* Each API call supports a set of `parameters`. These `parameters` can be used to help direct the API towards the data needed or be used to reduce the amount of data being returned by the server.

  * Ask the students: We've already made some API requests using `parameters`. Can anyone remember any examples?

    > "When using the `?format=json` tag."

* `Parameters` can be specified in one of two ways. `Parameters` can follow `/` forward slashes or specified by `parameter` name and then by `parameter` value.

  ```
  Parameter provided after /
  http://numbersapi.com/42
  ```

  ```
  Parameter provided using parameter name and value
  http://numbersapi.com/random?min=10?json
  ```

* When used with parameter names, `URL parameters` have to be separated from the `request url` with the `?` symbol.

  ```
  http://numbersapi.com/random?min=10
  ```

* Multiple parameters can be passed in with the same URL by separating each `parameter` with an `&` symbol

  ```
  http://numbersapi.com/random?min=10&max=20
  ```

Open the solution, and conduct a dry walk through of the following solution. Touch upon the following discussion points:

* The requests `GET` function can be used to submit a `parameterized` request to the Numbers API to get trivia facts about the number 42.

  ```python
  import requests
  import json

  # Create parameterized url
  request_url = "http://numbersapi.com/42?json"

  # Submit and format request
  response_data = requests.get(request_url).json()
  print(json.dumps(response_data, indent=4))

  # Select fact
  response_data['text']
  ```

  ![url_parameters.png](Images/url_parameters.png)

Open the starter file, and live code the following:

* The Numbers API URL can be `parameterized` to execute for the number `8` instead of `42`.

  ```python
  # Create parameterized url
  request_url = "http://numbersapi.com/8?json"

  # Submit and format request
  response_data = requests.get(request_url).json()
  print(json.dumps(response_data, indent=4))

  # Select fact
  response_data['text']
  ```

  ![url_parameters_8.png](Images/url_parameters_8.png)

End the class with a final question:

* What kind of parameters should be used when working with financial APIs? One example is dates. What are others? Hint: Think attributes related to people, stocks, bank accounts, credit scores, etc.

  > "Names, birthdays, social security numbers, tickers, trade limits, number of shares to buy, limit order dollar amounts, routing numbers, checking accounts, etc."

Ask the students if they have any remaining questions before moving on.
