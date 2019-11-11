import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = os.getenv("PRIVATE_KEY")

print(private_key)
