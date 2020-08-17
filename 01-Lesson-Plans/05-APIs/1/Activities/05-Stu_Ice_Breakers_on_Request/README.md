# Ice Breakers on Request

Your company has recently begun engaging in table talk sessions aimed towards helping the team continue to build soft and conversational skills by having co-workers engage each other for 5 minutes. You're tired of asking basic questions about hometowns and occupations, so you've decided to crawl the web for some new content to use. Your goal is to have ice breakers available on request. You've found 6 APIs that you feel could provide some good, random material for table/small talk.

Submit `GET` requests using the Python `requests` library for one of the below `request urls`. Then, interpret the JSON output and find an interesting fact or joke to share with the class. Save that fact/joke, or another value from the JSON output, as a variable.

APIS

* Random Programming Jokes -> https://official-joke-api.appspot.com/jokes/programming/random

* Random Jokes ->  https://official-joke-api.appspot.com/jokes/random

* Cat Facts -> https://cat-fact.herokuapp.com/facts

* U.S. Dept of Treasury Spending Stats -> https://api.usaspending.gov//api/v2/references/agency/456/

* U.S. GDP Data -> http://api.worldbank.org/v2/country/us?format=json

## Instructions

1. Choose one of the above APIs to work with for this assignment.

2. Execute the `requests.get` function using one of the `request urls`, and store the output in a variable named `response_data`.

3. Retrieve the status code of the request.

4. Execute `response_data.content` to extract the data from the request. Store the data in a variable named `response_content`, and output the data to the screen.

5. Use the `json` function to format `response_content` as JSON. Store the output as a variable named `data`.

6. Import the `json` package, and use `json.dumps` to print `response_content` to the screen with formatting. Use the `indent=4` parameter to format with indentation.

7. Decipher the JSON data, and identify an interesting fact/joke to share with the class. Write it down to tell the class during the activity review.

8. Select an element from the JSON and store it into a new variable. Hint: JSON attribute names are like keys in dictionaries (i.e., `response_content.fact` or `response_content.joke`).

### Challenge

If time remains, use the `GET` function to explore the other APIs.

### Hint

Selecting values from JSON data requires data be accessed first by parent object and then child. When an API returns output with multiple `JSON Objects`, `indices` have to be specified to indicate which object/record should be selected. For example,

  ```python
  selected_value = data['all'][0]['text']
  ```

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
