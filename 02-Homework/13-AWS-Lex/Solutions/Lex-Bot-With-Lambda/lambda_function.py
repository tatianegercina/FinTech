### Required Libraries ###
import requests
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

### API Keys ###
iex_key = "pk_a04696c8c38545a082a9d19e90b57228"

### Functionality Helper Functions ###
def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float("nan")

def get_retirement_date(age):
    """
    Calculates the retirement date and the years to retirement based on
    the current age of the user and a default retirement age of 65 years.
    """

    years_to_retirement = 65 - age
    retirement_date = datetime.now() + relativedelta(years=years_to_retirement)

    return {
        "retirement_date": retirement_date,
        "years_to_retirement": years_to_retirement
    }

def get_ticker_prices(ticker):
    """
    Retrieves one year old historical prices for the ticket based on the current date.
    """

    # Define API endpoint
    url = "https://cloud.iexapis.com/stable/stock/{}/chart/1y?token={}".format(
        ticker, iex_key)

    # Retrieve historical prices data
    data = requests.get(url).json()

    # Create response DataFrame taking only the date and the close price
    df = pd.DataFrame([{"date": price["date"], "close_"+ticker: price["close"]}
        for price in data])

    # Define DataFrame's index
    df.set_index("date", inplace=True)

    return df

def monte_carlo(age, investment_amount, risk_level):
    """
    Calculates the cumulative returns for the retirement plan running
    a Monte Carlo simulation.
    """

    # Gets retirement information
    retirement_info = get_retirement_date(age)

    # Fetch tickers data
    spy_data = get_ticker_prices("spy")
    agg_data = get_ticker_prices("agg")
    tickers_data = pd.merge(spy_data, agg_data, on="date")

    # Calculate the daily roi for the stocks
    daily_returns = tickers_data.pct_change()



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


def validate_data(age, investment_amount, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate the retirement date based on the user's age.
    # An age of 65 years is considered by default.
    if age is not None:
        age = parse_int(age)  # Since parameters are strings is important to cast values
        if age < 0:
            return build_validation_result(
                False,
                "age",
                "Your age is invalid, can you provide an age greater than zero?",
            )
        elif age >= 65:
            return build_validation_result(
                False,
                "age",
                "The maximum age to contract this services is 64, "
                "can you provide an age between 0 and 64 please?",
            )

    # Validate the investment amount, it should be >= 5000
    if investment_amount is not None:
        investment_amount = parse_int(investment_amount)
        if investment_amount < 5000:
            return build_validation_result(
                False,
                "investmentAmount",
                "The minimum investment amount is $5,000 USD, "
                "could you please provide a greater amount?",
            )

    return build_validation_result(True, None, None)


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
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)

        validation_result = validate_data(age, investment_amount, intent_request)
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
