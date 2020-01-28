# IPFS + Blockchain

In this activity, you will upload a Car TokenURI file to IPFS via Pinata and link it to a transaction via your ERC721 contract.

## Instructions

* Open the [example token uri file](Unsolved/example_uri.json) and fill out the corresponding `description` fields for the `make`, `model`, and `year` of the car token that you are planning to mint.

```solidity
{
  "make": "Tesla",
  "model": "3",
  "year": 2020
}
```

* Now open your web browser to the [pinata website](https://pinata.cloud) and register for a new account.

![Pinata Signup](Images/pinata_singup.png)

* After you have successfully registered your pinata account; navigate to your email inbox and click the `account activation link`.

![Pinata email verification](Images/pinata_confirm_account.png)

* Now click the `Pinata Upload` page and upload your customized car token URI.

![Pinata Upload Link](Images/pinata_upload_link.png)

* After your file has successfully uploaded, navigate to the `Pinata explorer` page.

![Pinata explorer](Images/pinata_pin_explorer_link.png)

* Confirm that your file was successfully uploaded to IPFS by clicking the link to it's corresponding `IPFS hash`.

  * By default, pinata generates a connection to the IPFS network through their free IPFS gateway, however, we will be using a direct `ipfs://` link to the hash that will be resolved through the IPFS browser extension.

* Navigate to the [IPFS Browser Companion github](https://github.com/ipfs-shipyard/ipfs-companion) and install the browser extension for your desired browser.

  ![IPFS Install Links](Images/ipfs-browser-companion.png)

* Originally the CIDv0 standard allowed for url hashes that supported both upper and lowercase characters but this breaks in many browers, including Firefox.

  * Pinata is a useful service but they have yet to update their file pinning frontend to support CIDv1. In order to avoid bugs you are going to convert your `IPFS hash` with a free CIDv1 converter at the [CID IPFS Website](https://cid.ipfs.io).

  ![CID Converter](Images/cid-converter.png)

 * Now to test the browser extension copy the files new CIDv1 `IPFS hash` and preppend `ipfs://` to the front of it, eg, [ipfs://bafybeig4kuemgvy57tczysgckwhc76r6uibrrtrkwzrcvlrvsjfmptiblq](ipfs://bafybeig4kuemgvy57tczysgckwhc76r6uibrrtrkwzrcvlrvsjfmptiblq). Your file should successfully render in your browser.

* Now deploy your CryptoFax contract onto your local ganache blockchain using remix.

* You may have to increase the `Gas Limit`, but once the contract has successfully deployed, click on the deployed contract and then click the `registerVehicle` function. Fill in the fields with a generated address from your wallet, the vin of the car, and the token URI; then call the function. The data you enter should look something like this:

* owner : `0xc3879B456DAA348a16B6524CBC558d2CC984722c`

* vin: `1HTMMAAL65H124192`

* token_uri: `ipfs://bafybeig4kuemgvy57tczysgckwhc76r6uibrrtrkwzrcvlrvsjfmptiblq`

## Challenge

* If time remains, try to upload multiple token URI files to pinata and then use the various token URI's to mint new unique car tokens.

## Hints

* You can read more about how `IPFS` works and the concepts behind it on  the [IPFS website](https://ipfs.io/#how)
