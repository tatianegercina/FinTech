### 8. Instructor Do: The Accident Report System (15 min) (Critical)

Now that students understand that IPFS is a content-routed system that works against hashes instead of IP addresses, it's time to put the systems together to make an Accident Report System.

In this activity, you will demonstrate uploading a sample "accident report" in JSON format to IPFS via the Pinata API, then permanently record the report's IPFS URI to the blockchain via the `reportAccident` function on the `CryptoFax` contract using a transaction generated with Web3.py.

**Files:**

* [crypto.py (web3.py + ipfs functionality)](Activities/08-Ins_Filters_Web3_IPFS/Solved/crypto.py)

* [accident.py (accident report system)](Activities/08-Ins_Filters_Web3_IPFS/Solved/accident.py)

* [CryptoFax.json (contract ABI, pasted from your compiled contract in Remix)](Activities/08-Ins_Filters_Web3_IPFS/Solved/CryptoFax.json)

First, create a new working directory called `accident`, and `cd` into it:

```bash
mkdir accident
cd accident
```

Create a file called `.env`. This is where we will store all of the environment variables needed in our Accident Report dApp.

```env
PINATA_API_KEY=
PINATA_SECRET_API_KEY=
WEB3_PROVIDER_URI=http://127.0.0.1:8545
CRYPTOFAX_ADDRESS=
```

* We will need to use our `.env` file to store our Pinata API credentials, as well as point Web3.py to our local Ganache chain via the `WEB3_PROVIDER_URI` variable.

* We also need to store the address of the `CryptoFax` contract we deployed here.

Fetch your Pinata API credentials by navigating to your [Pinata Account Page](https://pinata.cloud/account) and copying them into the `.env` file.

Paste the address of the deployed `CryptoFax` contract into the `CRYPTOFAX_ADDRESS` variable.

Next, create a file called `crypto.py`. This is where we will be writing the functions for uploading to IPFS via Pinata and initializing our contract via its ABI.

In this file, you will need to import the environment variables via the `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

* This will now load the previously defined environment variables. The `python-dotenv` package automatically imports the environment variables from a `.env` file in your project directory.

*Note:* This requires the `python-dotenv` package for importing private keys and other environment variables. You may need to install it by using:

```bash
pip install python-dotenv
```

Now it's time to setup a `POST` request to the Pinata API that will pin arbitrary JSON data to IPFS.

First, import the `requests` library, as well as `json` and `os`:

```python
import requests
import json
import os

from dotenv import load_dotenv
```

Now, its time to set the request headers that Pinata expects. Open up the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS) for the endpoint `pinJSONToIPFS`.

![Pinata Headers](Images/pinata-headers.png)

* As you can see, the endpoint is `https://api.pinata.cloud/pinning/pinJSONToIPFS`, and we need to set the following headers:

  * `Content-Type` which is going to be `application/json` to specify that we're sending JSON.

  * `pinata_api_key` from our personal account.

  * `pinata_secret_api_key` from our personal account.

* Essentially all we need to do is setup an object with these headers for later, then create a function that sends a `POST` request to that endpoint, with the JSON data that we want to pin to IPFS.

Below your imports, define the following variable:

```python
headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

* This object will now contain the keys that we defined in our `.env` file previously, and can be used as the request's header when sending JSON to IPFS with our account.

Next, define a function called `pinJSONToIPFS`, which will `POST` to the `pinJSONToIPFS` Pinata endpoint.

First, double check the response that Pinata will send back when posting to the endpoint by scrolling down to the `Response` section on the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS):

![Pinata Response](Images/pinata-response.png)

* As you can see, it will return a JSON object that will contain a key called `IpfsHash` that returns the IPFS hash of the data we send, that we can use as a URI later.

```python
def pinJSONtoIPFS(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers
    )
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"
```

* In this request, we are simply taking in some JSON object as input, then sending a `POST` request to the `pinJSONToIPFS` endpoint on Pinata. We use the headers defined above to authorize our request.

* Then, we return the `IpfsHash` value from the JSON response that Pinata defines inside of an `f` string. The final output is an IPFS URI, formatted like `ipfs://some_hash_here`.

Up to this point, this process should be pretty familiar. The last Pinata related item we need to take care of is a function called `convertDataToJSON` that will take our user input and convert it to a JSON object formatted in a way that allows us to set some options in the Pinata API:

```python
def convertDataToJSON(time, description):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": {
            "name": "Example Accident Report",
            "description": description,
            "image": "ipfs://bafybeihsecbomd7gbu6qjnvs7jinlxeufujqzuz3ccazmhvkszsjpzzrsu",
            "time": time,
        },
    }
    return json.dumps(data)
```

* In this function, we are simply taking in a `time` and `description` that we'll accept as user input later, then setting up a dictionary called `data` that contains a few fields.

* The first field, `pinataOptions`, tells the API to use `CIDv1` as the IPFS URL format. This just simply means to use the latest version of the way that IPFS generates the final address that allows for more metadata to be encoded, versus using `CIDv0` which are the shorter, case-sensitive URIs that IPFS originally used.

* `pinataContent` contains the object that will be pinned to IPFS by Pinata. Only what is in this field will be uploaded to IPFS.

* Finally, we are simply converting the `data` dictionary into a JSON string by using `json.dumps(data)`. The `json.dumps` function takes in a Python dictionary and outputs a compatible JSON `string`. Remember, JSON stands for `JavaScript Object Notation`. JSON originally came from JavaScript, and is used in many other systems, but Python needs to convert the way its stores data in dictionaries into the JSON format.

Now it's time to setup the functions we need to setup our `CryptoFax` contract object in Python using `web3.py`.

Before that, we need to actually get our contract's ABI. Hop over to Remix, make sure you have `CryptoFax` selected, head to the compile tab, and copy the ABI:

![CryptoFax ABI](Images/cryptofax-abi.png)

Paste this into a new file called `CryptoFax.json`. Make sure it is in the same working directory as the `crypto.py` and `.env` files.

Next, in `crypto.py`, add the following imports:

```python
from pathlib import Path

from web3.auto import w3
```

* Pathlib will be used to fetch our `CryptoFax.json` ABI.

* Web3.py will accept this ABI, plus the address we defined in our `.env` file, and output a contract object that we can use to interact with the `CryptoFax` contract.

* Since we configured `WEB3_PROVIDER_URI` in `.env`, `web3.auto` will automatically recognize the Ganache network and automatically connect and use the same accounts that Ganache generates. No need to work with private keys when using `web3.auto` and Ganache!

Now, create one last function in `crypto.py`:

```python
def initContract():
    with open(Path("CryptoFax.json")) as json_file:
        abi = json.load(json_file)

    return w3.eth.contract(address=os.getenv("CRYPTOFAX_ADDRESS"), abi=abi)
```

* This function opens up the `CryptoFax.json` ABI and converts it to a JSON object. Then, it returns a contract object using the `CRYPTOFAX_ADDRESS` we defined in our environment, and the ABI object. This is all we need to create the object we need to interact with our contract.

At this point, your code should match the provided [crypto.py](Activities/08-Ins_Filters_Web3_IPFS/Solved/crypto.py).

Finally, it's time to build the rest of the Accident Report System.

We'll need to create one more file called `accident.py`.

* `accident.py` is going to be a quick command line interface between the person reporting the accident, the Pinata API, and the final transaction sent to the contract.

* The flow of the application will start by asking the user `When did the accident occur?` and for a `Description of the accident`, and the `Token ID` associated with the report.

* Next, it will take these three variables, `time`, `description`, and `token_id` and upload the report to IPFS in JSON format. Finally, it will create a transaction that will `emit` an `Accident` event on the contract, passing in the `report_uri` (the URL of the report on IPFS) and `token_id`, permanently recording that event on the blockchain.

In this file, import the following:

```python
from crypto import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint
```

* We're importing these functions individually, as we won't be using all of the imports in `crypto`, like `json` and `os` and we don't want to pollute our import namespace.

* `pprint` will be used to pretty-print our transaction receipts later.

Below the imports, add the following global variable:

```python
cryptofax = initContract()
```

* We can use this object to interact with our contracts functions and events later.

Create a new function to create the accident report:

```python
def createAccidentReport():
    time = input("Date of the accident: ")
    description = input("Description of the accident: ")
    token_id = int(input("Token ID: "))

    json_data = convertDataToJSON(time, description)
    report_uri = pinJSONtoIPFS(json_data)

    return token_id, report_uri
```

* In this function, we are taking in the three variables as user input. We are also making sure to convert the `token_id` into a number.

* Then, we convert that data into the JSON object we want to send to Pinata via the `convertDataToJSON` function.

* We capture the final IPFS URI from our `pinJSONToIPFS` function, passing in the JSON data we want to upload, and return the `token_id` and `report_uri` variables.

Next, we'll need to create the function that will etch the event to the blockchain:

```python
def reportAccident(token_id, report_uri):
    tx_hash = cryptofax.functions.reportAccident(token_id, report_uri).transact(
        {"from": w3.eth.accounts[0]}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt
```

* In this function, we are calling the `reportAccident` function by using `cryptofax.functions.reportAccident`, and passing in our `token_id` and `report_uri`. This should match the parameters we set in our Solidity code.

* The `.transact` call creates and sends the transaction in one function, but we need to make sure to set our default `from` user to something like `w3.eth.accounts[0]`. This `accounts` array comes from the accounts that Ganache generates for you, so feel free to use any of them, or reference one specifically by index.

* Lastly, we wait for the transaction receipt from our chain and return it.

At this point, all we need to to is collect the data from the command line:

```python
def main():
    token_id, report_uri = createAccidentReport()

    receipt = reportAccident(token_id, report_uri)

    pprint(receipt)
    print("Report IPFS Hash:", report_uri)


main()
```

* What this main function does is simply collect the `token_id` and `report_uri` from the `createAccidentReport` function, pass the info to `reportAccident`, and pretty prints the Ethereum transaction receipt and the IPFS Hash of the report.

Feel free to demonstrate a sample report. Make sure you have previously called the `registerVehicle` function and have at least one Car Token on-chain and have its `token_id` available.

* What if we wanted to fetch all of the `Accident` report events relating to our `token_id`?

Simply add the following function:

```python
def getAccidentReports(token_id):
    accident_filter = cryptofax.events.Accident.createFilter(
        fromBlock="0x0", argument_filters={"token_id": token_id}
    )
    return accident_filter.get_all_entries()
```

* This function takes in a `token_id`, then creates a `Filter` on the `Accident event` available in the contract object. The filter captures from block `0x0` (genesis), to the current block, and makes sure that the `token_id` matches the argument parameters.

* Then, it returns all of the entries the filter found, by calling `accident_filter.get_all_entries()`.

We can make this a simple command line interface by importing `sys`, and parsing the arguments from the command line and modifying our `main` function:

```python
import sys

...

def main():
    if sys.argv[1] == "report":
        token_id, report_uri = createAccidentReport()

        receipt = reportAccident(token_id, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)

    if sys.argv[1] == "get":
        token_id = int(sys.argv[2])

        car = cryptofax.functions.cars(token_id).call()
        reports = getAccidentReports(token_id)

        pprint(reports)
        print("VIN", car[0], "has been in", car[1], "accidents.")
```

* `sys.argv` is the list of arguments passed from the command line. This is a universal concept in most general purpose programming languages. This is the list that other programs use to parse out the arguments you send them, like `--help` or `--port`.

* In Python, `sys.argv[0]` is always the name of the script. `sys.argv[1]` is the first argument, and so on.

For example:

```
       sys.argv[0]        sys.argv[1]    sys.argv[2]
python accident.py        report
python accident.py        get            1
```

* We can use this to pass the word `get` as the first argument, and a `token_id` as the second.

* Then, we simply check if the first argument is a `report` or a `get`, and proceed accordingly.

* In our `get` flow, we simply collect the `token_id`, then fetch the `Car` struct from the `cars` mapping to get details from the contract, then we fetch the accident reports from our event filter using `getAccidentReports`, and pretty-print the results.

At this point, your code should match the provided [accident.py](Activities/08-Ins_Filters_Web3_IPFS/Solved/accident.py).

Test out the system by creating an accident report, and then fetching it using the following commands (you can replace the `token_id`):

```bash
python accident.py report
python accident.py get 1
```

Voila! A complete vehicle accident report system that permanently stores accident reports to the blockchain and IPFS. Now it's time for the students to build the same system.
