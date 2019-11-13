from bit import wif_to_key

# replace with your private key (do not send this to students)
key = wif_to_key("cQpxiiQHueFJgK3EaHKvDqAE7cm8gWKMrSj3ZPMMHkDr7v5gbkQW")

# replace with student addresses
addresses = ["mn9CfkoXJpkCMkPbRcBfUphso7QaDmBmgz", "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"]

outputs = []

for address in addresses:
    outputs.append((address, 0.001, "btc"))

print(key.send(outputs))
