### 8. Students Do: Parle-vouz le JSON? (5 mins)

The key to working with APIs is being able to decipher their output. Because API output is commonly in JSON format, students will need practice deciphering JSON structures and syntax. In this activity, students will choose a sub-selection of the JSON output to decipher. They will then explain the sub-selection to a peer.

Walk around and instruct TAs to circulate during this activity so that students can ask questions as they make sense of the JSON data, including its structure and syntax. Some students will have had little to no exposure to JSON data in the past. It can be frustrating trying to interpret JSON data when the structure and syntax is foreign.

**Instructions:**

* [README.md](Activities/08-Stu_Decipher_Json/README.md)

### 9. Instructor Do: Review Turn and Teach (5 mins)

Navigate to 5.1 slides on deciphering JSON output, and use the visuals to highlight the following:

* `JSON` data is structured data. JSON data is comprised of `name/value` pairs. Names are data attributes/column names and values are the actual values associated with that attribute/column. JSON data is made up of `JSON Objects` and `JSON Arrays`.

* `JSON Objects` are identified by the use of curly braces `{}`. These objects often contain multiple name/value pairs, like a `row` (i.e {"ticker":"GOOG","close_price":192.57}).

* `JSON Arrays` are identified by brackets `[]`. An example of a `JSON Array` is the `column_names` object returned from the Quandl API call.

Open Postman and submit the below request to Quandl.

* https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json

Do a live deciphering of the JSON data, and emphasize the following:

* `Name/value` pairs are used to make deciphering JSON data easy because it does a single map between `name` and `value`. Point out an example of a `name` (i.e. the `description` field). Then, identify the corresponding value.

* Point out `JSON Array` and `JSON Objects` in order to compare them.

  ![decipher_json.png](Images/decipher_json.png)

End the review session by asking the students the following questions. Sample answers have been provided.

* We've seen a number of APIs in action (i.e. WrapAPI, Quandl, World Bank, Coinbase). Which API did everyone find the most interesting?

  > "WrapAPI. While it is not FinTech related, it's unique and has a number of different use cases. Of all of the APIs, WrapApi seems the most flexible and all-encompassing."

* Ask students to write down two things they like about APIs and the `client-server model`. Ask for two volunteers to present their answers.

  > "The client server-model is simple, easy to understand, and used almost everywhere. APIs are cool because they eliminate the need of having to redundantly re-invent the wheel."

* Ask students to write down one thing they do not like and/or find challenging about APIs and the `client-server model`. Ask one student to volunteer their answer, and collect the remaining answers as students leave the classroom.

  > "Not all APIs have good documentation. It's difficult to gauge exactly what an API can do and/or how it should be used."

Before moving forward, ask the students if there are any remaining questions.
