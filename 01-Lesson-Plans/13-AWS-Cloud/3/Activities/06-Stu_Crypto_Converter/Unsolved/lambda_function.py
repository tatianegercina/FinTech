### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
from botocore.vendored import requests

### Functionality Helper Functions ###
def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")


def get_btcprice():
    """
    Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.
    """
    bitcoin_api_url = "https://api.alternative.me/v2/ticker/bitcoin/?convert=CAD"
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    price_cad = parse_float(response_json["data"]["1"]["quotes"]["CAD"]["price"])
    return price_cad


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Defines an internal validation message structured as a python dictionary.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


def validate_data(birthday, cad_amount, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate that the user is over 18 years old
    if birthday is not None:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        age = relativedelta(datetime.now(), birth_date).years
        if age < 18:
            return build_validation_result(
                False,
                "birthday",
                "You should be at least 18 years old to use this service, "
                "please provide a different date of birth.",
            )

    # Validate the investment amount, it should be > 0
    if cad_amount is not None:
        cad_amount = parse_float(
            cad_amount
        )  # Since parameters are strings it's important to cast values
        if cad_amount <= 0:
            return build_validation_result(
                False,
                "cadAmount",
                "The amount to convert should be greater than zero, "
                "please provide a correct amount in dollars to convert.",
            )

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

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
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

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
def convert_cad(intent_request):
    """
    Performs dialog management and fulfillment for converting from dollars to bitcoin.
    """

    # Gets slots' values
    birthday = get_slots(intent_request)["birthday"]
    cad_amount = get_slots(intent_request)["cadAmount"]

    # Gets the invocation source, for Lex dialogs "DialogCodeHook" is expected.
    source = intent_request["invocationSource"]  #

    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(birthday, cad_amount, intent_request)

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

    # Get the current price of bitcoin in dolars and make the conversion from dollars to bitcoin.
    btc_value = parse_float(cad_amount) / get_btcprice()
    btc_value = round(btc_value, 4)

    # Return a message with conversion's result.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """Thank you for your information;
            you can get {} Bitcoins for your ${} dollars.
            """.format(
                btc_value, cad_amount
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # Get the name of the current intent
    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "convertCAD":
        return convert_cad(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
