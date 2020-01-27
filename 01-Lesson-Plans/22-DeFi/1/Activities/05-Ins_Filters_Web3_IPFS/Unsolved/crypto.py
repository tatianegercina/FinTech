import requests
import json
import os

# @TODO: Import web3.auto to use Ganache via the WEB3_PROVIDER_URI env variable

# @TODO: Load environment via dotenv

# @TODO: Import Path from pathlib and use it to fetch the contract ABI json

headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}


def initContract():
    # @TODO: Fetch the contract abi from the CryptoFax.json, initialize and return the contract object from w3.eth.contract


def convertDataToJSON(time, description):
    data = {
        "pinataOptions": {"cidVersion": 1}, # Needed to return new IPFS urls that have better support for IPFS companion
        "pinataContent": { # This object should contain the JSON you want to pin to IPFS
            "name": "Example Accident Report",
            "description": description,
            "image": "ipfs://bafybeihsecbomd7gbu6qjnvs7jinlxeufujqzuz3ccazmhvkszsjpzzrsu",
            "time": time,
        },
    }
    return json.dumps(data)


def pinJSONtoIPFS(json):
    # @TODO: Post the JSON object to Pinata according to their API spec
    r =
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"
