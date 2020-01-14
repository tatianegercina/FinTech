# IPFS + Blockchain

In this activity, you will upload a Car TokenURI file to IPFS via Pinata and link it to a transaction via your ERC721 contract.

## Instructions

* Open the [example token uri file](Unsolved/example_uri.json) and fill out the corresponding `description` fields for the `make`, `modl` and `year` of the car token that you are planning to mint.

```solidity
{
  "title": "Vehicle Metadata",
  "type": "object",
  "properties": {
      "make": {
          "type": "string",
          "description": " "
      },
      "model": {
          "type": "string",
          "description": " "
      },
      "year": {
          "type": "uint",
          "description": " "
      }
  }
}
```

* Now open your web browser to the [pianta website](https://pinata.cloud) and register for a new account.

![Pinata Signup](../../Images/pinata_singup.png)

* After you have successfully registered your pinata account; navigate to your email inbox and click the `account activation link`.

![Pinata email verification](../../Images/pinata_confirm_account.png)

* Now click the `Pinata Upload` page and upload your customized car token uri.

![Pinata Upload Link](../../Images/pinata_upload_link.png)

* After your file has successfully uploaded, navigate to the `Pinata explorer` page and click and copy the link to the token uri file.

![Pinata explorer](../../Images/pinata_pin_explorer_link.png)

* Deploy your CryptoFax contract onto your local ganche blochcain using remix.

* You may have to increase the `Gas Limit`, but once the contract has successfully deployed, click on the deployed contract and then click the `registerVehicle` function. Fill in the fields with a generated address from your wallet, the vin of the car, and the token URI; then call the function. The data you enter should look something like this:

* owner : `0xc3879B456DAA348a16B6524CBC558d2CC984722c`

* vin: `1HTMMAAL65H124192`

* token_uri: `https://gateway.pinata.cloud/ipfs/QmdAjcCixaefMxUkSjUQbuMoEc4hvoHNktagevNozHz6KD`

## Challenge

* If time remains, try to upload multiple token URI files to pinata and then use the various token URI's to mint new unique car tokens.

## Hints

* You can read more about how `IPFS` works and the concepts behind it on  the [IPFS wwebsite](https://ipfs.io/#how)
