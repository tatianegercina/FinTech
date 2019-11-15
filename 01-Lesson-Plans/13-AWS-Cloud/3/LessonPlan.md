## 13.3 Lesson Plan - Amazon Lex and Robo Advisors

### Overview

In Today's class, students will be introduced to conversational user interfaces (CUIs) also they will learn how CUIs are disrupting finance and banking. By the end of the class, students will create a robo advisor using Amazon Lex, Amazon Lambda and Slack.

### Class Objectives

By the end of the unit, students will be able to:

* Describe the applications of conversational interfaces for finance and banking.

* Recognize how machine learning contributes to create conversational interfaces.

* Create conversational interfaces using Amazon Lex.

* Apply their Python skills to add new features to an Amazon Lex bot using Amazon Lambda.

* Deploy a robo advisor application on Slack.

### Instructor Notes

* Slack out the [Deep Learning Installation Guide](../../14-Deep-Learning/Supplemental/deep_learning_installation_guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* There are several misconceptions and myths about what can be achieved with a Robo Advisor, make sure students understand what a Robo Advisor is and invite them to think about the endless possibilities of this technology for FinTech.

* Today's class may be challenging for students because they are going to deal with different AWS services and the Slack API, so be sure to get familiar with all the activities before class.

* Amazon Lambda functions will be created and edited using the online code editor. This editor sometimes has issues or freezes up, so tell students to backup their code with a local Python script.

* Testing Amazon Lambda functions could be tricky and frustrating, so have your TAs assisting students while they are coding and testing them.

* **Important:** At the end of Today´s class, remember students to create a local copy of all their deployments on AWS, so they can delete them from the cloud to avoid additional charges. Also, remind students to be aware of AWS free tier and trials expiration date.

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [13.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f288da5-fe69-4899-b21d-aaf1013917e1) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1n9mKCC7_yl_P_GUHnLCauvdgunTLigX0tfamq2kJ0RQ/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 min)

In this activity, students will be introduced to conversational user interfaces (CUIs); they will learn how CUIs are disrupting financial services and what are the tools they will use to create a robo advisor.

Welcome students back and explain that today, we will learn about conversational user interfaces, one of the coolest applications of natural language processing, explain to students that they will create a robo advisor with conversational capabilities by the end of the day.

Open the lesson slides and move to the _Conversational User Interfaces (CUIs) and Robo Advisors_ section, highlight the following:

* On the early years of computing history, people used to communicate with computers using text interfaces and some non-human-friendly commands.

* Thanks to AI, and especially to the advances in natural language processing (NLP), we can communicate with computer systems using human language through conversational user interfaces via voice or text.

* Chatbots are the most common applications of CUIs; however, Amazon Alexa, Apple Siri, or Google Assistant are also examples of CUIs.

* Financial services providers are using CUIs by offering Robotic Advisors or Robo Advisors, as an additional communication channel for customers.

Engage students by highlighting the benefits of this technology on finance and banking, slack out [this article from Deloitte](../Supplemental/deloitte-nl-fsi-chatbots-adopting-the-power-of-conversational-ux.pdf) where they can learn more about the impact of chatbots in financial services.

Present to students the use cases shown on the _Example Chatbots Use Cases_ slide, ask a couple of them if they are familiar with services like these, and what were their experience.

Explain to the class the technologies we will use Today and highlight the following:

* By the end of Today's class, we will create a robo advisor using AWS.

* Amazon Lex is a service for building conversational interfaces into any application using voice and text.

* Amazon Lambda is a computing service that runs code in response to events. We will use this service to program the actions of the robo advisor.

* The robo advisor will be deployed as a Slack application where users will interact with it.

Answer any additional questions before moving forward.

---

### 2. Instructor Do: Intro to Amazon Lex (10 min)

In this activity, students will be introduced to Amazon Lex; they will learn how to create a bot using the Amazon Lex console that returns parameters to the client by configuring a single intent, some slots, and a confirmation prompt.

**Files:**

* [Share_The_Bill Bot](Activities/01-Ins_Intro_Lex/Solved/Share_The_Bill_1_d57679ca-cc90-4b74-9a61-2211a93f7208_Bot_LEX_V1.zip)

* [ShareBill Intent](Activities/01-Ins_Intro_Lex/Solved/ShareBill_6_6f154262-76b0-465f-aed1-ce1f3914c492_Intent_LEX_V1.zip)

Start this activity by opening the slides to the _Intro to Lex_ section and highlight the following:

* Amazon Lex is an AWS service that allows developers to create conversational interfaces powered by the same deep learning technologies like Alexa.

* Getting started with Amazon Lex is quite easy, it is just a four-step process.

* All the complexity of deep learning algorithms is encapsulated, no coding is needed to start using it.

Introduce the Amazon Lex jargon to students using a day-to-day example like booking a hotel room; comment to students that they will gain hands-on experience with these concepts in Today's class.

Clarify to students the AWS regions where Amazon Lex is available, and pricing varies among regions. We will use `US West (Oregon)` for running the examples.

Slack out the [Amazon Lex Pricing policies](https://aws.amazon.com/lex/pricing/), remind students that from the date they get started with Amazon Lex, they can process up to 10,000 text requests and 5,000 speech requests per month for free for the first year. **Note:** This is subject to change, so they should verify the pricing structure using the link above.

Close the presentation and open the AWS Management Console, explain to students that now you will create an Amazon Lex bot that will assist users to split a bill between a given number of people.

Follow the next steps to perform a live demo.

* **Step 1:** Login into the AWS Management Console using your IAM Admin user and URL.

  ![Step 1](Images/lex-step1.png)

* **Step 2:** Select `US West (Oregon)` as the AWS region for this demo.

  ![Step 2](Images/lex-step2.png)

* **Step 3:** On the _Find Services_ search box, type `Lex` and select the `Amazon Lex` service from the list.

  ![Step 3](Images/lex-step3.png)

* **Step 4:** If this is the first time you use Amazon Lex, you will see the following page to get started with your first bot.

  ![Step 4a](Images/lex-step4a.png)

  If you have already created a bot, you will be led to the following page instead of where you can see a list with your current bots.

  ![Step 4b](Images/lex-step4b.png)

* **Step 5:** To create a new bot, click on the _Custom bot_ option and fill-out the following, next click the `Create` button to continue:

  * _Bot name:_ Share_The_Bill
  * _Output voice:_ Mathew
  * _Session timeout:_ 5 min
  * _COPPA:_ Select `No`

  ![Step 5](Images/lex-step5.png)

* **Step 6:** Now you will create an intent to respond to the user's actions. Click on the _Create Intent_ button, and you will see a pup-up window entitled _Add intent_ as you can see below. Click on the _Create intent_ option to continue.

  ![Step 6](Images/lex-step6.png)

* **Step 7:** In this step you should give a name to the intent, explain students that normally intents are named as actions to be performed by the bot; type `ShareBill` and click on the _Add_ button to continue.

  ![Step 7](Images/lex-step7.png)

* **Step 8:** In this step, you will configure the intent to allow the bot to interact with the user. Start by adding the following sample utterances:

  * `We want to split the bill`
  * `Please help me to share the bill`
  * `I want to share the bill with my friends`

  At this point, explain to the students that these sample utterances will be used by the deep learning algorithm of Amazon Lex to understand the context of the conversation, the more different sample utterances you add, the best the conversation will flow between the bot and the user.

  ![Step 8](Images/lex-step8.png)

  Add two slots as follows:

  | Name         | Slot type     | Prompt                                                   |
  | ------------ | ------------- | -------------------------------------------------------- |
  | totalAmount  | AMAZON.NUMBER | I will be pleased to help, what is the bill's total amount? |
  | numberPeople | AMAZON.NUMBER | How many people are going to pay the bill?                |

  On the _Confirmation prompt_ section, enable the confirmation prompt and type the following confirm and cancel prompts:

  * _Confirm prompt:_ `Are you sure you want to split a bill for ${totalAmount} between {numberPeople} people?`
  * _Cancel prompt:_ `Okay, let's start again.`

  Explain to students that in the confirm prompt, `{totalAmount}` and `{numberPeople}` are a kind of variables that will be filled out with the values given by the user.

* **Step 9:** Now it is time to see the bot in action, build your bot by clicking on the _Build_ button, and confirming the build option on the pop-up window.

  ![Step 9a](Images/lex-step9a.png)

  The building process takes a couple of minutes. Once the process finished, you will see the following confirmation message, and the _Test bot_ window will appear. You can now close the confirmation message and test your bot.

  ![Step 9b](Images/lex-step9b.png)

* **Step 10:**  Test your boot using the first sample utterance, you should have a dialog with the bot as follows.

  ![Step 10](Images/lex-step10.gif)

  Explain to students that at this time, the bot has no business rules logic attached, that is why the final message the bot sends after fulfilling all the slots is a kind of non-friendly confirmation message. We will improve this by adding an Amazon Lambda function to the bot.

  ![Fulfillment message](Images/lex-step10msg.png)

Answer any pending questions before continuing.

---

### 3. Students Do: Simple Crypto Conversation (15 min)

In Today's class, students will create a bot that converts a given amount on US Dollars to its value in bitcoin `BTC`, ethereum `ETH` or ripple `XRP`. In this activity, students will start creating the bot by defining an intent, some sample utterances and two slots in order to convert from US Dollars to `BTC`.

**Instructions:**

* [README.md](Activities/02-Stu_Simple_Crypto_Conversation/README.md)

---

### 4. Instructor Do: Review Simple Crypto Conversation (10 min)

**Files:**

* [Crypto Converted export file](Activities/02-Stu_Simple_Crypto_Conversation/Solved/Crypto_Converter_1_c99b8f7e-ea4d-4a6e-bb46-f179beeb5e60_Bot_LEX_V1.zip)

You can choose to live demo the solution or import the solution file into your Amazon Lex console.

To import the solution, click on the _Import_ option into the _Actions_ button and select the provided ZIP file; once the import process ends, you will have the bot and the intent available on your Amazon Lex console, be sure to build the bot before starting the review activity.

![Import Lex Bot](Images/import-lex-bot.png)

Click on the `Crypto_Converter` bot, once the `convertUSD` intent is on the screen highlight the following:

* Adding `{usdAmount}` on the sample utterances, will allow the user send messages like `I want to convert **100** dollars to BTC` where the deep learning algorithms will match the `{usdAmount}` label with a number on the utterance speech, as can be seen on the demo gif file bellow.

* When the bot is tested, the date of birth can be given on any format (e.g., `12/16/1978`, `16/12/1978`, `Dec 16, 1978`), using the `AMAZON.DATE` slot type will transform the date automatically to the `YYYY-mm-dd` format, as can be seen on the demo gif file bellow.

  ![Demo bot test](Images/crypto_converter_1.gif)

Answer any questions before moving on.

---

### 5. Instructor Do: Intro to AWS Lambda (10 min)

This activity will introduce AWS Lambda to students. Also, students will learn how they can integrate Lambda functions into an Amazon Lex bot. The full code of the lambda function could be found on the _Solved_ directory.

**Files:**

* [lambda_function.py](Activities/03-Ins_Intro_Lambda/Solved/lambda_function.py)

Start the activity by opening the lesson slides, navigate to the _Intro to AWS Lambda_ section, and highlight the following:

* Sometimes AWS Lambda is seen as a web service or and API since it runs code remotely, however, AWS Lambda is a serverless technology where you just upload your code and Lambda takes care of everything.

* In general terms. _serverless_ means that you do not have to be worried about any server configuration nor administration.

* AWS Lambda can have your automatically trigger from other AWS services or call it directly from any web or mobile app.

* We are going to use AWS Lambda by triggering code from an Amazon Lex Bot.

* AWS Lambda enhances chatbots by combining the NLP capabilities of Amazon Lex to understand human speech, with the possibility of running code to fulfill user's requests, for example, booking a hotel room, making a wire transfer, or providing financial advice about an investment portfolio.

* AWS Lambda interacts with other AWS services by processing events messages in `JSON`, every AWS Services has its specific format.

* Amazon Lex "talks" to AWS Lambda to perform initialization and validation, fulfillment, or both.

Explain to students that in this demo, you will show how to process `ElicitSlots`, `Delegate` and `Close` response events.

Close the slides and log-in into the AWS Management Console using your IAM administrator user, once you are logged in, type `Lambda` into the _AWS services_ search box and click on _Lambda_ to open the AWS Lambda console.

![Search for AWS Lambda service on the AWS Management console](Images/search-lambda-service.png)

In the AWS Lambda console, click on _Functions_ on the left side menu; continue by clicking on the _Create function_ button.

![AWS Lambda console](Images/aws-lambda-console.png)

On the _Create function_ page, select the _Author from scratch_ option, fill out the following information, and click on the _Create function_ button:

* **Function name:** `convertUSD` (This is the name to identify our new Lambda function)
* **Runtime:** `Python 3.7`

![Create function page](Images/aws-lambda-create-function.png)

Explain to students that now AWS will create the `convertUSD` lambda function, and it takes a few seconds. Once created, you will see the following page.

![convertUSD function created](Images/convertUSD-created.png)

Scroll down to the _Function code_ section, explain to students that this code is a starter `Hello World` example. Highlight that a lambda function has a main events handler; its goal is to manage all the incoming messages and dispatch them depending on the business logic defined.

* We will use the `lambda_handler` to route the incoming requests based on the user's intents captured by the Amazon Lex bot.

![Function code section](Images/convertUSD-function-code.png)

Open the slides and show students the anatomy of the lambda function you are going to use. Let the students know that this code can be used as a boilerplate template to code business logic to extend Amazon Lex bots functionality.

![Lambda function anatomy](Images/lambda-function-anatomy.png)

Explain to students that the lambda function contains six general building blocks, briefly present these blocks, and open the `lambda_function.py` script on VSCode by highlighting the following:

1. **Required Libraries:** This section contains all the necessary libraries to code the business logic on the lambda functions, despite AWS Lambda supports Python, the runtime doesn't support some common packages such as `pandas`, `numpy` or `requests`, so alternative packages should be used or installed. In this demo, we take the current price of bitcoin making an API call to [CoinMarketCap](https://api.coinmarketcap.com/v1/ticker/bitcoin/), so the `requests` library is imported from the [`botocore` package](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html). A complete list of the python modules available on AWS Lambda can be found [here](https://gist.github.com/gene1wood/4a052f39490fae00e0c3).

2. **Functionality Helper Functions:** These functions implement business logic and data validation. In this demo, we have four helper functions.

    * `parse_float()`: This function securely parses a non-numeric value to float.

    * `get_btcprice()`: Retrieves the current price of bitcoin in US Dollars from CoinMarketCap.

    * `build_validation_result()`: This function defines an internal validation message structured as a python dictionary.

    * `validate_data()`: This function validates the data provided by the user across the intent's dialog on Amazon Lex according to the business logic. In this demo, there are only to rules: (1) the user should be at least 21 years old (2) the amount in US Dollars to convert must be greater than zero.

Explain students that the `validate_data()` function uses the `build_validation_result()` function to return a validation result message. In this demo, if the user's age is less than 21 or the amount to convert is less than 0, a `False` result is returned; otherwise, a `True` result is returned.

```python
def validate_data(birthday, usd_amount, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate that the user is over 21 years old
    if birthday is not None:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        age = relativedelta(datetime.now(), birth_date).years
        if age < 21:
            return build_validation_result(
                False,
                "birthday",
                "You should be at least 21 years old to use this service, "
                "please provide a different date of birth.",
            )

    # Validate the investment amount, it should be > 0
    if usd_amount is not None:
        usd_amount = parse_float(
            usd_amount
        )  # Since parameters are strings it's important to cast values
        if usd_amount <= 0:
            return build_validation_result(
                False,
                "usdAmount",
                "The amount to convert should be greater than zero, "
                "please provide a correct amount in USD to convert.",
            )

    # A True result is returned if age or amount are valid
    return build_validation_result(True, None, None)
```

3. **Dialog Actions Helper Functions:** These functions handle the input and response events data from the "conversation" between Amazon Lex and AWS Lambda. The `get_slots()` function fetches all the slots and their values from the current intent. The `elicit_slot()`, `delegate()` and `close()` functions, construct response messages structured as a valid JSON Lex event. The full structure of event data that Amazon Lex exchanges with a Lambda function can be reviewed [here](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html).

4. **Intents Handlers:** The core business logic is coded into an intent handler. An intent handler is a function that implements the functionality that is willing to fulfill the user's intent.

Explain students that in this demo, the `convert_usd()` function contains all the logic to validate the user's input stored in the `slots` using the `validate_data()` helper function; along the conversation between the user and the bot, if any of the `slots` have invalid data, an `elicitSlot` dialog is returned to request the data again to the user, otherwise a `delegate()` dialog is returned to direct Lex to choose the next course of action according to the bot's configuration.

```python
if source == "DialogCodeHook":
    # This code performs basic validation on the supplied input slots.

    # Gets all the slots
    slots = get_slots(intent_request)

    # Validates user's input using the validate_data function
    validation_result = validate_data(birthday, usd_amount, intent_request)

    # If the data provided by the user is not valid,
    # the elicitSlot dialog action is used to re-prompt for the first violation detected.
    if not validation_result["isValid"]:
        slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

        # Returns an elicitSlot dialog to request new data for the invalid slot
        return elicit_slot(
            intent_request["sessionAttributes"],
            intent_request["currentIntent"]["name"],
            slots,
            validation_result["violatedSlot"],
            validation_result["message"],
        )

    # Fetch current session attributes
    output_session_attributes = intent_request["sessionAttributes"]

    # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
    return delegate(output_session_attributes, get_slots(intent_request))
```

Explain to students that once the conversation between the user and the bot ends, the current price of bitcoin in US Dollars is fetched using the `get_btcprice()` function, the conversion from USD to BTC in done and the `close()` function is called to return a `Fulfilled` event message to Lex.

```python
# Get the current price of BTC in USD and make the conversion from USD to BTC.
btc_value = parse_float(usd_amount) / get_btcprice()
btc_value = round(btc_value, 2)

# Return a message with conversion's result.
return close(
    intent_request["sessionAttributes"],
    "Fulfilled",
    {
        "contentType": "PlainText",
        "content": """Thank you for your information;
        you can get {} Bitcoins for your {} US Dollars.
        """.format(
            btc_value, usd_amount
        ),
    },
)
```

5. **Intents Dispatcher:** An Amazon Lex bot can have one or more intents, the purpose of the `dispatch()` function is to validate that the current intent is valid and to dispatch the intent to the corresponding intent handler. In this demo, we only have one intent, so we only have one intent handler call to the `convert_usd()` function.

    ```python
    def dispatch(intent_request):
        """
        Called when the user specifies an intent for this bot.
        """

        # Get the name of the current intent
        intent_name = intent_request["currentIntent"]["name"]

        # Dispatch to bot's intent handlers
        if intent_name == "ConvertUSD":
            return convert_usd(intent_request)

        raise Exception("Intent with name " + intent_name + " not supported")
    ```

6. **Main Handler:** Every time a user sends a message to Lex, using text or voice, an event will be sent to Lambda; the `lambda_handler()` function, catches every event and returns a response to Lex via the `dispatch()` function.

    ```python
    def lambda_handler(event, context):
        """
        Route the incoming request based on intent.
        The JSON body of the request is provided in the event slot.
        """

        return dispatch(event)
    ```

After presenting the Lambda function's building blocks, copy and paste the code from VSCode to the code editor on the AWS Lambda console, click on the _Save_ button to continue.

![Sample copied Lambda code](Images/copied-lambda-code.png)

Open the Amazon Lex console to bind the `convertUSD` lambda function to the bot. Open the _Lambda initialization and validation_ section, enable the _Initialization and validation code hook_ option and select the `convertUSD` Lambda from the list, next be sure to select the `Latest` version.

![Configure the Lambda initializations and validation](Images/lambda-init-val.png)

A pop-window asking you for permissions to your Lambda Function will appear next, click on the _Ok_ button to continue. Explain to students that this permission is needed to allow the communication between the bot and Lambda.

![Lambda permission prompt](Images/lambda-permissions-prompt.png)

Scroll down to the _Confirmation prompt_ section and disable the checkbox, continue by opening the _Fulfillment_ section and choose the _AWS Lambda function option_, select the `convertUSD` Lambda and the `Latest` version. Click on the _Build_ button on the upper right corner, and you are done, and now the bot is connected to Lambda to control the user's intent.

![Confirmation and fulfillment configuration](Images/lambda-confirmation-fulfillment.png)

Test the Lambda powered bot with some of the sample utterances; you should have a final conversation as it is shown below.

| _Bot demo conversation with valid user's data_ | _Bot demo conversation with invalid user's data_ |
| --- | ---|
| ![Converter without errors](Images/converter_ok.gif) | ![Converter with errors](Images/converter_errors.gif) |

Answer any pending questions from the class before moving forward.

---

### 6. Student Do: Understanding Lambdas (15 min)

In this activity, students will inspect the code of a Lambda function to have a better understanding of how it works. Students will create their own Lambda function by importing the provided code and will build a new version of their bot. Be sure to slack out the `lambda_function.py` code to students before starting the activity.

**Instructions:**

* [README.md](Activities/04-Stu_Understanding_Lambdas/README.md)

**Files:**

* [lambda_function.py](Activities/04-Stu_Understanding_Lambdas/Unsolved/lambda_function.py)

---

### 7. Instructor Do: Review Understanding Lambdas (10 min)

**Files:**

* [lambda_function.py](Activities/04-Stu_Understanding_Lambdas/Solved/lambda_function.py)

* [Crypto_Converter export file](Activities/04-Stu_Understanding_Lambdas/Solved/Crypto_Converter_1_6dfe9e0e-82de-4d08-b33b-3bfd1d827672_Bot_LEX_V1.zip)

Open the Lambda function code in VSCode, conduct a facilitated discussion by asking students about their findings, insights, or additional questions after reviewing the provided code. Start with some questions as follows.

* Does anyone has a different idea to organize the function's _building blocks_?

  **Sample Answer:** Maybe we can omit the `parse_float()`, `get_btcprice()` and `validate_data()` helper functions and embed all the functionality on the `convert_usd()` intent handler function.

  **Sample Answer:** We can drop the `dispatch()` function by adding the intents' name validation into the `lambda_handler()` function.

* Do you think we can avoid using the `parse_float()` function?

  **Sample Answer:** Yes, we can do that by simply using the `float()` function.

  **Sample Answer:** Yes, we can avoid defining the `parse_float()` function and use the `float()` function instead, however, having this function returning the value of `nan` for non-numeric values is more secure and eases testing.

* Is there any other way to define the dialog helper functions?

  **Sample Answer:** We could define a function that receives all the data from the current intent and have some nested `if` controlling the kind of dialog and response.

  **Sample Answer:** I think this is a very efficient way to handle the different dialog types.

Slack out the following resources, encourage students to learn more about AWS Lambda and Lex.

* [Lambda Function Input Event and Response Format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html#using-lambda-input-event-format)

* [Amazon Lex and AWS Lambda Blueprints](https://docs.aws.amazon.com/lex/latest/dg/lex-lambda-blueprints.html)

Be sure to answer any reminder question and move to the next activity.

---

### 8. Instructor Do: Testing AWS Lambda Functions (10 min)

In this activity, students will learn how to test AWS Lambda functions that validate Amazon Lex intents.

**Files:**

* [convertOkText.json](Activities/05-Ins_Testing_Lambdas/Solved/convertOkText.json)

* [convertErrAmount.json](Activities/05-Ins_Testing_Lambdas/Solved/convertErrAmount.json)

* [convertErrDate.json](Activities/05-Ins_Testing_Lambdas/Solved/convertErrDate.json)

Explain to students that one of the challenges working with AWS Lambda is dealing with errors, so it is important to know how to test a Lambda function on the AWS Lambda console. For this activity, three test cases are provided.

Explain to students that, in order to test a Lambda function, a `JSON` file should be created to send a testing event to Lambda, the structure of the event depends on the kind of service you are connecting to Lambda. This demo only will cover how to test Amazon Lex intents.

Open the `convertUSD` lambda function on the AWS Lambda console to show students how to create a test case. Click on the _Test_ button on the upper right corner, then choose the _Create new test event_ option and paste the code from the `convertOkText.json` test case.

```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "Crypto_Converter",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "ConvertUSD",
    "slots": {
      "birthday": "1978-12-16",
      "usdAmount": "10"
    },
    "confirmationStatus": "None"
  }
}
```

After pasting the test case code, highlight the following:

* On the `bot` key, the name of the Amazon Lex bot is defined, so students should be sure that this name matches with their bot's name.

* The `$LATEST` it's the default value to use for the `alias` and the `version` keys.

* Since this test event is passed as text, the value of the `outputDialogMode` key is `text`.

* Under the `currentIntent` key, the values of the bot's slots are given, students should be aware that those names match with their slots names.

* This is a test case where the `birthday` and `usdAmount` slots have valid data.

Continue the demo by naming the test `convertOkTest` and click on the _Create_ button to finish.

![Creating a test case](Images/lambda-text-case.png)

Now the name of the new test case appears on the dropdown list next to the _Test_ button, click on the _Test_ button and you can see the test results on the window bellow the Lambda function code.

![Test results](Images/lambda-test-ok.png)

Since this test case has valid data for both slots, comment to students that the test status is `Succeeded` and the execution results show a response with both slots fulfilled with the data passed on the test case.

Show students how to add a new test case, click on the test events dropdown list, and choose the _Configure test events_ option.

![Add new test event](Images/lambda-add-new-test-evet.png)

By default, you will see that the last used test case is selected, notice that the _Edit saved test events_ option is selected, so you can edit the test event.

![Edit saved test event](Images/lambda-add-new-test-default-selection.png)

Choose the _Create new test event_ option, and you will notice that the previous test event remains as a template. Change the value of the `usdAmount` slot to zero to test the amount validation coded on the Lambda. Click on the _Create_ button to continue.

![Create a new test event to cast amount value](Images/lambda-add-convertErrAmount.png)

Select the `convertErrAmount` test on the _Test events_ dropdown list and click on the _Test_ button. Explain to students that the test ran successfully again, however, now Lambda responses with a `ElicitSlot` type of dialog where the message defined on the Lambda can be read. This test event is validating that the incorrect value is caught by the code at the Lambda, and the appropriate new data elicitation is sent to the user via Amazon Lex.

![Running the convertErrAmount test event](Images/lambda-testing-convertErrAmount.png)

Create a final test event, but now to validate what happens when an invalid date of birth is given by the user. Repeat the same process described before to create a new test event. Introduce `2014-12-16` on the `birthday` slot and named the test event as `convertErrDate`.

![Adding the convertErrDate test event](Images/lambda-add-convertErrDate.png)

Execute the `convertErrDate` test, comment to the students that the date validation was successfully corroborated since the `ElicitSlot` dialog type is returned together with the message asking for a different age of birth.

Close the execution results window, and now you will introduce a typo on the code to raise a runtime error. On the `parse_float()` function, delete the closing parenthesis on line 12. Click on the _Save_ button and run any of the testing events.

![Provoking a runtime error](Images/lambda-provoking-runtime-error.png)

After running the test event, explain to students that the test status is `Failed` and that the response contains the error description and the line where the error was detected.

![Runtime error](Images/lambda-runtime-error.png)

Comment to the students that these types of errors are difficult to catch on Amazon Lex. That is why it is important to test Lambdas on the AWS Lambda console before linking the Lambda to the Amazon Lex bot.

Answer any remainder question and continue to the next activity.

---

### 9. Student Do: Buggy Lambdas (10 min)

In this activity, students will test their Lambdas and will practice their ability to find runtime errors. Slack out the instructions to students together with the starter test event.

**Instructions:**

* [README.md](Activities/06-Stu_Buggy_Lambdas/README.md)

**Files:**

* [convertOkTest.json](Activities/06-Stu_Buggy_Lambdas/Unsolved/convertOkTest.json)

---

### 10. Instructor Do: Review Buggy Lambdas (10 min)

**Files:**

* [convertOkTest.json](Activities/06-Stu_Buggy_Lambdas/Solved/convertOkTest.json)

* [convertErrNegAmount.json](Activities/06-Stu_Buggy_Lambdas/Solved/convertErrNegAmount.json)

* [convertOldAge.json](Activities/06-Stu_Buggy_Lambdas/Solved/convertOldAge.json)

Start the review activity by adding the `convertErrNegAmount` and `convertOldAge` test events to your `convertUSD` Lambda, run both tests, and highlight the following:

* The `convertErrNegAmount` behavior is the same as the case when a zero is passed, an `ElicitSlot` type is returned, asking the user for an amount greater than zero.

* The `convertOldAge` text case runs as a correct test event, there is no further validation to prevent a very old person to use the bot.

Open a facilitated discussion with the students by asking the following question:

* How can you prevent a possible fake date of birth from being given to the bot?

  **Sample Answer:** Let us suppose that the average life expectancy is 85 years old, we can add an additional condition to validate that the age is between 21 and 85 years.

  **Sample Answer:** We can unfairly discriminate an older person to use the service, so I would not be worried about this kind of validation.

Continue the discussion by asking for volunteers that want to share their experience finding the bugs provoked by her or his partner.

  **Sample Answer:** It was frustrating since error messages returned by Lambda were no clear.

  **Sample Answer:** It was funny to play becoming a bug detective.

  **Sample Answer:** It was a great opportunity to practice my debugging skills.

Close the discussion by answering any reminder question before moving forward.

---

### 11. BREAK (40 min)

---

### 12. Instructor Do: Custom Slots (10 min)

In this activity, students will learn how to create a custom slot and add it to an Amazon Lex bot intent.

**Files:**

* [Crypto Converter export file](Activities/07-Ins_Custom_Slots/Solved/Crypto_Converter_2_4aefdbf6-55cc-4892-b302-dc428c404e29_Bot_LEX_V1.zip)

Comment to students that it is possible to create custom slot types. This is intended to gather specific data values for a slot, for example, the size of a pizza (personal, small, medium, or large) on a pizza ordering bot. Explain to students that now you will show them how to create a custom slot to allow users to choose the cryptocurrency they want to convert to.

Open the Amazon Lex console and navigate to the `convertUSD` intent editor, on the left side menu, click on the blue plus symbol next to the _Slot types_ option to add a new custom slot type.

![Adding a new slot type](Images/add-slot-type.png)

Next, a popup window will appear, click on the _Create slot type_ option to continue.

![Create a new slot type](Images/create-slot-type.png)

Configure the new slot type as follows:

* **Slot type name:** `CryptoCurrency`
* **Description:** `Available cryptocurrencies to convert.`
* **Slot Resolution:** Choose _Restrict to Slot values and Synonyms_. By selecting this option, the user has to choose only among the available options.
* **Value:** Add three values and synonyms, one per each cryptocurrency, as can be seen below.

Once you are done, click on the _Save slot type_ button.

![Configuring the new slot type](Images/configure-new-slot-type.png)

Come back to the `convertUSD` intent editor, add a new slot named `crypto`, click on the _Slot type_ dropdown list, and you will see your brand new slot type, select `CryptoCurrency` from the list. End the slot configuration by typing `What cryptocurrency do you want to convert to?` on the prompt.

![Add the crypto slot](Images/add-crypto-slot.png)

Explain to the students that now the bot is configured to elicit the `crypto` slot; however, we need to modify the utterances to add a better dialog that includes the new slot.

Modify the utterances to have the _Sample utterances_ like the ones shown below.

![New sample utterances](Images/new-crypto-utterances.png)

Highlight to students that on the new utterances, the word `bitcoin` has been substituted by the slot `crypto` in order to allow users to specify on their dialog what cryptocurrency they want to convert to, for example by typing `I want to convert USD to Ripple`.

Build the bot and test it on the _Test bot_ window. Start with typing the sample utterance `I want to invest in crypto` in order to elicit all the slots as follows.

![Sample utterance 1](Images/custom_slots_1.gif)

Explain to students that, when the `crypto` slot is elicited, only the three options will be valid, however, giving the user the chance to type any cryptocurrency name could be prone to errors, that is why using _Card Slots_ could be useful.

To create a _Card Slot_, click on the gear icon next to `crypto` slot's prompt.

![Create a card slot](Images/create-card-slot.png)

The _Crypto settings_ window will open, scroll down to the _Prompt response cards_ section, and start by adding this URL in the _Image URL_ text field: https://cdn1.iconfinder.com/data/icons/cryptocurrency-set-2018/375/Asset_1480-128.png. Comment to students that this URL should point to a public image that they can store as a public asset on an AWS S3 bucket, for this demo we are using a free public image from [Iconfinder](https://www.iconfinder.com/).

![Add card slot image](Images/add-card-slot-image.png)

Comment to the students that a card slot can have up to five cards; in this demo, we will create one card with three options. Continue by adding the title and subtitle, as is shown below.

* **Tittle:** `Available CryptoCurrencies`
* **Subtitle:** `Choose one crypto to convert`

Next, explain to students that each option will appear as a button on the card, so a tittle should be defined for each one together with a value; the value is taken from the values defined when the custom slot type is created. In this demo, you will see three possible values on the _Button value_ dropdown list as it is shown below. Once you finish, click on the _Save_ button con continue.

![Card slot values](Images/card-slot-values.png)

Click on the _Build_ button, once the build process is done, test your bot on the _Test bot_ window, show to students how the card's options are presented and click on `Ethereum`; as you can see bellow something strange is happening, despite we selected `Ethererum` the bot is converting to `Bitcoin`.

![Sample card slot demo](Images/custo_slots_cards.gif)

**What is happening?** Explain to students that the bot dialog and elicitation process is working perfectly; however, we have to modify the Lambda function to allow the bot to make to correct conversion. This is going to be done in the next activity.

Answer any pending questions before continuing.

---

### 13. Students Do: Crypto Converter (20 min)

In this activity, students will extend their cryptocurrency converter by adding a custom slot to allow users to select between Bitcoin, Ethereum, or Ripple to convert from US Dollars. Also, business logic to identify the cryptocurrency selected by the user and make the conversion will be added to the Lambda function.

**Instructions:**

* [README.md](Activities/08-Stu_Crypto_Converter/README.md)

**Files:**

* [lambda_function.py](Activities/08-Stu_Crypto_Converter/Unsolved/lambda_function.py)

---

### 14. Instructor Do: Review Crypto Converter (10 min)

**Files:**

* [lambda_function.py](Activities/08-Stu_Crypto_Converter/Solved/lambda_function.py)

Start by reviewing the bot configuration. Open the Amazon Lex console, navigate to the `ConvertUSD` intent editor on the `Crypto_Converter` bot and highlight the following:

* As you presented on the previous demo, students should have created a new slot type called `CryptoCurrency` with the following structure:

  ![CrytoCurrency Slot Type](Images/cryptocurrency_slot_type.png)

* The user can use either the value or the synonyms to refer to the cryptocurrencies while talking to the bot.

* Once the new slot type is created, it is possible to add the `crypto` slot to the intent.

* The `crypto` slot is configured to show prompt response cards as follows:

  ![Crypto slot response cards](Images/crypto_slot_response_cards.png)

* The card image should be a public image, it can be stored anywhere on the web; an AWS S3 public asset could be the best option.

Continue to the Lambda function code, open the solution on your AWS Lambda online code editor, and highlight the following:

* There is no need to validate the name of the cryptocurrency since it is not typed by the user.

* On the `get_cryptoprice()` function, the price for each cryptocurrency is retrieved from CoinMarketCap using an URL defined on a `nested-if` structure.

  ```python
  def get_cryptoprice(crypto):
      """
      Retrieves the current price of BTC, ETH or XRP in US Dollars from CoinMarketCap.
      """
      url = ""
      if crypto == "Bitcoin":
          url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
      elif crypto == "Ethereum":
          url = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
      else:
          url = "https://api.coinmarketcap.com/v1/ticker/ripple/"

      response = requests.get(url)
      response_json = response.json()
      price_usd = parse_float(response_json[0]["price_usd"])
      return price_usd
  ```

* To fetch the value of the `crypto` slot, a new variable called `crypto` were defined at the beginning of the `convert_usd()` function.

  ```python
  crypto = get_slots(intent_request)["crypto"]
  ```

* The `get_cryptoprice()` function is used in the `convert_usd()` function to fetch the current price of the selected cryptocurrency, next the conversion to US Dollars is calculated.

  ```python
  # Get the current price of BTC, ETH or XRP in USD and make the conversion from USD.
  crypto_value = parse_float(usd_amount) / get_cryptoprice(crypto)

  crypto_value = round(crypto_value, 4)
  ```

* The fulfillment message is formatted in the `convert_usd()` function to include the name of the selected cryptocurrency dynamically.

  ```python
  # Return a message with conversion's result.
  return close(
      intent_request["sessionAttributes"],
      "Fulfilled",
      {
          "contentType": "PlainText",
          "content": """Thank you for your information;
          you can get {} {} for your {} US Dollars.
          """.format(
              crypto_value, crypto, usd_amount
          ),
      },
  )
  ```

Continue to the Amazon Lex console, test the bot to validate the changes made on Lambda; you should see a dialog as follows.

![Extended Cryto Converter demo](Images/crypto_converter_extended.gif)

Answer any reminder question before moving forward.

---

### 15. Everyone Do: Deploying an Amazon Lex bot to Slack (20 min)

This is a group activity, students will follow you on the process to publish the `Crypto_Converter` bot, and later, you will show them how to deploy the bot as a Slack App.

Follow the next steps, ask your TAs to assist students along with the demo and be sure all the class is following you along the process.

#### Step 1: Publish the Amazon Lex bot

1. Open the Amazon Lex console and navigate to the `Crypto_Converter` bot.

2. Click on the _Publish_ button located at the upper right corner. You should publish your bot before deploying it on any messaging or mobile application.

3. A popup window will appear where you should give a name for your bot's published instance. Name the bot as `CryptoConverterBot` and click on the _Publish_ button to continue.

  ![Publishing a bot](Images/publish-amazon-lex-bot.png)

4. Once the publishing process is finished, you will see the following window. Click on _Close_ to continue.

  ![Publishing bot process done](Images/bot-publishing-done.png)

#### Step 2: Create a Slack Team

Explain to students that, in order to publish the Amazon Lex bot as a Slack App, the first step is to create a Slack Team to deploy the app. Perform the following tasks and be sure students are on track as you move forward.

1. To create a new Slack Team, open your web browser, and navigate to https://slack.com/create. Enter your e-mail address and click on the _Next_ button to continue.

  ![Create Slack worspace - step 1](Images/slack-workspace-1.png)

2. A six-digit verification code will be sent to your e-mail, check your inbox, and type the code in the six boxes to continue.

  ![Create Slack worspace - step 2](Images/slack-workspace-2.png)

3. Once you confirm your six-digit code, you will see the next page where you have to create a Slack Team. Type an original name for your team and click on the _Next_ button to continue.

  ![Create Slack worspace - step 3](Images/slack-workspace-3.png)

4. On the next page, you will be asked for the name of a current project on your team. Type `Crypto Converter Bot` and click on the _Next_ button to continue.

  ![Create Slack worspace - step 4](Images/slack-workspace-4.png)

5. Next, you are asked to invite some people to your team, skip this to continue.

  ![Create Slack worspace - step 5](Images/slack-workspace-5.png)

6. You have finished the Slack Team creation, click on the _See Your Channel in Slack_ button to open your brand new channel.

  ![Create Slack worspace - step 6](Images/slack-workspace-6.png)

#### Step 3: Create a Slack Application

Comment to the students that now, you are going to login into the Slack Api to create a new Slack Application. The Slack Application will be the bridge between Amazon Lex and Slack to allow users to talk to the bot.

1. Open your web browser and navigate to the Slack API Console at http://api.slack.com. Click on the _Start Building_ button to continue.

  ![Create a Slack App - step 1](Images/slack-app-1.png)

2. Type a name for your new app, for this demo, name the app as `Crypto Converter Bot`. From the _Development Slack Workspace_ dropdown list, select the name of the team's workspace you created on **Step 2**. Click on the _Create App_ button to continue.

  ![Create a Slack App - step 2](Images/slack-app-2.png)

3. After you have successfully created the application, Slack displays the Basic Information page for the application.

  ![Create a Slack App - step 3](Images/slack-app-3.png)

4. In the left menu, choose _Bot Users_ and then choose _Add a bot user_.

  ![Create a Slack App - step 4](Images/slack-app-4.png)

5. Configure the new user as follows:

    * Left the default _Display name_ and a _Default username_ values.
    * On the _Always Show My Bot as Online_, choose `On`.
    * Save the changes by clicking on the _Add Bot User_ button.

  ![Create a Slack App - step 5](Images/slack-app-5.png)

6. In the left menu, choose _Interactive Components_. Toggle the _Interactivity_ option to `On` and specify any valid URL in the _Request URL_ textbox. Use https://slack.com to get the verification token that you need in the next step. You will update this URL later. Click on the _Save Changes_ button to continue.

  ![Create a Slack App - step 6](Images/slack-app-6.png)

7. In the left menu, under _Settings_, choose _Basic Information_. Record the following application credentials to be used in the next step. To protect the privacy of your credentials, be sure to regenerate your _Client Secret_ and _Verification Token_ after the class.

    * Client ID
    * Client Secret
    * Verification Token

  ![Create a Slack App - step 7](Images/slack-app-7.png)

#### Step 4: Integrate the Slack Application with the Amazon Lex Bot

Now that you have Slack application credentials, you can integrate the application with your Amazon Lex bot. To associate the Slack application with your bot, we will add a bot channel association in Amazon Lex.

1. Open the Amazon Lex console, select the `Crypto_Converter` bot and navigate to the _Channels_ tab. Choose _Slack_ from the left _Channels_ menu to continue.

  ![Integrating Slack App - step 1](Images/slack-integration-1.png)

2. Configure the _Slack_ channel as follows:

    * **Name:** `CyptoConverterSlackApp`
    * **Description:** `Slack channel for the Crypto Converter bot`
    * **KMS Key:** `aws/lex`
    * **Alias:** `CryptoConverterBot`
    * Type the _Client Id_, _Client secret_, and _Verification Token_, which you recorded in the preceding step. These are the credentials of the Slack application.

  ![Integrating Slack App - step 2](Images/slack-integration-2.png)

3. Click on the _Activate_ button to continue. The console creates the bot channel association and returns two URLs, record them.

    * **Postback URL:** It is the Amazon Lex bot's endpoint that listens to Slack events.
    * **OAuth URL:** It is your Amazon Lex bot's endpoint for an OAuth handshake with Slack.

  ![Integrating Slack App - step 3](Images/slack-integration-3.png)

#### Step 5: Complete Slack Integration

Explain to students that, in this section, you will use the Slack API console to complete the integration of the Slack application.

1. Come back to the Slack API console, in the left menu, choose _OAuth & Permissions_.

  ![Complete Slack integration - step 1](Images/complete-slack-integration-1.png)

2. In the _Redirect URLs section_, click on the _Add a new Redirect URL_ and add the OAuth URL that Amazon Lex provided in the preceding step. Once you typed the URL, click on the _Add_ button to continue and on _Save URLs_.

  ![Complete Slack integration - step 2](Images/complete-slack-integration-2.png)

3. In the _Scopes_ section, you need to add two permissions. In the _Select Permission Scopes_ dropdown list, filter the list with the following text to add the permissions:

    * `chat:write:bot`
  ![Complete Slack integration - step 3a](Images/complete-slack-integration-3a.png)

    * `team:read`
    ![Complete Slack integration - step 3b](Images/complete-slack-integration-3b.png)

    Click on the _Save Changes_ button to continue.

4. In the left menu, choose _Interactive Components_, update the _Request URL_ value to the Postback URL that Amazon Lex provided in the preceding step. Click on the _Save Changes_ button to continue.

  ![Complete Slack integration - step 4](Images/complete-slack-integration-4.png)

5. In the left menu, choose _Event Subscriptions_, configure this feature as follows:

    * Toggle the _Enable events_ option to `On`.

    * Set the _Request URL_ value to the Postback URL that Amazon Lex provided in the preceding step. Once you type it, Slack will verify the URL.
  ![Complete Slack integration - step 5a](Images/complete-slack-integration-5a.png)

    * In the _Subscribe to Bot Events_ section, click on the _Add Bot User Event_ button and filter the list by typing `message.im`. This event will enable direct messaging between the end-user and the Slack bot. Click on the _Save Changes_ button to continue.
    ![Complete Slack integration - step 5b](Images/complete-slack-integration-5b.png)

#### Step 6: Test the Integration Between Amazon Lex and Slack

Congratulate students on reaching this point, this is the final stage on getting Amazon Lex integrated with Slack, and there are just some last final touches to refine. Continue on the Slack API Console as follows.

1. In the left menu, choose _Manage Distribution_ under the _Settings_ option. Click on the _Add to Slack_ button to install the application.

  ![Test integration - step 1](Images/test-slack-integration-1.png)

2. On the next page, you should authorize the bot to respond to messages on the Slack Team you created. Notice that a new user called `@crypto_converter_bot` will be added to your Slack Team. Click on the _Allow_ button to continue.

  ![Test integration - step 2](Images/test-slack-integration-2.png)

3. You are redirected to your Slack team. In the left menu, in the _Apps_ section, choose your bot and engage in a chat with your Slack application, which is linked to the `Crypto_Converter` Amazon Lex bot. Start with the `I want to invest in crypto` sample utterance to test the bot. You should see a dialog like the shown below.

  ![Demo crypto converter bot on Slack](Images/slack-crypto-converter-bot-test.gif)

**Note:** If you do not see your bot, choose the plus icon (+) next to _Apps_ section to search for it.

Ask your TAs to assist students in testing their bots, answer any additional questions before continuing.

---

### 16. Instructor Do: Structured Review (35 min)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
