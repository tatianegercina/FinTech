import sys
from crypto import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint

# @TODO: Initialize cryptofax contract object using initContract


def createAccidentReport():
    # @TODO: Input from the user various details to upload, like "time" and "description" and the "token_id" to match against
    time =
    description =
    token_id = # Convert the user input to a number using int()

    json_data =
    report_uri =

    # convert the data collected to JSON, then return the token_id and the IPFS URI that pinJSONtoIPFS returns

    return token_id, report_uri


def reportAccident(token_id, report_uri):
    # @TODO: create a reportAccident transaction using cryptofax contract and return the tx receipt (make sure to set a 'from' account)


def getAccidentReports(token_id):
    # @TODO: create an Accident filter, filtering against token_id, and return all entries


# sys.argv is the list of arguments passed from the command line
# sys.argv[0] is always the name of the script
# sys.argv[1] is the first argument, and so on
# For example:
#        sys.argv[0]        sys.argv[1]    sys.argv[2]
# python accident.py        report
# python accident.py        get            1
def main():
    if sys.argv[1] == "report":
        # @TODO: collect token_id, report_uri from createAccidentReport
        # call reportAccident and pretty print the results


    if sys.argv[1] == "get":
        token_id = int(sys.argv[2]) # fetches token_id from next argument and converts the string input to number

        car = cryptofax.functions.cars(token_id).call()
        reports = getAccidentReports(token_id)

        pprint(reports)
        print("VIN", car[0], "has been in", car[1], "accidents.")


main()
