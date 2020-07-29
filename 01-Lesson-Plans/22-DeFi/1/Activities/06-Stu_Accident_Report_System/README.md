# Building the Accident Report System

In this activity, you will be building the Accident Report System command line interface that will upload and pin accident reports to IPFS via Pinata, permanently storing them on-chain by using the `reportAccident` function on your `CryptoFax` contract.

## Instructions

* Remember your deployed `CryptoFax` contract from earlier, before we can use our new Accident Report dApp we have to make sure that the contract is deployed and that we have registered a new vehicle with the `registerVehicle` function.

* Make sure you have the `python-dotenv` package installed. This can be done by running the following command:

```bash
pip install python-dotenv
```

* Create a new working directory called `accident` and `cd` into it. You will need to stay in this directory for the rest of this activity.

* Create a file called `.env` and populate it with the [starter code](Unsolved/.env).

  * Navigate to your [Pinata Account Page](https://pinata.cloud/account) and copy the API Key and Secret API Key into the corresponding environment variables in the `.env` file.

* In Remix, open your `CryptoFax` contract, navigate to the compile tab, and copy the ABI:

  ![CryptoFax ABI](Images/cryptofax-abi.png)

* Create a new file called `CryptoFax.json` and paste the ABI into the file, and save.

* Copy the deployed address for your `CryptoFax` contract (on Ganache) from the `Deploy` tab. Feel free to deploy a fresh contract, but make sure to run the `registerVehicle` function at least once to create a token to work with!

* Using the [starter code](Unsolved/crypto.py), create a file called `crypto.py`.

* In this file, you will need to import `web3.auto`, load the environment variables using `dotenv`, and import the `Path` library from `pathlib` to fetch our ABI later.

  * Add the web3.py import:

    ```python
    from web3.auto import w3
    ```

  * Import the environment variables automatically:

    ```python
    from dotenv import load_dotenv

    load_dotenv()
    ```

  * Import `Path` to work with the ABI later:

    ```python
    from pathlib import Path
    ```

  * Organize your imports, then move on. Your `headers` object should now properly populate with the variables you defined in `.env`.

  * In the `initContract` function, you will need to return the web3 contract object that will allow you to interact with the `CryptoFax` contract on-chain.

    * Open the JSON file:

      ```python
      with open(Path("CryptoFax.json")) as json_file:
        abi = json.load(json_file)
      ```

    * Then, return the contract object by using something like:

      ```python
      return w3.eth.contract(address=os.getenv("CRYPTOFAX_ADDRESS"), abi=abi)
      ```

      This will use the `CRYPTOFAX_ADDRESS` and its ABI to initialize a web3 contract object that points to `CryptoFax`.

  * In the `pinJSONtoIPFS` function, you will need to create a `POST` request to the pinJSONtoIPFS endpoint on Pinata. Use the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS) to find the endpoint's url.

    * The request should be formatted something like:

      ```python
      r = requests.post(
        "ENDPOINT_GOES_HERE", data=json, headers=headers
      )
      ```

* `crypto.py` should now be finished. Create a new file called `accident.py` and populate it with the [starter code.](Unsolved/accident.py).

  * At the top of the file, below the imports, create the `cryptofax` contract object using the `initContract` function from `crypto`.

    ```python
    cryptofax = initContract()
    ```

  * In the `createAccidentReport` function, you will need to fetch user data by using the `input` function in Python. For example:

    ```python
    time = input("Date of the accident: ")
    ```

    * Repeat the same process for the `description` and `token_id` variables. Make sure to convert the input for `token_id` to a number using the `int()` function in Python.

  * Pass the `time` and `description` variables to the `convertDataToJSON` function. Store the result in `json_data`, then pass `json_data` to the `pinJSONtoIPFS` function and save that as `report_uri`. Return the `token_id` and `report_uri` variables.

  * In the `reportAccident` function, you will generate the transaction that talks to the `CryptoFax` contract and return the transaction receipt.

    ```python
    tx_hash = cryptofax.functions.reportAccident(token_id, report_uri).transact(
        {"from": w3.eth.accounts[0]}
    )
    ```

    * Save the transaction hash as `tx_hash`. Make sure to specify the accounts using the `w3.eth.accounts` array, which uses the Ganache accounts.

    * Next, wait for the transaction receipt, then return it:

      ```python
      receipt = w3.eth.waitForTransactionReceipt(tx_hash)
      return receipt
      ```

  * In the `getAccidentReport` function, you will establish an event filter that filters `Accident` events against a specified `token_id`. Your event filter should look something like:

    ```python
    accident_filter = cryptofax.events.Accident.createFilter(
        fromBlock="0x0", argument_filters={"token_id": token_id}
    )
    ```

    * Save the filter as `accident_filter`, then return all of the entries by using the `accident_filter.get_all_entries()` function:

      ```python
      return accident_filter.get_all_entries()
      ```

* Almost there! All you need to do is put the pieces together inside of the `main` function.

* Start with the `report` flow.

    * Below the check for the first argument being the string `report`, create an accident report:

      ```python
      token_id, report_uri = createAccidentReport()
      ```

  * Then, store the receipt, and pretty print the results after.

    ```python
    receipt = reportAccident(token_id, report_uri)
    ```

* The `get` flow is even simpler.

  * Below the second `if` statement that checks if the first argument is the string `get`, and below the parsing of the `token_id` from the next argument, fetch the `Cars` struct from the main `cars` public mapping:

    ```python
    car = cryptofax.functions.cars(token_id).call()
    ```

  * Then, you will need to fetch the events corresponding with that `token_id`:

    ```python
    reports = getAccidentReports(token_id)
    ```

  * Make sure to pretty print the results. The `Cars` struct will return as an array, with each value that you set in the struct being the index. For instance, `cars[0]` will return the VIN, and `cars[1]` will return the `accidents` number from the struct.

* Test out your accident report system by navigating to the terminal, `cd`ing into the `accident` folder workspace, and running the following commands:

  ```bash
  python accident.py report
  ```

  * This command should ask a series of questions, then return an IPFS hash and a print a transaction receipt.


  ```bash
  python accident.py get 1
  ```

  * This command will fetch all `Accident` events using the `token_id` of `1`. Make sure this number matches the `token_id` that you made an accident report on.

* After you have verified that you can fetch this metadata from your CLI, check out your [Pinata Pin Explorer](https://pinata.cloud/pinexplorer) to see what was uploaded to IPFS.

## Challenge

* Set the `name` of each pin in Pinata's API by adding a field called `name` inside a `pinataMetadata` object for easy access by following the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS). You will need to add the `pinataMetadata` object that contains the `name` key next to the `pinataOptions` (not within it!).

## Hints

* Visit your [Pinata Account Page](https://pinata.cloud/account) to fetch your API keys and set them in the `.env` file.

* For more information on creating event filters in `web3.py`, visit the [createFilter](https://web3py.readthedocs.io/en/stable/contracts.html#web3.contract.Contract.events.your_event_name.createFilter) web3 documentation.

* To get more details about how `web3.auto` connects to networks, visit the [How Automated Detection Works](https://web3py.readthedocs.io/en/stable/providers.html#how-automated-detection-works) web3 documentation.
