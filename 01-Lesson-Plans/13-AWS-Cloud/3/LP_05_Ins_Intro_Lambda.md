### 5. Instructor Do: Intro to AWS Lambda (10 mins)

This activity will introduce AWS Lambda to students, also students will learn how they can integrate Lambda functions into an Amazon Lex bot. The full code of the lambda function could be found on the [_Solved_ directory](Activities/05-Ins_Intro_Lambda/Solved/lambda_function.py).

**Files:**

* [Lesson 13.3 Slides](#)

* [lambda_function.py](Activities/05-Ins_Intro_Lambda/Solved/lambda_function.py)

Start the activity by opening the lesson slides, navigate to the _Intro to AWS Lambda_ section and highlight the following:

* Sometimes AWS Lambda is seen as a webservice or and API since it runs code remotely, however AWS Lambda is a serverless technology where you just upload your code and Lambda takes care of everything.

* In general terms. _serverless_ means that you don't have to be worried about any servers configuration nor administration.

* AWS Lambda can have your code to automatically triggered from other AWS services or call it directly from any web or mobile app.

* We are going to use AWS Lambda by triggering code from an Amazon Lex Bot.

* AWS Lambda enhances chatbots by combining the NLP capabilities of Amazon Lex to understand human speech, with the possibility of running code tu fulfill user's requests, for example, booking a hotel room, making a wire transfer, or providing financial advice about an investment portfolio.

* AWS Lambda interacts with other AWS services by processing events messages in `JSON`, every AWS Services has its specific format.

* Amazon Lex "talks" to AWS Lambda to perform initialization and validation, fulfillment, or both.

Explain students that in this demo, you will show how to process `ElicitSlots`, `Delegate` and `Close` response events.

Close the slides and log-in into the AWS Management Console using your IAM administrator user, once you are logged-in, type `Lambda` into the _AWS services_ search box and click on _Lambda_ to open the AWS Lambda console.

![Search for AWS Lambda service on the AWS Management console](Images/search-lambda-service.png)

In the AWS Lambda console, click on _Functions_ on the left side menu; continue by clicking on the _Create function_ button.

![AWS Lambda console](Images/aws-lambda-console.png)

On the _Create function_ page, select the _Author from scratch_ option, fill-out the following information and click on the _Create function_ button:

* **Function name:** `convertUSD` (This is the name to identify our new Lambda function)
* **Runtime:** `Python 3.7`

![Create function page](Images/aws-lambda-create-function.png)

Explain students that now AWS will create the `convertUSD` lambda function, it takes few seconds. Once created, you will see the following page.

![convertUSD function created](Images/convertUSD-created.png)

Scroll-down to the _Function code_ section, explain students that this code is a starter `Hello World` example. Highlight that a lambda function has a main events handler, its goal is to manage all the incoming messages and dispatch them depending on the business logic defined.

* We will use the `lambda_handler` to route the incoming requests based on user's intents captured by the Amazon Lex bot.

![Function code section](Images/convertUSD-function-code.png)

Open [lesson slides](#) and show students the anatomy of the lambda function you are going to use. Comment to students that this code can be used as a boilerplate template to code business logic for extending Amazon Lex bots functionality.

![Lambda function anatomy](Images/lambda-function-anatomy.png)

Explain to students that the lambda function contains six general building blocks, briefly present these blocks, and open the [`lambda_function.py` script](Activities/05-Ins_Intro_Lambda/Solved/lambda_function.py) on VSCode by highlighting the following:

1. **Required Libraries:** This section contains all the necessary libraries to code the business logic on the lambda functions, despite AWS Lambda supports Python, the runtime doesn't support some common packages such as `pandas`, `numpy` or `requests`, so alternative packages should be used or installed. In this demo we take the current price of bitcoin making an API call to [CoinMarketCap](https://api.coinmarketcap.com/v1/ticker/bitcoin/), so the `requests` library is imported from the [`botocore` package](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html). A complete list of the python modules available on AWS Lambda can be found [here](https://gist.github.com/gene1wood/4a052f39490fae00e0c3).

2. **Functionality Helper Functions:** These functions implement business logic and data validation. In this demo we have four helper functions.

    * `parse_float()`: This function securely parses a non-numeric value to float.

    * `get_btcprice()`: Retrieves the current price of bitcoin in US Dollars from CoinMarketCap.

    * `build_validation_result()`: This function defines an internal validation message structured as a python dictionary.

    * `validate_data()`: This function validates the data provided by the user across the intent's dialog on Amazon Lex according to the business logic. In this demo there are only to rules: (1) the user should be at least 21 years old (2) the amount in US Dollars to convert must be greater that zero.

Explain students that the `validate_data()` function uses the `build_validation_result()` function to return a validation result message. In this demo if the user's age is less than 21 or the amount to convert is less than 0, a `False` result is returned, otherwise a `True` result is returned.

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

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)
```

3. **Dialog Actions Helper Functions:** These functions handle the input and response events data from the "conversation" between Amazon Lex and AWS Lambda. The `get_slots()` function simply fetches all the slots and their values from the current intent. The `elicit_slot()`, `delegate()` and `close()` functions, construct response messages structured as a valid JSON Lex event. The full structure of event data that Amazon Lex exchanges with a Lambda function can be reviewed [here](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html).

4. **Intents Handlers:** The core business logic is coded into an intent handler. An intent handlers is a function that implements the functionality that is willing to fulfill the user's intent.

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

Comment to students that once the conversation between the user and the bot ends, the current price of bitcoin in US Dollars is fetched using the `get_btcprice()` function, the conversion from USD to BTC in done and the `close()` function is called to return a `Fulfilled` event message to Lex.

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

A pop-window asking you for permissions to your Lambda Function will appear next, click on the _Ok_ button to continue. Explain students that this permission is needed to allow the communication between the bot and Lambda.

![Lambda permission prompt](Images/lambda-permissions-prompt.png)

Scroll down to the _Confirmation prompt_ section and disable the checkbox, continue by opening the _Fulfillment_ section and choose the _AWS Lambda function option_, select the `convertUSD` Lambda and the `Latest` version. Click on the _Build_ button on the upper right corner and you're done, now the bot is connected to Lambda to control the user's intent.

![Confirmation and fulfillment configuration](Images/lambda-confirmation-fulfillment.png)

Test the Lambda powered bot with some of the sample utterances, you should have a final conversation as it's shown bellow.

| _Bot demo conversation with valid user's data_ | _Bot demo conversation with invalid user's data_ |
| --- | ---|
| ![Converter without errors](Images/converter_ok.gif) | ![Converter with errors](Images/converter_errors.gif) |

Answer any pending questions from the class before moving forward.
