import subprocess
import json
import os

from constants import BTC, BTCTEST, ETH
from pprint import pprint

from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware

# connect Web3
w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER', 'http://localhost:8545')))

# enable PoA middleware
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

# set gas price strategy to built-in "medium" algorithm (est ~5min per tx)
# see https://web3py.readthedocs.io/en/stable/gas_price.html?highlight=gas
# see https://ethgasstation.info/ API for a more accurate strategy
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

# including a mnemonic with prefunded test tokens for testing
mnemonic = os.getenv("MNEMONIC", "later trouble diary worry divide quantum shift term pepper glass gown rotate")

def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    p = subprocess.Popen(
        f"./derive -g --mnemonic='{mnemonic}' --coin={coin} --numderive={depth} --format=json",
        stdout=subprocess.PIPE,
        shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return json.loads(output)

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    if coin == ETH:
        value = w3.toWei(amount, "ether") # convert 1.2 ETH to 120000000000 wei
        gasEstimate = w3.eth.estimateGas({ "to": to, "from": account.address, "amount": value })
        return {
            "to": to,
            "from": account.address,
            "value": value,
            "gas": gasEstimate,
            "gasPrice": w3.eth.generateGasPrice(),
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": w3.net.chainId
        }
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    if coin == ETH:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)

coins = {
    ETH: derive_wallets(coin=ETH),
    BTCTEST: derive_wallets(coin=BTCTEST),
}

pprint(coins)
