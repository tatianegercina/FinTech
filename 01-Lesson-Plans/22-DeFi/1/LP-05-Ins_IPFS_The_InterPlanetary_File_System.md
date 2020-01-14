### 5. Instructor Do: IPFS: The InterPlanetary File System (15 min)

In this activity, students are introduced to the `IPFS` technology and how it can be used to store immutable, hash-based content-routed data. Students will see first hand that when combined with blockchain, IPFS is able to store large datasets with the same degree of integrity as on-chain data.

**Files:**

* [Example URI file](Activities/05_Ins_IPFS_The_InterPlanetary_File_System/Solved/example_uri.json)

Begin by giving the students some background on IPFS, what it is, how it works.

* So what is IPFS?

* IPFS stands for `InterPlanetary Filesystem`, it is both:

  * a `Protocol`

  * a `Network`

  * and a `Filesystem`

* So what exactly does this mean and how does it all fit together?

* For two users to exchange data with one another across the internet, they need a common set of rules for how the information is sent between them; this is a `communication protocol`.

* `Communication protocols` are usually built within a stack known as a `protocol suite`. For example, the `internet protocol suite` is widely used today, and of the protocols that make up the suite `Hyper Text Transfer Protocol` or `HTTP` is the foundation for communication.

* Another important piece is known as the `system's architecure` or how the actual computers within the network are able to communicate with one another. Traditionally this is done in a `client-server` model, however, IPFS leverages a `peer-to-peer` network model of connection.

* In a typical `client-server` model, `centralized` servers store data that is accessed via `location-based addressing`. This provides an easy way to secure and manage data in a scalable manner, though it doesn't come without its drawbacks.

  * Since data is stored on `centralized` servers, anyone with access to those servers; whether an authorized admin or a hacker with malicious intent, can alter and remove data. This poses problems in both the realms of privacy and security because in this model control of the server is equal to control of the data.

  * In `location-based addressing`; a piece of data is recognized by location as opposed to its content; this means that to access a piece of data you must go to its specific location even if the same data is available from a closer source.

  * This also means a client has no defacto way to tell if the data it has received has been altered because the client isn't concerned with what the data is but rather where it is.

  * The `client-server` model works well for websites and small pieces of data, but it's not the most efficient when it comes to big pieces of data.

* IPFS hopes to address these issues with the traditional `client-server` model with the use of a distributed `peer to peer` file-sharing system.

Now that the students have a general grasp on what IPFS is and the purposes that it is trying to serve. Introduce the class to the Pinata service and how `IPFS` can be a valuable tool for building dApps and decentralized systems.

Open a web browser and navigate to the [Pinata Website](https://pinata.cloud/).

![Pinata](Images/pinata.png)

* Pinata is a file pinning service for IPFS. It allows you to host files on the IPFS network and reference them by hash; they also provide a free gateway for communicating with IPFS.

Click the `Try it for Free` or the `Signup` and register for a free account. If you already have an account login to the pinata dashboard.

![Pinata Signup](Images/pinata_singup.png)

![Pinata Login](Images/pinata_login.png)

* Pinata accounts are free and allow you to pin up to `1 gigabyte` of files on IPFS.

* The pinata website provides a simple user interface for developers to upload and access files on IPFS.

Open the [Example URI file](Activities/05_Ins_IPFS_The_InterPlanetary_File_System/Solved/example_uri.json) and display it to the class.

```json
{
  "title": "Artwork Metadata",
  "type": "object",
  "properties": {
      "type_of_art": {
          "type": "string",
          "description": "Painting"
      },
      "year_created": {
          "type": "uint",
          "description": "1503"
      }
  }
}
```

* As previously mentioned, each `ERC721` token typically has an associated `token URI` that is stored on some off-chain storage provider such as IPFS. A URI may resolve to any file, but an ERC721 token URI usually looks something like this.

Click on the `Pinata Upload` link in the website's top navigation bar.

![Pinata Upload Link](Images/pinata_upload_link.png)

Now click the `Browse` button and upload the [Example URI file](Activities/05_Ins_IPFS_The_InterPlanetary_File_System/Solved/example_uri.json)

![Pinata Upload](Images/pinata_upload.png)

* Let's upload the example `token URI` to IPFS for an Artwork Token.

* Uploading a file on Pinata is as simple as clicking `Browse` and then clicking `Upload`.

After the upload is successful, click the `Pin Explorer` link in the website's top navigation bar.

![Pin Explorer Link](Images/pinata_pin_explorer_link.png)

* Let's take a look at the file we uploaded by going to the `Pinata Explorer` page.

![Pinata Explorer](Images/pinata_pin_explorer.png)

* As you can see, our Artwork Token's json file shows up in our list of pinned files; make note of the corresponding IPFS hash.

![Pin Hash Click](Images/pinata_pin_hash.png)

* If we click the hash link, pinata will even generate a link to the file on IPFS accessible through pinata's free IPFS gateway.

Make a note to the class that the pinata gateway is a point of centralization, but that dApps can leverage the use of multiple IPFS gateways to mitigate this.

![Gateway File](Images/pinata_gateway_file.png)

  * By default, pinata generates a connection to the IPFS network through their free IPFS gateway, however, we will be using a direct `ipfs://` link to the hash that will be resolved through the IPFS browser extension.

* Navigate to the [IPFS Browser Companion github](https://github.com/ipfs-shipyard/ipfs-companion) and install the browser extension for your desired browser.

  ![IPFS Install Links](../../Images/ipfs-browser-companion.png)

In your browser open the [CID IPFS Website](https://cid.ipfs.io) and convert the CIDV0 hash to a CIDV1 hash.

![CID Converter](../../Images/cid-converter.png)

* Originally the CIDV0 standard allowed for url hashes that supported both upper and lowercase characters but this breaks in many browsers.

  * Pinata is a useful service but they have yet to update their file pinning frontend to support CIDV1. In order to avoid bugs we are going to convert the `IPFS hash` with a free CIDV1 converter.

Now to test the browser extension copy the files new CIDv1 `IPFS hash` and prepend `ipfs://` to the front of it, eg, [ipfs://bafybeig4kuemgvy57tczysgckwhc76r6uibrrtrkwzrcvlrvsjfmptiblq](ipfs://bafybeig4kuemgvy57tczysgckwhc76r6uibrrtrkwzrcvlrvsjfmptiblq). Demonstrate creating the link and opening it in your browser.

* Once the IPFS browser extension is installed files on IPFS can be accessed at `ipfs://whatever your file hash is`.

Now navigate to [Remix](http://remix.ethereum.org/). Then open the example contract for the `Artwork Token` and compile/deploy the contract on your local ganache blockchain.

You may have to increase the `Gas Limit`, but once the contract has successfully deployed, click on the deployed contract and click the `newAppraisal` function. Fill in the fields with a generated address from your wallet, some sample details about the artwork, and the token URI; then call the function. The data you enter should look something like this:

* owner : `0xc3879B456DAA348a16B6524CBC558d2CC984722c`

* name: `Mona Lisa`

* artist: ` Leonardo da Vinci`

* initial_value: `62,000,000`

* token_uri: `https://gateway.pinata.cloud/ipfs/QmX2F3KFJzELLkn7Qadkq19tF62wQzAKDToTwhzNqWLpJ4`

Congratulate them, that was a lot of new information to take in; then briefly introduce the next activity.

* We've now deployed our ERC721 non-fungible token with a linked IPFS `token URI`. In the next activity, you will be uploading a similar token URI file to pinata for your CryptoFax car token.
