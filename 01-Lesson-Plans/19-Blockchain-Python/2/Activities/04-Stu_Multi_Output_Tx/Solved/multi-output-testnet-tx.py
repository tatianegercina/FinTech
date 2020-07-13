from bit import wif_to_key

key = wif_to_key("")

# replace with different addresses
addresses = [
    "0xc3879B456DAA348a16B6524CBC558d2CC984722c",
    "0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5",
]

outputs = []

for address in addresses:
    outputs.append((address, 0.001, "btc"))

print(key.send(outputs))
