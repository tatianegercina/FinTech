# Integrating a frontend with your CryptoRight contract

In this activity, you will take a pre-built frontend that was designed against the same "EIP-333" specification you built your contract against, and combine it with your `CryptoRight` contract to create a full-fledged dApp!

## Instructions

* Create a new directory called `cryptoright-frontend` and `cd` into it.

* Copy the [dapp.js](Resources/cryptoright-frontend/dapp.js) file into this directory.

* Copy the [index.html](Resources/cryptoright-frontend/index.html) file into this directory.

* Create a new empty file called `CryptoRight.json`. This will contain your contract's ABI.

* Run the following command to serve the directory via HTTP:

  ```python
  python -m http.server 8000
  ```

* Navigate to Remix, and copy your deployed contract's address. You can deploy a fresh contract in this step to generate a new contract address to use.

* Open the `dapp.js` file, and modify the `contract_address` variable at the top of the file to match your deployed contract address. This is the only thing you need to change in this file, no need to worry about any other JavaScript.

* Back in Remix, navigate to the `Compile` tab and copy the contract's ABI. Paste this into `CryptoRight.json`.

  * This dApp expects the `CryptoRight.json` ABI file to be in the same directory as `index.html` and `dapp.js`. Ensure that the file is named properly and that it contains only the contract's ABI.

* Navigate to [localhost:8000](localhost:8000) in your web browser.

* Fill in the form accordingly, creating some copyrights. You will need your API keys for Pinata located at your [Pinata Account Page](https://pinata.cloud/account).

  ![CryptoRight Submit](Images/cryptoright-submit.gif)

## Challenge

* If time remains, try to create some open source materials!

* Switch networks to Kovan or Ropsten, and deploy the contract. Then, update the contract's address in `dapp.js` and try to interact with the dApp when deployed on a testnet.
