### 3. Student Do: Keys to the Kingdom (15 mins)

Over the next couple activities, students will be working with APIs that require **keys** for access. Use this time to confirm all students have the necessary **keys** for the **Quandl** and **Plaid** APIs. The instructor and TAs will circulate through the room confirming all students are ready to begin using their **API keys**. Provide assistance to any students who do not have **API keys**.

Each student should be met individually. Students should have their account pages ready for instructor/TA review. Instructor/TA must review each student's account pages to ensure all **API keys** are available.

Slack out the below API links just in case some students still need to sign up.

* [Quandl Signup Page](https://www.quandl.com/sign-up-modal?defaultModal=showSignUp)

* [Plaid Signup Page](https://dashboard.plaid.com/signup)

**Instructions:**

* [README.md](Activities/03-Stu_Api_Keys/README.md)

Indicate to students that this activity will focus on making sure everyone is prepared to begin using the **Quandl** and **Plaid** APIs. Students will need to confirm they have the necessary **keys** to access **Quandl** and **Plaid** as the TAs and yourself touchbase with each of them.

Ask students to pull up their account pages for **Quandl** and **Plaid** and to confirm that they have API keys for both APIs.

* Instruct TAs to circulate through the room and to check with each student to confirm availability of **Quandl** and **Plaid** **API keys**.

* Circulate the room and provide assistance to any students who do not have an **API key**. Provide troubleshooting if there are any issues.

* Confirm instructor **API keys** are available and ready for use. If not completed already, create a `keys.sh` file that will store **Quandl** and **Plaid** **API keys**.

Excite students about FinTech APIs by highlighting the following points.

* Communicate that many APIs, like **Plaid**, are disrupting the financial industry and market. Many APIs have grass roots initiatives, meaning they are creating tools and technologies for people rather than companies and corporations. These efforts echo the open-source movement.

* Reiterate that even though many APIs require **keys**, their services are often free. Obtaining an **API key** is like getting the **keys** to a kingdom. Once you're in, you're empowered to build products and submit API requests as you please. There are limitations, but services are still free.

If time remains, ask the following review questions:

* Do **ALL** APIs require API keys?

  **Answer** No. Only some APIs require keys to be used. Others allow users to submit requests for free (with rate limits).

* Why require users to have an API key when requests can be sent without APIs?

  **Answer** API keys allow companies monitor, analyze, and enforce rate limits.

* What happens when the `?api_key=` tag is used? Is a function executed or is a parameter passed.

  **Answer** A parameter is being passed.

* Can more than one user have the same API key?

  **Answer** No. API keys are unique identifiers. Each key is assigned to one user.

* Do you think API keys are naturally secure?

  **Answer** No, they are not. API keys are transmitted across network and are not naturally encrypted. API keys can be encrypted to make them private.

* Is there a problem with sharing an **API key**?

  **Answer** Yes. Rate limits are tied to API keys. Sharing an API key would mean sharing the total number of requests allowed with another individual. Sharing keys could also result in someone else charging your account for billable services.

Ask if there are any questions or comments before moving on.
