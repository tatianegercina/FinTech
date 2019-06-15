### 2. Instructor Do: API Keys (5 mins) (Critical)

In this activity, students and instructor will participate in a facilitated discussion regarding **API keys**. Students will learn the what, why, and how of **API keys**.

Guided questions are provided to help facilitate discussion. Use these questions as timing permits.

**Files:**

* [API Keys Slides]

Navigate to the 5.2 slides, and introduce students to **API keys**.

* Many companies that offer APIs require users to sign up for **API keys**. **API keys** are access tokens that serve as a form of credential (like a user name or password) that grants users privileges and permissions needed to submit API requests. **API keys** are unique identifiers used by APIs to recognize which users submitted which requests.

* **API keys** are like the keys to a house or a car. Without a **key**, one cannot gain access or make use of the services provided by an API. APIs that require **keys** will reject any request that does not include an **API key**.

  ![API Key](https://image.shutterstock.com/image-vector/lady-holding-key-put-lock-600w-670094866.jpg)

* Explain the main reason why companies use **API keys**. **API keys** is to monitor and control user requests, as well as receive compensation for their services/intellectual property. Because **API keys** detail permissions and privileges for users, companies can programmatically disable and enable API privileges based off of number of requests submitted.

Initiate a facilitated discussion by communicating the following guided questions and discussion points. Choose two or three questions to ask, depending on available time.

* Ask the students: API keys are submitted with all API requests. Does it seem safe to transmit a unique key over the internet with every request? If no, why not?

  * **Answer:** It is not safe. It is because **API keys** are transmitted over the internet that they are not considered a proper security layer. If someone were to intercept the client-server communications, they'd be able to retrieve a user's **API key**.

* Ask: If **API keys** can be intercepted with every submitted request, why use them?

  * **Answer:** **API keys** are used because they prohibit non-registered users from making requests. When an API requires a **key**, a **key** must be provided in order for the API to execute. This forces users to register for the API and request an API key, which also allows the owner of the API to monitor that user's usage and charge them for services rendered.

* Pose the following question: What type of privileges and permissions could be tied to an **API key**? (Hint: CRUD.)

  * **Answer:** Create, read, update, delete.

* Ask: Is there anything that can be done to securely transmit an **API key** so that others cannot gain access to the **key**? If yes, provide an example of how.

  * **Answer:** **API keys** can be made secure through encryption. Many companies offering APIs, like **Amazon Web Services**, provide users with **API keys** as well as **secret keys**. **Secret keys** work much like **API keys**; however, they're typically encrypted so they can be kept private.

* Ask: Any guesses regarding how to submit a request with an **API key**?

  * **Answer:** Submit the **key** with the request URL as a parameter.

End the activity by asking the students if they have any further questions.
