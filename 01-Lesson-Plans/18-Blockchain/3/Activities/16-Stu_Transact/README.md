# Transacting on your chain

In this activity, you will be connecting MyCrypto to your custom chain, importing your prefunded wallet,
then sending a test transaction to yourself!

## Instructions

* Open up MyCrypto, then click `Change Network` at the bottom left:

![change network](Images/change-network.png)

* Click `Add Custom Node`, then add the custom network information that you set in the genesis.
  Ensure that you scroll down to choose `Custom` in the `Network` column to reveal more options like `Chain ID`:

![custom network](Images/custom-network.png)

* The chain ID must match what you came up with earlier.

* The URL is pointing to the default RPC port on your local machine. Use `http://127.0.0.1:8545`.

* Once you save and use the network, double check that it is selected and is connected.

* Import the account that you pre-funded during genesis creation. This will vary based on the method used to generate, but will likely be a mnemonic, private key, or keystore file.

![prefunded account](Images/prefunded-account.png)

Looks like you're filthy rich! This is the balance that was prefunded for this account in the genesis configuration.

* Copy your address into the `To Address` field, then fill in an arbitrary amount of ETH:

![transaction send](Images/transaction-send.png)

* Confirm the transaction by clicking `Send` on the next prompt.

* Click the `Check TX Status` when the green message pops up, confirm the logout:

![check tx](Images/check-tx-status.png)

You should see the transaction go from `Pending` to `Successful` in around the same blocktime you set in the genesis.

* Click the `Check TX Status` button to update the status.

![successful transaction](Images/transaction-status.png)

Congratulations! That was the first transaction send on this blockchain network!
