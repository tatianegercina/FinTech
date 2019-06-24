### 12. Students Do: Sporting Plaid - Part 1 (15 mins)

This activity is the first part of a two part mini-project activity. Students will create **environment variables** for **Plaid** API keys and install the **Plaid** SDK, which will be used in the next activity to extract transaction data.

Instruct TAs to confirm that each student has **Plaid** API keys and can authenticate with **Plaid**. Circulate through the room to help troubleshoot any challenges related to **environment variables** and API keys.

Communicate to students that they can work with a partner to complete the activity; however, each student will need to complete the assignment.

**Files:**

* [keys.sh](Activities/13-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/key.sh)

* [sporting_plaid.ipynb](Activities/13-Stu_Sporting_Plaid_Pt_1/Unsolved/Core/sporting_plaid.ipynb)

**Instructions:**

* [README.md](Activities/13-Stu_Sporting_Plaid_Pt_1/README.md)

- - -

### 13. Instructor Do: Emotional Break (5 mins)

Facilitate discussion by asking students about their experiences working with API keys and SDKs.

* Ask students about the pace of the class. Is it going too fast, too slow, or just right?

* Empower students to continue on by emphasizing that they're one step away from adding **Plaid** to their toolkit. Reiterate that **Plaid** is going to help them acquire the data they need to perform financial analysis, and it will broke the communication channel between banks and FinTech application servers.

* Remind students that they are making excellent progress. Not only are they submitting requests to an API, they're submitting authenticated requests in a programmatic way using SDKs.

If time remains, ask the following questions:

* What data type can **environment variables** be stored as?

  **Answer:** String

* Are **environment variables** inherited?

  **Answer:** Yes. Parent processes pass environment variables down to child processes. The `export` and `source` commands ensure that child processes inherit the environment variables.

* Why is Plaid considered a FinTech disruptor?

  **Answer:** **Plaid** is changing the way developers and consumers can get access to FinTech data. Not only is **Plaid** providing a technology platform to get access to FinTech data, it is also providing analytic/insight products to help consumers understand their data and make data-driven decisions.

* How glad are you that SDKs don't require users to build long, parameterized request urls like the Python `requests` library?

Ask students if they have any questions before moving on.
