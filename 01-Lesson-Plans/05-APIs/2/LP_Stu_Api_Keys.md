### 3. Student Do: Under Lock and Key (15 mins)

In order to reinforce the importance of using environment variables for securing API credentials, as well as give students hands on practice, students will revisit the Quandl API and submit a request with API keys stored as environment variables. Steps will be included to make sure students are using best practices when working with and exporting environment variables, such as using as key.sh file to export and store user specific environment variables.

**Files:**

* [api_keys.ipynb](Activities/03-Stu_Api_Keys/Unsolved/api_keys.ipynb)

**Instructions:**

* [README.md](Activities/03-Stu_Api_Keys/README.md)

- - -

### 4. Instructor Do: Activity Review (5 mins)

In this activity, students will review the previous activity by watching the instructor perform a live walkthrough of the solution.

**Files:**

* [api_keys.ipynb](Activities/03-Stu_Api_Keys/Unsolved/api_keys.ipynb)

Open the [starter-file](Activities/03-Stu_Api_Keys/Unsolved/api_keys.ipynb), and begin live coding and discussing the following:

* Declare variable `api_key`. Then, concatenate `request_url` with `api_key`.

  ![request_with_key.PNG](Images/request_with_key.PNG)

* Execute a GET request using Quandl service with API key, and store the data in a variable named `response_data`.

* Use the `content` attribute to display results. Hint: `response_data.content`

  ![response_content.PNG](Images/response_content.PNG)

Ask the following review questions:

* Do **ALL** APIs require API keys?

  **Answer** No. Only some APIs require keys to be used. Others allow users to submit requests for free (with rate limits).

* Why require users to have an API key when requests can be sent without urls?

  **Answer** API keys allow companies monitor, analyze, and enforce rate limits.

* What happens when the `?api_key=` tag is used? Is a function executed or is a parameter passed.

  **Answer** A parameter is being passed.

* Can more than one user have the same API key?

  **Answer** No. API keys are unique identifiers. Each key is assigned to one user.

* Are API keys naturally secure?

  **Answer** No, they are not. API keys are transmitted across network and are not naturally encrypted. API keys can be encrypted to make them private.
