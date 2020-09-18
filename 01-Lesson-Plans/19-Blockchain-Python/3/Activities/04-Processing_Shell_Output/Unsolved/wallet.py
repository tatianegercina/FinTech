import subprocess
import json

command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

# @TODO: call hd-wallet-derive from a subprocess, store stdin in a variable, and print it
