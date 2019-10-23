from bit import wif_to_key

key = wif_to_key("")

# replace with student addresses
addresses = ["", ""]

outputs = []

for address in addresses:
    outputs.append((address, 0.001, "btc"))

print(key.send(outputs))
