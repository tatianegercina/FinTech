### 10. Instructor Do: Python Requests (10 mins)

Submitting APIs with Postman is useful, but API requests are better sent with Python code. Instructors will demonstrate to students how to submit an API request with Python instead of Postman. Emphasis will be placed on the similarities between the two processes, as well as the advantages of sending requests through Python.

The World Bank API (GDP extraction) should be used for this instructor demonstration activity.

**Files:**

* [python_requests.ipynb](Activities/10-Ins_Python_Requests/Solved/python_requests.ipynb)

Navigate to the 5.1 slides, and highlight the following:

* Just as API `requests` can be sent through Postman, they can slo be sent through Python. Python offers a `requests` package that can be used to submit API requests through a protocol known as `HTTP`. The `requests` library supports `GET`, `POST`, and `PUT` requests, just to name a few. `GET` requests will be the focus for this class.

* Each type of request serves a different purpose.

  * `GET` requests are used to extract/acquire data from a server

  * `POST` requests are used to push new or updated data to the server

  * `PUT` requests are used to overwrite content on the server

* APIs play a key role in data analytic pipelines, often being the source of data or a means to analyze data. By writing `requests` in Python, APIs can be used in-line with other processing. For example, data can be pulled from Coinbase in order to calculate `cumulative returns`, `sharpe ratio`, and `beta` for a set of cryptos. Similarly, data could be extracted from the Quandl API in order to complete portfolio simulations. Instead of switching back and forth between Postman and Python, everything can just be completed in Python.

Live code how to use the Python `requests` library, and use the following discussion points:

* The `requests` library has to be imported in order to be used

  ```python
  import requests
  ```

* The first step to using the requests library after importing it is to declare a variable that will hold the URL.

  ```python
  url = "http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD"
  ```

* Because most APIs support multiple output formats, the next step is to specify the desired output format. This can be added to the url with a `format` tag, `?format=`. Common formats used are JSON, CSV, and XML. For this lesson, JSON will be the focus. The format tag will need to be appended to the `url` string previously created; ask students if anyone remembers how to append to a string (Answer: concatenation).

  ```python
  url = url + "?format=json"
  ```

* `GET` requests can be sent using the `requests.get` function. The function accepts the `request url` as an argument.

  ```python
  # Execute GET request
  requests.get(url)
  ```

  ![request_response.png](Images/request_response.png)

* Most APIs incorporate programming that will return a code with each server response. These are called `response codes`. A list of common response codes and their meaning can be found below.

  ```
  Common Response Codes

  200s: Success
  400s: Error
  500s: Request accepted but error occurred server side
  ```

* Output from a `GET` request is best saved as a variable. This allows for the output to be parsed and manipulated down the road.

  ```python
  # Execute GET request and store response
  response_data = requests.get(url)
  ```

* The actual data returned from the server, called `content`, can be accessed with the `content` attribute.

  ```python
  # Get content
  response_content = response_data.content
  print(response_content)
  ```

  ![submit_python_request.png](Images/submit_python_request.png)
