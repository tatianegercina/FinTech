### 11. Students Do: Python Requests (20 mins)

In this activity, students are given a list of `request urls` to execute using the Python `requests` library. Students will also receive the opportunity to put their JSON knowledge to use by interpreting JSON output. Students will interpret the JSON output to find an interesting fact or joke to tell the class.

Walk around with TAs to provide assistance to students with parsing JSON data. Students may need assistance parsing JSON output. Make sure every student has been able to successfully execute a request and find an interesting fact/joke to share, even if the fact has to relate to their own experiences using Python requests.

**Files:**

* [python_requests.ipynb](Activities/11-Stu_Python_Requests/Unsolved/python_requests.ipynb)

**Instructions:**

* [README.md](Activities/11-Stu_Python_Requests/README.md)

### 12. Students Do: Requests Engagement Activity (15 mins)

In this activity, have each student reveal an interesting fact or joke they discovered while working with APIs. Round robin and have each student volunteer a fact or joke.

If a student doesn't find a fact or joke they feel like sharing, ask them to answer one of the following questions:

* Discuss their opinions regarding using the Python `requests` library to make API calls instead of `Postman`.

* Identify one advantage of using Python `requests` library over using `Postman`.

> "The `requests` library allows API calls to be made in-line with the rest of the code/processing. Postman requires users to transition from one development environment to another."

Transition into a reflective Q&A session. Ask the students the following questions:

* Having seen a range of FinTech and quirky APIs, what API can you see yourself implementing on your own accord?

* Are there specific types or categories of APIs you'd be interested in working with?

* What type of APIs are you interested in creating?

* Deciphering and parsing JSON can be frustrating and challenging, especially when the data isn't formatted in the best way. Did the `json.dumps` improve your ability to decipher the JSON data?

If time remains, tell students about some of the APIs you've worked with and how they've added to your professional success. Encourage students to take advantage of as many open source APIs as possible. Take this time to recommend any APIs that you feel students might be interested in.

Ask students if there are any comments or questions they'd like to make regarding their experiences working with APIs so far. Then transition into a formal review of the Python Requests activity.

### 13. Instructor Do: Review Python Requests (10 mins)

**Files:**

* [python_requests.ipynb](Activities/11-Stu_Python_Requests/Solved/python_requests.ipynb)

Open the solution and conduct a dry walkthrough review, highlighting the following discussion points:

* The Python `requests` library can be used to submit API requests. Just like `Postman`, the `requests` library will submit the request to the server, and then wait for the response. In order to use the library, it has to be imported.

  ```python
  import requests
  ```

* The `requests` library comes with a `GET` function that can be used to execute a `request url`.

  ```python
  request_data = requests.get(prog_joke_url)
  ```

* Each Python `request` generates a `response code`. The `response code` indicates whether or not the response was successful and details if there were any errors.

  ```python
  print(request_data)
  ```

  ```
  <Response [200]>
  ```

* The `content` from a `request` can be accessed using the `content` attribute.

  ```python
  # Store response using `content` attribute
  response_content = response_data.content
  ```

* The `JSON` function is used to format API into JSON format.

  ```python
  # Get content as JSON
  data = response_data.json()
  ```

* `json.dumps` can be used to format the JSON output in a way that is easy to decipher and interpret visually. The `indent` argument is used to specify how many indentations should be used when formatting. Indents help delineate JSON levels/hierarchies.

  ```python
  import json

  # Use json.dumps with argument indent=4 to format data
  print(json.dumps(data, indent=4))
  ```

  ![json_dumps.png](Images/json_dumps.png)

* Data from the API can be extracted from its JSON format by using brackets `[]` to specify the desired element, in fully qualified format (i.e. [parent][index][child]). Depending on the JSON format, the parent and index levels may not be applicable.

  ```python
  # Select a programming joke
  selected_value = data[0]['setup']
  selected_value_2 = data[0]['punchline']
  ```

  ![access_json_data.png](Images/access_json_data.png)
