### 15. Instructor Do: Transacting on the chain (10 min)

Now it's time to connect MyCrypto to the chain and send a transaction.

Open up MyCrypto, then click `Change Network` at the bottom left:

![change network](Images/change-network.png)

Click `Add Custom Node`, then add the custom network information that was set in the genesis.
Ensure that you scroll down to choose `Custom` in the `Network` column to reveal more options like `Chain ID`:

![custom network](Images/custom-network.png)

* Explain that the currency is still denominated by ETH since we never changed that.

* The chain ID must match what you came up with earlier.

* The URL is pointing to the default RPC port on your local machine. Everyone should use this same URL.

Once you save and use the network, double check that it is selected and is connected.

Import the account that you pre-funded during genesis creation. This will vary based on the method used to generate,
but will likely be a mnemonic, private key, or keystore file.

![prefunded account](Images/prefunded-account.png)

* Looks like we're filthy rich! This is the balance that was prefunded for this account in the genesis configuration.

* We're going to send a transaction to ourselves to test it out.

First, copy the address into the `To Address` field, then fill in an arbitrary amount of ETH:

![transaction send](Images/transaction-send.png)

Confirm the transaction by clicking `Send` on the next prompt.

Click the `Check TX Status` when the green message pops up, confirm the logout:

![check tx](Images/check-tx-status.png)

You should see the transaction go from `Pending` to `Successful` in around the same blocktime you set in the genesis.

You can click the `Check TX Status` button to update the status.

![successful transaction](Images/transaction-status.png)

Congratulations, that was the first transaction send on this blockchain network!
Now it's time for the students to do the same.
