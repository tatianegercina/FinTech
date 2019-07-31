### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


def get_investment_recommendation(risk_level):
    """
    Returns an initial investment recommendation based on the risk profile.
    """
    risk_levels = {
        "none": "100% Bonds, 0% equities",
        "very low": "80% Bonds, 20% equities",
        "low": "60% Bonds, 40% equities",
        "medium": "40% Bonds, 60% equities",
        "high": "20% Bonds, 80% equities",
        "very high": "0% Bonds, 100% equities",
    }

    return risk_levels[risk_level.lower()]


def validate_data(age):
    """
    Validates the data provided by the user.
    """

    # Validate the retirement date based on the user's age.
    # An age of 65 years is considered by default.
    if age < 0:
        return build_validation_result(
            False,
            "age",
            "Your age is invalid, Can you try an age greater than zero?",
        )


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)

        validation_result = validate_data(age)
        if not validation_result["isValid"]:
            slots[validation_result["violetedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Pass the user's name back through session attributes to be used
        # in various prompts defined on the bot model.
        output_session_attributes = intent_request["sessionAttributes"]
        if first_name is not None:
            output_session_attributes["Name"] = first_name

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the initial investment recommendation
    initial_recommendation = get_investment_recommendation(risk_level)

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """{} thank you for your information;
            based on the risk level you defined, my recommendation is to split your investment portfolio as follows: {}
            """.format(
                first_name, initial_recommendation
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "RecommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
